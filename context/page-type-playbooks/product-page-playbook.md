# Product Page Playbook

_Page-type playbook for any URL under `/products/*`. Read by SCRIBE on every product-page brief, ahead of the six copy-writing principles in `context/03-brand-voice.md`. The playbook governs subject matter (what the page is ABOUT). The six principles govern execution quality (HOW the copy reads). Subject first, then voice._

## Subject focus

A product page is ABOUT the specific product and the brand making it. The avatar landed here considering this purchase. Copy serves the avatar's hopes, anxieties, and identity for what owning this product will mean.

The product is the topic. The brand making it is part of the topic. ProSoccer the store is the venue, not the topic. The store's positioning surfaces on the homepage and on policy pages, not on a product page where the avatar is in active consideration of the purchase itself.

## Forbidden subjects on product pages

The following are out of scope for product-page body copy. A draft that includes them gets rewritten:

- ProSoccer the store. No retail-location call-outs in the body. Trust signals tied to the store (heritage, expertise) belong on the homepage and on category-level positioning copy, not in the product description.
- Generic warehouse and shipping logistics. "Same-day dispatch from Irwindale," "free shipping on orders over $X," "fitting room in Pasadena open until 8 pm." These belong in the cart and checkout flow, in the cart drawer, in the page chrome, in `/pages/shipping`. They do not belong in product-description body copy. (Exception: structured-data shipping fields VERITAS injects. Those are technical metadata, not body copy.)
- Cross-sells and competitive comparisons against other ProSoccer products. The Rebuy widget, the recommendations rail, and the related-products module own cross-sell. The product description does not say "compare to our other Predator models on the collection page." It commits to this product.
- Generic e-commerce platitudes. "The best soccer cleat," "shop now while supplies last," "you'll love this." These were forbidden by the rules in `context/03-brand-voice.md` anyway; flagging again because product copy tends to fall back on them.

## Required subjects on product pages

The following are in scope and the body copy must serve them:

- The product itself. Design, technology, materials, features. Every feature is translated to what it ENABLES for the avatar per `context/03-brand-voice.md` 'Emotional Connection Over Feature Selling'. Features support the feeling; they never lead.
- The brand. Signature elements, heritage, what distinguishes this brand from the alternatives the avatar is also considering. For an adidas Predator product page, the Predator-line context belongs here. For a Nike Mercurial Superfly page, the Mercurial heritage belongs here.
- The product's place in the catalog and lineup. The 2026 home kit, not just "a Mexico jersey." The Mercurial Superfly 9 Elite, not just "a Nike cleat." The avatar wants to know which version of the product this is and what they're getting that other versions don't have.
- The avatar's emotional context for ownership. What does wearing or using this product mean to the avatar? Carlos buying the 2026 El Tri home authentic feels something different from Tyler buying the same kit. Same product, different emotional anchor.
- Fit, sizing, and care information where relevant. Product copy is a place where avatar pain frames map directly to copy that closes the sale. Jennifer's "Wide Foot Nightmare" frame, Carlos's "is this real or fake" frame, Tyler's "will it actually run faster than my last pair" frame.

## Production workflow note (added 2026-05-29)

PDP production runs under ORIN's batch parallel dispatch + single daily batch commit pattern as of 2026-05-29. Mike submits up to a 10-URL batch (eligibility pre-vetted in Shopify admin); ORIN auto-classifies tier per URL; SCRIBE instances run in parallel; ORIN batch-commits all briefs as a single daily commit; single push; Mike reviews at end-of-batch. Per-brief Mike gate review and per-brief commit cycle are replaced; all quality discipline per brief stays intact. Full pattern: `context/workforce-conventions.md` 'Batch parallel dispatch + single daily batch commit'. ORIN procedural detail: `.claude/agents/master-strategist/agent.md` Section 9 'Batch parallel dispatch and single daily batch commit'.

## Tiered workflow architecture for PDP optimization (added 2026-05-28)

PDP brief production runs at one of three PDP-applicable tiers (Tier 2B is collection-only and lives in `context/page-type-playbooks/collection-page-playbook.md`). Tier is named at dispatch by ORIN; SCRIBE adapts scope accordingly. Quality discipline (voice check, 11 gates plus Gate 12 keyword distribution plus Gate 13 anti-stuffing plus Gate 14 unsupported specific counts, brand IP, year-specificity, eligibility verification, keyword distribution) preserved universally.

- **Tier 1 (Foundational PDP, ~25 to 35 min).** Dispatch when the PDP is the first in a new category for ProSoccer, when it will establish or refine a category-specific H2 template, or when it is a strategically critical hero product (highest-volume keyword target, flagship release, brand-narrative anchor). Full SCRIBE workflow: broad Tavily research across cultural / squad / tournament / kit-supplier / design dimensions; fresh brief build with template-refinement candidate analysis; all 14 gates surfaced (11 Section 11 gates plus Gate 12 keyword distribution plus Gate 13 anti-stuffing plus Gate 14 unsupported specific counts). Estimated 5 to 10% of PDP work.
- **Tier 2A (Pattern-follow PDP, ~12 to 16 min).** Dispatch when the PDP follows an established CANONICAL template (National Team Jersey four-time validated as of 2026-05-28, Club Jersey CANONICAL, Soccer Cleats VALIDATED v1) with no template-refining work expected. Scoped Tavily research: currency check only (squad / fixtures / manager / kit-supplier currency for the specific page), not broad cultural context (the template already encodes the cultural-context H2 pattern). Template-fill brief drafting: canonical structure with verified product-specific specifics swapped in, not fresh build from blank. Bulk of PDP work (~70 to 80%).
- **Tier 3 (Mike-drafted minimal, ~5 to 10 min).** Rare exception when Mike drafts 4 to 6 fields directly and ORIN runs lightweight QA (voice check + DFS keyword verify + brand IP compliance scan only). Requires explicit Mike request; NOT collection pages by default; NOT new categories without prior template work.

Cross-references: `context/workforce-conventions.md` 'Tiered workflow architecture (cross-cutting pattern)' (workforce-wide pattern + validation milestones), `.claude/agents/master-strategist/agent.md` Section 9 'Tier classification at candidate dispatch' (ORIN classification logic), `.claude/agents/on-page-seo/agent.md` Section 9 'Tiered workflow variants' (SCRIBE's per-tier scope adjustment).

## PDP-specific SEO discipline (added 2026-06-02)

Source: Mike's review of TinySEO's PDP analysis (2026-06-02), corrected against 2026 ecommerce SEO ranking data and ProSoccer's actual Shopify admin field structure. PDPs serve product-specific search intent (a buyer searching for one cleat in one tier), which differs from the category intent collection pages serve. That difference drives field-length constraints by field, cross-SKU title uniqueness, image and taxonomy requirements, and a body structure that splits reader-first prose from technical bullets. The nine disciplines below are PDP-only; they sit on top of the shared discipline (Gate 13 anti-stuffing, Gate 14 specific counts, the Phase 4 editorial disciplines, brand IP, year-specificity, keyword distribution) and govern Day 3+ PDP production. Day 2 batch #1 (collections) is not fix-forwarded.

### Reader-first operational principle (read this first)

This is the operational principle for ALL PDP copy, in Mike's words: "Write the copy to meet the needs and desires of our avatar first. Not Google algorithm. But also make sure the copy doesn't read like AI wrote it. Everything we talked about earlier: low cognitive load, value and emotion evoking, no feature selling for short or long description copy."

Concretely, on every PDP field:

- Write to the buyer's needs and desires, NOT to Google's algorithm. Ranking is the byproduct.
- No feature-selling in the Short Description or in the Description prose. Technical specs belong in the "Product Details" bullets, never in prose.
- Low cognitive load throughout (sentence-length variance, one concept per sentence, concrete over abstract, scan-able leads).
- Evoke positive emotion: belonging, identity, ritual, anticipation, heritage, place.
- Avoid manipulation patterns: scarcity, FOMO, status anxiety, hyperbole, false urgency.
- Copy must read as human-written, not AI-generated.

This is the editorial philosophy codified in commit dcfe6da (`context/workforce-conventions.md` 'Editorial philosophy (added 2026-06-02)'), applied as the governing principle for PDP drafting. The field-length and structure rules below serve this principle; they never override it.

### Field length constraints (hard limits, not targets)

ProSoccer's Hyper theme exposes three distinct description-related fields in Shopify admin, and they have different jobs and different lengths. "Short Description" and "Description" are NOT the same field:

| Field (ProSoccer admin name) | Renders | Length |
|---|---|---|
| Title | product title | 30 to 100 characters (min AND max) |
| Short Description (metafield) | hero block above Add to Cart | 50 to 100 words |
| Description (body_html) | collapsible accordion below the product images | tiered by product complexity (see below) |
| Meta Title | SERP title | 60 characters maximum, INCLUDING the Hyper theme brand suffix |
| Meta Description | SERP snippet | 160 characters maximum |
| URL handle (slug after `/products/`) | URL | 70 characters maximum |

Description (body_html) length tiers by product complexity:

- **Simple (~125 to 200 words):** single-use accessories and basic merchandise. Keychains, lapel pins, magnets, decals, stickers, mini balls, basic flags, simple practice cones.
- **Standard (~200 to 300 words):** single-tier products without pack/series complexity. Training and match balls, bags, backpacks, apparel with basic variants, shin guards, single-tier goalkeeper gloves.
- **Complex (~300 to 400 words):** multi-tier or multi-variant products that require buyer comparison. Soccer cleats (tier / plate / colorway / generation matrix), authentic jerseys (player versions, kit details), tournament-edition products with a collectibility narrative, technical goalkeeper gloves, anything that needs sizing / fit / surface guidance.

**Complexity classification test:** if a buyer needs more than 2 minutes to choose between sibling products in the same family, the product is complex. If they grab and go, it is simple.

FAIL if exceeded; SCRIBE revises. **Short Description** is a brief reader-first emotional / value-prop hook (no feature listing); live example from the Nike Superfly 11 Club PDP: "The Superfly 11 Club is designed for fast sprints. Its snug knit cuff helps keep you secure when running the field, while a lightweight plate helps keep you on your toes for bursts in open spaces." (44 words, slightly under the 50-word floor). **Meta Title budget:** the 60-char ceiling includes whatever the Hyper theme auto-appends (approximately 10 to 12 chars, " - ProSoccer" or similar). SCRIBE's Meta Title INPUT must therefore stay under approximately 48 to 50 characters. Never put "ProSoccer" in the field. **Meta Description:** 160 is the hard ceiling; the 150 to 158 desktop target sits within it. **Length architecture note:** the corrected ceilings are grounded in 2026 ecommerce ranking data (top-ranking ecommerce pages average 200 to 310 words; complex products are competitive at 300 to 400). The earlier single "150-word" figure is interpreted as the Short Description metafield, not the Description body. Mexico v5 (collection canonical, 340 words) supports the corrected range.

### Unique titles for pack/series products

Many cleats and footwear ship as a pack or series (e.g., Predator 26 in Elite / Pro / League / Club tiers, each possibly across FG / AG / SG plates). Product Title AND Meta Title must be UNIQUE across every SKU in the same pack or series, differentiated by the specific attribute that distinguishes that SKU from its siblings:

- Tier level (Elite, Pro, League, Club)
- Plate type (FG / AG / SG / MG / TF / IC / IN)
- Colorway name when official ("Hora Dorada", "Whiteout Pack", "Made in Japan")
- Generation or year when relevant (26, 6, IV)

Anti-pattern: all four tier SKUs titled "adidas Predator 26 Firm Ground Soccer Cleats" (no uniqueness, no signal of which tier the buyer is on); two colorways both titled "adidas F50 Elite FG Soccer Cleats". Correct: "adidas Predator 26 Elite Firm Ground Soccer Cleats", "adidas Predator 26 Pro Firm Ground Soccer Cleats", "adidas Predator 26 League Firm Ground Soccer Cleats", "adidas Predator 26 Club Firm Ground Soccer Cleats". When SCRIBE produces multiple PDPs from the same submitted batch, it cross-references all sibling titles for uniqueness in Phase 4; ORIN scans the batch for duplicate or near-duplicate titles across SKUs.

### URL handle constraint

The slug after `/products/` is 70 characters maximum. TOO LONG: `/products/adidas-predator-26-elite-firm-ground-soccer-cleats-mens-2026-world-cup-edition` (88 chars). WITHIN LIMIT: `/products/adidas-predator-26-elite-fg-soccer-cleats` (50 chars). SCRIBE includes a handle suggestion in the brief when it differs from the existing slug and verifies length. If the existing slug exceeds 70 chars and the page is high-traffic, SCRIBE flags it for Mike's review rather than auto-recommending a change, because a slug change requires 301 redirect coordination with Misha.

### Product image alt text

Every PDP product image needs descriptive alt text. Format: `[Brand] [product name] [colorway/edition if applicable] [view angle if specific] soccer cleats`. Examples: "adidas Predator 26 Elite Firm Ground soccer cleats" (primary), "adidas Predator 26 Elite Firm Ground side view" (side angle), "adidas Predator 26 Elite Firm Ground stud configuration" (sole view). Discipline: alt text describes what is in the image (not just the product name), includes the primary keyword naturally (soccer cleats, soccer shoes), is NOT keyword-stuffed (Gate 13 applies, no comma-stacking), and is distinct per image (differentiate by view angle or feature, never repeat the same alt text). SCRIBE includes alt text recommendations in the brief (one per primary product image; additional images noted where SCRIBE has gallery visibility).

### Product image optimization flags (workforce briefing only)

When the Firecrawl scrape reveals image issues, SCRIBE notes them in the workforce briefing audit trail, NOT in the visible brief (image optimization is implementation-side work for Mike and Misha, not editorial content): file dimensions clearly larger than display size (a 4000px image rendering at 800px), suboptimal format (PNG where JPG compresses better; non-WebP where WebP is available), or non-descriptive filenames (`DSC_1234.jpg` instead of `adidas-predator-26-elite.jpg`).

### Product taxonomy category

Every PDP needs a Shopify taxonomy category. For ProSoccer footwear: `Apparel & Accessories > Shoes > Athletic Shoes > Soccer Cleats` (firm / multi / soft ground), `... > Indoor Court Shoes` (indoor), `... > Turf Shoes` (turf). SCRIBE recommends the category in the workforce briefing audit trail; Mike applies it in Shopify admin during implementation (taxonomy is admin-side, not theme content). If the current PDP is missing a taxonomy category, SCRIBE flags it in the workforce briefing as an implementation-side action item.

### Description structure: prose H2 sections + a dedicated "Product Details" bullet H2

The Description (body_html) splits reader-first prose from technical bullets. Prose carries the WHY (why this matters to the buyer); bullets carry the WHAT (the specs). Prose readers get prose; scanner readers get bullets. The cognitive load discipline applies throughout.

**Prose H2 sections (reader-first body copy):** product overview / introduction (emotional or identity hook), use-case scenarios (how players actually use this), identity and belonging anchors (what the section wears, who this is for), heritage and brand narrative, sizing and fit guidance framed by buyer need.

**Dedicated "Product Details" H2 (bullet list).** Use this exact term, "Product Details" -- it matches the pattern ProSoccer already uses on live PDPs (e.g., the Nike Superfly 11 Club PDP). It lives as its own H2 within the Description, 5 to 8 bullets typical, one technical attribute per bullet. Always include it when the product has technical specs worth listing.

- **Bullets (specs, the WHAT):** materials (upper, stud configuration, lining, sole construction), plate type and surface compatibility (FG / AG / SG / MG / TF / IC), tier-specific features (Elite vs Pro vs League differentiation), weight, sizing system, fit notes, care instructions, technology callouts (Heat.RDY, K-leather, traction system, lacing).
- **Prose (the WHY):** why this matters to the buyer's life, emotional and identity anchors, use-case scenarios, heritage and brand context, sizing guidance framed by buyer need. No feature-selling in prose; specs live in the bullets.

**H2 count, flexible by complexity (SCRIBE decides at brief production):** Simple 2 to 3 H2 sections (overview + Product Details + optional fit); Standard 3 to 4; Complex 4 to 5 (overview + use case + heritage + Product Details + fit / sizing). Each prose paragraph carries one theme, 2 to 4 sentences, with white space for scan-ability. Anti-pattern: technical specs listed in prose sentences instead of the Product Details bullets, or a single undifferentiated block.

### FAQ for PDPs (recommended, net-new-value criterion)

FAQ is RECOMMENDED on PDPs (collection pages keep the conditional rule in `context/page-type-playbooks/collection-page-playbook.md`). The same net-new-value criterion governs both: a FAQ Q-and-A pair earns its place only when it answers a question the description body does not already cover, that real buyers actually ask, and that adds measurable value to the decision. Typical PDP patterns: sizing ("Does the Predator 26 run true to size?"), plate selection ("Should I get the FG or MG plate for mixed surfaces?"), sibling comparison ("What's the difference between Elite and Pro tiers?"), use-case fit ("Are these cleats good for hard ground?"), care or durability ("How do I care for K-leather uppers?"). Skip: questions already answered in the body, marketing fluff as questions ("Why are these the best cleats?"), generic non-product questions ("Where do you ship?"), and schema-stuffing questions. Count: 3 to 5 Q-and-A pairs typical, quality over quantity. Skip FAQ entirely if SCRIBE cannot generate 3 genuinely useful Q-and-As beyond the body.

### Tier time impact

Applying the full PDP discipline (complexity classification, length verification across the six fields, cross-SKU uniqueness checks, prose-vs-bullet Description structure with the Product Details H2, alt text, taxonomy, FAQ net-new-value judgment) adds roughly 3 to 5 minutes to a Tier 2A PDP, shifting the estimate from ~12 to 16 min toward ~15 to 20 min. Tier 1 foundational PDPs already budget for full discipline.

Cross-references: `.claude/agents/on-page-seo/agent.md` Section 9 (PDP Phase 4 self-checks), `.claude/agents/master-strategist/agent.md` Section 9 + Section 11 (ORIN PDP defense-in-depth), `context/workforce-conventions.md` 'PDP optimization discipline (cross-cutting)' (field-length reference table + FAQ reconciliation + architectural learning note).

## Eligibility verification (Mike-pre-vetted at URL submission, updated 2026-05-29)

_Original codification 2026-05-27 placed eligibility detection in the agent layer via Firecrawl scrape. 2026-05-29 diagnostic on the Mexico Stadium SS kit set confirmed storefront-rendered signals (schema.org availability, Add-to-cart button state, variant selector) are systematically unreliable: three different schema.org value formats across three pages of the same theme, dual-schema injection from apps, persistent variant selector lies on Home and Third (in-stock per Shopify admin, sold-out per storefront render). The "Available in stock (X)" inventory hint was the only reliable signal and had been dismissed as a JSON-extraction artifact. Rather than refine detection rules against an architecturally unreliable rendering layer, eligibility responsibility moves to the human-in-the-loop layer._

### Eligibility responsibility: Mike at URL submission

Mike verifies eligibility in Shopify admin (inventory adjustment history, product visibility settings, sales channel status, sitemap presence) before submitting a URL to ORIN or SCRIBE for optimization. URLs supplied by Mike are assumed eligible for normal optimization unless Mike explicitly flags a strategic exception. Agents skip Firecrawl-based eligibility detection.

Brief audit trail captures eligibility status verbatim in the strategic context section (or equivalent):

- Normal eligible: "Mike-verified in-stock at submission, [YYYY-MM-DD] (Shopify admin)."
- Strategic exception applied: "Mike-flagged [exception type] at submission, [YYYY-MM-DD]: [reasoning]."

### Strategic exception: closing-window optimization

_Trigger updated 2026-05-29: applies when Mike explicitly flags closing-window at URL submission, not when an agent auto-detects sold-out._

Closing-window narrative (older generations, closeout inventory, end-of-cycle kits) is a valid strategic exception for sold-out PDPs IF:

- The page has retained value for collectors, completists, or loyalists (e.g., a championship-winning kit, a signature cleat generation, a final season under a kit supplier)
- SEO equity from optimization persists for any restock potential, organic ranking benefit, or topical authority that flows to sibling pages
- Mike makes the strategic call explicitly at URL submission; the override is documented in the brief production decision

Documented examples of the exception (both 2026-05-26 production, predating the codification):

- Liverpool 2024-25 Nike Away Jersey v2 (commit b7159dc): sold out, optimized intentionally per closing-window framing on the Nike-to-adidas brand transition.
- adidas Predator Accuracy.1 FG Crazyrush Pack v2 (commit d52e56f): sold out, optimized intentionally per closing-window framing on the two-generation gap to the Predator 26.

### Strategic exception: pre-tournament demand spike optimization

_Trigger updated 2026-05-29: applies when Mike explicitly flags pre-tournament demand spike at URL submission, not when an agent auto-detects sold-out current-cycle inventory. The Mexico Stadium SS kit set application (2026-05-28) was triggered by false-positive eligibility detection and has been stripped from those briefs in a fix-forward commit; the exception type itself remains conceptually valid for legitimate future Mike-flagged cases._

Pre-tournament demand spike is a valid strategic exception for sold-out current-cycle PDPs IF:

- Product is current-cycle inventory (not end-of-life, not closeout). This is what distinguishes the exception from closing-window.
- A major tournament or seasonal demand event is imminent (typically within 30 to 60 days). Examples: World Cup, Euros, Copa América, AFCON, Champions League final, major club season opener, major league cup final.
- Restock is expected during or after the demand event window. Manufacturer typically restocks current-cycle inventory for tournament periods; pre-tournament sold-out is usually demand-driven inventory turnover, not discontinuation.
- SEO equity lead time matters. Optimizing now means rankings improve before traffic peaks at the demand event; sold-out copy that ranks at tournament kickoff captures the demand surge.
- Page must include strong internal linking to the relevant collection page so customers landing on a sold-out PDP can navigate to in-stock alternates (different tier, sleeve length, women's, youth, kids). The collection-page internal link is load-bearing for this exception; without it, the sold-out PDP is a dead end for the buyer.

Override requires Mike's explicit flag at URL submission with the strategic reasoning logged.

### Decision logic for strategic exceptions

Sold-out PDP flagged by Mike at URL submission, check exception type:

1. **End-of-life, closeout, or discontinued generation** with retained collector or completist value, restock not expected: closing-window exception. Examples: Liverpool 2024-25 Nike Away Jersey v2 (b7159dc), adidas Predator Accuracy.1 FG Crazyrush Pack v2 (d52e56f).
2. **Current-cycle inventory** with imminent tournament or seasonal demand event (typically 60 days or less), restock expected: pre-tournament demand spike exception.
3. **Neither applies, and Mike still wants the page optimized**: Mike documents the reasoning; ORIN proceeds; brief audit trail captures the reasoning.

Each exception override requires explicit strategic reasoning documented in the brief production decision. The decision is Mike's; agents document, they do not classify.

### Cross-references

- ORIN candidate-handling workflow: `.claude/agents/master-strategist/agent.md` Section 9 'Candidate eligibility verification at Phase 1 surfacing'.
- SCRIBE pre-Phase-1 audit-trail step: `.claude/agents/on-page-seo/agent.md` Section 2 Step 0.5 'Eligibility verification audit trail (Mike-pre-vetted)'.
- Workforce convention + architectural learning: `context/workforce-conventions.md` 'Eligibility verification (Mike-pre-vetted at URL submission)'.

### Strategic exception: closing-window optimization

Closing-window narrative (older generations, closeout inventory, end-of-cycle kits) is a valid optimization strategy on sold-out PDPs IF:

- The page has retained value for collectors, completists, or loyalists (e.g., a championship-winning kit, a signature cleat generation, a final season under a kit supplier)
- SEO equity from optimization persists for any restock potential, organic ranking benefit, or topical authority that flows to sibling pages
- Mike makes the strategic call explicitly in the candidate decision; the override is documented in the brief production decision

Default behavior: SKIP sold-out PDPs. Override requires explicit strategic reasoning documented in the brief production decision.

Documented examples of the exception (both 2026-05-26 production, predating the eligibility codification):

- Liverpool 2024-25 Nike Away Jersey v2 (commit b7159dc): sold out, optimized intentionally per closing-window framing on the Nike-to-adidas brand transition.
- adidas Predator Accuracy.1 FG Crazyrush Pack v2 (commit d52e56f): sold out, optimized intentionally per closing-window framing on the two-generation gap to the Predator 26.

New optimizations going forward default to in-stock candidates; closing-window overrides require explicit strategic reasoning.

### Strategic exception: pre-tournament demand spike optimization

_Added 2026-05-28 from production-reality reality check. Mexico 2026 kit set Stadium SS Home/Away/Third all sold out on Day 1 of 10/day rhythm with the 2026 World Cup opener about 14 days away; structurally a different exception type than closing-window._

Pre-tournament demand spike is a valid strategic exception for sold-out current-cycle PDPs IF:

- Product is current-cycle inventory (not end-of-life, not closeout). This is what distinguishes the exception from closing-window.
- A major tournament or seasonal demand event is imminent (typically within 30 to 60 days). Examples: World Cup, Euros, Copa América, AFCON, Champions League final, major club season opener, major league cup final.
- Restock is expected during or after the demand event window. Manufacturer typically restocks current-cycle inventory for tournament periods; pre-tournament sold-out is usually demand-driven inventory turnover, not discontinuation.
- SEO equity lead time matters. Optimizing now means rankings improve before traffic peaks at the demand event; sold-out copy that ranks at tournament kickoff captures the demand surge.
- Page must include strong internal linking to the relevant collection page so customers landing on a sold-out PDP can navigate to in-stock alternates (different tier, sleeve length, women's, youth, kids). The collection-page internal link is load-bearing for this exception; without it, the sold-out PDP is a dead end for the buyer.

Default behavior: SKIP sold-out current-cycle PDPs unless the criteria above are met. Override requires explicit strategic reasoning documented in the brief production decision.

Documented example: Mexico 2026 kit set (Home `/products/adidas-2026-mexico-mens-stadium-home-soccer-jersey`, Away `/products/adidas-2026-mexico-mens-stadium-away-soccer-jersey`, Third `/products/adidas-2026-mexico-mens-stadium-third-soccer-jersey`), all Stadium SS, all sold out on 2026-05-28 with 2026 World Cup opener June 11 (about 14 days out). Mexico is co-host with automatic qualification (no qualifying campaign required). Optimized under pre-tournament demand spike exception with `/collections/mexico` internal link strategy to capture buyers needing in-stock alternates (Authentic SS, Stadium LS, Authentic LS, Women's Stadium, Youth Stadium, GK Stadium). First documented pre-tournament demand spike override; codified with this same commit.

### Decision logic for strategic exceptions

Sold-out PDP detected at eligibility verification, check exception type:

1. **End-of-life, closeout, or discontinued generation** with retained collector or completist value, restock not expected: closing-window exception. Examples: Liverpool 2024-25 Nike Away Jersey v2 (b7159dc), adidas Predator Accuracy.1 FG Crazyrush Pack v2 (d52e56f).
2. **Current-cycle inventory** with imminent tournament or seasonal demand event (typically 60 days or less), restock expected: pre-tournament demand spike exception. Example: Mexico 2026 kit set on 2026-05-28 with WC opener June 11.
3. **Neither applies**: DEFAULT BLOCKER. Skip the PDP, or swap to an alternate variant (different tier, sleeve length, women's, youth) that is in stock.

Each exception override requires explicit strategic reasoning documented in the brief production decision. The decision is Mike's, not SCRIBE's or ORIN's; the agents surface the exception type as a recommendation, Mike approves or redirects.

### Cross-references

- ORIN candidate-selection workflow: `.claude/agents/master-strategist/agent.md` Section 9 'Candidate eligibility verification at Phase 1 surfacing'.
- SCRIBE pre-Phase-1 gate: `.claude/agents/on-page-seo/agent.md` Section 2 Step 0.5 'Eligibility verification'.
- Workforce convention: `context/workforce-conventions.md` 'Eligibility verification as logical extension of Step 0'.

## Primary keyword selection for year/generation/season-bound products

_Added 2026-05-27 from architectural refinement surfaced during client presentation prep. Applies to any product whose identity is bound to a specific year, generation, or season. Precedes the Five canonical brief-craft rules below because primary keyword selection sits upstream of brief construction._

Many products in the ProSoccer catalog are bound to a specific year, generation, or season. National team jerseys cycle on tournament rhythm (2024-25, 2025-26, 2026 World Cup). Club jerseys cycle on club season. Cleats cycle on brand generation (Predator 22, Predator Accuracy, Predator 24, Predator 26). Training apparel and goalkeeper jerseys often carry season tags. For all of these, primary keyword selection requires specificity match between the keyword and the specific product year or generation, not the highest-volume keyword in the broader category.

**The failure mode this rule prevents:** optimizing a 2024-25 Liverpool away jersey for `liverpool away jersey` (generic category-level term, 590/mo) and watching Google rank the current-cycle adidas 25/26 away product above it because SERP dynamics for unbound queries favor current-cycle relevance. The 2024-25 page can never win an unbound search in 2026; it can win bound searches for `liverpool 2024-25 away jersey`.

**Selection hierarchy for year/generation/season-bound products:**

1. **Primary keyword: year-specific or generation-specific exact-match.** Lower absolute volume, but the intent match is precise and the ranking target is realistic. Examples: `liverpool 2024-25 away jersey`, `predator 24 elite fg`, `mexico 2026 world cup jersey`, `nike goalkeeper jersey 2025-26`. The page can plausibly rank top 10 for these terms because the SERP is narrower and the page's specificity matches the searcher's specificity.
2. **Supporting keywords: generic category-level terms.** Higher volume, broader topical relevance, but NOT the ranking target. Examples: `liverpool away jersey`, `predator soccer cleats`, `mexico soccer jersey`. These earn natural mention in the body for topical depth and may pick up incidental long-tail traffic, but the page should not be structured to rank against current-cycle competitors for these terms.
3. **Long-tail modifiers for older products:** emotional, collector, or closing-window variants. Examples: `liverpool 2024-25 away jersey nike farewell`, `predator accuracy crazyrush pack closeout`, `mexico 2022 world cup jersey vintage`. These capture buyer intent specific to the older product's market position (collector, closeout, throwback cycle) where the year-specific term alone doesn't fully signal.

**Realistic ranking position assessment.** Before settling primary keyword, run a DataForSEO SERP check on both the year-specific exact-match candidate and the generic category-level candidate. If the generic-term SERP is dominated by current-cycle brand and retailer pages and the year-specific SERP has open positions (or weaker competition), the year-specific term is the correct primary keyword regardless of volume. Volume without realistic ranking is wasted optimization budget.

**Categories affected:**

- National team jerseys (year/tournament-cycle-specific)
- Club jerseys (season-specific)
- Cleats with generation versioning (Predator 22, Accuracy, 24, 26; Mercurial 9, 10; Phantom GX, GX 2; Tiempo generation cycles)
- Training apparel with season tags
- Goalkeeper jerseys with season tags

**Categories NOT affected.** Year-agnostic products use the standard category-level keyword selection (head keyword = highest-volume relevant term). Examples: scarves, training balls without year tags, generic shin guards, casual lifestyle apparel without season anchors.

**Reference for SCRIBE operational use.** Selection guidance summary lives in `.claude/agents/on-page-seo/agent.md` Section 9 'Year/generation/season specificity for primary keyword selection'.

## Keyword distribution discipline (added 2026-05-28, codifies Refinement 4)

Keyword SELECTION ('Primary keyword selection for year/generation/season-bound products' section above) addresses which keyword becomes primary. Keyword DEPLOYMENT addresses how the chosen primary propagates through the brief's six fields plus the Long Description body.

**Primary keyword placement (mandatory across all required fields):**

- **Title / H1:** exact match or close natural variant.
- **Meta Title:** exact match in field; under 60 chars accounting for Hyper theme auto-append of " - ProSoccer" suffix (codified 2026-05-28, theme verified to append across all page types); NEVER include "ProSoccer" or any brand variant in the Meta Title field itself.
- **Meta Description:** exact match or natural variant early in description (within first 100 chars where Google bolds the match).
- **Short Description:** exact match or natural variant in first sentence.
- **Slug:** exact match if creating new; preserve existing slug if optimizing existing page unless clearly suboptimal (slug changes trigger redirect-cost risk).
- **Long Description:** primary keyword in 2 to 3 H2 headings plus naturally in body copy 4 to 7 times.

**Supporting keyword placement (one supporting keyword, updated 2026-06-02).** SCRIBE selects ONE supporting keyword for body-copy use, not several. Selection criterion: the highest search volume among the supporting candidates from the Phase 2 keyword research. That single supporting keyword is woven naturally into the Short Description (1 to 2 mentions) and the Long Description body copy (3 to 5 mentions), and may take at least one H2 heading if it fits naturally. NOT in Meta Title (crowded with primary); NOT in Slug (URL stays clean). The other supporting candidates stay in the workforce briefing keyword-research record as the audit trail but are NOT deployed in body copy. Rationale: one supporting keyword at depth (3 to 5 body mentions) ranks better than three supporting keywords at shallow density (1 mention each), and copy reads as reader-focused rather than keyword-targeted. See 'Supporting keyword selection (added 2026-06-02)' below for the full rule, exception, and audit-trail requirement.

**Long-tail modifier placement (optional):** body copy of Long Description especially in cultural-context H2 (typically H2 4 for jerseys, H2 5 for cleats); internal link anchor text where the modifier reads naturally as the link's anchor.

**Forbidden: keyword stuffing.** Specifically:

- Repeating primary keyword more than 7 times in Long Description OR more than 1% of total word count, whichever is lower.
- Forcing primary keyword into headings where it doesn't fit naturally.
- Repeating primary keyword in consecutive sentences without natural variation.
- Using primary keyword as anchor text for more than 1 internal link per brief.

**Natural variation allowed.** Primary keyword variations count toward placement. Example for `mexico 2026 home jersey`: "Mexico 2026 home jersey" (exact), "Mexico home kit 2026" (reordered), "this 2026 home jersey" (natural variant), "this home kit" (contextual reference). Variations valid as long as semantic intent is clear from surrounding context.

**Verification:** SCRIBE Gate 12 (Section 11) checks (a) primary keyword presence across all required fields, (b) primary keyword count in Long Description within 4 to 7 range, (c) no keyword stuffing detected, (d) ONE supporting keyword present at 3 to 5 mentions in body copy (not multiple supporting keywords each at lower density) per the supporting keyword selection rule below. Failures surface as BLOCKER and refine before commit.

## Supporting keyword selection (added 2026-06-02)

SCRIBE selects ONE supporting keyword for body-copy use. The selection criterion is the highest search volume among the supporting keyword candidates from Phase 2 keyword research.

**Anti-pattern (prior behavior).** SCRIBE included multiple supporting keywords throughout the Short and Long Descriptions, treating each as a coverage opportunity. The result reads as keyword-targeted rather than reader-focused and dilutes the ranking signal for any single supporting term. Surfaced across multiple Day 2 batch #1 briefs (2026-06-02).

**The rule (Phase 2 to Phase 4 flow):**

1. Phase 2: SCRIBE produces full keyword research as today (primary plus supporting candidates with volume, KD, trends).
2. Phase 4: SCRIBE picks ONE supporting keyword, the highest-search-volume candidate from the supporting set.
3. Phase 4: that single supporting keyword is woven naturally into the Short Description (1 to 2 mentions) and the Long Description body copy (3 to 5 mentions).
4. The other supporting candidates remain in the workforce-briefing keyword-research record (audit trail) but are NOT used in body copy.
5. Primary keyword usage follows the existing Gate 12 keyword distribution rules unchanged.

**Exception (two clear winners).** If two supporting keywords have search volumes within 10% of each other AND are semantically distinct (not synonyms), SCRIBE may include the second one minimally (1 to 2 body mentions, not 3 to 5). This is the rare case where two clear winners exist among the supporting candidates.

**Workforce briefing audit trail.** SCRIBE documents: the full supporting candidate list with volumes, the selected supporting keyword plus selection rationale (highest volume), and where the selected keyword appears in the Short Description and Long Description.

Cross-references: `.claude/agents/on-page-seo/agent.md` Section 9 'Keyword distribution discipline' (operational summary + Gate 12 definition + supporting keyword selection), `context/page-type-playbooks/collection-page-playbook.md` 'Keyword distribution discipline' (collection 6-field adapted version), `context/workforce-conventions.md` 'Supporting keyword selection (cross-cutting)'.

## Anti-stuffing discipline (Gate 13, added 2026-06-02)

Keyword distribution discipline (the section above) governs how the primary keyword propagates through fields and caps repetition. Anti-stuffing discipline is a separate concern: it governs the STRUCTURE of any single field so that no field reads as a comma-stacked keyword list. The two are distinct. Gate 12 catches over-repetition of the same keyword; Gate 13 catches list-shaped fields that pack many adjacent keywords into one string. Gate 13 sits after Gate 12 in the gates suite (the suite runs 13 gates as of 2026-06-02). It is also distinct from the Gate 1 voice check, which governs prose voice and forbidden characters; Gate 13 governs structural keyword-stuffing patterns. Distinct concerns, distinct gates.

The quality issue that surfaced this gate: a Title field reading `National Team Soccer Accessories: Scarves, Hats, Bags, Flags & Balls` (Day 2 batch #1 URL #2, flagged during Mike's Shopify admin implementation 2026-06-02). A comma-stacked keyword list reads as keyword stuffing to Google quality systems (Helpful Content Update, Spam Updates) regardless of whether each item is technically relevant to the page, and it degrades user CTR in the SERP even at the same rank position.

**Core principle: product category breadth belongs in the body H2 framework and Long Description body copy, not in the Title or Meta Title fields.** Each output field should read as natural language a human would actually write. Breadth across product categories is expressed through the body's H2 sections and the narrative, not by listing categories in a title-level field.

### Anti-patterns to flag (any field)

1. **Comma-stacked keyword lists.** The format `[Topic]: keyword1, keyword2, keyword3 & keyword4` or `[Topic] - A, B, C, D` reads as stuffing regardless of relevance. Any field carrying 3+ comma-separated keywords fails.
2. **Ampersand-terminated lists.** A trailing `& [final keyword]` at the end of a comma list compounds the spam signal.
3. **Synonym stacking.** Treating synonyms (jerseys / shirts / kits / tops; cleats / `boots` / shoes) as variations to stack rather than picking one canonical term per field.
4. **Modifier stacking.** Stacking audience modifiers (Men's / Boys' / Youth / Kids') or product modifiers (Authentic / Replica / Stadium / Match-Worn) in a single field.
5. **Brand stacking (titles).** Listing multiple brands (adidas, Nike, Puma) in a title when only one or two are relevant to the page.
6. **Price stacking (body copy).** Specific dollar amounts in product-page body copy (added 2026-06-02). Prices decay; they belong in the PDP variant selector, product cards, and schema, not the body prose.
7. **Brand stacking (body sentences).** Three or more comma-separated brand names in a single sentence within the Body / Long Description (added 2026-06-02). The body-copy extension of anti-pattern 5; brand breadth belongs in product cards and faceted filters, not body prose.

### Stuffed vs natural

- STUFFED: `National Team Soccer Accessories: Scarves, Hats, Bags, Flags & Balls` -> NATURAL: `National Team Soccer Accessories` OR `2026 National Team Soccer Accessories`
- STUFFED: `Soccer Jerseys, Football Shirts, Kits & Tops` -> NATURAL: `Soccer Jerseys` OR `2026 National Team Soccer Jerseys`
- STUFFED: `Men's Boys' Youth Soccer Cleats` -> NATURAL: `Soccer Cleats` (audience breadth covered in body copy)

### Pricing discipline (body copy, added 2026-06-02)

Body copy on a product page must not contain specific dollar amounts. Use tier and positioning language instead. This is part of the broader content evergreen-ness principle (`context/workforce-conventions.md` 'Content evergreen-ness'): prices decay fast (sales, retail adjustments, discontinuations), stale prices in body copy create user trust issues (body says $34.99, the PDP shows $39.99), prices carry no SEO ranking benefit for category-intent queries, and every price change otherwise ripples into a body-copy edit. Pricing belongs in the PDP variant selector, product cards, and Product schema, where Shopify auto-maintains accuracy.

Stuffed vs natural:

- STUFFED: "Caps run around $34.99 across Mexico, Germany, Spain." -> NATURAL: "Caps span the federation roster from everyday snapbacks to premium fitted silhouettes."
- STUFFED: "Scarves run $24 to $44. Flags run $44.99; country flags run $19.99." -> NATURAL: "Scarves scale from match-day basics to collector-grade weaves; flags range from desk-size to wall-size."
- STUFFED: "Bags land between $30 and $80 across adidas, Nike, and Puma." -> NATURAL: "Bags scale from compact gym carry to full match-day kit haulers."

Natural alternatives: tier and positioning language ("entry-level", "mid-tier", "premium", "collector"); comparative language ("scales from compact to wall-size", "ranges from everyday to match-day"); category breadth without specific numbers.

### Brand mention discipline (body copy, added 2026-06-02)

A body sentence must not carry 3+ comma-separated brand names. Stacked brand names read as brand keyword surfacing, not editorial narrative; brand breadth belongs in product cards and faceted filters. Individual brand mentions are fine when the narrative justifies the brand's role: one or two brands per sentence at most, each with role-specific context.

Stuffed vs natural:

- STUFFED: "adidas, Nike, Puma, Wincraft, Mimi Imports, Logo Brands, and Fan Ink each carry federation-licensed pieces." -> NATURAL: "Federation-licensed pieces come from category leaders across apparel, accessories, and collectibles."
- NATURAL (narratively justified single/dual mention): "adidas covers cap silhouettes across the federation roster; Wincraft owns the wall-flag category."

### Gate 13 check criteria (per brief, across all output fields)

Fields in scope: Title, Meta Title, Meta Description, Short Description, Body / Long Description (including H2s and H3s), internal link anchor text, FAQ questions and answers when included.

- No field contains a comma-stacked keyword list (3+ comma-separated keywords).
- No field contains an ampersand-terminated keyword list.
- No field stacks synonyms of the same concept (pick one canonical term per field).
- No field stacks modifiers redundantly.
- No title field stacks brands where only one or two are relevant.
- NEW (2026-06-02): No specific dollar amounts in product body copy (use tier / positioning language).
- NEW (2026-06-02): No body sentence carries 3+ comma-separated brand names (brand mentions require narrative justification, one or two per sentence max).
- Each field reads as natural human-written prose.

FAIL = revise the field; PASS = the field clears. SCRIBE self-revises any failing field during Phase 4 (brief drafting) before the Phase 5 voice check. ORIN re-checks at the orchestrator layer as defense-in-depth.

Cross-references: `.claude/agents/on-page-seo/agent.md` Section 11 Gate 13 (SCRIBE self-check) and Section 9 'Anti-stuffing discipline', `.claude/agents/master-strategist/agent.md` Section 9 (ORIN defense-in-depth re-check), `context/workforce-conventions.md` 'Anti-stuffing discipline (Gate 13, cross-cutting)' + 'Content evergreen-ness' + 'Brand styling conventions'. Pricing discipline, body brand-mention discipline, and adidas brand styling (`context/workforce-conventions.md` 'Brand styling conventions': adidas is always lowercase, even at sentence start) are complementary disciplines all surfaced from the same Day 2 batch #1 review (2026-06-02).

## Unsupported specific counts (Gate 14, added 2026-06-02)

Gate 14 sits after Gate 13 in the gates suite (the suite runs 14 gates as of 2026-06-02). It is the same ephemeral-data family as Gate 13's pricing discipline: body copy must not contain specific counts of catalog items (federations, brands, products, styles, designs, tiers) that are unverified, decay as inventory shifts, or read as SEO ornamentation.

The issue that surfaced this gate: a Short Description reading "Ten federations, four brands, one piece of fan kit... the soccer scarf" (Day 2 batch #1 URL #3, flagged 2026-06-02). Counts like these are usually estimated by SCRIBE from scrape data rather than an authoritative source; they decay as the Shopify catalog changes (products discontinue, new SKUs add); they read as SEO ornamentation when not narratively justified; and they force the reader to either accept or audit the number.

### Anti-pattern examples

- "Ten federations, four brands, one piece of fan kit..."
- "Six bag styles across the adidas roster"
- "Twelve scarf designs span the federation lineup"
- "Three cleat tiers cover every skill level"

### Natural alternatives

- Positioning language: "the full federation roster", "the complete cleat lineup".
- Comparative language: "category leaders across multiple brands", "a deep selection".
- Specific examples without counts: "Argentina, Mexico, USMNT, and more".
- "across" / "spanning" / "from X to Y" framing.

### Exception (verified counts permitted)

Counts are allowed when sourced from a verified authoritative reference and noted in the workforce briefing:

- Tournament structure (e.g., "the 48-team 2026 World Cup expansion") from a public canonical source.
- Year or cycle references ("the 2026 cycle", "the 1986 World Cup") -- temporal, not inventory.
- Product-specific verified specs ("the soft-ground cleat's stud configuration") -- physical product attribute.

### Gate 14 check criteria

Body copy must not contain specific counts of catalog items (federations, brands, products, styles, designs, tiers, and similar) unless the count is sourced from a verified authoritative reference and noted in the workforce briefing. SCRIBE self-revises during Phase 4 (brief drafting) before the Phase 5 voice check; ORIN re-checks at the orchestrator layer as a sanity scan.

Cross-references: `.claude/agents/on-page-seo/agent.md` Section 11 Gate 14 + Section 9, `.claude/agents/master-strategist/agent.md` Section 9 + Section 11, `context/workforce-conventions.md` 'Unsupported specific counts (Gate 14, cross-cutting)'.

## Image precision discipline (SCRIBE Phase 4 self-check, added 2026-06-02)

A writing-quality discipline distinct from the structural gates. Every evocative sentence in body copy must pass the "what's the actual image?" test. For any sentence describing physical action, ritual, or sensory experience, SCRIBE asks: can I picture the specific physical motion? Is the temporal sequence clear (when, for how long)? Are the cause-and-effect relationships logically connected? If any of these fail, SCRIBE revises the sentence in Phase 4 before the Phase 5 voice check.

The issue that surfaced this discipline: a Short Description reading "It goes up over your head when the anthem starts and doesn't come off 'till the crowd finds its voice" (Day 2 batch #1 URL #3). "Goes up over your head" is unclear (over the head like a hood, or raised overhead with arms extended?); "'till the crowd finds its voice" is temporally vague.

Muddy vs sharper:

- MUDDY: "It goes up over your head when the anthem starts and doesn't come off 'till the crowd finds its voice." SHARPER: "Raised overhead during the national anthem and held high through the opening chants." (specific physical action, specific temporal sequence, clear cause-and-effect.)
- MUDDY: "The kit pulses with national pride that washes over the stadium." SHARPER: "The kit carries colors that fans recognize across the stadium and chants that travel from end to end." (specific sensory anchors, specific spatial reference.)

Apply field by field: Short Description (highest density of evocative copy), Long Description body prose, and H2 / H3 framing where evocative. ORIN re-checks at the orchestrator layer as a sanity scan (flag obvious muddy imagery for SCRIBE revision; this is a judgment call, not a regex match).

## Parallel construction discipline (SCRIBE Phase 4 self-check, added 2026-06-02)

A writing-quality discipline distinct from the structural gates. When listing 3+ examples in parallel, grammatical construction must match across all items. Elements that must match: possessive form (all use 's or none do), article usage (all use "the" or none do), preposition usage (same preposition or restructure), quote marks (all quoted or none quoted), descriptor style (all colors, all team names, or a consistent mix).

The issue that surfaced this discipline: a Short Description listing "Argentina's albiceleste, Mexico scarf called 'verde', USMNT red-white-blue, Germany's DFB black-red-gold, and Italy's azzurro" (Day 2 batch #1 URL #3). Mixed possessive (Argentina's, Italy's) vs descriptive (Mexico scarf called, USMNT red-white-blue); mixed quote marks ('verde' quoted, others not); mixed extra qualifiers (Germany's DFB inserted, others none).

Pick one construction and apply it consistently:

- OPTION A (all possessive): "Argentina's albiceleste, Mexico's verde, USMNT's red-white-blue, Germany's black-red-gold, and Italy's azzurro".
- OPTION B (all descriptive): "the albiceleste of Argentina, the verde of Mexico, the red-white-blue of USMNT, the black-red-gold of Germany, and the azzurro of Italy".

Apply wherever listing 3+ parallel examples: federation / country lists, product type lists, brand attribute lists, tournament / event lists. ORIN re-checks at the orchestrator layer as a sanity scan (flag inconsistent 3+ example lists; judgment call, not a regex match).

## Editorial philosophy disciplines (Phase 4 self-checks, added 2026-06-02)

Gate 13 (anti-stuffing) and Gate 14 (specific counts) catch structural manifestations of a deeper gap: copy that clears every gate but still reads as algorithm-serving rather than reader-serving. These four editorial philosophy sub-disciplines are judgment calls SCRIBE applies during Phase 4 drafting (alongside image precision, parallel construction, and supporting keyword selection) and ORIN sanity-scans at the orchestrator layer. They are NOT gates (gates govern structural patterns; editorial philosophy is judgment) and NOT script-enforced (too judgment-dependent for regex). The comprehensive principle documentation and the full positive-anchor / manipulation-pattern reference lists live in `context/workforce-conventions.md` 'Editorial philosophy (added 2026-06-02)'.

The issue that surfaced these: the URL #3 (national-team-scarves) Short Description opened with emotional work ("Soccer scarves started on the freezing terraces of early-1900s English grounds, and they never left") and then collapsed into list-of-products mode in the very next sentence. The emotional arc broke immediately, before it could carry the reader toward the purchase.

### 1. Reader-first copy orientation

Body copy serves the buyer's emotional connection to what they are buying. SEO ranking is the byproduct, not the goal; keywords appear because they describe what the reader actually cares about, not because they need to appear. Per-sentence test: does this sentence serve the reader's decision, or the algorithm? Would a first-time buyer find it valuable, or feel they are being marketed to? Anti-patterns: keyword surfacing without reader value (the structural form Gate 13 caught), specification listing without emotional context (the form Gate 13 pricing caught), generic positioning that could describe any product ("premium quality", "top-tier selection", "best-in-class"), and brand or manufacturer specs leading the copy before reader value is established. Natural alternatives: sentences that describe specific buyer experience or identity, concrete sensory anchors, and place / ritual / heritage tied to buyer identity.

### 2. Cognitive load reduction

Body copy is read mid-decision, when the buyer is already evaluating brand, color, fit, price, occasion, and alternatives. Copy that adds load loses the sale. Rules: vary sentence length (short 5 to 10 words for emphasis or transition; medium 15 to 25 for substance; long 30+ only when narrative justifies, rarely), and avoid stacking long sentence after long sentence into dense blocks. One concept per sentence: if two ideas are joined by "and", "but", "while", or "with", consider whether splitting serves the reader, since multiple ideas force the reader to hold both in working memory. Concrete over abstract: "fans raise scarves overhead during the anthem" beats "scarves embody the ritual of supporter culture"; "six matches into the tournament cycle" beats "deep into the competition phase". Scan-ability: the first sentence of each paragraph and each H2 carries the value proposition, because most collection-page and PDP readers scan rather than read every word; do not bury the lead.

### 3. Value-first sequencing

Lead with what the buyer cares about, not what the product is technically. Each body section follows the arc hook -> connection -> specifics -> action. HOOK (emotional or identity anchor: why this matters to the buyer's life, e.g. "what fans wear when the anthem starts"). CONNECTION (specific scenario: how the buyer uses or experiences this, the concrete sensory or social context). SPECIFICS (product context: tier / positioning language without specific prices, brand callouts with narrative justification, material or construction detail only where it serves the buyer's decision). ACTION (clear next step: implicit like "the full federation roster", or a low-pressure explicit invitation like "shop the lineup before kickoff week"; never "buy now" or "don't wait"). Anti-pattern: starting with brand or spec data before reader value. INCORRECT: "adidas produces the federation kit lineup using Heat.RDY moisture-wicking fabric in Stadium and Authentic tiers. The 2026 collection includes twelve national teams with..." CORRECT: "The 2026 World Cup brings the federations to a continent that has been waiting forty years for the tournament. The kits arrive in two tiers, Stadium for the everyday and Authentic for match day, across the adidas roster including Argentina, Mexico, Germany, Spain, and more."

### 4. Positive emotional anchoring

Copy evokes positive emotions tied to the purchase (belonging, identity, ritual, anticipation, heritage, place) and never uses manipulation (scarcity, FOMO, status anxiety, hyperbole, false urgency). Positive anchors invite the reader into a community or experience they want to belong to; manipulation pressures the reader through fear or insecurity. The first builds long-term brand affinity, the second extracts a single transaction. Quick reference (full lists with phrase examples in workforce-conventions): USE belonging ("how fans show up", "what the section wears"), identity ("the crest carried at the shoulder", "colors that say what side you are on"), ritual ("raised when the anthem starts", "held high through the opening chants"), anticipation ("six matches into the tournament cycle", "with kickoff week ahead"), heritage ("from the 1986 archive to the 2026 Stadium tier"), place ("the Rose Bowl, the diaspora's home stadium"). NEVER scarcity ("only 5 left", "selling out fast"), FOMO ("don't miss", "before they are gone"), status anxiety ("for true supporters only", "what real fans wear"), hyperbole ("the greatest scarf ever made", "the perfect kit"), false urgency ("limited time", "while supplies last").

### 5. Outcome-based copywriting (added 2026-06-03, extends dcfe6da)

Buyers buy outcomes, not products. The cleat isn't the product. The Saturday morning where their kid plays with confidence is the product. PDP Short Description and Description prose paint a concrete picture of the buyer's life after they own the cleat, showing the outcome they are really buying, not the features that produce it. Three techniques: future-pacing (sensory description that places the buyer in the moment of using the cleat, e.g. "Saturday morning, your kid's first kick, the grass still wet and they're already grinning"), show the transformation (the uncertain kid becomes the confident kid; the parent worried about quality becomes the parent who trusts the gear), and concrete over abstract (specific scenes like "their first goal in the new cleats, the way they look back at you on the sideline", never abstract claims like "premium comfort"). PDP application: the Short Description (50 to 100 words) is entirely outcome-based with no feature mention; each Description prose H2 opens with the outcome then connects to the cleat where natural (heritage as outcome, use case as outcome, fit as outcome); the Product Details bullet H2 stays technical and scannable (the outcome rule does NOT apply to bullets); FAQ answers apply the principle where the question is about a buyer outcome (fit, "is this right for my kid"), not where it is purely technical (Elite versus Pro tier differences). Full rule: `context/workforce-conventions.md` 'Editorial philosophy (added 2026-06-02)' sub-discipline 5.

Operational placement: SCRIBE applies all four during Phase 4 (brief drafting) before the Phase 5 voice check, self-revising any sentence or section that fails. ORIN sanity-scans at the orchestrator layer (flag obviously algorithm-serving sentences, dense paragraph blocks lacking sentence variety, H2 sections that lead with specs before reader value, and any manipulation language). Cross-references: `.claude/agents/on-page-seo/agent.md` Section 9 (Phase 4 editorial philosophy checks), `.claude/agents/master-strategist/agent.md` Section 9 + Section 11 (ORIN editorial sanity scan), `context/workforce-conventions.md` 'Editorial philosophy (added 2026-06-02)' (full principle documentation + reference lists).

## Five canonical brief-craft rules

These five rules govern every brief SCRIBE produces under the Fresh Optimization workflow. They emerged from the 2026-05-26 UAE PDP refinement session and lock in agency-grade craft standards across all future briefs. The five rules below are the NEW codification from this session; the PDP external link policy (internal-only, locked) is already canonical in 'Internal links only on product pages' later in this playbook, and the 1 to 2 internal-links target is already canonical in 'Internal link strategy' later in this playbook. Those existing policies stand; the five rules below extend them with the craft conventions that emerged from the UAE v3 work. Cross-referenced from `.claude/agents/on-page-seo/agent.md` Section 13 and `context/workforce-conventions.md`.

### Rule 1: Supporting keywords distributed as semantic variants in body

Each supporting keyword from the brief's Keyword research block appears 1 to 2 times in the Long Description, woven naturally as a semantic variant. The goal is topic depth signal, not keyword stuffing or exact-match density. A variant must read as natural English in its sentence; if a variant cannot land naturally, skip it rather than force the appearance. The primary keyword maintains 2 to 4 exact-match appearances across the body per the keyword-density guidance in `.claude/agents/on-page-seo/agent.md` Section 9 'Keyword placement per field'.

Worked example: UAE 2026 PDP v3 at `deliverables/page-optimizations/2026-05-26_session-01/uae-2026-home-stadium_brief-v3.md` distributes `uae football jersey`, `uae fa jersey`, `uae national team jersey`, and `uae football kit` across the body, each variant once or twice in natural reads.

### Rule 2: Primary keyword appears in at least one H2 header

Minimum one H2 in the Long Description contains the primary keyword or a close variant. The header signal carries SEO weight beyond body-text density. One natural integration is the floor, not the ceiling; don't force every H2 to carry the keyword. If the natural H2 framing cannot integrate the primary keyword, restructure the H2 rather than force the keyword into a clumsy heading.

Worked example: UAE 2026 PDP v3 first H2 reads "The 2026 UAE Soccer Jersey by adidas" (primary keyword plus brand qualifier as natural framing).

### Rule 3: Meta description structure (commercial intent + trust signal + emotional CTA)

The Meta Description is structured in three parts:

1. **First sentence: commercial intent confirmation.** Primary keyword plus brand. Front-loaded for SERP-bold matching and immediate intent recognition.
2. **Middle: trust signal plus specific differentiator.** Trust words ("Official", "Certified", "Licensed") combined with one or two specific differentiators (federation design, signature technology, edition tier).
3. **Close: emotional or commercial CTA matching body voice.** The close should echo the avatar's emotional anchor from the body. The close must NOT duplicate the Short Description's close (per Rule 5); each field closes with its own punch.

**Tier-aware language for branded products.** Edition tiers on branded national-team and pro-line products are distinct words with specific commercial meaning. "Authentic" and "Stadium" are two different adidas national-team kit tiers (Authentic = match-spec construction; Stadium = Replica-tier). Combining tier words ("Authentic Stadium") reads as a contradiction to soccer-knowledgeable readers. Use "Official" plus the tier name as the trust-and-tier pattern: "Official Stadium home kit" rather than "Authentic Stadium home kit". The same principle applies to other brand-line tier conventions (e.g., Nike Mercurial's Elite vs Vapor tiers); verify the hierarchy in topic research before drafting.

Target length: 150 to 158 characters for desktop display, 130 to 140 for the mobile threshold. The trust-and-tier pattern fits comfortably within both.

Worked example: UAE 2026 PDP v3 Meta Description reads "The 2026 UAE Soccer Jersey by adidas. Official Stadium home kit with UAEFA federation design and Climacool weave. Wear what Al-Abyad wears." (139 chars). First sentence: primary keyword plus brand. Middle: "Official" trust signal, tier-correct "Stadium home kit", "UAEFA federation design", and "Climacool weave" specific differentiators. Close: "Wear what Al-Abyad wears" emotional CTA matching the body's Al-Abyad framing.

### Rule 4: Named entities in body copy serve LLM search discoverability

Body copy includes 5 to 10 specific named entities per page where natural to the topic. LLMs (ChatGPT, Claude, Gemini, AI Overview) latch onto specific named entities far more than generic feature lists when surfacing source citations. A page that names players, federations, tournaments, and signature technology becomes a citable source; a page that says "premium quality jersey for soccer fans" becomes wallpaper.

Categories of named entities to include where relevant:

- **Players** (signature pros associated with the team, kit, or product line)
- **Teams or clubs** (the affiliation the page is about)
- **Federations** (governing bodies, e.g., UAEFA, FMF, FA, US Soccer Federation)
- **Tournaments** (current or upcoming events the product anchors to, e.g., AFC Asian Cup 2027, Copa America 2024)
- **Signature product lines** (e.g., Mercurial, Predator, Tiempo, Phantom GX)
- **Signature features or technologies** (Climacool, Heat.RDY, Flyknit, Air Zoom, ACC)
- **Locations** (relevant geographic anchors: host cities, training centers, stadium names)
- **Manager or coach names** (head coach of the team, head designer of the brand line where notable)

Each named entity should be specific (`Paulo Bento` not "the coach"), correct (verified in topic research), and integrated naturally into the body's narrative flow.

Worked example: UAE 2026 PDP v3 body names Al-Abyad, UAEFA, AFC Asian Cup, Saudi Arabia, Paulo Bento, Ali Mabkhout, Iraq, South Korea, Vietnam, Group E, Climacool, Stadium edition, and Authentic edition. Thirteen distinct named entities across the four H2 sections.

### Rule 5: Short Description structure

The Short Description (1 to 3 sentences, 200 to 300 chars target) carries five structural requirements:

1. Primary keyword in the first or second sentence.
2. Avatar identity hook in the first half (Carlos, Tyler, Jennifer, or Mike the Coach framing per `context/04-customer-avatars.md`).
3. 2 to 3 specific design or product details that differentiate the product from generic competitors.
4. Emotional or commercial CTA close, DIFFERENT from the Meta Description close. The Meta Description and Short Description must not duplicate the same closing line; each closes with its own punch.
5. Concise and scannable. The Short Description lives at the top of the description body and competes with the variant selector and add-to-cart for attention.

Worked example: UAE 2026 PDP v3 Short Description reads "For the supporter whose flag carries red, white, black, and green. The 2026 UAE soccer jersey by adidas: clean white base, red V neck and shoulder stripes, sleeve patterning drawn from the federation's Arabic-script logomark. Climacool weave, doubleknit build." Avatar identity hook in sentence one (the Emirati flag supporter, Carlos diaspora frame). Primary keyword in sentence two (`uae soccer jersey`). Three design details in sentence two (white base, red V neck, sleeve patterning). Technical close in sentence three (Climacool weave, doubleknit build), distinct from the Meta Description close ("Wear what Al-Abyad wears").

## Required pre-write research

Lighter than collection-page research because the topic is narrower (a specific SKU rather than an entire team or brand line). Either ORIN runs the research before SCRIBE writes, or SCRIBE runs it natively as part of the dispatched workflow. Both patterns are now architecturally supported (sub-agents have native MCP access per the canonical `mcpServers:` configuration documented in `context/workforce-conventions.md` 'Sub-agent configuration discipline'). The choice is a workflow design call: ORIN-runs keeps research visible in the main session for Mike's review; SCRIBE-runs keeps the dispatched workflow self-contained. Keyword research (DataForSEO MCP) and topic research (Tavily MCP, when authenticated) are both within SCRIBE's `mcpServers:` scope. Outputs land in SCRIBE's session briefing regardless of who pulled the data.

For any product page, ORIN researches:

- The brand's heritage and signature design elements relevant to this product. (Two to three Tavily queries.)
- The specific product's design rationale. What was the designer thinking? What problem does this version solve that the previous version didn't? What's new in this generation? (Two to four queries.)
- The product's place in the brand's lineup. Entry-level, mid-tier, premium, special edition, signature pro model. (One to two queries.)
- Who wears or uses this product. Pro athletes, demographics, occasions, surfaces. (Two to three queries.)
- The product's place in the avatar's purchase consideration set. What else is the avatar comparing this against? (Two to three queries.)

Six to twelve Tavily queries per product page is normal. Less if the product is a routine SKU in a known line (the third-pass on a Predator model the team has researched twice already). More if it's a flagship release the team hasn't researched before.

## Current state capture (Shopify Hyper theme on ProSoccer)

Before drafting the optimized brief, SCRIBE captures the live state of all six SEO-relevant fields directly from the live PDP via Firecrawl scrape. The live page is the source of truth; Mike does not paste content into the session.

### Field inventory (six fields per PDP)

Every PDP capture must include all six fields, in this order:

1. **Title (H1)**
2. **Slug** (the `/products/<slug>` path component)
3. **Meta Title** (the `<title>` element, may differ from H1)
4. **Meta Description** (the `<meta name="description">` content)
5. **Short Description** (rendered as the first paragraph in the description body, before bullets or any H2; stored as a Shopify metafield on ProSoccer's Hyper theme installation)
6. **Long Description** (bullets plus body content below the Short Description; the remainder of the description body after the Short Description paragraph)

### Capture method

`mcp__firecrawl-mcp__firecrawl_scrape` on the target PDP URL returns the rendered page content. SCRIBE parses the scrape output to identify:

- Title from the H1 element.
- Slug from the URL path.
- Meta Title and Meta Description from the page metadata block.
- Short Description from the first paragraph in the description body region (the metafield rendering point on Hyper).
- Long Description from the content after the Short Description paragraph through the end of the description body.

The Firecrawl scrape captures both Short Description and Long Description in a single call because both render in the visible description body. There is no separate metafield API call needed at capture time; Shopify renders the metafield content into the body HTML, and Firecrawl captures the rendered output.

### Hyper theme metafield reality

ProSoccer runs the Shopify Hyper theme. Short Description is implemented as a Shopify metafield (not as a separate field in the Shopify admin product editor's main description area) and is rendered by the theme's Liquid templates as the first paragraph of the description body, above the bullets and Long Description content. To the avatar, it reads as the lead paragraph of the product description; to the SEO workforce, it is a distinct, separately editable field with its own optimization rules per 'Rule 5: Short Description structure' in 'Five canonical brief-craft rules' above.

This is the field reality discovered 2026-05-26 during Liverpool PDP current-state capture. It supersedes the earlier "Mike supplies the existing Short Description and Long Description directly as input to the optimization" rule that appeared in the Fresh Optimization workflow before the Firecrawl MCP install made native PDP scraping viable at sub-agent dispatch level.

### Blocker condition

If a specific PDP scrape does not produce a clean separation between Short Description and Long Description (no distinct first paragraph; description content appears in an unexpected location; the metafield rendering is missing or merged into an unstructured block), SCRIBE surfaces the capture failure as a blocker BEFORE drafting the brief. Do NOT proceed with an empty Short Description input or a guess at where Short Description ends and Long Description begins. Surface to ORIN with the scrape output for inspection; ORIN routes the field-parsing question to Mike or to a manual Shopify admin lookup as appropriate.

### Brief-format implication

The visible brief stays forward-looking per the Fresh Optimization workflow in `context/workforce-conventions.md` (no Current state section in the brief itself; Mike references Shopify admin during implementation). Current-state capture is for SCRIBE's drafting context, not for surfacing in the deliverable. The capture lives in the workforce-internal briefing at `.claude/agents/on-page-seo/briefings/YYYY-MM-DD_<slug>.md` per the existing data-provenance discipline.

## Field-specific rules

Same six fields as a collection page, but with product-page subject framing.

### Title (Product Title)

Names the specific product. Brand, model, version. Avatar-search-language preserved here.

- 2026 Mexico Home Authentic by adidas: `Mexico 2026 Home Authentic Jersey by Adidas`
- Nike Mercurial Superfly 9 Elite: `Nike Mercurial Superfly 9 Elite FG Soccer Cleats`
- adidas Tiro 23 Training Pants: `Adidas Tiro 23 Training Pants`

The product name appears in this field exactly the way the avatar searches for it. If the avatar searches for "Mexico 2026 home jersey," that's the framing. If the avatar searches for "Mercurial Superfly Elite," that's the framing.

Length: 30 to 100 characters (hard min and max per 'PDP-specific SEO discipline' above). For pack/series products, the Title must be unique across sibling SKUs (tier / plate / colorway / generation differentiator).

### SEO Meta Title

Product head term first for SERP discovery. Brand and tier qualifiers follow.

- `Mexico 2026 Home Authentic Jersey | Adidas Player Edition`
- `Mercurial Superfly 9 Elite FG | Nike Pro Soccer Cleats`
- `Adidas Tiro 23 Training Pants | Slim-Fit Track Pant`

60 characters maximum INCLUDING the Hyper theme brand suffix, so the INPUT field stays under approximately 48 to 50 characters (per 'PDP-specific SEO discipline' above). Front-load the product name; never put "ProSoccer" in the field. Must be unique across sibling SKUs for pack/series products.

### SEO Meta Description

Speaks to the buyer (the avatar in purchase consideration), includes a CTA tied to the product. Anchored to the product's value, not to the store.

Product-anchored CTAs:

- `Lock in the 2026 home kit before kickoff`
- `Shop the cleat Mbappé wears`
- `Pick your Tiro fit`

Store-anchored CTAs (do not use):

- `Shop ProSoccer for the lowest price`
- `Order now for free shipping`

160 characters maximum (hard ceiling per 'PDP-specific SEO discipline' above); 150 to 158 is the desktop target inside that ceiling. Head term naturally placed in the first 100 characters.

### Short Description (intro paragraph or product blurb)

Emotion-first lead. The first sentence carries identity, moment, or feeling for the avatar buying this product. Per `context/03-brand-voice.md` 'Emotional Connection Over Feature Selling', features wait until sentence two or three.

50 to 100 words (per 'PDP-specific SEO discipline' above). On ProSoccer's Hyper theme this is the "Short Description" metafield, which renders in the hero block above Add to Cart (NOT the same field as the "Description" body_html that renders in the accordion below the product images). A brief reader-first emotional or value-prop hook; no feature listing.

### Long Description (body copy)

Three to five H2 sections about the product and the brand. Topic-research outputs become the substance.

H2 patterns by product type:

- **Premium kit jersey:** brand and federation context, the design story for this kit, the player edition vs the fan edition, fit and sizing, kit history and why this version matters.
- **Performance cleat:** brand line context (Predator, Mercurial, Tiempo), this generation's design rationale, who wears it, fit and surface guidance, plate and stud configuration, who the cleat is for and isn't for.
- **Training apparel:** brand context, fabric and tech detail, where it fits in the avatar's wardrobe (training, travel, casual), fit and sizing, care.
- **Equipment (balls, bags, gloves):** brand line context, design and tech, who uses it, durability and care.

This is ProSoccer's "Description" (body_html) field, rendering in the collapsible accordion below the product images. Length is tiered by product complexity (per 'PDP-specific SEO discipline' above): Simple ~125 to 200 words, Standard ~200 to 300, Complex ~300 to 400 (cleats, authentic jerseys, technical gloves, tournament editions). This tiered range supersedes the older flat "200 to 400 words" target and is grounded in 2026 ecommerce ranking data. Split reader-first prose H2 sections from a dedicated "Product Details" bullet H2 per 'Description structure: prose H2 sections + a dedicated "Product Details" bullet H2' below: prose carries the WHY, bullets carry the WHAT (specs). Never list technical specs in prose.

Each H2 passes the lift test from `.claude/agents/on-page-seo/agent.md` Section 11 Gate 9.

### FAQ section (optional)

For high-consideration products (premium kits, flagship cleats, technical equipment), three to five product-specific Q-and-A pairs help close the sale. Sizing, surface guidance, care, authenticity, customization. Schema attaches via VERITAS's FAQPage injection.

Forbidden FAQs (these belong on store-policy pages):

- `What's your return policy?`
- `How long does shipping take?`

Required if relevant:

- `What's the difference between the player and fan version?` (premium kits)
- `Should I get the Elite or the Pro?` (multi-tier cleat lines)
- `What size should I order if I'm between sizes?` (apparel and footwear)
- `Is this kit authentic Adidas, or a replica?` (high-counterfeit categories)

## Worked example 1: Premium kit jersey

URL: `/products/mexico-2026-home-authentic-jersey-adidas`
Primary avatar: Carlos
Secondary avatar: Tyler (performance buyer who wants the player cut for training-and-wear)
Topic-research outputs: adidas El Tri kit supplier since 1999; Heat.RDY weave on the player edition; player-edition tighter cut and heat-bonded badges; fan-edition softer fabric and standard fit; price gap typically $30 to $50; the 2026 home kit features a verde primary with Aztec patterning and FMF crest.

```
Title (Product Title)
Mexico 2026 Home Authentic Jersey by Adidas

SEO Meta Title
Mexico 2026 Home Authentic Jersey | Adidas Player Edition
[58 chars]

SEO Meta Description
The 2026 El Tri home kit, player edition. Adidas Heat.RDY weave, the close cut the squad wears, the official FMF crest and federation tags. Lock it in.
[152 chars]

Short Description
The kit El Tri walks out in at Estadio Azteca on June 11, 2026. Player edition Heat.RDY weave, the close cut the squad wears, the FMF crest heat-bonded the way Adidas does it for the federation. Wear what they wear.

Long Description:

## Adidas and El Tri

Adidas has supplied the Mexico kit since 1999. The 2026 home keeps verde as the primary, with an Aztec-coded pattern across the chest panel and a darker green shoulder shading. The crest sits centered in the traditional FMF placement.

## Player Edition vs Fan Edition

The player edition uses Adidas Heat.RDY weave, which moves more sweat than standard polyester. The cut runs closer to the body the way pro players prefer, and the badges are heat-bonded rather than stitched. This is the kit the squad wears on the pitch.

The fan edition (sold separately) uses softer climalite fabric and a regular fit, with stitched badges. Same look from across the room. Different feel up close, and a different price by $30 to $50. Pick the player edition if you want what they wear; pick the fan edition if you want the silhouette without the pro-tier fabric.

## Fit and Sizing

Player edition runs slim. If you wear an athletic-cut shirt or a fitted tee at the chest you measure today, that's your size. If you wear a relaxed-fit tee, size up one. The fabric stretches at the chest and shoulder; it doesn't stretch at the waist hem.

Adidas youth sizes run a size smaller than US-standard youth (Adidas YL is closer to a US small). For kids between sizes, size up; the kit has more shrink in the wash than stretch on the body.

## What's Included

The jersey itself. Federation tags inside the collar with the holographic. The Adidas care card. Customization (player name and number) is a separate option through the storefront and adds five to seven business days to ship.
```

Annotation:

- Body copy is about the product and adidas's design choices, not about the store.
- Topic-research outputs are visible: kit-supplier history, Heat.RDY context, player-vs-fan distinction, the verde-primary detail, the youth-sizing fact.
- Carlos primary anchors the emotional context (Estadio Azteca, "wear what they wear"). Tyler shows up implicitly in the player-edition framing for performance-minded buyers.
- The store doesn't appear inside the body copy. Returns, shipping, and retail are not mentioned. Those live in the cart and checkout flow.
- Voice rules: contractions used, varied sentence rhythm, specifics throughout, no forbidden words, no em-dashes.

## Worked example 2: Performance cleat

URL: `/products/nike-mercurial-superfly-9-elite-fg`
Primary avatar: Tyler
Secondary avatar: Carlos (collector buying because Mbappé wears them)
Topic-research outputs: Mercurial line launched 1998 with Ronaldo R9; Nike's speed-cleat franchise; Vapor (lighter, less collar) and Superfly (knit collar); Elite tier uses Flyknit and Air Zoom plate; signature pros include Mbappé, Vinicius Junior, Cristiano Ronaldo historically; Superfly 9 generation released for European season; firm-ground plate for natural grass.

```
Title (Product Title)
Nike Mercurial Superfly 9 Elite FG Soccer Cleats

SEO Meta Title
Mercurial Superfly 9 Elite FG | Nike Speed Cleat with Air Zoom
[60 chars]

SEO Meta Description
The cleat Mbappé and Vinicius wear. Nike Mercurial Superfly 9 Elite, Flyknit upper, Air Zoom plate, the speed cleat for the player who wants to break the line.
[157 chars]

Short Description
You're not asking how fast they are. You're asking how fast they make you. Mbappé chose them, Vinicius chose them, the Mercurial is the cleat for the player whose first move is the run.

Long Description:

## The Mercurial Line, Then and Now

Nike launched the Mercurial in 1998 for Ronaldo R9 at the World Cup in France. Twenty-six years and a dozen generations later, the line still belongs to the fastest player on the pitch. Mbappé wears them at PSG and the next club after. Vinicius Junior wears them for Real and Brazil. Cristiano Ronaldo built half his career in them.

## What's New in the Superfly 9 Elite

Flyknit upper, lighter than the previous generation by about ten grams per cleat. Air Zoom plate underneath for the energy return on the toe-off. Knit collar for ankle lock-in (the Superfly cut, vs the Vapor's lower collar). Heat-mapped traction stud pattern for cuts and turns.

## Superfly vs Vapor

Same upper, same plate, different collar. The Superfly's knit collar adds ankle support and locks the foot at the heel. The Vapor (sold separately) skips the collar for a couple of grams of weight savings and a lower-cut feel. Superfly for the player who wants the lock; Vapor for the player who wants the cleat to feel barely there.

## Surface and Fit

Firm-ground plate. Natural grass and most well-maintained turf. For artificial grass, see the Superfly 9 Elite AG (sold separately); for older astroturf, the Superfly 9 Pro TF. The Elite tier runs narrow at the forefoot. Wide-foot players usually find the Tiempo or the Predator a better fit.

Sizes run true. Order your standard US cleat size if you've worn Mercurials before; if you're crossing over from a wider cleat, consider half a size up.
```

Annotation:

- Body is about the Mercurial line and this specific generation, not about the store.
- Topic-research outputs visible: launch year, current pros, Flyknit and Air Zoom detail, Superfly-vs-Vapor distinction, narrow-fit fact.
- Tyler primary throughout: performance specifics, plate and surface guidance, fit comparison to other lines.
- Carlos secondary surfaces in the pro-roster opening (collectors care which pros wear them).
- The wide-foot guidance addresses Jennifer's pain frame even though Jennifer isn't a primary avatar for an Elite-tier $300+ cleat. That's a cross-avatar landing scenario captured cleanly.

## Worked example 3: Training apparel

URL: `/products/adidas-tiro-23-training-pants`
Primary avatar: Tyler (training fit)
Secondary avatar: Mike the Coach (team kit and travel)
Topic-research outputs: Tiro line launched in the 2000s as adidas's training-pant franchise; signature three-stripe down the side; tapered slim-fit cut; AEROREADY moisture management; ankle zip; popular as both a training pant and a casual wear item; Tiro 23 is the current generation as of 2026.

```
Title (Product Title)
Adidas Tiro 23 Training Pants

SEO Meta Title
Adidas Tiro 23 Training Pants | Slim-Fit Soccer Track Pant
[57 chars]

Short Description
The pant every player owns four pairs of. Tiro is what you train in, travel in, warm up in, and what you put on after the match because they're the most comfortable pants you own.

Long Description:

## The Tiro Line

Adidas launched the Tiro as a training pant in the early 2000s. It's evolved every couple of years; the current Tiro 23 is the seventh major generation. The three stripes down the side, the tapered slim cut, and the ankle zip have stayed constant. The fabric, the AEROREADY tech, and the cuts get refined each round.

## What the Tiro 23 Adds

AEROREADY moisture management for warm-weather training. A slimmer leg through the knee than the Tiro 21. Ankle zips that open wider for cleats. A redesigned waistband with a flat-front draw cord that doesn't bunch under a jersey.

## Fit and Sizing

Slim through the leg, tapered at the ankle. If you wear a slim-fit pant in jeans, this is your size. If you wear a relaxed cut, size up one. The waistband sits at the natural waist; the inseam runs about 31 inches on a medium.

## Where Players Wear Them

Training. Pre-match warmups. Travel days. Casual wear. Mike the Coach orders them for team-issue because they hold up to repeated wash cycles and they look the same in year three as in year one. Tyler wears them under a jersey when the morning's cold and over the kit on the bus to the away match.
```

Annotation:

- Body about the Tiro line and this generation, not about the store.
- Topic-research outputs: launch era, generation count, AEROREADY detail, fit specifics.
- Tyler primary in the fit guidance and the use-case detail. Mike the Coach surfaces in the durability and team-issue framing.
- The store doesn't appear in the body. Bulk-order and team-issue routing for Mike the Coach happens via the team-orders page, not via the product-page description.

## Category-specific H2 templates (DRAFT v1, to be validated through real PDP optimization work)

Draft H2 frameworks per product category. The frameworks are starting patterns; the FINAL template for each category becomes canonical only after a real PDP in that category passes gate review at agency-grade quality. Until then, treat them as DRAFT v1 starting points, not locked rules.

Notes that apply to all categories:

- The five canonical brief-craft rules earlier in this playbook apply universally regardless of category.
- Section structure may flex based on individual product needs. A specific cleat with minimal player association doesn't force the H2 5 section. A simpler accessory may use 3 H2s where a flagship uses 5.
- Number of H2s varies by category (4 for most, 5 for soccer cleats, sometimes 3 for simpler accessories).
- Worked example 1 (Premium kit jersey) and Worked example 2 (Performance cleat) earlier in this playbook are full worked examples for the National Team Jersey and Soccer Cleats categories; the templates below extract and generalize the patterns to cover ProSoccer's full catalog.

### 1. National team jersey (CANONICAL, four-time validated within 2026 World Cup cycle)

- H2 1: Brand + design + federation identity ("The [Year] [Country] Soccer Jersey by [Brand]")
- H2 2: Edition tier comparison (Stadium vs Authentic, where applicable)
- H2 3: Fit and sizing
- H2 4: What you're buying into (cultural + tournament context + future catalyst)

**Validation history:**

- UAE 2026 Home Stadium Jersey v3 (foundational, 2026-05-26 era at `deliverables/page-optimizations/2026-05-26_session-01/uae-2026-home-stadium_brief-v3.md`): template structure proven against a smaller-federation kit with federation-identity focus.
- Mexico 2026 Home Stadium SS Jersey (commit `e56a7d6`, 2026-05-28): template validated against a co-host federation with Aztec heritage design depth + Estadio Azteca opener narrative.
- Mexico 2026 Away Stadium SS Jersey (commit `85dd1f0`, 2026-05-28): template validated with travel / road-match angle on H2 4 and pre-Hispanic Mesoamerican design depth on H2 1.
- Mexico 2026 Third Stadium SS Jersey (commit `f2c2c34`, 2026-05-28): template validated with special-edition / wardrobe-completionist angle on H2 4 and adidas x Someone Somewhere artisan collaboration depth on H2 1.

Promotion to CANONICAL on 2026-05-28 after four-time validation across two federations, two design philosophies (UAE classic federation identity, Mexico co-host + Aztec heritage narrative), and three kit types within one team (Home / Away / Third differentiation). Template architecture proven stable; no refinements surfaced through the Mexico kit set production. Promotion documents validation breadth for future workforce session confidence; template structure unchanged.

### 2. Club jersey (CANONICAL as of 2026-05-26)

Validated by: Nike 2024-25 Liverpool Men's Stadium Away Jersey brief at `deliverables/page-optimizations/2026-05-26_session-01/nike-2024-25-liverpool-mens-stadium-away-jersey_brief.md`. Template applied clean without flex; topic depth from Slot title + Klopp farewell + Nike-to-adidas transition + Hillsborough tribute filled the framework substantively.

- H2 1: Brand + design + club crest / identity ("The [Year] [Club] [Home / Away / Third] Jersey")
- H2 2: Edition tier or player personalization options
- H2 3: Fit and sizing
- H2 4: Club narrative + season catalyst + player associations (or club heritage where the current narrative is thin)

**Refinement note on H2 4:** the Liverpool validation worked with an unusually rich season catalyst (Premier League title win, manager farewell, kit-supplier brand transition, Hillsborough tribute). Mid-table clubs in quiet seasons may not carry the same narrative depth; in those cases, fall back to club heritage (founding history, classic kit cycles, signature players across eras, derby rivalries) as the H2 4 substance. The H2 framing flexes; the section's role (anchor the avatar's emotional connection to the club beyond the on-pitch product spec) does not.

### 3. Soccer cleats (VALIDATED v1, validated by Predator Accuracy.1 FG 2026-05-26)

- H2 1: Model + generation + signature technology ("The [Model] [Generation] by [Brand]"). Player heritage anchor permitted here (heritage-line players who define brand identity, e.g. Beckham/Zidane/Gerrard for Predator); frees H2 5 to do narrative or closeout work.
- H2 2: Surface compatibility (FG / AG / IC / TF breakdown). REQUIRED across all cleat-category SKUs, not optional. Load-bearing for the competitive-player avatar; high cross-avatar utility for parents shopping for kids' cleats.
- H2 3: Position fit + player level (Elite / Pro / Club / Junior tiers, plus line-positioning vs sibling silhouettes like Predator vs F50 vs Copa, or Mercurial vs Tiempo vs Phantom).
- H2 4: Fit + sizing (with width considerations vs sibling lines).
- H2 5: Player association + tournament context (current-cycle cleats) OR generation-closing / closeout narrative (older-cycle cleats at clearance pricing). Flex the framing based on cleat freshness: when the verifiable current-generation player roster is rich, anchor to it; when the page is a closeout SKU and current-roster verification is thin, pivot to the colorway / pack-context / closing-window narrative that serves the closeout buyer. The H2 framing flexes; the section's role (anchor the avatar's emotional connection beyond the spec sheet) does not.

**Validation history:**
- Predator Accuracy.1 FG Crazyrush Pack (2026-05-26): 4 of 5 H2s landed clean; H2 5 reshaped from player-association to closing-window narrative because the page is a closeout product and the Accuracy-generation roster was not independently verifiable. This validation produced the three refinements above (heritage anchor in H2 1, surface compatibility required, H2 5 flex pattern). Promotion from DRAFT v1 to VALIDATED v1.
- Pending: a current-cycle flagship cleat PDP (e.g. Predator 25/26 or Mercurial Superfly 10) to validate the "player-association-rich" framing of H2 5 before promotion from VALIDATED v1 to CANONICAL.

### 4. Goalkeeper gloves (DRAFT v1, pending validation)

- H2 1: Cut + palm technology (negative, rolled, flat, hybrid)
- H2 2: Match conditions (dry / wet / hybrid)
- H2 3: Player level tier
- H2 4: Fit and sizing

### 5. Goalkeeper jerseys (DRAFT v1, pending validation)

- H2 1: Brand + design + GK-specific features
- H2 2: Padded vs unpadded options
- H2 3: Fit and sizing (GK fits differ from outfield)
- H2 4: Team affiliation and use cases

### 6. Training apparel (DRAFT v1, pending validation)

- H2 1: Affiliation + design
- H2 2: Match-day vs training vs lifestyle use
- H2 3: Fit and sizing
- H2 4: Material + climate + layering

### 7. Casual / lifestyle apparel (DRAFT v1, pending validation)

- H2 1: Affiliation + design + style identity
- H2 2: Streetwear vs match-day vs travel use
- H2 3: Fit and sizing
- H2 4: Material + season

### 8. Soccer balls (DRAFT v1, pending validation)

- H2 1: Type + use case (match / training / replica)
- H2 2: Specifications (size, weight, FIFA quality tier)
- H2 3: League / tournament affiliation
- H2 4: Technology + construction

### 9. Shin guards (DRAFT v1, pending validation)

- H2 1: Protection level + position fit
- H2 2: Strap vs slip-in construction
- H2 3: Fit and sizing
- H2 4: Material + ventilation

### 10. Goalkeeper accessories: caps, base layers (DRAFT v1, pending validation)

- H2 1: Use case (match conditions, training)
- H2 2: Material + features
- H2 3: Fit and sizing
- H2 4: Brand or team affiliation

### 11. Bags and backpacks (DRAFT v1, pending validation)

- H2 1: Capacity + use case (game day, training, travel)
- H2 2: Compartments and features
- H2 3: Material + durability
- H2 4: Team or brand affiliation

### 12. Socks (DRAFT v1, pending validation)

- H2 1: Team or league affiliation + design
- H2 2: Material + cushioning
- H2 3: Fit and sizing
- H2 4: Match vs training use

### 13. Accessories: scarves, hats, flags (DRAFT v1, pending validation)

- H2 1: Affiliation + design + cultural meaning
- H2 2: Construction + material
- H2 3: Use occasions (match day, fan zones, gift)
- H2 4: Sizing or display considerations

### 14. Equipment: cones, agility ladders, training aids (DRAFT v1, pending validation)

- H2 1: Training application + skill development focus
- H2 2: Construction + durability
- H2 3: Set composition + portability
- H2 4: Skill level + use case

### 15. Goalkeeper coaching gear (DRAFT v1, pending validation)

- H2 1: Training application + GK-specific drill compatibility
- H2 2: Material + durability
- H2 3: Set composition
- H2 4: Coaching context

## Internal links only on product pages

PDP copy includes internal links to ProSoccer collection or product pages ONLY. External links are forbidden on PDPs because:

- They leak link equity off-site during the purchase consideration window.
- They give the customer an exit ramp from the purchase decision.
- Authority signals through external links belong on homepage and blog content, not PDPs.

If body copy references external tournaments, events, or context (Asian Cup, Champions League, Premier League, etc.), keep the reference as plain text. Do not hyperlink to external sites. If the reference needs a destination, link to an internal ProSoccer page instead (e.g., a related collection).

This policy is product-page-specific. Collection pages may include external links per the collection-page playbook's link strategy.

## Internal link strategy

Same architecture as the collection-page playbook ('Internal link strategy' in `context/page-type-playbooks/collection-page-playbook.md`), adapted for product-page content. 1 to 2 internal links maximum in the long description body.

Link format: every internal link suggestion is a full HTTPS URL on the canonical domain `https://www.prosoccer.com` (with the `www` subdomain), never a relative path or `http://`. Full rule and examples: `context/workforce-conventions.md` 'Internal Link Format Discipline (added 2026-06-03)'.

### Selection rules

- Links derive from body content (the product's brand, the parent collection it sits in, related products in the same lineup, signature players the product is associated with).
- Topical relevance over keyword opportunism. The destination must serve the reader who's actively considering this purchase.
- All candidate URLs MUST be live-validated before inclusion (same Firecrawl scrape + status + content check as the collection-page playbook).
- **Prefer specific over generic when both validate.** When choosing between a brand-line collection (e.g. `/collections/adidas-predator`) and a brand-generic collection (e.g. `/collections/adidas-soccer-cleats`), the brand-line link wins because it serves a more committed buyer (someone already shopping the Predator line) and complements rather than duplicates the page's existing brand signals. Reserve the second link slot for a complementary discovery path (surface-category, related lineup, signature player) rather than a duplicate brand-discovery path. Mirrors the team-collection page pattern in `MEMORY.md` (`feedback_internal-link-selection-pattern.md`): prefer player-collection links to brand-line links when both validate.

### Live validation requirement

Identical to the collection-page playbook. Use the firecrawl skill (`firecrawl-scrape`) or `WebFetch` (MCP install pending; canonical install status in `context/workforce-conventions.md` 'Tool inventory'). Confirm `metadata.statusCode` is 200, confirm rendered content matches expectations (H1, product count, no soft-404 to homepage). Document failures inline.

### Optimal anchor text

Same rules as the collection-page playbook. 2 to 5 words, descriptive of destination, reads naturally in body sentence flow, no exact-match stuffing, varied across the site.

### Common patterns by product type

For team kit products (e.g., 2026 Mexico Home Authentic Jersey by adidas):

- **Collection link:** the team's collection page. E.g., `https://www.prosoccer.com/collections/mexico` (or `https://www.prosoccer.com/collections/mexico-soccer-jersey` post-rename), anchor `the Mexico collection` or `the full El Tri lineup`.
- **Brand link:** the brand's national-team-kit collection if relevant. E.g., `https://www.prosoccer.com/collections/adidas-soccer-jerseys`, anchor `Adidas's national team kits`.

For performance cleat products (e.g., Nike Mercurial Superfly 9 Elite FG):

- **Brand line collection:** the cleat's lineup. E.g., `https://www.prosoccer.com/collections/nike-mercurial`, anchor `the Mercurial lineup`.
- **Surface-type collection:** matched to the cleat's plate. E.g., `https://www.prosoccer.com/collections/firm-ground-cleats`, anchor `firm-ground cleats`.

For training apparel products (e.g., adidas Tiro 23 Training Pants):

- **Brand training collection:** E.g., `https://www.prosoccer.com/collections/adidas-training-apparel`, anchor `Adidas's training kit`.
- **Use-case collection:** E.g., `https://www.prosoccer.com/collections/training-pants`, anchor `the full training-pant lineup`.

### Brief format for surfacing link selections

Identical structure to the collection-page playbook. Embed inline; document below the body in an 'Internal links (1-2 max)' sub-section with URL, anchor text, body location, validation status (200 OK + fetched date + content-confirmation signal), and reasoning. Document any skipped failures with the specific reason and the alternative selected (or "none" if total stayed at 1-2).

## Brand IP Constraints

Hard legal constraint from `context/brand-ip-constraints.md` applies on every brief: FIFA-trademarked terminology family ("World Cup", "FIFA World Cup", "WC", "FIFA" in commercial contexts) is restricted to Adidas-licensed page contexts only.

Before writing copy:

1. Classify the page's brand-affiliation (Adidas-only / non-Adidas / brand-agnostic umbrella).
2. For non-Adidas pages, use Federation-anchored substitution language per `context/brand-ip-constraints.md`.
3. The year "2026" alone is permitted everywhere; the FIFA phrases are not.
4. Verify per-team brand-affiliation during topic research for national-team collection pages and product pages.

Run a final compliance scan across all six fields plus internal link anchors before voice check. Violations are higher-priority than voice violations because they create legal exposure.

## How this playbook integrates with the six copy-writing principles

Same integration order as the collection-page playbook:

1. Read this playbook. Confirm the product and brand subject lists.
2. Run topic research per the 'Required pre-write research' section above.
3. Apply the field-specific rules above to determine WHAT each field is about.
4. Apply the six copy-writing principles from `context/03-brand-voice.md` and `.claude/agents/on-page-seo/agent.md` Section 7 to determine HOW each field reads.
5. Run `voice_check.py` on the staged copy.
6. Self-verify per `.claude/agents/on-page-seo/agent.md` Section 11.

Conflicts between this playbook and a copy-writing principle (rare; the surfaces don't overlap much) escalate to ORIN.
