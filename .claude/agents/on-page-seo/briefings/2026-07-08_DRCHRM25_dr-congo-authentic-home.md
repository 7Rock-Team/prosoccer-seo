# SCRIBE workforce-internal audit -- DRCHRM25 Umbro DR Congo Men's Authentic Home (Batch 6 Wave 1 exemplar)

**Date:** 2026-07-08
**Brief:** `deliverables/page-optimizations/2026-07-08_session-01/DRCHRM25_umbro-2026-dr-congo-mens-authentic-home_brief.md`
**Tier:** 1 (NT exemplar anchoring the DR Congo pair; first Umbro + first DR Congo in the workforce). Validates Umbro non-FIFA + Authentic-tier + substitution discipline for the Wave 2 mirror (#4 DRCARM25 Away).
**Eligibility:** Mike-verified healthy PDP at submission (ORIN dispatch, 2026-07-08). Live storefront shows sold-out variants; jersey copy is evergreen, optimized normally per the healthy-PDP call. No strategic exception flagged.

## Phase 0 scrape (mandatory, scrape-wins) -- Firecrawl 2026-07-08, status 200
- Product: Umbro 2026 DR Congo Men's Authentic Home Soccer Jersey. SKU `DRCHRM25/KIT`. Vendor Umbro. Type Apparel.
- **Colorway (scrape-confirmed):** variant color label "Light Blue". Used "sky blue" in copy as the natural supporter term, consistent with the silo's sky-blue home palette and the variant label. Did NOT invent a design motif (no leopard-print claim on the home; KIRA's Phase 1 notes describe the home as "bright light-blue base with leopard heritage motif" but that is not scrape-confirmed on this render, so copy stays on the scrape-safe "sky blue with gold and red flag accents" and does not assert a leopard-print pattern for the home).
- Tier: "Authentic" per title + "100% Authentic Gear" trust badge. Sizes S to 2XL (2XL present in the men's selector). Price $91.00 from $130.00.
- Current live copy CARRIES A BRAND-IP VIOLATION: body text reads "Brand new 2026-27 World Cup Congo Home Jersey... worn at the FIFA World Cup 2026," and the "ROAD TO THE '26 WORLD CUP" countdown banner sits at the top. The banner is site-wide theme chrome (not a SCRIBE field). The body WC/FIFA text IS a field SCRIBE replaces; the new Description carries zero FIFA/WC terms and fixes the live violation. Flag for Mike: the theme countdown banner is a separate site-wide chrome item outside this brief's scope (VERITAS/Misha if it needs addressing on non-adidas pages).

## Brand-IP classification
- **Classification: NON-adidas (Umbro).** FIFA / "World Cup" / "WC" / "FIFA" terminology FORBIDDEN across all six fields + internal link anchor. Cycle/year language only.
- Substitution applied per `context/brand-ip-constraints.md` + dispatch:
  - 2026 qualification -> "sealed their place in the 2026 international tournament" (never "qualified for the World Cup").
  - 1974 finals -> "the finals as Zaire" / "reached the finals as Zaire" (never "1974 World Cup").
  - Year "2026" alone used freely (always permitted).
- **Compliance scan:** `grep -niE "world cup|fifa|\bwc\b|world-cup"` across the brief returned zero matches (exit 1). Clean across Title, Short Description, Description body, Meta Title, Meta Description, URL Handle, Image Alt, FAQ, Taxonomy, and the internal-link anchor text.
- Gate 11 (brand IP) precedence over voice: no conflict this brief; both pass.

## Keyword set (from KIRA Phase 1 candidates, ORIN-locked Checkpoint 1)
- **Primary:** `dr congo jersey 2026` (140/mo, recent peak 590; KD not returned by DataForSEO for the DR Congo family, confirmed via `bulk_keyword_difficulty` 2026-07-08 returning no KD field -> Difficulty cells left blank, not fabricated). Home-lane cycle-flagship primary.
- **Pack-secondary:** `dr congo home kit 2026` (GSC pos 1.1, floor-exempt, no tool volume -> blank cells). Woven into prose once ("2026 DR Congo home jersey" natural variant in FAQ; "home kit" in Short Description).
- **Supporting (body, one volume-selected + topical):** `dr congo soccer jersey` (480/mo, primary supporting, woven 3x per Gate 12(d)), `congo soccer jersey` (480/mo, topical), `umbro congo jersey` (70/mo, brand+team, present via "Umbro DR Congo" natural). Generic `congo jersey` (1,000/mo head) stays shared body term; home wins it by GSC default (pos 6.4, 3,351 impr) per the cannibalization resolution.
- **Cannibalization (vs #4 Away):** HOME takes year-qualified generic `dr congo jersey 2026`; AWAY takes away-qualified lane. Kept the PDP primary year-specific so it does NOT cannibalize the collection page's generic "DR Congo soccer jersey" term (dispatch requirement). Confirmed: primary is `dr congo jersey 2026`, collection targets `dr congo soccer jersey`.
- **Current ranking:** target URL NOT in top-100 organic for `dr congo jersey 2026` (umbroteam.com #1, worldsoccershop #2, goal.com #3, Dick's #4). GSC shows prosoccer ranks the whole Congo cluster pos 6-8 with very large impressions. Striking-distance; the win is CTR + Merchant Listings, not a fresh organic attempt. No top-5 warning needed (not top-5).

## Differentiation lane (ORIN spec #5) -- applied
- Angle: Les Léopards home identity via sky-blue heritage; Authentic match-spec tier; African-football + diaspora pride.
- Opening hook: the DR Congo supporter pulling on the sky-blue home shirt ("Pull on the sky blue and you're one of Les Léopards"). Distinct from the Away mirror's away-day/roaming lens.
- Primary metaphor: the Leopard as national identity + heritage pride (evergreen), NOT athletic performance.
- Heritage anchors used: Les Léopards; sky-blue/gold/red flag palette; AFCON titles 1968 (as Congo-Kinshasa) + 1974 (as Zaire); the finals as Zaire in 1974; FECOFA; CAF; Umbro current supplier; Authentic match-spec tier. 8 named entities (Gate: 5 to 10 target met): Les Léopards, DR Congo, Congo-Kinshasa, Zaire, FECOFA, CAF, Umbro, Africa/African football.
- "Les Léopards" / "the Leopards" used GENDER-NEUTRALLY (team-general). Did NOT coin a women's variant ("Léopards dames" not referenced; this is a men's kit).

## Tier discipline (Authentic, match-spec)
- Framed as Authentic = match-spec, closer performance fit, on-pitch pattern; distinguished from the roomier replica/Stadium fan version. Did NOT combine tier words ("Authentic Stadium" never appears). FAQ Q1 makes the Authentic-vs-replica distinction the buyer-decision anchor. Fit Notes + FAQ Q2 both carry the "runs closer to the body, size up if between sizes" guidance the Authentic cut requires.

## Structure (National Team Jersey CANONICAL template, four-time validated)
- H2 1 (brand+design+federation identity): "Wearing the sky blue of Les Léopards"
- H2 2 (cultural + heritage context): "The Leopards, and the colors behind them"
- H2 3 (edition tier): "The Authentic match-spec version" + internal link
- Product Details bullets (Title Case structural H2: "Product Details: DR Congo Authentic Home Jersey")
- Fit Notes
- Care and Maintenance (bullets; jersey category triggers Care H2; US-first dual notation "86°F (30°C)")
- FAQs about the DR Congo Authentic Home Jersey (H2 structural Title Case; 4 H3 questions; net-new value: Authentic-vs-replica, sizing, colors, authenticity)
- Editorial body H2s in sentence case; structural H2s (Product Details, Care and Maintenance, FAQs about) in Title Case per the 2026-06-17 split discipline. Voice check confirms no casing drift.

## Gates (silent) -- all pass
- Gate 1 self-verify: sources re-checked against Phase 0 scrape + KIRA candidates + silo file. Colorway, tier, sizes, SKU all scrape-sourced.
- Gate 2 voice_check.py: PASSED (exit 0), no em/en-dash, no forbidden words, no capitalized Adidas, no UK "boots", no lowercase editorial H2 drift.
- Gate 5 avatar full-scope: PRIMARY Carlos-type DR Congo supporter/diaspora fan (Desire/Action AIDAR, 2026 cycle). SECONDARY Tyler-type performance-minded fan who wants the authentic match cut (addressed via Authentic tier). EXCLUDED Jennifer (adult self-purchase men's Authentic, not parent-purchase) and Mike the Coach (national-team fan kit, not team uniforms). Cross-avatar landing: a diaspora parent might land here for an adult family member; sizing sentence in Fit Notes/FAQ covers.
- Gate 9 positioning lift-test: copy is DR-Congo-specific (Les Léopards, FECOFA, 1968/1974 AFCON, the finals as Zaire) and could not be lifted onto a generic retailer unchanged. Passes. (PDP subject discipline: no ProSoccer store call-outs in body; internal link is to the DR Congo collection, in scope.)
- Gate 10 emotion-first: intro leads with identity ("Pull on the sky blue and you're one of Les Léopards"), features support. Passes.
- Gate 11 brand IP: PASS (zero FIFA/WC, substitution applied, documented above).
- Gate 12 keyword distribution: primary present in Title (natural via product name), Short Desc (sentence 2), Description body (4x: H2 1, H2 1 body, FAQ, Short Desc), Meta Title, Meta Desc. Not stuffed (<7, no consecutive repetition, primary anchors 0 internal links). ONE volume-selected supporting (`dr congo soccer jersey`, 3x) + pack-specific long-tail once. Pass.
- Gate 13 anti-stuffing: no comma-stacked keyword lists, no synonym/modifier/brand stacking, no price in body (price only in Quick Reference/schema territory, not body prose), no 3+ brand sentences. Pass.
- Gate 14 unsupported counts: "two-time African champions" is a verified authoritative count (AFCON 1968 + 1974), permitted. No inventory/style counts. Pass.
- Brand styling: no "adidas" token in this brief (Umbro page). N/A but clean.
- US market language: "cleats" N/A (jersey); no "boots". Clean.
- Internal link format: single link, full HTTPS canonical `https://www.prosoccer.com/collections/dr-congo-national-soccer-team-jerseys-apparel`. Validated via Firecrawl (status 200, H1 "DR Congo National Soccer Team Jerseys & Apparel", collection page confirmed by title). Body only (in H2 3), NOT in Short Description. Collection currently shows "no products" but the collection URL is live/canonical and is the correct supporter-navigation destination; content signals (200 + H1 + title match) pass. Anchor text "DR Congo national team jerseys" (5 words, descriptive, natural).
- Measurement units: Care bullet uses US-first dual notation "86°F (30°C)". Pass.

## Length
- Description body full-body word count: 615 (editorial prose + Product Details + Fit Notes + Care + 4-Q FAQ). Above the shipped jersey-set high (~534) but within jersey-class exception territory (no hard band codified; national-team jerseys deliberately run above the cleat Complex ceiling). Trim already applied removed prose padding (H2 1/2/3), not decision-value content; the 4 FAQ Q&As carry the Authentic-vs-replica buyer decision and are load-bearing for the tier distinction. Held rather than cut FAQ substance. Note for the Away mirror (#4): match this structure but siblings write own prose; away can run slightly leaner if it helps parity toward ~534.
- Short Description: 66 words (within 50 to 100).
- Meta Title input: 43 chars ("DR Congo Jersey 2026 | Umbro Authentic Home"), renders ~55 with theme suffix, under 60.
- Meta Description: 156 chars (within 160).

## Wave 2 handoff note (for the #4 DRCARM25 Away mirror)
- Structure skeleton: same 4-prose-H2 + Product Details + Fit Notes + Care + FAQ order.
- Forbidden phrasings for the Away (from this exemplar's prose): opening "Pull on the sky blue and you're one of Les Léopards"; H2 titles "Wearing the sky blue of Les Léopards", "The Leopards, and the colors behind them", "The Authentic match-spec version"; the "one of the room knows where you stand" anthem framing; primary metaphor "the Leopard as national identity/heritage pride" (Away uses the away-day/roaming/the-Leopard's-range lens).
- Away colorway is NOT confirmed here; scrape-wins at Away brief time (KIRA notes a white base with leopard-skin/geometric pattern, but do not assume, scrape it).
- Same brand-IP discipline (Umbro non-FIFA, cycle language, substitution). Same Authentic tier.

## Tool spend this session
- Firecrawl: 3 credits (PDP scrape + collection validation + 1 collection re-read via PDP scrape). Within SCRIBE 100/mo.
- DataForSEO: 1 `bulk_keyword_difficulty` call (~$0.001). Within envelope.

## HOLD AT GATE
Not finalized. No registry touched. Awaiting ORIN Checkpoint 2b review.
