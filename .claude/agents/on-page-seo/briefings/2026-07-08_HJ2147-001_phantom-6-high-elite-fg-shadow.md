# SCRIBE workforce-internal audit -- HJ2147-001 Nike Phantom 6 High Elite FG Shadow (Batch 6 Wave 1 exemplar)

Date: 2026-07-08. Tier 1 (Shadow-cleat family structural exemplar). Dispatched by ORIN, hold at Checkpoint 2b.

## Tool pre-flight (Section 2 Step 0)
- Firecrawl MCP: operational (Phase 0 scrape returned 200 on the live PDP + both link-target collections). Note: KIRA's Phase 1 flagged Firecrawl down 2026-07-08; it is UP at SCRIBE brief time. Phase 0 scrape-wins discipline satisfied.
- DataForSEO / GSC: not called this session; primary + volumes inherited from KIRA Phase 1 (locked at Checkpoint 1, Mike-approved).
- Cost this session: 3 Firecrawl scrapes (PDP + 2 link validations) = 3 credits. No DFS spend.

## Eligibility (Step 0.5)
Mike-verified in-stock at submission (batch pre-vetted in Shopify admin, 2026-07-08). Live PDP renders "Add to Cart" / normal purchase state; no strategic exception flag. Normal optimization.

## Phase 0 scrape-wins (live PDP, scraped 2026-07-08)
Confirmed from live body copy, NOT invented:
- Model/tier/surface/colorway: Nike Phantom 6 High Elite Firm Ground - Shadow Pack (FA26). Colorway shown: **Black/Black/Illusion Green** (the green Shadow colorway; corroborates GSC "phantom 6 high elite green" / "shadow pack green" queries landing here).
- Upper: Nike Gripknit, sticky texture, grip in wet or dry, "ultimate precision."
- Traction: Cyclone 360 circular pattern, forefoot, plant-and-pivot.
- Frame: new shoe frame, natural fit esp. toe box, closer to the ball.
- Collar: Dynamic Fit collar, soft stretchy Flyknit (this is the "High" cut).
- Lacing: Ghost Lacing (covers laces once tied).
- Sockliner: cushioned.
- Surface: dry, natural-grass fields (FG).
- Style: HJ2147-001.
No stud count claimed (scrape did not give one; playbook FMG/AG note discipline applied to FG plate too). No weight claimed (scrape gave none; left out rather than fabricated -- Product Details weight bullet omitted deliberately).

## Two theme-level bugs observed (Misha audit items, NOT my copy; consistent with MEMORY.md open items)
1. Live `<title>` truncated: "Nike Phantom 6 High Elite Firm Ground Soccer Cleats - Shadow Pack (FA2 – ProSoccer" -- cut mid-word at "(FA2". This is the known `<title>` truncation theme bug. My Meta Title recommendation (40 chars input) fixes it for this SKU regardless.
2. `og:image` served over `http://` (`http://www.prosoccer.com/cdn/shop/files/...`). Known http:// og:image theme bug (6+ PDPs). Route to Misha; not copy.
Flag both to ORIN for the running Misha audit-request list; not blockers for this brief.

## Brand-IP classification (Gate 11)
Nike cleat -> non-adidas. FIFA / "World Cup" / "WC" / "FIFA" terminology FORBIDDEN. Moot in practice (a cleat, no tournament framing needed). Copy uses Nike-cleat + performance/cycle language only. "FA26" is a Nike season code, not a FIFA term. Compliance scan across all fields + link anchors: PASS, zero FIFA-family tokens.

## Keyword distribution (Gate 12)
- Primary `nike phantom 6 high elite fg shadow` (110/mo, KIRA-locked, GSC-protected). Deployed: Title (natural variant "High Elite FG Shadow Pack"), Meta Title, Meta Description (natural), Short Description (natural, first two sentences), Description H2 + body. Slug: no change (existing slug already carries the full phrase). Body primary-family count: "Phantom 6 High Elite FG" appears in overview, Product Details H2, Fit Notes, FAQ -- within 4-7 with natural variation, no stuffing.
- Pack-secondary `nike shadow pack` (210/mo, Mechanism C, floor-exempt): deployed in Title, Short Description ("Shadow Pack" via colorway), Description body (overview "green-tinged Shadow Pack colorway"; FAQ "What is different about the Shadow Pack colorway"). Woven >=1x in prose per the pack-specific rule. PASS.
- Supporting `nike phantom 6 high elite` (880/mo, KD 3) and `nike phantom 6 elite` (3600/mo, KD 2): body topical, natural. `phantom cleats` head is topical background, not forced.
- Single volume-selected supporting keyword rule: primary is the SKU-exact; the two "phantom 6 (high) elite" body terms are the natural parent family, not a stack of unrelated supporting keywords. No multi-supporting-keyword stuffing.
- NOT targeting the link-collection term "nike shadow soccer cleats" as a keyword (per dispatch + spec line 26). It appears only as internal-link anchor text.

## Anti-stuffing (Gate 13) + specific counts (Gate 14)
- No comma-stacked keyword lists, no ampersand-terminated lists, no synonym/modifier/brand stacking in any field. Title reads as natural product name.
- No prices in body copy (scrape showed "Free USA shipping over $100" in page chrome -- deliberately kept OUT of my body copy per forbidden-subjects; that is chrome, not description).
- No unsupported catalog counts.
- US market language: "cleats," never "boot(s)." Draft's figurative "in the boots of the number ten" was caught (US-market rule + `voice_check.py` `\bboots?\b`) and corrected to "in the game of the number ten." Final brief re-run: PASS (exit 0).

## Measurement units (Gate 15 family)
No temperature/weight/dimension values used in body (scrape gave no weight; not fabricated). Care bullets carry no temperature (cleats air-dry, no wash temp). US-first dual notation not triggered. Sizing stays US convention ("half size"). PASS.

## Anti-convergence vs IH1779-900 (Breakout twin, shipped 2026-06-08) -- CRITICAL for this exemplar
Forbidden carry-forward per phantom.md IH1779 log + spec line 40:
- IH1779 hook = "the moment of the strike" (reader inside a match-deciding finish). MY hook = the disguised pass no defender reads; the creator who shapes one way and plays the other. DISTINCT (creation/deception, not the finish).
- IH1779 metaphor = "the calm of a trained craft / marksman's rehearsed aim." MY metaphor = "the shadow the defense loses" (disguise/vision). ZERO marksman, aim, rehearsal, trained-craft language. Confirmed by string scan of the brief.
- IH1779 angle = rehearsed repeatable finish / precision as trained craft. MY angle = disguise in the final third, vision and weight of pass. DISTINCT.
- Shared (allowed): Phantom-as-accuracy-line heritage, Gripknit-across-the-upper spec, High-collar/Dynamic-Fit, FG/dry-grass. These are real shared specs (Product Details overlap allowed); prose framing is fully distinct.
Confirmation: brief contains NO "strike"(as-finish-moment), "marksman," "aim," "rehearsed," "trained craft," "calm." PASS.

## Cross-sibling differentiation (for Wave 2 handoff)
This exemplar claims the "disguise of the pass / vision in the final third / the shadow lost on the blind side" facet. Wave 2 siblings must avoid it:
- #8 HJ2146 (Low Elite FG): "unseen first step / quickness of release, no collar."
- #9 IF8512 (Vapor 17 Pro FG): "ghosted run in tight space" (Mercurial agility).
- #10 HQ2329 (High Elite AG): "unseen cut on turf under lights."
Exemplar handoff to Wave 2 = STRUCTURE SKELETON + FORBIDDEN-PHRASINGS, not this prose (Mechanisms A+B). Forbidden phrasings to hand down (this brief's claimed language): H2 titles ("The pass no one sees coming", "Gripknit holds the ball through the disguise", "Locked in for the creator on firm ground"); opening hook ("Shape one way, play the other... you are the shadow the defense loses"); primary metaphor ("the shadow the defense loses on the blind side"); closing line ("If your game is disguise and delivery rather than raw pace..."); the Gripknit definitional framing tied to "disguised pass."

## Internal links (Section 9 workflow; validated via Firecrawl, content signals)
1. `/collections/nike-shadow-soccer-cleats` -- REQUIRED. Validation: 200; H1 "Nike Shadow Soccer Cleats"; real product grid (many /products/ links); title "Nike Shadow Soccer Cleats | Dark Nike Cleats". Not a soft-404. Anchor: "Nike Shadow soccer cleats" (descriptive, natural, in closing prose). PLACED (Description body, "Locked in" H2 close).
2. `/collections/nike-phantom` -- OPTIONAL second; VALIDATED (200; H1 "Nike Phantom Soccer Cleats for Men, Women, Youth"; real grid) but NOT placed. Reason: one body link reads cleaner than two here; the Shadow collection is the load-bearing pack link and the more relevant destination for a Shadow-pack buyer. Held to 1 link (within the 1-2 target). Available for Mike if he wants a second.
Both links are full HTTPS on www.prosoccer.com (Internal Link Format check PASS). Link lives in Description body only, never Short Description (PASS).

## Field lengths (PDP discipline)
- Title: "Nike Phantom 6 High Elite FG Shadow Pack Soccer Cleats" = 53 chars (30-100). PASS. Unique vs siblings (High + FG + Shadow Pack).
- Short Description: 60 words (50-100). PASS. Reader-first hook, no feature-listing (Gripknit named as enabler of the hidden touch, not spec-recited).
- Description body: Complex/Elite tier, target 400-450. Count ~432 words full-body (prose + Product Details + Fit + Care; FAQ separate). Within band, under 465 ceiling. Elite tier earns the upper band.
- Meta Title INPUT: "Nike Phantom 6 High Elite FG Shadow Pack" = 40 chars; + theme suffix (~12) = ~52 rendered, under 60. PASS. No "ProSoccer" in field.
- Meta Description: 156 chars (<=160, 150-158 desktop target). PASS. Primary natural in first 90 chars.
- URL handle: unchanged, 62 chars (<=70). PASS.

## H2 casing (split discipline)
- Editorial H2s SENTENCE case: "The pass no one sees coming", "Gripknit holds the ball through the disguise", "Locked in for the creator on firm ground". (Gripknit = proper noun, capitalized correctly.)
- Structural H2s Title Case: "Product Details: Phantom 6 High Elite FG", "Care and Maintenance", "FAQs about the Phantom 6 High Elite FG". PASS.

## FAQ hierarchy
H2 "FAQs about the Phantom 6 High Elite FG" (short natural name, not full primary kw). 4 H3 questions (size, AG surface, Shadow colorway, high vs low collar), paragraph answers, net-new value (not in body). Sits last, after Care. PASS.

## Care H2
Footwear category -> Care required. Bullets (not prose), after Fit Notes. Synthetic-upper note (no leather conditioner). No wash temp (cleats). PASS.

## Editorial philosophy self-checks
Reader-first (serves the creator's identity, not algorithm); cognitive load (sentence-length variance, one concept/sentence, scannable leads); value-first sequencing (hook -> why -> specs in bullets); positive anchoring (identity/craft/belonging, no scarcity/FOMO); outcome-based (opens with the pass landing, the runner never covered -- the transformation, not a feature). Image precision: "shape your body toward the near post, the marker leans, the ball rolls the other way" = concrete physical action + sequence. PASS.

## Voice check remediation log
Initial draft contained "in the boots of the number ten" -- `\bboots?\b` FAIL (US-market rule + script regex). Rewrote to "in the game of the number ten." Re-ran full brief; see gate-status line in the return summary. Zero em/en dashes, zero forbidden AI-cliche vocabulary, "adidas" not present (Nike SKU), no "Adidas" cap issue.

## Gates summary
1 self-verify PASS; 2 voice PASS (post-remediation); 3 sourcing PASS (scrape-wins + KIRA cited); 4 severity/confidence in audit; 5 avatar (primary Tyler/creator + Carlos Shadow-colorway fan; Jennifer excluded-adult performance cleat; Mike-coach excluded-single-pair not team order); 6 reversibility (revert to current fields); 7 plain-language N/A batch; 8 red-team below; 9 positioning lift-test PASS (Phantom-line + creator identity, not liftable to Soccer.com generic); 10 emotion-first PASS; 11 brand-IP PASS; 12 keyword dist PASS; 13 anti-stuff PASS; 14 counts PASS; 15-family (casing/units/FAQ/Care) PASS.

Red-team: weakest link is that the Shadow Pack is a colorway, not a build change -- FAQ #3 states this honestly rather than overselling the colorway as performance. Second: no weight bullet (scrape gave none); acceptable, not fabricated. Third: primary 110/mo is modest and org rank is absent (Nike.com owns organic); the real near-term surface is Merchant Listings, per KIRA flag 7 -- copy quality + product schema alignment is the lever, which this brief serves.
