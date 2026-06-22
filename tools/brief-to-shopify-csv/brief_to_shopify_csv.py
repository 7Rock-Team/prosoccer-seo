#!/usr/bin/env python3
"""
brief_to_shopify_csv.py
=======================

Converts ProSoccer SEO workforce brief files (.md) into a Shopify-importable CSV
by modifying ONLY a small set of target columns on an exported Shopify product
CSV and passing every other column through verbatim.

This tool is built per ProSoccer_Brief-to-Shopify-CSV_Build-Spec.docx.

DESIGN DECISIONS (approved by Mike, 2026-06-22)
-----------------------------------------------
- Python standard library ONLY. No third-party dependencies.
  Rationale: this script must never modify a non-target column. The stdlib `csv`
  module gives exact RFC-4180 round-trip fidelity, and a small hand-rolled
  markdown->HTML converter (covering the fixed subset the spec defines) produces
  deterministic output we can pin with golden-file tests. A general markdown
  library would introduce smart quotes, its own escaping, <br> insertion, and
  version drift that we would have to fight forever.

- The markdown->HTML converter is locked by byte-for-byte golden tests in
  tests/golden/. Those tests MUST pass before any dry-run or write run.

SAFETY MODEL (spec section 8)
-----------------------------
The script touches exactly 5 fields and nothing else:
  1. Body (HTML)                         (parent row only)
  2. SEO Title                           (parent row only)
  3. SEO Description                     (parent row only)
  4. Short Description metafield         (parent row only)
  5. Image Alt Text                      (per-row, CONDITIONAL)

Never touched, ever: Title, Tags, all other metafields, variants, pricing,
regional columns, Google Shopping columns, row order, column order, headers.

This file is import-safe: running its functions requires no side effects until
main() is invoked.
"""

import re

# ---------------------------------------------------------------------------
# Target column headers (exact strings as they appear in the Shopify export).
# ---------------------------------------------------------------------------
COL_HANDLE = "Handle"
COL_TITLE = "Title"
COL_TAGS = "Tags"
COL_BODY = "Body (HTML)"
COL_SEO_TITLE = "SEO Title"
COL_SEO_DESC = "SEO Description"
COL_SHORT_DESC = "Short Description (product.metafields.products.new_short_description)"
COL_VARIANT_SKU = "Variant SKU"
COL_IMAGE_POSITION = "Image Position"
COL_IMAGE_ALT = "Image Alt Text"

# The 5 columns this script is permitted to write. Everything else is verbatim.
TARGET_COLUMNS = [
    COL_BODY,
    COL_SEO_TITLE,
    COL_SEO_DESC,
    COL_SHORT_DESC,
    COL_IMAGE_ALT,
]

# ===========================================================================
# MARKDOWN -> HTML CONVERTER  (spec section 5)
# ===========================================================================
# This converter implements ONLY the fixed subset the spec defines:
#   ## text          -> <h2>text</h2>
#   ### text         -> <h3>text</h3>
#   - item (run)     -> <ul>\n<li>item</li>...\n</ul>
#   prose paragraph  -> <p>prose</p>
#   [anchor](url)    -> <a href="url">anchor</a>   (no title= attribute, ever)
#   blank line       -> block separator
# Blocks are joined by a single newline. There is NO trailing newline, no <br>,
# no smart-quote conversion, and no HTML entity escaping of body text (the spec
# says preserve special characters verbatim; CSV-layer quoting is handled later
# by the csv module, NOT here).

# A markdown link: [anchor text](url). Anchor has no ']'; url has no ')'.
_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def _convert_links(text):
    """Convert [anchor](url) to <a href="url">anchor</a>. No title= attribute."""
    return _LINK_RE.sub(lambda m: '<a href="%s">%s</a>' % (m.group(2), m.group(1)), text)


def markdown_to_html(md):
    """Convert a markdown body block to a single HTML string (no trailing newline).

    See spec section 5. This is the function pinned by the golden-file tests.
    """
    lines = md.split("\n")
    blocks = []
    para = []  # accumulates consecutive prose lines into one paragraph

    def flush_paragraph():
        if para:
            text = " ".join(s.strip() for s in para).strip()
            if text:
                blocks.append("<p>%s</p>" % _convert_links(text))
            para.clear()

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i].strip()

        if line == "":
            # Blank line closes the current paragraph (block separator).
            flush_paragraph()
            i += 1
            continue

        if line.startswith("### "):
            flush_paragraph()
            blocks.append("<h3>%s</h3>" % _convert_links(line[4:].strip()))
            i += 1
            continue

        if line.startswith("## "):
            flush_paragraph()
            blocks.append("<h2>%s</h2>" % _convert_links(line[3:].strip()))
            i += 1
            continue

        if line.startswith("- "):
            # Consume a contiguous run of bullet lines into one <ul> block.
            flush_paragraph()
            items = []
            while i < n and lines[i].strip().startswith("- "):
                items.append(lines[i].strip()[2:].strip())
                i += 1
            li_html = "\n".join("<li>%s</li>" % _convert_links(it) for it in items)
            blocks.append("<ul>\n%s\n</ul>" % li_html)
            continue

        # Plain prose line: accumulate into the current paragraph.
        para.append(line)
        i += 1

    flush_paragraph()
    return "\n".join(blocks)


def short_description_to_html(md):
    """Wrap short-description prose in <p>...</p> (spec section 3/4).

    Multiple paragraphs (separated by blank lines) join with </p><p>.
    Markdown links are NOT converted here; text is preserved as-is.
    """
    raw_lines = md.split("\n")
    paragraphs = []
    current = []
    for raw in raw_lines:
        line = raw.strip()
        if line == "":
            if current:
                paragraphs.append(" ".join(current))
                current = []
        else:
            current.append(line)
    if current:
        paragraphs.append(" ".join(current))
    if not paragraphs:
        return ""
    return "<p>" + "</p><p>".join(paragraphs) + "</p>"


# ===========================================================================
# BRIEF PARSER  (spec section 4)
# ===========================================================================
# Section identification is by EXACT H3 header prefix (the literal text after
# "### "). We match the prefix, not the full line, because headers carry trailing
# parenthetical notes, e.g. '### Meta Title (Search engine listing)'.
#
# BODY BOUNDARIES (the part that is easy to get wrong):
#   START = the H3 line whose text begins with 'Description (body_html'
#   END   = the next H3 line whose text begins with 'URL Handle'
# Everything BETWEEN those two markers is body content (including the H2 and H3
# headers inside it, e.g. FAQ question subheads). Those interior H3s are NOT
# section delimiters for metadata extraction; we deliberately exclude them.


def _is_h3(line):
    return line.strip().startswith("### ")


def _h3_text(line):
    # Text after the leading '### '.
    return line.strip()[4:].strip()


class BriefParseError(Exception):
    """Raised when a required target field cannot be parsed from a brief."""


def parse_brief(text, filename=""):
    """Parse a brief's raw text into the 5 target fields.

    Returns a dict with keys: body_html, seo_title, seo_description,
    short_description_html, image_alts (list). Raises BriefParseError if any
    required field is missing, naming the field and the brief.
    """
    lines = text.split("\n")

    # --- locate body markers ---
    body_start = None
    for i, ln in enumerate(lines):
        if _is_h3(ln) and _h3_text(ln).startswith("Description (body_html"):
            body_start = i
            break
    body_end = None
    if body_start is not None:
        for i in range(body_start + 1, len(lines)):
            if _is_h3(lines[i]) and _h3_text(lines[i]).startswith("URL Handle"):
                body_end = i
                break

    if body_start is None:
        raise BriefParseError(
            "%s: missing body start marker '### Description (body_html'" % filename
        )
    if body_end is None:
        raise BriefParseError(
            "%s: missing body end marker '### URL Handle'" % filename
        )

    # --- collect TOP-LEVEL H3 delimiters (those outside the body region) ---
    # Interior H3s (FAQ questions, body_start < i < body_end) are skipped so the
    # FAQ subheads never get mistaken for metadata section boundaries.
    delims = []
    for i, ln in enumerate(lines):
        if _is_h3(ln) and not (body_start < i < body_end):
            delims.append(i)
    delims.append(len(lines))  # sentinel so the last section has an end bound

    def section_lines(prefix):
        """Return the raw lines between the H3 matching `prefix` and the next
        top-level delimiter, or None if no such section exists."""
        for j in range(len(delims) - 1):
            di = delims[j]
            if _h3_text(lines[di]).startswith(prefix):
                return lines[di + 1 : delims[j + 1]]
        return None

    def strip_blank_edges(seg):
        seg = list(seg)
        while seg and seg[0].strip() == "":
            seg.pop(0)
        while seg and seg[-1].strip() == "":
            seg.pop()
        return seg

    def single_value(seg):
        """First contiguous run of non-blank lines, joined by spaces, trimmed.
        Used for Meta Title / Meta Description (single-line plain text)."""
        seg = strip_blank_edges(seg)
        out = []
        for ln in seg:
            if ln.strip() == "":
                break
            out.append(ln.strip())
        return " ".join(out).strip()

    # --- body content (markdown -> HTML) ---
    body_seg = strip_blank_edges(lines[body_start + 1 : body_end])
    body_html = markdown_to_html("\n".join(body_seg))

    # --- short description metafield (prose -> <p>...</p>) ---
    short_seg = section_lines("Short Description")
    short_html = (
        short_description_to_html("\n".join(strip_blank_edges(short_seg)))
        if short_seg is not None
        else None
    )

    # --- meta title -> SEO Title ---
    mt_seg = section_lines("Meta Title")
    seo_title = single_value(mt_seg) if mt_seg is not None else None

    # --- meta description -> SEO Description ---
    md_seg = section_lines("Meta Description")
    seo_desc = single_value(md_seg) if md_seg is not None else None

    # --- image alt text bullets ---
    alt_seg = section_lines("Image Alt Text")
    image_alts = None
    if alt_seg is not None:
        image_alts = [
            ln.strip()[2:].strip()
            for ln in alt_seg
            if ln.strip().startswith("- ")
        ]

    # --- required-field validation (fail loudly, name the field) ---
    missing = []
    if not body_html:
        missing.append("Body (HTML)")
    if not short_html:
        missing.append("Short Description metafield")
    if not seo_title:
        missing.append("SEO Title (Meta Title)")
    if not seo_desc:
        missing.append("SEO Description (Meta Description)")
    if image_alts is None or len(image_alts) == 0:
        missing.append("Image Alt Text")
    if missing:
        raise BriefParseError(
            "%s: missing/empty target field(s): %s" % (filename, ", ".join(missing))
        )

    return {
        "body_html": body_html,
        "seo_title": seo_title,
        "seo_description": seo_desc,
        "short_description_html": short_html,
        "image_alts": image_alts,
    }


def sku_from_filename(name):
    """Brief filename pattern: <SKU>_<slug>_brief.md  ->  SKU is before first '_'."""
    base = name.replace("\\", "/").split("/")[-1]
    return base.split("_", 1)[0]


# ===========================================================================
# CSV LOADING + COLUMN RESOLUTION  (spec section 6)
# ===========================================================================
import argparse
import csv
import glob
import os
import sys


def load_export(path):
    """Read the Shopify export CSV. Returns (header, data_rows).

    Uses utf-8-sig so a leading BOM (common in Shopify 'CSV for Excel' exports)
    does not contaminate the first header name. Round-trip fidelity for write
    mode is handled separately when write mode is added.
    """
    with open(path, "r", newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    if not rows:
        raise ValueError("export CSV is empty: %s" % path)
    return rows[0], rows[1:]


def resolve_columns(header):
    """Map each required column name to its single index. Fails loudly if a
    required column is missing or duplicated (positional safety depends on this)."""
    idx = {}
    for name in [
        COL_HANDLE, COL_TITLE, COL_TAGS, COL_BODY, COL_SEO_TITLE, COL_SEO_DESC,
        COL_SHORT_DESC, COL_VARIANT_SKU, COL_IMAGE_POSITION, COL_IMAGE_ALT,
    ]:
        hits = [i for i, h in enumerate(header) if h.strip() == name]
        if len(hits) != 1:
            raise ValueError(
                "column %r resolved to %d matches (expected exactly 1)" % (name, len(hits))
            )
        idx[name] = hits[0]
    return idx


# ===========================================================================
# BRIEF -> PRODUCT MATCHING  (spec section 7)
# ===========================================================================
# Match a brief to a product by SKU PREFIX: the brief filename's SKU (e.g.
# HQ2254) is a prefix of the export's size-suffixed Variant SKUs (HQ2254-M 4).
# Defensive per spec open-item #3: if a brief maps to >1 distinct Handle, warn
# and skip rather than guess.


def find_handle_for_sku(data, idx, sku):
    """Return (handle, parent_row_index, [all_row_indices]) or (None, None, [])
    if unmatched. Raises MultiMatchError if the SKU prefix hits >1 Handle."""
    handle_col = idx[COL_HANDLE]
    sku_col = idx[COL_VARIANT_SKU]
    matched_handles = []
    for row in data:
        cell = row[sku_col].strip()
        if cell and cell.startswith(sku):
            h = row[handle_col]
            if h and h not in matched_handles:
                matched_handles.append(h)
    if not matched_handles:
        return None, None, []
    if len(matched_handles) > 1:
        raise MultiMatchError(sku, matched_handles)
    handle = matched_handles[0]
    row_indices = [i for i, r in enumerate(data) if r[handle_col] == handle]
    parent_idx = row_indices[0]
    return handle, parent_idx, row_indices


class MultiMatchError(Exception):
    def __init__(self, sku, handles):
        self.sku = sku
        self.handles = handles
        super().__init__("SKU %r matched multiple handles: %s" % (sku, handles))


# ===========================================================================
# OUTPUT CONSTRUCTION  (spec section 6 update logic)
# ===========================================================================


def build_output(data, idx, applied):
    """Build the output rows by applying each brief to its product.

    `applied` is a list of dicts: {sku, handle, parent_idx, row_indices, fields}.
    Returns (out_rows, change_log) where change_log records every cell change for
    reporting. out_rows is a deep copy of data with ONLY target cells modified.
    """
    out = [list(r) for r in data]
    log = []  # list of dicts describing each change

    bcol = idx[COL_BODY]
    stcol = idx[COL_SEO_TITLE]
    sdcol = idx[COL_SEO_DESC]
    smcol = idx[COL_SHORT_DESC]
    altcol = idx[COL_IMAGE_ALT]
    poscol = idx[COL_IMAGE_POSITION]

    for a in applied:
        p = a["parent_idx"]
        f = a["fields"]

        # --- product-level fields: PARENT ROW ONLY ---
        for col, key, label in [
            (bcol, "body_html", "Body (HTML)"),
            (stcol, "seo_title", "SEO Title"),
            (sdcol, "seo_description", "SEO Description"),
            (smcol, "short_description_html", "Short Description metafield"),
        ]:
            old = out[p][col]
            new = f[key]
            out[p][col] = new
            log.append({
                "sku": a["sku"], "handle": a["handle"], "row": p,
                "field": label, "old": old, "new": new,
                "changed": old != new,
            })

        # --- Image Alt Text: per-row CONDITIONAL ---
        # WHY this rule: ProSoccer's team owns alt text. We only FILL EMPTY slots
        # that correspond to an actual gallery image (a row with an Image Position).
        # If a cell already has any value, we preserve it verbatim. If a row has no
        # Image Position, it is not a gallery-image row, so we never touch it.
        alts = f["image_alts"]
        for ri in a["row_indices"]:
            pos_raw = out[ri][poscol].strip()
            cur_alt = out[ri][altcol]
            if pos_raw == "":
                continue  # not a gallery-image row
            if cur_alt.strip() != "":
                continue  # already has alt text -> preserve verbatim
            try:
                pos = int(pos_raw)
            except ValueError:
                continue  # non-numeric position -> skip defensively
            if 1 <= pos <= len(alts):
                new_alt = alts[pos - 1]
                out[ri][altcol] = new_alt
                log.append({
                    "sku": a["sku"], "handle": a["handle"], "row": ri,
                    "field": "Image Alt Text (pos %d)" % pos,
                    "old": cur_alt, "new": new_alt, "changed": True,
                })
            # brief has fewer alts than images -> leave the cell as-is (empty)

    return out, log


# ===========================================================================
# VALIDATION  (spec section 8 hard checks)
# ===========================================================================


def validate_output(header_in, header_out, data, out, idx):
    """Run the three §8 integrity checks. Returns list of (name, passed, detail)."""
    checks = []

    # 1. Column header integrity.
    checks.append((
        "Column header integrity (headers byte-identical, same order)",
        header_in == header_out,
        "in=%d cols, out=%d cols" % (len(header_in), len(header_out)),
    ))

    # 2. Row count integrity.
    checks.append((
        "Row count integrity (no rows added/removed/reordered)",
        len(data) == len(out),
        "in=%d rows, out=%d rows" % (len(data), len(out)),
    ))

    # 3. Non-target columns: zero changes anywhere.
    target_idx = {idx[c] for c in TARGET_COLUMNS}
    diffs = []
    ncols = len(header_in)
    for r in range(min(len(data), len(out))):
        for c in range(ncols):
            if c in target_idx:
                continue
            if data[r][c] != out[r][c]:
                diffs.append((r, c, header_in[c]))
    checks.append((
        "Non-target columns unchanged (verbatim pass-through)",
        len(diffs) == 0,
        "0 non-target cell changes" if not diffs
        else "%d non-target cell change(s): %s" % (len(diffs), diffs[:5]),
    ))

    return checks


# ===========================================================================
# CSV DIALECT DETECTION + WRITE  (spec section 6, write-mode fidelity)
# ===========================================================================
import datetime


def detect_dialect(path):
    """Detect the export's line terminator and BOM from its raw bytes.

    The row terminator is taken from the END OF THE HEADER ROW: column names
    never contain embedded newlines, so the first newline byte in the file is
    guaranteed to be a structural row terminator (not a newline inside a quoted
    cell, which DO occur later inside Body (HTML)). This is why we cannot just
    grep the whole file for \\r\\n. Returns (terminator, has_bom).
    """
    with open(path, "rb") as f:
        data = f.read()
    has_bom = data.startswith(b"\xef\xbb\xbf")
    i = data.find(b"\n")
    if i == -1:
        terminator = "\n"  # single-line file; default
    elif i > 0 and data[i - 1:i] == b"\r":
        terminator = "\r\n"
    else:
        terminator = "\n"
    return terminator, has_bom


def write_output(path, header, rows, terminator, has_bom):
    """Write the output CSV with byte-fidelity controls.

    - Encoding: UTF-8, with BOM only if the source had one.
    - Line terminator: exactly the source's (LF or CRLF).
    - Quoting: RFC 4180 QUOTE_MINIMAL with inner double-quotes doubled
      (csv default doublequote=True). Body (HTML) cells contain " in hrefs,
      so they will be wrapped and escaped correctly.
    """
    enc = "utf-8-sig" if has_bom else "utf-8"
    with open(path, "w", newline="", encoding=enc) as f:
        w = csv.writer(f, lineterminator=terminator, quoting=csv.QUOTE_MINIMAL)
        w.writerow(header)
        w.writerows(rows)


def reverify_on_disk(path, header_in, data_in, out_intended, idx):
    """Re-read the just-written file from disk and confirm it matches intent.

    This is defense in depth: we do not trust the in-memory `out`; we read the
    actual bytes back and compare. Returns (checks, ok). Each check is
    (name, passed, detail). The guarantee is VALUE-level (what Shopify imports
    by), which is exactly the spec section 8 definition of "cell that differs".
    """
    with open(path, "r", newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    h2 = rows[0] if rows else []
    d2 = rows[1:]

    checks = []
    checks.append((
        "On-disk header byte-identical to input header",
        h2 == header_in,
        "in=%d cols, on-disk=%d cols" % (len(header_in), len(h2)),
    ))
    checks.append((
        "On-disk row count equals input row count",
        len(d2) == len(data_in),
        "in=%d rows, on-disk=%d rows" % (len(data_in), len(d2)),
    ))
    # On-disk values must equal the intended output, cell for cell.
    mismatches = []
    for r in range(min(len(d2), len(out_intended))):
        if d2[r] != out_intended[r]:
            for c in range(max(len(d2[r]), len(out_intended[r]))):
                a = d2[r][c] if c < len(d2[r]) else "<missing>"
                b = out_intended[r][c] if c < len(out_intended[r]) else "<missing>"
                if a != b:
                    mismatches.append((r, c))
    checks.append((
        "On-disk values equal intended output (round-trip lossless)",
        len(mismatches) == 0,
        "0 mismatches" if not mismatches else "%d mismatch(es): %s" % (len(mismatches), mismatches[:5]),
    ))
    # And, independently, non-target columns on disk must equal the ORIGINAL input.
    target_idx = {idx[c] for c in TARGET_COLUMNS}
    nontarget_diffs = []
    for r in range(min(len(d2), len(data_in))):
        for c in range(len(header_in)):
            if c in target_idx:
                continue
            din = data_in[r][c] if c < len(data_in[r]) else ""
            dout = d2[r][c] if c < len(d2[r]) else ""
            if din != dout:
                nontarget_diffs.append((r, c, header_in[c]))
    checks.append((
        "On-disk non-target columns equal original input (verbatim pass-through)",
        len(nontarget_diffs) == 0,
        "0 non-target changes" if not nontarget_diffs
        else "%d change(s): %s" % (len(nontarget_diffs), nontarget_diffs[:5]),
    ))
    ok = all(c[1] for c in checks)
    return checks, ok


# ===========================================================================
# SHARED PIPELINE CORE  (used by both dry-run and write mode)
# ===========================================================================

def _hr(ch="-", n=78):
    return ch * n


def _q(s):
    return "(empty)" if s == "" else s


def _show_diff(label, old, new):
    state = "CHANGED" if old != new else "unchanged"
    print("  [%s] %s" % (state, label))
    print("    CURRENT  (%d chars): %s" % (len(old), _q(old)))
    print("    PROPOSED (%d chars): %s" % (len(new), _q(new)))


def _truncate(s, n):
    s = s.replace("\n", " ")
    return s if len(s) <= n else s[: n - 1] + "..."


def prepare(briefs_dir, export_path):
    """Run the full read/parse/match/build pipeline WITHOUT printing or writing.

    Returns a result dict. Pre-flight messages are collected into
    result['preflight'] so callers can print them in either mode.
    """
    result = {"preflight": []}

    def note(msg):
        result["preflight"].append(msg)

    # --- gather briefs ---
    pattern = os.path.join(briefs_dir, "*_brief.md")
    brief_paths = sorted(glob.glob(pattern))
    result["brief_paths"] = brief_paths

    # --- load export + resolve columns ---
    header, data = load_export(export_path)
    idx = resolve_columns(header)
    handle_col = idx[COL_HANDLE]
    unique_handles = []
    for r in data:
        if r[handle_col] and r[handle_col] not in unique_handles:
            unique_handles.append(r[handle_col])

    result.update({
        "header": header, "data": data, "idx": idx,
        "unique_handles": unique_handles, "export_path": export_path,
        "briefs_dir": briefs_dir,
    })

    # --- parse + match each brief ---
    applied = []
    skipped = []
    for bp in brief_paths:
        name = os.path.basename(bp)
        sku = sku_from_filename(name)
        with open(bp, "r", encoding="utf-8") as f:
            text = f.read()
        try:
            fields = parse_brief(text, name)
        except BriefParseError as e:
            note("[SKIP] %s -> PARSE FAILED: %s" % (sku, e))
            skipped.append((sku, "parse failed"))
            continue
        try:
            handle, parent_idx, row_indices = find_handle_for_sku(data, idx, sku)
        except MultiMatchError as e:
            note("[SKIP] %s -> matched MULTIPLE handles %s (defensive skip)" % (sku, e.handles))
            skipped.append((sku, "multi-match"))
            continue
        if handle is None:
            note("[SKIP] %s -> NO matching Variant SKU in export" % sku)
            skipped.append((sku, "unmatched"))
            continue
        note("[ OK ] %s -> handle '%s' (parent row %d, %d rows) | 5/5 target fields parsed"
             % (sku, handle, parent_idx, len(row_indices)))
        applied.append({
            "sku": sku, "handle": handle, "parent_idx": parent_idx,
            "row_indices": row_indices, "fields": fields, "brief": name,
        })

    result["applied"] = applied
    result["skipped"] = skipped

    # --- build output in memory ---
    if applied:
        out, log = build_output(data, idx, applied)
    else:
        out, log = [list(r) for r in data], []
    result["out"] = out
    result["log"] = log
    return result


def print_preflight(result):
    print("\n[PRE-FLIGHT] Briefs")
    print("  Briefs directory  : %s" % result["briefs_dir"])
    print("  Brief files found  : %d" % len(result["brief_paths"]))
    for bp in result["brief_paths"]:
        print("    - %s  (SKU %s)" % (os.path.basename(bp), sku_from_filename(os.path.basename(bp))))
    print("\n[PRE-FLIGHT] Export CSV")
    print("  Export file       : %s" % result["export_path"])
    print("  Columns           : %d" % len(result["header"]))
    print("  Data rows         : %d" % len(result["data"]))
    print("  Unique handles    : %d" % len(result["unique_handles"]))
    print("\n[PRE-FLIGHT] Brief parse + SKU match")
    for msg in result["preflight"]:
        print("  " + msg)
    print("\n  Ready to apply : %d brief(s)" % len(result["applied"]))
    print("  Skipped        : %d brief(s)" % len(result["skipped"]))


def print_diffs(result):
    data, idx = result["data"], result["idx"]
    for a in result["applied"]:
        print("\n" + _hr("="))
        print("PRODUCT  SKU %s  |  handle: %s  |  parent row: %d" % (a["sku"], a["handle"], a["parent_idx"]))
        print(_hr("="))
        f = a["fields"]
        p = a["parent_idx"]
        _show_diff("Body (HTML)", data[p][idx[COL_BODY]], f["body_html"])
        _show_diff("SEO Title", data[p][idx[COL_SEO_TITLE]], f["seo_title"])
        _show_diff("SEO Description", data[p][idx[COL_SEO_DESC]], f["seo_description"])
        _show_diff("Short Description metafield", data[p][idx[COL_SHORT_DESC]], f["short_description_html"])

        print("\n  Image Alt Text (conditional: write only if cell empty AND row has Image Position)")
        print("    Brief supplies %d alt entries." % len(f["image_alts"]))
        poscol = idx[COL_IMAGE_POSITION]
        altcol = idx[COL_IMAGE_ALT]
        touched = 0
        for ri in a["row_indices"]:
            pos = data[ri][poscol].strip()
            cur = data[ri][altcol]
            if pos == "":
                continue
            if cur.strip() != "":
                print("    pos %s row %d: PRESERVE (already has alt: %s)" % (pos, ri, _truncate(cur, 50)))
            else:
                try:
                    pi = int(pos)
                except ValueError:
                    pi = -1
                if 1 <= pi <= len(f["image_alts"]):
                    print("    pos %s row %d: WRITE -> %s" % (pos, ri, f["image_alts"][pi - 1]))
                    touched += 1
                else:
                    print("    pos %s row %d: EMPTY but brief has no alt for this position -> leave empty" % (pos, ri))
        print("    => %d Image Alt Text cell(s) would be written." % touched)


def print_validation(result):
    print("\n" + _hr("="))
    print("VALIDATION (spec section 8)")
    print(_hr("="))
    checks = validate_output(result["header"], result["header"], result["data"], result["out"], result["idx"])
    all_pass = True
    for name, passed, detail in checks:
        all_pass = all_pass and passed
        print("  [%s] %s" % ("PASS" if passed else "FAIL", name))
        print("         %s" % detail)
    return all_pass


def print_summary(result, mode, validation_pass):
    log = result["log"]
    total_changes = sum(1 for c in log if c["changed"])
    per_row = {c["row"] for c in log if c["changed"]}
    print("\n" + _hr("="))
    print("SUMMARY")
    print(_hr("="))
    print("  Briefs applied        : %d" % len(result["applied"]))
    print("  Briefs skipped        : %d" % len(result["skipped"]))
    print("  Total cells modified  : %d" % total_changes)
    print("  Rows touched          : %d" % len(per_row))
    print("  Validation            : %s" % ("ALL PASS" if validation_pass else "FAIL"))


# ===========================================================================
# DRY-RUN MODE
# ===========================================================================

def run_dry_run(briefs_dir, export_path):
    print(_hr("="))
    print("BRIEF -> SHOPIFY CSV  |  DRY-RUN (no file will be written)")
    print(_hr("="))
    result = prepare(briefs_dir, export_path)
    print_preflight(result)
    if not result["brief_paths"]:
        print("\n  No *_brief.md files found. Nothing to do.")
        return 0
    if not result["applied"]:
        print("\nNothing to apply. Exiting dry-run.")
        return 0
    print_diffs(result)
    ok = print_validation(result)
    print_summary(result, "dry-run", ok)
    print("\n  DRY-RUN complete. No file written.")
    return 0


# ===========================================================================
# WRITE MODE
# ===========================================================================

def _timestamp_name(batch):
    ts = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
    label = (batch or "batch").strip().replace(" ", "-")
    return "brief_to_shopify_%s_%s.csv" % (label, ts)


def _write_transaction_log(log_path, result, output_path, predisk_pass, ondisk_checks, ondisk_ok):
    lines = []
    lines.append("ProSoccer brief-to-Shopify CSV : TRANSACTION LOG")
    lines.append("Generated      : %s" % datetime.datetime.now().isoformat(timespec="seconds"))
    lines.append("Export (input) : %s" % result["export_path"])
    lines.append("Briefs dir     : %s" % result["briefs_dir"])
    lines.append("Output (CSV)   : %s" % output_path)
    lines.append("")
    lines.append("Briefs applied : %d" % len(result["applied"]))
    for a in result["applied"]:
        changed = [c for c in result["log"] if c["sku"] == a["sku"] and c["changed"]]
        lines.append("  - SKU %s -> handle '%s' (parent row %d): %d cell(s) changed"
                     % (a["sku"], a["handle"], a["parent_idx"], len(changed)))
        for c in changed:
            lines.append("      * row %d  %-28s  %d -> %d chars"
                         % (c["row"], c["field"], len(c["old"]), len(c["new"])))
    if result["skipped"]:
        lines.append("")
        lines.append("Briefs skipped : %d" % len(result["skipped"]))
        for sku, reason in result["skipped"]:
            lines.append("  - SKU %s : %s" % (sku, reason))
    lines.append("")
    lines.append("Pre-write validation (in-memory) : %s" % ("ALL PASS" if predisk_pass else "FAIL"))
    lines.append("Post-write validation (on-disk re-read):")
    for name, passed, detail in ondisk_checks:
        lines.append("  [%s] %s -- %s" % ("PASS" if passed else "FAIL", name, detail))
    lines.append("Result : %s" % ("SUCCESS" if (predisk_pass and ondisk_ok) else "ABORTED/FAILED"))
    with open(log_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def run_write(briefs_dir, export_path, output_path, batch, assume_yes):
    print(_hr("="))
    print("BRIEF -> SHOPIFY CSV  |  WRITE MODE")
    print(_hr("="))
    result = prepare(briefs_dir, export_path)
    print_preflight(result)
    if not result["applied"]:
        print("\nNothing to apply. No file written.")
        return 0
    print_diffs(result)
    predisk_pass = print_validation(result)
    print_summary(result, "write", predisk_pass)

    # HARD GATE: never write if the in-memory validation failed.
    if not predisk_pass:
        print("\nABORT: pre-write validation FAILED. No file written.", file=sys.stderr)
        return 4

    # Resolve output path.
    if not output_path:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        output_path = os.path.join(out_dir, _timestamp_name(batch))
    else:
        parent = os.path.dirname(os.path.abspath(output_path))
        os.makedirs(parent, exist_ok=True)

    # Interactive confirmation (spec section 11 default).
    print("\n" + _hr("="))
    print("CONFIRM WRITE")
    print(_hr("="))
    print("  About to write : %s" % output_path)
    if assume_yes:
        print("  --yes supplied: skipping interactive prompt.")
    else:
        if not sys.stdin.isatty():
            print("  Non-interactive shell and --yes not supplied. Refusing to write.", file=sys.stderr)
            print("  Re-run with --yes to confirm in a non-interactive context.", file=sys.stderr)
            return 5
        resp = input("  Type YES to write the output CSV (anything else aborts): ")
        if resp.strip() != "YES":
            print("  Aborted by user. No file written.")
            return 0

    # Detect dialect and write.
    terminator, has_bom = detect_dialect(export_path)
    print("\n  Writing with: terminator=%s, BOM=%s, quoting=QUOTE_MINIMAL"
          % (repr(terminator), has_bom))
    write_output(output_path, result["header"], result["out"], terminator, has_bom)
    print("  Wrote: %s" % output_path)

    # Post-write re-read verification (defense in depth).
    print("\n" + _hr("="))
    print("POST-WRITE VERIFICATION (re-read from disk)")
    print(_hr("="))
    ondisk_checks, ondisk_ok = reverify_on_disk(
        output_path, result["header"], result["data"], result["out"], result["idx"])
    for name, passed, detail in ondisk_checks:
        print("  [%s] %s" % ("PASS" if passed else "FAIL", name))
        print("         %s" % detail)

    # Transaction log alongside the output CSV.
    log_path = os.path.splitext(output_path)[0] + ".log"
    _write_transaction_log(log_path, result, output_path, predisk_pass, ondisk_checks, ondisk_ok)
    print("\n  Transaction log: %s" % log_path)

    if not ondisk_ok:
        print("\nWARNING: post-write verification FAILED. Do NOT import this file. "
              "Investigate before proceeding.", file=sys.stderr)
        return 6

    print("\n  WRITE complete and verified. Safe to import to Shopify.")
    return 0


# ===========================================================================
# CLI
# ===========================================================================

def build_arg_parser():
    p = argparse.ArgumentParser(
        description="Convert ProSoccer brief files into a Shopify-importable CSV.",
    )
    p.add_argument("--briefs", help="directory containing *_brief.md files")
    p.add_argument("--export", help="path to the exported Shopify product CSV")
    p.add_argument("--output", help="path for the output CSV (write mode). "
                                    "If omitted, auto-named under ./output/.")
    p.add_argument("--batch", help="batch label used in the auto-generated output filename")
    p.add_argument("--dry-run", action="store_true",
                   help="process and report what WOULD change; write nothing")
    p.add_argument("--yes", action="store_true",
                   help="skip the interactive confirmation prompt (for scripted runs)")
    p.add_argument("pos", nargs="*", help="positional: <briefs_dir> <export_csv> [output_csv]")
    return p


def main(argv=None):
    args = build_arg_parser().parse_args(argv)

    briefs = args.briefs
    export = args.export
    output = args.output
    if briefs is None and len(args.pos) >= 1:
        briefs = args.pos[0]
    if export is None and len(args.pos) >= 2:
        export = args.pos[1]
    if output is None and len(args.pos) >= 3:
        output = args.pos[2]

    if not briefs or not export:
        print("ERROR: need --briefs <dir> and --export <csv> (or positional args).", file=sys.stderr)
        return 2

    if args.dry_run:
        return run_dry_run(briefs, export)

    return run_write(briefs, export, output, args.batch, args.yes)


if __name__ == "__main__":
    raise SystemExit(main())
