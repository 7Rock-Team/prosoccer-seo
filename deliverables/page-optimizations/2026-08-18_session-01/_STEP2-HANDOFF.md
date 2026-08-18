# Batch 15: Step 2 handoff block

**Batch:** 15 | **Session:** `deliverables/page-optimizations/2026-08-18_session-01/`
**Handed off:** 2026-08-18 | **Gate:** PASS, exit 0, no skipped checks | **Layer 3:** clean

Paste this block at the top of a fresh Step 2 chat, followed by the ten briefs.

---

## 1. Paste-ready handle list (Matrixify export filter)

```
nike-tiempo-ligera-pro-firm-ground-soccer-cleats-su26,nike-phantom-6-high-elite-firm-ground-soccer-cleats-shadow-pack-fa25,adidas-f50-league-indoor-soccer-shoes-born-for-goals-pack-sp26,adidas-predator-elite-fold-over-tongue-artificial-grass-soccer-cleats-born-for-goals-pack-sp26,nike-tiempo-ligera-pro-turf-soccer-shoes-break-em-pack-fa26,nike-phantom-6-low-academy-turf-soccer-shoes-breakout-pack-su26,nike-phantom-6-low-pro-firm-ground-soccer-cleats-erling-haaland-pack-fa25,nike-vapor-17-elite-firm-ground-soccer-cleats-break-em-pack,adidas-f50-league-indoor-soccer-shoes-coral-blaze-pack-fa25,nike-phantom-6-high-club-firm-multi-ground-soccer-cleats-breakout-pack-su26
```

Ten handles. Every one verified present in the live product sitemap (14,402 products, fetched 2026-08-16), not reconstructed from a product title. Confirm the Matrixify export summary reads **10 products** before proceeding.

## 2. The ten rows

| # | SKU | Handle | Primary keyword | Body words (band) |
|---|---|---|---|---|
| 1 | HQ3158-001 | `nike-tiempo-ligera-pro-firm-ground-soccer-cleats-su26` | nike tiempo ligera pro fg | 389 (340-390) |
| 2 | HJ2147-003 | `nike-phantom-6-high-elite-firm-ground-soccer-cleats-shadow-pack-fa25` | nike phantom 6 high elite fg | 439 (400-450) |
| 3 | JR8971 | `adidas-f50-league-indoor-soccer-shoes-born-for-goals-pack-sp26` | adidas f50 league indoor | 328 (280-340) |
| 4 | JR5899 | `adidas-predator-elite-fold-over-tongue-artificial-grass-soccer-cleats-born-for-goals-pack-sp26` | adidas predator elite ag | 439 (400-450) |
| 5 | IB4477-101 | `nike-tiempo-ligera-pro-turf-soccer-shoes-break-em-pack-fa26` | nike tiempo ligera pro turf break em | 379 (340-390) |
| 6 | IQ2399-900 | `nike-phantom-6-low-academy-turf-soccer-shoes-breakout-pack-su26` | nike phantom 6 low academy turf breakout | 334 (280-340) |
| 7 | IB3094-800 | `nike-phantom-6-low-pro-firm-ground-soccer-cleats-erling-haaland-pack-fa25` | nike phantom 6 low pro fg erling haaland | 386 (340-390) |
| 8 | IF8508-600 | `nike-vapor-17-elite-firm-ground-soccer-cleats-break-em-pack` | nike vapor 17 elite fg break em | 430 (400-450) |
| 9 | JH7718 | `adidas-f50-league-indoor-soccer-shoes-coral-blaze-pack-fa25` | adidas f50 league indoor coral blaze | 333 (280-340) |
| 10 | IQ2162-900 | `nike-phantom-6-high-club-firm-multi-ground-soccer-cleats-breakout-pack-su26` | nike phantom 6 high club fg mg | 339 (280-340) |

All ten land **strictly inside** their tier band, none drawing on the +/-15 tolerance. Word counts are re-derived by ORIN from `batch_gate.body_word_count`, not taken from any agent's self-report.

## 3. Meta field pre-check (Step 2 should re-verify, not trust this)

| SKU | Meta Title | chars | Meta Desc chars |
|---|---|---|---|
| HQ3158-001 | Nike Tiempo Ligera Pro FG Soccer Cleats | 39 | 152 |
| HJ2147-003 | Nike Phantom 6 High Elite FG Shadow Pack | 40 | 142 |
| JR8971 | adidas F50 League Indoor Born For Goals | 39 | 143 |
| JR5899 | adidas Predator Elite AG Born For Goals | 39 | 139 |
| IB4477-101 | Nike Tiempo Ligera Pro Turf Break 'Em | 37 | 144 |
| IQ2399-900 | Nike Phantom 6 Low Academy Turf Breakout | 40 | 153 |
| IB3094-800 | Nike Phantom 6 Low Pro FG Haaland Pack | 38 | 145 |
| IF8508-600 | Nike Vapor 17 Elite FG Break 'Em | 32 | 139 |
| JH7718 | adidas F50 League Indoor Coral Blaze | 36 | 141 |
| IQ2162-900 | Nike Phantom 6 High Club FG/MG Breakout | 39 | 158 |

Every title at or under the 48-character cap, no manufacturer-brand pipe suffix, `adidas` lowercase. Every description inside 120 to 160 with no colon-fragment opener.

## 4. Things Step 2 should know about this batch specifically

- **No URL handle changes are proposed.** Three briefs flag their handle as over the 70-character guideline (IB3094-800 at 73, IQ2162-900 at 75, JR5899 at 93) and all three explicitly recommend no change, because a rewrite needs a 301 coordinated with Misha. Ignore handle length; it is not a defect to fix in this import.
- **All ten pages are currently raw white-label.** Theme-fallback meta description on 10 of 10, zero in-body internal links on 10 of 10. Every brief adds two validated internal links. This is expected: these are unoptimized incumbents, which is why they were selected.
- **Five primaries are pack-qualified and sub-floor** (rows 5, 6, 7, 8, 9). That is mandatory under pack succession, not a research failure. Do not flag them as weak keywords.
- **Row 4 (JR5899) uses `Nanostrike+`, with the plus.** That is correct for the Elite tier and was resolved against adidas.com on 2026-08-18. League-tier pages use `Nanostrike` with no plus. If you see both forms across batches, that is the tier rule, not an inconsistency.
- **Rows 3 and 9 are the same shoe in two colorways.** Row 3 (Born For Goals) holds the unqualified term as the measured incumbent; row 9 (Coral Blaze) takes the pack-qualified form. Both should ship.

## 5. Dependency: C-FIX Group 2 imports FIRST

Three of these rows brief on primaries that C-FIX Group 2 releases. That import is built and validated at `deliverables/page-optimizations/2026-08-18_cfix-group2/` and is Mike's to run.

| Batch 15 row | Needs | Released by |
|---|---|---|
| 2 (HJ2147-003) | nike phantom 6 high elite fg | C-FIX Group 2 row 10 (IH1779-900) |
| 4 (JR5899) | adidas predator elite ag | C-FIX Group 2 row 12 (HP9971) |
| 7 (IB3094-800) | takes the pack-qualified form instead | see note below |

**Row 7 is not blocked, it is resolved the other way.** IQ1886-900 keeps `nike phantom 6 low pro fg` as the measured incumbent, so row 7 takes `nike phantom 6 low pro fg erling haaland`. The Group 2 import file is unchanged by that decision; only the registry row differs.

## 6. Step 15 write-back, when the import lands

Report back the handle list that actually imported, plus any failures or skips, **and the import date**. ORIN flips exactly those rows to `shipped` and writes `batch` = B15 and `implementation_date` from your report. A handle not reported stays `pending`.

Also apply at that point, from the C-FIX Group 2 import:

| SKU | `primary_keyword` becomes |
|---|---|
| IQ1886-900 | nike phantom 6 low pro fg |
| IH1779-900 | nike phantom 6 high elite fg breakout |
| HP9971 | adidas predator elite fold over tongue ag road to glory |

## 7. Verification already run (re-check anything you doubt; do not take this as evidence)

| Check | Result |
|---|---|
| `batch_gate.py`, 10 briefs | PASS, exit 0, **no skipped checks** |
| Cross-batch cannibalization | ran against 148 registry primaries, 0 collisions |
| Intra-batch duplicate primaries | 0 |
| `voice_check.py` | 10 of 10 passed |
| Layer 3 claim check | 10 clean, 0 unsourced claims |
| Word bands | 10 of 10 strictly in band |
| Handles | 10 of 10 present in the live sitemap |

Step 2's job is to read the briefs cold and catch what the workforce approved. This table is what ORIN measured, not a reason to skip your own checks.
