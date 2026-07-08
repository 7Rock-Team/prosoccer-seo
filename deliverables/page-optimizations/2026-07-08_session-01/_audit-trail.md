# Audit Trail -- Batch 6 (2026-07-08, session-01)

Workforce-internal per-batch audit. Detailed per-SKU audit content (classification reasoning, topic research, data provenance, per-string gate status) lives in each SKU's SCRIBE briefing at `.claude/agents/on-page-seo/briefings/2026-07-08_*.md`; this file is the batch index and ORIN's gate record.

## Batch Metadata
- Total SKUs: 10 (5 cleats, 5 jerseys)
- Waves: Wave 1 = 4 exemplars/foundationals (this file, gated); Wave 2 = 6 (dispatched after Checkpoint 2b)
- Dispatch architecture: one SCRIBE agent per SKU, parallel within each wave; Mechanism A + B handoff (structure skeleton + forbidden-phrasings) to Wave 2, no exemplar prose
- Pre-dispatch: silo guardrails commit 70bc999; locked primaries + differentiation spec commit ef5f937
- Firecrawl: healthy; Phase 0 scrape-wins live for every SKU
- Registry 1 handoff: 10 locked primaries surfaced for the white-label team's PDPs-tab entry (4 GSC-override/protected terms flagged); write ownership stays with the white-label team

## Cross-batch cannibalization resolution (Registry 1 + 2 cross-check)
Three hard cross-batch collisions caught and resolved before dispatch: the Shadow cleats would have cannibalized their shipped Breakout twins on the generic model-tier-surface primary. Resolution: Shadow SKUs take pack-specific primaries, ceding the generic to the shipped Breakout page.
- HJ2147 (Shadow) vs IH1779 (Breakout, `nike phantom 6 elite fg`) -> `nike phantom 6 high elite fg shadow`
- HQ2329 (Shadow) vs IQ1869 (Breakout, `nike phantom 6 high elite ag`) -> `nike phantom 6 high elite ag shadow`
- IF8512 (Shadow) vs IO8225 (Breakout, Vapor 17 Pro model term) -> `nike vapor 17 pro shadow`

## Wave 1 per-SKU audit notes (gated 2026-07-08)

### IR4192-661 -- Nike Jr Phantom 6 Low Pro FMG (Tier 1 foundational: first junior + first FMG)
- Primary: `nike jr phantom 6 low pro` (110/mo; KD not returned, cell blank, not fabricated). Complexity: Complex, Pro-tier band (~365 words).
- Brand-IP: non-adidas (Nike cleat), non-FIFA (moot for a cleat); scan clean.
- Differentiation lane: parent / developing-player milestone (KI0662 precedent, adapted to Phantom control not Copa touch); FMG "goes anywhere the weekend does" versatility.
- Scrape-wins: FMG plate + Junior Pro tier confirmed; no stud count; $149.99 kept OUT of body (tier language only, evergreen-ness held).
- Links (2, content-validated, body only): `/collections/nike-phantom` (166 products), `/collections/nike-soccer-shoes-cleats` (143 via canonical). Rejected soft-404/404: youth-/kids-/junior-soccer-cleats (see follow-ups: junior collection gap).
- ORIN gate: PASS (independent file read). Handle 78 chars, over target: no change without a 301 coordinated with Misha (flagged).

### HJ2147-001 -- Nike Phantom 6 High Elite FG Shadow (Shadow-cleat family exemplar)
- Primary: `nike phantom 6 high elite fg shadow` (110/mo, GSC-protected). Pack-secondary: `nike shadow pack` (210). Complexity: Complex/Elite (~432 words, under 465 ceiling).
- Brand-IP: non-adidas, non-FIFA; zero FIFA-family tokens ("FA26" is a Nike season code).
- Differentiation lane: disguise of the pass; "the shadow the defense loses on the blind side."
- Anti-convergence: verified vs the shipped IH1779 Breakout log entry; zero carry-forward of the strike-moment hook or the marksman/rehearsed-aim metaphor.
- Scrape-wins: colorway Black/Black/Illusion Green; weight bullet omitted (scrape supplied none).
- Links (1, content-validated, body only): `/collections/nike-shadow-soccer-cleats` (required pack link); did not target its keyword term. `/collections/nike-phantom` validated but held to keep one load-bearing link.
- ORIN gate: PASS (independent file read). Serves as the Wave 2 structure-skeleton + forbidden-phrasings source.

### II1663-453 -- Nike 2026-27 Chelsea Youth Stadium Home (first club under Registry 2)
- Primary: `chelsea youth jersey` (170/mo, KD 14). Pack-secondary: `chelsea 2026/27 home jersey`. Body ~507 words (jersey-class exception; shipped Croatia set 507-534).
- Brand-IP / competition naming (club-team-jerseys.md policy): Premier League named directly ("Five Premier League titles"); Champions League generic ("two-time European champions," "European nights"); no PL/UEFA logos, no "official" phrasing. "EPL sleeve patch" is a factual scrape-confirmed customization option (audit line 25), nominative use, not a competition claim.
- Differentiation lane: club belonging (the young Blue, passed-down/self-claimed loyalty), not national pride. Liverpool anti-collision clean (young-Blue vs title-kit; no Hillsborough/farewell).
- Scrape-wins: Bright Blue / Midwest Gold; Dri-FIT (Stadium replica, NOT Aero-FIT); rampant-lion woven crest; youth YXS-YXL.
- Links (2, content-validated, body only): `/collections/cole-palmer` (13 products, player-spotlight preference), `/collections/chelsea` (58 products).
- ORIN gate: PASS. Fix applied at gate: lowercase "the chelsea youth jersey" -> "the Chelsea youth jersey" (proper-noun capitalization; SCRIBE Phase 4 / ORIN gate scope, not a voice_check gap).

### DRCHRM25 -- Umbro 2026 DR Congo Men's Authentic Home (NT exemplar for the pair)
- Primary: `dr congo jersey 2026` (140/mo; KD not returned, blank, not fabricated). Pack-secondary: `dr congo home kit 2026`. Body 615 words (jersey-class exception; Away mirror to trend leaner ~534).
- Brand-IP: Umbro non-adidas -> FIFA / "World Cup" FORBIDDEN. Independent full re-read: zero FIFA/WC terms in any field. Qualification via substitution only ("sealed their place in the 2026 international tournament"); "the finals as Zaire," never "1974 World Cup."
- Differentiation lane: Les Léopards home heritage-pride, sky-blue identity; Authentic (match-spec) tier vs replica.
- Scrape-wins: variant label "Light Blue" -> wrote "sky blue with gold and red flag accents"; did NOT assert a leopard-print motif (not scrape-confirmed on this render). Authentic confirmed (title + "100% Authentic" badge).
- Links (1, content-validated, body only): `/collections/dr-congo-national-soccer-team-jerseys-apparel`; PDP primary kept year-specific to avoid cannibalizing the collection's generic "DR Congo soccer jersey."
- ORIN gate: PASS (independent full re-read for FIFA compliance).
- Live-page finding (escalated, see follow-ups): current live PDP body contains "worn at the FIFA World Cup 2026" (fixed by this brief on implementation); site-wide WC theme banner is theme chrome (Misha).
- Taxonomy node flagged as not standardized (see follow-ups); Wave 2 jerseys to match.

## Wave 2 (dispatched after Checkpoint 2b; gate record to follow at Checkpoint 3)
- #8 HJ2146 Low Elite FG Shadow, #9 IF8512 Vapor 17 Pro FG Shadow, #10 HQ2329 High Elite AG Shadow (mirror HJ2147 structure, distinct facets, own Breakout-twin bars)
- #4 DRCARM25 DR Congo Away (mirror DRCHRM25, away-day/roaming lens)
- #1 KB7474 Jamaica Away (Tier 2A NT canonical, adidas FIFA-permitted-but-evergreen, Authentic)
- #3 IU3861-679 Korea Home (Tier 2A NT canonical, Nike non-FIFA, Stadium)
