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


def check(text: str) -> int:
    """Run the voice check against the text. Return 0 if clean, 1 if violations found."""
    violations: list[str] = []
    display_lines = text.splitlines()
    scan_lines = strip_backticks(text).splitlines()

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

    if violations:
        print("VOICE CHECK FAILED")
        for line in violations:
            print(f"  {line}")
        return 1

    print("VOICE CHECK PASSED: no em-dashes, no en-dashes, no forbidden words/phrases/openers.")
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
    return check(text)


if __name__ == "__main__":
    sys.exit(main())
