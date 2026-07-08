# SCRIBE audit trail: KB7474 adidas 2026 Jamaica Men's Authentic Away Jersey

**Date:** 2026-07-08
**Batch:** 6, Wave 2, Tier 2A (national-team-jersey CANONICAL template)
**Brief:** deliverables/page-optimizations/2026-07-08_session-01/KB7474_adidas-2026-jamaica-mens-authentic-away_brief.md
**Status:** HELD AT GATE for ORIN Checkpoint 3 review; not finalized, no registry append.

## Eligibility
Mike-pre-vetted at URL submission (Batch 6 dispatch). Phase 0 scrape confirms the PDP is currently Sold out / Out of stock across S and M (price $113.00, down from $150.00). Not flagged as a strategic exception by Mike; treated as normal optimization per the standing convention (dispatch named it a healthy Tier 2A page). Note for ORIN: page is sold-out at scrape time; if Mike wants closing-window or pre-tournament framing it was not requested, so copy stays evergreen fan-identity without stock-state chrome.

## Phase 0 scrape (scrape-wins), statusCode 200, 2026-07-08
Confirmed from live PDP:
- Colorway: Black base. Swatch label "Black." Store hero line names it the "Jamaica 26 x Bob Marley Away Authentic Jersey," "a bold tribute to the vibrant spirit of reggae and the legacy of Bob Marley."
- Tier: Authentic (match-spec). Slim fit, crew neck, transfer knit jacquard construction, adidas Climacool+ technology, puffed/heat-transfer adidas logo + crest, heat-applied label with hidden UV print (seal of authenticity).
- Material: 100% Polyester (100% Recycled).
- Price: $113.00 (was $150.00). Sold out.

**Fabrication-guard override:** dispatch hypothesis named "HEAT.RDY" as the authentic-tier fabric. Scrape says **Climacool+**. Scrape wins; brief uses Climacool+, not HEAT.RDY. Heat-pressed badges + hidden-UV authenticity label are scrape-confirmed and used as the authentic-tier differentiators instead of the generic HEAT.RDY hypothesis.

## Brand-IP classification
adidas product page. adidas is the FIFA commercial licensee, so FIFA / World Cup terminology IS permitted here. Decision: applied the tournament-status EVERGREEN discipline anyway. No "World Cup" wordmark used in copy; the France 1998 debut is referenced as "their debut at France 1998" and "the first English-speaking Caribbean nation to reach that stage," which conveys the milestone without invoking the trademarked phrase and stays evergreen. No "qualified for 2026," no "chasing the trophy," no live-bracket/title-defense chrome. Primary keyword evergreen. FORBIDDEN "only World Cup"/"only appearance" not used (Jamaica is in the 2026 inter-confederation playoff, so "only" is falsifiable); used "debut"/"reach that stage."

## Keyword selection (KIRA Phase 1 + lane spec)
- Primary (locked, Mike-approved): `jamaica soccer jersey 2026`, vol 170/mo (recent peak 590 Mar-26, 480 May-26), KD not returned by DataForSEO -> Difficulty cell left BLANK (not fabricated). GSC: this exact query 218 impr avg pos 3.4, 0 clicks, on the target page over 90 days (strongest single-query signal; already page-1). CTR-ceiling opportunity, not a fresh-ranking attempt.
- Supporting selected for body (highest-volume among Phase 1 supporting set): `jamaica away jersey` (110/mo, GSC pos 9.6) + `jamaica jersey adidas` (140/mo, GSC pos 3.1). Wove the away-authentic intent through body/FAQ.
- Colorway-specific secondary (Mechanism C, floor-exempt): `jamaica bob marley away jersey` -- volume not returned, cell blank. Woven into Product Details colorway bullet + FAQ ("black-based Bob Marley away design"). Single carve-out mention beyond the volume-selected supporting; not a Gate 12(d) violation.
- Cross-SKU note: a separate Youth Stadium Away SKU exists (seen in Jamaica collection + SERP Images). Watch generic `jamaica away jersey` cannibalization if that youth page enters scope; this brief keeps the primary variant-specific (authentic + men's + 2026) to reduce collision.

## Differentiation lane (spec #1) adherence
- Angle: Reggae Boyz identity through the unmistakable Jamaican colors; Authentic away as a cultural statement; diaspora + reggae-culture pride. Delivered.
- Opening hook: "Green, black, and gold read across a room, and you wear them like they're yours" -- the colors-read-across-a-room hook per lane. Distinct from DR Congo siblings (#4/#5 sky-blue Leopards away-day/home-heritage), Korea (#3 red taegeuk), Chelsea (#2 youth club-blue). Intra-batch unique.
- Primary metaphor: national/cultural pride carried in the flag's colors, NOT athletic performance. Held (no speed/power/performance metaphor leads).
- Reggae Boyz used for the MEN's team only (women's = Reggae Girlz; not misapplied).

## Heritage anchor (evergreen, verifiable)
"their debut at France 1998, where they became the first English-speaking Caribbean nation to reach that stage and beat Japan 2-1 in Lyon behind Theodore Whitmore's two goals." Source: silo guardrail (national-team-jerseys.md, Jamaica note, 2026-07-08) + widely documented. Exact 1998-debut phrasing in the brief (for ORIN's gate note): "from their debut at France 1998, where they became the first English-speaking Caribbean nation to reach that stage and beat Japan 2-1 in Lyon behind Theodore Whitmore's two goals."

## Federation / colors
JFF + CONCACAF context available in guardrail; brief references the "federation crest" (adidas-supplied crest per scrape says "club crest," which for a national team = federation crest; used "federation crest" for accuracy). Colors: green, black, gold from the flag per guardrail. Did NOT adopt the existing collection-page FAQ's "yellow, green, black" framing (that describes home kits); this away is black-based per scrape, so brief anchors flag palette + this shirt's black base without overclaiming accent colors.

## Internal links (validated via Firecrawl content signals)
1. https://www.prosoccer.com/collections/jamaica -- 200; H1 "Jamaica National Soccer Team Jerseys, Apparel & Gear"; 11 products; title confirms Jamaica NT collection. Anchor: "Jamaica national team collection." PASS.
2. https://www.prosoccer.com/collections/national-teams -- 200; H1 "National Soccer Teams"; 841 products; Jamaica in filter (11). Anchor: "national team jerseys collection." PASS.
Both body-only, full HTTPS with www, in the "Who it's for" H2. PDP internal-links-only policy honored (no external links). Short Description carries ZERO links.

## Gate self-verification
- Gate 1 self-verify: PASS (scrape re-read, sources match).
- Gate 2 voice_check.py: PASS (no em/en-dash, no forbidden words/openers, adidas lowercase incl. sentence-start "adidas" checked, no UK "boots," editorial H2s sentence case, structural H2s Title Case).
- Gate 3 sourcing: PASS.
- Gate 5 avatar: primary Carlos (the fan) + diaspora fan, Desire/Action AIDAR; secondary Tyler (authentic player-spec fit) light touch; Jennifer/Mike-Coach excluded (adult self-purchase national jersey, not parent/bulk). 
- Gate 9 positioning lift-test: PASS (Reggae Boyz + diaspora + France 1998 heritage + authentic-vs-Stadium expertise cannot be lifted onto a generic retailer unchanged).
- Gate 10 emotion-first: PASS (Short Desc + overview H2 lead with belonging/identity; specs support).
- Gate 11 brand IP: PASS (evergreen, no WC wordmark, no "only," debut framing).
- Gate 12 keyword distribution: PASS (primary across Title/Short/Meta Title/Meta Desc/body H2 + body; ~3 exact primary in body, within ceiling; one volume-selected supporting; colorway long-tail single carve-out).
- Gate 13 anti-stuffing: PASS (no comma-stacks, no price-stacking in body, no brand-stacking; H2 casing split correct; "Product Details: Jamaica Authentic Away Jersey" Title Case).
- Gate 14 unsupported counts: PASS (only verified specifics: France 1998, 2-1, Whitmore two goals).
- US-first dual units: PASS ("86°F (30°C)" in Care).
- Care H2: present (jersey category triggers it), bullets, after Fit Notes, inside-out/cold/no-softener/badge-heat notes.
- FAQ hierarchy: "FAQs about the Jamaica Authentic Away Jersey" H2 (short-name pattern), H3 per question, paragraph answers, 4 Q&As net-new-value (tier diff, sizing, colors, licensing), placed last.
- Length: national-team-jersey class (jersey Complex exception; holds jersey-set norm, evergreen fan-identity body). Not trimmed to cleat ceiling per the jersey-length clarification.

## Tool spend (this session)
Firecrawl: 3 scrapes (PDP + 2 internal-link validations) = 3 credits. DataForSEO: 0 (KIRA Phase 1 supplied keyword data). GSC: 0 (KIRA supplied). Within envelope.

## Held items for ORIN
- Sold-out at scrape time; no Mike exception flag requested -> evergreen fan copy, no stock chrome. Confirm if Mike wants a closing-window/collection-redirect treatment.
- Difficulty cell blank for all keywords (DataForSEO returned no reliable KD for the Jamaica family). Correct per "leave blank, don't fabricate."
