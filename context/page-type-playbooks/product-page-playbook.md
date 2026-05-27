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
- The brand. Signature elements, heritage, what distinguishes this brand from the alternatives the avatar is also considering. For an Adidas Predator product page, the Predator-line context belongs here. For a Nike Mercurial Superfly page, the Mercurial heritage belongs here.
- The product's place in the catalog and lineup. The 2026 home kit, not just "a Mexico jersey." The Mercurial Superfly 9 Elite, not just "a Nike cleat." The avatar wants to know which version of the product this is and what they're getting that other versions don't have.
- The avatar's emotional context for ownership. What does wearing or using this product mean to the avatar? Carlos buying the 2026 El Tri home authentic feels something different from Tyler buying the same kit. Same product, different emotional anchor.
- Fit, sizing, and care information where relevant. Product copy is a place where avatar pain frames map directly to copy that closes the sale. Jennifer's "Wide Foot Nightmare" frame, Carlos's "is this real or fake" frame, Tyler's "will it actually run faster than my last pair" frame.

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

- 2026 Mexico Home Authentic by Adidas: `Mexico 2026 Home Authentic Jersey by Adidas`
- Nike Mercurial Superfly 9 Elite: `Nike Mercurial Superfly 9 Elite FG Soccer Cleats`
- Adidas Tiro 23 Training Pants: `Adidas Tiro 23 Training Pants`

The product name appears in this field exactly the way the avatar searches for it. If the avatar searches for "Mexico 2026 home jersey," that's the framing. If the avatar searches for "Mercurial Superfly Elite," that's the framing.

### SEO Meta Title

Product head term first for SERP discovery. Brand and tier qualifiers follow.

- `Mexico 2026 Home Authentic Jersey | Adidas Player Edition`
- `Mercurial Superfly 9 Elite FG | Nike Pro Soccer Cleats`
- `Adidas Tiro 23 Training Pants | Slim-Fit Track Pant`

50 to 60 characters. Front-load the product name.

### SEO Meta Description

Speaks to the buyer (the avatar in purchase consideration), includes a CTA tied to the product. Anchored to the product's value, not to the store.

Product-anchored CTAs:

- `Lock in the 2026 home kit before kickoff`
- `Shop the cleat Mbappé wears`
- `Pick your Tiro fit`

Store-anchored CTAs (do not use):

- `Shop ProSoccer for the lowest price`
- `Order now for free shipping`

150 to 158 characters. Head term naturally placed in the first 100 characters.

### Short Description (intro paragraph or product blurb)

Emotion-first lead. The first sentence carries identity, moment, or feeling for the avatar buying this product. Per `context/03-brand-voice.md` 'Emotional Connection Over Feature Selling', features wait until sentence two or three.

40 to 80 words. Lives at the top of the description body. On Shopify, this is what appears above the fold on mobile, before the product variants and add-to-cart.

### Long Description (body copy)

Three to five H2 sections about the product and the brand. Topic-research outputs become the substance.

H2 patterns by product type:

- **Premium kit jersey:** brand and federation context, the design story for this kit, the player edition vs the fan edition, fit and sizing, kit history and why this version matters.
- **Performance cleat:** brand line context (Predator, Mercurial, Tiempo), this generation's design rationale, who wears it, fit and surface guidance, plate and stud configuration, who the cleat is for and isn't for.
- **Training apparel:** brand context, fabric and tech detail, where it fits in the avatar's wardrobe (training, travel, casual), fit and sizing, care.
- **Equipment (balls, bags, gloves):** brand line context, design and tech, who uses it, durability and care.

200 to 400 words across all H2s combined. Product pages run shorter than collection pages because the product variant selector and add-to-cart compete for attention; long body copy buries them.

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
Topic-research outputs: Adidas El Tri kit supplier since 1999; Heat.RDY weave on the player edition; player-edition tighter cut and heat-bonded badges; fan-edition softer fabric and standard fit; price gap typically $30 to $50; the 2026 home kit features a verde primary with Aztec patterning and FMF crest.

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

- Body copy is about the product and Adidas's design choices, not about the store.
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

Flyknit upper, lighter than the previous generation by about ten grams per boot. Air Zoom plate underneath for the energy return on the toe-off. Knit collar for ankle lock-in (the Superfly cut, vs the Vapor's lower collar). Heat-mapped traction stud pattern for cuts and turns.

## Superfly vs Vapor

Same upper, same plate, different collar. The Superfly's knit collar adds ankle support and locks the foot at the heel. The Vapor (sold separately) skips the collar for a couple of grams of weight savings and a lower-cut feel. Superfly for the player who wants the lock; Vapor for the player who wants the boot to feel barely there.

## Surface and Fit

Firm-ground plate. Natural grass and most well-maintained turf. For artificial grass, see the Superfly 9 Elite AG (sold separately); for older astroturf, the Superfly 9 Pro TF. The Elite tier runs narrow at the forefoot. Wide-foot players usually find the Tiempo or the Predator a better fit.

Sizes run true. Order your standard US cleat size if you've worn Mercurials before; if you're crossing over from a wider boot, consider half a size up.
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
Topic-research outputs: Tiro line launched in the 2000s as Adidas's training-pant franchise; signature three-stripe down the side; tapered slim-fit cut; AEROREADY moisture management; ankle zip; popular as both a training pant and a casual wear item; Tiro 23 is the current generation as of 2026.

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

### 1. National team jersey (validated: UAE v3, 2026-05-26)

- H2 1: Brand + design + federation identity ("The [Year] [Country] Soccer Jersey by [Brand]")
- H2 2: Edition tier comparison (Stadium vs Authentic, where applicable)
- H2 3: Fit and sizing
- H2 4: What you're buying into (cultural + tournament context + future catalyst)

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

For team kit products (e.g., 2026 Mexico Home Authentic Jersey by Adidas):

- **Collection link:** the team's collection page. E.g., `/collections/mexico` (or `/collections/mexico-soccer-jersey` post-rename), anchor `the Mexico collection` or `the full El Tri lineup`.
- **Brand link:** the brand's national-team-kit collection if relevant. E.g., `/collections/adidas-soccer-jerseys`, anchor `Adidas's national team kits`.

For performance cleat products (e.g., Nike Mercurial Superfly 9 Elite FG):

- **Brand line collection:** the cleat's lineup. E.g., `/collections/nike-mercurial`, anchor `the Mercurial lineup`.
- **Surface-type collection:** matched to the cleat's plate. E.g., `/collections/firm-ground-cleats`, anchor `firm-ground cleats`.

For training apparel products (e.g., Adidas Tiro 23 Training Pants):

- **Brand training collection:** E.g., `/collections/adidas-training-apparel`, anchor `Adidas's training kit`.
- **Use-case collection:** E.g., `/collections/training-pants`, anchor `the full training-pant lineup`.

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
