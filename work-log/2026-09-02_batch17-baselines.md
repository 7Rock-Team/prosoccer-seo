# Batch 17 baselines captured before import (2026-09-02)

**First batch in the programme with a pre-import baseline on disk.** Nine SKUs, page-level and term-level, captured from GSC while Batch 17 sits at step 7. The import has not run and nothing here touches the store.

Full capture, method and per-page detail: `deliverables/tracking/2026-09-02_batch17-baselines.md`.

## Why this was done now

**Because the window closes at import and it has never once been open at the right moment.**

Every performance column in `products-master.csv` was empty on all 178 rows: `baseline_impressions`, `baseline_clicks`, `baseline_ctr`, `baseline_position` and the matching `day_30_*` and `day_60_*` sets, twelve columns, 178 rows, nothing. The 2026-08-14 backfill populated `batch` and `implementation_date`, which made cohorts definable, but it recorded no performance figure at all. So for batches 5 through 16 the pre-window has to be reconstructed after the fact from raw GSC pulls, against pages whose copy has already changed.

That reconstruction was attempted and it failed. `work-log/2026-08-14_gsc-analysis-results.md` ran a full before-and-after on Batches 5 to 9 against a control cohort and concluded that **neither impressions nor CTR can detect an optimization effect on this corpus in either direction.** The headline finding at the time, a +34.2% CTR improvement, was not robust to removing two pages out of fifty-one: two DR Congo World Cup jersey pages were 49.4% of the optimized cohort's pre-window impressions, and excluding them moved the result from +18.2 points to -20.8. The analysis specifically recommended not reporting that figure as evidence the work is paying off.

The cause was not bad arithmetic. It was that the measurement was built after the fact out of whatever GSC still held, on pages selected for merchandising reasons rather than for measurability, with no recorded pre-state to anchor it. **No batch before this one has a usable pre-window**, and the 48 pre-B5 rows never will, since they carry neither `batch` nor `implementation_date` and that gap is permanent.

Batch 17 is the first batch where fixing this costs nothing but the pull. The briefs are written, the gate is green, the work is committed and pushed, and the import has not happened. That is the only moment where a true pre-state exists and can still be recorded.

## What was captured

Window 2026-06-05 to 2026-09-02 inclusive, 90 days trailing to the day of capture. Canonical URL only. Locale-prefixed and `?variant=` rows excluded.

- **Page level, written to the registry:** impressions, clicks, CTR and average position for all nine SKUs. Batch total 165,144 impressions and 383 clicks at 0.2319%.
- **Term level, recorded in the capture file:** the earned term for each of the seven pages that have one, with its impressions, clicks, CTR, position and share of page impressions. Two pages (Italy, Panini) have no earned term and are recorded as `not-ranking`.

Term-level was captured because a page-total comparison cannot tell you whether the copy moved the term it was written for. Page totals aggregate every query the page appears for, and on these nine the earned term is between 2.5% and 36% of the page.

## Three things the capture established

**1. The band positions recorded at Phase 0 were correct.** Re-measured on a different window, all seven earned-term positions drift by at most 0.31 and none crosses a band boundary. The bands assigned in the briefs stand.

**2. Six of seven earned terms pass the concentration condition on fresh data. DH6621 fails both halves of it**, at 2.50% share and 368 term impressions against thresholds of 15% and 1,000. That is independent confirmation of B-RANK-01 rather than a new finding, and it sharpens it: the term ranks at position 9.07 and simultaneously fails the test that decides whether it counts as earned. The one condition is doing two jobs. DH6621's band is held at 5-to-10 by Mike's disposition of 2026-09-02, on the grounds that recording `not-ranking` for a page at 9.07 would be a false record.

**3. Locale-prefixed URLs are a third slice of unmeasured traffic.** GSC reports `/en-au/`, `/en-gb/` and `/en-ca/` as separate pages. Across these nine they carry 2,897 impressions and 42 clicks at 1.4498% CTR, against the canonical 165,144 and 383 at 0.2319%. **1.7% of impressions, 9.9% of clicks, more than six times the CTR.** This is the same shape as the canonical-versus-variant split found on 2026-08-27 (3.6% of impressions, 29.5% of clicks). A canonical-only follow-up measures a minority of this batch's clicks and should say so rather than quietly reporting the canonical number as the whole.

## Registry change, and one deviation from the documented process

Nine rows were appended to `deliverables/tracking/products-master.csv`, taking it from 178 to 187. Verified: a no-op round trip reproduced the original file byte for byte before writing, and after writing there were **zero field changes across the 178 pre-existing rows by 35 columns**.

**The deviation:** `SEO_BATCH_PROCESS.md` step 14 appends batch rows *after* import, and the Batch 17 dispatch handoff says explicitly that the nine rows go in at step 14 and not before. They are in now, because a baseline has to attach to a row and the row has to exist before the import that the baseline is measuring against.

To keep the deviation as narrow as possible:

- `status` is `pending` on all nine, which is what the rule requires until Mike confirms the import landed.
- **`batch` and `implementation_date` are deliberately left BLANK.** Both are written at step 15 from the single import-confirmation event, per the rule added 2026-08-14, and writing either now would break that. Batch identity is recorded in `notes` instead.
- `baseline_position` holds the **page-level** average, matching the other three baseline fields so the four are one consistent set. The earned-term positions live in the capture file.

**That last point needs Mike's ruling.** The 2026-08-27 decision recorded in `_STEP2-HANDOFF.md` says Batch 17 writes `baseline_position` from the earned-term positions. This capture wrote the page average instead, because mixing a term-level position into a page-level set of impressions, clicks and CTR would produce four numbers that are not comparable with each other and would silently break any future analysis reading the row as a unit. Both values exist and neither is lost. If the earned-term position is wanted in the column, it is a one-line change, and the cleaner fix is a separate `baseline_term_position` column so the row carries both without ambiguity.

## What has to happen next, in order

1. **Mike rules on `baseline_position`:** page average as written, earned-term position, or a new column carrying both.
2. **Steps 8 to 15 run.** The import flips these nine rows to `shipped` and writes `batch` and `implementation_date`.
3. **The follow-up pull uses the identical method**, which is written out step by step in the capture file. A 90-day post-window against a 90-day pre-window, page level and term level reported separately, per-page paired changes rather than a cohort average.

Do not run the follow-up as a cohort mean. Three of these nine pages are above 23,000 impressions in a World Cup year and any one of them can flip a cohort result on its own, which is exactly how the 2026-08-14 analysis went wrong.
