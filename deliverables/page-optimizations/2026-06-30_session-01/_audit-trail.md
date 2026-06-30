# Batch Audit Trail - 2026-06-30 session-01

## Batch metadata
- Batch 5. 11 PDPs. Wave 1 dual Tier 1 exemplars (KI0586 Copa Pure IV Elite FG; 7651TX3926 Bosnia Youth Home, committed `812b613`) + Wave 2 (9 Tier 2A siblings).
- Composition: 5 senior adidas Copa Pure IV (Elite FG, Pro FG, Pro Turf, League FG, League Turf); 1 Nike Mercurial Superfly 11 Pro FG; 1 Nike Tiempo Maestro Academy Turf; 4 jerseys (Croatia Youth Home J000692-CRFT, Croatia Women's Away J000694-CRFT, Bosnia Youth Home 7651TX3926, Bosnia Youth Away 7651TX3927).
- Architectural firsts: first senior + multi-tier Copa family; first Pro-tier Superfly; first Nike Academy tier + first Tiempo Turf; first Bosnia nation + first Kelme brand; Croatia matrix extension (youth-home + women's-away).
- Brand-IP: 5 Copa = adidas (FIFA family permitted). 6 non-adidas (Superfly/Tiempo = Nike; 2 Croatia = Nike; 2 Bosnia = Kelme) = cycle language only, FIFA/WC copy-forbidden.
- Approval mode: APPROVE-EVERY-ACTION. Mike approved Checkpoint 1 (keywords), Checkpoint 2 (exemplar plan), Checkpoint 2b (exemplar gate), Checkpoint 3 (Wave 2 gate).
- Ran under the 6/29 fabrication codification + 6/30 heading-level-agnostic voice_check: 9/9 Wave 2 voice PASS, 0 `####` drift, 6 scrape-wins trap catches, 0 FIFA/WC copy violations (+1 permitted Bosnia "2014 World Cup debut").

## Per-SKU primary keyword assignments (white-label PDPs tab -- Mike manual entry; ORIN reads, never writes)
| SKU | Product | Primary | Floor status | Pack/cycle secondary |
|---|---|---|---|---|
| KI0586 | Copa Pure IV Elite FG | adidas copa pure iv elite | clears (cycle surge) | adidas copa pure road to glory |
| KI0625 | Copa Pure IV Pro FG | adidas copa pure iv pro fg | sub-floor* GSC override | adidas copa pure road to glory |
| KI0630 | Copa Pure IV Pro Turf | adidas copa pure iv pro turf | sub-floor* GSC override | adidas copa pure road to glory |
| KI0645 | Copa Pure IV League Turf | adidas copa pure iv league turf | sub-floor* GSC override | adidas copa pure road to glory |
| KI0653 | Copa Pure IV League FG | adidas copa pure iv league fg | sub-floor* GSC override | adidas copa pure road to glory |
| IO8224-900 | Superfly 11 Pro FG | nike mercurial superfly 11 pro | sub-floor* GSC override | nike mercurial superfly 11 breakout pack su26 |
| IQ2388-901 | Tiempo Maestro Academy Turf | nike tiempo maestro academy | clears (170/mo) | nike tiempo maestro breakout pack su26 |
| J000692-CRFT | Croatia Youth Home | croatia youth home jersey 2026 | sub-floor* GSC override | croatia 2026 home jersey youth |
| J000694-CRFT | Croatia Women's Away | women's croatia jersey | GSC override (pos 5.6, 164 impr) | croatia 2026 away jersey women |
| 7651TX3926 | Bosnia Youth Home | bosnia jersey 2026 | sub-floor* GSC override (pos 6.8) | kelme bosnia jersey 2026 |
| 7651TX3927 | Bosnia Youth Away | bosnia away jersey 2026 | sub-floor* GSC override | kelme bosnia away jersey 2026 |

## Defense-in-depth: gate catches (codification at production scale)
- 6 scrape-wins material/spec overrides: KI0625 Primeknit tongue (not floating); KI0630 Fusionfeel 2.0 (not Fusionskin/calfskin); KI0653 Comfort Plate TPU (not Comfort Frame) + League explicitly "not leather"; 7651TX3927 Bosnia away colorway White/Navy (not blue) + sizing YL/YXL only; IQ2388 FlyTouch leather + rubber outsole (not Techleather/Maestro360).
- Copa tier x surface matrix corrected vs the 6/29 guardrail (calfskin Fusionskin = FG Elite/Pro only; Fusionfeel synthetic = Pro Turf + both League; plate Comfort Frame [Elite FG] vs Comfort Plate TPU [League FG] vs rubber turf). copa.md guardrail refined this batch.
- Casing: 9/9 voice_check PASS under the new heading-level-agnostic backstop; KI0586 exemplar `####` defect caught at the Wave 1 gate and corrected before skeleton extraction.

## Standing flags for Mike (carried to handoff)
- **THEME BRAND-IP EXPOSURE (Tony escalation + Misha):** sitewide "ROAD TO THE '26 WORLD CUP" / "IT'S WORLD CUP TIME, BABY!" chrome on non-adidas (Nike/Kelme) PDPs; 4 SCRIBEs flagged it. Brief copy is clean; the theme chrome is the exposure. Fix: theme conditional logic rendering tournament chrome only on FIFA-licensed (adidas-family) vendor pages.
- **Bosnia men's PDP gap:** men's Bosnia Home/Away PDPs exist (Bosnia collection shows 3 men's products), in stock, untracked in the white-label sheet, absorbing 1,600-9,900/mo head demand unoptimized. Future batch + sheet rows; Tony sync.
- og:image `http://` + `<title>` truncation: standing Misha theme items, re-confirmed across these PDPs.
- White-label sheet rows to add (Mike): J000694-CRFT Croatia Women's Away; men's Bosnia Home PDP.
- J000694 gallery image mislabel ("Croatia Men's Away (Modric)" on the women's-away page); corrected alt text in the brief, apply at implementation.
- URL handles over 70: KI0586 (75), KI0653 (75). Not auto-changed (301 equity risk; Misha coordination if Mike opts in).
- Croatia jersey word-count: J000692 held at sibling parity (534 full-body; J000691=507, J000695=534). Jersey-length precedent clarified in the product-page-playbook this batch (jerseys run above the generic Complex ceiling; match the shipped nation set).

## Batch summary
11/11 briefs voice_check + ORIN-gate clean. Wave 1 exemplars committed `812b613`. Wave 2 + this consolidation + copa.md refinement + playbook clarification committed [batch-close hash]. Post-ship: 11 per-SKU prose-pattern entries appended to Registry 2 silos (copa +5, mercurial +1, tiempo +1, national-team-jerseys +4) in a separate post-ship commit per the silo append protocol.

## Per-SKU notes (consolidated; the 3 SKUs below carry full SCRIBE-written entries: IO8224, IQ2388, KI0630)
- **KI0586 Copa Pure IV Elite FG (Tier 1 exemplar, `812b613`).** Premium calfskin playmaker; Fusionskin + Comfort Frame; floating tongue; no current face (Declan Rice TIME-SENSITIVE); colorway Solar Turbo/Ivory/Core Black (scrape; corrected the silo "Solar Red" note); 430 words (Elite band). Gate: `####`/`#####` heading defect + 2 lowercase body H2s caught at Wave 1, corrected to `##`/`###`; voice PASS. Handle 75 (flag).
- **KI0625 Copa Pure IV Pro FG (Tier 2A).** Touch at value, FG natural grass; Fusionskin calfskin + **Primeknit tongue** (scrape override vs the silo "floating tongue" note); Comfort Frame; no Ortholite brand asserted (scrape said only "anatomical synthetic"); 348 words (Pro band); voice PASS.
- **KI0645 Copa Pure IV League Turf (Tier 2A).** Entry value/youth on turf; **Fusionfeel synthetic (NOT leather)**; rubber turf outsole; weight 9.3 oz (264.5g); 340 words (League band, top of band = realistic lean floor for the mandated footwear structure); voice PASS.
- **KI0653 Copa Pure IV League FG (Tier 2A).** Entry value/youth FG; **Fusionfeel synthetic (NOT leather; explicit "is it leather? No" FAQ)**; **Comfort Plate TPU** (scrape override vs Comfort Frame); 338 words (League band); voice PASS. Handle 75 (flag).
- **7651TX3926 Bosnia Youth Home (Tier 1 exemplar, `812b613`).** Zmajevi/Dragons gender-neutral youth hook; 2014 World Cup debut historical anchor (not "first/only"); blue + golden-lily; Kelme TIME-SENSITIVE; Fusionfeel n/a (jersey); 380 words; page sold-out (evergreen copy, no scarcity); internal link upgraded to the validated Bosnia collection; voice PASS.
- **7651TX3927 Bosnia Youth Away (Tier 2A).** Bosnia identity, away lane; **away colorway White/Navy (scrape override, not blue)**; **sizing YL/YXL only (scrape override vs Home YS-YXL)**; 2014 WC debut anchor; cycle language only (+1 permitted WC use); 317 words; voice PASS.
- **J000692-CRFT Croatia Youth Home (Tier 2A).** Parent/young-fan HOME red-white sahovnica; Modric 10 customization angle (on-page option, not a squad claim); 0 FIFA/WC; "Vatreni" avoided; 534 full-body (held at sibling parity with J000695=534; J000691=507); voice PASS.
- **J000694-CRFT Croatia Women's Away (Tier 2A).** Women's-cut AWAY royal-blue; gender-umbrella primary `women's croatia jersey` (GSC pos 5.6, 164 impr); 0 FIFA/WC; "Vatreni"/"Lavice" avoided (gender/team-neutral per J000691 precedent); ~329 prose words; gallery image mislabel flagged; voice PASS.

## SKU IO8224-900 - Nike Mercurial Superfly 11 Pro FG (Breakout Pack SU26)

### Tier and lane
- Tier 2A (pattern-follow PDP, cleat category, CANONICAL template).
- Lane: Mercurial SPEED line, Superfly = high-cut straight-line speed (vs Vapor low-cut agility). First PRO-tier Superfly. Mirrors the IO8225 Vapor 17 Pro Pro-tier handling model (speed lineage at Pro value, a step below the Elite's stripped-back AtomKnit/FlyLite package), while holding the Superfly high-cut identity.
- Complexity: Complex (multi-tier footwear, buyer comparison needed). Pro tier band 340 to 390 words.

### Eligibility
- Mike-pre-vetted at URL submission (Shopify admin), normal Tier 2A dispatch. No strategic-exception flag. Scrape showed "only 2 items left" plus most variants sold out, treated as normal optimization (not closing-window, not pre-tournament; no exception applied).

### Phase 0 ground-truth (live scrape 2026-06-30, status 200, 1 credit)
Verified specs (scrape wins):
- Upper: FlyWeave ("tailored, secure fit to help fuel your speed")
- Studs: Chevron studs ("grip the field to stop on a dime and change direction")
- Cushioning: Air Zoom unit in the forefoot ("bouncy sensation with each step")
- Plate/surface: Firm Ground (FG) (from product name)
- Colorway: Multi-Color/Black
- Price: $179.99 (not used in body copy; Meta Description shipping signal only)
- Vendor: Nike; Type: Footwear; SKU variant string IO8224-900-M 5 / W 6.5

### Brand-IP classification
- Non-Adidas (Nike product). FIFA / "World Cup" terminology family FORBIDDEN.
- Compliance scan across all fields + link anchors: PASS. Cycle language only ("Breakout pack", "SU26", "Pro tier"). No "World Cup", "FIFA", or "WC" in any field.
- Note (not a copy defect): site chrome carries "ROAD TO THE '26 WORLD CUP" / "IT'S WORLD CUP TIME, BABY!" banners. That is theme-level chrome, outside this brief's copy scope; flag only if Mike wants a brand-IP review of sitewide banners on Nike PDPs.

### Fabrication guard (scrape-data-wins)
- Weight: OMITTED. Not present in scrape; not invented.
- ZoomX: NOT claimed (Elite-only tech). Pro positioned as "a step below the Elite's stripped-back package" with Air Zoom forefoot only, which is scrape-true.
- High-cut collar: stated as the Superfly model identity (the high-cut silhouette is the literal Vapor-vs-Superfly distinction, an evergreen model-line fact in the silo file). No specific collar tech name invented.
- Player association: NONE named. Kept evergreen ("longtime Mercurial fans", "the fastest attackers"). No unverified current signature player asserted.
- Tournament-status: evergreen framing throughout; no "title defense", "this summer", bracket, or first/best/only claims.

### Keyword selection and distribution
- Primary `nike mercurial superfly 11 pro`: sub-floor, GSC override (KIRA Phase 1). Placed in Title, Meta Title, Meta Description (early), Short Description (sentence 1), and across Description H2s + body via exact match and natural variations ("Superfly 11 Pro", "Mercurial Superfly 11 Pro"). Reads natural, not stuffed (read-aloud pass; no consecutive-sentence repetition).
- Supporting keyword (ONE, body): `superfly 11 pro` / `nike superfly 11 pro` woven ~3 to 5x in Description prose. Highest-coverage non-pack secondary.
- Pack-specific carve-out (Mechanism C): "Breakout pack" + "SU26" + "Multi-Color/Black" present in Description prose (H2-2) and Product Details bullet; covers `nike mercurial superfly 11 breakout pack su26` via natural variation.
- Secondaries: KIRA supplied no volume/difficulty figures at dispatch; Keywords-table cells left blank (no fabrication).
- Cannibalization check: siblings are distinct models/tiers (Vapor 17 Pro `nike mercurial vapor 17 pro`; Superfly Elite FG/AG). No primary-keyword collision with `superfly 11 pro`.

### Cross-brief / silo differentiation (vs shipped Mercurial entries)
- vs IO8219 Superfly Elite FG (hook: breakaway/ball-over-top, sprinter out of the blocks): this Pro brief uses the BACK HALF of the sprint (the thirty-yard chase, pulling clear, not the start). Distinct hook + metaphor.
- vs IO8221 Superfly Elite AG (hook: 3G under weeknight lights, cinder-to-synthetic track): not used; FG natural-grass framing only.
- vs IO8225 Vapor 17 Pro (hook: touch-and-turn in a crowded pocket, pickpocket metaphor, close control): mirrored only for Pro-TIER handling; hook/metaphor fully distinct (straight-line speed, not close control). Vapor explicitly cited as the close-control sibling (internal link).
- No reused hooks, H2 titles, or metaphors from the silo log.

### Internal links (live-validated 2026-06-30, full HTTPS canonical, Description body only)
1. https://www.prosoccer.com/products/nike-vapor-17-pro-firm-ground-soccer-cleats-breakout-pack-su26 - status 200, H1 "Nike Vapor 17 Pro Firm Ground Soccer Cleats - Breakout Pack (SU26)", $169.99, Add-to-cart, "Firm Ground" x45. Live PDP, not soft-404. Anchor "Nike Vapor 17 Pro", placed in use-case H2 (close-control sibling reference, authentic contextual fit).
2. https://www.prosoccer.com/collections/nike-products - status 200, title "Nike Products", 329 "Nike" / 103 "cleats" / 141 "products". Live collection, not soft-404. Anchor "Nike's cleat lineup", placed in tech/heritage H2 (where prose references where this sits in Nike's range). Placement split across two H2s, not mechanically defaulted.
- Zero internal links in Short Description metafield (conversion-critical hero block).

### Structure / casing
- 3 editorial body H2s, sentence case: "Built for the thirty-yard foot race" / "What makes the Superfly 11 Pro fast" / "Who the Mercurial Superfly 11 Pro is for".
- Structural H2s, Title Case: "Product Details: Superfly 11 Pro" (natural short name) / "Fit Notes" / "Care and Maintenance" / "FAQs about the Superfly 11 Pro".
- Reading order: hook -> tech/heritage -> use case -> Product Details -> Fit Notes -> Care -> FAQ. FAQ supplied as separate paste block per Brief Output Structure.

### Field-length checks (PDP hard limits)
- Title: 70 chars (30-100 OK). Unique vs Vapor sibling (different model).
- Short Description: 71 words (50-100 OK). Outcome-first, no feature-selling lead, no links.
- Description body: 388 words (Pro band 340-390 OK; full body = editorial prose 255 + Product Details 54 + Fit Notes 33 + Care 45, FAQ counted separately). Drafted to Pro tier band, not the Complex ceiling.
- Meta Title input: 40 chars; +theme suffix ~52 (under 60 OK). No "ProSoccer" in field.
- Meta Description: ~159 chars (<=160 OK). Free-shipping claim verified against scrape ("Free Shipping on Orders over $100").
- URL handle: existing 70 chars, preserved (no change; 301-avoidance).

### FAQ net-new-value
- 4 Q&As: Pro-vs-Elite, Superfly-vs-Vapor, surface (FG), sizing. Each answers a real buyer comparison question beyond the body. Answers unique to this SKU (questions may overlap topically with siblings).

### Gates
- Voice check: PASS (see session run).
- Gate 11 brand IP: PASS. Gate 12 keyword distribution: PASS. Gate 13 anti-stuffing: PASS (no comma-stacked lists, no price in body prose, no brand-stacking). Gate 14 unsupported counts: PASS. US-market language: PASS ("cleats", no `boots`). Measurement units: n/a (no fabricated temps/weights). adidas styling: n/a (Nike product). Internal link format: PASS (full HTTPS www canonical).

### Cost
- Firecrawl: 3 credits this session (1 Phase 0 scrape + 2 internal-link validations).
- DataForSEO: 0 (keywords supplied by KIRA at dispatch).

### Image optimization flags (implementation-side, Misha/Mike)
- og:image emitted over `http://` not `https://` (known theme-level issue across Nike PDPs; standing Misha audit item, not a copy fix).
- Theme `<title>` truncates at ~character 60 ("...Breakout Pack (S"); known theme truncation bug, standing Misha audit item.

## SKU IQ2388-901 - Nike Tiempo Maestro Academy Turf Soccer Shoes - Breakout Pack (SU26)

### Tier and word band
- Tier: Academy = Nike's accessible entry tier (Nike ladder: Elite > Pro > Academy > Club). Per `context/workforce-conventions.md` 'Brand tier nomenclature (added 2026-06-29)', Nike Academy maps to adidas League. **Word band used: League/Club 280 to 340 words. NOT the Elite band.**
- Body word count: 338 words (prose + bullets, heading labels excluded; 3 editorial prose H2s + Product Details bullets + Fit Notes + Care bullets; FAQ counted separately). Within band.
- Complexity: Complex line (Tiempo Maestro spans Academy/Pro/Elite and FG/AG/MG/TF and multiple packs), written to the entry-tier (League/Club-equivalent) length per tier-appropriate-length-within-Complex.
- Tier 2A pattern-follow; follows the shipped Tiempo Maestro Elite precedent. Two firsts: Nike Academy tier + first Tiempo Turf in the workforce.

### Phase 0 ground-truth (live scrape 2026-06-30, status 200, 1 credit) - scrape wins
- Upper: **FlyTouch leather** ("incredibly soft", "molds to your foot for comfort without overstretching", "lightweight FlyTouch upper provides consistent touch in wet or dry conditions"). NOT Techleather, NOT k-leather.
- Outsole: **rubber outsole** for traction on turf surfaces. NOT a Maestro360 plate. No stud-count.
- Surface: Turf (TF), artificial turf / older astroturf. Price: $84.99 (not used in body). Colorway: Multi-Color/Black. Sizing: adult unisex M 4 / W 5.5 to M 12.5 / W 14.
- Sibling colorways (same Academy Turf body, other packs): NU3/United, Shadow, Attack.

### Fabrication guard / FIFA traps caught
1. **Techleather + Maestro360 hypothesis OVERRIDDEN by scrape** (KJ6746 target behavior). Dispatch named the Maestro = Techleather + Maestro360 lineage but instructed to confirm from scrape. Scrape says FlyTouch leather + rubber turf outsole. Wrote FlyTouch leather + rubber outsole; "Techleather" and "Maestro360" appear nowhere in the brief.
2. **FIFA / "World Cup" forbidden** (Nike non-adidas, `context/brand-ip-constraints.md` + 'Non-FIFA brand language discipline'). Live page chrome carries "ROAD TO THE '26 WORLD CUP" / "IT'S WORLD CUP TIME, BABY!" banners = site chrome, NOT my copy. Brief uses cycle language only (Breakout Pack, SU26). Scan across all fields + alt text + link anchors: zero FIFA-family terms. PASS.
3. **No stud-count claim** (rubber turf outsole, not studs).
4. **No `boots`**; turf product written as "soccer shoes" / "shoes" (US market language discipline).
5. **No fabricated specs.** Weight, sockliner/insole tech, lining, lacing specifics not in scrape, so omitted (no invented weight added to a Product Details bullet; no US-unit dual notation needed because no real measurement is claimed).

### Omitted specs (not in scrape)
Weight; sockliner/insole technology; stud or nub count; lining material; heel-counter detail; lacing-system specifics; exact FlyTouch composition beyond "leather".

### Brand IP classification
Nike PDP = non-adidas. FIFA/World Cup family forbidden, cycle language only. Scan PASS.

### Keyword deployment
- Primary `nike tiempo maestro academy` (170/mo, clears floor; KIRA Phase 1; page ranks #1 for the full title). Title, Meta Title, Meta Description (first sentence), Short Description (sentence 2), existing slug, ~4 to 5 natural appearances incl. close variants ("Tiempo Maestro Academy", "Maestro Academy") across body + structural H2s. Exact-match preserved in Title and H2-1 body (equity-preservation, page ranks #1; meta iteration is the low-risk lever).
- Supporting deployed at depth (one, highest volume): `nike tiempo maestro` (5,400/mo).
- Pack-specific carve-out (Mechanism C): `nike tiempo maestro breakout pack su26` via "the rest of the Breakout pack" + "Breakout Pack, SU26" bullet.
- `tiempo turf shoes` (140/mo) + `nike tiempo maestro academy turf` appear naturally (turf shoe / academy turf), not force-deployed; retained for record. Gate 12(d): one supporting at depth. PASS.
- No primary cannibalization with the Maestro Elite FG PDP (primary `nike tiempo maestro elite fg`, distinct). `nike breakout soccer cleats` not targeted (pack collection's term).

### Differentiation vs shipped Maestro Elite FG/AG (silo log `context/silo-positioning/tiempo.md`)
Avoided ALL Elite phrasings: no conductor/orchestra/tempo/"sets the rhythm"/"half-turn in space" (Elite FG), no pianist/"different stage" (Elite AG), no Maestro360/Techleather, no Elite H2 titles. This lane: entry-tier turf player on artificial turf, soft FlyTouch leather, parent-getting-it-right value angle. Hook = "soft leather, real touch, made for turf" (settle the ball, don't blast it). No music metaphor anywhere. New silo entry for ORIN to append post-commit.

### Avatar scope
- Primary: Jennifer (parent for the turf/rec player; value + soft-leather-no-painful-break-in + right-shoe-for-the-turf-field; "Turf Anxiety" + "Growth Spurt Tax" frames). AIDAR Desire/Action.
- Secondary: Tyler (rec/adult turf regular wanting real leather feel without elite price; adult unisex M/W sizing means the wearer is often the buyer).
- Tertiary: Mike the Coach (turf-league player on budget).
- Excluded: Carlos not led (footwear, not a federation kit; drop-follower served by the pack-collection link).

### Sibling-SKU title uniqueness
Differentiated by tier (Academy), surface (Turf), pack (Breakout). Distinct from Elite FG/AG and from the Academy Turf siblings in NU3/Shadow/Attack packs. Only Academy + Turf + Breakout combination. No collision.

### Internal links (2, PDP internal-only, Description body only, validated 2026-06-30 with content signals)
1. https://www.prosoccer.com/collections/nike-tiempo-maestro - status 200, meta title "Nike Tiempo Maestro Soccer Cleats | Prosoccer.com", 245 model mentions + 60 "academy turf" mentions (real grid incl. this SKU's siblings), not soft-404. Anchor "Tiempo Maestro range" (varied from Elite FG's "the Nike Tiempo Maestro lineup"), placed H2-3.
2. https://www.prosoccer.com/collections/nike-breakout-soccer-cleats - status 200, meta title "Nike Breakout Soccer Cleats & Shoes", 148 product links, this SKU's handle present in grid, not soft-404. Anchor "the Breakout pack", placed H2-3.
- Rejected: `/collections/turf-soccer-shoes` returned 200 but generic default title "Soccer Cleats, Apparel, Equipment & More" + zero product cards = soft-404 (caught by content-signal check per MEMORY link-validation-standard). Skipped; no turf-surface collection link.
- Placement: both in H2-3 (where prose authentically references both the tier lineup and the drop); contextual-fit rule governs count + validation, not fixed H2 position.

### Eligibility
Mike-verified in-stock at submission (Tier 2A). Live scrape shows "only 1 item left" + variant "sold out" tokens; storefront stock signals unreliable per 2026-05-29 codification, Mike's admin verification governs. Normal optimization, no strategic exception.

### Field-length checks
- Title: 56 chars (30-100). PASS.
- Meta Title input: 43 chars; +theme suffix ~55 (<60). PASS. No brand in field.
- Meta Description: 157 chars (<=160; 150-158 target). PASS.
- Short Description: ~62 words (50-100). PASS. No internal link. PASS.
- Description body: ~324 words (League/Club 280-340). PASS.
- URL handle: 64 chars (<=70). No change.

### Structure / casing
- Editorial body H2s, sentence case: "Soft leather, real touch, made for turf" / "Why FlyTouch leather feels broken in on day one" / "Who the Tiempo Maestro Academy turf shoe is for".
- Structural H2s, Title Case: "Product Details: Tiempo Maestro Academy Turf" / "Fit Notes" / "Care and Maintenance" / "FAQs about the Tiempo Maestro Academy Turf".
- Reading order: hook -> tech-build -> use case -> Product Details -> Fit Notes -> Care -> FAQ. Care H2 present (footwear trigger), bullets, after Fit Notes.

### Gates
- Voice check (`scripts/voice_check.py`): PASS (see session run).
- Gate 11 brand IP PASS. Gate 12 keyword distribution PASS. Gate 13 anti-stuffing PASS (no comma-stacked lists, no price in body, no brand-stacking). Gate 14 unsupported counts PASS. US-market language PASS ("shoes", no `boots`). Measurement units n/a (no fabricated temps/weights). adidas styling n/a in customer copy (Nike product). Internal link format PASS (full HTTPS www canonical).

### Cost this dispatch
Firecrawl 4 credits (PDP scrape + Tiempo Maestro silo + turf-shoes soft-404 check + Breakout pack). DataForSEO $0 (KIRA Phase 1 keywords pre-approved, no re-run). Tavily 0 (Tier 2A; scrape supplied all product facts).

### Image optimization flags (implementation-side, Misha/Mike)
- og:image emitted over `http://` not `https://` (`http://www.prosoccer.com/cdn/shop/...`); known theme-level issue across Nike PDPs, standing Misha audit item, not a copy fix.

## SKU KI0630 - adidas Copa Pure IV Pro Turf Soccer Shoes - Road To Glory Pack (SP26)

### Tier and word band
Tier 2A (pattern-follow PDP, follows KI0586 Elite exemplar STRUCTURE). Pro tier word band 340-390. Final body 389 words (excl. FAQ). Complexity: Complex (multi-tier / multi-surface / multi-colorway Copa Pure IV family).

### Eligibility
Mike-verified in-stock at submission, 2026-06-30 (Shopify admin). Live scrape shows "only 1 item left" plus variant "sold out" tokens; storefront stock signals unreliable per 2026-05-29 codification, Mike's admin verification governs. Normal optimization, no strategic exception.

### Phase 0 ground-truth (live scrape 2026-06-30, status 200, 1 credit) - scrape wins
- Price 129.99. Colorway "Solar Turbo / Ivory / Core Black" (scrape-confirmed, matches Elite exemplar and dispatch).
- Upper: "Fusionfeel 2.0" (scrape spec bullet and body). Touchprint forefoot texture. Floating tongue. adiPure pinline heel-to-toe.
- Outsole: rubber outsole for artificial turf ("a rubber outsole digs into artificial turf surfaces"). Ortholite anatomical sockliner / Formfit system. Regular fit. Laces.
- Weight: 281 g (UK 8.5) converted to US-first dual notation 9.9 oz (281g).
- Sibling colorways, same Pro Turf model: Core Black/Cloud White/Lucid Red (Immortal DNA), Zero Metalic/Core Black/Lucid Red (Born For Goals).

### Fabrication guard (scrape-data-wins) - traps caught
1. UPPER: dispatch hypothesis "Fusionskin (calfskin + synthetic mesh)" OVERRIDDEN by scrape, which says "Fusionfeel 2.0" (the synthetic upper). Wrote Fusionfeel 2.0 plus Touchprint texture; NO "calfskin" / "Fusionskin" / "kangaroo" / "K-leather" for this turf SKU. Aligns with silo guardrail (Fusionfeel = synthetic; calfskin/Fusionskin = FG Elite/Pro only). KJ6746-class behavior (material hypothesis overridden at SCRIBE level).
2. "leather": scrape literally reads "Fusionfeel 2.0 leather upper" (adidas marketing contradiction). Did NOT carry the bare word "leather" for the upper; Fusionfeel is synthetic.
3. PLATE: NO "Comfort Frame" and NO "Sprintframe" (forbidden) applied to turf. Described the actual rubber turf outsole only.
4. STUD COUNT: none claimed (turf rubber outsole, no studs).
5. SIGNATURE FACE: none asserted (Declan Rice current / Bernardo Silva historical both omitted); evergreen framing.
6. "Primeknit": the Born For Goals sibling map description claims "Primeknit construction"; this SKU's scrape shows a floating tongue (gen IV dropped the Primeknit tongue). Primeknit NOT claimed.
7. Internal-link soft-404: /collections/turf-soccer-shoes returned 200 but url/ogUrl resolved to homepage (og:title "Soccer Cleats"); silent redirect = soft-404. Rejected; used validated /collections/artificial-turf instead.

### Omitted specs (in scrape, intentionally not used)
- adidas marketing term `Football Boots` (US-market language; used "soccer shoes" / "turf shoes").
- Price 129.99 (Gate 13 pricing discipline; no dollar amounts in body).
- "for the court" adidas phrasing (translated to turf / small-sided, not quoted).
- Klarna financing, loyalty points, shipping, reviews(0), gift-box options (out of scope).

### Brand-IP classification
adidas product page, so the FIFA terminology family is PERMITTED. Not used (pack referenced by its own name "Road to Glory"; no "World Cup" in copy). Compliant either way. Gate 11 PASS.

### Keyword selection and distribution
- Primary adidas copa pure iv pro turf (sub-floor, GSC override per dispatch; no N/pos supplied, so Volume cell reads "sub-floor* (GSC override)", no fabricated number). Present in Title, Meta Title, Meta Description, Short Description, and body (H2-1 prose, Product Details H2, FAQ H2, Fit Notes = 5 exact occurrences; "Pro Turf" partials 8x total).
- Pack-specific secondary adidas copa pure road to glory (Mechanism C) = FIRST secondary row; woven once in H2-2 ("the adidas Copa Pure Road to Glory pack"). Single carve-out mention, exempt from Gate 12(d) count.
- Supporting secondaries (copa pure pro turf, adidas copa pure iv pro turf soccer shoes, copa pure iv pro turf) are substrings of the primary; the no-"adidas" variant "copa pure iv pro turf" appears naturally 3+ times (Fit Notes, Product Details H2, FAQ H2), satisfying Gate 12(d) via natural variation without a forced separate supporting (forcing distinct copies would be stuffing). Volumes/difficulty not supplied by KIRA, so table cells left blank, no fabrication.

### Cross-brief / silo differentiation
Lane: Copa TOUCH, Pro tier, TURF surface, small-sided / turf-regular (Tyler primary; Mike the Coach secondary). Distinct from:
- KI0586 Elite FG exemplar (playmaker / number-8-10, FG, calfskin). All forbidden phrasings avoided (hook, three H2 titles, "number 8/10", "settles like it was waiting", "look the part", Predator/F50 FAQ phrasing). Different H2 titles, hook, metaphor.
- KI0625 Pro FG sibling (same tier, FG natural grass, soft-calfskin touch). Differentiator = TURF surface plus Fusionfeel synthetic. Avoided its H2s ("First touch is where games turn" / "Where the soft touch comes from" / "Who reaches for the Pro") and its half-turn hook.
- KI0645 League Turf sibling (same surface, entry / value / parent framing). Differentiator = Pro tier / performance / Tyler. Avoided its "classic look" H2 and the kid/parent hook.
- KI0662 junior (parent / Jennifer). Differentiator = adult Pro / Tyler.

### Internal links (2, PDP internal-only, Description body only, validated 2026-06-30 with content signals)
1. https://www.prosoccer.com/collections/adidas-copa - status 200, url not redirected, og:title "adidas Copa Soccer Cleats | Classic Touch", 28 product cards, Copa Pure IV Pro Turf siblings present. Anchor "the full Copa lineup", placed heritage H2-2.
2. https://www.prosoccer.com/collections/artificial-turf - status 200, url not redirected, title "Turf Soccer Shoes & Cleats for Adults", 45 products / 42 turf, this SKU's Pro Turf siblings present. Anchor "turf soccer shoes", placed use-case H2-3.
- Rejected: /collections/turf-soccer-shoes (soft-404, redirects to homepage). Found canonical turf collection via firecrawl_map.
- Placement varies by contextual fit (heritage link in heritage H2, turf link in use-case H2), not a fixed-position template footprint.

### Structure / casing
- Editorial body H2s, sentence case: "Where the small-sided game gets decided" / "The Copa heritage, rebuilt for turf" / "For the player who lives on turf".
- Structural H2s, Title Case: "Product Details: Copa Pure IV Pro Turf" / "Fit Notes" / "Care and Maintenance" / "FAQs about the Copa Pure IV Pro Turf".
- Reading order: hook, heritage/tech-build, use case, Product Details, Fit Notes, Care, FAQ. Care H2 present (footwear trigger), bullets, after Fit Notes.

### Field-length checks
- Title: 62 chars (30-100). PASS.
- Meta Title input: 41 chars; plus theme suffix ~53 (under 60). PASS. No brand in field.
- Meta Description: 157 chars (160 max; 150-158 target). PASS.
- Short Description: 81 words (50-100). PASS. No internal link. PASS.
- Description body: 389 words (Pro band 340-390). PASS.
- URL handle: 65 chars (70 max). No change.

### FAQ net-new-value
4 Q&As, all net-new beyond body: surface / what-is-turf (required), true-to-size, "is the upper real leather" (answers the Fusionfeel-vs-calfskin question directly), and a fresh Copa/Predator/F50 small-sided lane question (not the Elite FAQ phrasing). H2 "FAQs about the Copa Pure IV Pro Turf"; each question H3; paragraph answers.

### Gates
- Voice check (scripts/voice_check.py): PASS (exit 0; no em/en-dashes, no forbidden words/openers, no capitalized Adidas, no UK "boots", no lowercase editorial body H2s).
- Gate 11 brand IP PASS. Gate 12 keyword distribution PASS (primary 5x in body, in band 4-7; supporting via natural variation; pack carve-out 1x). Gate 13 anti-stuffing PASS (no comma-stacked keyword lists, no dollar amounts in body, no brand-stacking). Gate 14 unsupported counts PASS. US-market language PASS ("shoes" / "turf shoes", no `boots`). Measurement units PASS (9.9 oz (281g) US-first dual notation). adidas styling PASS (lowercase throughout, including sentence starts). Internal-link format PASS (full HTTPS www canonical, Description body only).

### Cost this dispatch
Firecrawl 5 credits (PDP scrape, turf-soccer-shoes soft-404 check, adidas-copa validate, firecrawl_map turf collection, artificial-turf validate). DataForSEO 0 (KIRA Phase 1 keywords pre-approved, no re-run). Tavily 0 (Tier 2A; scrape supplied all product facts).

### Image optimization flags (implementation-side, Misha/Mike)
- og:image emitted over `http://` not `https://` (`http://www.prosoccer.com/cdn/shop/...`); known theme-level issue across PDPs, standing Misha audit item, not a copy fix.
