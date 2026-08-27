# Batch 16 -- Step 2 handoff

**Session:** `deliverables/page-optimizations/2026-08-26_session-02`  
**Batch:** 16. **Nine SKUs, not ten.** UF1F16X was pulled at pre-dispatch and deliberately NOT backfilled.  
**Gate:** PASS, exit 0, 9 briefs, 15 checks run, 0 skipped, 0 findings. See `_gate-run.json`.

## Paste-ready handle list for the Matrixify export filter

Handles come from the briefs and are never reconstructed from product titles.

```
adidas-predator-league-fg-soccer-cleats-chaos-vs-control-pack,adidas-predator-league-fo-tongue-in-soccer-shoes-chaos-vs-control,adidas-predator-pro-fo-tongue-fg-soccer-cleats-chaos-vs-control,adidas-predator-club-turf-soccer-shoes-chaos-vs-control-pack,adidas-jr-f50-hyperfast-club-fg-mg-soccer-cleats-chaos-vs-control,adidas-2026-27-arsenal-mens-authentic-home-soccer-jersey,pirma-2026-27-cruz-azul-mens-authentic-home-soccer-jersey,pirma-2026-27-cruz-azul-mens-authentic-away-soccer-jersey,pirma-2026-27-cruz-azul-womens-authentic-away-soccer-jersey
```

Confirm the export summary reads **9 products**, not 10.

## The nine

| # | SKU | Handle | Primary | Body words | Band |
|---|---|---|---|---|---|
| 1 | IH7154 | `adidas-predator-league-fg-soccer-cleats-chaos-vs-control-pack` | `adidas predator league fg chaos vs control` | 339 | 280-340 |
| 2 | IH7200 | `adidas-predator-league-fo-tongue-in-soccer-shoes-chaos-vs-control` | `adidas predator league indoor chaos vs control` | 339 | 280-340 |
| 3 | IH7234 | `adidas-predator-pro-fo-tongue-fg-soccer-cleats-chaos-vs-control` | `adidas predator pro fg chaos vs control` | 386 | 340-390 |
| 4 | IH2115 | `adidas-predator-club-turf-soccer-shoes-chaos-vs-control-pack` | `adidas predator club turf` | 319 | 280-340 |
| 5 | KK1308 | `adidas-jr-f50-hyperfast-club-fg-mg-soccer-cleats-chaos-vs-control` | `adidas junior f50 club chaos vs control` | 328 | 280-340 |
| 6 | JZ3165 | `adidas-2026-27-arsenal-mens-authentic-home-soccer-jersey` | `arsenal authentic jersey` | 506 | 450-520 |
| 7 | 18281 | `pirma-2026-27-cruz-azul-mens-authentic-home-soccer-jersey` | `cruz azul authentic jersey` | 509 | 450-520 |
| 8 | 18278 | `pirma-2026-27-cruz-azul-mens-authentic-away-soccer-jersey` | `cruz azul away jersey` | 512 | 450-520 |
| 9 | 18282 | `pirma-2026-27-cruz-azul-womens-authentic-away-soccer-jersey` | `cruz azul womens jersey` | 519 | 450-520 |

## Meta fields as written

| SKU | Meta Title | Len | Meta Description | Len |
|---|---|---|---|---|
| IH7154 | adidas Predator League Firm Ground Cleats | 41 | The adidas Predator League firm ground cleat pairs Nanostrike grip with a clean floating tongue. From the Chaos vs Control pack, built for dry grass. | 149 |
| IH7200 | adidas Predator League Indoor Soccer Shoes | 42 | The Predator League indoor shoe in the Chaos vs Control pack pairs a fold-over striking tongue with a flat rubber court outsole. Lace up for futsal. | 148 |
| IH7234 | adidas Predator Pro Fold-Over Tongue FG | 39 | The adidas Predator Pro FG in the Chaos vs Control pack pairs a Nanostrike Pro upper with a Strikeframe plate for firm natural grass. Pick your corner. | 151 |
| IH2115 | adidas Predator Club Turf Soccer Shoes | 38 | The adidas Predator Club Turf in the Chaos vs Control pack pairs a soft synthetic upper with a rubber turf outsole. Lace in and play your surface. | 146 |
| KK1308 | adidas Junior F50 Hyperfast Club FG/MG | 38 | The adidas Junior F50 Hyperfast Club in the Chaos vs Control pack is a junior speed cleat for grass or artificial turf. Check the fit notes before you order. | 157 |
| JZ3165 | adidas 2026-27 Arsenal Authentic Jersey | 39 | The adidas Arsenal 2026-27 authentic home jersey is the player-issue cut, slim through the body with Climacool+ cooling in Better Scarlet. Pull on the red. | 155 |
| 18281 | Pirma 2026-27 Cruz Azul Authentic Jersey | 40 | Cruz Azul's 2026-27 home jersey from Pirma comes in royal blue with a crest drawn from the club's 1927 to 2027 history. Add your name and number here. | 150 |
| 18278 | Pirma 2026-27 Cruz Azul Away Jersey | 35 | Cruz Azul's 2026-27 away jersey from Pirma, the authentic white change kit in 100% polyester. Add your name and number right on this page. | 138 |
| 18282 | Pirma 2026-27 Cruz Azul Women's Jersey | 38 | The Cruz Azul home jersey for 2026-27, cut and sized for women in the club's royal blue. Authentic tier by Pirma. Add your name and number on this page. | 152 |

## Import-file notes

- Four content fields ship: Body HTML, meta title, meta description, short description. Nothing else.
- `Command` = MERGE on every row. **No Title column** (absence is the preservation guarantee).
- **`Created 0` in the Matrixify job summary is a STOP CONDITION.** Report `Updated N / Created 0` with the job ID.
- Expected: **Updated 9 / Created 0**.

## Carry back to ORIN at step 15

The confirmed-live handle list, plus any failures or skips, plus `Updated N / Created 0` and the job ID.
ORIN flips exactly those rows to `shipped` and writes `batch` + `implementation_date`. A handle not reported stays `pending`.

## One flag for Mike

The three Pirma / Cruz Azul pages are the first of both a new brand and a new club, and their live source copy is
**193 to 198 characters** against a 450-520 word band. That is the thinnest source-to-band ratio the programme has run
(Batch 15.1 measured 381 to 917 characters against a 280-340 band). The briefs reach band from club facts and the
customization/shipping facts, both inside a deliberately tight claims bar, with no Pirma heritage and no invented
fabric technology. Worth a closer read than the six adidas rows on that basis alone.
