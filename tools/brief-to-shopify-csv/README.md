# Brief to Shopify CSV

Converts ProSoccer SEO workforce brief files (`*_brief.md`) into a
Shopify-importable product CSV. It edits only five content fields and passes
every other column through untouched, so you can bulk-update PDP copy without
risking variants, pricing, tags, or any other product data.

Built per `ProSoccer_Brief-to-Shopify-CSV_Build-Spec.docx` (in this folder).

---

## What it changes (and what it never touches)

**Updates exactly these 5 fields:**

| Field | Where it comes from in the brief | Where it lands |
|---|---|---|
| Body (HTML) | the `### Description (body_html…` section (markdown) | `Body (HTML)`, parent row |
| SEO Title | the `### Meta Title…` line | `SEO Title`, parent row |
| SEO Description | the `### Meta Description…` line | `SEO Description`, parent row |
| Short Description | the `### Short Description…` prose | the Short Description metafield, parent row |
| Image Alt Text | the `### Image Alt Text` bullets | `Image Alt Text`, per image row, **conditional** |

**Image Alt Text is conditional:** an alt is written only when a row's
`Image Alt Text` cell is *empty* AND the row has an `Image Position`. If the cell
already has any value, it is preserved verbatim. Rows without an Image Position
are never touched. (In practice, products whose images already have alt text get
zero alt changes; the tool only fills empty slots.)

**Never modified, under any circumstances:**

- `Title` (Mike's rule: existing titles are preserved)
- `Tags` (Jorge's pre-launch tag system / Tapcart gating depends on this)
- Any metafield except the Short Description metafield
- Variants, pricing, inventory, options, Google Shopping, regional columns
- Row order, column order, the header row

---

## Requirements

- **Python 3.10 or newer.** No third-party packages — standard library only.
  (See `requirements.txt`.)

---

## The operator workflow (full worked example)

This is the export → modify → import loop. The script is only the middle step.

### 1. Export the target SKUs from Shopify

Shopify admin → **Products** → select the SKUs you're updating → **Export** →
**Current page** (or selected) → **CSV for Excel** → Export products.

Save the downloaded file somewhere you can find it, e.g.
`tools/brief-to-shopify-csv/fixtures/sample_export.csv` or a working folder.

> **Keep this original export.** It is your rollback insurance. Do not delete it
> until you've verified the live PDPs are correct after import.

### 2. Dry-run first (no file is written)

From the `tools/brief-to-shopify-csv/` folder:

```
python brief_to_shopify_csv.py --briefs ../../deliverables/batch-4/ --export my-export.csv --dry-run
```

Read the output. For each product you'll see:

- the matched Shopify **handle** and parent row,
- a full **current vs proposed** diff for Body, SEO Title, SEO Description, and
  the Short Description metafield,
- the per-image **Image Alt Text** decision (WRITE / PRESERVE / leave empty),
- the **validation** block (3 checks), and
- a **summary** (briefs applied, cells modified, rows touched).

If anything looks wrong, fix the brief (or the export) and dry-run again. Nothing
has been written.

### 3. Write the output CSV

When the dry-run looks right, run the same command without `--dry-run`:

```
python brief_to_shopify_csv.py --briefs ../../deliverables/batch-4/ --export my-export.csv --batch batch-4
```

The script reprints the diffs and validation, then **pauses and asks you to type
`YES`** before writing. After it writes, it **re-reads the file from disk** and
re-runs the integrity checks (defense in depth) before telling you it's safe.

Output lands in `./output/` with a timestamped name, e.g.
`output/brief_to_shopify_batch-4_2026-06-22-1430.csv`, alongside a matching
`.log` transaction file recording exactly which briefs hit which handles.

You can force an explicit output path with `--output path/to/file.csv`, and skip
the confirmation prompt with `--yes` (intended for scripted runs).

### 4. Import the modified CSV back to Shopify

Shopify admin → **Products** → **Import** → upload the output CSV →
**Update existing products** (Shopify matches on `Handle`). Do **not** check
"overwrite" options that would replace unmentioned data — the standard import
updates the columns present and matches by handle.

### 5. Spot-check the live PDPs

Open each updated PDP in a browser and confirm:

- H2/H3 body structure and prose match the brief,
- FAQ section renders,
- Meta Title / Meta Description show in the search-engine-listing fields,
- the Short Description hero block above Add to Cart is the new copy,
- any newly-filled image alt text is correct,
- **nothing else changed** (price, variants, tags, status).

If something is wrong, re-import your **original** export from step 1 to restore
the prior state, then investigate.

---

## Command reference

```
# Dry-run (preview only, writes nothing):
python brief_to_shopify_csv.py --briefs <briefs_dir> --export <export.csv> --dry-run

# Write (interactive YES confirmation, auto-named output under ./output/):
python brief_to_shopify_csv.py --briefs <briefs_dir> --export <export.csv> --batch <label>

# Write to an explicit path, no prompt (scripted):
python brief_to_shopify_csv.py --briefs <briefs_dir> --export <export.csv> --output out.csv --yes

# Positional form also works:
python brief_to_shopify_csv.py <briefs_dir> <export.csv> [output.csv]
```

**Exit codes:** `0` success · `2` missing args · `3` (reserved) · `4` pre-write
validation failed (nothing written) · `5` non-interactive without `--yes` ·
`6` post-write verification failed (file written but DO NOT import — investigate).

---

## Sample run output (abbreviated)

Running the write mode against the bundled fixtures (2 SKUs, 202-column export):

```
[PRE-FLIGHT] Brief parse + SKU match
  [ OK ] HQ2254 -> handle 'adidas-predator-pro-...' (parent row 0, 15 rows) | 5/5 target fields parsed
  [ OK ] JP6271 -> handle 'adidas-predator-league-...' (parent row 15, 19 rows) | 5/5 target fields parsed

  Ready to apply : 2 brief(s)
  Skipped        : 0 brief(s)

... per-product current-vs-proposed diffs ...

VALIDATION (spec section 8)
  [PASS] Column header integrity (headers byte-identical, same order)   in=202, out=202
  [PASS] Row count integrity (no rows added/removed/reordered)          in=34,  out=34
  [PASS] Non-target columns unchanged (verbatim pass-through)           0 non-target cell changes

SUMMARY
  Briefs applied        : 2
  Briefs skipped        : 0
  Total cells modified  : 8
  Rows touched          : 2
  Validation            : ALL PASS

POST-WRITE VERIFICATION (re-read from disk)
  [PASS] On-disk header byte-identical to input header
  [PASS] On-disk row count equals input row count
  [PASS] On-disk values equal intended output (round-trip lossless)
  [PASS] On-disk non-target columns equal original input (verbatim pass-through)

  WRITE complete and verified. Safe to import to Shopify.
```

8 cells modified = 4 product fields × 2 parent rows. (These fixtures already had
alt text on every image row, so 0 alt cells were written — the conditional rule
working as intended.)

---

## Safety model

Two independent validation passes run on every write:

1. **Pre-write (in memory):** header integrity, row-count integrity, and a
   zero-change diff on every non-target column. If any fails, **nothing is
   written.**
2. **Post-write (re-read from disk):** the just-written file is parsed back and
   compared, cell for cell, to both the intended output and the original input's
   non-target columns. If any fails, the file is flagged **DO NOT import.**

The fidelity controls on write: UTF-8 (BOM only if the source had one), the
source's exact line terminator (LF or CRLF, auto-detected from the header row),
and RFC-4180 quoting (`QUOTE_MINIMAL`, inner quotes doubled — Body HTML cells
contain `"` inside `href`s). The guarantee is **value-level**, which is what
Shopify imports by.

---

## Tests

The markdown→HTML converter is pinned by **byte-for-byte golden-file tests**, and
the conditional Image Alt Text rule has dedicated synthetic tests. Tests must
pass before any real run.

```
python -m unittest discover -s tests -v
```

- `tests/golden/` — input/expected pairs for the converter (H2, multiple H2s,
  bullet lists, single/multiple links, the FAQ pattern, and a mixed document).
- `tests/test_alt_fill.py` — the conditional alt rule (write-empty, preserve-set,
  no-position-skip, fewer-alts-than-images) plus the parent-row-only update logic
  and the hard Title/Tags constraints.

---

## Conventions / notes

- The bundled fixture is `fixtures/sample_export.csv` (underscore). This is the
  locked operational name; the spec's hyphenated reference is superseded.
- Brief filenames must follow `<SKU>_<slug>_brief.md`; the SKU before the first
  `_` is matched as a **prefix** against the export's `Variant SKU` column
  (e.g. brief `HQ2254` matches variant SKUs `HQ2254-M 4`, `HQ2254-M 5`, …).
- A brief whose SKU isn't found is logged and skipped (the run does not fail). A
  brief missing any of the 5 target fields is logged and skipped from the update.
- `output/` and `*.log` are gitignored — operational artifacts, not source.
```
