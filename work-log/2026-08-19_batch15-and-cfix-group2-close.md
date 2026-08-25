# Batch 15 and C-FIX Group 2 close (imported 2026-08-19)

**Status: VERIFIED.** All ten Batch 15 pages and all three C-FIX Group 2 pages are confirmed live in the store, carrying the copy we authored.

## Import record (Matrixify job history, supplied by Mike, not inferred)

| Job | Time | What | Result |
|---|---|---|---|
| #729757812 | 2026-08-19 17:34 | C-FIX Group 2 import | **3 updated, 0 created**, Finished |
| #729760969 | 2026-08-19 17:42 | Batch 15 export | 10 exported |
| #729762205 | 2026-08-19 17:46 | Batch 15 import | **10 updated, 0 created**, Finished |

The export sitting between the two imports confirms the intended sequence: C-FIX Group 2 landed first, freeing the terms, and the Batch 15 export was then taken against the post-C-FIX store.

**Zero Created on both jobs is the check that matters most here.** Every handle matched an existing product, so nothing was accidentally created as a new product by a mistyped or reconstructed handle. That is the failure mode the "handles always come from the briefs" rule exists to prevent, and this is the first time we have positive evidence it held rather than an absence of complaints.

## Verification method: live fetch, not a report

All 13 pages were fetched and their live `<title>` compared against the meta title each brief or the import file specified. **10 of 10 Batch 15 and 3 of 3 Group 2 carry our authored string.** A page counted as landed only on that evidence, per the step 15 rule that a handle not confirmed stays `pending`. Nothing was taken on trust, and nothing stayed pending.

## The ten Batch 15 SKUs

| SKU | Primary | Vol/mo | Meta Title |
|---|---|---|---|
| HQ3158-001 | nike tiempo ligera pro fg | 140 | Nike Tiempo Ligera Pro FG Soccer Cleats |
| HJ2147-003 | nike phantom 6 high elite fg | 210 | Nike Phantom 6 High Elite FG Shadow Pack |
| JR8971 | adidas f50 league indoor | 30 | adidas F50 League Indoor Born For Goals |
| JR5899 | adidas predator elite ag | 590 | adidas Predator Elite AG Born For Goals |
| IB4477-101 | nike tiempo ligera pro turf break em | sub-floor | Nike Tiempo Ligera Pro Turf Break 'Em |
| IQ2399-900 | nike phantom 6 low academy turf breakout | sub-floor | Nike Phantom 6 Low Academy Turf Breakout |
| IB3094-800 | nike phantom 6 low pro fg erling haaland | sub-floor | Nike Phantom 6 Low Pro FG Haaland Pack |
| IF8508-600 | nike vapor 17 elite fg break em | sub-floor | Nike Vapor 17 Elite FG Break 'Em |
| JH7718 | adidas f50 league indoor coral blaze | sub-floor | adidas F50 League Indoor Coral Blaze |
| IQ2162-900 | nike phantom 6 high club fg mg | 10 | Nike Phantom 6 High Club FG/MG Breakout |

Five carry pack-qualified sub-floor primaries by design, which is what pack succession requires when a live sibling already holds the unqualified term. This is the first batch selected by **measured GSC impressions** rather than DFS volume, and the first composed entirely of unoptimized incumbents rather than new pack releases.

## The three C-FIX Group 2 SKUs

| SKU | Primary before | Primary after |
|---|---|---|
| IH1779-900 | nike phantom 6 elite fg (cut-less) | nike phantom 6 high elite fg breakout |
| IQ1886-900 | nike phantom 6 pro (cut-less and surface-less, 880/mo) | **nike phantom 6 low pro fg** (70/mo) |
| HP9971 | adidas predator elite ag (590/mo) | adidas predator elite fold over tongue ag road to glory |

**IQ1886-900's row deliberately differs from what the original C-FIX document proposed.** That document, written under the old season-earliest incumbency rule, assigned it the pack-qualified `nike phantom 6 low pro fg breakout`. Under the v3 rule Mike made on 2026-08-18, incumbency follows measured demand, and IQ1886-900 is the measured incumbent at that configuration (523 impressions against the runner-up's 363). It therefore keeps the unqualified term, and Batch 15's IB3094-800 took the pack-qualified form instead. The reason is written into the registry row's `notes` so the divergence is not later read as an error. The import file needed no change: its meta title reads correctly under either primary.

`nike phantom 6 pro` (880/mo) is released by this change and no PDP claims it. It is cut-less and surface-less, so it is not PDP-valid; it belongs to `/collections/nike-phantom`, which is live and unoptimized. Logged in B-KW-01 with the other four unowned collection terms.

## Registry state after the write-back

| | Before | After |
|---|---|---|
| Rows | 148 | **158** |
| Batched rows (B5 to B15) | 101 | **111** |
| `shipped` | 142 | **154** |
| `pending` | 6 | **4** |

The ten Batch 15 rows are **appends, not updates**: these pages were unregistered orphaned incumbents, which is exactly why the batch targeted them. Per-batch tally is now B5=11, B6 through B15=10 each.

The four rows still `pending` are the B-IMP-01 set, and they are correctly pending: the Predator Accuracy Crazyrush page and the three Mexico 2026 Stadium jerseys, all briefed but never imported, all failing current meta rules, queued for a re-run rather than a re-import.

### Write-back verification

| Check | Result |
|---|---|
| Row count | 148 to 158, exactly +10 |
| Column set | 35 columns, unchanged |
| Untouched rows | 135 compared, **zero field drift** |
| Duplicate URLs | 0 |
| Duplicate primaries across the registry | 0 |
| All 13 rows carry `implementation_date` 2026-08-19 | yes |
| IQ1886-900 reflects the v3 ruling, not the C-FIX proposal | confirmed, with the reason in `notes` |

## Other tracking files

**`ceded-terms.csv`: confirmed current, no change.** Regenerating it from `collections-master.csv` reproduces the committed file byte-for-byte (39 rows: 15 preserved non-collection cedes, 24 derived collection cedes). Neither import touched `collections-master.csv`, so no cede moved. That is the expected result, and it was verified rather than assumed.

**One footgun found in `scripts/build_ceded_terms.py`:** running it without `--date` silently rewrites every derived row's date to a hardcoded default of 2026-07-31, which would have regressed 24 rows from their real 2026-08-03 recording date. The content was identical; only the date column moved. Logged to follow-ups. The script should default to the existing file's date or refuse to run without `--date`, the same posture the gate now takes on a check that cannot run.

## Gate and checks at close

`batch_gate.py` exit 0 over the ten briefs, all 15 checks run, none skipped, cross-batch cannibalization on against 148 registry primaries. `voice_check.py` clean on all ten. Layer 3 claim check clean. Run log at `deliverables/page-optimizations/2026-08-18_session-01/_gate-run.json`.

## What this batch is a test of

Batch 15 is the first batch selected on measured GSC impressions rather than DFS volume, and the first drawn entirely from unoptimized incumbents. Two open items depend on how it performs:

- **B-COPY-02** designates Batch 15.1 as the controlled test of whether word bands hold on thin-source pages under the same dispatch discipline. Batch 15's ten all landed strictly in band with self-report drift of 2 words, against Batch 14's zero-of-ten-in-the-lower-half. Source richness and dispatch design changed together here, so this batch cannot separate them.
- **B-COLL-05** records the collection arithmetic these pages surfaced, and the constraint on it: the terms convert at 0.24% CTR against the optimized corpus's 0.64%, so the case rests on reachable headroom rather than impressions already earned.

Re-measure Batch 15 at 28 and 56 days post-import (2026-09-16 and 2026-10-14).
