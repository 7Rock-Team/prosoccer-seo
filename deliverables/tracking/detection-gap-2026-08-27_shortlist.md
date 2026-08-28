# Detection gap: stock-resolved shortlist

**Date:** 2026-08-27  |  **Items:** B-DETECT-01, B-MERCH-05  |  **Owner:** ORIN

Top 25 untracked PRODUCT pages by 90-day impressions, from the completed paginated pull.
Full 1,731-row pull: `detection-gap-2026-08-27.csv`.

**Result: 25 of 25 are SOLD OUT. 0 of 129 variants available.**

## How stock was established, and a correction

Stock was first read through Firecrawl's JSON extraction of each product's `.js` endpoint.
That is an LLM reading a JSON document, and on 4 of the 25 it miscounted the variant array,
reporting one more option than the product has. The first version of this file therefore said
**133 options**; the correct figure is **129**. Re-derived from the storefront's own
`products.json`, counted programmatically rather than read by a model, and cross-checked
against a direct `.js` fetch on the two largest disagreements. Both agree at 129.

**The sold-out verdict never moved.** Both sources put all 25 at zero available variants, and
the binary agreed on 25 of 25. Only the denominator was wrong. Recording it because it is the
house rule in miniature: a model reporting a count is not a measurement, even when the model
is reading structured data and even when its answer is nearly right.

## Control

25 of 25 is the shape of an instrument error, so three known-live shipped pages (Batch 15.1
and 16) were run through the identical method. All three returned IN STOCK with 8 to 10
available variants. The method can return in-stock. The result is real.

## The 25

| # | Product | Season | Created | Impr | Clicks | CTR | Pos | Top query | Price | Variants |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `adidas-mexico-2019-home-authentic-jersey-black` | 2019 | 2022-04-27 | 728,930 | 188 | 0.0258% | 6.03 | `black mexico jersey` | $95.00 | 0 / 5 |
| 2 | `nike-2024-25-norway-mens-stadium-home-jersey` | 2024 | 2024-04-25 | 693,678 | 679 | 0.0979% | 6.27 | `norway jersey` | $62.00 | 0 / 6 |
| 3 | `adidas-2026-mexico-mens-authentic-home-long-sleeve-soccer-jersey` | 2026 | 2025-11-10 | 191,587 | 287 | 0.1498% | 8.70 | `mexico jersey world cup 2026 authentic` | $104.00 | 0 / 6 |
| 4 | `puma-23-24-chivas-mens-away-promo-jersey` | 2023 | 2023-06-23 | 146,451 | 13 | 0.0089% | 11.31 | `chivas jersey` | $28.00 | 0 / 5 |
| 5 | `panini-2026-adrenalyn-xl-fifa-world-cup-cards-pack-8-cards-each` | 2026 | 2026-02-27 | 98,129 | 205 | 0.2089% | 9.32 | `world cup cards` | $4.99 | 0 / 1 |
| 6 | `nike-2026-norway-mens-authentic-away-soccer-jersey` | 2026 | 2026-04-27 | 92,623 | 898 | 0.9695% | 8.13 | `norway jersey` | $123.00 | 0 / 6 |
| 7 | `nike-elite-backpack-32l` | n/a | 2023-11-01 | 89,296 | 139 | 0.1557% | 8.46 | `nike elite bookbag` | $86.99 | 0 / 1 |
| 8 | `nike-2024-25-france-mens-authentic-home-jersey` | 2024 | 2024-04-05 | 86,207 | 72 | 0.0835% | 7.03 | `france soccer jersey` | $111.00 | 0 / 5 |
| 9 | `nike-2026-27-norway-mens-authentic-home-soccer-jersey` | 2026 | 2026-03-17 | 84,685 | 555 | 0.6554% | 7.67 | `norway jersey 2026` | $123.00 | 0 / 6 |
| 10 | `nike-2026-27-norway-mens-stadium-home-soccer-jersey` | 2026 | 2026-03-17 | 66,959 | 742 | 1.1081% | 8.42 | `norway soccer jersey` | $70.00 | 0 / 6 |
| 11 | `nike-2022-23-korea-away-long-sleeve-jersey-black` | 2022 | 2022-12-22 | 66,140 | 34 | 0.0514% | 6.06 | `south korea away jersey` | $70.00 | 0 / 5 |
| 12 | `adidas-2026-colombia-mens-authentic-away-soccer-jersey` | 2026 | 2026-03-28 | 59,506 | 54 | 0.0907% | 6.69 | `colombia jersey 2026` | $98.00 | 0 / 6 |
| 13 | `nike-2026-27-france-mens-authentic-away-soccer-jersey` | 2026 | 2026-03-20 | 56,719 | 798 | 1.4069% | 7.52 | `france away jersey` | $132.00 | 0 / 6 |
| 14 | `adidas-predator-freak-3-laceless-fg-black-pink-purple` | n/a | 2022-04-27 | 56,457 | 15 | 0.0266% | 7.80 | `adidas predator cleats` | $50.00 | 0 / 13 |
| 15 | `nike-2026-27-norway-mens-stadium-third-soccer-jersey` | 2026 | 2026-03-23 | 55,921 | 547 | 0.9782% | 7.01 | `norway soccer jersey` | $70.00 | 0 / 5 |
| 16 | `nike-2024-25-portugal-mens-stadium-away-jersey` | 2024 | 2024-04-09 | 55,163 | 259 | 0.4695% | 3.97 | `portugal away jersey` | $48.00 | 0 / 6 |
| 17 | `puma-2026-27-egypt-mens-stadium-home-soccer-jersey` | 2026 | 2026-03-17 | 51,337 | 256 | 0.4987% | 7.19 | `egypt soccer jersey` | $65.00 | 0 / 6 |
| 18 | `adidas-2025-mexico-mens-de-oro-authentic-soccer-jersey` | 2025 | 2025-03-17 | 49,307 | 98 | 0.1988% | 6.33 | `mexico de oro jersey` | $149.99 | 0 / 5 |
| 19 | `adidas-2024-25-spain-mens-authentic-home-jersey` | 2024 | 2024-03-25 | 49,238 | 115 | 0.2336% | 6.86 | `spain jersey` | $75.00 | 0 / 5 |
| 20 | `fifa-2026-world-cup-match-bracket-poster` | 2026 | 2026-05-13 | 48,176 | 596 | 1.2371% | 5.45 | `world cup bracket poster` | $14.00 | 0 / 1 |
| 21 | `adidas-2026-spain-mens-authentic-away-long-sleeve-soccer-jersey` | 2026 | 2026-03-30 | 47,062 | 1044 | 2.2184% | 6.88 | `spain jersey 2026` | $159.99 | 0 / 5 |
| 22 | `adidas-2025-mexico-mens-de-oro-authentic-long-sleeve-soccer-jersey` | 2025 | 2025-03-25 | 46,528 | 92 | 0.1977% | 5.74 | `mexico black long sleeve jersey` | $159.99 | 0 / 3 |
| 23 | `adidas-2026-japan-mens-authentic-away-soccer-jersey` | 2026 | 2026-04-03 | 45,970 | 492 | 1.0703% | 6.57 | `japan away jersey 2026` | $98.00 | 0 / 5 |
| 24 | `adidas-2022-23-mexico-away-long-sleeve-jersey-wonder-white` | 2022 | 2022-10-21 | 43,165 | 158 | 0.3660% | 6.70 | `mexico jersey long sleeve` | $55.00 | 0 / 5 |
| 25 | `adidas-2026-spain-mens-authentic-home-soccer-jersey` | 2026 | 2025-11-11 | 42,046 | 103 | 0.2450% | 7.50 | `spain jersey 2026` | $149.99 | 0 / 6 |

**Combined: 3,051,280 impressions, 8,439 clicks, blended CTR 0.2766%.**

## Age

13 of 25 are current 2026 season, created between 2025-11-10 and 2026-05-13. 10 are prior
seasons (2019 through 2025). 2 carry no season tag. So this is two populations, not one: half
is current product that sold out in a World Cup year, half is older stock whose demand
outlived it. The impressions split leans old only because the top two pages are outliers.

Do not select a batch from this list. It is a measurement, not a plan. Batch 17 candidates are
drawn from the 10k to 100k band instead, and only from pages that are in stock.
