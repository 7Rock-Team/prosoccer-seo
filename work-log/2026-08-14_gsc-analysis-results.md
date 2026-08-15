# GSC analysis results: registry backfill, B6 test, orphaned-incumbent baseline (2026-08-14)

_Continuation of `2026-08-14_gsc-analysis-handoff.md`. Three items, in the priority order Mike set. Every figure below is re-derived from the raw files on disk, not carried over from a prior report._

Scripts are in the session scratchpad: `backfill.py`, `verify.py`, `b6_traj.py`, `b6_decomp.py`, `concentration.py`, `ctr_check.py`, `orphan_baseline.py`, `orphan_headroom.py`.

---

## 1. Registry backfill: DONE, 101 rows

`deliverables/tracking/products-master.csv` now carries a `batch` column and a populated `implementation_date`, both sourced from the verified mapping in `optimized_group.json`.

- 148 rows total. **101 backfilled, 47 left blank.**
- The join was exact: 101 of 101 source rows matched a registry row on URL, no duplicates on either side, nothing unmatched.
- Column inserted before `implementation_date`. Row order preserved.

**Verification (`verify.py`), all four checks pass:**

| Check | Result |
|---|---|
| Column set | exactly one column added, `batch`; none lost |
| Non-target field drift | **0** fields changed across 148 rows x 32 columns |
| Provenance | 101 of 101 values match `optimized_group.json` exactly; 0 unsourced values |
| Blank rows | 47, all with both fields blank, none with one populated |

A no-op CSV round-trip was run first and reproduced the file byte-for-byte, so the diff contains only the intended change.

**The 47 blanks are clean.** Their `brief_date` runs 2026-05-26 to 2026-06-17; the earliest backfilled row is 2026-06-30. The two sets do not overlap, which independently confirms the blanks are the pre-B5 manual work rather than rows the join missed.

Per-batch counts: B5 **11**, B6 through B14 10 each. B5 genuinely holds eleven pages (five Copa Pure IV, two Bosnia, two Croatia, two Nike), not a duplicate artifact.

**Note:** the handoff said 41 pre-B5 rows; the actual figure is 47. The handoff's number predates the removal of 3 superseded duplicates and was computed against the 142-page inspect set rather than the 148-row registry. Nothing is missing.

### Codified

The handoff asked that step 15 populate `implementation_date` once the backfill landed. Done in three places:

- `SEO_BATCH_PROCESS.md` step 15 row and the step 15 rule block: the status flip now also writes `batch` and `implementation_date`, from the same confirmation event.
- `STEP_2_BRIEFING.md`: Step 2 must report the batch label and the import date, not just the handle list.
- `.claude/agents/master-strategist/agent.md`: both fields documented in the `products-master.csv` schema, which was also stale (it omitted the seven keyword columns and still claimed `product_id` holds a numeric Shopify ID).

The brief-to-import gap, measured across B5 to B14, runs **0 to 10 days** (B9 ten, B13 nine, B10 three, four batches at 0 to 1). That range is the reason the date cannot be inferred from `brief_date` and is now recorded in the rule.

---

## 2. B6 trajectory test: HYPOTHESIS NOT SUPPORTED

The refinement was that post-tournament decay tracks tournament trajectory (early exit vs deep run) rather than category. **It does not.** But the test found the actual cause, and it is more consequential than either hypothesis.

### The trajectory label does not predict the outcome

B6_pre to B6_post, the window the -78.9% came from:

| Page | Group | Trajectory (per handoff) | Pre | Post | Change |
|---|---|---|---|---|---|
| DR Congo away | optimized | early / non-qual | 8,583 | 405 | **-95.3%** |
| DR Congo home | optimized | early / non-qual | 10,351 | 465 | **-95.5%** |
| Jamaica | optimized | early / non-qual | 417 | 255 | -38.8% |
| Korea | optimized | early / non-qual | 596 | 878 | **+47.3%** |
| Argentina | control | deep run | 5,614 | 5,429 | -3.3% |
| Guatemala | control | unlabelled | 385 | 117 | -69.6% |
| El Salvador | control | unlabelled | 153 | 84 | -45.1% |
| Netherlands | control | deep run | - | - | no post data |

Korea is an early exit and went **up 47%**. Jamaica is an early exit and fell less (-38.8%) than control Guatemala did (-69.6%). The label sorts the pages no better than chance once DR Congo is set aside.

I could not source the 2026 World Cup results myself (the tournament postdates my knowledge cutoff), so trajectory labels are taken verbatim from the handoff. Guatemala and El Salvador were unlabelled there and are left unlabelled here rather than guessed.

### What actually drives B6: two pages

DR Congo home and away are **89.8% of B6's optimized pre-window impressions.**

| B6 optimized | Pre | Post | Change | vs control |
|---|---|---|---|---|
| All 10 pages | 21,083 | 4,445 | **-78.9%** | gap **-71.1 pts** |
| Excluding DR Congo x2 | 2,149 | 3,575 | **+66.4%** | gap **+74.2 pts** |

Removing two of ten pages moves B6 from catastrophic to strongly positive, and flips the gap by 145 points.

### The mechanism is peak timing, not trajectory

Every national-team page in this set follows the same spike-and-decay curve and loses 85-99% from its own peak. What differs is **where the peak sits relative to the import date**, which decides what the pre and post windows happen to catch.

- DR Congo away peaks at the earliest observed window (10,489) and decays to 67. **-99.4% from peak.**
- Argentina peaks two windows later (7,489) and decays to 326. **-95.6% from peak.**

Argentina collapsed just as hard. It peaked later, so B6's post window caught it still near plateau (-3.3%) instead of on the way down. The control did not hold up because it was better matched; it held up because its clock was offset.

Both pages are real traffic, not a data artifact: position degrades smoothly (7.6 to 13.7 for DR Congo, 7.2 to 9.3 for Argentina) as impressions fall, and clicks track.

### This is systemic, not a B6 quirk

The single largest page in each batch/group cell carries **26% to 100%** of that cell's pre-window impressions (median ~60%). Removing just the top page swings the cell result by tens of points in almost every case: B6 control by -38 pts, B8 optimized by +49, B7 optimized by +47, B12 optimized by +40. B8's control cell is one page.

On the full primary set B5-B9, the two DR Congo pages alone are **49.4%** of optimized pre-window impressions:

| B5-B9 | Optimized | Control | Gap |
|---|---|---|---|
| As reported | -59.0% | -43.3% | **-15.7 pts** |
| Excluding DR Congo x2 | -23.4% | -43.3% | **+19.9 pts** |

### The CTR finding does not survive this either

This is the part that changes what can be reported. I reproduced the handoff's CTR figures exactly (optimized 0.3915% to 0.5253% = +34.2%; control 0.4874% to 0.5651% = +15.9%; gap +18.2 pts; 71.7 expected vs 83 actual clicks at 1.33 sigma), which confirms the pipeline matches. Then:

| B5-B9 CTR | Optimized rel | Control rel | Gap | Excess clicks |
|---|---|---|---|---|
| As reported | +34.2% | +15.9% | **+18.2 pts** | +11.3 (1.33 sigma) |
| Excluding DR Congo x2 | **-4.8%** | +15.9% | **-20.8 pts** | -14.4 (-1.60 sigma) |
| Excluding all 8 B6 national-team pages | -7.7% | +11.6% | **-19.3 pts** | -10.9 (-1.37 sigma) |

**The sign flips on two pages out of 51.** And the mechanism is mechanical rather than earned: DR Congo away went from 0.48% CTR at 8,583 impressions to 0.99% CTR at 405 impressions. The page did not get better; the low-intent impression flood receded, leaving a higher-converting remainder. Argentina shows the same effect more starkly, 0.02% to 1.53%.

**Recommendation: do not report the +34.2% CTR improvement to Mike or Tony as evidence the work is paying off.** It is not "directionally positive, not significant" as the handoff recorded. It is not robust to the removal of two pages, and it reverses. Neither impressions nor CTR can currently detect an optimization effect in either direction on this corpus.

### What this means for the control rebuild (handoff item 3, still parked)

The result changes that item's spec. The handoff proposed matching on a baseline impression band plus a national/club/footwear key. The band is directionally right but insufficient, and the national/club key is now doubly ruled out.

Matching on pre-window impression **level** does not help when the real variable is **phase**: DR Congo and Argentina had comparable magnitudes and opposite measured outcomes purely because one was past peak and the other was not. Any rebuild needs to match on position within the page's own demand curve, or exclude spike pages from the measured set. Otherwise the trimmed-mean or median-of-per-page-changes route avoids the problem entirely and is probably cheaper than rebuilding matching at all.

---

## 3. Orphaned-incumbent baseline: Batch 15 decision input

Source: `perf_allqueries.jsonl`, 22,587 site-wide query rows, 2026-07-17 to 2026-08-14 (29 days). Site totals for context: 1,972,622 impressions, 16,808 clicks.

**A scope correction first.** The handoff asked for page-level earnings on the 8 live-verified URLs. **That data does not exist on disk.** `perf_allqueries.jsonl` has no page dimension at all (see `perf_proc.py` allqueries mode), and `perf_pages.jsonl` covers only the 159 optimized-plus-control URLs, none of which are orphaned incumbents. Getting page-level figures for them requires a new GSC pull. This baseline is therefore query-level only, which is the part the handoff scoped as reportable anyway.

Separately: **the 8-SKU Batch 15 proposal was never written to disk.** It exists only in the prior session's conversation. I worked from the 19-term queue in `2026-08-14_batch15-handoff.md` plus the row-6 upgrade recorded in the C-FIX document, and did not reconstruct a selection, since guessing which 8 were chosen is precisely the handle-inference failure the process forbids. If Batch 15 proceeds, that proposal needs re-recording.

### What the whole queue earns

All 20 terms (19 queued plus the row-6 upgrade), clustered to catch variants and surface synonyms:

| | Impressions | Clicks | Distinct queries |
|---|---|---|---|
| Entire orphaned queue, 29 days | **643** | **37** | 56 |
| Share of site | 0.033% | 0.22% | |
| Per page, if 8 pages briefed | ~80 | ~4.6 | |

**Three terms earn literally nothing** in 29 days: `adidas predator elite fold over tongue ag` (70/mo claimed), `adidas f50 pro indoor` (20/mo), `adidas f50 club mid fg mg` (10/mo).

Top earners: `nike phantom 6 high elite fg` 133i/7c, `nike vapor 17 elite fg` 63i/2c, `nike phantom 6 low pro turf` 61i/5c, `nike tiempo ligera pro turf` 49i/4c, `adidas predator elite ag` 49i/9c.

### Headroom exists, but the base is small

Impression-weighted average position across the queue is **7.5**. Only 11% of impressions rank top-3; 70% sit at 4-10 and 19% at 11-20. So there is real ranking headroom, and moving 7.5 to 3 would meaningfully raise CTR. The problem is the base it multiplies: 643 impressions.

The claimed DFS volume across the queue is ~1,800/mo, or ~1,717 searches in the 29-day window. GSC shows 643 impressions, so ProSoccer appears for roughly **37% of the claimed demand** and is absent from the other 63%. That absent share is genuine upside, but it is upside that requires ranking where the site currently does not appear at all, which a meta-and-body optimization may not deliver on its own.

**Limitation, stated plainly:** GSC only records queries where the site actually appeared. Demand ProSoccer never surfaces for is invisible here by construction, so 643 is a floor on the opportunity, not a measure of it. The DFS volumes remain the better estimate of total demand; this is the better estimate of what is currently reachable.

### Comparison, from the same corpus

| Cluster | Queries | Impressions | Clicks | Weighted pos |
|---|---|---|---|---|
| **Entire orphaned queue (Batch 15)** | 56 | **643** | 37 | 7.5 |
| `f50 hyperfast` (B-KW-01, nobody holds it) | 87 | **4,471** | 34 | 7.7 |
| tiempo, all | 173 | 44,561 | 120 | 10.2 |
| predator, all | 425 | 39,582 | 149 | 8.6 |
| f50, all | 422 | 28,365 | 178 | 7.6 |
| phantom, all | 422 | 16,193 | 291 | 8.0 |

`f50 hyperfast` alone is **7x the impressions of the entire 20-term Batch 15 queue**, at a comparable average position, and B-KW-01 already records that nobody holds it.

### The read

B-STRAT-01's strategic premise survives: optimizing incumbents that hold demand beats optimizing new pack SKUs that hold none. The queue that premise produced is the weak part. It was ranked by DFS volume, and DFS volume on these long-tail configuration terms does not convert into ProSoccer impressions at anything like the implied rate.

Batch 15 as specified would spend ten briefs to compete harder for a pool earning 37 clicks per 29 days. That is not nothing, and the pages are cheap to do, but B-KW-01's hyperfast finding is sitting in the same backlog at seven times the reachable volume and is currently unowned.

**This is Mike's call, not mine.** The three options: run Batch 15 as specified; re-rank the queue by GSC-measured impressions rather than DFS volume (which would reorder it substantially and drop the three zero-earning terms); or route the batch at B-KW-01 instead. My recommendation is the second or third, but the decision has real arguments on each side and the analysis above is the input, not the answer.

---

## Carried forward

- **C-FIX stays held and unimported. Nothing pushed.** Local commit only.
- Handoff items 2 (per-batch and paired CTR) and 4 (28/56-day re-runs) remain open. Item 2 should be reconsidered in light of section 2: per-batch CTR on cells this concentrated will be as fragile as the aggregate, and the honest fix is a per-page paired view with spike pages excluded, not a finer slice of the same weighted average.
- Item 3 (control rebuild) still parked, with a revised spec (see section 2).
- **New:** the Batch 15 8-SKU proposal is not on disk and needs re-recording before that batch can proceed.
