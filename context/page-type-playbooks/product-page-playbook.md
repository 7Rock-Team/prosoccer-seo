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

## Required pre-write research

Lighter than collection-page research because the topic is narrower (a specific SKU rather than an entire team or brand line). ORIN runs the research before SCRIBE writes; outputs land in SCRIBE's session briefing.

For any product page, ORIN researches:

- The brand's heritage and signature design elements relevant to this product. (Two to three Tavily queries.)
- The specific product's design rationale. What was the designer thinking? What problem does this version solve that the previous version didn't? What's new in this generation? (Two to four queries.)
- The product's place in the brand's lineup. Entry-level, mid-tier, premium, special edition, signature pro model. (One to two queries.)
- Who wears or uses this product. Pro athletes, demographics, occasions, surfaces. (Two to three queries.)
- The product's place in the avatar's purchase consideration set. What else is the avatar comparing this against? (Two to three queries.)

Six to twelve Tavily queries per product page is normal. Less if the product is a routine SKU in a known line (the third-pass on a Predator model the team has researched twice already). More if it's a flagship release the team hasn't researched before.

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

## Internal link strategy

Same architecture as the collection-page playbook ('Internal link strategy' in `context/page-type-playbooks/collection-page-playbook.md'), adapted for product-page content. 1 to 2 internal links maximum in the long description body.

### Selection rules

- Links derive from body content (the product's brand, the parent collection it sits in, related products in the same lineup, signature players the product is associated with).
- Topical relevance over keyword opportunism. The destination must serve the reader who's actively considering this purchase.
- All candidate URLs MUST be live-validated before inclusion (same Firecrawl scrape + status + content check as the collection-page playbook).

### Live validation requirement

Identical to the collection-page playbook. Use `mcp__firecrawl-mcp__firecrawl_scrape`, confirm `metadata.statusCode` is 200, confirm rendered content matches expectations (H1, product count, no soft-404 to homepage). Document failures inline.

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
