# Collection Page Playbook

_Page-type playbook for any URL under `/collections/*`. Read by SCRIBE on every collection-page brief, ahead of the six copy-writing principles in `context/03-brand-voice.md`. This playbook governs subject matter (what the page is ABOUT). The six principles govern execution quality (HOW the copy reads). Subject first, then voice._

## Subject focus

A collection page is ABOUT the collection's topic. The topic is the team, the player, the brand, or the category. The avatar landed here to learn about and feel connected to that topic. Every word in Title, Meta Title, Meta Description, Short Description, and Long Description serves the avatar's connection to the topic.

ProSoccer the store does not appear on a collection page beyond the Shopify chrome (header, footer, cart). Carlos opened `/collections/mexico` because he wants to feel his connection to El Tri. He didn't open it to read about the Pasadena fitting room or the Irwindale dispatch cutoff. The store is invisible inside the page body because Carlos didn't come for the store.

## Forbidden subjects on collection pages

The following are out of scope for collection-page copy. Any draft that includes them is on weak ground and gets rewritten:

- ProSoccer the store. No Pasadena retail mentions, no Irwindale warehouse mentions, no "30 years in business" framing, no "Why ProSoccer for X" sections.
- Store positioning, brand promotion, "what makes us different" content. The homepage handles store positioning. See `context/page-type-playbooks/homepage-playbook.md`.
- Store logistics. Shipping policies, return policies, fitting-room hours, dispatch cutoffs. These belong on `/pages/shipping`, `/pages/returns`, `/pages/locations`, the cart flow, and the checkout flow. They do not belong in collection-page body copy.
- Store-specific operational detail. Retail hours, store addresses, warehouse location, customer-service phone numbers. Same routing as logistics above.
- Generic e-commerce platitudes. "Shop our wide selection," "find what you need," "the best deals on X." This copy was forbidden anyway under the cognitive-load and human-not-AI rules in `context/03-brand-voice.md`, but flagging it again here because store-anchored copy tends to fall back on it.

## Required subjects on collection pages

The following are in scope and the body copy must serve them:

- The collection's topic in depth. History, culture, identity, key facts, current relevance. For a national team: founding, federation, kit history, signature players, tournament record. For a player: biography, club career, signature moments. For a brand category: brand heritage, signature products, who wears them. For a product category: what the category is, how it differs from adjacent categories, who uses it.
- The avatar's emotional connection to the topic. What does owning gear from this collection mean to the avatar's identity? Apply `context/03-brand-voice.md` 'Emotional Connection Over Feature Selling' to the topic specifically. Carlos's connection to El Tri runs through cultural diaspora, family memory, and matchday ritual; that's the well to draw from for a Mexico page.
- Topic-specific information the avatar's super-fans want to learn or be reminded of. Carlos knows the 2026 World Cup hosts. He may not remember the exact group draw or the kit-supplier history. Useful detail for a super-fan beats generic detail for a casual buyer.
- Product range explanation through the topic lens. "The 2026 home kit, the away kit, and the third drop before kickoff" is product-range explanation through the El Tri lens. "We carry a wide range of Mexico jerseys in many sizes" is product-range explanation through the store lens. The first belongs on the page; the second does not.

## Eligibility verification (Mike-pre-vetted at URL submission, updated 2026-05-29)

_Original codification 2026-05-27 placed eligibility detection in the agent layer via Firecrawl scrape. 2026-05-29 diagnostic on the Mexico Stadium SS PDP kit set confirmed storefront-rendered signals are systematically unreliable (see `context/workforce-conventions.md` 'Eligibility verification (Mike-pre-vetted at URL submission)' for full architectural learning). For collection pages: Mike pre-vetts in Shopify admin (collection populated, visible / indexed, sales channel active, sitemap presence per `deliverables/tracking/sitemap-state.md`) before submitting the URL. Agents skip Firecrawl-based detection. URLs supplied by Mike are assumed eligible unless Mike explicitly flags a strategic exception (e.g., seasonal empty collection). Brief audit trail captures eligibility status as "Mike-verified populated and visible at submission, [YYYY-MM-DD]" or "Mike-flagged [exception type] at submission, [YYYY-MM-DD]: [reasoning]." Strategic exception subsection (seasonal empty) below preserved as architectural concept; trigger is explicit Mike flag, not agent detection._

## Eligibility verification (legacy detection content, superseded 2026-05-29)

_Added 2026-05-27. Eligibility check is a gate, not an optimization step. Every collection-page candidate proposed for optimization must pass eligibility before any brief production begins. Optimization of empty, hidden, or redirecting collections is wasted SEO effort: the improved page can't carry traffic to product._

### Populated collection requirement

The collection page must surface real product cards. Detection method: Firecrawl scrape the candidate URL and confirm product cards are rendered.

Indicators:

- One or more product cards present in the rendered HTML = populated
- Empty product grid with "no products found" or equivalent message = empty
- Smart collection with an empty tag rule (no products currently match) = empty (e.g., `/collections/backyard-soccer-goals-and-rebounders` flagged in `work-log/follow-ups.md` 2026-05-08)

Empty collections do not qualify for optimization. Brief production cannot lift a page with nothing to sell.

### Visibility requirement

The collection page must be discoverable and indexable.

- Firecrawl scrape returns 200 OK with real collection content (not a soft-404, not a redirect to the homepage, not the empty-state landing).
- Collection appears in the public sitemap. Source of truth: `deliverables/tracking/sitemap-state.md`. Sitemap-absent collections need VERITAS investigation before optimization (see follow-ups 2026-05-08 reconciliation).
- Collection's `Online Store` sales channel is active in Shopify admin. Deferred automated check; correlates to sitemap presence.

### Default blocker behavior

If eligibility verification fails (empty collection, sitemap-absent collection, redirecting collection, hidden collection):

- ORIN candidate-selection phase: surface the ineligible candidate informationally with the eligibility issue flagged; default recommendations stay limited to eligible candidates; route the underlying VERITAS issue (sitemap gap, redirect anomaly) to the technical SEO log.
- SCRIBE Phase 1 capture: detect as BLOCKER and hold at gate. Mike decides: skip the collection, override with strategic reason, or escalate to VERITAS for fix-then-optimize sequencing.

### Strategic exception: temporarily empty seasonal collections

A small set of collections may be intentionally empty out of season (e.g., a "Black Friday Deals" collection in May, a "Champions League Final" collection between tournament cycles, a "Summer 2026 Headquarters" landing collection ahead of seasonal product drops). Optimizing these in advance is occasionally justified for SEO equity ahead of the product wave.

Default behavior: SKIP empty collections. Override requires Mike's explicit approval with clear seasonal reasoning. The override is rare; the default is the discipline.

### Cross-references

- ORIN candidate-selection workflow: `.claude/agents/master-strategist/agent.md` Section 9 'Candidate eligibility verification at Phase 1 surfacing'.
- SCRIBE pre-Phase-1 gate: `.claude/agents/on-page-seo/agent.md` Section 2 Step 0.5 'Eligibility verification'.
- Workforce convention: `context/workforce-conventions.md` 'Eligibility verification as logical extension of Step 0'.
- Product page eligibility (canonical, closing-window exception examples): `context/page-type-playbooks/product-page-playbook.md` 'Eligibility verification (mandatory pre-Phase-1)'.

## Production workflow note (added 2026-05-29)

Collection-page production runs under ORIN's batch parallel dispatch + single daily batch commit pattern as of 2026-05-29. Mike submits up to a 10-URL batch (eligibility pre-vetted in Shopify admin); ORIN auto-classifies tier (collection pages are Tier 2B); SCRIBE instances run in parallel alongside any PDP work in the same batch; ORIN batch-commits all briefs as a single daily commit; single push; Mike reviews at end-of-batch. Per-brief Mike gate review and per-brief commit cycle are replaced; all Tier 2B quality discipline stays intact. Full pattern: `context/workforce-conventions.md` 'Batch parallel dispatch + single daily batch commit'. ORIN procedural detail: `.claude/agents/master-strategist/agent.md` Section 9 'Batch parallel dispatch and single daily batch commit'.

## Tier 2B canonical workflow (added 2026-05-28)

Collection-page optimization runs as Tier 2B per the tiered workflow architecture (`context/workforce-conventions.md` 'Tiered workflow architecture (cross-cutting pattern)'). Tier 2B is full agent workflow scoped to six collection-specific fields, target ~15 to 20 min per page.

**Six fields optimized (codified 2026-05-28 per Refinement 1):**

1. **Title (H1):** visible heading on the collection page.
2. **Slug (URL handle):** typically unchanged unless current is suboptimal; preserve existing slugs to avoid redirect-cost risk and to keep PDP-to-collection internal-link integrity intact.
3. **Meta Title:** under 60 chars in field; NEVER include "ProSoccer" or brand variant (Hyper theme auto-appends " - ProSoccer" per Refinement 3).
4. **Meta Description:** ~150 to 158 chars desktop; primary keyword in first 100 chars.
5. **Short Description / hero block:** 50 to 80 words / ~300 to 450 chars; 3 to 4 sentences; emotion-first; avatar identity hook (per the updated 'Short Description (intro paragraph / hero block)' section below).
6. **Body Description:** the main body copy field on Shopify collection pages. Collection pages DO carry a body Description (NOT skipped despite the early Tier 2B draft suggesting otherwise). Carries 4 to 6 H2s per the existing 'Long Description (body copy)' section below.

**Six phases (all run regardless of page; per-phase scope flexes with topic complexity):**

1. **Phase 1 Current state capture (~3 min):** Firecrawl scrape collection page; extract the 6 fields above; capture current product count and any filter/sort UI context.
2. **Phase 1.5 Eligibility verification (~1 min):** apply 'Eligibility verification' section above; PASS / BLOCKER / strategic exception.
3. **Phase 2 Keyword research (~3 to 4 min):** apply year-specificity discipline + keyword distribution preparation (see 'Keyword distribution discipline' section below); DFS lookup for primary + supporting candidates; SERP ranking assessment.
4. **Phase 3 Topic research (~2 to 3 min):** scoped Tavily; currency check (squad / fixtures / manager / kit-supplier / cultural anchors); reuse same-day kit set briefings where available to avoid duplicate queries.
5. **Phase 4 Brief generation (~5 to 7 min):** output the 6 fields applying all codified rules (keyword distribution, FAQ conditional inclusion, brand IP, year-specificity). Apply the five canonical brief-craft rules where structurally applicable (Rule 2 'primary keyword in at least one H2' applies to body Description H2s).
6. **Phase 5 Voice check + gates (~1 min):** `scripts/voice_check.py` on both visible brief and workforce-internal briefing; 11 self-verification gates per SCRIBE Section 11 plus Gate 12 (keyword distribution) and Gate 13 (anti-stuffing), the 13-gate suite as of 2026-06-02. Gate 13 anti-stuffing self-revision happens in Phase 4 (brief generation) before this Phase 5 voice check.
7. **Phase 6 Internal link validation (~2 min):** validate 1 to 2 final selected links per 'Internal link strategy' section below; broader-catalog-destination preference per Refinement 1.

Voice consistent with the page-type playbook ecosystem and the avatar's emotional life from `context/04-customer-avatars.md`.

**Canonical reference: Mexico collection v5 (in production tonight as the first canonical Tier 2B brief under this codification).** v4 at commit `f3cac86` is the pre-codification sketch that surfaced the four refinements absorbed in this codification commit.

## Keyword distribution discipline (added 2026-05-28, codifies Refinement 4, collection 6-field adapted)

Keyword SELECTION (year-specificity rule per `context/page-type-playbooks/product-page-playbook.md` 'Primary keyword selection for year/generation/season-bound products') addresses which keyword becomes primary. At the collection-page level, the year-specificity rule inverts at head-term scope: collection pages aggregate product depth across an entire cycle and rank for broader head terms than PDPs, so the primary keyword may legitimately be the unbound head term (e.g., `mexico jersey`) with year-specific variants carried as supporting via natural body copy semantic variants. The selection-vs-deployment distinction still applies.

**Primary keyword placement (mandatory across the six collection fields):**

- **Title / H1:** exact match or close natural variant.
- **Meta Title:** exact match in field; under 60 chars; NO brand suffix in field.
- **Meta Description:** exact match or natural variant early in description (within first 100 chars).
- **Short Description:** exact match or natural variant in first sentence.
- **Slug:** exact match if creating new; preserve existing slug if optimizing existing page unless clearly suboptimal.
- **Body Description:** primary keyword in 2 to 3 H2 headings plus naturally in body copy 4 to 7 times (same range as PDP Long Description per Refinement 4).

**Supporting keyword placement (recommended):** body Description 2 to 4 times naturally per supporting variant; at least one H2 heading if the variant fits naturally; NOT in Meta Title (crowded with primary); NOT in Slug (URL stays clean); optional in Short Description if natural.

**Long-tail modifier placement (optional):** body Description especially in cultural-context H2; internal link anchor text where the modifier reads naturally.

**Forbidden: keyword stuffing.** Same rules as PDP version: no more than 7 primary mentions or 1% of word count whichever is lower; no forced H2 keywords; no consecutive sentence repetition; no primary keyword anchoring more than 1 internal link per brief.

**Natural variation allowed.** Variations count toward placement when semantic intent is clear.

**Verification:** SCRIBE Gate 12 checks all four sub-criteria. Failures surface as BLOCKER.

Cross-references: `context/page-type-playbooks/product-page-playbook.md` 'Keyword distribution discipline' (canonical PDP version), `.claude/agents/on-page-seo/agent.md` Section 9 'Keyword distribution discipline' (operational summary + Gate 12 definition).

## Anti-stuffing discipline (Gate 13, added 2026-06-02)

Collection pages are the page type most prone to comma-stacking because a collection aggregates multiple product categories by definition. The temptation is to list every category the collection holds inside the Title or Meta Title. That temptation is the failure mode this gate prevents. Gate 13 sits after Gate 12 in the gates suite (the suite runs 13 gates as of 2026-06-02). It is distinct from Gate 12 (which caps over-repetition of one keyword) and from the Gate 1 voice check (which governs prose voice and forbidden characters). Gate 13 governs the STRUCTURE of any single field so that no field reads as a comma-stacked keyword list. Distinct concerns, distinct gates.

The quality issue that surfaced this gate was a collection Title: `National Team Soccer Accessories: Scarves, Hats, Bags, Flags & Balls` (Day 2 batch #1 URL #2, flagged during Mike's Shopify admin implementation 2026-06-02). A comma-stacked keyword list reads as keyword stuffing to Google quality systems (Helpful Content Update, Spam Updates) regardless of whether each item is technically relevant to the collection, and it degrades user CTR in the SERP even at the same rank position.

**Core principle: product category breadth belongs in the body Description H2 framework and the hero / Long Description body copy, not in the Title or Meta Title fields.** A collection that holds scarves, hats, bags, flags, and balls names that breadth through its H2 sections and narrative, not by stacking the categories in a title-level field. Each output field should read as natural language a human would actually write.

### Anti-patterns to flag (any field)

1. **Comma-stacked keyword lists.** The format `[Topic]: keyword1, keyword2, keyword3 & keyword4` or `[Topic] - A, B, C, D` reads as stuffing regardless of relevance. Any field carrying 3+ comma-separated keywords fails.
2. **Ampersand-terminated lists.** A trailing `& [final keyword]` at the end of a comma list compounds the spam signal.
3. **Synonym stacking.** Treating synonyms (jerseys / shirts / kits / tops; cleats / boots / shoes) as variations to stack rather than picking one canonical term per field.
4. **Modifier stacking.** Stacking audience modifiers (Men's / Boys' / Youth / Kids') or product modifiers (Authentic / Replica / Stadium / Match-Worn) in a single field.
5. **Brand stacking (titles).** Listing multiple brands (adidas, Nike, Puma) in a title when only one or two are relevant to the collection.
6. **Price stacking (body copy).** Specific dollar amounts in collection-page body copy (added 2026-06-02). Collections are especially prone to this because they aggregate many products at many price points; the temptation is to enumerate them. Prices decay and belong in product cards and schema, not body prose.
7. **Brand stacking (body sentences).** Three or more comma-separated brand names in a single sentence within the Body Description (added 2026-06-02). The body-copy extension of anti-pattern 5; collections aggregate multiple brands, so the temptation to list them all in one sentence is high. Brand breadth belongs in product cards and faceted filters, not body prose.

### Stuffed vs natural

- STUFFED: `National Team Soccer Accessories: Scarves, Hats, Bags, Flags & Balls` -> NATURAL: `National Team Soccer Accessories` OR `2026 National Team Soccer Accessories`
- STUFFED: `Soccer Jerseys, Football Shirts, Kits & Tops` -> NATURAL: `Soccer Jerseys` OR `2026 National Team Soccer Jerseys`
- STUFFED: `Men's Boys' Youth Soccer Cleats` -> NATURAL: `Soccer Cleats` (audience breadth covered in body copy)

### Pricing discipline (body copy, added 2026-06-02)

Collection body copy must not contain specific dollar amounts. Use tier and positioning language instead. Collections are the page type most prone to price-stacking because they aggregate many products across many price points. This is part of the broader content evergreen-ness principle (`context/workforce-conventions.md` 'Content evergreen-ness'): prices decay fast (sales, retail adjustments, discontinuations), stale prices in body copy create user trust issues (body says $34.99, the PDP shows $39.99), prices carry no SEO ranking benefit for category-intent queries, and every price change otherwise ripples into a body-copy edit. Pricing belongs in PDPs, product cards, and Product schema, where Shopify auto-maintains accuracy.

Stuffed vs natural (the URL #1 pricing block, Day 2 batch #1):

- STUFFED: "Caps run around $34.99 across Mexico, Germany, Spain. Scarves run $24 to $44. Flags run $44.99; Mimi Imports country flags run $19.99. Bags land between $30 and $80." -> NATURAL: "Caps span the federation roster from everyday snapbacks to premium fitted silhouettes; scarves scale from match-day basics to collector-grade weaves; flags range from desk-size to wall-size; bags scale from compact carry to full match-day haulers."

Natural alternatives: tier and positioning language ("entry-level", "mid-tier", "premium", "collector"); comparative language ("scales from compact to wall-size", "ranges from everyday to match-day"); category breadth without specific numbers.

### Brand mention discipline (body copy, added 2026-06-02)

A body sentence must not carry 3+ comma-separated brand names. Stacked brand names read as brand keyword surfacing, not editorial narrative; brand breadth belongs in product cards and faceted filters. Individual brand mentions are fine when the narrative justifies the brand's role: one or two brands per sentence at most, each with role-specific context.

Stuffed vs natural (the URL #1 opening sentence, Day 2 batch #1):

- STUFFED: "adidas, Nike, Puma, Wincraft, Mimi Imports, Logo Brands, and Fan Ink each carry federation-licensed pieces." (7 comma-separated brands) -> NATURAL: "Federation-licensed pieces come from category leaders across apparel, accessories, and collectibles."
- NATURAL (narratively justified single/dual mention): "adidas covers cap silhouettes across the federation roster; Wincraft owns the wall-flag category."

### Gate 13 check criteria (per brief, across all output fields)

Fields in scope: Title, Meta Title, Meta Description, Short Description / hero block, Body Description (including H2s and H3s), internal link anchor text, FAQ questions and answers when included.

- No field contains a comma-stacked keyword list (3+ comma-separated keywords).
- No field contains an ampersand-terminated keyword list.
- No field stacks synonyms of the same concept (pick one canonical term per field).
- No field stacks modifiers redundantly.
- No title field stacks brands where only one or two are relevant.
- NEW (2026-06-02): No specific dollar amounts in collection body copy (use tier / positioning language).
- NEW (2026-06-02): No body sentence carries 3+ comma-separated brand names (brand mentions require narrative justification, one or two per sentence max).
- Each field reads as natural human-written prose.

FAIL = revise the field; PASS = the field clears. SCRIBE self-revises any failing field during Phase 4 (brief generation) before the Phase 5 voice check. ORIN re-checks at the orchestrator layer as defense-in-depth.

Cross-references: `context/page-type-playbooks/product-page-playbook.md` 'Anti-stuffing discipline (Gate 13, added 2026-06-02)' (canonical version), `.claude/agents/on-page-seo/agent.md` Section 11 Gate 13 + Section 9 'Anti-stuffing discipline', `.claude/agents/master-strategist/agent.md` Section 9 (ORIN defense-in-depth re-check), `context/workforce-conventions.md` 'Anti-stuffing discipline (Gate 13, cross-cutting)' + 'Content evergreen-ness' + 'Brand styling conventions'. Pricing discipline, body brand-mention discipline, and adidas brand styling (`context/workforce-conventions.md` 'Brand styling conventions': adidas is always lowercase, even at sentence start) are complementary disciplines all surfaced from the same Day 2 batch #1 review (2026-06-02).

## Five canonical brief-craft rules

These five rules govern every brief SCRIBE produces under the Fresh Optimization workflow. They emerged from the 2026-05-26 UAE PDP refinement session and lock in agency-grade craft standards across all future briefs. The five rules below are the NEW codification from this session; the collection-page external-link allowance (per link strategy) and the 1 to 2 internal-links target are already canonical in 'Internal link strategy' later in this playbook. Those existing policies stand; the five rules below extend them with the craft conventions that emerged from the UAE v3 work. Cross-referenced from `.claude/agents/on-page-seo/agent.md` Section 13 and `context/workforce-conventions.md`.

### Rule 1: Supporting keywords distributed as semantic variants in body

Each supporting keyword from the brief's Keyword research block appears 1 to 2 times in the Long Description, woven naturally as a semantic variant. The goal is topic depth signal, not keyword stuffing or exact-match density. A variant must read as natural English in its sentence; if a variant cannot land naturally, skip it rather than force the appearance. The primary keyword maintains 2 to 4 exact-match appearances across the body per the keyword-density guidance in `.claude/agents/on-page-seo/agent.md` Section 9 'Keyword placement per field'.

Worked example: UAE 2026 PDP v3 at `deliverables/page-optimizations/2026-05-26_session-01/uae-2026-home-stadium_brief-v3.md` distributes `uae football jersey`, `uae fa jersey`, `uae national team jersey`, and `uae football kit` across the body, each variant once or twice in natural reads. The same principle applies to collection-page bodies; the worked example is PDP-side because that's where the rule was codified, but it transfers cleanly to collection-page H2s.

### Rule 2: Primary keyword appears in at least one H2 header

Minimum one H2 in the Long Description contains the primary keyword or a close variant. The header signal carries SEO weight beyond body-text density. One natural integration is the floor, not the ceiling; don't force every H2 to carry the keyword. If the natural H2 framing cannot integrate the primary keyword, restructure the H2 rather than force the keyword into a clumsy heading.

Worked example: UAE 2026 PDP v3 first H2 reads "The 2026 UAE Soccer Jersey by adidas" (primary keyword plus brand qualifier as natural framing). Collection-page analogue: a Mexico collection page with primary keyword `mexico soccer jersey` could carry an H2 like "The Mexico Soccer Jersey across the El Tri Cycles."

### Rule 3: Meta description structure (commercial intent + trust signal + emotional CTA)

The Meta Description is structured in three parts:

1. **First sentence: commercial intent confirmation.** Primary keyword plus brand. Front-loaded for SERP-bold matching and immediate intent recognition.
2. **Middle: trust signal plus specific differentiator.** Trust words ("Official", "Certified", "Licensed") combined with one or two specific differentiators (federation design, signature technology, edition tier).
3. **Close: emotional or commercial CTA matching body voice.** The close should echo the avatar's emotional anchor from the body. The close must NOT duplicate the Short Description's close (per Rule 5); each field closes with its own punch.

**Tier-aware language for branded products.** Edition tiers on branded national-team and pro-line products are distinct words with specific commercial meaning. "Authentic" and "Stadium" are two different adidas national-team kit tiers (Authentic = match-spec construction; Stadium = Replica-tier). Combining tier words ("Authentic Stadium") reads as a contradiction to soccer-knowledgeable readers. Use "Official" plus the tier name as the trust-and-tier pattern: "Official Stadium home kit" rather than "Authentic Stadium home kit". The same principle applies to other brand-line tier conventions (e.g., Nike Mercurial's Elite vs Vapor tiers); verify the hierarchy in topic research before drafting.

Target length: 150 to 158 characters for desktop display, 130 to 140 for the mobile threshold.

Worked example: UAE 2026 PDP v3 Meta Description reads "The 2026 UAE Soccer Jersey by adidas. Official Stadium home kit with UAEFA federation design and Climacool weave. Wear what Al-Abyad wears." (139 chars).

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
3. 2 to 3 specific design or product details (PDPs) or topic specifics (collection pages) that differentiate from generic competitors.
4. Emotional or commercial CTA close, DIFFERENT from the Meta Description close. The Meta Description and Short Description must not duplicate the same closing line; each closes with its own punch.
5. Concise and scannable. The Short Description lives at the top of the description body and competes with adjacent UI elements (variant selector and add-to-cart on PDPs; product grid on collection pages) for attention.

Worked example: UAE 2026 PDP v3 Short Description reads "For the supporter whose flag carries red, white, black, and green. The 2026 UAE soccer jersey by adidas: clean white base, red V neck and shoulder stripes, sleeve patterning drawn from the federation's Arabic-script logomark. Climacool weave, doubleknit build." Avatar identity hook in sentence one. Primary keyword in sentence two. Three design details in sentence two. Technical close in sentence three, distinct from the Meta Description close.

## Required pre-write research

Either ORIN runs topic research before SCRIBE writes, or SCRIBE runs it natively as part of the dispatched workflow. Both patterns are now architecturally supported (sub-agents have native MCP access per the canonical `mcpServers:` configuration documented in `context/workforce-conventions.md` 'Sub-agent configuration discipline'). The choice is a workflow design call: ORIN-runs keeps research visible in the main session for Mike's review; SCRIBE-runs keeps the dispatched workflow self-contained. Topic research becomes the substantive backbone of the body copy. Without it, SCRIBE falls back on whatever the model already knows about the topic, which is usually generic and often stale.

For any collection page, ORIN researches:

- The topic's history. Team founding, federation history, player biography, brand origins, category evolution. Five to ten Tavily queries sized to the topic.
- Current cultural and competitive relevance. Current squad or roster, recent achievements, recent kit drops, upcoming tournaments, current brand catalog. Three to five Tavily queries.
- Identity markers. Colors, nicknames, traditions, anthem references, key moments fans reference, signature numbers (Maradona's 10, Messi's 10, Ronaldo's 7). Two to three queries.
- Avatar relationship to the topic. Cultural diaspora connections, fan rituals, identity expression, matchday traditions. Two to three queries.
- Current or upcoming events that anchor emotional urgency. Kit drops, tournaments, milestones, season openers. Two to three queries.

Tavily MCP is the default research tool. Five to fifteen queries per page is normal. Document key findings in SCRIBE's session briefing under `.claude/agents/on-page-seo/briefings/YYYY-MM-DD_<slug>.md`, not in the visible brief Mike reads. The visible brief shows finished copy only.

If the topic is one ORIN already knows deeply (e.g., a third pass at Mexico after running it twice), the research budget can shrink. Default posture is research first; trim only when the existing topic file in the briefing folder is fresh and complete.

## Field-specific rules

Six fields on a Shopify collection page. Each has a different optimization target.

### Title (Collection Title)

The visible H1 on the live collection page. Names the topic specifically. Avatar-search-language specificity is preserved here; the storefront Title doesn't have to lead with the head keyword the way the SEO Meta Title does.

- Mexico: `Mexico National Team Jerseys & El Tri Fan Gear`. Differentiates from Liga MX club content.
- Argentina: `Argentina National Team Jerseys & La Albiceleste Gear`. Differentiates from Argentine club content.
- adidas Predator: `Adidas Predator Boots, Cleats & Pro Edition Lineup`. Differentiates from generic "soccer cleats" browsing.

Per `.claude/agents/on-page-seo/agent.md` Section 9 'Keyword placement per field', the head keyword sits in the first three words. Brand prefix only when it adds trust.

### SEO Meta Title

Head-keyword-first for SERP discovery. Can be more generic than the storefront Title because the purpose is search ranking, not browsing differentiation.

**Brand suffix rule (codified 2026-05-28, Refinement 3 verified).** Hyper theme auto-appends " - ProSoccer" suffix to the Meta Title across ALL page types (collection pages confirmed via browser tab observation; PDPs confirmed same per Hyper theme default). **NEVER include "ProSoccer" or any brand variant in the Meta Title field.** Including it creates double-branding in SERP display ("Title text | ProSoccer - ProSoccer"). The full 60-char field budget is available for keyword + positioning content.

Examples (post-codification, no brand suffix in field):

- Mexico: `Mexico Jersey & El Tri 2026 World Cup Gear` (42 chars in field; theme renders to ~55 chars SERP display).
- Argentina: `Argentina Jersey & La Albiceleste 2026 World Cup Kit` (52 chars in field; theme renders to ~65 chars SERP display, slight over but acceptable).
- adidas Predator: `Adidas Predator Cleats | Pro Edition & Elite Models` (51 chars in field; theme renders to ~64 chars SERP display).

50 to 60 characters in field. Front-load the head keyword in the first 30 characters. Mobile cuts around 40 characters; the value-prop sits before that line.

### SEO Meta Description

Speaks to the avatar (the fan), not to the store, and includes a call-to-action that earns the click. Topic-anchored, never store-anchored. The CTA names something the avatar actually wants to do on this page.

Topic-anchored CTAs:

- `Shop the 2026 home kit`
- `Find your El Tri size`
- `Get the 2026 drops first`
- `Pick the player edition or the fan cut`

Store-anchored CTAs (do not use):

- `Shop ProSoccer for the best deals`
- `Find your favorite at our store`
- `Browse our wide selection`

150 to 158 characters desktop. The head keyword sits naturally in the first 100 characters (Google bolds the match). Don't repeat the title verbatim.

### Short Description (intro paragraph / hero block)

Emotion-first lead about the topic and what it means to the avatar. Per `context/03-brand-voice.md` 'Emotional Connection Over Feature Selling', the first sentence carries feeling, identity, or moment. Features and product detail come in supporting sentences if at all. By the end of the first paragraph the avatar should feel seen as a fan of the topic.

**Target range (codified 2026-05-28, Refinement 1):** 50 to 80 words / approximately 300 to 450 characters. Three to four sentences. Does not name the store. Does not name shipping, returns, or retail locations. This range supersedes the earlier draft Tier 2B sketch (200 to 350 chars) which was a tighter PDP-Rule-5-derived target that didn't carry enough narrative depth for the collection-page hero-block role. The 50 to 80 word range aligns with this playbook's longstanding Short Description spec and produces stronger hero copy.

### Long Description (body copy)

Four to six H2 sections about the TOPIC, not the store. The topic research from the pre-write step becomes the substance here. 200 to 500 words across all H2 sections combined (Shopify scrolls a long body cleanly; over 500 words tends to bury the products on mobile).

H2 patterns by collection type (these are starting frames, not rigid templates; topic research dictates the actual H2s):

- **National team:** team history, current squad, kit history and design, cultural significance to fans, what the next major tournament means, key players to watch.
- **Player:** biography, career arc, signature moments, current season, what their gear means to fans, kit and boot lineage.
- **Brand category (e.g., adidas Predator):** brand heritage, signature design elements, who wears them and why, model lineage (gen-by-gen evolution), current top model, who the line is for.
- **Product category (e.g., goalkeeper gloves):** what the category is and isn't, how to choose, who plays in this category, signature brands and models, fit and care basics.

Each H2 should pass the lift test from `.claude/agents/on-page-seo/agent.md` Section 11 Gate 9. If the section could appear unchanged on Soccer.com or any generic retailer's site, it lacks topic depth and gets rewritten.

Per `.claude/agents/on-page-seo/agent.md` Section 9 'Keyword placement per field', long-tail variants belong inside the H2 wording naturally (not "Mexico Jersey FAQs" but "What the 2026 El Tri Home Kit Means for the Diaspora" or similar).

### FAQ section (conditional inclusion, codified 2026-05-28, Refinement 2)

**FAQ is conditional inclusion, NOT a template requirement.** The deciding question is NOT "do buyers ask questions about this collection" but "do buyers ask questions that the Long Description body copy does not already answer."

**FAQ EARNS its place ONLY when all three criteria are met:**

1. Real buyer questions exist with search-volume signal (verified via DataForSEO or known query patterns).
2. Those questions are NOT addressed in body copy already (substantive narrative coverage in H2s defaults to NO need for FAQ rephrasing).
3. Adding them as FAQ creates net-new value, not repetition.

**Examples where FAQ MIGHT earn inclusion:** return policy specifics not in body, sizing comparison across brands not in body, fixture / schedule specifics for date-bound tournament gear, customization availability questions.

**Examples where FAQ should NOT be added:**

- "What is the X jersey?" (covered in H1 + body H2 1).
- "Who makes the X jersey?" (covered in body H2 1).
- "When does X play?" (covered in body H2 4 cultural-context / catalyst section).
- "What's the difference between the player and fan version?" (covered in body H2 2 edition tier comparison).

**Default behavior: SKIP FAQ unless the three criteria are clearly met.** Don't add FAQ as template requirement. When YES: 3 to 5 questions max (revised down from prior "5 to 7 standard range"), each answer 2 to 4 sentences. Schema attaches via VERITAS's FAQPage injection.

**Forbidden FAQ questions** (these belong on store-policy pages, not on collection pages):

- "What's your return policy?"
- "How long does shipping take?"
- "Do you have a fitting room?"
- "Can I exchange a jersey?"

## Evergreen body, contained catalyst

Long description body must be predominantly evergreen: topic identity, history, kit lineage, cultural significance, player eras across history, brand-supplier history. Evergreen content survives across catalyst cycles (World Cup, season transitions, kit drops) without requiring page rewrites.

Time-sensitive content is allowed but must be contained to ONE clearly-framed catalyst H2 section, ideally labeled with current-cycle framing (e.g., `## Current Tournament: El Tri at the 2026 World Cup` rather than `## El Tri at the 2026 World Cup`). When the catalyst passes, ONLY that section needs updating; the rest of the page persists.

Approximate structure: 5 evergreen H2 sections + 1 contained catalyst section per collection page. Adjust per topic; sole rule is the page must remain useful 12+ months after publication without major rewrites.

The catalyst section is the place to name the current tournament, the current kit drop, the current squad-naming cycle, the current friendly schedule. Everything else (kit design tradition, color identity, players past-and-present, brand-supplier sequence, cultural diaspora context) holds across cycles.

## Internal link strategy

The long description supports 1 to 2 internal links maximum. More than that turns the body into a navigation menu and dilutes topical authority. Fewer than that leaves the page orphaned in the site's link graph.

### Selection rules

- Link candidates derive from body content (named entities, brands, players, related teams mentioned naturally in the topic substance). The link should serve a reader who's already engaged with the topic, not a reader the page is trying to redirect.
- Topical relevance over keyword opportunism. The destination must genuinely deepen the topic.
- All candidate URLs MUST be live-validated before inclusion (see Live validation requirement below).

**Broader-catalog-destination preference (codified 2026-05-28, Refinement 1).** When PDPs link to the collection page (the established pattern, e.g., kit-set PDPs all link to `/collections/<team>`), the collection's body links should prefer broader catalog destinations (umbrella collections like `/collections/adidas-2026-fifa-world-cup-soccer-jerseys-gear`, brand collections, category collections) rather than reciprocal kit set PDP routing. Reciprocal collection-to-PDP-back-to-collection routing splits equity and duplicates the grid-level surfacing already on the live page.

**Named-entity-anchor exception:** when a specific PDP carries a unique narrative anchor that ties directly to the body copy (the Mexico Third + adidas Archive in Germany narrative example, applied in Mexico collection v4 commit f3cac86 and Mexico collection v5 onward), include the PDP as a secondary body link with named-entity anchor tied to the narrative. The unique narrative tie justifies the reciprocal routing.

**Visible brief format: minimal (codified 2026-05-28).** The visible brief's `Internal links:` sub-section lists only URL + anchor text + body location. NO validation metadata (no "200 OK validated DATE via Firecrawl" boilerplate, no H1 quotes, no product counts, no destination page descriptions). The full validation audit trail (status code, H1 / product count verification, soft-404 check, per-candidate failure reasons for skipped links) lives in the workforce-internal session briefing under `.claude/agents/on-page-seo/briefings/YYYY-MM-DD_<slug>.md`. Per SCRIBE agent.md Section 9 'Internal link selection workflow' step 6: "Document final selections in the brief's Internal links sub-section per the minimal template format. Skipped failures and per-candidate failure reasons live in the workforce-internal briefing, not in the visible brief." This rule applies to all brief tiers (1, 2A, 2B); the visible brief stays paste-ready and one-page for Mike's review while the audit trail stays complete in the workforce briefing.

### Live validation requirement

`deliverables/tracking/sitemap-state.md` confirms a URL is registered in the public sitemap. It does NOT confirm the URL returns the expected live page. Pages can be silently unpublished, set to draft, redirected, blocked by metafield, or returning soft-404s (homepage-instead-of-error, as found in 2026-05-08 404 remediation work).

For each internal link candidate, run live validation:

1. Fetch the URL using the firecrawl skill (`firecrawl-scrape` for the single-URL path; canonical install status for `mcp__firecrawl-mcp__firecrawl_scrape` in `context/workforce-conventions.md` 'Tool inventory'). Fall back to `WebFetch` for lighter reads when the skill overhead is excessive. Once the Firecrawl MCP is installed, prefer the MCP tool call over the skill.
2. Confirm HTTP status is 200 OK in the response metadata (not 301 / 302 redirect, not 404, not 410, not 5xx). Both the firecrawl skill and the Firecrawl MCP return `metadata.statusCode` for the resolved URL; WebFetch surfaces the same via response headers.
3. Confirm the rendered page content matches expectations. Check the H1 / page title, the product count if it's a collection, and that the URL did not silently land on the homepage. A `/collections/adidas` link that returns the homepage is a soft-404, not a live link.
4. If validation fails: log the failure inline in the brief's Internal links sub-section with the specific failure reason, then select an alternative candidate or skip the link.

A link that fails live validation is worse than no link. Broken or unexpected internal links signal to Google that the site has crawl-health issues and to users that they're being misdirected.

### Optimal anchor text

For each validated link, propose explicit anchor text. Best practices:

- 2 to 5 words (longer reads unnatural; shorter lacks context).
- Descriptive of the destination (signals to the reader what the linked page is about).
- Reads naturally in body sentence flow (not jammed in awkwardly).
- Topical relevance to the destination without exact-match keyword stuffing.
- Varies across the site. Don't reuse identical anchor text from every page linking to the same destination.

Bad anchor text:

- `click here` (no signal)
- `Mexico jersey` on a link from a Mexico-related page targeting `mexico jersey` head term (exact-match stuffing)
- `the page about Adidas Mexico jerseys with the Aztec design` (too long, unnatural)

Good anchor text:

- `Adidas national team kits` (descriptive, 4 words, contextual)
- `every other national team` (natural sentence flow, 4 words)
- `the full Predator lineup` (specific destination, 4 words)

### Common patterns by collection type

For team collection pages (Mexico, Argentina, Brazil):

- **Brand link:** kit supplier's collection if mentioned in body. E.g., `/collections/adidas-soccer-jerseys`, anchor `Adidas's national team kits` or `Adidas's federation roster`.
- **Adjacent topic link:** parent national-teams collection (`/collections/national-teams`) or a mentioned related team.
- **Player link:** if a specific player with their own collection is featured prominently in the body. E.g., `/collections/hirving-lozano` from a Mexico body that names Lozano in the Players sub-section.

For player collection pages (Messi, Ronaldo):

- **Team link:** the player's national team collection.
- **Brand link:** the player's signature boot or kit brand collection.
- **Era / tournament link:** relevant historical context collection if one exists.

For brand category collection pages (adidas Predator, Nike Mercurial):

- **Parent brand collection.**
- **Prominent player collection** if featured.
- **Adjacent product category collection.**

### Brief format for surfacing link selections

Embed each validated link inline in the body at its natural anchor point. Below the body copy (after the FAQ sub-block), add a sub-section listing the selections with validation status:

```
## Internal links (1-2 max)

1. **URL:** /collections/<slug>
   - **Anchor text:** <exact phrase used in body>
   - **Body location:** <section name where the link appears>
   - **Validation:** 200 OK / fetched <date> / content confirmed (<H1 of destination> / <product count> / <other observed signal>)
   - **Reasoning:** <why this link, why this anchor>

2. **URL:** /collections/<slug>
   - **Anchor text:** <exact phrase used in body>
   - **Body location:** <section name>
   - **Validation:** 200 OK / fetched <date> / content confirmed
   - **Reasoning:** <why this link, why this anchor>
```

If a candidate failed validation, document the failure inline so the audit trail is visible:

```
## Skipped link (validation failure)

- **URL:** /collections/<slug>
- **Failure:** 404 Not Found / 301 redirect to /collections/<other> / soft-404 returns homepage / <other>
- **Alternative selected:** <URL of the link that took its place>, OR none (skipped to keep total at 1-2)
```

## Worked example 1: National team collection (Mexico template)

URL: `/collections/mexico`
Primary avatar: Carlos
Topic-research outputs: El Tri founded 1927; FMF; current head coach; 2026 World Cup co-host; Estadio Azteca opener June 11 2026; recent kit history (1986, 1994, 1998, 2010, 2014, 2018, 2022, 2026); diaspora identity in LA; adidas as kit supplier since 1999.

_The H2 names below reflect the 'Evergreen body, contained catalyst' rule above (1 catalyst + 5 evergreen). Body excerpts are abbreviated to show topic substance per heading; for the full applied example with body content fully matched to evergreen-plus-catalyst structure, see `deliverables/page-optimizations/2026-05-08_mexico-v3.md`._

```
Title (Collection Title)
Mexico National Team Jerseys & El Tri Fan Gear

SEO Meta Title
Mexico Jersey & El Tri Gear 2026 World Cup Kit
[57 chars]

SEO Meta Description
The 2026 El Tri home kit, the away, and the player and fan cuts. Authentic Adidas Mexico jerseys for the diaspora that bleeds verde, blanco, y rojo. Shop the kit.
[157 chars]

Short Description
El Tri opens the 2026 World Cup at Estadio Azteca on June 11. Mexico is the country LA's diaspora carries on its back every four years, and the kit is how that identity walks down the street. Wear what they wear.

Long Description (H2 sections, topic-anchored, no store mentions in body):

## Current Tournament: El Tri at the 2026 World Cup

Mexico co-hosts with the US and Canada. The opener is at Estadio Azteca, the same stadium that hosted the 1970 and 1986 finals. No other country has hosted three Men's World Cups. The squad mixes Liga MX core with Europe-based players: Edson Alvarez, Hirving Lozano, Cesar Montes, Santi Gimenez, Luis Romo. Group draw lands in December 2025.

## The Aztec Coding Tradition: Mexico's Kit Design Heritage

Adidas keeps the verde primary with a Aztec-coded pattern across the chest and a darker green panel along the shoulders. The crest is centered traditional FMF style. Player version uses Adidas Heat.RDY weave with the closer cut Hugo Sanchez wore in '94 and the squad wears today. Fan version uses softer fabric and a regular fit. Both carry the official tags and holographic.

## The Verde, Blanco, y Rojo

The colors are the flag. The eagle on the crest is from the Mexican coat of arms. Green for hope, white for unity, red for the blood of the nation. Every kit since 1968 has held those colors as primary, with the away alternating in white through most eras and once in red ('98). The 2026 third kit, expected closer to the tournament, traditionally lets Adidas experiment with the deep red or a black variant.

## Players Who've Worn the Green: Past and Present

Lozano on the wing for pace and pocket runs. Alvarez in the double pivot, the squad's metronome. Santi Gimenez at striker after his Feyenoord move and now Milan time. Cesar Montes in the back, leading the line out from the back. The wildcard is Marcelo Flores, the dual-eligible Arsenal academy product who chose El Tri.

## Kit History from 1994 to 2026

The 1994 kit (Aztec-pattern home, the bright red away) is the diaspora's favorite. The 1998 home was a clean green with the eagle large across the chest. 2006 and 2010 went black-trim minimalist. 2014 ran a deep red away. 2018 and 2022 leaned modern with thinner crest panels. 2026 is being read as a return-to-tradition design.

## Why El Tri Means More in LA

LA County has more Mexican-Americans than any city outside Mexico City. Estadio Azteca is a six-hour flight; Pasadena's Rose Bowl has hosted El Tri friendlies for forty years. When Mexico plays the US in Pasadena, the green in the stands isn't an away crowd. It's the home crowd. The kit isn't fan merch; it's a flag a quarter of the city wears in shifts.

(FAQ follows as a separate section)
```

Annotation:

- The Long Description never names ProSoccer, Pasadena retail, Irwindale warehouse, or any store-positioning element.
- Every H2 is about Mexico, not about the store.
- Topic-research outputs are visible: founding date, kit-supplier history, current squad, kit history by tournament, cultural diaspora data.
- The avatar (Carlos) is anchored throughout: diaspora identity, matchday ritual, the flag-as-kit framing.
- The lift test (Gate 9) passes: this body copy could not appear unchanged on Soccer.com because it commits to a specific cultural angle Soccer.com avoids.
- Voice rules: no forbidden words, no em-dashes, contractions used, varied sentence lengths, specifics throughout (player names, years, kit details).

## Worked example 2: Player collection (Messi template)

URL: `/collections/lionel-messi-jersey`
Primary avatar: Carlos secondary; Tyler primary if URL emphasizes performance kit; for an Inter Miami fan-jersey URL, Carlos is primary.
Topic-research outputs: Messi born 1987 Rosario; Barcelona 2004 to 2021; PSG 2021 to 2023; Inter Miami 2023 to present; 2022 World Cup winner; eight Ballons d'Or; Argentina cap leader; signature 10; current Inter Miami #10 home and away kits; recent Messi-edition adidas Predator and F50.

```
Title (Collection Title)
Lionel Messi Jerseys & Argentina + Inter Miami Kits

SEO Meta Title
Messi Jersey | Inter Miami #10, Argentina, Barcelona Kits
[58 chars]

Short Description
Messi turned the #10 into a verb. The kits in this collection trace the arc: Argentina's albiceleste from the 2014 final to the 2022 trophy lift, the Inter Miami pink that's redefining MLS, and the Barcelona blaugrana that started it. The same name on the back, in five different colors of his career.

Long Description (H2 sections):

## The 2022 World Cup Final and What the Albiceleste Means Now

Messi lifted the trophy in Lusail on December 18, 2022. The final he'd lost in 2014, in extra time on the same continent, eight years on. The albiceleste he wore that night is the one fans want. The current Argentina home kit carries the three-stars detail above the crest, one for each World Cup, the third earned in Qatar.

## The Inter Miami Era

He chose Miami in summer 2023 over a Saudi offer that would've paid more than every European league combined. Pink and black is a kit no one else in MLS owns the visual of. The #10 home and the black away are the bestselling MLS kits of the modern era. Apple TV broadcasts every match.

## Barcelona, the Beginning

Messi joined La Masia at 13. He debuted for the first team in 2004. By 2009 he was the best player alive. The Barcelona kits across his run, the Qatar Foundation chest in '12, the Rakuten chest in '17, the blaugrana stripes that don't change much except in their accents, are the kits older Messi fans associate with him most.

## What Makes a Messi Kit a Messi Kit

Number 10 on the back. The name in the federation or club font. For Argentina that's the AFA blocky font; for Inter Miami it's the cleaner sans-serif Adidas designed for the league. The crest matters: AFA with the three stars, Inter Miami with the heron silhouette, Barcelona with the cross of Saint George. Authentic kits carry the Adidas climacool or Heat.RDY tech (Argentina, Barcelona) or the league-issued tech (Inter Miami).

## The Boots He Wore

Adidas across his career. The F50 era in his early Barcelona run. The Nemeziz he was the face of from 2017 to 2023. The Adizero F50 since the 2024 relaunch. Each generation tied to a chapter of his career; collectors usually pick by chapter, not by what's current.
```

Annotation:

- Every H2 is about Messi, not about the store.
- Topic-research outputs are visible throughout: the 2022 final detail, the Inter Miami move detail, the boot-generation history.
- Avatar (Carlos primary) anchors the diaspora and matchday emotional language; Tyler shows up in the boot-generation H2 because that's where performance-kit buyers think.
- The body works for Argentina, Barcelona, and Inter Miami fans simultaneously without diluting any of them.
- Lift test passes: the specifics (Lusail 2022, the Saudi-offer detail, the Heat.RDY vs league-tech distinction) commit to angles a generic retailer would avoid.

## Worked example 3: Brand category collection (adidas Predator template)

URL: `/collections/adidas-predator`
Primary avatar: Tyler (performance buyer)
Secondary avatar: Carlos (collector)
Topic-research outputs: Predator launched 1994 by Craig Johnston; Beckham era; Zidane wore them; controlled-shot rubber elements; relaunched as Predator Accuracy in 2023; Predator 24 Elite is the current top model; the line has gone through seven generations; key signature pros wearing them now (Bellingham, Pedri, Rice).

```
Title (Collection Title)
Adidas Predator Boots, Cleats & Pro Edition Lineup

SEO Meta Title
Adidas Predator Cleats | Pro Edition, Elite & 24 Models
[55 chars]

Short Description
The Predator is the boot Beckham wore for England, Zidane wore for the Real treble, Rice wears for Arsenal now. Thirty years of controlled-shot rubber, redesigned every generation, still the boot for the player who wants the ball to do exactly what they tell it to.

Long Description:

## The Predator Story, 1994 to Now

Craig Johnston, the former Liverpool winger, designed the original in 1994 with rubber strips on the upper to give the ball more spin and control. Adidas bought the design and launched it that year. The Mania era ran through the early 2000s. The Pulse, the Powerswerve, the X, the Predator 18 with the laceless upper, the Accuracy in 2023, and now the Predator 24. Every generation a different take on the same idea: more control, more curve, more shot.

## Who Wears Them Now

Jude Bellingham at Real Madrid. Declan Rice at Arsenal. Pedri at Barcelona. Trent Alexander-Arnold for the long-range crossfield ball that bends like a Predator boot is supposed to make it bend. The Predator is the boot for the midfielder who runs the game with the ball more than the leg.

## Predator 24 Elite vs Predator 24 League

Elite is the pro tier: K-leather upper, knit collar, lighter chassis, stiffer plate. League is the same silhouette and rubber-element design at a lower price, with synthetic upper and a softer plate. Elite for the player who needs the touch at the top level. League for the club player who wants the look and most of the feel without the pro-tier cost.

## Why the Rubber Elements Matter

The rubber strips on the front of the boot grip the ball at impact. More grip means more spin on a struck ball, which means more curve. It's not magic; it's friction. Free-kick takers love them. Long-range passers love them. Strikers who want a controlled-finish over a power-finish prefer them to the F50 or the Mania.

## The Predator at Different Surfaces

Firm ground for natural grass. Artificial grass for the green-plastic surface. Turf for older astroturf. The Predator runs across all three. Pick the plate to match the surface; the upper and the rubber-element design stay the same across the line.
```

Annotation:

- Body copy is about Predator the boot line, not about ProSoccer the store.
- Topic-research outputs visible: launch year, designer, signature pros, generation history, current models.
- Tyler primary: performance specifics, plate-and-surface detail, pro-tier vs league-tier comparison.
- Carlos secondary lands at the generation history (collectors care about which generation a player wore).
- Lift test passes: a Soccer.com page on Predator would avoid the Craig Johnston detail and stay closer to "the Predator is a great boot for control." This page commits.

## Brand IP Constraints

Hard legal constraint from `context/brand-ip-constraints.md` applies on every brief: FIFA-trademarked terminology family ("World Cup", "FIFA World Cup", "WC", "FIFA" in commercial contexts) is restricted to Adidas-licensed page contexts only.

Before writing copy:

1. Classify the page's brand-affiliation (Adidas-only / non-Adidas / brand-agnostic umbrella).
2. For non-Adidas pages, use Federation-anchored substitution language per `context/brand-ip-constraints.md`.
3. The year "2026" alone is permitted everywhere; the FIFA phrases are not.
4. Verify per-team brand-affiliation during topic research for national-team collection pages.

Run a final compliance scan across all six fields plus internal link anchors before voice check. Violations are higher-priority than voice violations because they create legal exposure.

## How this playbook integrates with the six copy-writing principles

The playbook governs subject matter. The six copy-writing principles in `context/03-brand-voice.md` and `.claude/agents/on-page-seo/agent.md` Section 7 govern execution quality. The order is:

1. Read this playbook. Confirm the page's topic and the forbidden / required subject lists.
2. Run topic research per the 'Required pre-write research' section above.
3. Apply the field-specific rules above to determine WHAT each field is about.
4. Apply the six copy-writing principles to determine HOW each field reads:
   - The "Human, Not AI" Test (rhythm, openers, transitions, closings)
   - Cognitive Load Minimization (lead with the noun, one idea per sentence, scannable specifics)
   - Emotional Connection Over Feature Selling (emotion before feature, avatar-anchored hook, show-them-what-they'll-feel test)
   - Full-Avatar-Scope Discipline (primary, secondary, excluded, cross-avatar landing)
   - Business Context Anchor (the four positioning claims from `context/00-business-overview.md`)
   - Keyword Placement per Field (the table in `.claude/agents/on-page-seo/agent.md` Section 9)
5. Run `voice_check.py` on the staged copy.
6. Self-verify per `.claude/agents/on-page-seo/agent.md` Section 11.

If the playbook and a principle ever conflict (rare; the principles are voice-and-rhythm rules, and the playbook is subject-matter rules, so the surfaces don't overlap much), surface to ORIN before resolving.
