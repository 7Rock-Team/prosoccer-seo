# Batch 13 audit trail (2026-08-04 session-01)

_ORIN pre-dispatch record. 10 footwear SKUs. First batch produced under the pack-succession rule (`context/workforce-conventions.md` 'Pack succession and PDP keyword ownership (v2)'). Mike approved the ten primaries 2026-08-04._

## READ THIS FIRST: every primary in this batch has NO MEASURABLE SEARCH VOLUME, and that is the rule working correctly, not sloppy keyword work

All ten pages ship with a pack-qualified primary that returns **no measurable volume in both DFS endpoints** (`kw_data_google_ads_search_volume` and `dataforseo_labs_google_keyword_overview`, US/en, 2026-08-04). This is BY DESIGN under pack succession: every one of the ten has a concurrent live pack sibling on the sitemap for the same model + tier + cut + surface, so the unqualified model-tier term belongs to the earliest-shipped live incumbent, and each of these newer packs takes a pack-qualified sub-floor primary. Pack-qualified terms are near-zero by design.

The alternative (letting all ten compete with their own live siblings for the incumbent unqualified term) is worse: ten pages cannibalizing one term. So these ten are **not search-acquisition surfaces**. Their value is conversion quality, internal linking (sibling tongue/surface choice + model-collection support), and collection support. A future reader who sees ten zero-volume primaries should read them as correct pack-succession bookkeeping, not as a keyword-research miss. Where the demand actually lives (the unqualified model-tier terms) is recorded per SKU below and is a collection-workstream dependency, logged in `work-log/follow-ups.md` 2026-08-04.

DFS ground truth for the demand that these PDPs do NOT target (it belongs to collections): `adidas predator elite` 9,900/mo; `adidas predator elite fg` 1,000; `adidas predator elite fold over tongue fg` 1,000; `adidas predator elite ag` 590; `adidas f50 league` 720; `nike phantom 6 high club` 170; `nike tiempo maestro academy turf` 20; `nike shadow pack` 260; `nike phantom 6 shadow pack` 50; `chaos vs control` 50 (informational).

## Brand-IP posture (all ten): cycle-language-only, no FIFA / World Cup language

Nike holds no FIFA license. adidas holds an event-scoped 2026 World Cup license, but these are Chaos vs Control pack cleats, NOT World Cup products, so the WC license is not invoked. Every SKU's gate-meta posture is `cycle-language-only` (the enum value that bans FIFA/WC terms); for the adidas SKUs this is deliberate, not an error (the `fifa-permitted` posture is reserved for adidas 2026 WC pages only).

## Per-SKU resolutions (pack collision + incumbent + primary + DFS)

| SKU | Primary (pack-qualified, sub-floor) | DFS (both endpoints) | Incumbent holding unqualified term | Avatar |
|---|---|---|---|---|
| IH4699 | adidas predator elite fg chaos vs control | no measurable volume | earliest live SP24 std-tongue FG pack; our shipped HP9973 holds `adidas predator elite fg` (1,000) grandfathered | Tyler |
| JP6248 | adidas predator elite fold-over tongue fg chaos vs control | no measurable volume | JP6237 holds `adidas predator elite fold over tongue fg` (1,000) | Tyler |
| IH4707 | adidas predator elite fold-over tongue ag chaos vs control | no measurable volume | HP9971 holds `adidas predator elite ag` (590) | Tyler |
| IH7090 | adidas f50 league mid fg chaos vs control | no measurable volume | KJ6714 holds `adidas f50 league` (720) | Tyler (2nd Jennifer) |
| IH4586 | adidas f50 league mid turf chaos vs control | no measurable volume | IH4582 (RTG SP26, confirmed same mid-cut config via Phase 0) holds `adidas f50 league turf` | Tyler (2nd Jennifer) |
| HQ2275 | nike phantom 6 high club fg mg shadow fa26 | no measurable volume | earliest live FA25 pack (Shadow FA25 / Scary Good FA25) | Jennifer |
| IB4484 | nike tiempo maestro academy turf shadow fa26 | no measurable volume | earliest live SP26 pack (Shadow SP26 / Attack SP26); IQ2388 Breakout SU26 is NOT incumbent (re-qualified, below) | Jennifer |
| IO1486 | nike kids vapor 17 club flex ps shadow | no measurable volume | Break 'Em FA26 kids twin (FA26 ship-order tie) | Jennifer |
| IO1552 | nike junior superfly 11 club fg mg shadow | no measurable volume | Breakout SU26 junior twin | Jennifer |
| IO1554 | nike junior superfly 11 club turf shadow | no measurable volume | Break 'Em FA26 junior twin (FA26 ship-order tie) | Jennifer |

Season-coding: `fa26` only on HQ2275 and IB4484 (Shadow recurs FA25/FA26 and SP26/FA26 respectively). No season code on the five Chaos vs Control (single FA26 occurrence) or on the Superfly/Kids-Vapor configs (Shadow does not recur for those exact configs).

## IH4586 Phase 0 finding (was flagged ambiguous, now resolved)

IH4586 (Chaos FA26) and IH4582 (RTG SP26) are the SAME config: both League Mid Turf, both mid-cut ankle height (IH4586 title says "Mid"; IH4582 drops "Mid" from its title but its body confirms mid-cut), both $89.99. So IH4586 has a concurrent live pack sibling (IH4582, incumbent) and is pack-qualified, not unqualified.

## IQ2388 re-qualification (Mike decision 2026-08-04; folds into this batch commit)

IQ2388 (Tiempo Maestro Academy Turf, Breakout SU26) was retargeted to the UNQUALIFIED `nike tiempo maestro academy turf` (20/mo), committed but NOT imported. Under pack succession the incumbent is the earliest live pack = SP26 (Shadow SP26 / Attack SP26), not IQ2388 (SU26). So IQ2388 must be pack-qualified. Re-qualified primary: **`nike tiempo maestro academy turf breakout`** (no measurable volume; "Breakout" does not recur for this config, so no season code). The 20/mo unqualified term releases to the earliest live SP26 incumbent (unregistered). IQ2388 still ships as its own meta-only change. Asymmetry on the record: HP9973 / KJ6714 / JP6237 share the not-truly-earliest property but stay grandfathered under clause 9 because they are shipped; IQ2388 is not shipped, so it is fixed. Registry row + retarget spec edit applied in this batch commit.

## Cannibalization (exact / containment / token-subset), full-registry via _registry1_primaries.txt

No exact or harmful collisions. Registry containments (IH4699 -> HP9973, JP6248 -> JP6237, IH4707 -> HP9971, IH7090 -> KJ6714, IB4484 -> IQ2388) are the intended incumbent-unqualified -> newer-pack-qualified structure. Three post-index GSC watch items logged: (1) YF3F3V9 kids/youth; (2) IO1552 / IO1554 junior terms as token-supersets of shipped adult IM0358 / IO1498; (3) IH4699 std-tongue term as a token-subset of JP6248 fold-over term (tongue is the differentiator).

## Differentiation lanes (anti-convergence; SCRIBE writes prose FROM the lane, exemplar anchors structure only)

- IH4699 (EXEMPLAR, Predator Elite std FG, Tyler): the deep-lying creator who dictates tempo on firm natural grass; standard tongue for the traditionalist; set-piece control.
- JP6248 (Predator Elite fold-over FG, Tyler): the fold-over tongue as an unbroken strike surface; the finisher who wants a clean instep; heritage-detail angle.
- IH4707 (Predator Elite fold-over AG, Tyler): the artificial-grass specialist; plate tuned to the synthetic blade; the player whose home pitch is 3G.
- IH7090 (F50 League Mid FG, Tyler/Jennifer): F50 speed DNA at an accessible tier, mid-cut ankle lockdown; the accelerating winger on firm grass who wants the F50 feel without the Elite spend.
- IH4586 (F50 League Mid Turf, Tyler/Jennifer): the same speed built for weeknight turf and small-sided; grip for the short synthetic blade.
- HQ2275 (Phantom 6 High Club FG/MG, Jennifer): an accessible real-Phantom control cleat for the developing player, high collar, mixed FG/MG grounds; parent-buyer reassurance.
- IB4484 (Tiempo Maestro Academy Turf, Jennifer): soft FlyTouch leather touch on turf; the young player who wants a leather feel on the hard surface.
- IO1486 (Kids Vapor 17 Club Flex PS, Jennifer): the youngest player's first speed cleat, knit cuff snug fit; first organized soccer.
- IO1552 (Junior Superfly 11 Club FG/MG, Jennifer): grade-school speed cleat, knit cuff, the young player who wants the Superfly look on grass.
- IO1554 (Junior Superfly 11 Club Turf, Jennifer): the turf version for the young player; weeknight turf.

## Validated internal links (ORIN link-check, all live 200 + content signal from 2026-08-04 sitemap map)

Collections: `/collections/adidas-predator`, `/collections/adidas-f50`, `/collections/adidas-chaos-vs-control-soccer-cleats`, `/collections/nike-phantom`, `/collections/nike-mercurial`, `/collections/nike-tiempo-maestro`, `/collections/nike-shadow-soccer-cleats`, `/collections/youth-soccer-shoes`, `/collections/artificial-turf`. Sibling PDPs (this batch, all live + purchasable per Phase 0): Predator trio cross-link; F50 FG<->Turf pair; Junior Superfly FG/MG<->Turf pair. Per-SKU placement in each input file.

## Step 14 note
The 10 new registry rows are appended to products-master.csv AT STEP 14 (post-import), per SEO_BATCH_PROCESS.md. This commit contains briefs + input files + IQ2388 re-qualification + audit trail + follow-up logs, NOT the 10 new rows.

## Pre-import corrections (2026-08-13, Step 2 cold review, Mike-directed)

Six items came back from Step 2's cold read of the ten briefs. Nothing had been imported, so all of it was fixed in place in the brief files.

**Season-code re-check (live storefront, 2026-08-13).** Rule applied: the primary carries the pack name always, the season code only when a live same-pack sibling from ANOTHER season exists for the same model + tier + cut + surface. Checked HQ2275, IO1486, IO1552, IO1554 against the live Shopify storefront (`/search/suggest.json`, published products only) plus the 2026-08-03 product sitemap chunks. IB4484 was already confirmed and was not re-opened.

| SKU | Cross-season same-pack sibling | Evidence | Season code |
|---|---|---|---|
| HQ2275 | YES | `nike-phantom-6-high-club-firm-multi-ground-soccer-cleats-shadow-pack-fa25`, live 200, H1 "Nike Phantom 6 High Club Firm/Multi Ground Soccer Cleats - Shadow Pack (FA25)", $46.00, tagged `footwear-pack_nike-shadow-pack-fa25` | keeps `fa26` |
| IO1486 | NO | only other live Kids Vapor 17 Club Flex PS FG/MG pack is Break 'Em FA26 (`...-flex-ps-fg-mg-soccer-cleats-break-em`), a different pack | none |
| IO1552 | NO | other live Junior Superfly 11 Club FG/MG packs are Break 'Em and Breakout SU26, both different packs | none |
| IO1554 | NO | only other live Junior Superfly 11 Club Turf pack is Break 'Em, a different pack | none |

All four primaries were already correct as written; the season-coding line above this section holds. The defect was confined to HQ2275's meta title.

**Applied fixes.**

1. HQ2275 Meta Title: `Nike Phantom 6 High Club FG/MG Soccer Cleats` to `Nike Phantom 6 High Club FG/MG Shadow FA26` (42 chars). The old title was the bare `nike phantom 6 high club` term this brief's own keyword table marks incumbent-owned, do-not-target. Same defect class as the IQ2388 error, caught pre-import again.
2. IH4707 Meta Title: `adidas Predator Elite FO AG Chaos vs Control` to `adidas Predator Elite Fold-Over Tongue AG` (41 chars). Matches its own primary and its FG sibling JP6248's title. "FO" is a live-product-title abbreviation, not a search term. Live product title unchanged.
3. IH4699 third FAQ answer: rewritten to link the AG sibling and to stop calling artificial grass "turf" (the AG plate is for artificial grass; turf is the separate short-pile surface).
4. JP6248 third FAQ answer, final sentence: same AG-sibling link added. IH4707 already linked back to JP6248, so the Predator trio now cross-links in both directions.
5. Brand technology name casing normalized to title case: IH4586 HALOSKIN to Haloskin, HALOSHELL+ to Haloshell+; JP6248 PRIMEKNIT to Primeknit (3 instances), STRIKEFRAME to Strikeframe (3 instances). Sweep of the other eight briefs found no further all-caps tech names.
6. `nike shadow pack` (260/mo) as the secondary on five briefs is NOT a defect; the hierarchy rule governs primaries. Logged as `strategy/sprint-backlog.md` B-COLL-02 (collection-side question) and left alone here.

Link target validated live 2026-08-13: `adidas-predator-elite-fo-tongue-ag-soccer-cleats-chaos-vs-control`, 200, H1 "adidas Predator Elite Fold-Over Tongue Artificial Ground Soccer Cleats - Chaos Vs Control Pack (FA26)", $279.99.

Codified from this pass: `context/page-type-playbooks/product-page-playbook.md` 'Brand technology name casing' and 'Pack season-code qualifier', both with worked examples; `context/workforce-conventions.md` pack-succession point 2 tightened to the configuration-scoped form, and a brand-technology entry added to the brand-styling registry.

No product title, URL handle, taxonomy, tag, variant, or price was touched. Registry rows for the changed fields land at step 14 with the rest of the batch.
