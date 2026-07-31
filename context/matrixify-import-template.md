# Matrixify Import File Template (canonical)

This is the required shape for any Matrixify product-import file the workforce builds (SEO title, meta description, short description, and body updates for a batch of PDPs). **Build every import file by copying the committed blank template `data/templates/ProSoccer_Matrixify_Template.xlsx` and filling it in. Never construct the header by hand, and never copy a previous batch's populated file.** A description of the format is not the format, and a populated old file invites someone carrying stale IDs and stale copy into a new batch. Batch 9's first import file was built from a remembered column list and would have silently half-failed; this document plus the blank template exist so that cannot recur.

## Why this matters: the silent-ignore failure class

Matrixify does not reject unrecognized column headers. It ignores them and reports the import as successful. So an import file with the wrong headers looks like it worked: the rows Matrixify does recognize (Body HTML) apply, and everything keyed to an unrecognized header (the SEO title, meta description, short description) silently does not import. There is no error at import time. The failure is invisible until someone checks the live pages field by field and finds the SEO fields never changed.

That is why the header has to match this template exactly, and why a mismatch is not a cosmetic issue. Bare metafield names are not "close enough." They are ignored.

## The canonical seven columns (byte for byte)

These are the seven headers, spelled and cased exactly as below. Do not type them; they already sit in row 1 of `data/templates/ProSoccer_Matrixify_Template.xlsx`, so copy that file rather than re-creating the header. The list here is for reference and validation. Matrixify requires its own metafield syntax (`Metafield: <namespace.>key [type]`); the bare key alone is not a column Matrixify recognizes.

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

- **ID**: the real Shopify numeric product ID, stored as a TEXT string (see "The ID column" below). Not the SKU.
- **Handle**: the product URL handle, live-verified.
- **Command**: `MERGE` on every row. MERGE updates the named fields on the existing product and leaves everything else untouched. No other command value for an SEO field update.
- **Body HTML**: the product description body (`body_html`), the accordion content below the images.
- **Metafield: title_tag [string]**: the SEO / browser title (Shopify's "title tag").
- **Metafield: description_tag [string]**: the meta description.
- **Metafield: products.new_short_description [multi_line_text_field]**: the hero-block short description above Add to Cart. Note the `products.` namespace prefix and the `multi_line_text_field` type; both are part of the header and both are required.

No **Title** column. Title here would mean the product's storefront name (`title`), which the workforce does not change in an SEO batch; including it risks overwriting the product name. The SEO title lives in `Metafield: title_tag [string]`, not in `Title`.

## File format: XLSX with a sheet named "Products"

- Format: **XLSX**, not CSV.
- Sheet name: exactly **`Products`**.

The sheet name is how Matrixify auto-detects which entity the file targets. `Handle` and `Command` are columns on both the Products and the Collections entity, so a bare CSV carrying only those shared columns is ambiguous, and Matrixify stops with "Sheets require entity selection" instead of importing. A sheet named `Products` removes the ambiguity. This is the specific error Batch 9's CSV would have triggered.

## Filename convention

```
ProSoccer_SEO_Batch{N}_{ProductCount}_Products.xlsx
```

Example: `ProSoccer_SEO_Batch9_10_Products.xlsx` for the 10-product Batch 9 file. Match the pattern of the proven prior batch file.

## The ID column: numeric Shopify IDs, stored as text, never invented

- The value is the Shopify **numeric product ID** (for example `9553887625471`), not the SKU.
- Store it as a **TEXT string** in the cell, not a number. As a number, the spreadsheet can reformat it into scientific notation or drop precision, which breaks the match.
- The numeric IDs are **not on disk anywhere in this repo**. `deliverables/tracking/products-master.csv` holds the SKU in its `product_id` column, not the numeric ID (that column is misnamed; see `work-log/follow-ups.md` entry dated 2026-07-28).
- **Never invent, guess, or derive an ID.** Source it from a Matrixify export filtered to the batch's handles, which returns the ID-to-handle mapping. Wait for that export before finalizing the file.

Handle-keyed matching (ID column absent) technically works, because Handle is a valid match key. But every batch that has imported cleanly carried the numeric ID, and there is no benefit to dropping it. Keep the ID column and populate it from an export.

## Canonical template file (copy this)

The source of truth is the committed blank template **`data/templates/ProSoccer_Matrixify_Template.xlsx`**:

- one sheet, named exactly `Products`
- the seven headers in row 1, byte for byte
- zero data rows
- the `ID` column pre-formatted as TEXT, so a pasted numeric ID stays text and does not turn into scientific notation

Copy this file, rename it per the filename convention, and fill in the rows. The template is deliberately **blank, not a copy of a past batch**. A populated old file (like Batch 8's) would invite someone carrying stale IDs and stale live copy into a new batch, which is a different silent failure than the header one. Copy the blank; bring in this batch's own IDs and copy.

If the template is ever lost, rebuild it from the seven-header list above, one `Products` sheet, no data rows, `ID` column set to text format.

## What a wrong file looks like (Batch 9, before fix)

The rejected Batch 9 CSV header was:

```
Handle,Command,Body HTML,title_tag,description_tag,new_short_description
```

Three defects, all silent at import time:

1. **Bare metafield names.** `title_tag`, `description_tag`, `new_short_description` are not columns Matrixify recognizes. They would have been ignored: Body HTML applies, the three SEO fields silently do not.
2. **CSV, no `Products` sheet.** Entity ambiguous (Handle and Command exist on Products and Collections), triggering "Sheets require entity selection."
3. **No ID column.** Dropped because products-master holds SKUs, not numeric IDs.

## Pre-import validation checklist

Before handing an import file to Mike, confirm:

- [ ] Built by copying `data/templates/ProSoccer_Matrixify_Template.xlsx`, not hand-constructed and not a copy of a past batch's populated file.
- [ ] Format is XLSX, sheet named exactly `Products`.
- [ ] Header row is the seven canonical columns above, byte for byte (it already is if you copied the template).
- [ ] `Command` is `MERGE` on every row.
- [ ] No `Title` column.
- [ ] `ID` populated with numeric Shopify IDs sourced from a Matrixify export, stored as text.
- [ ] Filename follows `ProSoccer_SEO_Batch{N}_{count}_Products.xlsx`.

A deterministic validator that fails when the header does not match this template exactly is on the gate-hardening backlog (`work-log/follow-ups.md`, 2026-07-28). It matters because this error class is invisible at import time: Matrixify reports success while ignoring columns, so a human or gate check before import is the only place to catch it.

## Cross-references

- `data/templates/ProSoccer_Matrixify_Template.xlsx`: the committed blank template to copy for every import file.
- `work-log/follow-ups.md`: the `product_id`-holds-SKU registry item (2026-07-28) and the import-file-validator gate-hardening item (2026-07-28).
- `context/workforce-conventions.md` "Matrixify import file" cross-reference.
- `deliverables/tracking/products-master.csv`: where numeric Shopify IDs land once exported (in a new `shopify_product_id` column; `product_id` stays the SKU).
