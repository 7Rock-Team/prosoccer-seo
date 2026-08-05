# IQ2388-901 -- Nike Tiempo Maestro Academy Turf: meta-only retarget

**Date:** 2026-08-04 (re-qualified under pack succession before import)
**Type:** Meta-field retarget (title_tag + description_tag only). No body rewrite, no title change, no handle change.
**Ships as:** Its own small Matrixify change, NOT bundled with a batch (Step 2 builds a single-row import).

## Why (re-qualified 2026-08-04 per the pack-succession rule, Mike-approved)

IQ2388 is the Nike Tiempo Maestro Academy Turf in the **Breakout SU26** pack. An earlier version of this
retarget gave it the UNQUALIFIED `nike tiempo maestro academy turf` (20/mo). That was wrong under pack
succession: the incumbent for the model + tier + cut + surface "Tiempo Maestro Academy Turf" is the
EARLIEST-shipped live pack, and the live sitemap shows earlier SP26 packs (Shadow SP26, Attack SP26). So the
unqualified term belongs to the SP26 incumbent, and IQ2388 (Breakout SU26) must take a pack-qualified primary.
Caught before import, so this is a free fix (no churn), unlike shipped SP26 pages grandfathered under clause 9.

- **Superseded primary:** `nike tiempo maestro academy turf` (20; releases to the SP26 incumbent)
- **New primary:** `nike tiempo maestro academy turf breakout` (no measurable DFS volume, both endpoints 2026-08-04; sub-floor by design). "Breakout" does not recur for this config, so no season code.
- Volume never overrides hierarchy; the pack-qualified term is a conversion/navigational surface, not a ranking target.

## The two fields to change (copy-paste into the Matrixify row)

### Metafield: title_tag [string]
```
Nike Tiempo Maestro Academy Turf Breakout
```
41 characters. Under the 48-char written cap. Carries the pack qualifier ("Breakout") that distinguishes this
page from the SP26 Shadow/Attack packs. "Turf" per the turf-title convention (the live product title is "Soccer
Shoes," not cleats). No manufacturer-brand pipe suffix.

### Metafield: description_tag [string]
```
The Nike Tiempo Maestro Academy Turf in the Breakout pack brings soft FlyTouch leather and a flat rubber outsole for real ball feel on artificial turf.
```
149 characters (in the 120-160 band). Full sentence, no colon-fragment opener. Also corrects the prior live meta
description's forbidden "Product Name: fragment" colon opener.

## For Step 2 (single-row Matrixify import, meta-only)

Verbatim handle (do not reconstruct):
```
nike-tiempo-maestro-academy-turf-soccer-shoes-breakout-pack-su26
```

One row, `Command` = MERGE. Ship only the two metafield columns below (no Body HTML, no short_description, no
Title column). Absence of every other column is the preservation guarantee.

| Handle | Command | Metafield: title_tag [string] | Metafield: description_tag [string] |
|---|---|---|---|
| nike-tiempo-maestro-academy-turf-soccer-shoes-breakout-pack-su26 | MERGE | Nike Tiempo Maestro Academy Turf Breakout | The Nike Tiempo Maestro Academy Turf in the Breakout pack brings soft FlyTouch leather and a flat rubber outsole for real ball feel on artificial turf. |

Validation: title_tag 41 chars (<=48, no brand pipe suffix), description_tag 149 chars (120-160, no colon opener),
no em dashes, MERGE.

## Do NOT change
- Title (Shopify "Title" field), URL handle, Body HTML / short description, taxonomy, variants, price.
- Only `title_tag` and `description_tag` ship.

## Layer 3 -- claim verification (both new strings)

Claims traced to the IQ2388 brief (`deliverables/page-optimizations/2026-06-30_session-01/IQ2388-901_nike-tiempo-maestro-academy-turf-soccer-shoes-breakout-pack-su26_brief.md`, scrape-sourced 2026-06-30):

| Claim | Source | Verdict |
|---|---|---|
| soft FlyTouch leather | "soft FlyTouch leather that molds to the foot" | sourced |
| flat rubber outsole | "flat rubber outsole"; "Rubber outsole and turf (TF) build" | sourced |
| artificial turf | "made for artificial turf and older astroturf" | sourced |
| Breakout pack (SU26) | live product title "...Breakout Pack (SU26)"; handle | sourced |
| real ball feel / touch | "soft FlyTouch leather for real ball feel" | sourced |

No FIFA / World Cup terms (Nike, non-licensed). No em dashes. adidas rule n/a. Turf = "shoes," not "cleats."

## Registry
`deliverables/tracking/products-master.csv` row IQ2388-901 updated 2026-08-04: primary_keyword /
normalized_primary -> `nike tiempo maestro academy turf breakout`; primary_volume blanked (no measurable);
notes document the pack-succession re-qualification. Status stays `shipped` (page is live); the two meta fields
land on the next single-row import.
