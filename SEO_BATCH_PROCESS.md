# ProSoccer SEO Batch Process

**Owner:** Mike Hakopyan, 7 Rock Marketing LLC
**Last updated:** 2026-07-28
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

**Never:**
- Runs git commits or pushes
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
- Every git commit and push. Commits are Mike's by default; **push is the hard gate.** Nothing reaches origin without Mike running it. If the workforce commits locally, those commits stay unpushed until Mike reviews the diff.
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

- Gate hardening spec: checks queued, to be built before Batch 10
- 20 meta title brand-suffix violations found across all batches. KA6868 fixed manually 2026-07-28; 19 remain live, awaiting fix-forward.
- Meta title and meta description format rules being codified into the playbook
- Collection page workstream, pending audit of the 61 inherited white-label primaries
- `products-master.csv` `product_id` column holds the SKU, not the Shopify numeric ID
