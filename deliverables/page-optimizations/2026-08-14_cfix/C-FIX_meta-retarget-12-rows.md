# C-FIX: consolidated meta-only retarget, 12 rows

**Date:** 2026-08-14
**Type:** Meta-field retarget (`title_tag` + `description_tag` only). No body rewrite, no Title change, no handle change, no taxonomy change.
**Ships as:** ONE Matrixify import, 12 rows, `Command` = MERGE on every row.
**Approved by Mike:** 2026-08-14 (12 rows IN; Decision 3 four rows no-action; four F50 rows held pending B-KW-01; rows 9/10/23 held for the collection workstream; 38-row compliance block deferred to C-FIX-2).
**Runs BEFORE Batch 15**, so Batch 15 authors into clean term space instead of shipping known collisions on a promise.

Format follows the `IQ2388-901_meta-retarget.md` precedent (2026-08-04): a meta-only retarget is a retarget document, not a SCRIBE brief, so no per-SKU brief or input file is produced. Flagged for Mike in the C-FIX report as a standing-process question.

---

## Why these 12

Every row is a live, shipped page holding a primary keyword that does not resolve to one product. Three causes:

1. **Pack-succession omission (9 rows).** The page took the unqualified model + tier + cut + surface term while a concurrent live pack sibling exists, so the term belongs to the earliest live pack, not to this one. Source: B-PACK-01, B-DUP-03.
2. **Cut-less term (1 row, HQ2325).** The term carries no cut token while both cuts are live. Source: B-DUP-03.
3. **Broader hierarchy-invalid term (3 rows).** The page holds a cut-less, surface-less or config-less term spanning many live products. Source: Batch 15 selection-gate Decision 2.

Season code is included only where a live same-pack sibling from another season exists at that exact configuration, checked against the live product sitemap per row (`context/page-type-playbooks/product-page-playbook.md` 'Pack season-code qualifier').

**Volume honesty.** Eleven of the twelve proposed primaries return no measurable volume on either DFS endpoint (checked 2026-08-14, Google Ads + Labs); the twelfth returns 10/mo. That is expected and correct under the sub-floor lock: a term the page cannot legitimately own is worth less than a qualified term that resolves to it. Four rows give up measurable volume, all recorded below and all approved knowingly.

---

## The 12 rows

| # | SKU | Handle (verbatim, do not reconstruct) | Current primary | Vol | New primary | Vol |
|---|---|---|---|---|---|---|
| 1 | HQ2278-001 | `nike-phantom-6-high-academy-fg-mg-soccer-cleats-shadow-fa26` | nike phantom 6 high academy fg mg | none | nike phantom 6 high academy fg mg shadow fa26 | none |
| 2 | HQ2277-001 | `nike-phantom-6-high-academy-turf-soccer-shoes-shadow-fa26` | nike phantom 6 high academy turf | **70** | nike phantom 6 high academy turf shadow | none |
| 3 | HJ4564-001 | `nike-phantom-6-low-academy-fg-mg-soccer-cleats-shadow-fa26` | nike phantom 6 low academy fg mg | 10 | nike phantom 6 low academy fg mg shadow fa26 | none |
| 4 | IO1494-001 | `nike-superfly-11-academy-turf-soccer-shoes-shadow-pack-fa26` | nike superfly 11 academy turf | none | nike superfly 11 academy turf shadow | none |
| 5 | IM0358-001 | `nike-superfly-11-club-fg-mg-soccer-cleats-shadow-fa26` | nike superfly 11 club fg mg | none | nike superfly 11 club fg mg shadow | none |
| 6 | IB1600-001 | `nike-tiempo-maestro-academy-fg-mg-soccer-cleats-shadow-fa26` | nike tiempo maestro academy fg mg | none | nike tiempo maestro academy fg mg shadow | none |
| 7 | 540394.9025 | `mizuno-morelia-neo-v-beta-elite-fg-soccer-cleats-bright-black` | mizuno morelia neo beta elite | **30** | mizuno morelia neo beta elite bright black | none |
| 8 | 540396.9025 | `mizuno-morelia-neo-v-beta-pro-fg-soccer-cleats-bright-black` | mizuno morelia neo beta pro | none | mizuno morelia neo beta pro bright black | none |
| 9 | HQ2325 | `nike-phantom-6-low-academy-turf-soccer-shoes-shadow-fa26` | nike phantom 6 academy turf shadow | none | nike phantom 6 low academy turf shadow | none |
| 10 | IH1779-900 | `nike-phantom-6-high-elite-firm-soccer-cleats-breakout-pack-su26` | nike phantom 6 elite fg | **140** | nike phantom 6 high elite fg breakout | none |
| 11 | IQ1886-900 | `nike-phantom-6-low-pro-firm-ground-soccer-cleats-breakout-pack-su26` | nike phantom 6 pro | **880** | nike phantom 6 low pro fg breakout | none |
| 12 | HP9971 | `adidas-predator-elite-fold-over-tongue-artificial-grass-soccer-cleats-road-to-glory-pack-sp26` | adidas predator elite ag | **590** | adidas predator elite fold over tongue ag road to glory | 10 |

Season-code rationale per row: #1 and #3 carry `fa26` because a Shadow **FA25** page is live at the same configuration. #2, #4, #5, #6, #9 carry the pack name only, because no cross-season sibling of that pack exists at their configuration. #7 and #8 carry `bright black` only (no live cross-season Bright Black). #10 and #11 carry `breakout` only (one Breakout each). #12 carries `road to glory` only (one Road to Glory at the AG fold-over configuration).

---

## The two fields to change, per row

### 1. HQ2278-001, Nike Phantom 6 High Academy FG/MG, Shadow Pack (FA26)

**Metafield: title_tag [string]**
```
Nike Phantom 6 High Academy FG/MG Shadow FA26
```
45 chars. Brand front, pack whole, season code carried (Shadow FA25 live at this config). No brand pipe suffix.

**Metafield: description_tag [string]**
```
A Flyknit Dynamic Fit collar locks the ankle on the Nike Phantom 6 High Academy, over an FG/MG plate for grass and turf. Lace up in the Shadow Pack.
```
148 chars. Full sentences, no colon opener.

### 2. HQ2277-001, Nike Phantom 6 High Academy Turf, Shadow Pack (FA26)

**Metafield: title_tag [string]**
```
Nike Phantom 6 High Academy Turf Shadow
```
39 chars. No cross-season Shadow at High Academy Turf, so pack name only.

**Metafield: description_tag [string]**
```
The Nike Phantom 6 High Academy Turf runs a rubber outsole over ReactX foam, with a high Flyknit collar for lockdown on 3G. Shadow Pack colorway.
```
145 chars. Turf product, so no "cleat" noun.

### 3. HJ4564-001, Nike Phantom 6 Low Academy FG/MG, Shadow Pack (FA26)

**Metafield: title_tag [string]**
```
Nike Phantom 6 Low Academy FG/MG Shadow FA26
```
44 chars. Season code carried (Shadow FA25 live at this config).

**Metafield: description_tag [string]**
```
No collar, no fuss. The Nike Phantom 6 Low Academy puts Cyclone 360 forefoot traction under an FG/MG plate for grass and mixed ground. Shadow Pack.
```
147 chars. Short opener then a longer thought, per the varied-rhythm rule.

### 4. IO1494-001, Nike Superfly 11 Academy Turf, Shadow Pack (FA26)

**Metafield: title_tag [string]**
```
Nike Superfly 11 Academy Turf Shadow
```
36 chars.

**Metafield: description_tag [string]**
```
The Nike Superfly 11 Academy Turf keeps a NikeSkin upper and a Dynamic Fit collar over a rubber outsole tuned for 3G. Shadow Pack black and Illusion Green.
```
155 chars.

### 5. IM0358-001, Nike Superfly 11 Club FG/MG, Shadow Pack (FA26)

**Metafield: title_tag [string]**
```
Nike Superfly 11 Club FG/MG Shadow
```
34 chars.

**Metafield: description_tag [string]**
```
Nike's entry-price Superfly runs a durable synthetic leather upper on a light FG/MG plate, with chevron and conical studs for grip. Shadow Pack.
```
144 chars.

### 6. IB1600-001, Nike Tiempo Maestro Academy FG/MG, Shadow Pack (FA26)

**Metafield: title_tag [string]**
```
Nike Tiempo Maestro Academy FG/MG Shadow
```
40 chars.

**Metafield: description_tag [string]**
```
Soft FlyTouch leather gives the Nike Tiempo Maestro Academy a clean touch, with bladed and conical studs on an FG/MG plate. Shadow Pack colorway.
```
145 chars. FlyTouch in title case per the brand-technology rule.

### 7. 540394.9025, Mizuno Morelia Neo V Beta Elite FG, Bright Black Pack (FA26)

**Metafield: title_tag [string]**
```
Mizuno Morelia Neo V Beta Elite FG Bright Black
```
47 chars.

**Metafield: description_tag [string]**
```
Kangaroo leather and an external heel counter make the Mizuno Morelia Neo V Beta Elite a firm-ground touch cleat. Bright Black Pack, Lava Orange trim.
```
150 chars.

### 8. 540396.9025, Mizuno Morelia Neo V Beta Pro FG, Bright Black Pack (FA26)

**Metafield: title_tag [string]**
```
Mizuno Morelia Neo V Beta Pro FG Bright Black
```
45 chars.

**Metafield: description_tag [string]**
```
The Mizuno Morelia Neo V Beta Pro brings real kangaroo leather and a foot-shaped Engineered Fit Last Neo to firm ground. Bright Black Pack.
```
139 chars.

### 9. HQ2325, Nike Phantom 6 Low Academy Turf, Shadow Pack (FA26)

**Metafield: title_tag [string]**
```
Nike Phantom 6 Low Academy Turf Shadow
```
38 chars. Adds the LOW cut token the current term omits.

**Metafield: description_tag [string]**
```
Engineered mesh and a NikeSkin touch zone give the Nike Phantom 6 Low Academy real feel on turf, over a rubber outsole built for grip. Shadow Pack black.
```
153 chars. Also brings this SKU into the length band: the shipped brief's description measures 170 chars, over the 160 ceiling (measured from the brief file, not from the live page).

### 10. IH1779-900, Nike Phantom 6 High Elite FG, Breakout Pack (SU26)

**Metafield: title_tag [string]**
```
Nike Phantom 6 High Elite FG Breakout
```
37 chars. Adds the HIGH cut token and the Breakout pack the current term omits.

**Metafield: description_tag [string]**
```
Gripknit grip and Ghost Lacing give the Nike Phantom 6 High Elite FG a clean strike surface, with Cyclone 360 traction underfoot. Breakout Pack.
```
144 chars.

### 11. IQ1886-900, Nike Phantom 6 Low Pro FG, Breakout Pack (SU26)

**Metafield: title_tag [string]**
```
Nike Phantom 6 Low Pro FG Breakout
```
34 chars. Adds cut, surface and pack.

**Metafield: description_tag [string]**
```
VNMSkin over a Flyknit base brings the ball close on the Nike Phantom 6 Low Pro FG, a low-cut firm-ground cleat. Breakout Pack colorway.
```
136 chars.

### 12. HP9971, adidas Predator Elite Fold-Over Tongue AG, Road to Glory Pack (SP26)

**Metafield: title_tag [string]**
```
adidas Predator Elite FO AG Road to Glory
```
41 chars. "FO" is licensed by the store's own live product titles at this model and configuration (`adidas-predator-elite-fo-tongue-ag-soccer-cleats-chaos-vs-control`), the same basis as the Batch 13 IH4707 and JP6248 precedent. Pack name whole, brand prefix kept, config abbreviated. Spelled out the string is 55 chars, over the cap.

**Metafield: description_tag [string]**
```
The adidas Predator Elite AG runs a Nanostrike+ Primeknit upper behind a fold-over tongue, on an AG outsole made for 3G. Road to Glory Pack, 7.2 oz.
```
148 chars. adidas lowercase at sentence start per the brand-styling rule. Nanostrike+ and Primeknit in title case. Weight US-only, correct for meta fields (dual notation applies to body, bullets and FAQ, not to metas).

---

## The import file (built 2026-08-14)

- **`ProSoccer_SEO_CFIX_12_Products.xlsx`** (primary). Single sheet named exactly `Products`, which auto-resolves the entity so Matrixify does not prompt for it. Four columns, 12 data rows.
- **`ProSoccer_SEO_CFIX_12_Products.csv`** (fallback, same content). Handle-keyed CSV; Matrixify will prompt "Sheets require entity selection", answer **Products**.

No `ID` column: no numeric-ID export is on hand and `context/matrixify-import-template.md` permits Handle-keying, proved on Batch 9. No `Title`, no `Body HTML`, no short-description column; their absence is the preservation guarantee.

Both files are generated from the table below, so the strings have one source and were never retyped. The written XLSX was then read back and re-checked against this document: 12 of 12 rows verbatim, all titles at or under 48, all descriptions inside 120 to 160, `Command` = MERGE on every row, 12 unique handles.

## Matrixify import content (the table both files are built from)

Handle-keyed, 12 rows, three columns plus Handle. `Command` = MERGE on every row. **No Title column, no Body HTML, no short description.** Absence of every other column is the preservation guarantee.

| Handle | Command | Metafield: title_tag [string] | Metafield: description_tag [string] |
|---|---|---|---|
| nike-phantom-6-high-academy-fg-mg-soccer-cleats-shadow-fa26 | MERGE | Nike Phantom 6 High Academy FG/MG Shadow FA26 | A Flyknit Dynamic Fit collar locks the ankle on the Nike Phantom 6 High Academy, over an FG/MG plate for grass and turf. Lace up in the Shadow Pack. |
| nike-phantom-6-high-academy-turf-soccer-shoes-shadow-fa26 | MERGE | Nike Phantom 6 High Academy Turf Shadow | The Nike Phantom 6 High Academy Turf runs a rubber outsole over ReactX foam, with a high Flyknit collar for lockdown on 3G. Shadow Pack colorway. |
| nike-phantom-6-low-academy-fg-mg-soccer-cleats-shadow-fa26 | MERGE | Nike Phantom 6 Low Academy FG/MG Shadow FA26 | No collar, no fuss. The Nike Phantom 6 Low Academy puts Cyclone 360 forefoot traction under an FG/MG plate for grass and mixed ground. Shadow Pack. |
| nike-superfly-11-academy-turf-soccer-shoes-shadow-pack-fa26 | MERGE | Nike Superfly 11 Academy Turf Shadow | The Nike Superfly 11 Academy Turf keeps a NikeSkin upper and a Dynamic Fit collar over a rubber outsole tuned for 3G. Shadow Pack black and Illusion Green. |
| nike-superfly-11-club-fg-mg-soccer-cleats-shadow-fa26 | MERGE | Nike Superfly 11 Club FG/MG Shadow | Nike's entry-price Superfly runs a durable synthetic leather upper on a light FG/MG plate, with chevron and conical studs for grip. Shadow Pack. |
| nike-tiempo-maestro-academy-fg-mg-soccer-cleats-shadow-fa26 | MERGE | Nike Tiempo Maestro Academy FG/MG Shadow | Soft FlyTouch leather gives the Nike Tiempo Maestro Academy a clean touch, with bladed and conical studs on an FG/MG plate. Shadow Pack colorway. |
| mizuno-morelia-neo-v-beta-elite-fg-soccer-cleats-bright-black | MERGE | Mizuno Morelia Neo V Beta Elite FG Bright Black | Kangaroo leather and an external heel counter make the Mizuno Morelia Neo V Beta Elite a firm-ground touch cleat. Bright Black Pack, Lava Orange trim. |
| mizuno-morelia-neo-v-beta-pro-fg-soccer-cleats-bright-black | MERGE | Mizuno Morelia Neo V Beta Pro FG Bright Black | The Mizuno Morelia Neo V Beta Pro brings real kangaroo leather and a foot-shaped Engineered Fit Last Neo to firm ground. Bright Black Pack. |
| nike-phantom-6-low-academy-turf-soccer-shoes-shadow-fa26 | MERGE | Nike Phantom 6 Low Academy Turf Shadow | Engineered mesh and a NikeSkin touch zone give the Nike Phantom 6 Low Academy real feel on turf, over a rubber outsole built for grip. Shadow Pack black. |
| nike-phantom-6-high-elite-firm-soccer-cleats-breakout-pack-su26 | MERGE | Nike Phantom 6 High Elite FG Breakout | Gripknit grip and Ghost Lacing give the Nike Phantom 6 High Elite FG a clean strike surface, with Cyclone 360 traction underfoot. Breakout Pack. |
| nike-phantom-6-low-pro-firm-ground-soccer-cleats-breakout-pack-su26 | MERGE | Nike Phantom 6 Low Pro FG Breakout | VNMSkin over a Flyknit base brings the ball close on the Nike Phantom 6 Low Pro FG, a low-cut firm-ground cleat. Breakout Pack colorway. |
| adidas-predator-elite-fold-over-tongue-artificial-grass-soccer-cleats-road-to-glory-pack-sp26 | MERGE | adidas Predator Elite FO AG Road to Glory | The adidas Predator Elite AG runs a Nanostrike+ Primeknit upper behind a fold-over tongue, on an AG outsole made for 3G. Road to Glory Pack, 7.2 oz. |

---

## Do NOT change

Title (Shopify "Title" field), URL handle, Body HTML, short description metafield, taxonomy node, variants, tags, price. Only `title_tag` and `description_tag` ship.

---

## Layer 3, claim verification on all 24 new strings

Every checkable assertion, classified PASS-WITH-SOURCE / FIX / ESCALATE. Sources are each SKU's own shipped brief, whose Product Details block is scrape-sourced.

| Row | Claim | Source | Verdict |
|---|---|---|---|
| 1 | Flyknit Dynamic Fit collar | HQ2278 brief: "Dynamic Fit collar in soft, stretchy Flyknit for ankle lock-in" | PASS |
| 1 | FG/MG plate, grass and turf | HQ2278 brief: "Firm/Multi-Ground (FG/MG) plate for natural grass and artificial turf" | PASS |
| 1 | Shadow Pack | live title "...Shadow Pack"; handle `...shadow-fa26` | PASS |
| 2 | rubber outsole | HQ2277 brief: "Outsole: rubber with short, multi-directional turf studs" | PASS |
| 2 | ReactX foam | HQ2277 brief: "Midsole: ReactX foam" | PASS |
| 2 | high Flyknit collar | HQ2277 brief: "Collar: Dynamic Fit high collar in soft Flyknit" | PASS |
| 2 | 3G | HQ2277 brief: "Surface: turf (TF), for artificial grass and hard court" | PASS |
| 3 | no collar | HJ4564 brief: "LOW cut, no Dynamic Fit collar" | PASS |
| 3 | Cyclone 360 forefoot traction | HJ4564 brief: "Cyclone 360 circular forefoot traction for plant-and-pivot" | PASS |
| 3 | FG/MG plate, grass and mixed ground | HJ4564 brief: "Firm/Multi-Ground (FG/MG) plate for grass and mixed surfaces" | PASS |
| 4 | NikeSkin upper | IO1494 brief: "Lightweight NikeSkin upper for close control at speed" | PASS |
| 4 | Dynamic Fit collar | IO1494 brief: "Snug, supportive Dynamic Fit collar for ankle lockdown" | PASS |
| 4 | rubber outsole tuned for 3G | IO1494 brief: "Rubber outsole tuned for turf and 3G traction" | PASS |
| 4 | black and Illusion Green | IO1494 brief: "Shadow Pack colorway: Black/Illusion Green-Black" | PASS |
| 5 | entry-price Superfly | IO/IM0358 brief meta: "Nike's entry-price Superfly"; brief: "Club" is the entry tier | PASS |
| 5 | durable synthetic leather upper | IM0358 brief: "Synthetic leather upper for full-season durability" | PASS |
| 5 | light FG/MG plate | IM0358 brief: "Lightweight FG/MG plate for quick bursts and pivots" | PASS |
| 5 | chevron and conical studs | IM0358 brief: "Chevron studs at heel and forefoot"; "Conical studs to plant and change direction" | PASS |
| 6 | soft FlyTouch leather, clean touch | IB1600 brief: "FlyTouch leather upper: soft, consistent touch in wet or dry" | PASS |
| 6 | bladed and conical studs | IB1600 brief: "Bladed studs at heel and forefoot"; "Conical studs to plant and pivot" | PASS |
| 6 | FG/MG plate | IB1600 brief: "Firm/Multi-Ground (FG/MG) plate for grass and firm surfaces" | PASS |
| 7 | kangaroo leather | 540394 brief: "Upper: Mizuno Kangaroo Leather (K-leather)" | PASS |
| 7 | external heel counter | 540394 brief: "Support: external heel counter for a locked-in heel" | PASS |
| 7 | firm ground | 540394 brief: "Traction: firm ground (FG), for dry natural grass" | PASS |
| 7 | Lava Orange | 540394 brief: "Colorway: Black-Lava Orange (Bright Black Pack, FA26)" | PASS |
| 8 | real kangaroo leather | 540396 brief: "Mizuno Kangaroo Leather upper for natural touch" | PASS |
| 8 | foot-shaped Engineered Fit Last Neo | 540396 brief: "Engineered Fit Last Neo for a foot-shaped last" | PASS |
| 8 | firm ground | 540396 brief: "Firm ground (FG) outsole for natural grass and dry surfaces" | PASS |
| 9 | NikeSkin touch zone over engineered mesh | HQ2325 brief: "Upper: expanded NikeSkin touch zone over engineered mesh" | PASS |
| 9 | rubber outsole made for turf | HQ2325 brief: "Outsole: rubber turf outsole for quick traction" | PASS |
| 9 | black on black | HQ2325 brief: "Colorway: Black/Black/Illusion Green (Shadow Pack)" | PASS |
| 10 | Gripknit | IH1779 brief: "Nike Gripknit upper: sticky texture across the whole upper" | PASS |
| 10 | Ghost Lacing, clean strike surface | IH1779 brief: "Ghost Lacing system covers the laces for a cleaner strike surface" | PASS |
| 10 | Cyclone 360 traction | IH1779 brief: "Cyclone 360 circular forefoot traction" | PASS |
| 11 | VNMSkin | IQ1886 brief: "Nike VNMSkin: grippy layer over the strike zone" | PASS |
| 11 | Flyknit base, ball close | IQ1886 brief: "Flyknit base works with VNMSkin to bring your foot closer to the ball" | PASS |
| 11 | low-cut, firm ground | IQ1886 brief: "Low-cut collar"; "Firm-ground (FG) outsole for dry natural grass" | PASS |
| 12 | Nanostrike+ Primeknit upper | HP9971 brief: "Upper: synthetic and textile Primeknit with the Nanostrike+ striking zone" | PASS |
| 12 | fold-over tongue | HP9971 brief: "Closure: laces with the signature fold-over tongue" | PASS |
| 12 | AG outsole for 3G | HP9971 brief: "Surface: Artificial Grass (AG), for 3G and 4G synthetic pitches" | PASS |
| 12 | 7.2 oz | HP9971 brief: "Weight: 7.2 oz (204.5 g)" | PASS |

**No ESCALATE, no FIX.** Every claim traces to a scrape-sourced brief line.

Compliance sweep across all 24 strings: no em dashes; no forbidden AI vocabulary; `adidas` lowercase including at sentence start (row 12); brand technology names in title case (Gripknit, Flyknit, FlyTouch, NikeSkin, VNMSkin, ReactX, Primeknit, Nanostrike+, Engineered Fit Last Neo); no FIFA or World Cup terms on any page (Nike and Mizuno hold no licence, and the adidas row is not a World Cup product); "cleats" used only on firm-ground products, turf products carry no cleat noun; no prices, stock state, size runs or store CTA; no heritage counts or superlatives; every meta title at or under 48 chars with no manufacturer-brand pipe suffix; every meta description between 120 and 160 chars with no colon-fragment opener.

---

## Post-C-FIX registry state

On import confirmation, `deliverables/tracking/products-master.csv` updates for the 12 rows: `primary_keyword` and `normalized_primary` to the new term, `primary_volume` to the new figure (blank where unmeasurable), `kw_recorded_date` 2026-08-14, and a note recording the pack-succession or hierarchy reason. `status` stays as-is (the pages are live; only two metafields change).

**Terms released, and who may claim them next:**

| Released term | Vol | Now available to |
|---|---|---|
| nike phantom 6 high academy turf | 70 | the Scary Good FA25 incumbent (`...-scary-good-pack-fa25`, live, in stock, unregistered). Not in Batch 15; candidate for the next batch |
| nike phantom 6 elite fg | 140 | nobody as written (cut-less). Batch 15 takes the cut-qualified `nike phantom 6 high elite fg` (210) |
| nike phantom 6 pro | 880 | nobody as written (cut-less and surface-less). Belongs to `/collections/nike-phantom`, status `inherited` |
| adidas predator elite ag | 590 | **Batch 15 row 6**, the Radiant Blaze FA25 AG incumbent, per Mike's 2026-08-14 upgrade decision |
| the other 8 | none | no measurable demand released |

---

## Batch 15 dependency

Batch 15 resumes once C-FIX is imported, and its cannibalization check runs against the **post-C-FIX** registry, not today's. Three Batch 15 rows are unblocked by this change:

- Row 2 `nike phantom 6 high elite fg` (210), previously overlapped by IH1779-900
- Row 5 `nike phantom 6 low pro fg` (70), previously overlapped by IQ1886-900
- Row 6, upgraded to `adidas predator elite ag` (**590**, up from 70), previously overlapped by HP9971
