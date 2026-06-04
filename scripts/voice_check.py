"""Voice-check any file against the forbidden list in context/03-brand-voice.md.

Usage:
    python scripts/voice_check.py <path>
    python scripts/voice_check.py --file <path>

Supports .md, .txt, and .docx. Exit code 0 on clean, non-zero on violations.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FORBIDDEN_WORDS = [
    "delve", "delving",
    "unlock", "unlocks", "unlocked",
    "elevate", "elevating",
    "revolutionize",
    "seamless",
    "cutting-edge",
    "game-changer",
    "unleash",
]

FORBIDDEN_PHRASES = [
    "leverage",   # as verb; enforced with \b boundaries below
    "leverages",
    "leveraging",
    "in today's world",
    "it's important to note",
    "navigate the complex landscape",
    "dive into",
    "embark on a journey",
]

SENTENCE_OPENERS = ["In conclusion", "In summary"]

EM_DASHES = ["—", "–"]  # — and –

# Brand styling: "adidas" is always lowercase, even at sentence start (official
# trademark styling). Flag a capitalized, standalone "Adidas", EXCEPT when it is:
#   - inside a fenced block or inline backticks (already blanked by strip_backticks)
#   - immediately preceded by a backtick or a hyphen (taxonomy compounds like
#     "non-Adidas", and any backtick-adjacent literal that survived stripping)
#   - immediately followed by a hyphen + word char ("Adidas-only", "Adidas-licensed",
#     "Adidas-specific" -- workforce taxonomy jargon, not output styling)
#   - on a line carrying a pedagogical anti-pattern marker (see PEDAGOGICAL_MARKERS)
ADIDAS_PATTERN = re.compile(r"(?<![-`])\bAdidas\b(?!-\w)")

# US market language: soccer footwear is "cleats" (US market) not "boots"
# (UK/global convention). Flag standalone "boot"/"boots" in body copy; the US
# market term is "cleat(s)" (primary), "shoe(s)" (acceptable secondary variation).
# Non-soccer technical and idiom uses ("boot up", "boot camp", "boot loader",
# "to boot", "das boot") are blanked before the check so they do not false-flag;
# "bootstrap" and "reboot" never match because \b requires a word boundary.
# Backtick/fenced content and pedagogical anti-pattern lines are exempt, same as
# the Adidas check above.
BOOT_PATTERN = re.compile(r"\bboots?\b", re.IGNORECASE)
BOOT_NON_SOCCER = re.compile(
    r"\bboots?\s+(?:up|camp|loader|sector|disk|drive|menu|partition|record|screen)\b"
    r"|\bto\s+boot\b"
    r"|\bdas\s+boot\b"
    r"|\bboots?\s+on\s+the\s+ground\b",
    re.IGNORECASE,
)

# Internal link format: link suggestions in deliverables and briefings must be full
# HTTPS URLs on the canonical domain (https://www.prosoccer.com/...). These two
# patterns catch the two failure modes seen in production: an insecure http://
# ProSoccer URL, and a mangled link that lost its domain segment (http:///path).
# These checks run ONLY when the file path is inside deliverables/ or briefings/;
# the playbooks carry these strings as pedagogical INCORRECT examples and are out of
# scope. Backtick/fenced content and pedagogical lines are exempt, same as above.
LINK_INSECURE_PATTERN = re.compile(r"http://[^/\s]*prosoccer\.com", re.IGNORECASE)
LINK_MANGLED_PATTERN = re.compile(r"http:/{3,}[a-z]", re.IGNORECASE)

# Lines demonstrating what NOT to do are exempt from the Adidas check; the
# capitalized form on these lines is intentional teaching content.
PEDAGOGICAL_MARKERS = (
    "incorrect",
    "do not use",
    "anti-pattern",
    "stuffed:",
    "wrong:",
    "bad example",
    "forbidden",
    "uk convention",
    "uk-convention",
    "uk/global",
)

SUPPORTED_EXTS = {".md", ".txt", ".docx"}


def extract_text(path: Path) -> str:
    """Return the full readable text of the file, format-aware."""
    suffix = path.suffix.lower()
    if suffix in {".md", ".txt"}:
        return path.read_text(encoding="utf-8")
    if suffix == ".docx":
        try:
            from docx import Document
        except ImportError:
            print("ERROR: python-docx is not installed. Run: pip install python-docx", file=sys.stderr)
            sys.exit(2)
        doc = Document(path)
        parts: list[str] = []
        for p in doc.paragraphs:
            parts.append(p.text)
        for tbl in doc.tables:
            for row in tbl.rows:
                for cell in row.cells:
                    for p in cell.paragraphs:
                        parts.append(p.text)
        for section in doc.sections:
            for hdr_ftr in (section.header, section.footer, section.first_page_header, section.first_page_footer):
                for p in hdr_ftr.paragraphs:
                    parts.append(p.text)
        return "\n".join(parts)
    raise ValueError(f"Unsupported file type: {suffix}. Supported: {sorted(SUPPORTED_EXTS)}")


def strip_backticks(text: str) -> str:
    """Blank out content inside fenced code blocks (```...```) and inline backticks (`...`).

    Voice rules apply to ProSoccer's own prose, not to verbatim quotations of
    competitor copy, code, or terminal output that get cited inside backticks.
    Replacement preserves newlines so line numbers in violation output stay accurate.
    """
    def blank_keep_newlines(match: re.Match) -> str:
        return "".join("\n" if c == "\n" else " " for c in match.group(0))

    text = re.sub(r"```.*?```", blank_keep_newlines, text, flags=re.DOTALL)
    text = re.sub(r"`[^`\n]*`", blank_keep_newlines, text)
    return text


def find_line_contexts(
    scan_lines: list[str], display_lines: list[str], pattern: re.Pattern
) -> list[tuple[int, str]]:
    """Return (line_number, line_text) tuples for each line where the pattern matches.

    Matches are evaluated against scan_lines (backtick content blanked); the
    displayed context is taken from display_lines (original text).
    """
    hits: list[tuple[int, str]] = []
    for idx, (sline, dline) in enumerate(zip(scan_lines, display_lines), start=1):
        if pattern.search(sline):
            hits.append((idx, dline.strip()))
    return hits


def check(text: str, path: Path | None = None) -> int:
    """Run the voice check against the text. Return 0 if clean, 1 if violations found.

    When `path` is inside deliverables/ or briefings/, also enforce the internal-link
    URL-format checks (full HTTPS canonical-domain links; no insecure or mangled URLs).
    """
    violations: list[str] = []
    display_lines = text.splitlines()
    scan_lines = strip_backticks(text).splitlines()
    link_scope = path is not None and bool(
        re.search(r"deliverables|briefings", str(path), re.IGNORECASE)
    )

    for em in EM_DASHES:
        pattern = re.compile(re.escape(em))
        hits = find_line_contexts(scan_lines, display_lines, pattern)
        if hits:
            name = "em-dash" if em == "—" else "en-dash"
            violations.append(f"{name.upper()} '{em}' found on {len(hits)} line(s):")
            for ln, ctx in hits[:5]:
                violations.append(f"    line {ln}: {ctx[:120]}")
            if len(hits) > 5:
                violations.append(f"    ... and {len(hits) - 5} more")

    for word in FORBIDDEN_WORDS:
        pattern = re.compile(r"\b" + re.escape(word) + r"\b", re.IGNORECASE)
        hits = find_line_contexts(scan_lines, display_lines, pattern)
        if hits:
            violations.append(f"FORBIDDEN WORD '{word}' found on {len(hits)} line(s):")
            for ln, ctx in hits[:5]:
                violations.append(f"    line {ln}: {ctx[:120]}")
            if len(hits) > 5:
                violations.append(f"    ... and {len(hits) - 5} more")

    for phrase in FORBIDDEN_PHRASES:
        pattern = re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE)
        hits = find_line_contexts(scan_lines, display_lines, pattern)
        if hits:
            violations.append(f"FORBIDDEN PHRASE '{phrase}' found on {len(hits)} line(s):")
            for ln, ctx in hits[:5]:
                violations.append(f"    line {ln}: {ctx[:120]}")
            if len(hits) > 5:
                violations.append(f"    ... and {len(hits) - 5} more")

    for opener in SENTENCE_OPENERS:
        pattern = re.compile(r"(?:^|[.!?]\s+)" + re.escape(opener), re.MULTILINE)
        hits = find_line_contexts(scan_lines, display_lines, pattern)
        if hits:
            violations.append(f"FORBIDDEN SENTENCE OPENER '{opener}' found on {len(hits)} line(s):")
            for ln, ctx in hits[:5]:
                violations.append(f"    line {ln}: {ctx[:120]}")

    # Brand styling check: capitalized "Adidas" (adidas is always lowercase).
    # Skip lines carrying a pedagogical anti-pattern marker; backtick/fenced
    # content and taxonomy compounds are excluded by ADIDAS_PATTERN itself.
    adidas_hits: list[tuple[int, str]] = []
    for idx, (sline, dline) in enumerate(zip(scan_lines, display_lines), start=1):
        lowered = sline.lower()
        if any(marker in lowered for marker in PEDAGOGICAL_MARKERS):
            continue
        if ADIDAS_PATTERN.search(sline):
            adidas_hits.append((idx, dline.strip()))
    if adidas_hits:
        violations.append(
            f"CAPITALIZED 'Adidas' found on {len(adidas_hits)} line(s) "
            "(adidas is always lowercase, even at sentence start):"
        )
        for ln, ctx in adidas_hits[:5]:
            violations.append(f"    line {ln}: {ctx[:120]}")
        if len(adidas_hits) > 5:
            violations.append(f"    ... and {len(adidas_hits) - 5} more")

    # US market language check: soccer footwear is "cleats" (US market), not
    # "boots" (UK/global). Skip pedagogical lines; blank non-soccer "boot" phrases
    # before matching. Mirrors the Adidas check (scan_lines already have backtick
    # and fenced content blanked).
    boot_hits: list[tuple[int, str]] = []
    for idx, (sline, dline) in enumerate(zip(scan_lines, display_lines), start=1):
        lowered = sline.lower()
        if any(marker in lowered for marker in PEDAGOGICAL_MARKERS):
            continue
        cleaned = BOOT_NON_SOCCER.sub(lambda m: " " * len(m.group(0)), sline)
        if BOOT_PATTERN.search(cleaned):
            boot_hits.append((idx, dline.strip()))
    if boot_hits:
        violations.append(
            f"UK/GLOBAL 'boot(s)' found on {len(boot_hits)} line(s) "
            "(US market term is 'cleat(s)'; 'shoe(s)' acceptable for variation):"
        )
        for ln, ctx in boot_hits[:5]:
            violations.append(f"    line {ln}: {ctx[:120]}")
        if len(boot_hits) > 5:
            violations.append(f"    ... and {len(boot_hits) - 5} more")

    # Internal link format check (deliverables/ and briefings/ only): link
    # suggestions must be full HTTPS canonical-domain URLs. Flag insecure http://
    # ProSoccer URLs and mangled missing-domain links. Skip pedagogical lines;
    # backtick/fenced content is already blanked in scan_lines.
    if link_scope:
        for label, pattern, detail in (
            ("INSECURE LINK", LINK_INSECURE_PATTERN,
             "ProSoccer links must be https:// (insecure http:// found; "
             "use https://www.prosoccer.com/...):"),
            ("MANGLED LINK", LINK_MANGLED_PATTERN,
             "link is missing its domain (e.g. http:///path); "
             "use the full https://www.prosoccer.com/... form:"),
        ):
            link_hits: list[tuple[int, str]] = []
            for idx, (sline, dline) in enumerate(zip(scan_lines, display_lines), start=1):
                lowered = sline.lower()
                if any(marker in lowered for marker in PEDAGOGICAL_MARKERS):
                    continue
                if pattern.search(sline):
                    link_hits.append((idx, dline.strip()))
            if link_hits:
                violations.append(f"{label}: {detail}")
                for ln, ctx in link_hits[:5]:
                    violations.append(f"    line {ln}: {ctx[:120]}")
                if len(link_hits) > 5:
                    violations.append(f"    ... and {len(link_hits) - 5} more")

    if violations:
        print("VOICE CHECK FAILED")
        for line in violations:
            print(f"  {line}")
        return 1

    print("VOICE CHECK PASSED: no em-dashes, no en-dashes, no forbidden words/phrases/openers, no capitalized Adidas, no UK 'boots'.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Voice-check a file against the ProSoccer brand-voice forbidden list.")
    parser.add_argument("path", nargs="?", help="Path to the file to check (.md, .txt, or .docx).")
    parser.add_argument("--file", dest="file_flag", help="Alternate way to pass the file path.")
    args = parser.parse_args()

    target = args.path or args.file_flag
    if not target:
        parser.error("A file path is required (positional or --file).")

    path = Path(target).resolve()
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    if path.suffix.lower() not in SUPPORTED_EXTS:
        print(f"ERROR: unsupported file type '{path.suffix}'. Supported: {sorted(SUPPORTED_EXTS)}", file=sys.stderr)
        return 2

    text = extract_text(path)
    print(f"Checking: {path}")
    return check(text, path)


if __name__ == "__main__":
    sys.exit(main())
