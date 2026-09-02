# ProSoccer SEO Pipeline: Master Reference

The full workflow start to finish, every file the system uses, every rule it enforces, and the business context those rules come from.

**Updated:** 2026-09-02
**Client:** ProSoccer.com, Shopify Plus, roughly 15,000 products
**Agency:** 7 Rock Marketing LLC
**State:** Batches 1 through 16 live. `products-master.csv` at 178 rows. `collections-master.csv` at 199 rows (137 not_started, 60 inherited, 1 approved, 1 existing-optimized). Batch 17 is briefed, gate-green and pushed at nine SKUs, and has NOT been imported. Its rows are not yet in the registry, because step 14 has not run.

**Verification status of this document.** Parts 1, 3, 4, 5 and 6 were reconciled against `SEO_BATCH_PROCESS.md`, `STEP_2_BRIEFING.md` and `context/workforce-conventions.md` on 2026-09-02. **Part 2, the file inventory, has NOT been verified against disk.** At least one entry in it was wrong: `scripts/crossfile_audit.py` is described below but does not exist anywhere in the repository. Treat every other entry in Part 2 as a claim until ORIN confirms it against a directory listing. See the note at the head of Part 2.

---

# PART 1: THE WORKFLOW

## The four participants

**Claude Code, the workforce.** Runs in the repository on Mike's machine. Three active agents:

- **ORIN** (master-strategist) is the project manager. It reads the records, checks for conflicts, scrapes the live pages, prepares a briefing packet for each product, hands those to the writers, runs the quality checks, and commits the work. It does not write copy itself.
- **KIRA** (keyword-research) is the researcher. It pulls search volumes and proposes which keyword each page should target.
- **SCRIBE** (on-page-seo) is the writer. One writer is dispatched per product, each working only from that product's briefing packet.

Defined but not currently used: VERITAS (technical SEO), RECON (competitor research), content-writer, reporting.

**Claude.ai Workforce chat.** A separate conversation with no access to the repository. It writes the instructions ORIN receives, reviews what comes back, and runs the checks the workforce cannot: comparing against outside spreadsheets, reading documents from third parties, checking a new file against the last one that worked.

**Claude.ai Step 2 chat.** Another separate conversation, started fresh for every batch. It reads the finished briefs cold, produces the list of product handles for the Shopify export, builds and validates the import file, and reports back which pages actually went live.

**Mike.** Every judgment call, and every action that changes the live store.

---

## The tools the agents have

Four external services plus local file and version-control access. A live auto-generated inventory sits at `context/agent-inventory.md`.

| Tool | What it does | Used at |
|---|---|---|
| **Firecrawl** | Scrapes live web pages and returns clean text. Used to read what a product page actually says: specs, materials, colorway, price, existing copy. Also used to map a collection and confirm what is really in it. | Step 5, the batched scrape. Also link validation and any live check. |
| **DataForSEO** | Keyword search volumes and difficulty, plus a SERP endpoint that reports where a URL currently ranks for a term. Two endpoints are used and both are checked, because a term can return nothing on one and a real figure on the other. | Step 4, keyword research. Also the ranking check before recommending title changes. |
| **Google Search Console** | What the store actually earns: impressions, clicks, average position, per page and per query. Also URL Inspection, which reports whether Google has re-crawled a page and what canonical it sees. | Selecting batches by real demand, measuring whether shipped work performed, confirming a page was re-crawled after import. |
| **Tavily / web search** | General topic research where a club, brand or product needs background the scrape does not supply. Scaled to familiarity: a couple of queries for a well-known club, more for something unfamiliar. | Step 5, where heritage or context is needed. |
| **Shopify Admin API** | Reads store data directly: whether a collection exists, how many products are in it, product creation dates. Creation dates matter because they establish which pack of a shoe launched first. | Verifying collections before linking to them, resolving which page is the incumbent. |
| **Bash, file read and write** | Running the check scripts, reading and writing repository files, and git. | Throughout. |

**What the agents do not have.** No access to the Shopify storefront as an editor, no access to Matrixify, and no ability to publish anything. Every change to the live store passes through Mike.

**On permissions.** Routine commands are pre-approved so the workforce is not stopping every few seconds: reading files, running scripts, committing, and the four connectors above. Destructive commands still prompt or are blocked outright, including force-push and recursive delete.

---

## Where the keyword records live

There are three separate records, and it is easy to confuse them. Here is what each one is in plain terms.

### Registry 1: the white-label Google Sheet

An external spreadsheet with two tabs, one for product pages and one for collection pages. It is the shared record of which keywords are claimed across all ProSoccer SEO work, including work done by the white-label team.

This is where Mike picks the ten SKUs for a batch and marks them In Progress.

The white-label team owns writing to it. The workforce reads it and hands back a summary block for manual entry.

Because the AI agents cannot open a Google Sheet directly, ORIN copies the relevant portion into a plain text file at the start of every batch (`inputs/_registry1_primaries.txt`). The quality gate refuses to run without that file, so the copy cannot be quietly skipped.

### Registry 2: the silo files

A folder of markdown files, one per product family (Furon, Tekela, F50, club jerseys and so on).

These do not hold keywords. They hold **writing patterns**: which opening hooks, metaphors, use-case scenarios and angles each product page has already used. When the next page in that family gets written, the writer checks this file so it does not accidentally produce a near-copy of its sibling.

ORIN adds to these files at the end of every batch. Nothing is ever deleted from them.

### The on-disk registry: the CSV files

Three spreadsheets stored inside the repository itself: `products-master.csv`, `collections-master.csv`, and `ceded-terms.csv`.

These exist because the agents need to check for keyword conflicts before assigning anything, and they can only check against files they can actually read. Registry 1 lives in Google Sheets, outside their reach. These CSVs are the version the automated conflict check reads.

**In short:** Registry 1 is the shared human record. Registry 2 is the writing-style memory. The CSVs are the machine-readable record the checks run against.

---

## The 15 steps

| # | Step | Owner | What it does and why |
|---|---|---|---|
| 0 | Select SKUs from Registry 1, mark In Progress | Mike | Picks which ten products get worked on and flags them so nobody else picks them up. |
| 1 | Supply the SKUs and URLs | Mike → Workforce chat | Hands the list over to start the batch. |
| 2 | Write the ORIN dispatch prompt | Workforce chat | Turns the list into detailed instructions. This is where the specific risks in this batch get named: which two products are nearly identical, which brand has licensing limits, which product family is new. |
| 3 | Conflict check against the records | ORIN | Checks every keyword we might use against every keyword already claimed. Runs **before** anything is assigned, so a conflict gets solved before copy is written around it. |
| 4 | Pull volumes, propose keywords, Mike approves | KIRA → Mike | Finds out how many people actually search each candidate term, then Mike signs off before any writing starts. |
| 5 | Scrape pages, build briefing packets, write, check | ORIN, SCRIBE | The actual production step. Live product pages are scraped for real specs, one packet is built per product, ten writers work in parallel, then the automated gate and a claims review run over the results. |
| 6 | Review the briefs | Mike | Human read for voice and quality. The machine checks structure; this checks whether the copy is any good. |
| 7 | Commit locally, then push on instruction | ORIN, then Mike | ORIN saves the work to version control automatically. Sending it to the shared repository waits for Mike, because that step is harder to undo. |
| 8 | Paste briefing and briefs into a fresh Step 2 chat | Mike | Hands the finished work to a reader who has not seen any of the decisions behind it. |
| 9 | Produce the handle list | Step 2 | Extracts the exact product URLs, copied word for word from the briefs. Guessing them from product names does not work. |
| 10 | Export those ten products from Shopify | Mike | Pulls the current state of the pages, which supplies the product IDs the import file needs. |
| 11 | Build and validate the import file | Step 2 | Assembles the file that will update Shopify and checks it before it goes anywhere near the store. |
| 12 | Import to Shopify | Mike | The irreversible step. Stays in human hands. |
| 13 | Spot-check the live pages | Mike | Confirms the changes actually appeared. |
| 14 | Record the batch in the registry | ORIN | Writes what each page now targets, so the next batch's conflict check can see it. |
| 15 | Close the work log, report handles and import date | Step 2 → ORIN | Records what actually went live and when. Status only changes to shipped after the import is confirmed. |

**Steps 3 and 14 are a pair.** Step 3 reads the record. Step 14 writes to it. Skip step 14 and the next batch's conflict check reports everything clean while missing collisions it simply cannot see.

**Step 3 runs before step 4** deliberately. It is far cheaper to move a keyword before anyone writes 400 words around it.

**Step 4 branches by batch type (added 2026-09-02).** For a new-product batch the input is search volume, because the page has no measured performance to read. For a ranking-page batch the governing input is the page's own measured performance: query-level impressions, share and position from GSC, canonical URL only. Volume is secondary there, because the page has already demonstrated what it earns. A ranking-page batch that runs step 4 on volume alone cannot derive a band, and the band is what decides how much of the page may be rewritten.

**The band derives from the term the page earns, never from the assigned primary string.** A primary that earns nothing returns not-ranking and grants full latitude on a page that may in fact hold protected position. This failed once, on Batch 17's DH6621, where the assigned primary `nike strike sleeves` returned no query of its own while the page sat at 9 and 10 on its earned cluster.

---

## How SKUs get chosen for a batch

Step 0 is a real decision, not admin. Which ten pages you pick largely determines what the batch achieves, so the basis should be recorded each time.

**Merchandising need.** New product releases that launched with default or missing descriptions. These pages need copy because they are live and thin, not because anyone is searching for them. Expect keywords with little or no measurable search volume. That is the correct outcome, not a failure.

**Measured demand.** Older pages that are already earning search impressions on terms no optimized page owns. These are the pages where better copy has something to work with, because the traffic already exists.

**Lane completion.** Finishing a club or product family that is already partly done, so the whole set is consistent and the pages support each other with internal links.

**Why it matters:** a batch chosen for merchandising reasons and a batch chosen for demand reasons produce very different results, and judging one by the other's standard is misleading. Recording the basis keeps that honest.

### Detection-gap batches (added 2026-09-02, first run as Batch 17)

A detection-gap batch is the measured-demand basis run systematically rather than opportunistically. It starts from a GSC pull of pages earning impressions that hold no registry row, and works down by demand.

The framework exists because of a finding from the 2026-08 GSC analysis: roughly 1,280 untracked product pages earn the large majority of the store's impressions, against roughly 62,000 for the 178 optimized pages. The pages holding real demand were not the pages being briefed.

**Selection conditions.** The governing conditions live in `context/workforce-conventions.md` and are quoted, not paraphrased, in `SEO_BATCH_PROCESS.md` §2. In outline: a page-level impression band, and a concentration condition requiring the earned term to hold both a minimum share of page impressions and a minimum absolute impression count. **Both conditions bind.**

**Known gap, B-RANK-01.** The concentration condition is currently used both to select pages into a batch and to derive the ranking band that governs how much of the page may be rewritten. Those are different questions. A page whose demand is fragmented across many near-identical phrasings can fail the absolute-impression condition on every single query while still holding real position worth protecting. Batch 17's DH6621 is the worked case: no single query cleared the absolute threshold, yet the page sat at position 9.38 on its head term and 41.7% of its impressions fell inside one phrasing cluster. Unresolved. Do not treat the Batch 17 disposition as precedent.

**Selection basis must be recorded in the batch's candidates file**, so that the eventual before-and-after comparison is read against the right standard.

**Read-out, locked before authoring.** A detection-gap batch is a measurement, so what would count as success is fixed before any copy exists. For each page record four things: success, failure, null, and confound. Null is what movement inside noise looks like, stated in absolute terms rather than as a ratio, since a low-CTR page produces large ratio swings on a handful of clicks. Confound is the variable most likely to move the metric independently of the copy, most often stock depth.

**Registry blind spot, B-DETECT-02.** By construction, a detection-gap batch targets pages the registry does not cover. The cross-batch cannibalization check will run and find nothing to collide against, because none of the batch's terms are claimed anywhere. **A clean cannibalization pass on a detection-gap batch carries less evidential weight than on a new-product batch,** and Step 2 is told so in the per-batch additions. All nine Batch 17 terms were absent from all 177 registry rows.

---

## Inside step 5: how the work is dispatched

The workforce was rebuilt in July 2026 to cut a batch from roughly 4 to 6 hours down to under 90 minutes without losing quality.

The core change: **ORIN gathers everything once, instead of ten writers each gathering it separately.** Previously every writer scraped its own product page, looked up its own keywords, and validated its own links, repeating the same work ten times. Now ORIN does all of that upfront and writes the results into one packet per product.

**The briefing packet** contains everything a writer needs and nothing it has to go find:

- Product identity, URL, handle, brand
- Whether that brand has licensing restrictions
- Real specs from the live page scrape, with anything the scrape did not supply explicitly marked "not in scrape" so the writer leaves it out rather than inventing it
- The approved keyword and supporting terms
- Internal links, already checked as working
- The differentiation angle for this product against its siblings
- The section structure to follow
- Phrases the sibling product already used, which this one must avoid
- A machine-readable block at the bottom that the automated gate reads

### The wave decision, in plain terms

Writers usually all work at the same time. The one exception is when a product family is brand new to the system.

If we have already written about this family before, there is a house style on file: how a Furon page opens, what angle it takes, what it compares itself to. Ten writers can work simultaneously because each one has that pattern to follow.

If the family is brand new (a brand we have never covered, a club we have never written about), there is no pattern yet. So **one page is written first** and reviewed. That page establishes the voice, and its siblings follow it. Everything else in the batch still runs in parallel alongside; only the new family waits.

The test ORIN applies per product: *has this family shipped at least one page with an established pattern?* Yes, write it now. No, write one first and let the rest of that family follow.

---

## Inside steps 10 to 12: Shopify updates via Matrixify

**Export.** In Matrixify: Products → Filter by Handle → paste the comma-separated list → Groups: Basic Columns, Metafields, Media → Format: Excel → confirm it reads 10 products.

If the handle filter fails, tag the ten products `seo-batch-N` in the Shopify admin and filter by Tag instead. Safe because the import file has no Tags column, so the tag cannot be affected. Remove it after verification.

**Import file, standard format.** XLSX, single sheet named exactly `Products`, filename `ProSoccer_SEO_Batch{N}_{count}_Products.xlsx`, seven columns:

```
ID
Handle
Command
Body HTML
Metafield: title_tag [string]
Metafield: description_tag [string]
Metafield: products.new_short_description [multi_line_text_field]
```

**Alternative that also works.** CSV, six columns, handle-keyed, using the short metafield names. Matrixify accepts these. The only difference is that it will ask which type of record you are importing, because Handle and Command exist on both Products and Collections. Choose Products.

XLSX stays the default because the sheet name answers that question automatically, and the numeric product ID is a more reliable match than the handle.

**In both formats:**
- `Command` = MERGE on every row, meaning update the existing record rather than replace it
- **No Title column.** Leaving it out is what protects the live product names. This is the safety mechanism, not an omission.
- If an ID column is used, it holds the real Shopify numeric ID as text, taken from the export. Never a SKU.

**The import must report Updated 10 and Created 0.** If it created anything, a handle did not match and Shopify made a new product instead of updating the intended one. That product is live and invisible to every check we run, so a nonzero Created is a stop condition.

---

# PART 2: THE FILES

> **VERIFIED AGAINST DISK 2026-09-02 (ORIN).** Every entry below was checked against `ls` output for the repository root, `context/`, `context/page-type-playbooks/`, `context/silo-positioning/`, `templates/`, `scripts/`, `deliverables/tracking/`, `data/`, `strategy/`, `work-log/` and `.claude/agents/`. This supersedes the "not verified against disk" warning that stood here.
>
> **Result: four entries described files that do not exist, and four existed but were described wrongly.**
>
> The absent four are `scripts/crossfile_audit.py`, `scripts/build_registry.py`, `HOW_IT_WORKS.md` and `seo-batch-workflow.svg`. Neither script appears anywhere in `git log --all`, so they were never built and never deleted. **They are struck through rather than removed**, because this document was itself cited as evidence they existed, and a deleted row cannot warn anyone about that. This is §5 rule 6 and principle 14: a described tool is not a tool.
>
> The four described wrongly were `sitemap-state.md`'s location, the contents of `.claude/agents/`, the per-batch file counts, and `_audit-trail.md`. Each is corrected in place with the correction marked.
>
> **This part is still not a complete inventory.** Files present but undocumented are now listed at the end of each section where the omission is material, rather than being silently absent.

## Repository root

| File | Purpose |
|---|---|
| `SEO_BATCH_PROCESS.md` | The operational reference. Participants, the 15 steps, standing rules, Matrixify formats. Agents read it at startup. |
| `STEP_2_BRIEFING.md` | Pasted at the top of every fresh Step 2 chat so that conversation starts with the rules. |
| `CLAUDE.md` | Governing instructions all agents read first. |
| `README.md` | Repository orientation. |

All four verified present 2026-09-02. **Also at root, undocumented above:** `docs/`, `deliverables/`, `assets/`, `reports/`, `shared-intelligence/`, `tools/` (which holds the `brief-to-shopify-csv` tool), plus **18 untracked `scratch_*.json` files** left over from analysis sessions. The scratch files are working residue rather than part of the system, and `shared-intelligence/` is worth noting because CLAUDE.md's startup protocol tells every agent to check it for anything dated within the last 14 days.

## `context/`: business knowledge and rules, read at startup

| File | Contents | State |
|---|---|---|
| `00-business-overview.md` | ProSoccer as a business | Active |
| `03-brand-voice.md` | Voice, tone, and the copy-writing principles | Active |
| `04-customer-avatars.md` | **The four customer avatars in full.** Each one's age, buying motivation, budget, what they care about, and voice-of-customer language. This is where the detail behind "Carlos" or "Jennifer" lives; SCRIBE reads it every batch. | Active |
| `06-business-goals.md` | Objectives | Active |
| `07-operational-context.md` | Operations | Active |
| `08-affiliate-program.md` | Affiliate context | Active |
| `09-strategic-principles.md` | Strategy principles | Active |
| `brand-ip-constraints.md` | Licensing, FIFA, trademark posture | Active |
| `shipping-customization-facts.md` | Authoritative shipping and customization timings | Active |
| `workforce-conventions.md` | Cross-cutting rules, forbidden phrasings, pack succession, the codification checklist | Active |
| `matrixify-import-template.md` | Import file reference for Step 2 | Active |
| `agent-inventory.md` | Auto-generated tool and connector inventory | Active |
| `01-industry-context.md` | Industry background | **Template, unpopulated** |
| `04-product-catalog-overview.md` | Catalog overview | **Template, unpopulated** |
| `05-competitors.md` | Competitor set | **Largely placeholder** |

All fifteen verified present 2026-09-02, and `context/` holds nothing else besides the two subfolders below. See the note under `strategy/` on what "unpopulated" means for the three template rows: they contain prompts, not facts.

**`context/page-type-playbooks/`**

| File | State |
|---|---|
| `product-page-playbook.md` | Active. Brief structure, section order, worked examples, meta rules. |
| `collection-page-playbook.md` | **Written, never used in production.** See the note below on the collection workstream. |
| `homepage-playbook.md` | Written, never used. The homepage has never been optimized. |
| `technical-seo-playbook.md` | Active for technical checks. |

All four verified present 2026-09-02.

**`context/silo-positioning/`**. Registry 2, described above. README plus one file per product family. Append-only. Verified 2026-09-02: `README.md` plus **11 family files** (club-team-jerseys, copa, f50, furon, mercurial, morelia, national-team-jerseys, phantom, predator, tekela, tiempo).

## `templates/`

| File | State | Purpose |
|---|---|---|
| `per-sku-input-template.md` | **In active use.** | The briefing packet ORIN writes per product and SCRIBE reads. The bottom of the file carries a machine-readable block that is the single authority on brand, licensing posture, tier, word band, keyword and forbidden phrases. The readable sections above it repeat the same values for the writer's convenience. |
| `consolidated-page-brief-template.md` | **Not in current use.** | A one-page brief format for Mike, from before the batch workflow. Describes a flow where Mike supplies the existing descriptions rather than ORIN scraping them, which is no longer how it works. |
| `consolidated-page-brief-template-archive.md` | **Not in current use.** | The deep-brief format for landmark pages, merging contributions from all four specialist agents. Kept for reference. |

All three verified present 2026-09-02, and `templates/` holds nothing else.

## `scripts/`: what each one actually does

| File | In plain terms |
|---|---|
| `batch_gate.py` | **The quality gate.** Reads every brief in the batch at once and runs 16 automated checks over them (verified against `_gate-run.json` 2026-09-02): are the required sections there, is the word count in range, are there banned words or em dashes, does any keyword clash with one already in use, is a brand name capitalized wrong, are the shipping facts stated correctly, is there at least one internal link. It either passes or lists exactly which brief and which line failed. It cannot be argued with, which is the point. |
| `test_batch_gate.py` | **Proof the gate still works.** A set of deliberately broken examples drawn from real past mistakes. If a change to the gate ever stops it catching one of them, this fails loudly. |
| `voice_check.py` | **The style checker.** Scans for banned terms, em dashes, wrong brand capitalization and UK terminology. Also checks inside code-block examples in instruction files, because an example teaches more than a rule. |
| `test_voice_check.py` | Same idea for the style checker. |
| `build_ceded_terms.py` | **Keeps the "handed over" keyword list in sync.** Some keywords are deliberately given to collection pages rather than product pages. This script rebuilds that list from the collections file so there is only one place to maintain it. It refuses to run without being told today's date, so it cannot quietly stamp wrong dates on the record. |
| ~~`build_registry.py`~~ | **DOES NOT EXIST (confirmed 2026-09-02).** Previously described here as a backfill tool reading old batch folders to reconstruct the record for work predating the registry. No such file is in `scripts/`, and `git log --all` returns nothing for the path, so it was never built. **The backfill it describes was really performed, by hand, on 2026-08-14**, from verified Matrixify session folders: 101 shipped rows were reconstructed that day and the 47 pre-B5 rows were left permanently blank. The work is real, the tool is not, and this row made a manual effort look like a repeatable one. |
| ~~`crossfile_audit.py`~~ | **DOES NOT EXIST (confirmed 2026-09-02).** Previously described here as a contradiction finder comparing rule files against each other. No such file is in the repository and nothing references it. Cross-file reconciliation is currently a manual read, done by ORIN against the three governing documents. Building this script is a real open item, since the reconciliation on 2026-09-02 found ten contradictions by hand. |
| `_build_sitemap_state.py` | **Store inventory refresh.** Pulls Shopify's sitemap and writes down every live product and collection URL, so the workforce can check what actually exists rather than guessing. Writes to `deliverables/tracking/sitemap-state.md`, not to `data/`. |

Six of the eight rows above are real. **Present in `scripts/` but undocumented here:** `phase0_product_facts.py` and `test_phase0_product_facts.py` (the Phase 0 scrape helper, which is production code and runs on every batch), `test_build_ceded_terms.py`, `_classify_404_table.py`, `convert_to_pdf.py`, `generate_presentation.py`, `crawl-national-team-collections.js`, `crawl-retry.js`, and a `build/` directory. Two more are untracked scratch and are not part of the system: `_wordcount_probe.py` and `test-firecrawl.ps1`.

**`phase0_product_facts.py` is the notable omission.** It is production code in the step-5 path, and it was missing from an inventory that found room for two scripts that do not exist.

## `deliverables/tracking/`: the running record

This folder is the system's memory of what has been done and what each page owns.

| File | What we do with it |
|---|---|
| `products-master.csv` | **One row per optimized product page.** Records the URL, the keyword it targets, supporting keywords, the search volume at the time, which batch it belonged to, the date it went live, and its current status. Every batch reads this before assigning keywords, so two pages never end up chasing the same term, and every batch appends to it afterwards. It also holds baseline search performance so we can compare before and after. |
| `collections-master.csv` | **One row per collection page.** Same idea, plus a column recording which keywords have been deliberately handed to that collection from product pages. That column is what makes the decision permanent instead of something re-argued every batch. |
| `ceded-terms.csv` | **The flat list of handed-over keywords** the automated check reads. Generated from the collections file, never edited by hand, so the two cannot drift apart. |
| `technical-seo-log.md` | Technical findings that need a developer rather than a copy change. |
| `cost-log.md` | Token and cost tracking per batch. |
| `sitemap-state.md` | **The live-URL snapshot. It lives HERE, not in `data/`**, where this document placed it until 2026-09-02. Written by `scripts/_build_sitemap_state.py`. Pack succession reads it; see the correction in the `data/` section below for why the wrong path was dangerous. |

The five original rows and `sitemap-state.md` all verified present 2026-09-02. **Also present, undocumented:** `detection-gap-2026-08-27.csv` and `detection-gap-2026-08-27_shortlist.md`, the working files behind B-DETECT-01.

## `deliverables/page-optimizations/<date>_session-NN/`: one folder per batch

| File | What it is |
|---|---|
| `<SKU>_<slug>.md` × N | The finished briefs. This is the deliverable. **CORRECTED 2026-09-02: both this row and the one below said × 10.** A batch is not always ten. **Batch 5 was eleven; Batch 16 and Batch 17 were nine.** Anything that assumes ten, including a Matrixify export summary check, is asserting something the process does not guarantee. |
| `inputs/<SKU>_input.md` × N | The briefing packets ORIN built for each writer. One per brief, always the same count as the row above. |
| `inputs/_registry1_primaries.txt` | The copy of Registry 1 taken at the start of the batch. The gate refuses to run without it. |
| `inputs/_phase0-scrape.md` | What the live pages actually said when scraped, so any spec in the copy can be traced back. |
| ~~`_audit-trail.md`~~ | **NO LONGER WRITTEN (confirmed 2026-09-02).** The last session folder containing one is `2026-08-04_session-01`. The five sessions since it (`2026-08-16_batch15`, `2026-08-18_session-01`, `2026-08-26_session-01`, `2026-08-26_session-02`, `2026-08-28_session-01`) have none. The v2 refactor moved this content into `_STEP2-HANDOFF.md` and the batch commit message, and nobody recorded that the file had stopped being produced. **Listed as expected-but-absent rather than as a defect**, since the decision record did not vanish, it relocated. Worth deciding whether the relocation was intended, because a commit message is not a searchable audit trail. |
| `_gate-run.json` | The gate's own record: pass or fail, which checks ran, which were skipped, when. Turns "the gate passed" from a memory into evidence. |
| `_STEP2-HANDOFF.md` | Everything the Step 2 chat needs: the handle list and this batch's deliberate exceptions. |

## `data/`: reference data pulled from outside

| File | What we do with it |
|---|---|
| ~~`sitemap-state.md`~~ | **WRONG PATH, corrected 2026-09-02. This file is not in `data/`. It is at `deliverables/tracking/sitemap-state.md`.** The description was right: a snapshot of every live URL on the store, products and collections, refreshed before any footwear batch, used to answer questions the registry cannot, most importantly whether a competing version of a shoe is currently live, since the registry only knows about pages we have already optimized.<br><br>**Why the path matters more than a typo normally would.** Pack succession reads this file by rule: §3.2 says qualification is checked against the live sitemap and explicitly not against the registry, because the competing page is usually one nobody has optimized. **An agent that looks in `data/`, finds nothing, and proceeds concludes that no live sibling exists.** That is a false negative that hands a page an unqualified term it is not entitled to. It is B-FRESH-01's failure shape exactly, a check that runs, prints nothing unusual and is wrong, except that the cause here is not a stale file but a document pointing at the wrong shelf. **Documentation caused it, which means no freshness assertion would have caught it.** |
| `templates/ProSoccer_Matrixify_Template.xlsx` | A blank import file with the correct sheet name and column headers and no data. Copy it rather than rebuilding the format by hand. Verified present. |
| `gsc-exports/` | Search Console data pulls, kept so an analysis can be re-run without re-fetching. Verified present. |
| `shopify-exports/` | Product exports from Shopify. Verified present. |

**Also in `data/`, undocumented:** `ahrefs/`, `ga4-exports/`, `screaming-frog/`, `README.md`, and two national-team collection crawl JSON files.

## `strategy/`: planning documents

| File | What we do with it | State |
|---|---|---|
| `sprint-backlog.md` | **The live to-do list and decision record.** Every open issue with its evidence, what was decided, and why. When something is found but deliberately not fixed yet, this is where it goes with the reasoning attached, so it does not get re-argued. | **Active and heavily used** |
| `master-strategy.md` | Intended as the standing strategy document | **Empty template, and this one has a cost.** See the finding below. |
| `90-day-roadmap.md` | Intended as the quarterly plan | **Empty template** |
| `keyword-map.md` | Intended as the keyword-to-URL map | **Empty template, superseded** by the registry CSVs |

All four verified present 2026-09-02, and the three "empty template" labels are accurate in substance. **None of them is a zero-length file**, which is the part worth stating: `master-strategy.md` holds 28 non-blank lines, `90-day-roadmap.md` 31 and `keyword-map.md` 23, each made of a purpose statement, a "How to Use This File" block and an example row. The same is true of the three unpopulated `context/` files (39, 41 and 49 non-blank lines).

**FINDING: `master-strategy.md` is read at startup by every agent and returns nothing usable.** CLAUDE.md's startup protocol names it as step 4 of four, unconditionally, for every agent on every task. What an agent reads there today is **a set of prompts for writing a strategy rather than a strategy**: who owns the file, when to update it, and an instruction never to delete prior strategy. That is a worse failure than an empty file, because an empty file reads as absent while this reads as present. Every batch to date has run with no standing strategy in context, and the work has been steered instead by the dispatch prompt and the backlog. Whether to fill it is an open question for Mike, not a defect an agent should fix by writing a strategy into it.

## `work-log/`: the running journal

| File | What we do with it |
|---|---|
| `follow-ups.md` | **Open items that came up mid-work.** Smaller and more immediate than the backlog: things noticed in passing that should not be lost. |
| `<date>_*.md` | **Dated records of specific pieces of work**: claims reviews, analysis results, session handoffs. Written when a piece of work produces findings someone will need later. |
| `README.md` | Present but undocumented until 2026-09-02. |

Both original entries verified present 2026-09-02, nine dated files among them. **The most recent close entry is `2026-08-26_batch15.1-close.md`.** Batches 16 and 17 have none, so this folder currently understates what has shipped. That is step 15 output rather than a repository defect, but anyone reading the journal to reconstruct history will come up two batches short.

## `.claude/agents/`

One folder per agent containing `agent.md` (the agent's own instructions), `learnings.md`, and `briefings/` (a per-session record of what that agent did).

**CORRECTED 2026-09-02: `decisions.md` is not universal.** Verified across all seven agent folders. **Three have one: `competitor-intel`, `on-page-seo` and `technical-seo`.** Four do not: `content-writer`, `keyword-research`, `master-strategist` and `reporting`. Notably **ORIN, the agent that makes the most decisions, has no decisions file**, which is where the B-RANK-01 reasoning would naturally have lived. Reading the old row as written would have an agent look for a record that was never created and read its absence as data loss.

`.claude/settings.json` holds the permission list: routine commands like reading files, running scripts and committing are pre-approved, while destructive ones like force-push or recursive delete still prompt.

## Human-facing documents

| File | Purpose |
|---|---|
| `docs/workforce-v2-pipeline.md` | Narrative description of the batch flow. Line 3 cites the refactor spec below by path. |
| `docs/workforce-v2-refactor-promt.md` | The specification the current architecture was built from. Untracked until 2026-09-02, committed that day byte-for-byte. **The filename misspells "prompt" as "promt"** and was left as-is deliberately, because renaming requires updating the citation in `workforce-v2-pipeline.md` in the same commit. It is Mike's own source prompt text and contains em dashes, which is fine, since the language rules govern agent output rather than source material. If `docs/` is ever linted, this file will flag. |
| `docs/PROSOCCER_SEO_MASTER_REFERENCE.md` | **This document.** Added to the repository 2026-09-02. It previously existed only as a chat attachment, which meant it did not exist for anyone cloning the repository. |
| ~~`HOW_IT_WORKS.md`~~ | **NOT IN THE REPOSITORY (confirmed 2026-09-02).** No file of that name exists anywhere in the repo, under any casing, and nothing in git history has it. If a system explainer exists, it exists outside the repository, which by principle 4 means it does not exist for any agent. |
| ~~`seo-batch-workflow.svg`~~ | **NOT IN THE REPOSITORY (confirmed 2026-09-02).** No workflow `.svg` anywhere in the repo, including `assets/`. The file is understood to exist outside the repository, so this row described an external artifact as a repo one. **The known defect recorded against it still stands and is why it should not be committed as-is:** it labels the commit node "Review and commit, Mike", when ORIN commits autonomously at batch close and Mike owns the push, so it assigns the commit to the wrong party and omits the push gate entirely. Principle 5 applies. Committing it would put a diagram that teaches the wrong ownership model in front of every reader; fix the diagram first, then commit it, then restore this row. |
| `deliverables/client-presentations/2026-05-27_pdp-optimization-framework.md` | Untracked as of 2026-09-02. Untouched since May, listed in the Batch 17 dispatch handoff as out of scope. Same shape as the v2 spec was before it was committed: an untracked document that may or may not have a tracked citation pointing at it. Needs a decision. |

---

# PART 3: THE RULES

## 3.1 Keyword hierarchy

**Collections own broad terms.** Brand, model, club, category. Anything where a searcher would be happy with any of a dozen products.

**Product pages own specific terms.** Model + tier + cut + surface + pack + width + colorway. Terms that point to exactly one product.

**The test:** if someone searching this would be satisfied by twelve different products, it belongs on a collection page.

**Volume never overrides hierarchy.** If a product page's only honest keyword gets 20 searches a month while the collection term gets 60,000, the product page takes the 20. Chasing the bigger term means two of your own pages competing for it, and the product page loses that fight regardless.

**Sub-floor lock.** Sub-floor means fewer than 100 searches a month. When no higher-volume term is valid for that page under the hierarchy, the page takes the exact qualified term and it is flagged sub-floor. It does not reach for a broader term belonging to something else.

**Ceded terms.** Keywords deliberately handed from product pages to a collection are recorded in `collections-master.csv`, one policy per family, so the decision applies automatically to every future batch. Currently in place for Manchester United, Real Madrid, Liverpool, Barcelona, Arsenal, Bayern Munich, Chivas and Mizuno.

### The earned-term rule (ranking-page batches only, added 2026-09-02)

On a page selected for already earning impressions, the page adopts the term it already ranks for rather than being assigned a new target. The authoritative text is in `context/workforce-conventions.md` and is quoted in `SEO_BATCH_PROCESS.md` §2. It applies only to ranking-page batches. New-product batches continue to assign primaries through KIRA in the normal way.

### OPEN DECISION: hierarchy versus earned term

**This is not resolved and must not be resolved by an agent.**

The hierarchy above says collections own any term a searcher would be satisfied by multiple products for, and that volume never overrides that. The earned-term rule says a ranking page adopts what it earns. These conflict whenever a PDP earns a term the hierarchy assigns to a collection.

The worked case is `messi cleats`. Four ProSoccer PDPs earn it simultaneously, and a junior page is better positioned on it than the adult Elite page that would have been optimized for it. The term carries no tier, cut, surface, age band or pack, so by §3.1's own test it is a collection term. By the earned-term rule the page takes it.

Three resolutions were identified and none was chosen:

1. The page takes the term, and four-way self-competition is accepted
2. The page takes a configuration-qualified variant, and the plain term cedes to the F50 Messi collection
3. The page is optimized and the term assignment is held pending a decision on the whole Messi cluster

Logged as B-CANNIB-03. Until it is decided, a ranking page earning a hierarchy-level term is escalated to Mike rather than assigned by rule.

**A related distinction not yet made anywhere:** earning a term and holding it as a registry primary are different facts. A detection-gap batch surfaces impression overlap, which is not the same as an assigned-primary collision. The registry answers the second question and nothing currently answers the first.

## 3.2 Pack succession

Footwear brands release the same shoe repeatedly in new colorways under new pack names, several times a year. ProSoccer carries multiple packs of the same shoe at once, and each stays live as long as stock exists.

**When qualification is needed.** A pack name is added to the keyword only when another live page exists for the same model, tier, cut and surface. Checked against the live sitemap, not the registry, because the competing page is often one nobody has optimized.

**Who keeps the plain term.** The incumbent, meaning the page earning the most search impressions at that configuration over the trailing 90 days. Where search data is **absent or below threshold**, the earliest-released live pack is the fallback. Stock level does not affect this: a sold-out page keeps its keyword, because search equity does not disappear when inventory does.

**Measure the term, not the page (added 2026-09-02).** Incumbency is decided on impressions for the contested term at that configuration. Total page impressions are a different quantity and must not be substituted for it. A page can lead its siblings on total impressions while trailing them on the specific term in dispute, because total impressions aggregate every query the page earns, most of which are not the contested one. An incumbency argument that cites page totals has not established incumbency, whatever conclusion it reaches.

Every newer pack takes a pack-qualified keyword. A season code is added where a pack name repeats across years.

**Churn guard.** Incumbency only moves on sustained change across two consecutive measurement periods, and never for an already-published page without an explicit decision.

**When a page is retired.** If one live sibling remains, the plain term passes to it. If several remain, it goes to the model collection. If none remain, it goes to the collection or its redirect target.

**Forward-only.** Published pages are not retargeted on account of this rule alone.

**On volume.** Pack-qualified terms have almost no search volume, by design. A pack product page's job is conversion and navigation, not ranking for the model name. The model name belongs to the collection.

## 3.3 Licensing and claims

**No brand in this catalog holds a standing FIFA license.** adidas obtained a specific license covering the 2026 World Cup, which permits FIFA and World Cup terminology on adidas 2026 World Cup product pages. It is tied to that one event and does not extend to future tournaments.

**Nike, New Balance, Mizuno, Kelme, Umbro and Hummel hold no FIFA license.** Their pages carry no FIFA or World Cup language at all, even for a soccer cleat sold during a World Cup year.

**Club heritage claims are qualitative only.** No trophy counts, no "most successful," never naming the Champions League. Domestic leagues can be named directly.

| Club | Bar |
|---|---|
| Real Madrid | Strictest. No European Cup count, no superlatives. La Liga nameable, European competition generic. |
| Liverpool | One permitted European-scoped superlative, because it is factually safe. No English league count. |
| Manchester United | "Among England's most decorated." Heritage framing, no counts. |
| Bayern Munich | "One of Germany's most storied clubs." Bundesliga nameable, European generic. |
| Arsenal, Barcelona, Chivas | Qualitative honours only, domestic league nameable |

**Every spec and heritage claim traces to that product's scrape or is qualified.**

**Scrape-wins, with one exception.** The live product page is normally the authority on specs. The exception is where the store's own page erases a distinction the brand makes: adidas uses `Nanostrike+` on Elite and `Nanostrike` below it, while ProSoccer renders both in capitals. In that narrow case the brand source wins. If the scrape is simply silent, the fact stays out.

## 3.4 Copy conventions

- **adidas** is always lowercase. Every other brand is capitalized in customer copy.
- **Cleats** or **shoes**, never "boots" and never other UK terminology.
- Turf and indoor products say "shoes" because the live product titles do.
- **No em dashes** anywhere.
- **No stock levels, size runs or variant availability** in body copy. Shopify displays live variants.
- **No store or Pasadena mention** on product pages. That belongs on the homepage and collection pages.
- Brand technology names in title case, not capitals.
- No prices in body copy.
- FAQ heading is `FAQs about [short product name]` on product pages, plain `Frequently Asked Questions` on collections.

### Shipping and customization timings

Authoritative source is `context/shipping-customization-facts.md`. State exactly, never round.

| Tier | Timing |
|---|---|
| Standard | 1 to 2 business days |
| Customized name and number | 2 to 3 business days |
| Personalized jerseys | 5 to 10 business days |
| Team and club orders | up to 4 weeks |

Name and number customization is selected **on the product page**, not at checkout. A name and number add is **not** a personalized jersey; the tiers are separate and must not be merged.

Correct: "Add your name and number right on this page. Name and number orders ship in about 2 to 3 business days."

### Forbidden-phrase lists

When a phrase is barred so a sibling page does not reuse it, the barred phrase must not be contained inside a phrase we approve. The check matches on substrings, so barring a short phrase will also flag a longer approved one that contains it. For the same reason, never put a brand name on a forbidden list.

## 3.5 Meta fields

**Meta title.** Maximum 48 characters for the part you write; the theme adds the store name automatically. Never type the store name. Never end with a manufacturer brand after a pipe. A pack or product-line suffix is fine. Brand at the front is correct.

**Priority when it will not all fit:** brand, model, generation, configuration, pack. The pack drops first, and when it does, the meta description must name it instead.

**When the cap forces a choice between a spelled-out configuration and the pack,** the pack wins and the configuration abbreviates, using an abbreviation the store's own titles already use. Never shorten a pack name. Never drop the brand.

**Meta description.** 120 to 160 characters. Full sentences. No "Product Name: fragment" opener. What it is, the key benefit, a light call to action.

## 3.6 Customer avatars

Four buyer profiles. **Full detail lives in `context/04-customer-avatars.md`**, which carries each avatar's age, budget, buying triggers, concerns and voice-of-customer language. SCRIBE reads it every batch.

| Avatar | In short |
|---|---|
| Carlos, the Fan | Buys jerseys. Concerned about authenticity. |
| Tyler, the Athlete | Seventeen. Buys cleats, reads specs, follows drops, funds gear himself. |
| Jennifer, the Mom | Buys cleats for her kid. Wide feet, safety, value, growth spurts. |
| Mike, the Coach | Bulk team orders, buys on utility. |

A youth product is written for the parent buying it, not the child wearing it.

**Known gap:** the adult self-funded craft buyer, 25 to 40, plays adult rec or Sunday league, buys on materials and provenance, price-insensitive at the flagship tier. Recurs on every leather flagship. Tracked as B-AVATAR-01.

## 3.7 Structure and length

**Tier naming across brands.** Nike runs Elite > Pro > Academy > Club. adidas runs Elite > Pro > League > Club. Nike Academy corresponds to adidas League.

**Word bands by tier,** with 15 words of tolerance either side, always the product's own band and never inherited from a sibling:

| Tier | Band |
|---|---|
| Elite | 400 to 450 |
| Pro | 340 to 390 |
| League / Club | 280 to 340 |

**Care and Maintenance section required** for footwear, jerseys, apparel, goalkeeper gloves and balls. Not required for accessories, flags or small merchandise.

**Structure sharing.** When a sibling page hands its structure to the next one, it passes the section *sequence* only: category labels, no titles, no prose, no metaphors. Mirror the structure, never the wording.

**Heading case.** Editorial headings are sentence case. Structural headings (`Product Details:`, `Care and Maintenance`, `FAQs about`) are Title Case.

**Internal links.** One or two per page, each confirmed working, placed where the copy naturally refers to the target rather than defaulting to the same two spots every time. Links go in the main description only, never the short description. **External links are not used on product pages.**

## 3.8 Ranking-aware posture

**The band table that stood here until 2026-09-02 was obsolete and is removed.** It was written before the four-field import existed. It cautioned against changing the title and the H1, neither of which the pipeline can write, and it was silent on the meta title, which the pipeline rewrites on every page. On a batch made entirely of ranking pages, that silence covered the only field actually in play.

Copied verbatim from `context/workforce-conventions.md` as committed at `3449bfd`, section "The bands (v2), keyed on EARNED-TERM position". **That file is the source of truth because it is what SCRIBE reads. If the table changes there, recopy it here rather than editing this copy.**

| Earned-term position | Posture |
|---|---|
| **Under 5** | Protect the Meta Title fully. Exact-match phrasing of the earned term preserved. Changes to that field require Mike per page. Iterate on Meta Description, Short Description and Long Description. The brief MUST carry the WARNING line. |
| **5 to 10** | The Meta Title may be improved but MUST retain the earned term in exact-match form. Everything else is open. No per-page Mike gate; the brief states the earned term and its position so the constraint is visible and auditable. |
| **10 to 20** | Standard recommendations. Carry the earned term into the Meta Title where it fits naturally. Not binding. |
| **Over 20, or not ranking** | Standard recommendations. Nothing to protect; treat as a fresh attempt. |

Three things that must survive into whatever text lands here:

**The H1 standing rule (Mike, 2026-08-30).** No brief recommends an H1 on a PDP, in any band. On a ProSoccer PDP the H1 renders from the Shopify product title, and product titles are never changed, so an H1 recommendation names a field the workforce cannot write. **Collection pages are explicitly scoped out of this rule,** because their H1 is editable.

**The band derives from the term the page earns,** not from the assigned primary string, and the derivation source is named in the brief, the input's gate-meta block and the Step 2 handoff.

**B-RANK-01 is open.** The condition used to select a page into a detection-gap batch is currently also used to derive its band. A page can fail the selection condition on every individual query while holding position that a rewrite could damage. Until this is split, a page in that state is escalated rather than banded by rule. See the detection-gap section in Part 1 for the worked case.

Enforcement note: `check_ranking_input` is the sixteenth gate check and it verifies that a ranking input is present and that the earned term appears where the band requires. **Presence of a ranking input is not correctness of the band derived from it.** The check passed on DH6621 while the band was wrong.

## 3.9 What never changes

Product titles. URL handles, which are flagged only and need a redirect coordinated with the developer. Tags, taxonomy, variants, prices. The import file physically cannot touch any of them, because those columns are not in it.

---

# PART 4: HOW QUALITY IS ENFORCED

Four layers, deliberately different in kind, because each catches things the others cannot.

## The automated gate

A script that reads every brief in the batch and runs 16 checks. It either passes or it fails with the exact brief and line number. It cannot be reasoned with and it does not accept an agent's word for anything.

The sixteen, named from `_gate-run.json` on 2026-09-02: `voice`, `heading-levels`, `section-presence`, `customization-claims`, `url-handle`, `price-in-body`, `heritage-counts`, `fabrication-hedge`, `fifa-terms`, `forbidden-phrasings`, `word-band`, `brand-casing`, `cannibalization`, `cross-brief`, `registry1-present`, `ranking-input`.

`ranking-input` is the newest and was added for the ranking-page work. Note what it does and does not do: it confirms a ranking input exists and that the earned term appears where the band requires. It does not confirm the band was derived correctly. It passed on Batch 17's DH6621 while that page's band was wrong.

Two known limits carried forward: the cannibalization check is exact-match only, with no containment or token-subset detection, so that class is caught by ORIN's manual pre-dispatch pass rather than by the gate. Meta title length and meta description length and format are not gated and are enforced by SCRIBE plus the claims review.

**A check that cannot run counts as a failure.** If the file a check depends on is missing, the gate fails rather than quietly skipping that check and reporting success. There is no path where something goes unchecked and the batch still passes.

**A check that legitimately does not apply is silent.** An adidas page skipping the FIFA restriction is not a skipped check, it is a rule that does not apply.

**The gate writes its own record** to `_gate-run.json` in the batch folder: pass or fail, which checks ran, which did not, and when. That way "the gate passed" is something you can look up rather than something someone remembers.

## The claims review

A human-style reading pass over the actual copy, looking for what pattern-matching cannot catch: a performance claim with no source behind it, a statement about a club's current form that will be wrong in three months, a specification that sounds plausible but was not in the scrape.

## The registry

The three CSV files. Every keyword assigned to every page, plus every keyword deliberately handed to a collection. This is what makes the conflict check possible, and it lives inside the repository so the agents can read it directly rather than depending on a spreadsheet they cannot open.

## Human review

Mike reads the briefs before they are committed and checks the live pages after import. The machine confirms the structure is right; the human confirms the copy is any good.

## What is not automated

Meta title and description length and format are checked by the writers and the claims review, not by the gate. Sibling-page conflicts for footwear require checking the live sitemap, because the registry only knows about pages already optimized.

---

# PART 5: BUSINESS AND NICHE

## The catalog

Roughly 15,000 products. Cleats, jerseys, turf shoes, indoor shoes, balls, training gear. Physical stores in Pasadena and Irwindale, California.

Brands: Nike, adidas, Puma, New Balance, Mizuno, Kelme, Umbro, Hummel.

## How footwear is structured

**Model lines.** Nike: Phantom, Mercurial (Vapor and Superfly), Tiempo (Legend, Maestro, Ligera). adidas: Predator, F50, Copa. New Balance: Furon, Tekela. Mizuno: Morelia.

**Tiers,** most to least expensive: Elite, Pro, Academy, Club, League.

**Surfaces:** FG (firm ground, natural grass), MG (multi ground), FG/MG (both), AG (artificial grass), Turf, Indoor. Turf and indoor products are "shoes," everything else is "cleats."

**Cuts:** High (with an ankle collar) and Low. Some lines split further on tongue construction, such as Predator's Fold-Over Tongue and Laceless versions.

**Age tiers:** Adult, Junior (grade school, roughly sizes 1 to 6), Kids (little kid, roughly 11K to 13.5K), PS (preschool). When a model splits by size range it becomes two separate products sharing a SKU stem, so the SKU alone does not identify a product and the URL is the reliable key.

**Packs.** Brands release several packs a year: the same shoe, new colorway, new pack name. Shadow, Breakout, Break 'Em, Chaos vs Control, Road to Glory, Born For Goals, Scary Good, Radiant Blaze, Attack, Immortal DNA, Coral Blaze, Electric Stealth, Vivid Horizon, Neon Tide, Bright Black, Prism White. Player-signature editions (Messi, Haaland, Mbappé) are packs in their own right, and the player name is the pack qualifier.

**Season codes:** SP (spring), SU (summer), FA (fall), HO (holiday), plus the year. Within a year: SP, then SU, then FA, then HO.

## What this means for SEO

Search demand builds for a shoe over its life, while packs rotate every few months. So the newest products carry the least search demand, and the pages holding real demand tend to be older packs nobody has optimized yet.

Model-level terms carry most of the volume, and by the hierarchy rule those belong to collection pages, not product pages.

## Handle conventions

ProSoccer's URL handles abbreviate where the product titles spell things out: `man-united`, `ls`, `fg`, `in`, `tf`, `ll`. Pack suffixes are sometimes absent entirely.

**Handles always come from the briefs, word for word.** Rebuilding one from a product title returns no matches.

Collection handles do not reliably describe their contents. `/collections/indoor-soccer-shoes` is the **kids** collection; the adult equivalent is `/collections/indoor`. So **a collection link is checked by reading its heading and product count, not by seeing whether the URL loads.** A page that loads but serves the wrong audience is more dangerous than one that 404s, because the 404 gets noticed.

## Integrations

Shopify Plus with the Hyper theme by FoxEcom. Matrixify for bulk import and export. Tapcart for the mobile app channel, with pre-launch tag gating through Shopify Flow. Shopify POS in both stores. Klaviyo for email and SMS, managed separately. Google Search Console, GA4, Google Ads. DataForSEO for keyword volumes. Firecrawl for page scraping.

---

---

# PART 5B: THE COLLECTION WORKSTREAM (NOT IN PRODUCTION)

**No collection page has been optimized through this pipeline.** Everything in this document describes PDP work. `collection-page-playbook.md` exists but has never been used, and nothing here should be read as a collection workflow.

This section records what has been decided and what has not, so the next team does not re-derive it.

**What is genuinely different from a PDP, and must be designed for rather than inherited:**

1. **Keyword hierarchy runs the other way.** Collection pages own the head terms, the ones §3.1 has spent this whole pipeline keeping off product pages. A cannibalization guard is required in both directions, because the risk is no longer only PDP-takes-collection-term but also collection-takes-a-term-a-PDP-already-holds.
2. **The content model is a buying guide,** not a spec sheet. What is in the category, how to choose within it, who each option suits. The PDP structure does not transfer.
3. **The gate must become page-type aware.** Several of the sixteen checks are PDP-specific by construction. `section-presence` asserts the PDP section set. `word-band` bands by footwear tier. The FAQ heading rule differs (`FAQs about [product]` on a PDP, plain `Frequently Asked Questions` on a collection). Running the PDP gate over a collection brief would fail correct work and pass incorrect work.
4. **H1 is editable on a collection.** The standing rule barring H1 recommendations is PDP-scoped precisely because of this. On a collection the H1 is in play, which changes what the ranking-aware posture means there.

**Open before any of it starts:**

- Are these mostly existing collections, meaning copy and keyword work only, or new ones, which brings URL, taxonomy and navigation decisions requiring Jorge and Misha, plus a merchandising step?
- The 61 inherited white-label primaries on `collections-master.csv` have never been audited. That audit is the precondition, because the cannibalization guard cannot run against an unverified claim set.
- Do collection briefs ship through the same Matrixify four-field path? The metafield names differ for collections and this has not been tested.

**Build order, if it proceeds:** audit the inherited primaries, define the collection playbook, extend KIRA for head-term research with the two-way guard, make the gate page-type aware, then pilot two or three collections with heavy human review before any scaling.

---

# PART 6: THE PRINCIPLES

Sixteen working rules, read at the start of every session.

**1. A report is not verification.** When an agent says it did something, that is a claim, not proof. Open the file and look. The report and the work are two different things, and only one of them is the work.

**2. A check that did not run is not a pass.** If a check was skipped for any reason, the result is unknown, not clean. Silence has to be treated as failure, or a missing check looks identical to a passing one.

**3. Nothing self-referential counts as a check.** Comparing a document against a value recorded inside that same document proves only that it is internally consistent. Real verification means going out and fetching the live page.

**4. Rules that live outside the repository do not exist.** If an agent cannot read the file, it cannot follow the rule in it. A policy in a Google Sheet or someone's head is not enforced, however clearly it is written.

**5. Examples teach louder than rules.** A worked example in an instruction file is copied more faithfully than the rule beside it. When the two disagree, the example wins. So examples get audited whenever a rule changes.

**6. Numbers, not adjectives.** "In band," "roughly," "sub-threshold" all hide the actual value. A figure can be checked; a description of a figure cannot.

**7. Codify at the point of discovery.** When a rule is worked out, write it into the canonical file immediately. Deferring it means the next batch hits the same problem, because nothing changed except one conversation.

**8. Cross-file contradictions are a recurring class.** When two files describe the same rule and only one gets updated, agents follow whichever they happen to read. Audit for it deliberately rather than waiting to trip over it.

**9. An exemplar must name its source.** Any example held up as correct should cite the SKU, the brief it came from, and the date it was verified live. If the source cannot be named, it is not an exemplar, it is something somebody wrote.

**10. An exemplar must satisfy every rule in the repository,** not just the one it is demonstrating. An example illustrating heading structure can still be teaching the wrong brand capitalization.

**11. An artifact producing no evidence fails silently.** A log that never leaves the machine, a test asserting the wrong thing, a tool that fills in a default date. Each appears to work perfectly. Confirm a new artifact exists in a fresh clone, not just locally.

**12. When a failure looks partial, check whether something upstream is broken everywhere.** Three pages wrong out of ten usually means all ten were affected and seven were rescued by something downstream. Look up the chain before concluding it was three.

**13. An agent's self-report about its own output is not evidence.** An agent measuring its own word count uses its own method, which is exactly what the deterministic check exists to standardize. Re-derive any figure from the gate before it enters a report, a commit message or the registry.

**14. Do not assert a tool's behavior without testing it.** Infer, flag, then verify. An untested claim stated as fact costs more than the uncertainty it was meant to resolve. This extends to a tool's existence: `crossfile_audit.py` was described in this document in detail, cited twice as something to run, and does not exist. A described tool is not a tool. Matches `SEO_BATCH_PROCESS.md` §5 rule 6.

**15. A check that ran against stale data is not a pass, and it is harder to catch than one that did not run.** Principle 2 covers the check that skips and says so. This is the check that runs, prints nothing unusual, exits 0, and is wrong, because its cached input aged out. Assert the snapshot's freshness before trusting the verdict, and fail on stale rather than warn. Batch 15.1: a twelve-day-old sitemap cache would have reported no live pack sibling for both Sparkfusion SKUs, because the two pages that are their siblings were published inside those twelve days. Nothing in the output would have differed from a correct run. Matches `SEO_BATCH_PROCESS.md` §5 rule 7.

**16. A report describing analysis that produced no artifact is not analysis (added 2026-09-02).** Distinct from principle 1, which covers an agent overstating work it did perform. This is work held only in the agent's context and lost, then reported in the past tense so it reads as finished. A session reported a completed scrape, an incumbency resolution across four sibling pages, a full metrics table and a locked read-out for a SKU that had no file of any kind anywhere on disk. The tell is that every number in it was unreproducible. After any interruption, verify from disk before building on what the previous session said it did.
