#!/usr/bin/env python3
"""Regenerate deliverables/tracking/ceded-terms.csv from the source of truth.

A cede is a property of the collection page, so `collections-master.csv` `ceded_from`
is the SOURCE OF TRUTH for COLLECTION-level cedes; this script derives the flat
ceded-terms.csv list from it. Cedes whose target is NOT a /collections/ URL (cedes
to shipped PDPs / pack-groups / model-level pages) have no collection home, so they
are PRESERVED verbatim from the existing ceded-terms.csv rather than dropped.

Run from repo root:  python scripts/build_ceded_terms.py [--date YYYY-MM-DD]

Output ceded-terms.csv = preserved non-collection cedes + derived collection cedes.
Idempotent: running twice yields the same file.
"""
import csv, sys, os

COLL = "deliverables/tracking/collections-master.csv"
CEDED = "deliverables/tracking/ceded-terms.csv"
HEADER = ["term", "normalized_term", "ceded_to_url", "source_file", "date"]


def norm(t: str) -> str:
    return t.strip().lower().replace("'", " ").replace("  ", " ")


def main():
    date = "2026-07-31"
    if "--date" in sys.argv:
        date = sys.argv[sys.argv.index("--date") + 1]

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
