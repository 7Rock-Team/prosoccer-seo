# Matrixify Import File Template (reference)

Reference for the shape of a Matrixify product-import file (batch SEO title, meta description, short description, and body updates for a set of PDPs).

## Scope: who owns this

The SEO workforce (ORIN and the specialists) does **not** build the Matrixify export filter or the import file. A separate process (the "Step 2" Claude.ai chat) owns both, working from the briefs and Mike's export. The workforce handoff to that process is the **briefs themselves, plus the handle list when asked**. Everything downstream of that handoff, including the import file, belongs to Step 2. This document is reference for that build step, not a workflow the workforce runs.

## Two valid forms (both import correctly)

Matrixify accepts more than one shape, and both of these import correctly. This was verified against Batch 9: the live UF3F51W page had its body, meta title, meta description, and short description all applied from the imported file.

1. **Seven-column XLSX (documented default).** A workbook with a sheet named exactly `Products`, carrying `ID` plus the metafield-syntax headers. Preferred because the sheet name auto-resolves the entity and the numeric `ID` is a stronger match key than the handle.
2. **Six-column CSV (also works).** The same columns minus `ID`, with bare metafield names (`title_tag`, `description_tag`, `new_short_description`). Bare metafield names are **accepted**, not ignored. The only difference from the XLSX form is that a CSV carrying `Handle` and `Command` (columns shared by the Products and Collections entities) makes the target entity ambiguous, so Matrixify shows a "Sheets require entity selection" prompt. Resolve it by picking **Products** and the import proceeds. Batch 9 imported successfully from exactly this CSV form.

Use the XLSX form by default for the two reasons above (entity auto-resolves, numeric ID is the stronger key). Reach for the CSV form when a numeric-ID export is not on hand; keying on `Handle` alone is sufficient, as Batch 9 proved.

## The seven columns (XLSX default form)

Spelled and cased exactly as below. Matrixify's metafield syntax is `Metafield: <namespace.>key [type]`.

```
ID
Handle
Command
Body HTML
Metafield: title_tag [string]
Metafield: description_tag [string]
Metafield: products.new_short_description [multi_line_text_field]
```

Column-by-column:

- **ID**: the Shopify numeric product ID, stored as a TEXT string (see "The ID column" below). Not the SKU. Omit this column in the six-column CSV form.
- **Handle**: the product URL handle, live-verified. This is the match key when `ID` is absent.
- **Command**: `MERGE` on every row. MERGE updates the named fields on the existing product and leaves everything else untouched.
- **Body HTML**: the product description body (`body_html`), the accordion content below the images.
- **Metafield: title_tag [string]**: the SEO / browser title. (Bare `title_tag` in the CSV form.)
- **Metafield: description_tag [string]**: the meta description. (Bare `description_tag` in the CSV form.)
- **Metafield: products.new_short_description [multi_line_text_field]**: the hero-block short description above Add to Cart. (Bare `new_short_description` in the CSV form.)

No **Title** column. Title here would mean the product's storefront name (`title`), which an SEO batch does not change; including it risks overwriting the product name. The SEO title lives in `title_tag`, not in `Title`.

## File format: XLSX with a sheet named "Products"

- Format: **XLSX** (the default form).
- Sheet name: exactly **`Products`**.

The sheet name is how Matrixify auto-detects which entity the file targets, so the XLSX form never shows the entity-selection prompt. The CSV form does (see "Two valid forms" above); pick Products to resolve it.

## Filename convention

```
ProSoccer_SEO_Batch{N}_{ProductCount}_Products.xlsx
```

Example: `ProSoccer_SEO_Batch9_10_Products.xlsx` for the 10-product Batch 9 file.

## The ID column: numeric Shopify IDs, stored as text

- The value is the Shopify **numeric product ID** (for example `9553887625471`), not the SKU.
- Store it as a **TEXT string** in the cell, not a number. As a number, the spreadsheet can reformat it into scientific notation or drop precision, which breaks the match.
- The numeric IDs are **not on disk in this repo**. `deliverables/tracking/products-master.csv` holds the SKU in its `product_id` column, not the numeric ID (that column is misnamed; see `work-log/follow-ups.md` entry dated 2026-07-28). Source numeric IDs from a Matrixify export filtered to the batch's handles, and do not invent or derive them.
- The numeric ID is a **preference, not a requirement**. Handle-keyed matching (no `ID` column) imports correctly, as Batch 9 did. Use the numeric ID when an export is on hand because it is the stronger match key.

## Canonical blank template (copy this for the XLSX form)

A committed blank template for the XLSX default form lives at **`data/templates/ProSoccer_Matrixify_Template.xlsx`**:

- one sheet, named exactly `Products`
- the seven headers in row 1, byte for byte
- zero data rows
- the `ID` column pre-formatted as TEXT, so a pasted numeric ID stays text and does not turn into scientific notation

Copy it, rename it per the filename convention, and fill in the rows. It is deliberately **blank, not a copy of a past batch**, so no stale IDs or stale live copy get carried into a new batch. If it is ever lost, rebuild it from the seven-header list above (one `Products` sheet, no data rows, `ID` column set to text format).

## Pre-import checklist (for the build step)

- [ ] `Command` is `MERGE` on every row.
- [ ] No `Title` column.
- [ ] XLSX form: sheet named exactly `Products`; `ID` populated with numeric IDs stored as text (or omitted for the handle-keyed CSV form).
- [ ] CSV form: expect the entity-selection prompt and pick **Products**.
- [ ] Filename follows `ProSoccer_SEO_Batch{N}_{count}_Products.xlsx`.

## Cross-references

- `data/templates/ProSoccer_Matrixify_Template.xlsx`: the committed blank template for the XLSX form.
- `work-log/follow-ups.md`: the `product_id`-holds-SKU registry item (2026-07-28).
- `context/workforce-conventions.md` "Matrixify import file" cross-reference.
