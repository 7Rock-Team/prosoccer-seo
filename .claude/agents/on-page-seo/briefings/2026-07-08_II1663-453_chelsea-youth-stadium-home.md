# SCRIBE workforce-internal audit -- II1663-453 Nike 2026-27 Chelsea Youth Stadium Home

**Date:** 2026-07-08
**Batch:** Batch 6 Wave 1 exemplar (first CLUB jersey under Registry 2)
**Tier:** Tier 1 (first club under Registry 2; competition-naming + club-prose-lane validation)
**Status:** HOLD AT GATE for ORIN Checkpoint 2b. Registry NOT touched.

## Pre-flight tool verification (Step 0)
- firecrawl-mcp: OPERATIONAL. Phase 0 PDP scrape returned statusCode 200, creditsUsed 1. Both internal-link candidate scrapes returned 200.
- tavily-mcp: OPERATIONAL. Two currency-check searches returned live results.
- dfs-mcp: not called this session (KIRA supplied the locked keyword set in Phase 1; no independent SCRIBE SERP lookup needed for a pattern-fill exemplar).
- gsc-server: not called (primary-keyword input arrived via lane spec per the KIRA input contract).
- Google Drive (Category B): not needed; no audit-folder content in scope.

## Eligibility (Step 0.5)
Mike-pre-vetted at URL submission (batch metadata: eligibility pre-vetted in Shopify admin, Batch 6). Phase 0 scrape corroborates live and in-stock: "Hurry up, only 2 items left in stock" plus active variant selector. No strategic-exception flag. Normal optimization.

## Phase 0 scrape-wins facts (confirmed from live PDP 2026-07-08)
- Colorway: Bright Blue / Midwest Gold / Midwest Gold (variant swatch label). Rich royal-blue base, gold trims.
- Fabric/tech: Nike Dri-FIT (Stadium replica tier). NOT Aero-FIT (that is the Match/Authentic tier, confirmed via Nike.com currency check). Scrape-wins applied: used Dri-FIT.
- Badge: rampant lion crest. Design story on live PDP + Nike.com verbatim: "A celebration of Chelsea FC's own 'Italian Renaissance,' their 2026/27 Home kit's rich blue base and elevated gold trims pay homage to their transformative 1990s era."
- Design detail (Chelsea official site currency check): crest refreshed after fan consultation, woven into the front fabric; collar with button-down neck; Midwest Gold accents on lion + swoosh.
- Youth sizing: YXS, YS, YM, YL, YXL (confirmed variant list).
- Price: $84.99. SKU II1663-453 (variant -YXS). Vendor Nike, Type Apparel.
- Customization: player name/number (Palmer 10, Enzo 8, etc.), EPL sleeve patch option, "No Room for Racism" patch. Name/number ships as league-play version, 1-3 wk lead.
- Stock: 2 left (in-stock, eligible).

## Keyword selection rationale (from KIRA Phase 1 + Mike Checkpoint 1 lock)
- PRIMARY: `chelsea youth jersey` (170/mo, KD ~14 low-authority field, transactional intent). Locked by Mike at Checkpoint 1. Audience-matched to the youth SKU over the year-specific alt.
- Alt primary considered and rejected: `chelsea jersey 2026-27` (50/mo, GSC pos 8, year-specific). Rejected because the SKU's defining attribute is YOUTH and the parent/young-fan avatar matches `chelsea youth jersey` better. Carried as lead supporting term.
- Pack-secondary: `chelsea 2026/27 home jersey` (GSC pos 1 on 2 impr; floor-exempt, release-specific). Woven into body once ("The 2026/27 home jersey leans on...").
- Supporting: `chelsea jersey 2026-27` (50/mo, GSC pos 8), `chelsea home jersey` (480/mo, KD 7, broad body term), `chelsea jersey youth` (170/mo, same cluster).
- Head reference NOT targeted: `chelsea jersey` 18,100/mo (too broad/competitive for a youth home SKU; body-topical only).
- Current ranking (KIRA Phase 1 DataForSEO SERP 2026-07-08): target URL NOT in top-100 organic. Competitive youth-Chelsea SERP (Dick's #1, Nike.com #2, store.chelseafc.com #3). Fresh ranking attempt; Merchant Listings the faster surface. Ranking-aware posture: NOT top-5, standard recommendations, no equity-risk warning.

## Brand-IP classification (Gate 11)
- Page type: Nike CLUB product page (Chelsea FC).
- Classification: NON-adidas -> FIFA / World Cup terminology family FORBIDDEN. Moot for club framing (no national-tournament chrome belongs on a club page), but the discipline held: zero FIFA/WC references drafted.
- Competition-naming policy (club-team-jerseys.md, Mike Decision 2):
  - Premier League: named DIRECTLY. Used "Five Premier League titles" (body) and "Chelsea Youth Jersey 2026-27 Home | Nike Stadium" (Meta Title, no competition name). "EPL" appears once, only as the factual product-option name "EPL sleeve patch" (nominative reference to the real customization option on the live PDP, not a competition claim).
  - Champions League: GENERIC framing only. Used "two-time European champions" (body) and "the European nights that made the Blues who they are" (body). NO direct "Champions League" wording. NO "official" phrasing. NO PL/UEFA logo references.
- Compliance scan across all fields (Title, Meta Title, Meta Description, Short Description, Description body, FAQ, alt text, taxonomy): PASS. No restricted-term violations.

## Avatar scope (full-scope discipline)
- PRIMARY: Jennifer (The Mom) + the young Blue (Tyler-as-youth), buying for a young Chelsea fan. AIDAR: Desire/Action (parent at the purchase decision for a specific gift/kit). Headline copy and Short Description target the parent buying for the kid ("Your kid picked the Blues"). Club-belonging (passed-down or self-claimed loyalty) is the emotional anchor per the differentiation lane, NOT national pride.
- SECONDARY: Carlos (The Fan), the older youth fan buying for themselves. The "found their own way to the Blues through a favorite player" line and the heritage/rivalries section serve the fan-identity angle.
- EXCLUDED: Mike the Coach (team uniforms route through team-orders, not a single youth replica PDP). Reasoning: this is a single-fan replica, not bulk.
- CROSS-AVATAR LANDING: an adult fan searching "chelsea youth jersey" for their own smaller frame might land here; the Fit Notes YXL-to-adult-small line addresses them.

## Differentiation lane adherence (spec SKU #2)
- Angle: youth club loyalty + Blues identity + young fan's first real Chelsea shirt + parent-facing. HELD.
- Opening hook: parent/young-fan, the kid who chose Chelsea (passed down or own hero). HELD ("Some kids inherit Chelsea from a parent. Some find their own way...").
- Primary metaphor: club belonging claimed or passed down (the young Blue), distinct from NT national-pride lane. HELD.
- Heritage anchors used: the Blues, Stamford Bridge / Fulham / west London, founded 1905, five Premier League titles, two-time European champions, rampant lion, Nike current supplier. All confirmed via currency check.
- Liverpool anti-collision (silo log): Liverpool brief's claimed patterns = traveling-supporter/away-day hook, "the title kit" metaphor, Hillsborough tribute, Nike-farewell-to-adidas narrative. This brief uses NONE of those: home (not away) framing, "young Blue passed-down belonging" metaphor (not "title kit"), no tribute-detail narrative, Nike-as-current-supplier (not a farewell). Clean separation.

## Named entities (LLM discoverability, 5-10 target)
Chelsea FC, the Blues, Stamford Bridge, Fulham / west London, Nike, Dri-FIT, rampant lion, Premier League, Arsenal, Tottenham/Spurs, Cole Palmer (via internal link). 10+ specific entities. PASS.

## Internal link validation (content signals, not just 200)
- `/collections/cole-palmer`: statusCode 200; H1 "Cole Palmer Soccer Jersey"; title "Cole Palmer Jerseys, Apparel & Gear | Pro Soccer"; 13 products (this Chelsea youth home jersey is the first product listed). VALIDATED. PREFERRED per codified player-spotlight-over-brand-cross-promotion preference. Used as body anchor.
- `/collections/chelsea`: statusCode 200; H1 "Chelsea Soccer Jerseys, Apparel, & Gear"; title "Chelsea Soccer Jerseys & Gear | Prosoccer.com"; 58 products. VALIDATED. Used as body anchor (parent club collection).
- NOTE on placement: On final review, I embedded the two internal links as anchor text at natural points in the Description body prose. See "Internal links placed" below.

## Internal links placed (Description body only, per policy; NOT Short Description) -- RESOLVED
Both links placed inline at authentic anchor points (not defaulted to fixed H2s, per the link-placement discipline). Both destinations content-validated (200 + H1 + product count + title).
1. `https://www.prosoccer.com/collections/cole-palmer` -- anchor text "Cole Palmer", placed in the overview ("...through a favorite player, a Cole Palmer shirt on the back..."). Palmer is the confirmed current Chelsea attacking mid, Nike-sponsored, and the top customization pick (Palmer 10 is first in the live name/number selector). Player-spotlight preference satisfied.
2. `https://www.prosoccer.com/collections/chelsea` -- anchor text "west London side", placed in the heritage section ("Chelsea has been the west London side since 1905..."). Parent club collection.

Voice check + link-format check re-run after placement: PASS (exit 0; both full HTTPS www canonical URLs; no relative/http/missing-www forms).

## Field-length checks (PDP discipline)
- Title: 52 chars (30-100). PASS.
- Meta Title INPUT: "Chelsea Youth Jersey 2026-27 Home | Nike Stadium" = 48 chars, + theme suffix stays under 60. PASS.
- Meta Description: 158 chars (<=160). PASS.
- Short Description: ~55 words (50-100). PASS. No internal link (correct).
- Description body: ~507 words incl H2 labels + bullets, excl FAQ. Above generic Complex 465 ceiling, WITHIN the national/club-jersey-class length exception (clarified 2026-06-30; shipped Croatia set 507-534). Trimmed from initial 527 to 507 to avoid write-to-ceiling drift on a replica-tier SKU while holding the jersey-class norm. PASS under jersey exception.
- URL handle: no change, 51 chars. PASS.

## Gate self-verify (silent; all pass unless noted)
- Gate 1 self-verification: PASS (all scrape facts, keyword figures, and link states re-confirmed against source).
- Gate 2 voice_check.py: PASS (exit 0, re-run after edits).
- Gate 3 sourcing: PASS (all facts sourced to Phase 0 scrape / KIRA Phase 1 / Tavily currency check).
- Gate 4 severity/confidence/lift: High confidence (scrape + Nike.com + Chelsea official all align on design + heritage).
- Gate 5 avatar full-scope: PASS (primary/secondary/excluded/cross-avatar all named).
- Gate 6 reversibility: current fields captured via Shopify admin (Mike references); revert = restore prior fields.
- Gate 9 positioning lift-test: club-belonging + Stamford Bridge/1905 heritage + Palmer link are ProSoccer/Chelsea-specific; could not be lifted onto a generic retailer unchanged. PASS.
- Gate 10 emotion-first: overview leads with feeling ("turns 'I like Chelsea' into 'I'm a Chelsea fan'"), features support. PASS.
- Gate 11 brand-IP: PASS (see classification above).
- Gate 12 keyword distribution: primary in Title/Meta Title/Meta Desc/Short Desc/body; body exact-match count 1 in prose (+ Keywords table + Meta Title), well under 7; supporting woven naturally; pack-secondary present once. No stuffing. PASS.
- Gate 13 anti-stuffing: no comma-stacked keyword lists, no price in body copy, no brand-stacking, no synonym-stacking. PASS.
- Gate 14 unsupported counts: "five Premier League titles" and "two-time European champions" are verified authoritative facts (currency check). No unverified catalog counts. PASS.
- Measurement units: Care bullet uses US-first "86°F (30°C)". PASS.
- FAQ hierarchy: H2 "FAQs about the Chelsea Youth Stadium Home Jersey", each Q an H3, paragraph answers, placed last after Care. PASS.
- H2 casing: editorial H2s sentence case ("A young Blue gets their colors", "Blue and gold, straight from the 1990s", "A club worth handing down"); structural H2s Title Case ("Product Details: Chelsea Youth Stadium Home", "Care and Maintenance", "FAQs about..."). PASS.

## Cost tracking (this session)
- Firecrawl: 3 credits (1 PDP + 2 internal-link validations).
- Tavily: 2 searches.
- DataForSEO: 0.
- Within SCRIBE envelopes.

## Open items for ORIN
- None blocking. Internal links resolved and placed (see above).
- Theme-level (not a copy item, for the standing Misha audit list): og:image on this PDP uses `http://` (og:image = http://www.prosoccer.com/cdn/...). Matches the known http:// og:image theme bug already logged across 6+ PDPs. No action for this brief; noting for completeness.
