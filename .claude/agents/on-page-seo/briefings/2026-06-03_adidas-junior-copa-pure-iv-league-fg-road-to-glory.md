# Workforce briefing: adidas Junior Copa Pure IV League FG (Road To Glory Pack, SP26)

- **Date:** 2026-06-03
- **Brief:** `deliverables/page-optimizations/2026-06-03_session-01/adidas-junior-copa-pure-iv-league-fg-road-to-glory_brief.md`
- **SKU:** KI0662 (ProSoccer internal KI0662-1)
- **URL:** /products/adidas-junior-copa-pure-iv-league-firm-ground-soccer-cleats-road-to-glory-pack-sp26
- **Tier:** Tier 1 foundational (first real-product PDP pilot; validates the full PDP discipline end to end and the Soccer Cleats template for a current-cycle, in-stock SKU)

## Phase 0: SKU resolution and eligibility

- **Eligibility:** Mike-verified in-stock at submission, 2026-06-03 (Shopify admin). Pre-vetted live and in-stock per the batch dispatch eligibility rule. Storefront render confirms "only 1 item left in stock" and a $59.99 price; all size variants render "sold out or unavailable" in the scrape, which is the known unreliable storefront signal (eligibility codification 2026-05-29). Trusting Mike's pre-vet.
- **Resolution path note (architectural finding, surface to Mike):** the on-site search `https://www.prosoccer.com/search?q=KI0662&type=product` returns "No results found for KI0662" with status 200. ProSoccer storefront search does not index the manufacturer/adidas article number. SKU had to be resolved through external search (adidas.com confirms product code KI0662 = Copa Pure IV League FG Junior; Soccer Village lists SV-KI0662). Implication for the Phase 0 workflow: a raw `?q=<SKU>` search URL is not a reliable resolver. Recommend Phase 0 resolve by product handle or by ProSoccer internal SKU (KI0662-1), or Mike supplies the handle at submission.

### Current-state capture (six fields, live PDP, Firecrawl 2026-06-03)

1. **Title (H1):** adidas Junior Copa Pure IV League Firm Ground Soccer Cleats - Road To Glory Pack (SP26)
2. **Slug:** adidas-junior-copa-pure-iv-league-firm-ground-soccer-cleats-road-to-glory-pack-sp26 (83 chars, over the 70 limit)
3. **Meta Title:** truncated theme output `adidas Junior Copa Pure IV League Firm Ground Soccer Cleats - Road To  – ProSoccer` (the theme appended the brand suffix and the field overflowed; current Meta Title is just the H1, unoptimized)
4. **Meta Description:** auto-generated from the body, overflows and truncates (`...Paying tribute to the iconic adiPure, a 'pinline' design runs from forefoot to heel for unmistakable...`). Not a written meta.
5. **Short Description (metafield):** verbatim current-state citation (the live UK-convention copy this optimization replaces): `Watch them bring their class to the pitch in Copa Pure IV League Firm Ground Football Boots engineered for assured play. Their synthetic upper has a cushioned sockliner to help keep every kick and tackle comfortable. Underneath, a TPU Comfort Plate outsole digs into dry natural grass surfaces to help keep their football flowing.` (adidas stock copy, ~53 words; note the live page uses "Football Boots", exactly the UK convention the new US market language discipline corrects)
6. **Long Description (body):** adidas stock one-liner ("The lace closure and floating tongue offer an easy step-in...Paying tribute to the iconic adiPure, a 'pinline' design runs from forefoot to heel for unmistakable adidas style.") plus 7 spec bullets (Regular fit / Laces / Synthetic upper / Cushioned textile sockliner / COMFORT PLATE TPU outsole for firm ground / Floating tongue / Weight 193 g).

Current copy is bare adidas-supplied content. Clean separation between Short Description (metafield hero block) and Description (accordion) confirmed, no blocker. Large optimization headroom.

### Product specs captured

- Colorway Solar Turbo / Ivory / Core Black; weight 193 g (6.8 oz); synthetic Fusionfeel upper (League tier; NOT the calfskin Fusionskin of Elite/Pro); COMFORT PLATE TPU outsole, firm ground; floating tongue; lace closure; cushioned textile sockliner; regular fit; adiPure "pinline" heritage design; youth sizes 1 to 6; price $59.99; vendor adidas; type Footwear.
- 8 gallery images: Side1, Side2, Lateral-Front, Lateral-Back, Top, Bottom, Detail1, Detail2.

## Phase 2: Keyword research (DataForSEO, US, en, 2026-06-03)

- `kids soccer cleats` 18,100/mo (HIGH, transactional) | `youth soccer cleats` 5,400 | `adidas copa pure` 2,400 | `copa pure` 1,300 | `adidas copa` 8,100 (broad, partly Spanish-intent) | `adidas copa pure soccer cleats` 320 | `copa pure 4` 260 (yearly +743%) | `adidas copa pure 4` 210 (yearly +556%) | `copa pure cleats` 170 | `adidas copa pure iv league` below DB volume floor.
- Primary selection rationale: the product is a year/generation-bound SKU, so primary is the generation + tier exact match `adidas copa pure iv league` (the product's name), not the higher-volume generic. Realistic target is the junior + generation + colorway long-tail plus incidental category traffic.
- Supporting keyword deployed (one, highest-volume candidate): `kids soccer cleats`. Deployed once in Short Description and three times in the body (two `kids' soccer cleats`, one `kids' cleats` variant). Exception clause not triggered (no second candidate within 10% of 18,100).
- Other supporting candidates retained as record, not deployed at depth: `youth soccer cleats`, `adidas copa pure`, `copa pure`, `adidas copa pure soccer cleats`, `copa pure 4`.
- SERP (`adidas copa pure iv league`): adidas.com owns #1, #2, #6, plus the Kids JR6262 at #8; Pro:Direct #4; Soccer Village #9; prosoccer.com absent. Google AI Overview frames the League as "high-value, mid-tier... classic leather-like feel with modern comfort... budget-friendly." People Also Ask: "Are copa pure 4 good?", "Who wears the adidas Copa pure?", "What positions are Copa Pure best for?", "Which is better, F50 or Copa?" Reddit: `Do Adidas Copa Pure IV League TF run long?` (fed FAQ + sizing copy).

## Phase 3: Topic research (Tavily + SERP, 2026-06-03)

- adidas three-silo structure: F50 = speed, Predator = control/power, Copa = touch/comfort. Copa is "best for touch, comfort, clean ball feel; technical players, midfielders, all-game comfort over speed."
- Copa Pure IV (4) = 2026 generation. Change vs III: returned to a classic u-throat with a floating tongue (dropped III's Primeknit/knit tongue), less bulk, upper sits closer to the foot. adiPure "pinline" heritage design (Footy Headlines confirms "pinline" on the 2026 Copa Pure 4 packs).
- Tiers Elite / Pro / League / Club. League = value/mid tier, recreational + youth + entry; uses Fusionfeel synthetic (leather-like softness, NOT calfskin; calfskin Fusionskin is Elite/Pro). TPU Comfort Plate outsole, FG.
- Copa silo pro wearers (adidas.com): Bernardo Silva, Sam Coffey, Joško Gvardiol. Used honestly in copy as the silo/feel "worn across the line... sized down for younger feet," not a claim that this junior League SKU is pro-worn. Sam Coffey chosen alongside Bernardo Silva to nod to both boys and girls (the youth collection is "Boys, Girls").
- Kids-cleat buying context (Storelli): three tiers; League/Club mid-tier roughly $60 to $150; FG = natural grass, AG = artificial turf; true to size, fast break-in; wide feet half-size up.
- "Road To Glory" = adidas's SP26 World Cup pack. adidas is FIFA-licensed, so World Cup terminology is permitted; used as a light seasonal anchor.

## Brand IP classification

adidas product page = adidas-classified. FIFA World Cup terminology family permitted. "Road To Glory" is adidas's own 2026 World Cup collection. Compliance scan across Title, Meta Title, Meta Description, Short Description, Long Description, FAQ, and internal-link anchors: clean (the only FIFA-family usage is the permitted "World Cup summer / World Cup drop" on an adidas page).

## Sibling-SKU uniqueness

Four colorway packs share the junior Copa Pure IV League FG model on prosoccer.com: Road To Glory (this SKU), Ice Cold Precision, Immortal DNA, Born For Goals. Title and Meta Title differentiate ours by "Road To Glory" plus "Junior/Jr" against the adult SKUs. No duplicate or near-duplicate title risk after optimization.

## Internal-link validation (content-signal, 2026-06-03)

- `/collections/adidas-copa`: 200 OK, H1 `Adidas Copa Soccer Cleats for Men, Women, Youth`, 57 product cards, Copa Pure IV line (incl. this SKU) at the top. Selected (brand-line, anchor "the adidas Copa lineup").
- `/collections/firm-ground`: 200 OK, H1 `Youth Firm Ground Soccer Cleats`, 156 youth product cards, youth-products flag true. Selected (surface + age, anchor "youth firm-ground cleats"). Minor caveat: the first-three product extraction surfaced a couple of turf/indoor items (likely a cross-sell widget bleed); the collection identity, H1, title, and 156-product depth are unambiguously youth firm ground, so the link is on-topic.
- Considered and not used: `/collections/adidas-products` (brand-generic, beaten by the more specific Copa link); `/collections/youth-soccer-shoes` (age-only; the firm-ground collection is the more specific surface + age match and avoids duplicating a discovery path).

## Image optimization flags (implementation-side, for Mike/Misha)

- Filenames are descriptive (`adidasJuniorCopaPureIVLeagueFirmGroundSoccerCleats-RoadToGloryPack_SP26_Side1.jpg` etc). Good, no rename needed.
- Source images are large (width up to 1946 to 2000 px); Shopify serves responsive WebP variants via CDN params, so this is acceptable, no action required.
- Gallery order: the media set opens on `Detail2` first, with `Side1` (the natural hero) further down the order. Recommend reordering so Side1 is the primary/hero image. Implementation-side, admin work.

## Taxonomy

`Apparel & Accessories > Shoes > Athletic Shoes > Soccer Cleats` (firm ground). Apply in Shopify admin (taxonomy is admin-side, not theme content).

## Gate and discipline self-check (SCRIBE Phase 4, before ORIN re-check)

- 14 gates: Gate 1 voice check PASS (script run, clean). Gate 12 keyword distribution: primary present in all required fields; body primary count 4 to 7 with variants; one supporting keyword at three body mentions plus one Short Description mention. Gate 13 anti-stuffing: no comma-stacked keyword lists, no prices in body, no 3+ brand sentences, alt text distinct and not stuffed. Gate 14 specific counts: only verified product-structure counts used (three adidas silos, four tiers, eight images), no catalog-inventory counts.
- 8 Phase 4 disciplines: image precision (floating tongue / pinline / outsole described concretely), parallel construction (the F50/Predator/Copa list and the turf/AG/IC list are parallel), supporting-keyword selection (one, highest volume), adidas styling (lowercase throughout, script-verified), and the four editorial sub-disciplines (reader-first, cognitive load, value-first sequencing, positive emotional anchoring; no manipulation language in our copy).
- 9 PDP disciplines: complexity classified Complex; field lengths Title 71, Meta Title input 45 (59 with suffix), Meta Description 156, Short Description 79 words, Description body 395 words, handle flagged; unique titles vs siblings; alt text per image; taxonomy recommended; prose H2 + dedicated Product Details bullet H2; FAQ 4 net-new; reader-first principle governs throughout.

## Items surfaced for Mike at the gate

1. Storefront SKU search does not resolve manufacturer article numbers (Phase 0 resolver change recommended).
2. URL handle is 83 chars (over 70); recommend rename to `adidas-jr-copa-pure-iv-league-fg-road-to-glory` (46 chars) but only with a Misha-coordinated 301; safe to defer since the page is new with little equity.
3. Theme-level scarcity message "Hurry up, only 1 item left in stock" renders on this live PDP (the same theme-level pattern flagged in commit 9b665b2; out of workforce copy scope, Mike's call).
4. Gallery hero-image order (Detail2 first, Side1 lower) recommended for reorder.
5. Copa silo pro wearers are framed at the silo level, not as a claim about this junior League SKU. Confirm the honest framing reads right to Mike.
