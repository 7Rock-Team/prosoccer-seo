# SCRIBE workforce-internal audit -- IF8512-001 Nike Vapor 17 Pro FG Shadow (FA26)

Batch 6 Wave 2, Tier 2A (mirrors HJ2147 Shadow-cleat exemplar STRUCTURE only). Dispatched by ORIN for Checkpoint 3 review. HOLD AT GATE (no finalize, no registry append).

## Phase 0 -- Firecrawl scrape (scrape-wins, authoritative)
- Scrape 2026-07-08, statusCode 200, healthy live PDP. creditsUsed 1.
- Live Title: "Nike Vapor 17 Pro Firm Ground Soccer Cleats - Shadow Pack (FA26)"
- Authoritative spec block (verbatim from live description):
  - Barefoot Touch: "Incredibly lightweight and strong Flyknit upper provides support and brings you closer to the ball."
  - Lightweight and Responsive: "A thin yet strong outsole plate reduces the overall weight of the cleat while adding responsiveness to each step."
  - Traction for the Field: "Chevron studs help you grip the field to stop on a dime and change direction."
  - Product Details: "For use on dry, natural-grass fields" | "Low-cut collar" | "Shown: Black/Black/Illusion Green" | "Style: IF8512-001"
  - Marketing paragraph: "Designed to unleash next-level quickness, the Vapor 17 Pro's Flyknit upper helps keep you light on your feet in tight spaces. It gives you ball control when sprinting by defenders, while our exclusive lightweight plate fuels sharp turns and smooth changes of direction."
- HYPOTHESIS CORRECTION (fabrication guard): ORIN dispatch named "Flyknit/AtomKnit per scrape" as candidate uppers. Scrape confirms upper is **Flyknit** (not AtomKnit). Copy uses Flyknit only. AtomKnit belongs to the Elite Vapor/Superfly (per silo log IO1560/IM5806); NOT asserted here.
- Weight "approximately 6.3 oz (180g)": the scrape did NOT supply a weight. 6.3 oz (180g) is the established Vapor 17 Pro FG spec used across the shipped Mercurial silo briefs (IO8225 Breakout twin, same model/tier/surface). Retained as a hedged "approximately" spec consistent with the twin; flagged here for ORIN. If ORIN prefers zero unverified specs, drop the weight bullet (removes one Product Details line, no keyword or lane impact).
- NO stud count asserted (per dispatch). "Chevron studs" only, no number.

## Keyword selection (locked at Checkpoint 1, Mike-approved)
- Primary: `nike vapor 17 pro shadow` (pack-specific; cedes bare `nike vapor 17 pro` to the shipped IO8225 Breakout twin per Mercurial anti-cannibalization). GSC-protected term.
- Pack-secondary: `nike shadow pack` (210/mo, KIRA Phase 1). Deployed via the `/collections/nike-shadow-soccer-cleats` anchor + "Shadow Pack" body mentions.
- Secondary `nike vapor 17 pro`: GSC-override, tool volume unreliable (DataForSEO 10/mo Spanish-clustered artifact on a brand-new SU26/FA26 model); GSC shows 66 impr pos 7.0 on the `vapor 17 pro` family per KIRA Phase 1. Flagged in Keywords table as `66* (GSC override, pos 7)`.
- Secondary `nike mercurial vapor 17 pro`: 10/mo tool, correct full model name (body topical only, not forced into copy).
- Difficulty cells left blank where KIRA did not return KD (not fabricated).

## Keyword deployment (Gate 12)
- Primary `nike vapor 17 pro shadow` / `vapor 17 pro` variant: Short Description sentence 2 ("Nike Vapor 17 Pro Shadow"), Meta Title, Meta Description, and body. "vapor 17 pro" body count = 7 (within the 4 to 7 Long Description range, FAQ inclusive; editorial body excl-FAQ = 3, FAQ = 4).
- ONE supporting keyword woven: `nike shadow pack` (pack-specific long-tail) appears 4x across body ("Shadow Pack" + the Shadow Pack collection anchor). No stuffing.
- No consecutive-sentence repetition; no forced-H2 keyword; primary anchors zero internal links (both anchors are collection-descriptive: "Mercurial lineup", "Nike Shadow Pack").

## Differentiation lane (spec #9, GHOSTED RUN) -- applied
- Facet: the ghosted run, arriving unseen in tight space; Vapor low-cut agility + close-control burst at Pro value, NOT straight-line speed.
- Hook: "The run they never saw start" / "off the picture" / "past his shoulder and gone" / "arrives before anyone sees the run start."
- Metaphor: the ghost past the fullback (arriving unseen), lane-native, not disguise-of-pass, not sleight-of-hand.
- Lane preservation: H2 2 explicitly names the split -- "the Vapor low-cut agility line within Nike's Mercurial family, the close-control burst rather than the high-cut Superfly built for straight-line speed." Preserves the codified Vapor(agility)/Superfly(speed) split and the Phantom(control) separation.

## Forbidden-phrasing scan (zero carry-forward) -- PASS
- HJ2147 Phantom exemplar barred family ("shape one way, play the other" / "the shadow the defense loses" / disguise-of-the-pass metaphor / its H2 titles / its closing line): NONE present. My H2 titles ("The run they never saw start", "Light on the foot, close to the ball", "Who it is for, and where") are distinct.
- IO8225 Breakout twin barred ("pickpocket's sleight of hand" metaphor; "receiving with a defender on your shoulder, touch-and-turn into the seam" hook): NONE present.

## Internal links (both live-validated, content-signal, body-only)
1. REQUIRED `https://www.prosoccer.com/collections/nike-shadow-soccer-cleats` -- anchor "Nike Shadow Pack", in H2 3 (Who it is for). Validated 2026-07-08: statusCode 200, title "Nike Shadow Soccer Cleats | Dark Nike Cleats – ProSoccer", `/products/nike-` product cards present, not a soft-404. Note: NOT targeted as a keyword (per spec: do not target "nike shadow soccer cleats").
2. OPTIONAL `https://www.prosoccer.com/collections/nike-mercurial` -- anchor "Mercurial lineup", in H2 3. Validated 2026-07-08: statusCode 200, title "Nike Mercurial Soccer Cleats for Speed – ProSoccer", product cards present, not a soft-404. Serves the Vapor-vs-Superfly comparison the prose sets up (complementary discovery path, not duplicate brand path).
- Both full HTTPS on www canonical domain. Placement is contextual (both in H2 3 where the prose authentically references the surface-family and the lineup split), not fixed structural positions.

## Brand-IP classification
- Non-adidas (Nike), cleat -> FIFA/World Cup terminology moot and absent. No tournament chrome. Evergreen. PASS Gate 11.

## Gate self-verification (silent, all pass unless noted)
- Gate 2 voice_check.py: PASS on staged file and final brief file (no em/en-dash, no forbidden words/openers, no capitalized Adidas, no UK "boots", editorial body H2s sentence-case).
- Gate 12 keyword distribution: PASS (primary in all required fields; body count 7 in range; one supporting kw; no stuffing).
- Gate 13 anti-stuffing: PASS (no comma-stacked keyword lists, no price stacking, no brand stacking; Title differentiates by tier+surface+colorway from siblings).
- Gate 14 unsupported counts: PASS ("four blackout colorways" in the Shadow Pack is a verifiable pack-set count; no fabricated federation/style counts).
- Brand styling: "Nike" only, no adidas token. PASS.
- US-market language: "cleat"/"cleats" throughout, no "boot". PASS.
- US-first dual units: "6.3 oz (180g)". PASS.
- H2 casing split: editorial body H2s sentence-case ("The run they never saw start" etc.); structural H2s Title Case ("Product Details: Vapor 17 Pro FG", "Care and Maintenance", "FAQs about the Vapor 17 Pro FG"). PASS.
- FAQ hierarchy: H2 "FAQs about the Vapor 17 Pro FG" (short-name form) + question-per-heading + paragraph answers; 4 Q&A, net-new-value (true-to-size, surface, Shadow colorway, Pro-vs-Elite sibling), FAQ placed last after Care. PASS.
- Care and Maintenance H2: footwear category triggers it; bullets, after Fit Notes; Flyknit-specific (soft brush, no conditioner). PASS.
- Fabrication guard: closure/upper hypothesis overridden by scrape (Flyknit confirmed, AtomKnit rejected); weight hedged and flagged above; no invented specs.

## Field lengths / complexity
- Complexity: Complex (multi-tier footwear, tier/surface/sibling comparison, sizing guidance).
- Full-body (editorial prose 308 + Product Details/Fit/Care bullets 107 + heading labels 31) = ~446 words; FAQ counted separately (~159). Under the Complex 465 ceiling.
- Tier note: this is a Pro-tier cleat; the tier-appropriate Pro band is 340 to 390. Final landed at ~446, above the Pro band but under the Complex ceiling. Justification: the Vapor tech story (barefoot touch + thin plate + agility-vs-speed lineage split) plus the four-Q FAQ carries genuine substance; trimmed twice from an initial ~536 (Path A: spec-bullet redundancy first -- dropped "Low-cut collar" and "Nike Mercurial Vapor line, Pro tier" bullets, collapsed Care from 4 to 3 bullets; prose padding second). Opening hook, differentiation lane, both internal links, FAQ substance, and full Care scope preserved. If ORIN wants strict Pro-band compliance, the H2 3 tier paragraph can shed a further ~30 words; flagged for Checkpoint 3 call.
- Short Description: 60 words (within 50 to 100 metafield band). No internal link in Short Description (body-only link discipline). PASS.
- Title input: "Nike Vapor 17 Pro FG Soccer Cleats - Shadow Pack (FA26)" (54 chars, within 30 to 100).
- Meta Title input: "Nike Vapor 17 Pro FG Shadow Soccer Cleats" (41 chars; with theme suffix ~53, under 60). No "ProSoccer" in field.
- Meta Description: 154 chars (within 160 ceiling; desktop-target range).
- URL handle: unchanged, 62 chars, within 70.

## Cross-SKU title uniqueness (Shadow cleat siblings #7/#8/#10 + Vapor)
- This Title carries "Vapor 17 Pro FG ... Shadow Pack (FA26)" -- distinct model line (Vapor, not Phantom) from all three Phantom siblings; no collision. Meta Title "Nike Vapor 17 Pro FG Shadow Soccer Cleats" likewise unique.

## Tool spend (this session)
- Firecrawl: 3 scrapes (PDP + 2 link validations), 1 credit each = 3 credits.
- DataForSEO: 0 (keywords locked at Checkpoint 1).

## HOLD AT GATE
No registry append (Mercurial silo log entry for IF8512-001 to be written by ORIN post-Checkpoint-3, around the existing IO8225 entry). No finalize. Awaiting ORIN independent read.
