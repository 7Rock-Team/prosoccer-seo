# ProSoccer SEO Batch Process

**Owner:** Mike Hakopyan, 7 Rock Marketing LLC
**Last updated:** 2026-09-02
**Applies to:** PDP optimization batches (10 SKUs per batch). Collection page batches will extend this once that workstream is defined.

---

## 1. The four participants

### 1.1 Claude Code: the workforce (ORIN, SCRIBE, KIRA)

Runs in Cursor against `C:\Dev-Projects\marketing\prosoccer-seo`.

**Owns:**
- Pre-dispatch cannibalization check against the registry, before any primary is assigned
- Keyword research and primary assignment (KIRA)
- Phase 0 scrape of each live PDP
- Brief authoring, one dispatch per SKU (SCRIBE)
- Gate runs and Layer 3 claim checks (ORIN)
- Appending each closed batch to `products-master.csv`
- Codification of rules into playbook and conventions files
- Git commit at batch close, autonomously as a single atomic commit (see §3 Git). Push to `origin/main` only when a prompt instructs it; a bare "push" means push everything pending, with no commit enumeration requested from Mike.

**Never:**
- Pushes to origin without an instruction to. No push instruction, no push: batch close does not imply a push (the local commit does; see §3 Git)
- Touches the Shopify store
- Builds the Matrixify export filter or import file. That is Step 2's job.
- Authors briefs directly. ORIN orchestrates, SCRIBE writes. This is the mechanism that enforces the playbook.

### 1.2 Claude.ai: Workforce chat

**Owns:**
- Writing the ORIN dispatch prompt for each new batch
- Independent review of what the workforce produces
- Cross-checks the workforce cannot run: collection briefs vs PDP primaries, external spreadsheets, live-page comparisons
- Reading ORIN's reports critically. Does the evidence support the claim.

**Never:**
- Touches the repo or the store
- Builds the Matrixify export filter or import file. That is Step 2's job.
- Accepts a report as verification. Reports describe work; the work itself is on disk.

### 1.3 Claude.ai: Step 2 chat

**Owns:**
- Reading the 10 briefs and producing the paste-ready handle list for the Matrixify export filter
- Building the Matrixify import file from the export plus the briefs
- Validating the file before it goes near Shopify: structure, MERGE on every row, meta description lengths, compliance scan
- The SEO work log, one dated entry per batch, flipped to Verified after Mike's spot check

**Never:**
- Touches the repo or the store

### 1.4 Mike: decisions and everything irreversible

**Owns:**
- When work reaches origin. ORIN commits locally at batch close without being asked; the push to origin happens only when Mike's prompt instructs it, and the workforce then stages the specific files and confirms the pushed ref (see §3 Git). Batch close does not imply a push. Mike owns the push call, not the keystroke. **A bare "push" from Mike means push everything pending; the workforce never asks him to enumerate commit hashes (added 2026-08-26).**
- The Matrixify export from Shopify
- The Matrixify import to Shopify
- Verification in the Shopify admin after import
- All judgment calls: keyword trade-offs, when to ship, what is in scope

---

## 2. The batch workflow

| # | Step | Owner |
|---|---|---|
| 1 | Supply the 10 SKUs and URLs | Mike → Workforce chat |
| 2 | Write the ORIN dispatch prompt, including the pre-dispatch registry check | Workforce chat |
| 3 | Pre-dispatch cannibalization check **before** any primary is assigned | ORIN |
| 4 | Phase 0 scrape, KIRA primaries with volumes, Mike approves | ORIN → Mike |
| 5 | SCRIBE authors briefs, one dispatch per SKU. Gate + Layer 3. | ORIN |
| 6 | Review the briefs | Mike, with Workforce chat |
| 7 | **Commit** (ORIN, autonomous at batch close) then **push on Mike's instruction** | ORIN / Mike |
| 8 | Paste the 10 briefs into the Step 2 chat | Mike |
| 9 | Produce the paste-ready handle list for the export filter | Step 2 |
| 10 | Matrixify export filtered by handle | Mike |
| 11 | Send the export to Step 2; Step 2 builds and validates the import file | Mike → Step 2 |
| 12 | Import to Shopify | Mike |
| 13 | Spot-check live PDPs | Mike |
| 14 | **Append the batch primaries to `products-master.csv`** | ORIN |
| 15 | Close the SEO work log entry, flip to Verified. **Report the confirmed-live handle list back; ORIN flips `status` to `shipped` and writes `batch` + `implementation_date` for those rows only** | Step 2 → ORIN |

**Steps 3 and 14 are the pair that keeps the registry honest.** Step 3 is worthless if step 14 stops happening. If a batch ships without being appended, the next batch's check goes blind.

**Step 15 is what keeps the registry TRUTHFUL (added 2026-08-14).** Appending a row (step 14) records that a page was briefed. It does not record that the page is live. Those are different facts and the registry had been conflating them.

- **`status` = `shipped` only after Mike confirms the Shopify import landed.** Never at brief close, never at commit, never because the export matched. Until confirmation the row stays `pending`.
- Step 2 reports the handle list that actually imported, plus any failures or skips. ORIN flips exactly those rows. A handle not reported stays `pending`.
- **The report states `Updated N / Created 0` from the Matrixify job summary, with the job ID (added 2026-08-19). A nonzero Created is a STOP CONDITION, not a note.** Matrixify matches on handle, so a mistyped or reconstructed handle matches nothing and CREATES a phantom product instead of failing. That product is live and invisible to every check we run, because the registry only tracks pages we chose and the gate only reads the session folder. `Created 0` is the only cheap positive evidence that the handles-from-briefs rule held; before 2026-08-19 we had only an absence of complaints. Full rule: `STEP_2_BRIEFING.md`.
- The safe direction is deliberate: a live row wrongly left `pending` costs one re-check; a never-imported row wrongly marked `shipped` hides finished work indefinitely.
- **The same flip writes `batch` and `implementation_date` (added 2026-08-14).** They come from the one confirmation event, so they are recorded in the one step. `implementation_date` is the import date Mike confirms, not the brief date and not the commit date. **Never infer it from `brief_date`:** Batch 9's brief-to-import gap is ten days. A row without a confirmed import leaves both fields blank rather than carrying a guess.
- Why this was added: the 2026-08-14 GSC cohort analysis found `implementation_date` populated on **0 of 142 rows** and `batch` absent entirely, so every before/after comparison had to reconstruct the cohorts from Matrixify session folders before it could run at all. The 101 shipped rows were backfilled that day from that verified mapping; the 47 pre-B5 rows stay blank permanently. Recording it at step 15 is what stops the next analysis paying that cost again.

**A batch that captures baselines appends its registry rows BEFORE import (added 2026-09-02, Mike).** This is a deliberate exception to step 14, which otherwise appends after the import is confirmed.

The reason is mechanical: a baseline has to attach to a row, and the row has to exist before the import that the baseline will be measured against. Once the import runs, the pre-window is gone and cannot be reconstructed, because the copy on the page has already changed.

When a batch appends early, three things hold:

- **`status` is `pending`.** Unchanged from the normal rule. A row is `shipped` only after Mike confirms the import landed, and an early append does not make a page live.
- **`batch` and `implementation_date` stay BLANK.** Both are written at step 15 from the single import-confirmation event, per the 2026-08-14 rule above, and populating either at append time breaks that. Batch identity goes in `notes` until step 15 fills the columns.
- **The append is verified, not assumed.** Round-trip the CSV before writing and confirm zero field drift across the pre-existing rows afterwards. Adding rows to the registry is the one place where a bad write silently corrupts every future cannibalization check.

Step 14 then has nothing left to append for that batch, and step 15 does what it always does: flip the reported handles to `shipped` and write `batch` and `implementation_date`.

**Batch 17 is the first case, on 2026-09-02.** Nine rows appended while the batch sat at step 7, taking the registry from 178 to 187, with page-level and term-level GSC baselines recorded. It is the first batch in the programme with a pre-import baseline on disk: every performance column was empty on all 178 prior rows, and the 2026-08-14 attempt to reconstruct a pre-window after the fact could not detect an effect in either direction. Full capture and method: `deliverables/tracking/2026-09-02_batch17-baselines.md`.

**Two baseline position columns exist and they are not interchangeable.** `baseline_position` is the page average across every query the page appears for and is comparable with `baseline_impressions`, `baseline_clicks` and `baseline_ctr`, which are all page-scope. `baseline_term_position` is the position of the earned term only, and it is the figure the ranking bands key on and the one a follow-up should measure. Never substitute one for the other, and never average them.

Origin: a live audit of all 151 registry rows on 2026-08-14 found **16 statuses wrong in both directions**. Ten `pending` rows were live (the whole Batch 10 set). Six `shipped` rows had never been imported: the three Mexico 2026 Stadium jerseys, the Predator Accuracy Crazyrush page, HP9971 and IH1779-900. Two of those six were about to be touched by a correction batch that assumed their copy was live. The audit is the expensive way to find this; this step is the cheap way to prevent it.

**The gate (step 5).** `scripts/batch_gate.py` runs **16** mechanical checks over the session folder. Exit 0 only when nothing fires. The gate replaces the human per-brief review for mechanical defect classes; the escalate-on-exception batch mode (CLAUDE.md 'Approval mode') is safe only because it runs.

The sixteen, named as `ALL_CHECKS` emits them into `_gate-run.json` (verified against the code and against a live run 2026-09-02):

`voice`, `heading-levels`, `section-presence`, `customization-claims`, `url-handle`, `price-in-body`, `heritage-counts`, `fabrication-hedge`, `fifa-terms`, `forbidden-phrasings`, `word-band`, `brand-casing`, `cannibalization`, `cross-brief`, `registry1-present`, `ranking-input`.

Two of those deserve naming here because they are unconditional hard fails:
- `section-presence` (added 2026-07-31): every required PDP section must be present WITH content, and the Description body must carry at least one internal link.
- `ranking-input` (added 2026-08-27, the sixteenth): `earned_term_position` is a mandatory `gate-meta` field and its absence is a FAIL. See §2 "Ranking-page batches" below. This is the check the count was stale by: the doc said 15 from 2026-08-25 until 2026-09-02 while the code ran 16 from Batch 17 onward.

**A check that CANNOT run is now a hard failure (changed 2026-08-18, Mike).** The gate used to print a skip line and still exit 0. Three false-green paths existed and all three are closed:
1. `inputs/_registry1_primaries.txt` absent, empty or unreadable, which silently downgraded cannibalization to intra-batch only. Now `registry1-missing`, a batch-level FAIL.
2. A missing per-SKU input file, which disabled word-band, forbidden-phrasings and the branded FIFA check for that SKU. Now an `input-file` FAIL.
3. A gate-meta block PRESENT but carrying no usable `word_band`, which disabled the word-band check with **no output at all**. That was the worst of the three, because there was nothing to notice. Now a `word-band` FAIL.

A backstop in `report()` returns non-zero on any remaining skip, so a future skip source cannot reach exit 0 before someone notices it. **ORIN must write `inputs/_registry1_primaries.txt` at pre-dispatch**, one claimed primary per line from `products-master.csv`, with any pending retargets applied so it reflects post-import truth. Origin: this is codification candidate 2 from Batch 9, logged 2026-07-27. It cost the same false green three times (Batch 9, Batch 14, Batch 15) and both later catches were luck: once because a human read the output, once because a subagent quoted the line back. Six regression tests now assert non-zero exit for each path.

**The gate now writes a run log: `<session>/_gate-run.json` (added 2026-08-19).** Exit code and verdict, timestamp, briefs checked and their SKUs, which checks RAN and which were skipped, finding counts by check, and the Registry 1 file's presence and row count. It exists because gate output went to stdout and was never persisted, so "the gate passed" was a recollection rather than evidence. Two cases motivated it and neither can be settled retrospectively: Batch 9 provably ran without the cross-batch cannibalization check, known only because the registry file is absent from git; and Batch 14 is recorded as printing the skip DESPITE having the file committed with its session. `cross_batch_cannibalization_ran` is recorded explicitly because that is the fact neither case could establish afterwards. Writing the log never fails the gate: the verdict is the product, the log is the record.

**`### URL Handle` must restate the handle (gate check `url-handle`, added 2026-08-19).** A no-change rationale is welcome, but it goes AFTER the handle, never instead of it. Step 9 says handles always come from the briefs and are never reconstructed from product titles, so this field is the only source; two Batch 15 briefs wrote only prose and an extractor building the paste list returned the words "70-character" instead of a handle.

Handles always come from the briefs (step 9). Never reconstruct them from product titles. ProSoccer handles abbreviate in ways titles do not: `man-united` not `manchester-united`, `ls` not `long-sleeve`, `fg` not `firm-ground`.

**And the converse, which is a separate rule (added 2026-08-25, Mike): the LIVE TITLE governs product attributes, and the handle is never a source for them.** Tier, cut, surface, age band, closure and gender come from a fresh fetch of the live title. The two rules point in opposite directions on purpose: the brief is authoritative about what the URL SAYS, the live title is authoritative about what the product IS. Batch 15.1 had two SKUs where reading attributes off the handle would have produced the wrong primary: `adidas-jr-f50-hyperfast-mid-fg-mg-...` carries no tier token and is actually a **Club** Mid page, and `adidas-kids-f50-hyperfast-club-fg-mg-...` omits **Velcro**, the closure that separates it from the laced Junior page in the same pack. Full rule, prior instances (`jr`/`ll`/`in`/`tf`) and the Shopify option-label trap: `context/workforce-conventions.md` 'The live title governs; the handle is never a source of product attributes'.

### Ranking-page batches (added 2026-09-02)

Where a batch's SKUs already earn impressions, primary assignment is not a free choice. The
authority is `context/workforce-conventions.md` 'Ranking-aware posture (v2, approved by Mike
2026-08-27)'. **That file is the source of truth and this section quotes it rather than restating
it, because SCRIBE reads conventions and a paraphrase here would be a second, divergent rule.**

**The earned-term rule, quoted:**

> **For a page already earning impressions, the primary is the term it already earns.** The copy
> supports that term rather than redirecting the page. We are improving performance on a query the
> page has already won the right to appear for, not picking a new destination.

**The concentration condition, quoted:**

> **The concentration condition (approved 2026-08-27).** The rule applies only where the page HAS
> an earned term. A term qualifies as earned when it holds **at least 15% of the page's impressions
> AND at least 1,000 term impressions** over a trailing 90 days. Below either threshold the page
> has no earned term and falls back to conventional keyword assignment.

Both thresholds bind, and the measurement is term-level:

> **Measure the TERM, never the page average.** GSC page position is an average across every query
> the page appears for and is not the number this rule keys on.

**The bands, quoted:**

| Earned-term position | Posture |
|---|---|
| **Under 5** | Protect the Meta Title fully. Exact-match phrasing of the earned term preserved. Changes to that field require Mike per page. Iterate on Meta Description, Short Description and Long Description. The brief MUST carry the WARNING line. |
| **5 to 10** | The Meta Title may be improved but MUST retain the earned term in exact-match form. Everything else is open. No per-page Mike gate; the brief states the earned term and its position so the constraint is visible and auditable. |
| **10 to 20** | Standard recommendations. Carry the earned term into the Meta Title where it fits naturally. Not binding. |
| **Over 20, or not ranking** | Standard recommendations. Nothing to protect; treat as a fresh attempt. |

The bands are written against the **Meta Title** and never the H1. See §3 "Never changed".

**The input is mandatory.** `earned_term` and `earned_term_position` are required fields in every
per-SKU `gate-meta` block, written by ORIN at Phase 0 from GSC term-level data. The `ranking-input`
gate check FAILS the batch when the position is absent or malformed, when a page under position 5
carries no WARNING line, and when a page in the 5-to-10 band drops the earned term from its Title
or Meta Title. Where there is no earned term, set the position to the string `"not-ranking"`: that
is an explicit declaration, not an omission.

---

## 3. Standing rules

### Never changed
- Product titles. Under any circumstances, even if a brief proposes one.
- URL handles. Changes are flagged only and require a 301 coordinated with Misha.
- Taxonomy nodes, tags, variants, prices, or any metafield not in the import file.
- **The H1 on a PDP. No brief recommends one, in any band.** See the standing rule below.

**STANDING RULE: on a PDP the H1 is never a brief output (Mike, 2026-08-30).** Quoted from
`context/workforce-conventions.md`:

> The H1 on a ProSoccer PDP renders from the Shopify product title, and product titles are never
> changed (`SEO_BATCH_PROCESS.md` §3 'Never changed'). **No brief recommends an H1 on a PDP, in any
> band.** The bands above are therefore written against the Meta Title, which is the only title
> field the workforce writes on a product page.

The earlier band wording ("Protect Title and H1 fully", "Title and H1 may be improved") came over
from a collection-page frame and named a field this store's structure makes unwritable. It was
corrected in conventions rather than resolved case by case.

**Collection pages are explicitly out of scope for this rule.** A collection H1 IS an editable
field, and nothing here changes how collection briefs treat it. The rule is about PDPs only. The
collection workstream is not yet in production (§6), so this scoping is forward-looking.

### Keyword hierarchy
Collections own brand, model, club, category, and any term where a searcher would be satisfied by multiple products. PDPs own **age band** + model + tier + cut + surface + **pack (when a concurrent live pack sibling exists)** + width + colorway, terms that resolve to one product.

**Age band (adult, women's, junior, kids) is part of the configuration tuple (added 2026-08-25).** It always was in practice, since `adidas f50 club` and `adidas junior f50 club` have long been separate held primaries, but the tuple text did not name it. Read it off the live title and confirm against variant size VALUES, not the Shopify option label. Full rule: `context/workforce-conventions.md` 'Pack succession' point 1.

Volume never overrides hierarchy. When no floor-clearing term is hierarchy-valid, the page takes the exact qualified term and is flagged sub-floor. It does not take a collection or sibling term.

**Pack succession (added 2026-08-04, approved by Mike).** A footwear model ships in multiple concurrent packs of the same model + tier + cut + surface, so that unqualified term does not always resolve to one product. Pack-qualification is required only when a concurrent LIVE pack sibling exists (checked against the live sitemap, not the registry alone, since incumbents are often unoptimized). With no live sibling, the PDP keeps the unqualified term. With a live sibling, the incumbent keeps the unqualified term and every newer pack takes a pack-qualified sub-floor primary, which is mandatory, not a fallback failure. **The incumbent is the live page earning the most GSC impressions at that configuration over a trailing 90 days (v3, Mike 2026-08-18); season-earliest is the fallback where GSC data is absent or below threshold.** A churn guard bars reassignment except on sustained divergence across two consecutive measurement periods, and never for a shipped page without Mike's explicit per-page decision. The rule applies forward-only; shipped pages are not retargeted on account of it alone. Full rule, including archival succession and the season-code qualifier: `context/workforce-conventions.md` 'Pack succession and PDP keyword ownership (v2)'. This supersedes the Batch 12 shadow-suffix omission rationale.

### Meta fields
- **Meta Title:** max 48 characters for the written part. The theme appends the store suffix automatically. Never type the store name. Never end with a manufacturer brand as a pipe suffix (`| adidas`, `| Nike Stadium`). A pack or product-line pipe suffix is fine (`| Breakout`, `| Road to Glory`). Brand at the front is correct.
- **Meta Description:** 120 to 160 characters. Full sentences. No "Product Name: fragment" colon opener. What the product is + key benefit + light call to action.

### Copy rules
- adidas always lowercase
- "cleats" or "shoes", never "boots"
- No em dashes anywhere
- Non-adidas products never use FIFA or World Cup language
- Club jersey copy names Premier League directly; European competition stays generic
- Every heritage or spec claim sourced to the scrape or qualified. No bare PASS.

### Git
- ORIN commits locally at batch close as a single atomic commit, without being asked. This is autonomous and expected. Commit with a real message plus the `Co-Authored-By` trailer.
- Push is instruction-gated. Nothing reaches origin without Mike instructing it. Batch close does not imply a push. Left uninstructed, the workforce commits locally and reports the unpushed ref.
- **A BARE "push" MEANS PUSH EVERYTHING PENDING (added 2026-08-26, Mike).** On any push instruction that does not name specific commits, push the whole pending set: `git push origin main` with every local commit ahead of `origin/main` included. **Never ask Mike to enumerate commit hashes.** The gate is that he said push, not which hashes he listed. Requiring an enumeration turns a gate into ceremony and pushes the bookkeeping back onto the person the gate exists to serve. Mike does not push manually; he says push and the workforce runs it.
- Reporting after a push is unchanged and still required: confirm the pushed ref range and that `HEAD` equals `origin/main`. If Mike names specific commits, that is a narrower instruction and it is honoured as given; the bare form is the default.
- Stage the specific files changed. Never `git add <dir>/` blindly: it sweeps untracked scratch files into the commit. Verify the staged file list before committing.
- A change to how git works comes from Mike stating it deliberately, not inferred from a command line appearing in context. A command in a prompt executes that command; it does not silently rewrite the standing rule.

### Shipping and customization claims
Authoritative facts: `context/shipping-customization-facts.md` (source: ProSoccer shipping-delivery page). State them exactly, never round, never invent.
- Name/number customization is selected ON THE PRODUCT PAGE, never "at checkout." Point the customer to the option on the page.
- Name/number customization adds BUSINESS DAYS (Customized name/number: 2-3 business days, about one extra day), never "1-2 weeks" or "extra weeks."
- Keep the processing tiers distinct: Standard 1-2 business days; Customized name/number 2-3 business days; Personalized jerseys 5-10 business days; Team/club orders up to 4 weeks. A name/number add is not a personalized jersey; do not conflate the tiers.
- CORRECT: "Add your name and number right on this page. Name and number orders ship in about 2 to 3 business days." INCORRECT: "Customize at checkout. Personalized jerseys take an extra 1 to 2 weeks."
- Enforced by `scripts/batch_gate.py` `check_customization_claims` (see §7 pattern 1).

### Forbidden-phrasing lists
A forbidden verbatim (or title-frame) entry must never be a substring of an approved phrasing. `scripts/batch_gate.py` matches those tiers by substring, so a bare form embedded inside an approved phrase false-FAILs the approved copy (Batch 11: the barred `germany's most storied club` fired on the approved `one of Germany's most storied clubs`). Before adding a verbatim or title-frame bar, confirm it is not a substring of any phrasing the claims bar approves. Full rule and worked example: `context/workforce-conventions.md` 'Forbidden-phrasings three-tier scope (v2)'.

---

## 4. Matrixify

### Export (Mike, filter supplied by Step 2)
Products → Filter by Handle → paste the comma-separated list → Groups: Basic Columns + Metafields + Media → Format: Excel → confirm the summary reads 10 products.

Fallback if the handle filter fails: tag the 10 products `seo-batch-N` in the admin and filter the export by Tag. Safe because the import file has no Tags column. Remove the tag after the batch is verified.

### Import file (Step 2 builds)

Four content fields ship: Body HTML, meta title, meta description, short description. Nothing else.

**Documented default, XLSX.** Single sheet named exactly `Products`, filename `ProSoccer_SEO_Batch{N}_{count}_Products.xlsx`, seven columns:

```
ID
Handle
Command
Body HTML
Metafield: title_tag [string]
Metafield: description_tag [string]
Metafield: products.new_short_description [multi_line_text_field]
```

**Also works, CSV.** Six columns, Handle-keyed, using bare metafield key names (`title_tag`, `description_tag`, `new_short_description`). Verified on Batch 9: Matrixify accepts bare metafield names and applies all fields correctly. The only difference is that Handle plus Command are ambiguous across Products and Collections, so Matrixify prompts "Sheets require entity selection." Pick Products and proceed.

The XLSX form stays the default because the sheet name auto-resolves the entity and the numeric ID is a stronger match key than the handle.

**In both forms:**
- `Command` = MERGE on every row
- No Title column. Absence is the preservation guarantee.
- If an ID column is used, it holds the real Shopify numeric product ID stored as text, sourced from the export. Never a SKU, never invented.

---

## 5. What must never happen

1. **A report is not verification.** Read the artifact, not the summary of it. This extends to SELF-measurement: an agent's report about its own output is not evidence, only the deterministic check is, and any figure or pass claim must trace to a check that ran. Three instances of that class (Batch 9, 12 and 14) and the practical rule for ORIN: `context/workforce-conventions.md` 'Codification checklist' item 6.
2. **A check that did not run is not a pass.** If the gate prints that it skipped something, that is a failure.
3. **Nothing self-referential counts as a check.** Verifying a brief against its own recorded value proves nothing. Ground truth means a fresh scrape or a live fetch.
4. **Rules that live outside the repo do not exist.** If SCRIBE cannot read it, SCRIBE will not follow it. Codify at the point of discovery, not at batch close.
5. **Examples teach louder than rules.** The 20 meta title brand-suffix violations happened because the playbook's own examples demonstrated the violation while the rule beside them forbade it. When an exemplar and a rule disagree, the exemplar wins. Audit examples whenever a rule is written or changed.
6. **Do not assert a tool's behavior without testing it.** Infer, flag, then verify. An untested claim stated as fact costs more than the uncertainty it was meant to resolve.
7. **A check that ran against STALE data is not a pass, and it is harder to catch than one that did not run (added 2026-08-25, Mike).** Rule 2 covers the check that skips and says so. This is the check that runs, prints nothing unusual, exits 0, and is wrong, because its cached input aged out. Assert the snapshot's freshness before trusting the verdict, and fail on stale rather than warn. Batch 15.1: a 12-day-old sitemap cache would have reported "no live pack sibling" for both Sparkfusion SKUs, because the two pages that ARE their siblings were published inside those 12 days. Nothing in the output would have differed from a correct run. Full rule: `context/workforce-conventions.md` codification checklist item 12.

---

## 6. Open at last update

_Refreshed 2026-09-02 against disk. The previous state of this section was written at Batch 11 and stood six batches stale._

**Batches.** Everything through Batch 16 is live on Shopify. `products-master.csv` carries **178 data rows: 173 `shipped`, 4 `pending`, 1 `intentionally-unoptimized`.** Batch labels run B5 through B16 (B5 is 11 rows, B6 through B15.1 are 10 each, B16 is 9); **48 pre-B5 rows carry no batch label** and permanently never will.

**Batch 17 is briefed and not imported.** Nine SKUs, gate green (exit 0, 16 checks, 0 findings), committed. It stops before the Matrixify export. **Step 14 has NOT run: no Batch 17 rows are in `products-master.csv` yet**, so the registry currently knows nothing about those nine pages. Step 3 goes blind on the next batch if that append is skipped.

**The 4 `pending` rows are the unimported remainder of the 2026-08-14 audit:** the Predator Accuracy Crazyrush page and the three Mexico 2026 Stadium jerseys (home, away, third). All four are briefed, none imported, and all four now fail current meta rules. Tracked as B-IMP-01 in `strategy/sprint-backlog.md`.

**Gate.** Now **16** mechanical checks, not 15 (`ALL_CHECKS`, verified against the code and a live run 2026-09-02). `ranking-input` is the sixteenth, added 2026-08-27 and first exercised in Batch 17. Hardening status, re-verified 2026-09-02:
- (a) **Still open.** The cannibalization check is exact-match only, keyed on the literal primary string, with no containment or token-subset detection. That class is caught by ORIN's manual pre-dispatch pass, never by the gate.
- (b) **RESOLVED.** `voice_check.py` no longer skips fenced blocks in canonical instruction files: `strip_backticks(keep_fenced=True)` plus `is_canonical_instruction` puts worked examples back in scope. This closed the exemplar class that produced the brand-suffix violations.
- (c) **Still open.** Meta-title length (48-char cap) and meta-description length/format are not gated at all. Enforced by SCRIBE, the Step 2 validation pass, and Layer 3 only.

**Still open, carried forward:**
- 20 meta title brand-suffix violations found across all batches. KA6868 fixed manually 2026-07-28; 19 remain live, awaiting fix-forward. Status not re-verified against the live store on 2026-09-02.
- Collection page workstream. `collections-master.csv` holds **199 rows: 137 `not_started`, 60 `inherited`, 1 `approved`, 1 `existing-optimized`.** **The workstream is not in production and there is no collection workflow documented anywhere in this repo.** No collection batch has run. The inherited white-label primaries still need their audit.
- `products-master.csv` `product_id` is **populated on only 3 of 178 rows** and blank on the rest. Where it was populated historically it held the SKU rather than the Shopify numeric ID. Nothing reads it; the import file sources real numeric IDs from the Matrixify export instead.

**Open decision, not resolved here:** where an earned term and the keyword hierarchy point at different owners, conventions call the override an amendment and require a measured test per contested term. What conventions do NOT state is which query the band derives from when several members of one cluster qualify. Logged in `strategy/sprint-backlog.md`; see the Batch 17 DH6621 case.

---

## 7. Documented failure patterns

A customer-facing fact or mechanical class that shipped wrong. Each entry: symptom, root cause, discovered, fix. Numbered; add the next in sequence when a new class is found.

### 1. Name/number customization stated as "at checkout" and in "weeks"
- **Symptom:** shipped briefs said name/number customization is done "at checkout" and that it adds "1 to 2 weeks" (some "1 to 3 weeks") of processing.
- **Root cause:** both facts are wrong. Name/number customization is a PRODUCT-PAGE option, not a checkout step, and it adds business days (Customized name/number: 2-3 business days, about one extra day), not weeks. The "weeks" figure conflated the name/number add with the separate personalized-jersey tier and rounded days up to weeks.
- **Discovered:** Mike, Batch 11 prep (2026-08-03). Present in 7 of 10 Batch 10 briefs (II1624-683, KB8261, KB8251, KC3952, KC3989, KC3947, KC3993), which were pushed but not yet imported to Shopify.
- **Fix:** facts codified in `context/shipping-customization-facts.md` (read every run, referenced from `CLAUDE.md`); standing rule in §3 "Shipping and customization claims"; deterministic gate check `check_customization_claims` in `scripts/batch_gate.py` (FAILS customization language paired with "checkout", or name/number timing given in weeks) with a regression fixture in `scripts/test_batch_gate.py`; handoff-template discipline: brief inputs and FAQs state the product-page location and the 2-3 business-day figure, never "at checkout" or "weeks."

### 2. An agent report described analysis that produced no artifact

- **Symptom:** a past-tense agent report stating that the Phase 0 scrape had been run, metrics pulled and incumbency resolved for a SKU, reading as finished work. **No file for that SKU existed anywhere on disk:** no input, no brief, no scrape record, nothing in the session folder, nothing untracked. The report was the only trace.
- **Root cause:** the analysis really was performed. It lived entirely in the agent's context and was never written down, then the session ended before anything was persisted. The report described a true past event whose only artifact was the context that reported it, so the work and the record of the work died together.
- **This is NOT §5 rule 1 and the difference is the whole point.** Rule 1 covers a report that overstates the work performed: the claim outruns what was done, and reading the artifact catches it. This is the opposite failure. The work was done and the claim is honest; there is simply no artifact to read. Rule 1's remedy ("read the artifact, not the summary of it") does not fire here, because a reader who goes looking finds nothing at all rather than finding a discrepancy. **Treat absence of an artifact as absence of the work, however credible the report and however genuinely the work happened.**
- **Discovered:** 2026-09-02, reconciling Batch 17 state after a session crash.
- **Fix:** persist at the point of production, not at the end of a phase. Any analysis a later step depends on gets written to the session folder as it is produced, so a crash costs the tail of the work rather than all of it. When a report and the filesystem disagree about whether something exists, **the filesystem is right**. Re-run the analysis; do not reconstruct it from the report, because a reconstruction inherits the report's confidence without inheriting its evidence.
