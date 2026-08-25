#!/usr/bin/env python3
"""Regenerate deliverables/tracking/ceded-terms.csv from the source of truth.

A cede is a property of the collection page, so `collections-master.csv` `ceded_from`
is the SOURCE OF TRUTH for COLLECTION-level cedes; this script derives the flat
ceded-terms.csv list from it. Cedes whose target is NOT a /collections/ URL (cedes
to shipped PDPs / pack-groups / model-level pages) have no collection home, so they
are PRESERVED verbatim from the existing ceded-terms.csv rather than dropped.

Run from repo root:  python scripts/build_ceded_terms.py --date YYYY-MM-DD

--date is REQUIRED, not optional: the script refuses to run without it rather than
default, because a defaulted date silently rewrites the recording date of every
derived row while leaving the content identical. See main().

Output ceded-terms.csv = preserved non-collection cedes + derived collection cedes.
Idempotent: running twice yields the same file.
"""
import csv, re, sys, os

COLL = "deliverables/tracking/collections-master.csv"
CEDED = "deliverables/tracking/ceded-terms.csv"
HEADER = ["term", "normalized_term", "ceded_to_url", "source_file", "date"]


def norm(t: str) -> str:
    return t.strip().lower().replace("'", " ").replace("  ", " ")


def main():
    # --date is REQUIRED. It used to default to a hardcoded date, which silently
    # rewrote every derived row's date on any plain run: at the Batch 15 close a bare
    # invocation regressed 24 rows from their real 2026-08-03 recording date back to
    # 2026-07-31. The rows' CONTENT was byte-identical, so the diff read as an ordinary
    # update rather than a regression, and it was caught only because the regeneration
    # was diffed against the committed file instead of trusted.
    #
    # Same posture as batch_gate.py on a check that cannot run: fail rather than proceed
    # on a silent default. A tool that writes data must never invent the value that says
    # WHEN it was written.
    if "--date" not in sys.argv:
        sys.exit(
            "build_ceded_terms.py: --date YYYY-MM-DD is REQUIRED.\n"
            "  Refusing to run rather than default, because a defaulted date silently\n"
            "  rewrites the recording date of every derived row while leaving the content\n"
            "  identical, so the regression is invisible in a diff.\n"
            "  Pass the date the cedes are being recorded on. To reproduce the committed\n"
            "  file unchanged, pass the date already in its derived rows."
        )
    try:
        date = sys.argv[sys.argv.index("--date") + 1]
    except IndexError:
        sys.exit("build_ceded_terms.py: --date given with no value.")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        sys.exit(f"build_ceded_terms.py: --date must be YYYY-MM-DD, got {date!r}.")

    # 1. Preserve existing NON-collection (PDP/pack) cede rows.
    preserved = []
    if os.path.exists(CEDED):
        for r in csv.DictReader(open(CEDED, encoding="utf-8")):
            if not r["ceded_to_url"].startswith("/collections/"):
                preserved.append(r)

    # 2. Derive collection cedes from collections-master ceded_from (the source of truth).
    derived = []
    seen = set()
    for r in csv.DictReader(open(COLL, encoding="utf-8")):
        cf = (r.get("ceded_from") or "").strip()
        if not cf:
            continue
        url = r["url"].strip()
        for term in cf.split(";"):
            term = term.strip()
            if not term:
                continue
            key = (norm(term), url)
            if key in seen:
                continue
            seen.add(key)
            derived.append({
                "term": term,
                "normalized_term": norm(term),
                "ceded_to_url": url,
                "source_file": "collections-master.csv (derived)",
                "date": date,
            })

    rows = preserved + derived
    with open(CEDED, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=HEADER)
        w.writeheader()
        w.writerows(rows)

    print(f"wrote {CEDED}: {len(rows)} rows "
          f"({len(preserved)} preserved non-collection PDP/pack cedes, "
          f"{len(derived)} derived collection cedes)")


if __name__ == "__main__":
    main()
