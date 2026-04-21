# Google Search Console Exports
Date range: April 19, 2025 — April 18, 2026 (12 months)
Pulled: April 20, 2026

## Files
- `_weekly-performance.csv` — clicks, impressions, CTR, avg position by week
- `_top-queries.csv` — top 1000 search queries
- `_top-pages.csv` — top 1000 landing pages
- `_countries.csv` — performance by country
- `_devices.csv` — mobile vs desktop vs tablet breakdown
- `_search-appearance.csv` — product snippets, merchant listings, etc.
- `Filters.csv` — applied filters metadata

## Key baseline numbers (12-month)
- Total clicks: 169,553
- Total impressions: 25,504,511
- Avg CTR: 0.66%
- Avg position: 16.4

## Key trend
- Avg position improved from 20.8 → 10.0 over the 12-month window
- Weekly clicks grew from ~2,900 to ~4,300
- Position lift started mid-September 2025 (before 7 Rock re-engaged Feb 2026) — not attributable to our work
- Impressions surged 2x starting Feb 2026 (330k/week → 700k+/week), CTR compressed through the surge — consistent with Google AI Overviews impression double-counting, not a real click gain

## Data hygiene
Raw CSVs live on Mike's local machine in this folder and are gitignored per `.gitignore`.
Only this README is version-controlled. Future state: move raw exports to Google Drive
and reference from here. Do not commit raw exports containing query- or URL-level detail.