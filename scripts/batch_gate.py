"""Deterministic batch gate for a page-optimization session's brief files.

Runs every MECHANICAL compliance check in one pass over a session folder and
prints a single PASS / FAILURES report with SKU + line number + which check.
ORIN reads only the failures and reasons only about genuine judgment calls; the
human-in-the-loop gate this replaces used to read every brief and reason about
every dimension by hand (Batches 1 to 6). This script is the safety net that
makes cutting the human gate safe: it provably catches every historical defect
class (see scripts/test_batch_gate.py, built from real past defects).

Usage:
    python scripts/batch_gate.py <session-dir>
    python scripts/batch_gate.py deliverables/page-optimizations/2026-07-08_session-01

Exit codes:
    0  clean: no findings
    1  REVIEW findings only (judgment calls: cross-brief similarity, fabrication
       hedges) -- ORIN reviews, none are hard defects
    2  FAIL findings present (hard mechanical defects) -- ORIN must resolve

Design: EXTENDS scripts/voice_check.py, does not duplicate it. The voice checks
(em-dash / en-dash, forbidden words / phrases / openers, capitalized Adidas, UK
'boots', lowercase editorial body H2 casing, internal-link URL format) run via
voice_check.collect_violations. This file adds only the net-new batch checks:
heading levels, FIFA/WC brand-aware grep, per-SKU forbidden-phrasings (verbatim +
motifs + title-frames), cross-brief lexical similarity, word-count band,
cannibalization, price-in-body, and fabrication-hedge markers.

Single source of truth: the motif and title-frame lists this script checks are
the SAME per-SKU lists ORIN writes into each SKU's input file
(deliverables/<session>/inputs/<SKU>_input.md, in a fenced ```gate-meta JSON
block). ORIN extracts a barred motif once, it lands in the input file, SCRIBE is
told not to use it, and this script enforces it. Three consumers, one list; no
hardcoded motif dictionary that could drift.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
if str(_THIS_DIR) not in sys.path:
    sys.path.insert(0, str(_THIS_DIR))

import voice_check as vc  # noqa: E402  (reuse; do not duplicate the voice checks)


# --------------------------------------------------------------------------- #
# Severity
# --------------------------------------------------------------------------- #
FAIL = "FAIL"        # hard mechanical defect; ORIN must fix
REVIEW = "REVIEW"    # judgment call surfaced for ORIN's eyes; not auto-defect


class Finding:
    """One gate finding, tied to a SKU, a check, and (usually) a line number."""

    __slots__ = ("sku", "check", "severity", "line", "message")

    def __init__(self, sku, check, severity, message, line=None):
        self.sku = sku
        self.check = check
        self.severity = severity
        self.message = message
        self.line = line

    def format(self) -> str:
        loc = f":{self.line}" if self.line is not None else ""
        return f"  [{self.severity}] {self.sku}{loc} ({self.check}): {self.message}"


# --------------------------------------------------------------------------- #
# Brief field / body-region parsing
# --------------------------------------------------------------------------- #
# The brief file uses "### <FieldName>" markers for the copy-paste fields, and the
# Description field's body content nests "## H2" section headers *shallower* than
# its own "### Description" marker (a ProSoccer convention: the ## headers are what
# get pasted into Shopify as real on-page H2s). We therefore delimit the body by
# the KNOWN trailing field markers, not by heading depth.
BODY_START = re.compile(r"^#{2,4}\s+Description\b", re.IGNORECASE)
# First trailing field marker after the Description ends the body region. These are
# the fields the template places after Description in copy-paste order.
BODY_END = re.compile(
    r"^#{2,4}\s+(Meta\s+Title|Meta\s+Description|URL\s+Handle|Image\s+Alt|"
    r"Internal\s+Links?|Taxonomy)\b",
    re.IGNORECASE,
)
# Field-scan markers used to isolate customer-facing prose fields for the FIFA and
# forbidden-phrasing greps (excludes Quick Reference, Keywords, URL Handle, Internal
# Links, Taxonomy -- those carry SKUs, volumes, slugs, and URLs, not customer copy).
FIELD_MARKER = re.compile(r"^#{2,3}\s+(?P<name>[A-Za-z][^\n(]*?)\s*(\(|$)")
PROSE_FIELDS = {
    "title", "short description", "description", "meta title",
    "meta description", "image alt text",
}
NON_PROSE_FIELDS = {
    "quick reference", "keywords", "url handle", "internal links", "internal link",
    "taxonomy category", "seo details",
}

URL_RE = re.compile(r"https?://\S+")


def discover_briefs(session_dir: Path) -> list[Path]:
    """Return the brief .md files in a session folder, sorted, excluding the audit
    trail, differentiation spec, other underscore-prefixed batch files, and anything
    under inputs/."""
    briefs = []
    for p in sorted(session_dir.glob("*.md")):
        if p.name.startswith("_"):
            continue
        briefs.append(p)
    return briefs


def sku_from_brief(path: Path) -> str:
    """SKU is the filename segment before the first underscore (SKUs carry hyphens,
    never underscores: IF8512-001, J000691-CRFT, 7651TX3926, DRCHRM25)."""
    return path.name.split("_", 1)[0]


def body_region(lines: list[str]) -> tuple[int, int]:
    """Return (start_idx, end_idx) 0-based half-open line range of the Description
    body content, or (-1, -1) if the brief has no Description field."""
    start = -1
    for i, ln in enumerate(lines):
        if BODY_START.search(ln):
            start = i + 1  # content begins after the marker line
            break
    if start == -1:
        return -1, -1
    end = len(lines)
    for i in range(start, len(lines)):
        if BODY_END.search(lines[i]):
            end = i
            break
    return start, end


def prose_field_lines(lines: list[str]) -> set[int]:
    """Return the set of 0-based line indices that belong to customer-facing prose
    fields (Title, Short Description, Description body incl. FAQ, Meta Title, Meta
    Description, Image Alt Text). Used to scope the FIFA and forbidden greps so that
    slugs/URLs in the URL Handle and Internal Links fields never false-positive."""
    included: set[int] = set()
    current_included = False
    for i, ln in enumerate(lines):
        m = FIELD_MARKER.match(ln)
        if m:
            name = m.group("name").strip().lower()
            # A shallow "## H2" body header (inside Description) is not a field
            # boundary unless it names a known field; treat unknown headers as
            # continuation of the current field.
            if name in PROSE_FIELDS:
                current_included = True
                included.add(i)
                continue
            if name in NON_PROSE_FIELDS:
                current_included = False
                continue
            # Unknown header (e.g. an editorial body H2 like "## Built for...",
            # or a FAQ "### question"): inherit the current field's inclusion.
        if current_included:
            included.add(i)
    return included


def blanked_prose(lines: list[str], indices: set[int]) -> list[tuple[int, str]]:
    """Return (line_number, cleaned_text) for prose-field lines with URLs and
    backtick content blanked, so FIFA/forbidden greps see only real customer copy."""
    scan = vc.strip_backticks("\n".join(lines)).splitlines()
    out = []
    for i in sorted(indices):
        text = scan[i] if i < len(scan) else lines[i]
        text = URL_RE.sub(" ", text)
        out.append((i + 1, text))
    return out


# --------------------------------------------------------------------------- #
# Input-file (gate-meta) loading -- single source of truth for per-SKU metadata
# --------------------------------------------------------------------------- #
GATE_META_FENCE = re.compile(r"```gate-meta\s*\n(.*?)\n```", re.DOTALL)


def load_input_meta(session_dir: Path, sku: str) -> dict | None:
    """Load the per-SKU gate metadata from deliverables/<session>/inputs/<SKU>_input.md.

    The input file carries a fenced ```gate-meta JSON block (parsed here) plus
    human-readable markdown SCRIBE reads. Returns the parsed dict, or None if the
    input file or its gate-meta block is absent (the caller then honestly reports
    which input-dependent checks it skipped for that SKU -- never a silent skip).
    """
    inputs_dir = session_dir / "inputs"
    candidate = inputs_dir / f"{sku}_input.md"
    if not candidate.exists():
        return None
    text = candidate.read_text(encoding="utf-8")
    m = GATE_META_FENCE.search(text)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError as e:
        return {"_parse_error": str(e)}


def load_registry1_primaries(session_dir: Path) -> list[str] | None:
    """Load claimed Registry 1 (white-label sheet) primaries from
    inputs/_registry1_primaries.txt (one primary per line) if ORIN wrote it at
    pre-dispatch. None if absent (cannibalization then checks intra-batch only)."""
    f = session_dir / "inputs" / "_registry1_primaries.txt"
    if not f.exists():
        return None
    return [
        ln.strip().lower()
        for ln in f.read_text(encoding="utf-8").splitlines()
        if ln.strip() and not ln.strip().startswith("#")
    ]


# --------------------------------------------------------------------------- #
# Check 2: heading levels in the body (## sections, ### FAQ; flag #### / #####)
# --------------------------------------------------------------------------- #
HEADING_TOO_DEEP = re.compile(r"^(#{4,})\s+(\S.*)$")


def check_heading_levels(sku, lines) -> list[Finding]:
    """Body sections must be ## and FAQ questions ###; any #### or deeper is the
    KI0586 / IF8512 defect (body headers one or two levels too deep)."""
    start, end = body_region(lines)
    if start == -1:
        return []
    findings = []
    for i in range(start, end):
        m = HEADING_TOO_DEEP.match(lines[i])
        if m:
            depth = len(m.group(1))
            findings.append(Finding(
                sku, "heading-level", FAIL,
                f"body heading at level {depth} ('{'#' * depth} {m.group(2)[:60]}'); "
                f"body sections must be ## and FAQ questions ###, never #### or deeper",
                line=i + 1,
            ))
    return findings


# --------------------------------------------------------------------------- #
# Check 5: FIFA / World Cup terminology on non-adidas (non-licensed) pages
# --------------------------------------------------------------------------- #
# adidas is the FIFA commercial licensee; adidas pages MAY use the family. Every
# non-adidas brand (Nike, Umbro, Kelme, Puma, Hummel, ...) is forbidden from it.
FIFA_TOKENS = re.compile(
    r"\b(FIFA|World\s+Cup|World\s+Cup\s+20\d\d|WC\s?20\d\d)\b",
    re.IGNORECASE,
)
# Codified permitted historical anchor: naming a nation's past appearance without
# the FIFA/World Cup wordmark is allowed (e.g. "the finals as Zaire", "a semi-final
# run on home soil in 2002"). We only flag the FIFA/World Cup/WC tokens themselves;
# a bare year like "2026" or "1974" is always permitted and never matched here.


def check_fifa_terms(sku, lines, meta) -> list[Finding]:
    """Flag FIFA / World Cup / WC tokens in customer-facing prose on non-adidas
    pages. Brand and posture come from the SKU's input file (single source). If no
    input meta, fall back to a best-effort brand read from the brief title line and
    mark the finding provisional."""
    posture = None
    brand = None
    if meta:
        posture = (meta.get("brand_ip_posture") or "").lower()
        brand = (meta.get("brand") or "").lower()
    # adidas / fifa-permitted pages: the family is licensed, skip the check.
    if posture == "fifa-permitted" or brand == "adidas":
        return []

    prose = blanked_prose(lines, prose_field_lines(lines))
    findings = []
    provisional = meta is None
    for ln, text in prose:
        for m in FIFA_TOKENS.finditer(text):
            note = "" if not provisional else " [provisional: no input file; brand unverified]"
            findings.append(Finding(
                sku, "fifa-terms", FAIL,
                f"FIFA/World Cup term '{m.group(0)}' in body copy on a non-adidas "
                f"(non-licensed) page; use federation / cycle language{note}",
                line=ln,
            ))
    return findings


# --------------------------------------------------------------------------- #
# Checks 6 & 7 helpers: per-SKU forbidden lists (verbatim / motifs / title-frames)
# --------------------------------------------------------------------------- #
def _forbidden_lists(meta) -> tuple[list[str], list[str], list[str]]:
    if not meta:
        return [], [], []
    fp = meta.get("forbidden_phrasings") or {}
    return (
        [s for s in fp.get("verbatim", []) if s],
        [s for s in fp.get("motifs", []) if s],
        [s for s in fp.get("title_frames", []) if s],
    )


def check_forbidden_phrasings(sku, lines, meta) -> list[Finding]:
    """Check 6: a brief must contain NONE of its OWN input file's forbidden phrasings.
    Three literal tiers, one source of truth (the input file):
      - verbatim: exact hooks / H2 titles / closing lines (substring match)
      - motifs:   distinctive payoff tokens like "gone" (word-boundary match)
      - title-frames: distinctive frame fragments like "sees coming" that survive
                  noun-swapping (substring match)
    """
    verbatim, motifs, frames = _forbidden_lists(meta)
    if not (verbatim or motifs or frames):
        return []
    prose = blanked_prose(lines, prose_field_lines(lines))
    findings = []
    for ln, text in prose:
        low = text.lower()
        for s in verbatim:
            if s.lower() in low:
                findings.append(Finding(
                    sku, "forbidden-verbatim", FAIL,
                    f"reuses barred verbatim phrasing '{s}' from its own forbidden list",
                    line=ln,
                ))
        for token in motifs:
            if re.search(r"\b" + re.escape(token) + r"\b", text, re.IGNORECASE):
                findings.append(Finding(
                    sku, "forbidden-motif", FAIL,
                    f"reuses barred motif token '{token}' from its own forbidden list",
                    line=ln,
                ))
        for frame in frames:
            if frame.lower() in low:
                findings.append(Finding(
                    sku, "forbidden-title-frame", FAIL,
                    f"reuses barred title-frame '{frame}' from its own forbidden list",
                    line=ln,
                ))
    return findings


# --------------------------------------------------------------------------- #
# Check 8: word-count band per tier (from input file)
# --------------------------------------------------------------------------- #
_WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9'\-]*")


def body_word_count(lines: list[str]) -> int:
    """Count words in the Description body content: prose, heading text, and bullet
    text, with markdown markers (#, -, |, backticks) and inline-link URLs stripped."""
    start, end = body_region(lines)
    if start == -1:
        return 0
    scan = vc.strip_backticks("\n".join(lines)).splitlines()
    words = 0
    for i in range(start, min(end, len(scan))):
        text = scan[i]
        text = re.sub(r"^\s*#{1,6}\s*", " ", text)   # heading hashes
        text = re.sub(r"^\s*[-*]\s+", " ", text)      # bullet markers
        text = URL_RE.sub(" ", text)                  # inline link targets
        text = text.replace("|", " ")                 # stray table pipes
        words += len(_WORD_RE.findall(text))
    return words


def check_word_band(sku, lines, meta) -> list[Finding]:
    """Flag a body word count outside the SKU's tier band (+ tolerance). The band is
    SKU-specific from the input file, never inherited from the exemplar (the IF8512
    Elite-band-on-a-Pro-SKU defect)."""
    if not meta or not meta.get("word_band"):
        return []
    band = meta["word_band"]
    if not (isinstance(band, list) and len(band) == 2):
        return []
    lo, hi = band
    tol = meta.get("word_band_tolerance", 15)
    count = body_word_count(lines)
    tier = meta.get("tier", "?")
    if count > hi + tol:
        return [Finding(
            sku, "word-band", FAIL,
            f"body is {count} words, over the {tier}-tier band {lo}-{hi} "
            f"(+{tol} tolerance = {hi + tol} ceiling)",
        )]
    if count < lo - tol:
        return [Finding(
            sku, "word-band", FAIL,
            f"body is {count} words, under the {tier}-tier band {lo}-{hi} "
            f"(-{tol} tolerance = {lo - tol} floor)",
        )]
    return []


# --------------------------------------------------------------------------- #
# Check 10: price in body copy (evergreen discipline)
# --------------------------------------------------------------------------- #
PRICE_RE = re.compile(r"\$\s?\d")


def check_price_in_body(sku, lines) -> list[Finding]:
    start, end = body_region(lines)
    if start == -1:
        return []
    scan = vc.strip_backticks("\n".join(lines)).splitlines()
    findings = []
    for i in range(start, min(end, len(scan))):
        if PRICE_RE.search(scan[i]):
            findings.append(Finding(
                sku, "price-in-body", FAIL,
                f"price in body copy ('{scan[i].strip()[:60]}'); prices decay -- use "
                f"tier/positioning language, keep prices in PDP fields and schema",
                line=i + 1,
            ))
    return findings


# --------------------------------------------------------------------------- #
# Check 11: fabrication-hedge markers near specs (weight / dimensions)
# --------------------------------------------------------------------------- #
HEDGE_WORDS = re.compile(r"\b(approximately|around|about|roughly|circa)\b", re.IGNORECASE)
SPEC_UNIT = re.compile(
    r"\d+(?:\.\d+)?\s?(?:oz|g|kg|lbs?|mm|cm|in|inch(?:es)?|grams?)\b|\d+\s?°",
    re.IGNORECASE,
)


def check_fabrication_hedge(sku, lines) -> list[Finding]:
    """REVIEW: a hedge word next to a weight/dimension spec is a fabrication smell
    (a guessed number dressed as approximate). Surfaced for ORIN to check against the
    Phase 0 scrape; not a hard defect on its own. Inspired by IF8512's fabricated
    '6.3 oz (180g)' weight."""
    start, end = body_region(lines)
    if start == -1:
        return []
    scan = vc.strip_backticks("\n".join(lines)).splitlines()
    findings = []
    for i in range(start, min(end, len(scan))):
        text = scan[i]
        for sm in SPEC_UNIT.finditer(text):
            window = text[max(0, sm.start() - 40): sm.end() + 40]
            hedge = HEDGE_WORDS.search(window)
            if hedge:
                findings.append(Finding(
                    sku, "fabrication-hedge", REVIEW,
                    f"hedge word '{hedge.group(0)}' next to spec '{sm.group(0)}' "
                    f"-- verify the value against the Phase 0 scrape (possible guess)",
                    line=i + 1,
                ))
    return findings


# --------------------------------------------------------------------------- #
# Check 9: cannibalization (primary vs Registry 1 + intra-batch)
# --------------------------------------------------------------------------- #
def check_cannibalization(briefs_meta, registry1) -> list[Finding]:
    """Flag any SKU whose primary keyword duplicates another SKU's primary in the
    batch, or collides with an already-claimed Registry 1 primary."""
    findings = []
    seen: dict[str, str] = {}   # primary -> first SKU that claimed it this batch
    for sku, meta in briefs_meta:
        if not meta:
            continue
        primary = (meta.get("primary_keyword") or "").strip().lower()
        if not primary:
            continue
        if primary in seen and seen[primary] != sku:
            findings.append(Finding(
                sku, "cannibalization", FAIL,
                f"primary '{primary}' duplicates {seen[primary]}'s primary in this batch",
            ))
        else:
            seen.setdefault(primary, sku)
        if registry1 is not None and primary in registry1:
            findings.append(Finding(
                sku, "cannibalization", FAIL,
                f"primary '{primary}' is already claimed in Registry 1 (white-label sheet)",
            ))
    return findings


# --------------------------------------------------------------------------- #
# Check 7: cross-brief lexical similarity (motifs, title-frames, openings/closings)
# --------------------------------------------------------------------------- #
STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "for", "of", "to", "in", "on", "at", "by",
    "with", "from", "as", "is", "it", "its", "this", "that", "these", "those", "you",
    "your", "youre", "yours", "we", "our", "they", "their", "them", "he", "she",
    "when", "where", "what", "who", "how", "so", "if", "then", "than", "into", "up",
    "out", "over", "before", "after", "not", "no", "yes", "be", "been", "are", "was",
}


def _tokens(text: str) -> list[str]:
    return [w.lower() for w in _WORD_RE.findall(text)]


def _content_ngrams(text: str, n: int) -> set[tuple]:
    toks = [t for t in _tokens(text) if t not in STOPWORDS and len(t) > 1]
    return {tuple(toks[i:i + n]) for i in range(len(toks) - n + 1)} if len(toks) >= n else set()


def brief_opening(lines: list[str]) -> tuple[int, str]:
    """Return (line_number, text) of the brief's opening: the Short Description field
    content (first non-empty prose line after the '### Short Description' marker)."""
    for i, ln in enumerate(lines):
        m = FIELD_MARKER.match(ln)
        if m and m.group("name").strip().lower() == "short description":
            for j in range(i + 1, len(lines)):
                if lines[j].strip():
                    return j + 1, lines[j].strip()
    return 0, ""


STRUCTURAL_H2 = re.compile(
    r"^#{2,5}\s+(Product\s+Details|Care\s+and\s+Maintenance|Fit\s+Notes|FAQs?\b)",
    re.IGNORECASE,
)


def brief_closing(lines: list[str]) -> tuple[int, str]:
    """Return (line_number, text) of the last EDITORIAL prose line of the body.

    Bounds the search to the editorial region (body start up to the first structural
    H2: Product Details / Care / Fit Notes / FAQ) and skips headings and bullet lines.
    Product Details and Care bullets are legitimately shared across pack siblings, so
    including them would false-positive the cross-brief closing-overlap check; the
    convergence class we care about is the editorial closing SENTENCE (the Shadow
    'gone' closings), not the spec bullets."""
    start, end = body_region(lines)
    if start == -1:
        return 0, ""
    edit_end = end
    for i in range(start, end):
        if STRUCTURAL_H2.search(lines[i]):
            edit_end = i
            break
    for i in range(edit_end - 1, start - 1, -1):
        s = lines[i].strip()
        if s and not s.startswith("#") and not s.startswith("|") \
                and not s.startswith("-") and not s.startswith("*"):
            return i + 1, s
    return 0, ""


def _overlap(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


CROSS_BRIEF_OPENING_THRESHOLD = 0.4
CROSS_BRIEF_CLOSING_THRESHOLD = 0.4


def check_cross_brief(briefs_data) -> list[Finding]:
    """Lexical (deterministic, offline) cross-brief convergence detection:
      (a) shared barred motif token appearing across 2+ briefs
      (b) shared barred title-frame appearing across 2+ briefs
      (c) opening/closing trigram overlap above threshold between any pair
    The motif and title-frame vocabulary is the union of the per-SKU forbidden lists
    from the input files -- the SAME lists check 6 uses -- never a separate hardcoded
    dictionary. Conceptual convergence that lexical matching misses is a genuine
    judgment call left to ORIN, by design.
    briefs_data: list of dicts with sku, lines, meta, opening, closing.
    """
    findings: list[Finding] = []

    # (a) + (b): barred motif / title-frame recurring across siblings.
    motif_owner: dict[str, list[str]] = {}
    frame_owner: dict[str, list[str]] = {}
    for d in briefs_data:
        _, motifs, frames = _forbidden_lists(d["meta"])
        prose_text = " ".join(t for _, t in blanked_prose(d["lines"], prose_field_lines(d["lines"])))
        low = prose_text.lower()
        for token in set(m.lower() for m in motifs):
            if re.search(r"\b" + re.escape(token) + r"\b", low):
                motif_owner.setdefault(token, []).append(d["sku"])
        for frame in set(f.lower() for f in frames):
            if frame in low:
                frame_owner.setdefault(frame, []).append(d["sku"])
    for token, skus in motif_owner.items():
        uniq = sorted(set(skus))
        if len(uniq) >= 2:
            findings.append(Finding(
                ", ".join(uniq), "cross-brief-motif", REVIEW,
                f"shared motif token '{token}' appears across sibling briefs {uniq} "
                f"(convergence class; differentiate or bar per-SKU)",
            ))
    for frame, skus in frame_owner.items():
        uniq = sorted(set(skus))
        if len(uniq) >= 2:
            findings.append(Finding(
                ", ".join(uniq), "cross-brief-title-frame", REVIEW,
                f"shared title-frame '{frame}' appears across sibling briefs {uniq}",
            ))

    # (c): pairwise opening / closing trigram overlap.
    n = len(briefs_data)
    for i in range(n):
        for j in range(i + 1, n):
            a, b = briefs_data[i], briefs_data[j]
            o = _overlap(_content_ngrams(a["opening"][1], 3), _content_ngrams(b["opening"][1], 3))
            if o >= CROSS_BRIEF_OPENING_THRESHOLD:
                findings.append(Finding(
                    f"{a['sku']}, {b['sku']}", "cross-brief-opening", REVIEW,
                    f"opening trigram overlap {o:.0%} between {a['sku']} and {b['sku']} "
                    f"(near-identical openings; differentiate)",
                ))
            c = _overlap(_content_ngrams(a["closing"][1], 3), _content_ngrams(b["closing"][1], 3))
            if c >= CROSS_BRIEF_CLOSING_THRESHOLD:
                findings.append(Finding(
                    f"{a['sku']}, {b['sku']}", "cross-brief-closing", REVIEW,
                    f"closing trigram overlap {c:.0%} between {a['sku']} and {b['sku']} "
                    f"(near-identical closings; differentiate)",
                ))
    return findings


# --------------------------------------------------------------------------- #
# Per-brief driver (voice reuse + all per-brief checks)
# --------------------------------------------------------------------------- #
def gate_brief(sku, path, meta) -> tuple[list[Finding], list[str]]:
    """Run every per-brief check. Returns (findings, skipped_checks)."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    findings: list[Finding] = []
    skipped: list[str] = []

    # Checks 1, 3, 4 (+ boots, link-format): reuse voice_check, do not duplicate.
    for v in vc.collect_violations(text, path):
        if not v.startswith("    "):   # header line names the violation class
            findings.append(Finding(sku, "voice", FAIL, v))
        else:
            # attach the indented context line to the last voice finding
            if findings and findings[-1].check == "voice":
                findings[-1].message += "\n    " + v.strip()

    # Check 2: heading levels.
    findings += check_heading_levels(sku, lines)
    # Check 10: price in body.
    findings += check_price_in_body(sku, lines)
    # Check 11: fabrication hedges (REVIEW).
    findings += check_fabrication_hedge(sku, lines)

    # Input-dependent checks (5, 6, 8). Honest skip reporting when no input meta.
    if meta is None:
        skipped += ["fifa-terms(no-input)", "forbidden-phrasings(no-input)", "word-band(no-input)"]
        # FIFA still runs best-effort/provisional so a missing input can't hide a leak.
        findings += check_fifa_terms(sku, lines, None)
    elif meta.get("_parse_error"):
        findings.append(Finding(
            sku, "input-file", FAIL,
            f"gate-meta JSON is malformed ({meta['_parse_error']}); fix the input file",
        ))
    else:
        findings += check_fifa_terms(sku, lines, meta)
        findings += check_forbidden_phrasings(sku, lines, meta)
        findings += check_word_band(sku, lines, meta)

    return findings, skipped


# --------------------------------------------------------------------------- #
# Orchestration + report
# --------------------------------------------------------------------------- #
def run(session_dir: Path) -> int:
    briefs = discover_briefs(session_dir)
    if not briefs:
        print(f"batch_gate: no brief files found in {session_dir}", file=sys.stderr)
        return 2

    registry1 = load_registry1_primaries(session_dir)
    all_findings: list[Finding] = []
    all_skipped: list[str] = []
    briefs_meta: list[tuple[str, dict | None]] = []
    briefs_data: list[dict] = []

    for path in briefs:
        sku = sku_from_brief(path)
        meta = load_input_meta(session_dir, sku)
        briefs_meta.append((sku, meta))
        findings, skipped = gate_brief(sku, path, meta)
        all_findings += findings
        all_skipped += [f"{sku}: {s}" for s in skipped]
        lines = path.read_text(encoding="utf-8").splitlines()
        briefs_data.append({
            "sku": sku, "lines": lines, "meta": meta,
            "opening": brief_opening(lines), "closing": brief_closing(lines),
        })

    # Cross-brief checks (7, 9).
    all_findings += check_cannibalization(briefs_meta, registry1)
    all_findings += check_cross_brief(briefs_data)

    return report(session_dir, briefs, all_findings, all_skipped, registry1)


def report(session_dir, briefs, findings, skipped, registry1) -> int:
    fails = [f for f in findings if f.severity == FAIL]
    reviews = [f for f in findings if f.severity == REVIEW]

    print(f"BATCH GATE -- {session_dir}")
    print(f"  briefs checked: {len(briefs)}")
    if registry1 is None:
        print("  Registry 1 primaries file absent (inputs/_registry1_primaries.txt); "
              "cannibalization checked intra-batch only")
    print()

    if not findings:
        print("PASS: no findings across all mechanical checks.")
        if skipped:
            print("\nInput-dependent checks skipped (no input file):")
            for s in skipped:
                print(f"  - {s}")
        return 0

    if fails:
        print(f"FAILURES ({len(fails)}) -- ORIN must resolve:")
        for f in sorted(fails, key=lambda x: (x.sku, x.line or 0)):
            print(f.format())
        print()
    if reviews:
        print(f"REVIEW ({len(reviews)}) -- judgment calls for ORIN:")
        for f in sorted(reviews, key=lambda x: (x.sku, x.line or 0)):
            print(f.format())
        print()
    if skipped:
        print("Input-dependent checks skipped (no input file for that SKU):")
        for s in skipped:
            print(f"  - {s}")
        print()

    return 2 if fails else 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deterministic batch gate over a page-optimization session folder.")
    parser.add_argument("session_dir", help="Path to deliverables/page-optimizations/<session>/")
    args = parser.parse_args()
    session_dir = Path(args.session_dir).resolve()
    if not session_dir.is_dir():
        print(f"ERROR: not a directory: {session_dir}", file=sys.stderr)
        return 2
    return run(session_dir)


if __name__ == "__main__":
    sys.exit(main())
