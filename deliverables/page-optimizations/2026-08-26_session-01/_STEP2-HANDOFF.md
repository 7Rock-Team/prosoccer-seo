# Batch 15.1: Step 2 handoff block

**Batch:** 15.1 | **Session:** `deliverables/page-optimizations/2026-08-26_session-01/`
**Handed off:** 2026-08-26 | **Gate:** PASS, exit 0, 15 of 15 checks ran, zero skips | **Layer 3:** clean
**Commit:** 374e754 (pushed to origin/main)

Paste this block at the top of a fresh Step 2 chat, followed by the ten briefs.

---

## 1. Paste-ready handle list (Matrixify export filter)

```
adidas-jr-f50-hyperfast-league-in-soccer-shoes-chaos-vs-control,adidas-kids-f50-hyperfast-club-fg-mg-soccer-cleats-chaos-vs-control,adidas-jr-f50-hyperfast-league-ll-fg-soccer-cleats-chaos-vs-control,adidas-jr-f50-hyperfast-league-mid-fg-soccer-cleats-chaos-vs-control,adidas-jr-predator-league-ll-fg-soccer-cleats-chaos-vs-control,adidas-kids-f50-hyperfast-club-in-soccer-shoes-chaos-vs-control,adidas-f50-sparkfusion-elite-fg-ag-soccer-cleats-chaos-vs-control,adidas-jr-f50-hyperfast-mid-fg-mg-soccer-cleats-chaos-vs-control,adidas-f50-sparkfusion-league-fg-ag-soccer-cleats-chaos-vs-control,adidas-kids-f50-hyperfast-club-turf-soccer-shoes-chaos-vs-control
```

Ten handles, taken from the briefs' `### URL Handle` fields verbatim, never reconstructed from a product title. Every one verified present in the live product sitemap (14,496 products, fetched 2026-08-25). Confirm the Matrixify export summary reads **10 products** before proceeding.

**Note the abbreviations.** These handles do NOT match their product titles: `jr` where the title says Junior, `kids` where it says Kids', `ll` for Laceless, `in` for Indoor, `mid-fg-mg` on a page titled Club Mid, and no `womens` token on the two pages titled Women's. Use them exactly as given.

## 2. The ten rows

| # | SKU | Handle | Primary keyword | Body words (band) |
|---|---|---|---|---|
| 1 | KK1326 | `adidas-jr-f50-hyperfast-league-in-soccer-shoes-chaos-vs-control` | adidas junior f50 league indoor | 329 (280-340) |
| 2 | KK1345 | `adidas-kids-f50-hyperfast-club-fg-mg-soccer-cleats-chaos-vs-control` | adidas kids f50 club velcro | 332 (280-340) |
| 3 | KK1314 | `adidas-jr-f50-hyperfast-league-ll-fg-soccer-cleats-chaos-vs-control` | adidas junior f50 league laceless fg | 322 (280-340) |
| 4 | KK1316 | `adidas-jr-f50-hyperfast-league-mid-fg-soccer-cleats-chaos-vs-control` | adidas junior f50 league mid fg chaos vs control | 337 (280-340) |
| 5 | IH2080 | `adidas-jr-predator-league-ll-fg-soccer-cleats-chaos-vs-control` | adidas junior predator league laceless fg | 319 (280-340) |
| 6 | KK1341 | `adidas-kids-f50-hyperfast-club-in-soccer-shoes-chaos-vs-control` | adidas kids f50 club indoor | 328 (280-340) |
| 7 | IH4459 | `adidas-f50-sparkfusion-elite-fg-ag-soccer-cleats-chaos-vs-control` | adidas womens f50 sparkfusion elite chaos vs control | 443 (400-450) |
| 8 | KJ0670 | `adidas-jr-f50-hyperfast-mid-fg-mg-soccer-cleats-chaos-vs-control` | adidas junior f50 club mid | 334 (280-340) |
| 9 | IH4488 | `adidas-f50-sparkfusion-league-fg-ag-soccer-cleats-chaos-vs-control` | adidas womens f50 sparkfusion league chaos vs control | 336 (280-340) |
| 10 | KK1368 | `adidas-kids-f50-hyperfast-club-turf-soccer-shoes-chaos-vs-control` | adidas kids f50 club turf | 336 (280-340) |

All 10 of 10 land **strictly inside** their tier band, none drawing on the +/-15 tolerance. Word counts are re-derived by ORIN from `batch_gate.body_word_count`, never taken from an agent's self-report (4 of 10 self-reports disagreed with the gate, worst case by 17 words).

## 3. Meta field pre-check (Step 2 should re-verify, not trust this)

| SKU | Meta Title | chars | Meta Desc chars |
|---|---|---|---|
| KK1326 | adidas Junior F50 League Indoor Shoes | 37 | 141 |
| KK1345 | adidas Kids F50 Club Velcro Cleats | 34 | 150 |
| KK1314 | adidas Junior F50 League Laceless FG | 36 | 135 |
| KK1316 | adidas Junior F50 League Mid Chaos vs Control | 45 | 143 |
| IH2080 | adidas Junior Predator League Laceless FG | 41 | 152 |
| KK1341 | adidas Kids F50 Club Indoor Shoes | 33 | 127 |
| IH4459 | adidas Women's F50 Sparkfusion Elite | 36 | 150 |
| KJ0670 | adidas Junior F50 Club Mid FG/MG Cleats | 39 | 148 |
| IH4488 | adidas Women's F50 Sparkfusion League | 37 | 150 |
| KK1368 | adidas Kids F50 Club Turf Shoes | 31 | 157 |

All ten Meta Titles are under the 48-character written cap, none ends with a manufacturer brand as a pipe suffix, and none types the store name (the theme appends ` - ProSoccer`). All ten Meta Descriptions sit inside 120 to 160.

## 4. Import file

Four content fields ship: Body HTML, meta title, meta description, short description. Nothing else. `Command` = MERGE on every row. No Title column: its absence is the preservation guarantee.

Filename: `ProSoccer_SEO_Batch15.1_10_Products.xlsx`, single sheet named exactly `Products`.

## 5. Stop conditions

- **The import report must read `Updated 10 / Created 0`, with the job ID.** A nonzero Created is a STOP, not a note: Matrixify matches on handle, so a mistyped handle matches nothing and CREATES a phantom product that is live and invisible to every check we run.

- Export summary reading anything other than 10 products.

- Any handle in the export that does not appear in section 1.

## 6. Registry write-back (ORIN, step 15)

Report back the handle list that ACTUALLY imported plus any failures or skips. ORIN flips `status` to `shipped` and writes `batch` = `B15.1` and `implementation_date` for exactly those rows. A handle not reported stays `pending`. These ten are new rows appended to `products-master.csv` at step 14, taking it from 158 to 168.

## 7. Two things a reviewer should know

- **IH4459 and IH4488 are WOMEN'S pages**, not men's or unisex, confirmed by live H1. They are written to an adult woman buying for herself, and both briefs state that no existing avatar fits (gap logged B-AVATAR-02). If the copy reads parent-facing anywhere, that is a defect.

- **Three of the ten carry pack-qualified sub-floor primaries by design** (KK1316, IH4459, IH4488), because a live pack sibling holds the unqualified term. Seven carry unqualified terms, two of those (KJ0670, KK1368) as the measured incumbents at their configuration. Zero measurable DFS volume across all ten is expected, not a research failure.

