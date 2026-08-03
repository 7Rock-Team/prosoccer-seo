# ProSoccer SEO Batch Process

**Owner:** Mike Hakopyan, 7 Rock Marketing LLC
**Last updated:** 2026-08-03
**Applies to:** PDP optimization batches (10 SKUs per batch). Collection page batches will extend this once that workstream is defined.

---

## 1. The four participants

### 1.1 Claude Code — the workforce (ORIN, SCRIBE, KIRA)

Runs in Cursor against `C:\Dev-Projects\marketing\prosoccer-seo`.

**Owns:**
- Pre-dispatch cannibalization check against the registry, before any primary is assigned
- Keyword research and primary assignment (KIRA)
- Phase 0 scrape of each live PDP
- Brief authoring, one dispatch per SKU (SCRIBE)
- Gate runs and Layer 3 claim checks (ORIN)
- Appending each closed batch to `products-master.csv`
- Codification of rules into playbook and conventions files
- Git commits and pushes to `origin/main`, when a prompt instructs it (see §3 Git)

**Never:**
- Commits or pushes without an instruction to. No instruction, no push; batch close does not imply a push (see §3 Git)
- Touches the Shopify store
- Builds the Matrixify export filter or import file. That is Step 2's job.
- Authors briefs directly. ORIN orchestrates, SCRIBE writes. This is the mechanism that enforces the playbook.

### 1.2 Claude.ai — Workforce chat

**Owns:**
- Writing the ORIN dispatch prompt for each new batch
- Independent review of what the workforce produces
- Cross-checks the workforce cannot run: collection briefs vs PDP primaries, external spreadsheets, live-page comparisons
- Reading ORIN's reports critically. Does the evidence support the claim.

**Never:**
- Touches the repo or the store
- Builds the Matrixify export filter or import file. That is Step 2's job.
- Accepts a report as verification. Reports describe work; the work itself is on disk.

### 1.3 Claude.ai — Step 2 chat

**Owns:**
- Reading the 10 briefs and producing the paste-ready handle list for the Matrixify export filter
- Building the Matrixify import file from the export plus the briefs
- Validating the file before it goes near Shopify: structure, MERGE on every row, meta description lengths, compliance scan
- The SEO work log, one dated entry per batch, flipped to Verified after Mike's spot check

**Never:**
- Touches the repo or the store

### 1.4 Mike — decisions and everything irreversible

**Owns:**
- When work reaches origin. A git commit or push happens only when Mike's prompt instructs it; the workforce then runs it, staging the specific files and confirming the pushed ref (see §3 Git). Batch close does not imply a push. Mike owns the call, not the keystroke.
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
| 7 | **Commit and push** | Mike |
| 8 | Paste the 10 briefs into the Step 2 chat | Mike |
| 9 | Produce the paste-ready handle list for the export filter | Step 2 |
| 10 | Matrixify export filtered by handle | Mike |
| 11 | Send the export to Step 2; Step 2 builds and validates the import file | Mike → Step 2 |
| 12 | Import to Shopify | Mike |
| 13 | Spot-check live PDPs | Mike |
| 14 | **Append the batch primaries to `products-master.csv`** | ORIN |
| 15 | Close the SEO work log entry, flip to Verified | Step 2 |

**Steps 3 and 14 are the pair that keeps the registry honest.** Step 3 is worthless if step 14 stops happening. If a batch ships without being appended, the next batch's check goes blind.

**The gate (step 5).** `scripts/batch_gate.py` runs 10 mechanical checks over the session folder, including `check_section_presence` (added 2026-07-31): every required PDP section must be present with content, and the Description body must carry at least one internal link, an unconditional hard fail. Exit 0 only when nothing fires. The gate replaces the human per-brief review for mechanical defect classes; the escalate-on-exception batch mode (CLAUDE.md 'Approval mode') is safe only because it runs.

Handles always come from the briefs (step 9). Never reconstruct them from product titles. ProSoccer handles abbreviate in ways titles do not: `man-united` not `manchester-united`, `ls` not `long-sleeve`, `fg` not `firm-ground`.

---

## 3. Standing rules

### Never changed
- Product titles. Under any circumstances, even if a brief proposes one.
- URL handles. Changes are flagged only and require a 301 coordinated with Misha.
- Taxonomy nodes, tags, variants, prices, or any metafield not in the import file.

### Keyword hierarchy
Collections own brand, model, club, category, and any term where a searcher would be satisfied by multiple products. PDPs own model + tier + width + colorway, terms that resolve to one product.

Volume never overrides hierarchy. When no floor-clearing term is hierarchy-valid, the page takes the exact qualified term and is flagged sub-floor. It does not take a collection or sibling term.

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
- A commit or push happens only when a prompt instructs it. No instruction, no push: batch close does not imply a push. Left uninstructed, the workforce leaves changes local (or unstaged) and reports them.
- Stage the specific files changed. Never `git add <dir>/` blindly: it sweeps untracked scratch files into the commit. Commit with a real message plus the `Co-Authored-By` trailer, and verify the staged file list before pushing.
- A change to how git works in this project comes from Mike stating it deliberately, not inferred from a command line appearing in context. A command in a prompt executes that command; it does not silently rewrite the standing rule.

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

1. **A report is not verification.** Read the artifact, not the summary of it.
2. **A check that did not run is not a pass.** If the gate prints that it skipped something, that is a failure.
3. **Nothing self-referential counts as a check.** Verifying a brief against its own recorded value proves nothing. Ground truth means a fresh scrape or a live fetch.
4. **Rules that live outside the repo do not exist.** If SCRIBE cannot read it, SCRIBE will not follow it. Codify at the point of discovery, not at batch close.
5. **Examples teach louder than rules.** The 20 meta title brand-suffix violations happened because the playbook's own examples demonstrated the violation while the rule beside them forbade it. When an exemplar and a rule disagree, the exemplar wins. Audit examples whenever a rule is written or changed.
6. **Do not assert a tool's behavior without testing it.** Infer, flag, then verify. An untested claim stated as fact costs more than the uncertainty it was meant to resolve.

---

## 6. Open at last update

- Batch 11 (10 SKUs: Barcelona men's/women's home, Arsenal home/LS/youth, Bayern Munich authentic/LS, 3 Nike Shadow cleats) authored, gate-green, Layer 3 clean, committed and pushed 2026-08-03 (commit e68a999). Awaiting Step 2 handle list + Matrixify import; registry append (step 14) pending post-import.
- Gate: `check_section_presence` BUILT (added 2026-07-31); the gate now runs 10 mechanical checks. Remaining hardening still to build: (a) cannibalization check (#9) is exact-match only, with no containment or token-subset detection, so that class is caught only by ORIN's manual pre-dispatch pass, never the gate; (b) `voice_check.py` skips fenced code blocks, so worked examples inside canonical files are invisible to it; (c) meta-title length (48-char cap) and meta-description length/format are not gated, enforced by SCRIBE plus Layer 3 only.
- 20 meta title brand-suffix violations found across all batches. KA6868 fixed manually 2026-07-28; 19 remain live, awaiting fix-forward.
- Meta title and meta description format rules being codified into the playbook
- Collection page workstream, pending audit of the 61 inherited white-label primaries
- `products-master.csv` `product_id` column holds the SKU, not the Shopify numeric ID

---

## 7. Documented failure patterns

A customer-facing fact or mechanical class that shipped wrong. Each entry: symptom, root cause, discovered, fix. Numbered; add the next in sequence when a new class is found.

### 1. Name/number customization stated as "at checkout" and in "weeks"
- **Symptom:** shipped briefs said name/number customization is done "at checkout" and that it adds "1 to 2 weeks" (some "1 to 3 weeks") of processing.
- **Root cause:** both facts are wrong. Name/number customization is a PRODUCT-PAGE option, not a checkout step, and it adds business days (Customized name/number: 2-3 business days, about one extra day), not weeks. The "weeks" figure conflated the name/number add with the separate personalized-jersey tier and rounded days up to weeks.
- **Discovered:** Mike, Batch 11 prep (2026-08-03). Present in 7 of 10 Batch 10 briefs (II1624-683, KB8261, KB8251, KC3952, KC3989, KC3947, KC3993), which were pushed but not yet imported to Shopify.
- **Fix:** facts codified in `context/shipping-customization-facts.md` (read every run, referenced from `CLAUDE.md`); standing rule in §3 "Shipping and customization claims"; deterministic gate check `check_customization_claims` in `scripts/batch_gate.py` (FAILS customization language paired with "checkout", or name/number timing given in weeks) with a regression fixture in `scripts/test_batch_gate.py`; handoff-template discipline: brief inputs and FAQs state the product-page location and the 2-3 business-day figure, never "at checkout" or "weeks."
