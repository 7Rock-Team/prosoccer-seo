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
heading levels, section presence (required PDP sections present WITH content, incl. at
least one internal link -- unconditional, never input-gated), customization claims
(name/number location = product page not checkout, duration = business days not weeks),
FIFA/WC brand-aware grep,
per-SKU forbidden-phrasings (verbatim + motifs + title-frames), cross-brief lexical
similarity, word-count band, cannibalization, price-in-body, fabrication-hedge markers,
and heritage-honour claims (specific title/trophy counts + "most"/"record" superlatives).

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
    inputs/_registry1_primaries.txt (one primary per line).

    Returns None if the file is absent, empty, or unreadable. **None is now a HARD
    FAIL at the batch level**, not a downgrade to intra-batch-only checking: see
    check_registry1_present(). A check that cannot run is a failure, not a pass.
    """
    f = session_dir / "inputs" / "_registry1_primaries.txt"
    if not f.exists():
        return None
    try:
        raw = f.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    out = [
        ln.strip().lower()
        for ln in raw.splitlines()
        if ln.strip() and not ln.strip().startswith("#")
    ]
    # An empty or comments-only file cannot detect a cross-batch collision either.
    return out or None


def check_registry1_present(registry1) -> list[Finding]:
    """Batch-level hard fail when the cross-batch cannibalization check cannot run.

    Origin, and why this is a FAIL rather than a printed note: the gate printed
    "Registry 1 primaries file absent; cannibalization checked intra-batch only"
    and still exited 0. That false green shipped three times (codification
    candidate 2, Batch 9, logged 2026-07-27; recurred Batch 14; recurred Batch 15,
    where it was caught only because a subagent happened to quote the line back).
    Both catches were luck. Mike's ruling 2026-08-18: absent, missing, empty or
    unreadable all hard fail.
    """
    if registry1 is None:
        return [Finding(
            "BATCH", "registry1-missing", FAIL,
            "inputs/_registry1_primaries.txt is absent, empty or unreadable, so the "
            "CROSS-BATCH cannibalization check could not run. A check that cannot run "
            "is a failure. Write the file at pre-dispatch (one claimed primary per "
            "line, from products-master.csv) and re-run.",
        )]
    return []


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
# Check 5: FIFA / World Cup terminology on non-adidas pages
# --------------------------------------------------------------------------- #
# adidas holds a specific FIFA license for the 2026 World Cup, so adidas 2026 World
# Cup pages MAY use the FIFA / World Cup family (past tense, that event). It is not a
# standing partnership and does not extend to future tournaments. Every non-adidas
# brand (Nike, Umbro, Kelme, Puma, Hummel, ...) holds no FIFA license and is forbidden.
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
    # adidas / fifa-permitted pages: permitted under the 2026 World Cup license, skip the check.
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
                f"page (no FIFA license); use federation / cycle language{note}",
                line=ln,
            ))
    return findings


# --------------------------------------------------------------------------- #
# Check: brand-name casing in customer-facing prose (added 2026-08-04, Batch 12)
# --------------------------------------------------------------------------- #
# Only adidas is lowercase (registered trademark); every other kit brand must be
# capitalized in customer copy. voice_check catches a capitalized "Adidas"; this
# catches the inverse for the other brands. Scoped to prose fields via
# prose_field_lines + blanked_prose, and backtick spans are stripped, so keyword
# citations, slugs, and keyword-table rows never fire. Standalone-word match with a
# hyphen/slash adjacency guard so slugs like "nike-phantom" never trip it.
_LOWERCASE_BRANDS = re.compile(
    r"(?<![\w/-])(nike|puma|mizuno|kelme|umbro|hummel|new\s+balance)(?![\w/-])"
)


def check_brand_casing(sku, lines) -> list[Finding]:
    """Flag a lowercase non-adidas brand token as a standalone word in customer-facing
    prose. adidas is intentionally lowercase and is deliberately not in the pattern."""
    findings = []
    for ln, text in blanked_prose(lines, prose_field_lines(lines)):
        text = re.sub(r"`[^`]*`", " ", text)   # never fire on a backtick keyword citation
        for m in _LOWERCASE_BRANDS.finditer(text):
            findings.append(Finding(
                sku, "brand-casing", FAIL,
                f"lowercase brand '{m.group(0)}' in customer-facing copy; capitalize the "
                f"brand name (only adidas is lowercase)",
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
    if not meta:
        # meta is None is already a batch-level FAIL raised in gate_brief; nothing to add.
        return []
    # A gate-meta block that is PRESENT but carries no usable word_band silently
    # disabled this check with no skip line at all, which is the worst shape of the
    # false-green class: no output to notice. It is now a hard fail.
    if not meta.get("word_band"):
        return [Finding(
            sku, "word-band", FAIL,
            "input file has a gate-meta block but no `word_band`, so the word-band "
            "check could not run. Set it from the SKU's OWN tier (Elite 400-450, "
            "Pro 340-390, League/Club/Academy 280-340).",
        )]
    band = meta["word_band"]
    if not (isinstance(band, list) and len(band) == 2
            and all(isinstance(b, int) for b in band) and band[0] <= band[1]):
        return [Finding(
            sku, "word-band", FAIL,
            f"gate-meta `word_band` is malformed ({band!r}); expected [low, high] as two "
            "integers with low <= high. The word-band check could not run.",
        )]
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
# Section presence: every required PDP section present WITH real content beneath
# (added 2026-08-01, codification candidate 4 from Batch 9, deferred twice).
#
# A heading with nothing under it counts as missing. Two production origins:
#   - Batch 9 shipped briefs missing Product Details / Fit Notes / Care / FAQ. That
#     was caught ONLY because the absent prose dragged the word count under band and
#     the gate does check word band -- an accident of a different check, not a section
#     check. Internal links are too short to move the count, so an omitted link fires
#     nothing.
#   - Batch 10 shipped three briefs (KC3952, KB8251, YT3FL1NM) with ZERO internal
#     links. batch_gate ran nine mechanical checks, none of them section presence;
#     Layer 3 checks claims; the voice check checks language. Four green reports, none
#     looking at whether a required section exists. This check is that missing look.
#
# It runs UNCONDITIONALLY -- never gated on the per-SKU input file -- because the
# Batch 10 root cause was exactly that the input contract (ORIN's template calls for a
# pre-validated 1-2 internal links block per SKU) went unmet batch-wide and nothing
# verified the OUTPUT. A check that trusts the input cannot catch an input that lied by
# omission. Hard FAIL, so a missing section can never bare-PASS.
# --------------------------------------------------------------------------- #
_ANY_HEADING = re.compile(r"^#{1,6}\s+\S")
_ANY_H2 = re.compile(r"^#{2}\s+\S")
_ANY_H3 = re.compile(r"^#{3}\s+\S")
SEC_PRODUCT_DETAILS = re.compile(r"^#{2}\s+Product\s+Details\b", re.IGNORECASE)
SEC_FIT_NOTES = re.compile(r"^#{2}\s+Fit\s+Notes\b", re.IGNORECASE)
SEC_CARE = re.compile(r"^#{2}\s+Care\s+(?:and|&)\s+Maintenance\b", re.IGNORECASE)
SEC_FAQ = re.compile(r"^#{2}\s+FAQs?\b", re.IGNORECASE)
FIELD_IMAGE_ALT = re.compile(r"^#{3}\s+Image\s+Alt(\s+Text)?\b", re.IGNORECASE)
# An internal link is a markdown link whose target is a ProSoccer collection or product
# PATH. Presence only -- canonical-URL FORMAT (https + www) is voice_check's job, so a
# relative or bare-domain path still counts as PRESENT here and gets flagged for format
# there. This split keeps the two failure modes (absent vs malformed) independent.
INTERNAL_LINK = re.compile(r"\]\(\s*[^)]*?/(?:collections|products)/[^)\s]")


def _has_content_below(lines: list[str], i: int, end: int) -> bool:
    """True if a non-blank, non-heading line appears after heading line i and before the
    next heading (any level) or `end`. A heading immediately followed by another heading
    (nothing but blanks between) is an empty section -> False."""
    for j in range(i + 1, end):
        s = lines[j].strip()
        if not s:
            continue
        return not bool(_ANY_HEADING.match(lines[j]))
    return False


def _faq_has_qa(lines: list[str], faq_idx: int, end: int) -> bool:
    """True if the FAQ H2 at faq_idx has >=1 '### question' with a non-empty answer line
    beneath it, before the next H2 or `end`. A bare '## FAQs' with no Q&A, or questions
    with empty answers, is missing content."""
    for j in range(faq_idx + 1, end):
        if _ANY_H2.match(lines[j]):
            break
        if _ANY_H3.match(lines[j]) and _has_content_below(lines, j, end):
            return True
    return False


def check_section_presence(sku, lines) -> list[Finding]:
    """FAIL for each required PDP section that is absent, or present as a heading with no
    content beneath it. Required PDP set: an editorial narrative region (overview,
    heritage/build, use-case -- the skeleton calls for three; the deterministic floor is
    at least one editorial H2 with prose, since the titles are creative and unbounded),
    Product Details, Fit Notes, Care and Maintenance, FAQs about [product], Image Alt
    Text, and at least one internal link in the Description body."""
    findings: list[Finding] = []
    start, end = body_region(lines)
    if start == -1:
        return [Finding(sku, "section-presence", FAIL,
                        "no Description body ('### Description' field missing)")]

    # Locate the named structural H2 sections inside the Description body.
    idx = {"Product Details": None, "Fit Notes": None,
           "Care and Maintenance": None, "FAQ": None}
    for i in range(start, end):
        if idx["Product Details"] is None and SEC_PRODUCT_DETAILS.match(lines[i]):
            idx["Product Details"] = i
        elif idx["Fit Notes"] is None and SEC_FIT_NOTES.match(lines[i]):
            idx["Fit Notes"] = i
        elif idx["Care and Maintenance"] is None and SEC_CARE.match(lines[i]):
            idx["Care and Maintenance"] = i
        elif idx["FAQ"] is None and SEC_FAQ.match(lines[i]):
            idx["FAQ"] = i

    # Editorial narrative region: >=1 H2 with content before the first structural section.
    struct_positions = [i for i in idx.values() if i is not None]
    first_struct = min(struct_positions) if struct_positions else end
    editorial = [i for i in range(start, first_struct) if _ANY_H2.match(lines[i])
                 and _has_content_below(lines, i, end)]
    if not editorial:
        findings.append(Finding(
            sku, "section-presence", FAIL,
            "no editorial narrative section (overview / heritage / use-case) with content "
            "before the spec sections; the body is missing its lead copy"))

    # Named spec sections: present AND non-empty.
    for label in ("Product Details", "Fit Notes", "Care and Maintenance"):
        i = idx[label]
        if i is None:
            findings.append(Finding(sku, "section-presence", FAIL,
                                    f"required PDP section '{label}' is missing"))
        elif not _has_content_below(lines, i, end):
            findings.append(Finding(sku, "section-presence", FAIL,
                                    f"section '{label}' is a heading with no content beneath it",
                                    line=i + 1))

    # FAQ: present AND carries at least one question with an answer.
    if idx["FAQ"] is None:
        findings.append(Finding(sku, "section-presence", FAIL,
                                "required PDP section 'FAQs about [product]' is missing"))
    elif not _faq_has_qa(lines, idx["FAQ"], end):
        findings.append(Finding(sku, "section-presence", FAIL,
                                "FAQ section has no question with an answer beneath it",
                                line=idx["FAQ"] + 1))

    # Image Alt Text: a field (### level) after the body, present AND non-empty.
    alt_idx = next((i for i, ln in enumerate(lines) if FIELD_IMAGE_ALT.match(ln)), None)
    if alt_idx is None:
        findings.append(Finding(sku, "section-presence", FAIL,
                                "required field 'Image Alt Text' is missing"))
    elif not _has_content_below(lines, alt_idx, len(lines)):
        findings.append(Finding(sku, "section-presence", FAIL,
                                "'Image Alt Text' has a heading but no alt lines beneath it",
                                line=alt_idx + 1))

    # At least one internal link in the Description body (the Batch 10 defect class).
    if not any(INTERNAL_LINK.search(lines[i]) for i in range(start, end)):
        findings.append(Finding(
            sku, "section-presence", FAIL,
            "no internal link in the Description body; at least one link to a ProSoccer "
            "collection or product page is required (Batch 10 KC3952/KB8251/YT3FL1NM class)"))

    return findings


# --------------------------------------------------------------------------- #
# Customization claims: name/number customization LOCATION and DURATION facts
# (added 2026-08-03, failure pattern 1 in SEO_BATCH_PROCESS.md §7).
#
# Authoritative facts: context/shipping-customization-facts.md. Two customer-facing
# facts shipped wrong across Batch 10 briefs:
#   (a) LOCATION: name/number customization is selected ON THE PRODUCT PAGE, not "at
#       checkout". Briefs said "add one at checkout".
#   (b) DURATION: it adds BUSINESS DAYS (Customized name/number: 2-3 business days),
#       not weeks. Briefs said "an extra 1 to 2 weeks" / "1 to 3 weeks".
# Neither moved the word count, so nothing fired. This check looks directly, hard FAIL.
# Runs unconditionally (never input-gated). The team/club "up to 4 weeks" tier is the
# only correct use of "weeks", and it does not belong in a single-product PDP's
# name/number copy, so requiring the customization term nearby avoids false positives.
# --------------------------------------------------------------------------- #
CUSTOMIZATION_TERMS = re.compile(
    r"\b(name[\s/&-]*(?:and[\s/&-]*)?number|"   # name and number / name-and-number / name/number
    r"customi[sz](?:e[ds]?|able|ation)|"        # customize(d/s), customizable, customization
    r"personali[sz](?:e[ds]?|ation))\b",        # personalize(d/s), personalization
    re.IGNORECASE,
)
CHECKOUT_RE = re.compile(r"\bcheckout\b", re.IGNORECASE)
WEEKS_RE = re.compile(r"\bweeks?\b", re.IGNORECASE)
# Proximity window (chars) around a customization term to look for the wrong location
# ("checkout") or the wrong unit ("week"). PDP paragraphs are short; this ties the two
# together within one claim rather than flagging an unrelated distant mention.
_CUST_WINDOW = 200


def check_customization_claims(sku, lines) -> list[Finding]:
    """FAIL: customer-facing copy that (a) pairs customization language with 'checkout'
    (name/number customization is a PRODUCT-PAGE option), or (b) gives name/number
    customization timing in weeks (it adds business days: Customized name/number is 2-3
    business days). Scans the prose fields (Title, Short Description, Description body
    incl. FAQ, Meta fields). See context/shipping-customization-facts.md."""
    findings: list[Finding] = []
    seen: set[tuple[int, str]] = set()
    for ln, text in blanked_prose(lines, prose_field_lines(lines)):
        spans = [(m.start(), m.end()) for m in CUSTOMIZATION_TERMS.finditer(text)]
        if not spans:
            continue

        def _near(rx) -> bool:
            return any(rx.search(text[max(0, s - _CUST_WINDOW): e + _CUST_WINDOW])
                       for s, e in spans)

        if (ln, "checkout") not in seen and _near(CHECKOUT_RE):
            seen.add((ln, "checkout"))
            findings.append(Finding(
                sku, "customization-claim", FAIL,
                "customization language paired with 'checkout'; name/number customization "
                "is selected ON THE PRODUCT PAGE, not at checkout "
                "(context/shipping-customization-facts.md)",
                line=ln))
        if (ln, "week") not in seen and _near(WEEKS_RE):
            seen.add((ln, "week"))
            findings.append(Finding(
                sku, "customization-claim", FAIL,
                "name/number customization timing given in weeks; it adds BUSINESS DAYS "
                "(Customized name/number: 2-3 business days), never weeks "
                "(context/shipping-customization-facts.md)",
                line=ln))
    return findings


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
# Heritage honour claims: specific title/trophy counts + "most"/"record" superlatives
# (added 2026-07-13, claims gate). Heritage honours DEFAULT TO QUALITATIVE: specific
# league/title/trophy counts and outright "most"/"record" superlatives age and are
# contested. Origin: KA6871's first draft shipped "among England's most successful
# clubs: 13 Premier League titles, a record 20 English league titles (shared with
# Liverpool)"; Liverpool drew level with Manchester United at 20 English league titles
# in 2024-25, breaking both the "record 20" count and the "most successful" superlative.
# A count ships ONLY with a durable cited source (scrape / club site); otherwise it is
# cut to qualitative. This check flags the count/superlative so it can never bare-PASS.
# NOTE: the approved qualitative language ("one of England's most decorated clubs",
# "a European pedigree few can match") is deliberately NOT matched.
# --------------------------------------------------------------------------- #
HERITAGE_COUNT = re.compile(
    r"\b(?:\d{1,3}|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    r"thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)\s+"
    r"(?:\S+\s+){0,3}?"
    r"(?:league|top[\s-]?flight|premier\s+league|european|continental|champions)\s+"
    r"(?:titles?|crowns?|cups?|trophy|trophies)\b",
    re.IGNORECASE,
)
HERITAGE_SUPERLATIVE = re.compile(
    r"\b(?:most\s+successful\s+(?:club|side|team|english)|"
    r"most\s+(?:titles|trophies|league\s+titles)|"
    r"more\s+than\s+any\s+other\s+(?:club|side|team|english)|"
    r"record[\s-]+(?:\d|holders?|number))",
    re.IGNORECASE,
)


def check_heritage_counts(sku, lines) -> list[Finding]:
    """FAIL: a specific honour count ("13 Premier League titles", "20 English league
    titles", "six European crowns") or an outright "most"/"record" superlative in
    customer-facing copy. Heritage honours default to qualitative; counts age and are
    contested. Cut to qualitative or attach a durable cited source. Regression fixture:
    KA6871's "a record 20 English league titles" (see test_batch_gate.py)."""
    findings = []
    for ln, text in blanked_prose(lines, prose_field_lines(lines)):
        for m in HERITAGE_COUNT.finditer(text):
            findings.append(Finding(
                sku, "heritage-count", FAIL,
                f"specific honour count '{m.group(0).strip()}' in body copy; heritage "
                f"honours default to qualitative (counts age and are contested) -- cut "
                f"to qualitative or attach a durable cited source (claims gate)",
                line=ln,
            ))
        for m in HERITAGE_SUPERLATIVE.finditer(text):
            findings.append(Finding(
                sku, "heritage-superlative", FAIL,
                f"outright honour superlative '{m.group(0).strip()}' in body copy; use "
                f"qualitative honours ('one of England's most decorated clubs') -- no "
                f"unsourced 'most'/'record' claim (claims gate)",
                line=ln,
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
    # Section presence: required sections present with content (unconditional, never
    # input-gated). Catches the Batch 9 missing-spec-section and Batch 10 missing-link classes.
    findings += check_section_presence(sku, lines)
    # Customization claims: name/number location (product page, not checkout) + duration
    # (business days, not weeks). Unconditional. SEO_BATCH_PROCESS.md §7 pattern 1.
    findings += check_customization_claims(sku, lines)
    # Check 10: price in body.
    findings += check_price_in_body(sku, lines)
    # Heritage honour claims (specific counts / "most"-"record" superlatives) -- claims gate.
    findings += check_heritage_counts(sku, lines)
    # Check 11: fabrication hedges (REVIEW).
    findings += check_fabrication_hedge(sku, lines)

    # Input-dependent checks (5, 6, 8). A missing input file means three checks
    # CANNOT RUN, including word-band and the full forbidden-phrasings pass. That is
    # a hard failure, not a skip note: same false-green class as the Registry 1 file
    # (Mike's ruling 2026-08-18, extended from registry1 to every unrunnable check).
    if meta is None:
        skipped += ["fifa-terms(no-input)", "forbidden-phrasings(no-input)", "word-band(no-input)"]
        findings.append(Finding(
            sku, "input-file", FAIL,
            "no input file at inputs/{}_input.md (or it carries no gate-meta block), so "
            "word-band, forbidden-phrasings and the branded FIFA check could not run for "
            "this SKU. A check that cannot run is a failure.".format(sku),
        ))
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

    # Per-brief brand-name casing (lowercase non-adidas brand in customer prose).
    for bd in briefs_data:
        all_findings += check_brand_casing(bd["sku"], bd["lines"])

    # Cross-brief checks (7, 9).
    all_findings += check_registry1_present(registry1)
    all_findings += check_cannibalization(briefs_meta, registry1)
    all_findings += check_cross_brief(briefs_data)

    return report(session_dir, briefs, all_findings, all_skipped, registry1)


def report(session_dir, briefs, findings, skipped, registry1) -> int:
    fails = [f for f in findings if f.severity == FAIL]
    reviews = [f for f in findings if f.severity == REVIEW]

    print(f"BATCH GATE -- {session_dir}")
    print(f"  briefs checked: {len(briefs)}")
    if registry1 is not None:
        print(f"  cross-batch cannibalization: ON ({len(registry1)} claimed primaries)")
    print()

    if not findings:
        # Backstop. Any future skip source that does not yet raise its own FAIL must
        # still never reach exit 0: a check that did not run is not a pass.
        if skipped:
            print("BLOCKED: checks could not run, so this is not a pass.")
            for s in skipped:
                print(f"  - {s}")
            return 2
        print("PASS: no findings across all mechanical checks.")
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
