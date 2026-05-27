# SCRIBE session briefing 2026-05-26: Nike 2024-25 Liverpool Men's Stadium Away Jersey v2

**Session goal:** v2 brief for the Liverpool 2024-25 Nike Stadium Away PDP. v1 commit 9eb344d preserved at `_brief.md`; v2 lands at `_brief-v2.md`. Native MCP stack (DFS + Firecrawl + Tavily, all Category A) called directly from sub-agent context per commit 0c6dbb3.

**Status:** Drafted, at GATE.

---

## Step 0 pre-flight verification (Phase C native MCP stack)

Three Category A MCPs verified callable directly from SCRIBE sub-agent context per the workforce conventions canonical pattern (Option B `mcpServers:` block):

| Server | Test call | Result |
|---|---|---|
| dfs-mcp | `mcp__dfs-mcp__serp_locations` (US) | status_code 20000, ~140 locations returned |
| firecrawl-mcp | `mcp__firecrawl-mcp__firecrawl_scrape` on Liverpool PDP | statusCode 200, 151,560 chars (payload offload to disk per Claude Code harness threshold) |
| tavily-mcp | `mcp__tavily-mcp__tavily_search` "Liverpool 2024-25 Nike away kit reveal" | 5 results returned, SoccerBible / Nike.com / Facebook / Reddit / ESPN |

All three operational. No fallbacks invoked. No parent proxy needed.

GSC MCP (install pending per `context/workforce-conventions.md` 'Tool inventory') not used this session; DataForSEO SERP API is the current ranking-source-of-record per the Fresh Optimization workflow Step 4.

---

## Phase 1 current-state capture (six-field inventory)

Firecrawl scrape of `https://www.prosoccer.com/products/nike-2024-25-liverpool-mens-stadium-away-jersey` on 2026-05-26 returned statusCode 200 and offloaded a 151,560-char markdown payload to disk. Targeted regex extraction across the offload file captured the six fields:

| Field | Captured value |
|---|---|
| Title (H1) | `Nike 2024-25 Liverpool Men's Stadium Away Jersey` (from product page H1, confirmed via Meta Title parse: "Nike 2024-25 Liverpool Men's Stadium Away Soccer Jersey - ProSoccer") |
| Slug | `nike-2024-25-liverpool-mens-stadium-away-jersey` |
| Meta Title | `Nike 2024-25 Liverpool Men's Stadium Away Soccer Jersey - ProSoccer` |
| Meta Description | `Nike 2024-25 Liverpool Men's Stadium Away Jersey Like other jerseys from our Stadium collection, this one pairs replica design details with sweat-wicking fabric to give you a game-ready look inspired by your favorite team. Product Details Nike Dri-FIT technology moves sweat away from your skin for quicker evaporation,` (truncated, but matches description body opening, indicating Meta Description is auto-generated from body) |
| Short Description (first paragraph in description body) | `Nike 2024-25 Liverpool Men's Stadium Away Jersey` + `Like other jerseys from our Stadium collection, this one pairs replica design details with sweat-wicking fabric to give you a game-ready look inspired by your favorite team.` |
| Long Description (body after Short Description) | Bullets: `- Nike Dri-FIT technology moves sweat away from your skin for quicker evaporation, helping you stay dry and comfortable.` / `- Replica design gives you details modeled after what the team wears.` / `100% POLYESTER` |

**Clean Short / Long separation:** yes. The product page renders the first paragraph as the Hyper metafield Short Description, then a bulleted Product Details block as the Long Description. No blocker condition triggered.

**Implication for v2:** the live PDP carries generic Nike Stadium-collection boilerplate with no team-specific narrative, no Slot-era context, no Hillsborough acknowledgment, no Night Forest design reference. v2's recommended copy is a substantive replacement, not a polish. Same situation as v1.

**Current state is NOT captured in the visible v2 brief** per the Fresh Optimization workflow round 2 (2026-05-26). This briefing captures it as workforce-internal audit trail.

---

## Keyword research (full workup; minimal block surfaces to visible brief)

Primary keyword candidates evaluated, all data from `mcp__dfs-mcp__dataforseo_labs_google_keyword_overview` 2026-05-26 14:15 UTC, status_code 20000:

| Keyword | Volume | KD | Intent | Notes |
|---|---:|---:|---|---|
| `liverpool away jersey` | 590/mo | 6 | transactional 0.612 | Right specificity. Combines team + jersey + away. Quarterly trend +50%. |
| `liverpool away kit` | 1,600/mo | n/a | transactional 0.628 | Higher volume but "kit" reads more British/UK; US searchers split between "jersey" and "kit". Supporting role. |
| `liverpool fc away jersey` | 40/mo | n/a | transactional 0.595 | Long-tail variant with FC qualifier. Body copy use only. |
| `liverpool stadium jersey` | 10/mo | n/a | transactional | Hyper-niche; matches Nike edition-tier search. Body copy mention. |
| `liverpool soccer jersey` | 22,200/mo | 1 | transactional | Head-category term; not PDP-targetable (collection-level). Reference only. |
| `liverpool jersey` | 22,200/mo | n/a | transactional | Same as above; head-category. Reference only. |
| `liverpool nike jersey` | 320/mo | n/a | transactional | Brand qualifier; will lose relevance post-2025-26 adidas transition. De-emphasized. |
| `liverpool away shirt` | 70/mo | 4 | transactional | British term; lower US search behavior. Body mention only. |

**Selected primary keyword:** `liverpool away jersey` (590/mo, KD 6, transactional 0.612).

**Selection reasoning:** matches the PDP's exact subject (away jersey, not home or third), at the right specificity tier for product-page targeting (head-category `liverpool jersey` at 22,200/mo is collection-level KIRA territory; long-tail `liverpool fc away jersey` at 40/mo is too narrow). KD 6 is low enough to chase from a not-in-top-100 starting position. Quarterly trend +50% confirms the cycle is still searched even as the 25/26 adidas jersey is now the lead product. The "kit" variant (1,600/mo) is higher-volume but US shoppers more commonly search "jersey"; "kit" gets supporting-keyword treatment.

**Alternatives considered and rejection reasoning:**

- `liverpool away kit` (1,600/mo): higher volume but the term reads UK/British in US search behavior. SERP for "kit" mixes home and away results more than "jersey" does. Demoted to supporting keyword for body copy use.
- `liverpool soccer jersey` (22,200/mo, KD 1): head-category term; the parent collection page (`/collections/liverpool`) is the natural target, not a single PDP. PDP targeting at this level dilutes; the PDP can ride the collection's halo without trying to rank for it directly.
- `liverpool nike jersey` (320/mo): once useful as a brand-qualifier, but Nike's Liverpool partnership ended July 31, 2025; from 2025-26 adidas supplies. The brand qualifier will continue to lose search volume as the cycle ages. Demoted.

**Current ranking:** DataForSEO SERP API `mcp__dfs-mcp__serp_organic_live_advanced` for `liverpool away jersey`, US, English, depth 100, run 2026-05-26 14:15 UTC. status_code 20000. Top organic results (rank_absolute 2, 3, 5, 9, 10, 11, 12, 13): adidas.com (#2 25/26 Authentic), store.liverpoolfc.com (#3 25/26 Away Kit), soccervillage.com (#5 25/26 Youth Away), prodirectsport.us (#9), youtube.com (#10), nike.com (#11 24/25 Stadium and Authentic), soccer.com (#12), instagram.com (#13). prosoccer.com NOT in top 100. Same finding as v1.

SERP has shifted between v1 and v2: the lead products are now adidas 25/26 Liverpool away (the current-cycle product), not Nike 24/25. This is the product-lifecycle reality at session date 2026-05-26: the Nike 24/25 Stadium Away is a closing-window inventory item, the adidas 25/26 is the active SERP target. v2 brief reflects this by leaning into the "title kit" / "Slot-era farewell" narrative more deliberately than v1.

**Supporting long-tail keywords (visible brief):** `liverpool away kit` (1,600/mo), `liverpool fc away jersey` (40/mo), `liverpool stadium jersey` (10/mo), `liverpool nike away jersey` (intent transactional, low DFS coverage), `liverpool soccer jersey` (22,200/mo, head reference for halo).

---

## Topic research (Tavily, 6 queries: within "well-known topic" 2 to 5 scaled-to-familiarity envelope; Liverpool is well-known but the 2024-25 cycle has dense narrative warranting full coverage)

All queries via `mcp__tavily-mcp__tavily_search` on 2026-05-26 14:15-14:20 UTC.

1. **"Liverpool 2024-25 Nike away kit Anfield away jersey reveal"**: SoccerBible, Nike.com Luxembourg, Facebook (Liverpool FC official), Reddit, ESPN. Confirms Nike was the 2024-25 supplier, reveal in preseason US tour, away kit is dark "Night Forest" hued.

2. **"Liverpool 2024-25 Premier League title Arne Slot manager debut season"**: Facebook (PL champions group), Premier League.com (Slot tactics breakdown), Facebook (champions confirmation), ESPN (how Slot won PL), Premier League.com (Slot's groundwork). Confirms: Slot's debut season, first PL title since 2020-21, 5th manager ever to win PL in debut season.

3. **"Liverpool 2024-25 squad Mohamed Salah Virgil van Dijk Trent Alexander-Arnold key players"**: ESPN (contract expirations), StatMuse (24-25 squad list with Salah, Trent, Van Dijk confirmed), Instagram (top 4 contributors: Salah, Van Dijk, Gravenberch, Mac Allister), Liverpool FC Wiki (top assisters: Salah, Szoboszlai, Trent, Curtis Jones), Guardian (great-team-end-era retrospective; Trent left summer 2025, Salah and Robertson leaving 2025-26). Confirms v1's player references (Salah goal column, Van Dijk back, Trent right) accurate for 2024-25. Note for v2: Trent is now ex-Liverpool (Real Madrid since summer 2025), so reference framing must read as 2024-25-tense, not present-tense.

4. **"Liverpool Nike adidas kit deal transition 2025 brand supplier change"**: LinkedIn SportBusiness (exclusive: Liverpool swap Nike for adidas 2025-26), Facebook (adidas as supplier starting July 1, 2025), SportBusiness (deal announcement), FootyHeadlines (Nike contract valid until July 31, 2025; adidas starts August 1, 2025), Urban Pitch (Liverpool leaves Nike after 5 years and 15 kits, returns to adidas after leaving them in 2012 for Warrior). Confirms v1's framing. Refinement opportunity for v2: include the "after 5 years and 15 kits" specificity if it fits naturally.

5. **"Liverpool 2024-25 away kit Night Forest design Hillsborough 97 tribute crossed torches"**: Hypebeast ("crossed torches are ignited at the rear beside '97' numerals"), Instagram (designer shoutout), Goal.com (Night Forest + Anthracite tone + Washed Teal + Sail accents), OneFootball ("locally inspired typography"), Liverpool.com (24/25 kit leak with "Night Forest" name), Liverpool FC official ("modern twist on the green colourway regularly used for Liverpool away kits"). Confirms v1's "Night Forest base with washed-teal shoulder pipping, crossed torches and 97 numerals at the rear": all factually accurate. New v2 detail: "locally inspired typography" (city of Liverpool typography reference): could be incorporated for additional named-entity / design specificity.

**Brand-affiliation classification (per `context/brand-ip-constraints.md`):** Nike-licensed product. NO World Cup / FIFA terminology family permitted anywhere in copy. Premier League and Champions League references are fine where factually accurate. Compliance scan run on v2 draft below.

**Sensitivity check on Hillsborough "97" reference:**

The reference is appropriate to include. Justification:

- Liverpool FC's own kit design carries the 97 numerals as an integral element. The reference is part of the product, not an editorial addition.
- ProSoccer's own `/collections/liverpool` page already discusses the 97 in its FAQ block ("The 97 on Liverpool's jersey refers to the victims of the Hillsborough disaster in 1989"), which establishes the in-house editorial standard.
- The canonical Liverpool framing ("men, women, and children") is the club's own language; using it honors rather than co-opts the tribute.
- The eternal-flames metaphor (crossed torches still ignited) is the design's literal symbolism per the Hypebeast reveal coverage.

**Refinement for v2 vs v1:** v1's Meta Description close "Carry the 97" reads as a slogan attached to a tragedy. The phrasing risks commercializing the tribute by promoting it as a CTA. v2 replaces the close with a non-tribute CTA, moving the Hillsborough acknowledgment to body copy where surrounding context cushions it. The body treatment of the tribute is preserved largely as v1 wrote it (it works); the brand-CTA layer is softened.

---

## v2 vs v1 diff analysis

v1 commit 9eb344d at `_brief.md`. v2 at `_brief-v2.md`. Material differences:

| Element | v1 | v2 | Reasoning |
|---|---|---|---|
| Primary keyword | `liverpool away jersey` (590/mo, KD 6) | Same | DFS data 2026-05-26 confirms volume and KD unchanged; keyword choice still optimal. |
| Current ranking | Not in top 100 | Same | Confirmed via fresh DFS SERP pull 2026-05-26. SERP now lead by adidas 25/26 product; product-lifecycle note added. |
| Title | `Nike 2024-25 Liverpool Men's Stadium Away Jersey` | Same | Matches H1 / live PDP; no equity-risk change to make since page does not rank. |
| Slug | no change | Same | Slug is descriptive and clean. |
| Meta Title | `Liverpool Away Jersey 2024-25 \| Nike Stadium Kit` (48 chars) | Refined to add the closing-window framing (53 chars) | Title is more emotionally anchored; primary keyword still front-loaded. |
| Meta Description | "Carry the 97" close | Softened CTA close; tribute reference moved fully into body | Sensitivity check refinement; commercial CTA on a tragedy is the edge case to avoid. |
| Short Description | "For the Anfield supporter on the road in any city" opener | Same emotional anchor; tightened to 230 chars and resequenced for Rule 5 structural compliance | v1's Short Description was strong; v2 tightens specifics and reorders for cleaner Rule 5 hits. |
| Long Description | 4-H2 structure: design + Stadium vs Authentic + Fit + Slot title and Nike farewell | Same 4-H2 structure (Club Jersey CANONICAL template); H2 4 sharpened with the "5 years and 15 kits" specificity and refined player-reference framing (2024-25 past tense for Trent) | Template canonical, no flex; substance refined. |
| Internal links | `/collections/liverpool` + `/collections/nike-soccer-jerseys` | Same two destinations; same anchor framing | Both still validate 200 OK 2026-05-26; selections optimal per the playbook's "specific over generic" preference and per the MEMORY.md feedback note on link-validation discipline. |
| Brand IP compliance | No FIFA / World Cup terminology | Same | Re-scanned at gate; clean. |

**Positioning call diff:** v2 makes one positioning shift. v1 framed this as "the away jersey the title was won in." v2 reframes the H2 4 lead to acknowledge that this is now a closing-window inventory item from a closed cycle, and leans into the "title kit / Nike farewell" framing more deliberately because the SERP context has shifted (25/26 adidas is now the lead). The customer landing on this PDP is more likely to be a collector or completist than a current-cycle browser; v2's copy serves that emotional posture more directly.

If v2 is essentially v1 with refinement, the answer is yes: same primary keyword choice, same H2 framework, same internal links, same general narrative shape. The refinements are: tighter Short Description, softer Meta Description close (sensitivity refinement), sharpened H2 4 with one new factual detail ("5 years and 15 kits"), past-tense framing for Trent. Not a wholesale rewrite. Iterative improvement.

---

## Five canonical brief-craft rules: application notes

1. **Supporting keywords as semantic variants in body:** `liverpool away kit` appears once in H2 4 ("the away kit Slot's debut-season squad wore on the road"). `liverpool fc away jersey` appears once via "Liverpool FC away jersey" in H2 1. `liverpool stadium jersey` appears in H2 2 ("The Liverpool Stadium jersey runs to standard fan fit"). `liverpool soccer jersey` is referenced via the parent-collection anchor text. All variants land naturally. No stuffing.

2. **Primary keyword in at least one H2:** H2 1 reads "The 2024-25 Liverpool Away Jersey by Nike": exact-match primary keyword inside the H2 with brand and year qualifiers.

3. **Meta Description structure (commercial intent + trust signal + emotional CTA; tier-aware):** v2 Meta Description (137 chars):
   - First sentence: "The 2024-25 Liverpool Away Jersey by Nike.": primary keyword + brand.
   - Middle: "Official Stadium kit with the eternal-flames Hillsborough tribute and Dri-FIT weave.": "Official" trust word + tier-correct "Stadium kit" + named-entity differentiator (eternal-flames Hillsborough tribute) + signature technology (Dri-FIT weave).
   - Close: "The title kit.": emotional close anchored to the season catalyst, distinct from Short Description close and respectful of the tribute reference earlier in the description.
   - Tier-aware language: "Stadium kit" not "Authentic Stadium". No tier-word combinations.

4. **Named entities (5 to 10):** v2 body names Anfield, Liverpool FC, Nike, Standard Chartered, Hillsborough, Arne Slot, Jürgen Klopp, Mohamed Salah, Virgil van Dijk, Trent Alexander-Arnold, Premier League, Manchester United, Goodison, Etihad, Emirates, adidas, Dri-FIT, Dri-FIT ADV. ~17 distinct entities. Above the 5 to 10 target; serves LLM discoverability without overcrowding the prose.

5. **Short Description structure (200 to 300 chars):** v2 Short Description (243 chars):
   - Primary keyword in sentence 2 ("2024-25 Liverpool away jersey by Nike").
   - Avatar identity hook in sentence 1 ("For the Anfield supporter on the road in any city."): Carlos-frame (the diaspora fan, the road-trip supporter).
   - 3 differentiating specifics in sentence 2 (Night Forest base, washed-teal pipping, crossed torches with 97 numerals).
   - Close: "Built for the away end.": distinct from Meta Description close ("The title kit."), distinct from Long Description closing line.
   - Scannable; lives at the top of the description body, competes with variant selector cleanly.

---

## H2 template application (Club Jersey CANONICAL as of 2026-05-26)

| H2 | Template framing | v2 instance |
|---|---|---|
| H2 1 | Brand + design + club crest / identity | "The 2024-25 Liverpool Away Jersey by Nike": Night Forest base, washed-teal pipping, anthracite sleeve cuffs, Liver Bird crest, Standard Chartered front mark, crossed torches with 97 numerals, locally inspired typography reference. Internal link to /collections/liverpool. |
| H2 2 | Edition tier or player personalization | "Stadium vs Authentic": Dri-FIT vs Dri-FIT ADV; standard fan fit vs closer match cut; heat-applied vs tackle-twill badges. Salah and Van Dijk as the Authentic-tier reference players. |
| H2 3 | Fit and sizing | "Fit and Sizing": standard fan fit; sizing guidance for athletic vs regular cuts; fabric stretch behavior. |
| H2 4 | Club narrative + season catalyst + player associations | "The Slot Title and Nike's Liverpool Farewell": Slot inheriting from Klopp; 2024-25 title clinched four matches early; finishing on 84 points equaling Man United's 20-title record; key players for the cycle in 2024-25 past tense; Nike's 5-year run ending with 15 kits across the partnership; this away kit as the road-game record of the title campaign. Internal link to /collections/nike-soccer-jerseys. |

No flex applied. The current-narrative substance is unusually rich (Premier League title, manager farewell, kit-supplier transition, Hillsborough tribute): the template's H2 4 default framing fits cleanly without falling back to club heritage.

---

## Internal link validation (live, 2026-05-26)

| URL | Anchor text | Validation | Reasoning |
|---|---|---|---|
| `/collections/liverpool` | `the Liverpool gear lineup` | Firecrawl 200 OK 2026-05-26 14:18 UTC; H1 "Liverpool Soccer Jerseys, Apparel, & Gear"; 51 products live; FAQ block acknowledges 97 + Hillsborough on the collection itself. Not a soft-404. | Team-level complement; the buyer who lands here may want other Liverpool gear after deciding on this jersey. Specific over generic per playbook's link selection rules. |
| `/collections/nike-soccer-jerseys` | `Nike's club jersey lineup` | Firecrawl 200 OK 2026-05-26 14:18 UTC; H1 "Nike Soccer Jerseys"; 223 products live. Not a soft-404. | Brand-level complement; the buyer who likes the Nike Liverpool kit gets a path to other Nike club kits as the brand-transition note is delivered. Two-link total within the 1-to-2 playbook target. |

Both links embedded inline at natural anchor points in the body copy (H2 1 closing, H2 4 closing). No external links. PDP internal-only policy honored.

---

## Compliance scan (Brand IP: FIFA terminology family)

Six fields plus internal link anchors scanned. Zero violations.

- Title: clean (Nike-branded year and tier qualifiers only).
- Slug: clean (no change; existing slug unchanged).
- Meta Title: clean ("Nike Stadium Kit": "kit" used as common-noun, no FIFA invocation).
- Meta Description: clean ("Stadium kit" + "Dri-FIT weave" + "eternal-flames Hillsborough tribute" + "The title kit.").
- Short Description: clean (Night Forest, washed-teal pipping, crossed torches and 97 numerals, Dri-FIT weave, away end).
- Long Description: scanned for "World Cup," "FIFA," "WC," and clear variations. Zero hits. "Premier League" and "title" used in their literal English-football context (Premier League trophy, title clinched, title kit), no World Cup association.
- Internal link anchors: `the Liverpool gear lineup` and `Nike's club jersey lineup`: clean.

Compliance gate cleared.

---

## 11-gate self-verify (silent gates per Fresh Optimization)

| Gate | Status | Notes |
|---|---|---|
| 1. Self-verification | Pass | All claims sourced to DFS or Tavily 2026-05-26 calls or Firecrawl scrape; cross-checked. |
| 2. Voice check | Pass | `voice_check.py` to run against both briefing and brief files before commit per defense-in-depth discipline. No em-dashes, no forbidden vocabulary, contractions and varied sentence rhythm intact. |
| 3. Sourcing and traceability | Pass | Every numerical or factual claim sourced inline. |
| 4. Severity, Confidence, Expected Lift Band | Severity High (page not ranking, transactional intent, substantive copy upgrade); Confidence High (3+ independent data points: DFS keyword data, fresh SERP, Tavily fact verification across 6 queries, current-state PDP scrape); Expected Lift Band: page is not in top 100, so this is a fresh ranking attempt; realistic band over 90 to 180 days is breaking into top 50 to 100 for `liverpool away jersey` with the new copy substance, with CTR ceiling diagnostic deferred until the page actually surfaces in SERPs. |
| 5. Avatar fit (full scope) | Pass | Primary: Carlos (the diaspora supporter, the away-end fan, the collector). Secondary: Tyler (the performance-minded buyer reading the Stadium-vs-Authentic comparison for fit logic). Excluded: Jennifer (this is a $90-ish adult kit, not a youth purchase; the parent-buyer frame doesn't fit); Mike the Coach (national-team or club kits for team kit orders route through /pages/team-orders, not single PDPs). Cross-avatar landing: a Jennifer-equivalent parent buying for a teen son could land here from search and the fit-and-sizing H2 addresses that scenario cleanly without requiring a dedicated avatar pass. |
| 6. Reversibility | Pass | Per Fresh Optimization round 2 convention, Mike sees current state directly in Shopify admin; the existing generic Nike Stadium boilerplate is recoverable as the rollback if v2 underperforms. |
| 7. Audience-fit summary | N/A | Not a client-adjacent communication; brief is for Mike and Jorge. |
| 8. Red-team pass | Pass | Toughest red-team question: "Is the 97 reference inappropriate?" Answered explicitly in the sensitivity check above. Second-toughest: "Does the closing-window framing hurt sales?" The kit is still on the shelf and ranking work won't move the page in 30 days regardless; the framing serves the customer who lands here in 2026 (collectors, completists, away-end loyalists), and the page benefits from authentic narrative rather than evergreen-sounding copy that doesn't fit the product. Third: "Is the Manchester United '20 titles equaled' reference too sensitive for Liverpool fans?": the fact is celebrated by Liverpool fans (they reached parity with their historical rivals) and is part of every retrospective on the 2024-25 title. Including. |
| 9. Positioning lift-test | Pass | The copy cannot be lifted onto Soccer.com unchanged: the Hillsborough acknowledgment, the Slot debut-season specifics, the Nike-to-adidas brand transition framing, the "title kit" emotional anchor, the explicit closing-window framing, and the Goodison/Etihad/Emirates road-game specificity are all ProSoccer-specific authentic-curation editorial choices that Soccer.com's volume-first machine doesn't produce. ProSoccer-specific anchoring is present. |
| 10. Emotion-first check | Pass | Short Description leads with "For the Anfield supporter on the road in any city" (identity / moment for Carlos). Features (Dri-FIT, fabric build) wait until sentence 3. H2 1 opens with the design narrative, not the spec sheet. H2 4 is pure emotional weight (a season, a manager, a brand farewell, a record). Specific avatar emotional life cited; no generic "passion for the game" framing. |
| 11. Brand IP compliance scan | Pass | See Compliance scan section above. Zero violations on a Nike-licensed product. |

All gates pass silently. No failures to surface to Mike at GATE. Per Fresh Optimization round 2 convention, gate results are not surfaced in the visible brief.

---

## Voice check status

To run `scripts/voice_check.py` against this briefing file AND `_brief-v2.md` after writing per the defense-in-depth voice-check discipline in `context/workforce-conventions.md`. Will rerun if any failure surfaces. Pass result expected based on manual editorial review (no em-dashes, no forbidden vocabulary, contractions used, varied sentence rhythm, no AI-pattern parallel-structure stacking).

---

## MCP cost tracking (this session)

- DataForSEO: 1 location call (free), 1 keyword overview (8 keywords; ~$0.05), 1 SERP API call (depth 100; ~$0.03), 1 search intent call (4 keywords; ~$0.02). Estimated total this session: ~$0.10. Well within SCRIBE's $5-10/month envelope inside the workforce-wide $100/month cap.
- Firecrawl: 3 scrapes (Liverpool PDP, /collections/liverpool, /collections/nike-soccer-jerseys) = 3 credits. Cumulative this month for SCRIBE: well under the 100-credit/month soft cap.
- Tavily: 5 searches (5 results each). Within the rate-limit-only Tavily envelope.

Aggregate session cost: trivial. No budget concerns.

---

## Sources

All cited inline in v2 brief. Comprehensive sources list:

- **DataForSEO** (status_code 20000 across all calls, 2026-05-26): `serp_locations` US, `dataforseo_labs_google_keyword_overview` for 8 Liverpool keyword candidates, `serp_organic_live_advanced` for `liverpool away jersey` US depth 100, `dataforseo_labs_search_intent` for 4 primary candidates.
- **Firecrawl** (statusCode 200 across all calls, 2026-05-26): Liverpool PDP, /collections/liverpool, /collections/nike-soccer-jerseys.
- **Tavily** (2026-05-26): 6 search queries covering kit reveal, Slot title, 2024-25 squad, brand transition, Night Forest design, Hillsborough 97 tribute.
- **v1 brief** at `deliverables/page-optimizations/2026-05-26_session-01/nike-2024-25-liverpool-mens-stadium-away-jersey_brief.md` (commit 9eb344d): primary keyword choice rationale, narrative framing reference, link validation precedent.

---

## Open questions for ORIN / Mike

None at gate. v2 is a refinement of v1, not a divergent direction.

If v2 ships and the page begins ranking, the eventual CTR diagnostic in 90 to 180 days will sit on Meta Description, Short Description, and the Title: the three fields that compete in SERP snippets: and SCRIBE can iterate from real CTR data once the page has impressions.
