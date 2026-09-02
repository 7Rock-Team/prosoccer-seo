# Batch 17 -- Step 2 handoff

**Session:** `deliverables/page-optimizations/2026-08-28_session-01`
**Batch:** 17. **Nine SKUs.** Colombia was pulled at candidate selection and deliberately NOT backfilled.
**Gate:** PASS, exit 0, 9 briefs, **16 checks run, 0 skipped, 0 findings.** See `_gate-run.json`.
**Registry 1:** present, 177 claimed primaries, cross-batch cannibalization ON.

## Paste-ready handle list for the Matrixify export filter

Handles come from the briefs and are never reconstructed from product titles.

```
umbro-2025-2026-guatemala-mens-home-soccer-jersey,adidas-2026-spain-mens-stadium-away-soccer-jersey,puma-2026-paraguay-mens-authentic-home-soccer-jersey,adidas-2026-italy-mens-authentic-home-soccer-jersey,nike-phantom-6-low-elite-firm-ground-soccer-cleats-erling-haaland-pack-fa25,adidas-2026-27-club-america-mens-authentic-home-soccer-jersey,nike-2026-27-usmnt-mens-stadium-home-shorts,panini-2026-fifa-world-cup-stickers-box-50-packs-each,nike-strike-sleeves-socks
```

Confirm the export summary reads **9 products**.

**One handle is deliberately not what the product is.** `nike-2026-27-usmnt-mens-stadium-home-shorts`
carries `2026-27`; the live title, H1 and `og:title` all read **2026**. The live title governs product
attributes, so the copy says 2026 and the handle is exported unchanged. Do not "correct" it in the
export filter or the import file, and do not reconstruct it from the title.

## The nine

| # | SKU | Handle | Primary | Body words | Band | Earned term | Term pos |
|---|---|---|---|---|---|---|---|
| 1 | UUM1GUAJ525101-U10 | `umbro-2025-2026-guatemala-mens-home-soccer-jersey` | `guatemala home jersey` | 461 | 400-470 | `guatemala soccer jersey` (CEDED) | 4.88 |
| 2 | JN4397 | `adidas-2026-spain-mens-stadium-away-soccer-jersey` | `spain jersey 2026` | 518 | 450-520 | `spain jersey 2026` | 5.50 |
| 3 | 783301-01 | `puma-2026-paraguay-mens-authentic-home-soccer-jersey` | `paraguay jersey` | 516 | 450-520 | `paraguay jersey` | 4.89 |
| 4 | JL6934 | `adidas-2026-italy-mens-authentic-home-soccer-jersey` | `italy authentic jersey` | 501 | 450-520 | none | not-ranking |
| 5 | HQ2332-800 | `nike-phantom-6-low-elite-firm-ground-soccer-cleats-erling-haaland-pack-fa25` | `haaland cleats` | 446 | 400-450 | `haaland cleats` | 6.08 |
| 6 | KB9024 | `adidas-2026-27-club-america-mens-authentic-home-soccer-jersey` | `america jersey 2026` | 497 | 450-520 | `america jersey 2026` | 3.50 |
| 7 | IB4855-410 | `nike-2026-27-usmnt-mens-stadium-home-shorts` | `usmnt shorts` | 351 | 300-360 | `usmnt shorts` | 10.57 |
| 8 | 20490-BOX | `panini-2026-fifa-world-cup-stickers-box-50-packs-each` | `panini sticker box` | 372 | 320-380 | none | not-ranking |
| 9 | DH6621 | `nike-strike-sleeves-socks` | `nike strike sleeves` | 292 | 240-300 | `nike sleeve socks` | 9.38 |

Word counts are `batch_gate.py`'s own `body_word_count` run against the written files, not a
self-report. Every one sits inside its base band, none is riding the tolerance line.

**Bands differ more than usual across this batch and that is deliberate.** Five jerseys at 450-520,
the Elite cleat at 400-450, and four SKU-specific bands set below them: Guatemala at 400-470 because
its source copy is the product title and nothing else, shorts at 300-360, the sticker box at 320-380
and the sleeves at 240-300. A band is set from the SKU's own tier and source depth, never inherited.

## Meta fields as written

| SKU | Meta Title | Len | Meta Description | Len |
|---|---|---|---|---|
| UUM1GUAJ525101-U10 | Umbro 2025-26 Guatemala Home Jersey | 35 | The Umbro Guatemala home jersey for 2025-2026 is the men's home kit, officially licensed. Pull on the crest for the next match and wear it after. | 145 |
| JN4397 | adidas Spain Jersey 2026 Stadium Away | 37 | The adidas Spain 2026 Stadium away jersey is the alternate shirt, cut slim in Climacool interlock. Add a name and number on this page. | 134 |
| 783301-01 | Puma 2026 Paraguay Authentic Home Jersey | 40 | Puma builds this Paraguay jersey to Pro fit, the on-pitch specification, with a Dobby main material and dryCELL moisture management. Shop the authentic. | 152 |
| JL6934 | adidas 2026 Italy Authentic Home Jersey | 39 | The Italy authentic jersey is built to the on-pitch spec, with a lenticular heat-transfer crest, a slim cut, and Climacool+ cooling. Add your name and number. | 158 |
| HQ2332-800 | Nike Phantom 6 Elite Haaland Cleats FG | 38 | The Nike Phantom 6 Low Elite runs blue at the heel and warms to red and yellow up front. Gripknit grips the ball wet or dry. Lace up for firm ground. | 149 |
| KB9024 | adidas Club America 2026 Authentic Jersey | 41 | The authentic America jersey for 2026-27 is adidas's on-pitch cut, slim fit with Climacool+ and Aeroready. Pull it on and back Las Águilas. | 139 |
| IB4855-410 | Nike 2026 USMNT Stadium Home Shorts | 35 | The 2026 USMNT home shorts finish the kit you started with the jersey. Nike Stadium replica details, Dri-FIT to keep you dry. Get the other half. | 145 |
| 20490-BOX | Panini 2026 World Cup Sticker Box, 50 Packs | 43 | The Panini 2026 World Cup sticker box holds 50 packs, 7 stickers each, 350 in all. Enough to fill real spreads in one sitting. Grab a box. | 138 |
| DH6621 | Nike Sleeve Socks, Strike Footless Sleeves | 42 | The Nike Strike Sleeves are footless soccer sleeve socks that pull on over your shin guard and hold it in place. Dri-FIT, in five colors and two sizes. | 151 |

All nine Meta Titles are under the 48-character cap and none ends with a manufacturer brand as a
pipe suffix. All nine Meta Descriptions are 120 to 160 characters, full sentences, no colon opener.

**Three Meta Titles are load-bearing and must not be reworded in the import file.** Spain, the
Haaland Phantom and the Strike Sleeves sit in the 5-to-10 ranking band, where the earned term must
be retained in exact-match form. `Spain Jersey 2026`, `Haaland Cleats` and `Nike Sleeve Socks` are
the strings that satisfy it.

**DH6621 was corrected on 2026-09-02, after the briefs were first committed.** It was recorded as
not-ranking against the assigned primary; it in fact ranks 9 and 10 across its sleeve/sock cluster
(6,152 impressions, 41.7% of the page). The Meta Title is now
`Nike Sleeve Socks, Strike Footless Sleeves`, leading with the earned term rather than repeating
the brand. It was `Nike Strike Sleeves, Shin Guard Sleeves` when the briefs were first committed.
Body copy, the shin-guard FAQ and the `/collections/shin-guards` link are unchanged. If you
exported before 2026-09-02, re-pull DH6621.

**One character to watch on import: `Las Águilas` in KB9024's Meta Description carries an accented
Á.** Confirm it survives the export-to-import round trip rather than arriving as a mojibake pair.

## Import-file notes

- Four content fields ship: Body HTML, meta title, meta description, short description. Nothing else.
- `Command` = MERGE on every row. **No Title column** (absence is the preservation guarantee).
- **A nonzero `Created` in the Matrixify job summary is a STOP CONDITION.** Report `Updated N / Created 0` with the job ID.
- Expected: **Updated 9 / Created 0**.

## Publish-priority note: three of the nine are close to sold out

Copy is evergreen and ships regardless, and no brief makes an availability claim in either
direction. This is implementation ordering, not a blocker.

| SKU | Stock | The detail that matters |
|---|---|---|
| JN4397 Spain | **1 of 6** | The only size left is 2XL. The candidate sheet recorded 3 of 8 the day before; today's live read is 1 of 6. |
| HQ2332-800 Haaland | **2 of 15** | Both remaining sizes are at the small end of the run, M 4.5 and M 5.5. Everything from M 6 up is gone. |
| UUM1GUAJ525101-U10 Guatemala | **2 of 6** | The two are 2XL and 3XL. |

The other six are healthy: Paraguay 5 of 5, Club America 6 of 6, USMNT shorts 4 of 4, Panini 1 of 1,
Italy 5 of 6, sleeves 6 of 10.

## Carry back to ORIN at step 15

The confirmed-live handle list, plus any failures or skips, plus `Updated N / Created 0` and the job ID.
ORIN flips exactly those rows to `shipped` and writes `batch` + `implementation_date`. A handle not
reported stays `pending`.

### Baselines: what step 15 writes, corrected 2026-09-02

~~**Batch 17 also writes `baseline_position` from the earned-term positions in the table above**, per
the 2026-08-27 ruling that the registry starts recording the one metric this work is supposed to
move.~~

**SUPERSEDED 2026-09-02. Struck rather than deleted, because anyone who read the earlier version of
this handoff was told to write the earned-term position into `baseline_position`, and following that
now would overwrite a page-level figure with a term-level one.**

The registry carries **two** position columns and they are different scopes:

| Column | Scope | Holds |
|---|---|---|
| `baseline_position` | page | GSC average across every query the page appeared for. Comparable with `baseline_impressions`, `baseline_clicks` and `baseline_ctr`, which are all page scope |
| `baseline_term_position` | term | GSC average for the earned term only. **This is the metric the 2026-08-27 ruling was reaching for, and the one the follow-up measures** |

The 2026-08-27 ruling was right about what to record and wrong about where. Writing a term-level
position into `baseline_position` would have left four fields in one row that look like a single
measurement and are not, so anything reading the row as a unit would mix scopes silently.
`baseline_term_position` was added on 2026-09-02 to carry both facts without ambiguity.

**For Batch 17 specifically, step 15 does NOT write either column. They are already populated.**
Baselines were captured on 2026-09-02 **before** the import, which is the only moment a true
pre-state exists, and the nine rows were appended early to hold them. Step 15's job here is
narrower than usual: flip `status` to `shipped`, and write `batch` and `implementation_date`.
**Do not overwrite the baseline columns.** Full capture and method:
`deliverables/tracking/2026-09-02_batch17-baselines.md`.

Term positions as captured, for reference against the table above (measured 2026-06-05 to
2026-09-02, canonical URL only): Club America 3.40, Guatemala 4.93, Paraguay 4.89, Spain 5.50,
Haaland 6.08, Strike Sleeves 9.07, USMNT shorts 10.55. Italy and the Panini box are `not-ranking`
and are correctly blank.

**For a future batch that does NOT capture pre-import baselines**, step 15 writes both columns from
a GSC pull at that time, page average into `baseline_position` and earned-term position into
`baseline_term_position`. That is a worse measurement than capturing before import, because the
copy has already changed by then. Capture early where you can. See `SEO_BATCH_PROCESS.md` §2.
