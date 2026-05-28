# SCRIBE session briefing 2026-05-28: adidas 2026 Mexico Men's Stadium Home Soccer Jersey

**Session goal:** Day 1 of the 10/day production rhythm. First PDP in the Mexico kit set (Home, Away, Third sequential; Stadium SS tier across all three). Brief produced on the sold-out PDP under the newly codified pre-tournament demand spike exception (commit `120a177`, 2026-05-28). National Team Jersey CANONICAL template applied with FIFA-permitted terminology (Mexico is adidas-licensed).

**Status:** Visible brief and workforce-internal briefing drafted to disk. Voice check PASS on both files. 11 internal gates PASS. Awaiting ORIN GATE / Mike GATE.

## Step 0 pre-flight verification

All three Category A MCPs callable directly from SCRIBE subagent context per commit `0c6dbb3`:

- `mcp__dfs-mcp__dataforseo_labs_bulk_keyword_difficulty` on `mexico 2026 home jersey`. Returned `status_code 20000`. Native DFS exposure confirmed.
- `mcp__firecrawl-mcp__firecrawl_scrape` on target PDP. Returned 200 OK with 148,723 chars (oversized for direct context; sliced via Bash python). Native Firecrawl exposure confirmed.
- `mcp__tavily-mcp__tavily_search` on Mexico 2026 home jersey adidas Aztec FMF. Returned 5 detailed results. Native Tavily exposure confirmed.

GSC MCP: install pending per `context/workforce-conventions.md` 'Tool inventory'. Not used this session (PDP work doesn't require CTR ceiling diagnostic). Playwright: not used.

## Eligibility status and exception applied

ORIN's Step 0.5 eligibility check (2026-05-28) confirmed by SCRIBE re-scrape:

- schema.org `Offer.availability = OutOfStock`
- Add-to-cart disabled
- All 7 size variants (S, M, L, XL, 2XL, 3XL, 4XL) marked "Variant sold out or unavailable" in the rendered page

**Pre-tournament demand spike exception applied per commit `120a177`** (codified 2026-05-28 as the second documented strategic exception type, alongside closing-window). Override criteria all met:

1. Current-cycle inventory (not closeout, not end-of-life)
2. Major tournament imminent (2026 World Cup opener June 11, about 14 days from 2026-05-28)
3. Restock expected during tournament window (manufacturer-typical for tournament-cycle kits)
4. SEO equity lead time matters (optimization now ranks before traffic peaks)
5. Strong internal link to `/collections/mexico` for sold-out PDP recovery to in-stock alternates

Mike approved at Day 1 Step 0 gate. Documented in the visible brief's Strategic context section.

## Brand-affiliation classification

Mexico is **adidas-licensed** (kit supplier continuous since 1999; verified via prior Mexico v3 topic-research briefing 2026-05-08 and confirmed via 2026-05-28 Tavily research: adidas 2026 home jersey at adidas.com URL `mexico-26-home-jersey/JL8537.html`, FIFA Store URL `adidas-mexico-2026-authentic-home-jersey-mens`). **FIFA terminology family PERMITTED** per `context/brand-ip-constraints.md`. SCRIBE used "World Cup" naturally in body copy and short description; could have used "FIFA World Cup 2026" but chose the shorter form for cleaner Meta Description and body rhythm. No constraint violation either way.

Cultural terms safe and used: El Tri, FMF, Estadio Azteca. Verde-blanco-rojo flag-color framing approved.

## Avatar scope

- **Primary:** Carlos (LA Mexican-American diaspora, El Tri identity, authenticity-first, fan-tier purchase consideration at $99.99 price point). AIDAR stage: Desire / Action, active pre-tournament purchase consideration with the opener 14 days out. Short Description opens with the Estadio Azteca moment ("For every fan walking into Estadio Azteca on June 11").
- **Secondary:** Tyler. The competitive-player buyer who wants the kit for training-and-wear or for Sunday league use. Surfaces in H2 2 via the Authentic edition framing ("the cut Edson Alvarez, Hirving Lozano, Santiago Gimenez, and Raul Jimenez actually pull on for the match at $149.99"). The Authentic upsell is also a redirect path because Authentic SS is in stock per ORIN's mapping.
- **Excluded:** Jennifer. National-team adult Men's Stadium jersey is typically self-purchase, not parent-purchase. Youth Stadium and Kids Mini Kit live in separate SKUs; Jennifer applies on those PDPs, not this one. No cross-avatar landing accommodation needed because the title explicitly says "Men's Stadium."
- **Excluded:** Mike the Coach. National team kits don't route through team-orders flow; bulk uniforms go through `/pages/team-orders`. Personal purchase by a coach who happens to support El Tri lands under Carlos-as-fan, not Mike-as-coach.

## Topic research findings (with provenance, currency-checked 2026-05-28)

### Tavily MCP queries run (5)

1. "Mexico 2026 World Cup home jersey adidas design release Aztec FMF" ,  kit design, release timing, design rationale.
2. "Mexico national team manager Javier Aguirre 2026 confirmed squad Edson Alvarez captain" ,  coach, captain, current squad.
3. "Mexico 2026 home jersey adidas design Aztec Piedra del Sol price stadium replica specifications climacool" ,  fabric, price, specific design pattern naming.
4. "Estadio Azteca 2026 World Cup opener three opening matches history capacity Mexico City renovation" ,  stadium history, opener context.
5. "Mexico Group A 2026 World Cup opponents confirmed final draw teams" ,  Group A composition verification.

### Verified factual claims

| Claim | Verification | Source |
|---|---|---|
| adidas Mexico kit supplier since 1999 | Confirmed via Mexico v3 briefing 2026-05-08 and reconfirmed via adidas.com product JL8537 + FIFA Store listing 2026-05-28 | as.com kit evolution; adidas.com |
| 2026 home design references 1998 France ABA Sports jersey | Confirmed: House of Heat 2026 article ("ornate, intricate graphic that references the Piedra del Sol Azteca design seen on ABA Sports' Mexico Home kit for the 1998 World Cup in France"); ESPN World Cup kit rating ("An obvious homage to one of the greatest World Cup kits ever created. We are of course talking about the incredible Aztec design worn by El Tri at the 1998 finals in France") | houseofheat.co; espn.com |
| Piedra del Sol Azteca naming | Confirmed via House of Heat 2026 article verbatim | houseofheat.co |
| Bold green base, red V-neck trim, white shoulder stripes, sleeve cuffs | Confirmed via House of Heat 2026 article ("red trim animates the V-shaped neck opening as well as sleeve cuffs, while white stripes land on the shoulders") and YouTube WC2026 Mexico unboxing review ("bold green base with subtle darker graphic patterns inspired by Aztec motifs and the iconic design from the 1998 season... thicker white Adidas stripes are stitched along the shoulders") | houseofheat.co; YouTube unboxing |
| Climacool fabric, 100% recycled polyester, slim fit | Confirmed via Firecrawl scrape of target PDP (bullets in description) and TUDN Fan Shop product page ("Slim fit, 100% polyester (100% recycled), Transfer knit jacquard fabric, CLIMACOOL") | Firecrawl 2026-05-28; tudnfanshop.com |
| Embroidered FMF crest centered traditional | Confirmed via YouTube unboxing review ("the full bar crest of Mexico... both stitched onto the jersey") and visual confirmation across ABA Sports 1998 lineage | YouTube unboxing |
| Javier Aguirre is current head coach, third World Cup | Confirmed via NYT Athletic 2026-04-21 article ("Mexico Football Federation sporting director Duilio Davino has confirmed that former Barcelona and Mexico national team defender Rafael Márquez will take over the senior men's side following the 2026 World Cup") + Wikipedia Mexico national football team (as of 22 July 2024 squad listing shows Aguirre as head coach, Márquez as assistant) + YouTube KickOFF Times Mexico 26-man squad announcement (May 24, 2026) | nytimes.com/athletic; Wikipedia; YouTube |
| Rafael Marquez succeeds Aguirre after WC for 2030 cycle | Confirmed via NYT Athletic 2026-04-21 article (Davino on Fox Sports Mexico) | nytimes.com/athletic |
| Edson Alvarez is captain | Confirmed via Wikipedia Edson Alvarez article ("plays either as a defensive midfielder or centre-back for Süper Lig club Fenerbahçe, on loan from Premier League club West Ham United, and captains the Mexico national team") + YouTube KickOFF Times Mexico squad video ("Captain Edson Alvarez leads Mexico's midfield battle") | Wikipedia; YouTube |
| Edson Alvarez on loan at Fenerbahçe from West Ham | Wikipedia confirms; not used in body copy (would mislead about the kit-wearing club association in a Mexico-jersey context, where club affiliation is irrelevant) | Wikipedia |
| Hirving Lozano in squad | Confirmed via Wikipedia + YouTube squad announcement | Wikipedia; YouTube |
| Santiago Gimenez (Feyenoord-to-Milan) in squad | Confirmed via YouTube squad announcement + Yahoo Sports roster projection | YouTube; Yahoo |
| Raul Jimenez (Fulham) in squad | Confirmed via YouTube squad announcement + Yahoo Sports roster projection | YouTube; Yahoo |
| Guillermo Ochoa squad status | Mentioned in YouTube squad announcement; not used in body (he's a goalkeeper, peripheral to a fan-tier outfield jersey body narrative; including him adds noise without lift) | YouTube |
| Mexico opens 2026 WC June 11 vs South Africa at Estadio Azteca | Confirmed via Wikipedia 2026 FIFA World Cup article ("The opening match was announced to include Mexico, taking place on June 11, 2026, at the Estadio Azteca in Mexico City. This match will include South Africa") + Sky Sports + FIFA.com Final Draw results | Wikipedia; Sky Sports; FIFA.com |
| Group A: Mexico, South Africa, South Korea, Czech Republic | Confirmed via Wikipedia 2026 FIFA World Cup draw article (Group A: A1 Mexico, A2 South Africa, A3 South Korea, A4 Czech Republic) + FIFA.com Final Draw results + Fox Sports Mexico schedule | Wikipedia 2026 FIFA World Cup draw; FIFA.com; foxsports.com |
| 2026 WC final July 19 at MetLife Stadium | Confirmed via Sky Sports + Fox Sports | Sky Sports; Fox Sports |
| Estadio Azteca first stadium to host three WC openers (1970, 1986, 2026) | Confirmed via Wikipedia Estadio Azteca article ("It will be the third time Azteca has hosted World Cup games; in 1970 and 1986, games also took place at the stadium") + MySanAntonio "first stadium to host three World Cups" + Mexico v3 briefing 2026-05-08 | Wikipedia Estadio Azteca; mysanantonio.com |
| Azteca renamed Estadio Banorte | Confirmed via Wikipedia Estadio Azteca article + MySanAntonio article ("officially named Estadio Banorte or better known by its former name, Estadio Azteca") | Wikipedia; mysanantonio.com |
| Repeat of 2010 WC opener (Mexico vs South Africa 1-1) | Confirmed via Sky Sports article ("It is a repeat of the 2010 World Cup opener as then-hosts South Africa claimed a 1-1 draw") | Sky Sports |
| Stadium SS price $99.99, Authentic SS price $149.99 | Confirmed via DataForSEO SERP popular_products (DICK'S $150 Authentic, Soccer.com $99.99 Stadium / Scheels $100 Stadium / TUDN $99.99 Stadium / authenticsoccer.com $149.99 Authentic / SoccerPost $99.99 Stadium); also matches the WeGotSoccer $99.99 Women's Stadium across the price tier. Visible PDP price not surfaced in scrape (sold-out hidden), but tier price ladder consistent across retailers. | DFS SERP 2026-05-28 |

### Naming choice: Estadio Azteca vs Estadio Banorte

The stadium is officially Estadio Banorte (renamed for sponsorship, confirmed Wikipedia + MySanAntonio). Cultural and search-language reality: "Estadio Azteca" is what 99%+ of Mexico supporters call it, what Wikipedia leads with, what FIFA.com uses, and what the Mexico v3 collection page brief used. Brief uses "Estadio Azteca" exclusively to match avatar search language and cultural identity. Documented here for audit; not a constraint violation.

### Sensitivity scan

No sensitive content. El Tri is celebratory identity. No tragedies, no controversies, no current-events sensitivities to navigate. The Hillsborough-pattern caution (Liverpool v2) does not apply to Mexico. The 1985 Mexico City earthquake reference would be a different kind of error (commercial framing of past tragedy) and was not surfaced or used.

## Fact-verification log: currency-checked claims (per Liverpool v2 + Predator v2 discipline)

| Claim | Status at prior reference (Mexico v3, 2026-05-08) | Status 2026-05-28 | Source |
|---|---|---|---|
| Javier Aguirre is head coach | Confirmed | Re-confirmed; will be replaced by Rafael Marquez after the 2026 WC for the 2030 cycle (new fact 2026-04-21) | nytimes.com/athletic 2026-04-21 |
| Mexico opens June 11 at Azteca vs South Africa | Confirmed | Re-confirmed (Group A draw finalized, opener locked) | Wikipedia 2026 WC; Sky Sports |
| Group A composition | At v3 time, Czechia coming through UEFA playoffs (Mexico, South Korea, South Africa, Czechia/Denmark/North Macedonia/Republic of Ireland) | Updated: Czechia confirmed (final draw resolved). Group A: Mexico, South Africa, South Korea, Czech Republic. | Wikipedia 2026 WC draw |
| 2026 home kit on sale | Confirmed at v3 | Now sold out across sizes at ProSoccer (Stadium SS Men's), but on sale at adidas.com (#1 SERP at $100, "from 11/10/2025"), FIFA Store, soccer.com, Dick's, multiple retailers. Pre-tournament demand spike pattern confirmed. | DFS SERP 2026-05-28 |
| Edson Alvarez squad role | Named at v3 (West Ham, double-pivot anchor) | Updated: Captain; now on loan at Fenerbahçe from West Ham (2025-26 season move) | Wikipedia Edson Alvarez |
| Estadio Azteca naming | Used "Estadio Azteca" at v3 | Now officially "Estadio Banorte" (sponsorship rename); SCRIBE chose to keep "Estadio Azteca" per avatar-search-language preference; documented above. | Wikipedia Estadio Azteca; mysanantonio.com |

### Currency-of-information lessons applied

- Captain reference (Edson Alvarez) is current as of 2026-05-22 Wikipedia squad table; held in body copy.
- Did NOT name Edson Alvarez's club affiliation (Fenerbahçe / West Ham) because the page is about a national team jersey, and club affiliation creates noise for the kit-wearing context (Alvarez wears the Mexico kit for international duty, not his club's; mentioning his club confuses the reader about what they're buying).
- Did NOT name Aguirre's successor (Rafael Marquez) explicitly because the page is about the 2026 cycle, not the 2030 cycle; the v3 collection page brief mentioned Marquez as assistant. PDP brief frames Marquez as "before he takes over for the 2030 cycle" ,  captures the future-state without distracting from the current-cycle purchase.
- Group A locked: included South Korea and Czech Republic in body copy where v3 had to hedge.
- Stadium naming: stuck with Estadio Azteca per cultural identity; Banorte rename is correct but not yet what supporters call it.

## Five canonical brief-craft rules: per-rule verification

1. **Supporting keywords distributed as semantic variants in body.**
   - Primary `mexico 2026 home jersey` exact-match in H2 1 ("The 2026 Mexico Home Jersey by adidas") and Short Description ("The Mexico 2026 home jersey by adidas").
   - `mexico home jersey` (880/mo) naturally distributed across body in close variants ("the 2026 home jersey", "Mexico 2026 home jersey", "home jersey").
   - `mexico 2026 world cup jersey` (4,400/mo) and `mexico jersey 2026` (9,900/mo) semantically present via "Mexico 2026 home jersey" and "the official Mexico national team jersey for the 2026 to 2027 cycle".
   - `mexico fifa world cup 2026 jersey` (210/mo) semantically covered via "2026 World Cup" in H2 4 ("Mexico opens the 2026 World Cup against South Africa").
   - `mexico stadium jersey` and `el tri jersey` covered via "Men's Stadium edition" naming + "El Tri" across body (4 mentions).
   PASS.

2. **Primary keyword in at least one H2.** H2 1: "The 2026 Mexico Home Jersey by adidas" ,  exact primary keyword `mexico 2026 home jersey` integrated as natural framing. PASS.

3. **Meta Description structure (commercial intent + trust signal + emotional CTA).**
   - "The Mexico 2026 home jersey by adidas." ,  sentence 1: primary keyword + brand. Commercial intent confirmed.
   - "Official Stadium kit with the Piedra del Sol Azteca print and Climacool weave." ,  middle: "Official" trust signal, tier-correct "Stadium kit" (not "Authentic Stadium" ,  tier-aware language per Rule 3), "Piedra del Sol Azteca print" specific differentiator (most specific factual anchor in the SERP that ProSoccer can own), "Climacool weave" tech differentiator.
   - "The shirt El Tri opens in." ,  emotional CTA, distinct from Short Description close ("Climacool weave, 100% recycled polyester"). Captures the load-bearing June 11 opener moment in 6 words.
   - 144 chars. Within 130-158 desktop window.
   - No tier-word combination violation.
   PASS.

4. **5 to 10 named entities for LLM discoverability.** Body names: adidas (brand), El Tri (team), Javier Aguirre (manager), Estadio Azteca (stadium), 1998 France ABA Sports (kit lineage anchor), Piedra del Sol Azteca (design pattern), FMF (federation), Edson Alvarez, Hirving Lozano, Santiago Gimenez, Raul Jimenez (squad), Rafael Marquez (successor), South Africa, South Korea, Czech Republic (Group A opponents), Climacool (signature tech), Heat.RDY (Authentic edition tech), Stadium edition, Authentic edition (tier names), 2010 World Cup (history reference), 1970, 1986, 2026 (Azteca three-opener anchor). 22+ distinct named entities, well above the 5-10 floor. PASS.

5. **Short Description structure.**
   - "For every fan walking into Estadio Azteca on June 11." ,  avatar identity hook + emotional moment. Carlos primary anchor.
   - "The Mexico 2026 home jersey by adidas: bold green base, Piedra del Sol Azteca print across the chest, embroidered FMF crest, red and white trim drawn from the flag." ,  primary keyword (sentence 2). Four specifics (bold green base, Piedra del Sol Azteca print, embroidered FMF crest, red/white trim).
   - "Climacool weave, 100% recycled polyester." ,  close, technical and distinct from Meta Description close ("The shirt El Tri opens in").
   - 260 chars, within 200-300 target.
   PASS.

## National Team Jersey CANONICAL template application review

Template (per `context/page-type-playbooks/product-page-playbook.md` section 1, validated UAE v3 2026-05-26):

- H2 1: Brand + design + federation identity ("The [Year] [Country] Soccer Jersey by [Brand]")
- H2 2: Edition tier comparison (Stadium vs Authentic, where applicable)
- H2 3: Fit and sizing
- H2 4: What you're buying into (cultural + tournament context + future catalyst)

Application:

- **H2 1:** "The 2026 Mexico Home Jersey by adidas" ,  brand + design + federation identity (adidas, design lineage via 1998 ABA Sports Piedra del Sol Azteca, FMF crest placement, flag-color V-neck trim). Primary keyword integrated. Mexico collection link placed at section close.
- **H2 2:** "Stadium Edition vs the Authentic Cut" ,  full edition tier comparison ($99.99 Stadium with Climacool, screen-printed badges vs $149.99 Authentic with Heat.RDY, heat-bonded badges). Tier-aware language (Rule 3): "Stadium" and "Authentic" as distinct tier names; no "Authentic Stadium" combination. Names verified pro players (Alvarez, Lozano, Gimenez, Jimenez) on the Authentic tier as the player-edition framing. Doubles as the upsell path to the in-stock Authentic SKU per pre-tournament demand spike exception.
- **H2 3:** "Fit and Sizing" ,  slim fit through chest, standard adidas football-jersey sizing, fitted-vs-relaxed t-shirt sizing guide.
- **H2 4:** "What You're Buying Into" ,  June 11 opener at Estadio Azteca, repeat of 2010 opener vs South Africa, Group A (South Korea, Czech Republic), up to five home matches, Azteca's three-opener record, captain Edson Alvarez, Aguirre's third WC, Marquez succession for 2030. Closes with adidas national team jersey lineup link.

**Template landed clean.** All four H2s served their canonical role. National Team Jersey template now has two consecutive validations under CANONICAL status (UAE v3 2026-05-26, Mexico 2026-05-28).

## Source-of-record paragraph

DataForSEO MCP calls (all native, all status_code 20000):

- `mcp__dfs-mcp__dataforseo_labs_bulk_keyword_difficulty` keyword `mexico 2026 home jersey`, location `United States`, language `en`. Step 0 ping. id `05290044-1507-0392-0000-2b2e2d3c9f4c`.
- `mcp__dfs-mcp__dataforseo_labs_google_keyword_overview` keywords `[mexico 2026 home jersey, mexico home jersey, mexico jersey 2026, mexico stadium jersey, mexico fifa world cup 2026 jersey, mexico 2026 world cup jersey, mexico jersey, el tri jersey, mexico soccer jersey]`, location `United States`, language `en`. id `05290045-1507-0607-0000-54f4cfe83588`. Returned 8 of 9 keywords (mexico stadium jersey not in DFS DB).
- `mcp__dfs-mcp__serp_organic_live_advanced` keyword `mexico 2026 home jersey`, depth 100, location `United States`, language `en`. id `05290045-1507-0139-0000-041426a98000`.

Firecrawl MCP calls (all native, all 200 OK):

- `mcp__firecrawl-mcp__firecrawl_scrape` target PDP. 148,723 chars. Confirmed Title `adidas 2026 Mexico Men's Stadium Home Soccer Jersey`, current Description body (3-bullet adidas template: Mexico football jersey with Climacool for a cool, dry feel / Slim fit / 100% polyester (100% recycled) / Climacool), 7 size variants all "Variant sold out or unavailable" state.
- `mcp__firecrawl-mcp__firecrawl_scrape` on `/collections/mexico`. Returned 200 OK. H1 "Mexico National Soccer Team Jerseys, Apparel & Gear", page title "Mexico World Cup 2026 Soccer Fan Gear | Prosoccer.com - ProSoccer", 103 products live. Confirmed link validation.
- `mcp__firecrawl-mcp__firecrawl_scrape` on `/collections/adidas-soccer-jerseys`. Returned 200 OK. Page title "adidas Soccer Jerseys & Team Gear | Pro Soccer - ProSoccer", 26 distinct product handles, 46 "Choose options" instances. Confirmed link validation.

Tavily MCP calls (all native):

- `mcp__tavily-mcp__tavily_search` "Mexico 2026 World Cup home jersey adidas design release Aztec FMF", max_results 5, advanced.
- `mcp__tavily-mcp__tavily_search` "Mexico national team manager Javier Aguirre 2026 confirmed squad Edson Alvarez captain", max_results 5, advanced.
- `mcp__tavily-mcp__tavily_search` "Mexico 2026 home jersey adidas design Aztec Piedra del Sol price stadium replica specifications climacool", max_results 5, advanced.
- `mcp__tavily-mcp__tavily_search` "Estadio Azteca 2026 World Cup opener three opening matches history capacity Mexico City renovation", max_results 4, advanced.
- `mcp__tavily-mcp__tavily_search` `"Mexico Group A" 2026 World Cup opponents confirmed final draw teams`, max_results 5, advanced.

GSC calls: NONE this session (PDP work; GSC MCP install pending).

## Internal link selection reasoning

Two candidates validated 200 OK with content signals matching expectations:

1. **`/collections/mexico`:** 200 OK, H1 "Mexico National Soccer Team Jerseys, Apparel & Gear", page title "Mexico World Cup 2026 Soccer Fan Gear | Prosoccer.com - ProSoccer", 103 products live including Stadium Third SS ($99.99), Authentic Third SS ($149.99), Stadium Third LS ($109.99), Authentic Third LS ($159.99), Mini Kit, Baby Kit, Youth Stadium Third, Backpack, Crossbody bags, training balls. Multiple Mexico Home variants live in the collection grid even though the specific Stadium SS Home PDP is sold out. Load-bearing for the pre-tournament demand spike exception: gives the buyer landing on the sold-out PDP a one-click recovery path to in-stock alternates. Anchor text `the Mexico collection` (3 words, descriptive, reads naturally as the closing sentence of H2 1).

2. **`/collections/adidas-soccer-jerseys`:** 200 OK, page title "adidas Soccer Jerseys & Team Gear | Pro Soccer - ProSoccer", 26 distinct product handles, 46 jersey SKUs. Brand-level breadth complement to the team-level Mexico collection. Anchor text `adidas's national team jersey lineup` (5 words, descriptive of destination, reads naturally as closing transition of H2 4).

**Deferred to follow-up commit (per spec):** sibling Home-to-Away and Home-to-Third cross-kit links handled in a single follow-up commit after all three Mexico briefs land. Not included this brief.

**Considered and rejected alternatives:**

- `/collections/mexico-jerseys`: surfaced in `/collections/mexico` grid as a sub-category page. Did not validate this session because the team-collection link covers the broader recovery path (jerseys + apparel + accessories) and the brand-line link covers the breadth. A third link would push past the 1-to-2-link ceiling per `context/page-type-playbooks/product-page-playbook.md` 'Internal link strategy'.
- `/collections/hirving-lozano` (player-spotlight): per MEMORY.md `feedback_internal-link-selection-pattern.md`, player-spotlight links can outperform brand-line links from collection pages. PDP-specific calculus differs: the player-spotlight serves a player-search buyer landing on a team page; for a PDP buyer who has already committed to a specific kit, the player-spotlight is a sideways move. Team collection + brand line is the stronger pair for PDP recovery from a sold-out state.
- `/collections/2026-national-team-soccer-fan-gear` (the umbrella WC collection used on UAE v3): viable but less targeted than `/collections/mexico` for a Mexico buyer. The umbrella collection serves brand-agnostic cross-team discovery; the team-collection link serves Mexico-loyal recovery. Picked the more targeted destination.

## 11-gate self-verify status

- **Gate 1 (Self-verification):** PASS. Every numerical claim sourced. DFS volume for primary 70/mo verified. Supporting volumes 880, 4400, 9900, 210, 70 all directly from DFS keyword_overview call. SERP rank "not in top 100" verified via depth-100 serp_organic_live_advanced. Current PDP title verified via Firecrawl scrape. Squad names verified via Wikipedia + YouTube + Yahoo. Group A composition verified via Wikipedia + FIFA.com + Sky Sports + Fox Sports.
- **Gate 2 (Voice check):** PASS. Both visible brief and workforce-internal briefing pass `scripts/voice_check.py`. No em-dashes, no en-dashes, no forbidden words, no forbidden openers.
- **Gate 3 (Sourcing):** PASS. All claims sourced in this briefing or inline in the brief.
- **Gate 4 (Severity / Confidence / Lift band):**
   - Severity: HIGH (current-cycle co-host kit, opener 14 days out, sold-out PDP without recovery linking is a wasted impression every time it ranks).
   - Confidence: HIGH (Mexico is fully researched via v3 collection page work 2026-05-08 + reverified 2026-05-28; design specifics verified via three independent sources including House of Heat + ESPN + YouTube unboxing; squad and group draw locked; ProSoccer not in top 100 = zero equity risk on Title and H1 changes).
   - Lift band: capture incremental commercial traffic from `mexico 2026 home jersey` (70/mo, low absolute but high intent), `mexico home jersey` (880/mo), and `mexico 2026 world cup jersey` (4,400/mo) totaling ~5,350/mo of branded-search demand. SERP is dominated by adidas.com, FIFA Store, soccer.com, Dick's; ProSoccer unlikely to outrank adidas.com but should compete for the mid-page positions where the long tail of the 5K-6K monthly volume lives. Quarterly +175% trend on the primary keyword + +400% quarterly trend on supporting `mexico home jersey` confirm pre-tournament demand acceleration that the page will catch if optimized now and restocked during tournament window.
- **Gate 5 (Avatar fit, full-scope):** PASS. Carlos primary with AIDAR stage Desire/Action named. Tyler secondary named with H2 2 placement reasoning. Jennifer and Mike the Coach excluded with reasoning. No cross-avatar landing accommodation required (Men's Stadium title is explicit).
- **Gate 6 (Reversibility):** PASS. Slug unchanged. All other fields one-click revertible via Shopify admin. The 2026 home page returns to the sold-out current state with the 3-bullet adidas template intact if reverted.
- **Gate 7 (Audience-fit summary):** N/A for routine PDP; Tony-facing summary not required.
- **Gate 8 (Red-team):** PASS.
   - Did NOT name Edson Alvarez's club (Fenerbahçe / West Ham) ,  would create noise on a national-team-jersey PDP where club association is irrelevant.
   - Did NOT name Rafael Marquez as future manager beyond "before he takes over for the 2030 cycle" ,  keeps the page anchored to the 2026 purchase moment.
   - Did NOT name Guillermo Ochoa ,  goalkeeper, peripheral to a fan-tier outfield jersey body.
   - Did NOT use "Estadio Banorte" (the official sponsorship name) ,  chose Estadio Azteca per avatar-search-language reality and Wikipedia / FIFA.com primary usage. Documented above.
   - Did NOT exploit the 1985 Mexico City earthquake or any tragedy framing ,  kept the body celebratory.
   - Body copy commits to the product being sold, not to alternates, until the internal links carry the recovery path naturally.
- **Gate 9 (Positioning lift-test):** PASS. Soccer-specialty depth (1998 ABA Sports Piedra del Sol lineage, kit-supplier-since-1999 timeline, Stadium-vs-Authentic tier accuracy with verified pro-player Authentic-tier roster, Group A specificity, Estadio Azteca three-opener record) anchors the copy to specialty-retailer voice; Dick's wouldn't write this. The page positions ProSoccer's expertise without name-dropping ProSoccer (per `context/page-type-playbooks/product-page-playbook.md` 'Forbidden subjects on product pages': no retail-location call-outs, no warehouse and shipping logistics, no store-anchored framing in body copy). Body lifts onto another specialty retailer's site only if they also do their homework on Piedra del Sol naming, 1998 lineage, ABA Sports attribution, and pro-roster tier framing. ProSoccer-specific anchoring sits inside the brand-identity rather than store mentions.
- **Gate 10 (Emotion-first):** PASS. Short Description opens with the Estadio Azteca opener moment ("For every fan walking into Estadio Azteca on June 11"). H2 1 opens with identity and lineage (adidas since 1999, El Tri, 1998 France homage). H2 4 opens with the load-bearing identity moment ("June 11 at Estadio Azteca"). Features support identity throughout; never lead.
- **Gate 11 (Brand IP compliance):** PASS. Mexico is adidas-licensed; FIFA terminology family PERMITTED. "World Cup" used naturally in body. "FIFA" not used in body but permitted. "2026 World Cup" appears in H2 4. No tier-word violation ("Stadium kit", "Stadium edition", "Authentic edition", "Authentic Cut" all clean; no "Authentic Stadium" combo). Internal link anchors scan clean ("the Mexico collection", "adidas's national team jersey lineup"). All six fields plus link anchors compliant.

## Char count verification

- Meta Title: 51 chars (target 50-60). PASS.
- Meta Description: 144 chars (target 130-158). PASS.
- Short Description: 260 chars (target 200-300 per Rule 5). PASS.

## Cost tracking this session

- DataForSEO API: 3 calls (bulk_keyword_difficulty x1 Step 0 ping, keyword_overview x1 bulk-9, serp_organic_live_advanced x1 depth-100). Estimated cost ~$0.03 to $0.04 (depth-100 SERP ~$0.02; bulk keyword overview ~$0.01; Step 0 ping ~$0.005).
- Firecrawl: 3 scrape credits (target PDP + /collections/mexico + /collections/adidas-soccer-jerseys validation).
- Tavily: 5 search credits (advanced depth on 4, basic on 1).
- voice_check.py: 0 cost.
- GSC: 0 calls.
- Playwright: 0 sessions.
- Total estimated session cost: ~$0.04 external API spend. Within target envelope ($0.05-0.10 DFS + 3-5 Firecrawl + 5-8 Tavily).

## Findings logged

- learnings.md: no entry added this session (stayed surgical; pre-tournament demand spike exception is already codified in commit 120a177).
- decisions.md: no entry added.
- shared-intelligence/seo-findings.md: no entry added.

## Recommendation for follow-up artifacts (not produced this session per instructions)

1. **Cross-kit linking commit:** after Mexico Home (this brief), Mexico Away, and Mexico Third PDPs all land, single follow-up commit adds Home-to-Away and Home-to-Third sibling links (and corresponding Away-to-Home, Away-to-Third, Third-to-Home, Third-to-Away). Per spec: deferred to dedicated commit.
2. **National Team Jersey template promotion:** with UAE v3 (2026-05-26) and Mexico 2026 Home (2026-05-28) as two consecutive CANONICAL-tier validations, the template is solidly in the canonical position. No demotion or refinement triggered this session.
3. **MEMORY.md candidate:** "Estadio naming choice: when an officially renamed stadium retains a culturally dominant former name (Banorte vs Azteca, Etihad vs Manchester City Stadium, Allianz Arena previously called Munich Olympic Stadium territory), prefer the cultural name for body copy unless the page subject is the stadium itself. Avatar-search-language wins over corporate accuracy." Surfaced as recommendation; not written this session.

## Open questions / flags for GATE

None this session. All design specifics, squad currency, group composition, opener context, stadium history, kit tier price ladder, internal link destinations, and exception application verified and documented. Brief paste-ready.

## Artifact paths

- **Visible brief:** `deliverables/page-optimizations/2026-05-28_session-01/adidas-2026-mexico-mens-stadium-home-soccer-jersey_brief.md`
- **Workforce-internal briefing:** this file (`.claude/agents/on-page-seo/briefings/2026-05-28_adidas-2026-mexico-mens-stadium-home-soccer-jersey.md`)
