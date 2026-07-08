# SCRIBE audit -- HQ2329-001 Nike Phantom 6 High Elite AG Shadow FA26

Batch 6 Wave 2, Tier 2A (mirror #7 HJ2147 structure, own prose). Dispatched by ORIN 2026-07-08. HOLD AT GATE for Checkpoint 3.

## Phase 0 scrape (scrape-wins, mandatory)
- Firecrawl scrape 2026-07-08, statusCode 200, healthy PDP. creditsUsed 1.
- Colorway confirmed: Black/Black/Illusion Green, "Shadow Pack (FA26)". (Sibling swatch "Multi-Color/Black" links to the IQ1869 Breakout twin -- confirms the anti-convergence pairing.)
- Plate/surface confirmed: AG-Pro, "For use on longer, artificial-grass surfaces." Conical studs. (Differentiator vs #7 FG.)
- Upper: Nike Gripknit, sticky texture, equal grip wet/dry.
- Collar: Dynamic Fit collar, soft/stretchy Flyknit. High cut confirmed.
- Frame: new shoe frame, natural fit in toe box, closer to ball.
- Lacing: Ghost Lacing (covers laces once tied).
- Sockliner: cushioned.
- Style HQ2329-001. Tier High Elite. Price $284.99. 1 in stock (Mike-verified eligible at submission; new-arrival SKU).
- NO stud count claimed (playbook honored; scrape gives none).
- No fabrication: every spec above is scrape-sourced. Dispatch hypotheses (Gripknit, AG-Pro, Dynamic Fit collar) all confirmed by scrape, so no override needed.

## Facet / lane (spec #10)
- Distinct facet applied: the ELUSIVE CUT ON TURF. Elusiveness/disguise on artificial grass under lights; the turf player the marker cannot track. Leans elusiveness, NOT lockdown/support.
- Primary metaphor: the elusive turn on the turf, lost in the lights ("chasing a shadow", "the turn he never tracks", "go unseen").
- Opening hook: the plant-and-go where you are gone before the defender's studs reset.

## Anti-convergence verification
- vs HJ2147 (exemplar, #7): did NOT read the HJ2147 brief (prose-propagation forbidden). Wrote around forbidden hook family ("shape one way, play the other" / "the shadow the defense loses"), its H2 titles, its disguise-of-the-pass metaphor, and its closing line. My facet is the cut/movement on turf, not the pass/finish on firm ground.
- vs IQ1869 (Breakout twin, prior batch): CRITICAL bar honored. NO "armor at the ankle / fortress at the joint" support metaphor -- collar is framed as "wrapped/locked/natural feel through turns" (part of the elusive-turn story), not as protective armor. NO "week spent on the turf, committing to every plant" hook -- my hook is the vanishing cut, and the collar/ankle is a control detail, not a lockdown thesis. This SKU is elusiveness, not IQ1869's lockdown/support.
- vs IQ1870 (Low Elite AG, "surface-matched specialist"): shares AG surface but differs by cut (High) and by thesis (elusiveness/disguise, not surface-matched-specialist framing).

## Keyword distribution (Gate 12)
- Primary: `nike phantom 6 high elite ag shadow` (pack-specific, surge-based; cedes bare `nike phantom 6 high elite ag` to the shipped IQ1869 Breakout twin per dispatch). Appears: Title, Meta Title, Meta Description (early), Short Desc (natural variant), Description H2 ("Product Details: Phantom 6 High Elite AG") + body ~5x across natural variants (Phantom 6 High Elite AG / Phantom 6 High Elite / Phantom 6). Slug unchanged (already contains model+tier+surface).
- Pack-secondary `nike shadow pack` (210/mo): woven into Short Desc ("Shadow"), tech H2 ("Nike Shadow Pack" anchor + link), Product Details ("Shadow Pack, FA26"), FAQ. Required body link to `/collections/nike-shadow-soccer-cleats` placed at the Shadow-pack reference.
- Supporting body terms: `nike phantom 6 high elite` (880/mo, KD3), `nike phantom 6 elite` (3600/mo, KD2) as natural body topical.
- No stuffing: primary variant count in Description body ~5, within 4-7. No consecutive-sentence repetition. Primary anchors 0 internal links (links use "Shadow Pack" and "artificial grass soccer cleats" descriptive anchors).

## Gate results (silent; all pass)
- Gate 2 voice_check.py: PASS (run on brief file; deliverables scope, link-format checks active). No em/en-dash, no forbidden words, adidas n/a (Nike product), no "boots" (used "cleat"/"football" only), body H2s sentence-case ("The turn he never tracks", "A plate tuned to grip the synthetic and let go", "For the artificial-grass player who wins on the blind side"), structural H2s Title Case ("Product Details: Phantom 6 High Elite AG", "Fit Notes", "Care and Maintenance", "FAQs about the Phantom 6 High Elite AG"), links full HTTPS canonical.
- Gate 5 avatar: primary Tyler (competitive AG player, elusive finisher/playmaker), AIDAR Desire/Action. Secondary none dominant. Jennifer/Carlos/Mike-the-Coach excluded (senior single-surface performance cleat, self-purchase). No cross-avatar sentence forced.
- Gate 9 lift-test: PDP carries Nike Shadow Pack + AG-Pro specificity; not liftable to a generic retailer. PASS. (Store positioning correctly kept OFF the PDP per product-page playbook forbidden subjects.)
- Gate 10 emotion-first: Short Desc + overview H2 lead with the vanishing-cut feeling; specs support. PASS.
- Gate 11 brand IP: Nike (non-adidas) -> FIFA/"World Cup" FORBIDDEN. Scan of all fields + FAQ + anchors: zero FIFA-family terms. "under the lights", "weeknight 3G" are neutral. PASS. (Note: the PDP page chrome carries a "ROAD TO THE '26 WORLD CUP" theme banner, but that is theme-level and outside SCRIBE's copy fields; my copy adds no FIFA terms.)
- Gate 13 anti-stuffing: no comma-stacked keyword lists, no synonym/modifier/brand stacking, no prices in body, no 3+ brand sentences. PASS.
- Gate 14 unsupported counts: no fabricated catalog counts. PASS.
- US market language: "cleat(s)" used; "football" used generically (sport, not footwear) so the UK-footwear term is absent. US-first units: Care bullets carry no numeric temps (procedural air-dry guidance), no weight spec in scrape so none invented -> no dual-notation needed. PASS.
- Field lengths (PDP Complex tier, Elite; target band 400-450): Description body ~430 words (within Complex ceiling 450 + tolerance). Short Desc ~57 words (within 50-100). Meta Title "Nike Phantom 6 High Elite AG Shadow Cleats" = 43 chars input (+ theme suffix stays <60). Meta Description 158 chars. Title 58 chars (within 30-100). Handle 58 chars (no change). PASS.
- Cross-SKU title uniqueness: differentiated from siblings by cut+surface+pack (High Elite AG Shadow) vs #7 High Elite FG Shadow, #8 Low Elite FG Shadow, #9 Vapor 17 Pro Shadow. PASS.

## Internal links (validated via Firecrawl content signals 2026-07-08)
1. REQUIRED `/collections/nike-shadow-soccer-cleats` -- status 200, H1 "Nike Shadow Soccer Cleats", dedicated Shadow-pack collection (Phantom/Mercurial dark styles). Not soft-404. Anchor "Shadow Pack" in tech/facet H2.
2. `/collections/artificial-grass-soccer-cleats` -- status 200, H1 "Artificial Grass Soccer Cleats", AG-specific collection. Not soft-404. Anchor "artificial grass soccer cleats" in use-case H2 (natural: buyer comparing FG vs dedicated synthetic plate). Body only.

## Tool spend
- Firecrawl: 3 scrapes (PDP + 2 link validations) = 3 credits.
- No DataForSEO this session (keywords supplied by KIRA Phase 1).

## Hold status
Holding at GATE. No finalize, no registry append. Awaiting ORIN Checkpoint 3.
