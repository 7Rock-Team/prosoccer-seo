# Handoff: GSC analysis continuation and registry backfill (2026-08-14)

_For a fresh session. Read this, then `CLAUDE.md`, `SEO_BATCH_PROCESS.md`, `context/workforce-conventions.md`. Everything below is scoped and approved by Mike; nothing here needs re-litigating._

## State of play

- **C-FIX is BUILT and HELD, not imported.** 12 rows, meta-only, at `deliverables/page-optimizations/2026-08-14_cfix/`. Files: the retarget document, `ProSoccer_SEO_CFIX_12_Products.xlsx` (primary) and `.csv` (fallback). Mike is holding it pending the GSC re-triage, which will likely cut the list. Do not import it. Do not push it.
- **Batch 15 is HELD at the selection gate**, 8 SKUs proposed, live-verified, with row 6 upgraded to `adidas predator elite ag` (590/mo).
- Working tree committed this session (see the commit at the end of this file). Nothing pushed.
- `products-master.csv` is now 148 rows: 3 superseded duplicates deleted, 16 statuses corrected.

## Data already on disk, do not re-pull

All in the session scratchpad (path in the commit message; if it is gone, the pulls must be re-run):

| File | Contents |
|---|---|
| `inspect_results.jsonl` | 142 rows, URL Inspection: lastCrawlTime, coverageState, verdict, googleCanonical, userCanonical, userCanonicalIsSelf |
| `perf_pages.jsonl` | 1,551 rows, per-page impressions/clicks/position/ctr across 12 windows |
| `perf_queries.jsonl` | 129 rows, page+query. **TRUNCATED, unusable**, the call hit the 25,000-row site-wide cap |
| `perf_allqueries.jsonl` | 22,587 rows, site-wide query totals 2026-07-17 to 2026-08-14 |
| `optimized_group.json` | 101 optimized pages with **verified** batch + import date |
| `control_group.json` | 101 matched controls, category + brand + tier, all exact |
| `analyse_perf.py`, `crawl_analysis.py`, `build_control.py` | the analysis scripts |

## Settled findings, carry forward, do not redo

1. **Crawl staleness is ruled out.** All 142 pages crawled 2026-07-19 to 2026-08-15; 134 of 142 crawled on or after 2026-08-04, the latest B5-B12 import. Performance reads on B5 through B12 are valid.
2. **B-TECH-01 is ruled out as a performance explanation.** 72 of 142 pages declare a `userCanonical` pointing at a different page, but **all 142** return verdict PASS, "Submitted and indexed", and `googleCanonical` equal to their own URL. Google overrides the bad declaration everywhere. Still worth fixing as signal hygiene; it is not why anything is flat. This corrects the original IH4577 attribution in the B-TECH-01 backlog item.
3. **Impressions show no resolvable effect.** Primary set B5-B9, 14-day windows: optimized -58.8%, control -43.5%, difference -15.3 pts. Paired test 12 of 24, a coin flip. Aggregate is dominated by B6 (55% of pre-impressions) and reverses sign against the per-batch view, where optimized beat control in 5 of 8 batches.
4. **CTR is the better metric and it is directionally positive.** Verified 2026-08-14:
   - optimized 0.3915% to 0.5253%, **+34.2% relative**
   - control 0.4874% to 0.5651%, **+15.9% relative**
   - gap **+18.2 pts**. Counterfactual: at the control's improvement rate the optimized set earns **71.7** clicks against **83** actual, an excess of **+11.3 clicks at 1.3 sigma** (Poisson).
   - Directionally positive, not significant. This is the metric meta work actually targets, and it moves on a weeks timescale where impressions move on months.

## THE B6 HYPOTHESIS WAS TESTED AND DOES NOT HOLD

Mike's hypothesis: B6's -78.9% against a -8.2% control is a matching artifact, because B6's optimized pages are national-team jerseys (post-tournament cliff) while its controls are club jerseys (no cliff).

**Checked. The composition is actually well matched:**

- B6 optimized: 4 national team (DR Congo x2, Korea, Jamaica), 1 club (Chelsea youth), 5 footwear
- B6 control: 4 national team (Argentina, Netherlands, Guatemala, El Salvador), 1 club (Club America youth), 5 footwear

Near-identical. **National-versus-club is not the explanation.** Do not "fix" the matching on that axis and assume B6 resolves.

**A refinement that IS worth testing:** the two national-team sets differ in tournament trajectory, not in category. Optimized carries DR Congo, Korea and Jamaica, all early exits or non-qualifiers. Control carries Argentina and Netherlands, deep-run sides whose kit demand persists long after a minnow's collapses. If the cliff is real it is a *trajectory* effect inside the national-team category, not a national-versus-club effect. Test it before building matching around it, and note the sample is 4 pages against 4.

## Work to do, in order

### 1. Commit is already done. Do not push.

### 2. CTR as the primary metric
Recompute CTR per batch and paired (each optimized page against its own matched control, same windows), with impressions reported only as context. The aggregate CTR figures above are verified; the per-batch and paired CTR views are not yet built. Per-batch CTR is already printed by `ctr_b6.py` but is unstable on tiny click counts, so report confidence honestly and suppress any cell built on fewer than about 10 clicks.

### 3. Rebuild the control group
Two additions to `build_control.py`, keeping the existing category + brand + tier keys:
- **baseline impression band.** The current control is badly mismatched on exposure: 47 of 51 optimized pages had pre-window impressions against only 25 of 51 controls. Half the control earns nothing, so percentage changes sit on unstable bases. Match within a band (for example same order of magnitude of pre-window impressions).
- **national-team versus club versus footwear** as an explicit key, and record tournament trajectory for national-team pages so the B6 refinement above can be tested.

### 4. Re-run at 28 and 56 days post-import
28 days is available for B5 through B8 now; B9 reaches 28 days on 2026-08-28. 56 days is available for B5 and B6 now. Equal window length across batches matters more than window length, so run each horizon as its own comparison rather than mixing.

### 5. Orphaned-incumbent baseline (Batch 15's baseline)
`perf_allqueries.jsonl` holds 22,587 site-wide query rows for 2026-07-17 to 2026-08-14. Join the orphaned incumbent terms against it. **Only 8 of the roughly 28 incumbents have live-verified URLs**, the 8 in the Batch 15 proposal; the rest rest on a sitemap handle match that proved wrong about a quarter of the time. Report query-level earnings for the terms, and page-level earnings only for the 8 verified URLs. Do not attach earnings to unverified URLs.

### 6. Registry backfill, 101 rows
Add `batch` and populate `implementation_date` in `products-master.csv` from `optimized_group.json`, which carries the **verified** mapping:

| Cohort | Batch | Imported |
|---|---|---|
| 2026-06-30_session-01 | B5 | 2026-07-02 |
| 2026-07-08_session-01 | B6 | 2026-07-10 |
| 2026-07-11_session-01 | B7 | 2026-07-13 |
| 2026-07-13_session-01 | B8 | 2026-07-13 |
| 2026-07-21_session-01 | B9 | 2026-07-31 |
| 2026-07-31_session-01 | B10 | 2026-08-03 |
| 2026-08-03_session-01 | B11 | 2026-08-03 |
| 2026-08-03_session-02 | B12 | 2026-08-04 |
| 2026-08-04_session-01 | B13 | 2026-08-13 |
| 2026-08-13_session-01 | B14 | 2026-08-14 |

Verification already done: B9's ten SKUs land in `2026-07-21_session-01` and B10's in `2026-07-31_session-01`, each with one apparent spillover that is entirely the YF3F3V9 non-unique-SKU artifact (Junior in B9, Kid's in B10; `work-log/follow-ups.md` item 60). The remaining 41 rows are pre-B5 manual work with no Matrixify record: leave `implementation_date` blank, do not infer one from `brief_date`.

`implementation_date` is the field this whole analysis needed and it was 0 of 142 populated. The Step 2 rule codified in `SEO_BATCH_PROCESS.md` step 15 now flips `status` on confirmed import; it should populate `implementation_date` in the same step. Codify that when the backfill lands.

### Explicitly OUT of scope
- The primaries-versus-other-queries re-pull. Mike's call: 200 more calls to learn which queries moved, on a corpus producing about three clicks per page per fortnight, is not worth the quota yet.
- B-EXEMPLAR-02 fixes. Approved in principle, waiting on the GSC report. Spec is in the backlog item.

## WHAT NOT TO DO

1. **Do not import C-FIX or push anything.** Both are Mike's call, every time.
2. **Do not trust the aggregate impression figures as an effect estimate.** One batch is 55% of the sample and the aggregate reverses the per-batch sign.
3. **Do not use `perf_queries.jsonl`.** It is truncated at the API cap and only 129 rows survived filtering.
4. **Do not rebuild the control on national-versus-club alone.** That hypothesis was tested and rejected; see above.
5. **Do not infer import dates from `brief_date`.** Batch 9's gap is ten days. Batches 1 to 4 have no record at all.
6. **Do not report a self-measured number.** Re-derive from the scripts. The subagent self-reports in this session were verified against the raw files and agreed, but that verification is why they can be trusted.
