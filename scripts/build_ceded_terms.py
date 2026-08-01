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
PROD = "deliverables/tracking/products-master.csv"
CEDED = "deliverables/tracking/ceded-terms.csv"
HEADER = ["term", "normalized_term", "ceded_to_url", "source_file", "date"]


def norm(t: str) -> str:
    return t.strip().lower().replace("'", " ").replace("  ", " ")


def main():
    date = "2026-07-31"
    if "--date" in sys.argv:
        date = sys.argv[sys.argv.index("--date") + 1]

    # 1. Derive cedes from BOTH masters' ceded_from (the single source of truth per
    #    registry row: collection rows and PDP/pack rows both carry ceded_from the
    #    same way). Decision 1 (Mike, 2026-07-31): one pattern, one concept.
    derived = []
    seen = set()
    for master in (COLL, PROD):
        label = os.path.basename(master) + " (derived)"
        for r in csv.DictReader(open(master, encoding="utf-8")):
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
                    "term": term, "normalized_term": norm(term),
                    "ceded_to_url": url, "source_file": label, "date": date,
                })

    # 2. TRANSITIONAL: preserve any existing cede whose target is neither a /collections/
    #    nor a /products/ URL (the legacy free-text PDP/pack cedes not yet migrated into
    #    products-master ceded_from). Remove this fallback once migration is complete and
    #    every cede derives from a master registry row.
    preserved = []
    if os.path.exists(CEDED):
        derived_terms = {(d["normalized_term"]) for d in derived}
        for r in csv.DictReader(open(CEDED, encoding="utf-8")):
            tgt = r["ceded_to_url"]
            if tgt.startswith("/collections/") or tgt.startswith("/products/"):
                continue
            if norm(r["term"]) in derived_terms:
                continue
            preserved.append(r)

    rows = derived + preserved
    with open(CEDED, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=HEADER)
        w.writeheader()
        w.writerows(rows)

    print(f"wrote {CEDED}: {len(rows)} rows "
          f"({len(preserved)} preserved non-collection PDP/pack cedes, "
          f"{len(derived)} derived collection cedes)")


if __name__ == "__main__":
    main()
