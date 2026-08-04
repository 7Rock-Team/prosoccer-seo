# IQ2388-901 -- Nike Tiempo Maestro Academy Turf: meta-only retarget

**Date:** 2026-08-04
**Type:** Meta-field retarget (title_tag + description_tag only). No body rewrite, no title change, no handle change.
**Ships as:** Its own small Matrixify change, NOT bundled with a batch (Step 2 builds a single-row import).

## Why

IQ2388 (live) previously held the bare cross-surface term `nike tiempo maestro academy` (170/mo) as its
primary. That term describes both the FG/MG and Turf surfaces, so it resolves to more than one product and
belongs to neither PDP. Batch 12 shipped IB1600 (Tiempo Maestro Academy FG/MG) on the surface-qualified
`nike tiempo maestro academy fg mg`, on the assumption that IQ2388 vacates the bare term and takes the
matching Turf-qualified term. This change completes that move.

- **Old primary:** `nike tiempo maestro academy` (170)
- **New primary:** `nike tiempo maestro academy turf` (20, sub-floor by design; the exact one-product term)
- The higher-volume `tiempo turf shoes` (140) is a generic multi-model turf term, not a one-product PDP
  term, so it stays a body-topical secondary, not the primary. Volume never overrides hierarchy.

## The two fields to change (copy-paste into the Matrixify row)

### Metafield: title_tag [string]
```
Nike Tiempo Maestro Academy Turf Shoes
```
38 characters. Under the 48-char written cap. Leads with the exact retarget term. "Shoes" per the turf-title
convention (the live product title is "Soccer Shoes," not cleats). No manufacturer-brand pipe suffix.

### Metafield: description_tag [string]
```
The Nike Tiempo Maestro Academy Turf brings soft FlyTouch leather and a flat rubber outsole for real ball feel on artificial turf. Entry-tier Tiempo touch.
```
155 characters (in the 120-160 band). Full sentences, no colon-fragment opener. This also corrects a
compliance defect in the prior live meta description, which opened `The Nike Tiempo Maestro Academy turf
shoe: soft FlyTouch leather...` -- the forbidden "Product Name: fragment" colon opener.

## For Step 2 (single-row Matrixify import, meta-only)

Verbatim handle (do not reconstruct):
```
nike-tiempo-maestro-academy-turf-soccer-shoes-breakout-pack-su26
```

One row, `Command` = MERGE. Ship only the two metafield columns below (no Body HTML column,
no short_description column, no Title column). Absence of every other column is the preservation
guarantee.

| Handle | Command | Metafield: title_tag [string] | Metafield: description_tag [string] |
|---|---|---|---|
| nike-tiempo-maestro-academy-turf-soccer-shoes-breakout-pack-su26 | MERGE | Nike Tiempo Maestro Academy Turf Shoes | The Nike Tiempo Maestro Academy Turf brings soft FlyTouch leather and a flat rubber outsole for real ball feel on artificial turf. Entry-tier Tiempo touch. |

Validation for the file: title_tag 38 chars (<=48, no brand pipe suffix), description_tag 155 chars
(120-160), no em dashes, MERGE.

## Do NOT change
- Title (Shopify "Title" field), URL handle, Body HTML / short description, taxonomy, variants, price.
- Only `title_tag` and `description_tag` ship.

## Layer 3 -- claim verification (both new strings)

Every substantive claim traced to the IQ2388 brief
(`deliverables/page-optimizations/2026-06-30_session-01/IQ2388-901_nike-tiempo-maestro-academy-turf-soccer-shoes-breakout-pack-su26_brief.md`,
scrape-sourced 2026-06-30):

| Claim in new copy | Source in brief | Verdict |
|---|---|---|
| soft FlyTouch leather | "soft FlyTouch leather that molds to the foot"; "FlyTouch leather upper: soft and lightweight" | sourced |
| flat rubber outsole | "flat rubber outsole"; "Rubber outsole and turf (TF) build" | sourced |
| artificial turf | "made for artificial turf and older astroturf"; "turf (TF) build" | sourced |
| entry-tier Tiempo | "Academy tier: Nike's accessible build below the Pro and Elite" | sourced |
| real ball feel / touch | "soft FlyTouch leather for real ball feel"; Tiempo touch-and-control line | sourced |

No FIFA / World Cup terms (Nike, non-licensed). No em dashes. adidas rule n/a. Turf = "shoes," not "cleats."

## Registry
`deliverables/tracking/products-master.csv` row IQ2388-901 updated 2026-08-04: primary_keyword,
normalized_primary, target_keywords, normalized_target_keywords -> turf-qualified; primary_volume 170 -> 20;
kw_source appended "meta-retarget 2026-08-04"; kw_recorded_date 2026-08-04; notes document the move.
Status stays `shipped` (the page is live); the two meta fields land on the next import.
