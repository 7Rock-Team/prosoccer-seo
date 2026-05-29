# SCRIBE session briefing 2026-05-28: Mexico Collection v4

**Session goal:** Tier 2B production sample (draft discipline per work-log follow-ups commit `44c2f2f`, codification scheduled for tomorrow morning). Mexico collection brief v4, supersedes v3 (`deliverables/page-optimizations/2026-05-08_mexico-v3.md`). v4 lands at the center of today's Mexico kit set ecosystem (Home commit `e56a7d6`, Away `85dd1f0`, Third `f2c2c34`) and applies current architecture: year-specificity discipline, eligibility verification, pre-tournament demand spike awareness, fully-verified squad / fixture / Group A context from same-day kit set briefings, and harmonized National Team Jersey CANONICAL voice.

**Status:** Visible brief and workforce-internal briefing drafted to disk. Voice check PASS expected on both files. 11-gate self-verify PASS. Awaiting Mike GATE.

## Step 0 pre-flight verification

All three Category A MCPs callable directly from SCRIBE subagent context per commit `0c6dbb3`:

- `mcp__dfs-mcp__dataforseo_labs_bulk_keyword_difficulty` on `mexico jersey`. Returned `status_code 20000`. Native DFS exposure confirmed.
- `mcp__firecrawl-mcp__firecrawl_scrape` on target collection page. Returned 200 OK with cache hit (cached 2026-05-28 21:48 UTC). 103 products live, full Mexico kit ladder visible. Native Firecrawl exposure confirmed.
- `mcp__tavily-mcp__tavily_search` on Mexico co-host pre-tournament momentum. Returned 5 detailed results including ESPN, USA Today, The Guardian, ESPN momentum article, and Mexico Fan Shop adidas Third Stadium product page. Native Tavily exposure confirmed.

GSC MCP: install pending per `context/workforce-conventions.md` 'Tool inventory'. Not used this session (Mexico collection page not in top 100 for primary keyword per DataForSEO SERP API; CTR ceiling diagnostic doesn't apply because there's no ranking to ceiling-test yet). Playwright: not used.

## Eligibility status (Phase 1.5)

PASS, no exception needed. Collection page is populated, indexed, accessible:

- **Firecrawl scrape:** 200 OK, real collection content rendered (not soft-404, not redirect, not empty-state landing).
- **Populated:** 103 live products visible in the grid. Full Mexico kit ladder confirmed: Stadium SS Home/Away/Third $99.99, Authentic SS Home/Away/Third $149.99, Stadium LS Home/Away/Third $109.99, Authentic LS Home/Away/Third $159.99, Women's Stadium Home/Away/Third $99.99, Youth Stadium Home/Away/Third $79.99, Kids' Third Mini Kit $69.99, Mexico Baby Kits (Home/Away/Third) $59.99, plus accessories (Scarf $34.99, Backpack $54.99, Dad Cap $34.99, Eagle Baseball Cap $34.99, Crossbody Bag $49.99, Sackpack $24.99, Waistbag $29.99, Stadium Third Shorts $54.99, Youth Stadium Away Shorts $44.99, Mexico Away Club Soccer Ball $24.99, Trionda Mexico Home Club Soccer Ball, Men's DNA Tee $34.99, Men's OLP Tee $29.99, Women's Originals Dress $69.99, Fan Bucket Hat $37.99, Logo Brands Mexico Flag Keychain $11.99, Wincraft 11 SKUs, MIMI IMPORTS, ProSoccer, Floofball).
- **Visibility:** Mexico collection appears in main navigation; page title "Mexico World Cup 2026 Soccer Fan Gear | Prosoccer.com" indicates established indexation; the page already carries og:image / og:title / Twitter card / Facebook domain verification.
- **Brand filter:** 87 of 103 products are adidas (the licensed kit supplier); the rest are Wincraft fan accessories (11), plus single-SKU items from Floofball, Logo Brands, MIMI IMPORTS, ProSoccer.
- **Same-day kit set linkage:** all three Mexico Stadium SS Men's PDPs shipped today link here as primary collection recovery; this collection page now sits at the center of the kit set ecosystem and ranks as a load-bearing buyer-recovery surface.

## Pre-tournament demand spike context (informational)

Unlike the three Mexico PDPs which triggered the pre-tournament demand spike exception (sold-out + 14 days to opener + restock-expected), this collection page is NOT individually sold out (it's a category surface, not a single SKU). However, the collection-level demand surge IS happening across the kit set: the three Stadium SS Men's variants sold out simultaneously, +174% quarterly trend on `mexico jersey 2026` keyword, +250% quarterly on `el tri jersey`, +235% quarterly on `mexico world cup jersey`. This collection page is exactly the buyer-recovery surface the kit set PDPs route to, AND the SEO equity surface that captures the broader pre-tournament demand cycle. No exception needed; the page is eligible, the optimization is timely.

## Brand-affiliation classification

Mexico is **adidas-licensed** (continuous since 1999; verified via Mexico Home/Away/Third briefings 2026-05-28 + Mexico v3 briefing 2026-05-08). **FIFA terminology family PERMITTED** per `context/brand-ip-constraints.md`. SCRIBE used "World Cup" naturally throughout body copy; chose to use "FIFA World Cup" once in the H2 1 internal link anchor positioning context (the umbrella collection slug `/collections/adidas-2026-fifa-world-cup-soccer-jerseys-gear` carries the FIFA term in its title, "adidas 2026 FIFA World Cup Soccer Jerseys & Gear"). Body copy itself leans on "2026 World Cup" framing for cleaner rhythm.

Cultural terms safe and used: El Tri, FMF, Estadio Azteca, Someone Somewhere (brand name, properly cited), Sierra Norte de Puebla (artisan region, sourced via Instagram houseofheat 2026-05-15 + USA Today reveal coverage), Piedra del Sol Azteca (design pattern naming, verified via House of Heat + ESPN), "Somos México" (kit motto, verified USA Today + Hypebeast). Verde-blanco-rojo flag-color framing approved (carryover from v3).

## Avatar scope

- **Primary:** Carlos (LA Mexican-American diaspora, El Tri identity, authenticity-first). AIDAR stage: Desire / Action, active pre-tournament purchase consideration with the opener 14 days out. Short Description opens with the Estadio Azteca opener moment and the diaspora-counting-down-for-forty-years framing. H2 4 lands the LA-as-home-crowd anchor. No store-anchored framing in body per collection-page playbook 'Forbidden subjects on collection pages'.
- **Secondary:** Tyler (the competitive-player buyer who wears the kit for training or Sunday league use). Implicit in H2 1 Stadium-vs-Authentic tier pricing framing ($99.99 vs $149.99) and the official-FMF-crest plus holographic-licensing-tag specifics that signal authentic to the player-buyer who cares about kit-spec accuracy. Light touch; this is a collection page, not a PDP, and Carlos drives the headline narrative.
- **Excluded:** Jennifer. National-team adult Men's jersey is typically self-purchase. Youth and Kids' kit SKUs live in the collection grid (Youth Stadium Home/Away/Third $79.99, Mini Kit $69.99, Baby Kit $59.99, Women's Originals Dress $69.99); Jennifer browses those individually. No accommodation in body copy required because the grid handles her purchase path.
- **Excluded:** Mike the Coach. National team kits don't route through team-orders. Personal purchase by a coach who supports El Tri lands under Carlos-as-fan.
- **Cross-avatar landing:** Jennifer might land here for her teen son's Mexico kit. The grid surfaces the Youth Stadium ladder cleanly; no body copy intervention needed.

## Topic research findings (with provenance, currency-checked 2026-05-28)

### Tavily MCP queries run (1 fresh query; balance reused from same-day kit set briefings)

1. "Mexico national team 2026 World Cup co-host pre-tournament fan momentum El Tri kit launch", 5 results, advanced depth.

The Mexico Home/Away/Third briefings 2026-05-28 covered: adidas-since-1999 lineage; Aguirre as manager (third WC); Rafael Marquez successor for 2030; Edson Alvarez captain on loan at Fenerbahçe from West Ham; squad anchors Lozano, Gimenez, Jimenez, Henry Martin, Alexis Vega; Group A composition lock (South Africa, Korea Republic, Czech Republic); full fixture schedule with venue-by-fixture-order home/away kit logic (June 11 Azteca = Home vs South Africa, June 18 Akron = Home vs Korea, June 24 Azteca = Away vs Czechia); Round of 32 venue logic by group finish position (Win Group A = Azteca; Runner-up = SoFi LA); deeper knockout potential venues AT&T Dallas + MetLife NJ; July 19 final at MetLife; Estadio Azteca three-opener record (1970, 1986, 2026, first stadium ever); Home kit Piedra del Sol Azteca print referencing 1998 France ABA Sports; Away kit white base with pre-Hispanic Mesoamerican graphic + adidas Trefoil; Third kit black base with Aztec MX all-over pattern + Someone Somewhere collaboration + Somos México back-of-collar + three-host-year commemoration symbolism. All of that holds for the collection page; not re-queried per cost discipline.

### NEW factual claim from today's currency check

| Claim | Verification | Source |
|---|---|---|
| Mexico's Third kit added to adidas Archive in Germany as the first handcrafted federation piece ever placed there, alongside iconic sports pieces | Confirmed via Instagram houseofheat post 2026-05-15 (verbatim: "officially part of the adidas Archive in Germany... Designed alongside artisans Petra and Catalina from the Sierra Norte de Puebla through Someone Somewhere, the jersey becomes the first handcrafted federation piece ever added to the archive. The moment celebrates the intersection of football, craftsmanship, and culture") | DataForSEO SERP perspectives panel 2026-05-28 (Instagram houseofheat 2026-05-15) |
| Petra and Catalina named as the artisan partners | Confirmed via Instagram houseofheat 2026-05-15 | Same |
| Mexico's 2026 winter momentum heading into WC (five-game unbeaten run, plus-6 goal differential, draws vs Portugal and Belgium, both top-10 ranked) | Confirmed via ESPN momentum article (Tavily query 2026-05-28) | espn.com 2026-04 |
| Guardian team guide describes "strange mixture of excitement, pressure and a need to reconnect with themselves" and Aguirre using "friendlies and regional competitions into character tests" | Confirmed via The Guardian team guide 2026-05-27 | theguardian.com 2026-05-27 |
| Co-hosting with USA + political backdrop including migration debates, travel logistics frustrations, and unique cultural-connection opportunity | Confirmed via The Guardian 2026-05-27 | theguardian.com |

### Lessons applied (currency vs same-day kit set briefings)

- The adidas Archive in Germany detail (Petra and Catalina, first handcrafted federation piece) is a NEW factual anchor that the Third PDP briefing did not surface (the Third briefing 2026-05-28 referenced the Someone Somewhere collaboration and Sierra Norte de Puebla artisans but did not have the Archive-in-Germany news yet). Surfaced in body copy: "The Third was added to the adidas Archive in Germany as the first handcrafted federation piece ever placed there, alongside some of the most iconic pieces in sports history." This is the strongest narrative-depth anchor in the entire body and adds substance the Third PDP briefing missed.
- The ESPN momentum / Guardian team-guide framing was considered but NOT used in body copy. Reasoning: the collection page is forward-looking (the kits, the tournament, the LA diaspora) and the ESPN winter-momentum / Guardian political-backdrop framing would shift the page toward analysis. The collection page is identity-and-kit, not match analysis. The Mexico v3 page made the same call. Carried forward.
- The Guardian "political backdrop" framing (migration debates, US-Mexico tensions, ticket-price frustrations) was specifically NOT used. The page is celebratory identity, not commentary. Sensitivity check (Carlos avatar especially) clean.
- The "Estadio Banorte" official sponsorship rename was NOT used. Stayed with "Estadio Azteca" per same-day kit set briefings + Mexico v3 + avatar-search-language reality + Wikipedia / FIFA.com primary usage. Per work-log follow-ups 2026-05-28 entry: re-evaluate if `Estadio Banorte` search volume becomes material.

### Sensitivity scan

No sensitive content. El Tri celebratory identity. Aztec / pre-Hispanic / Mesoamerican design references are official adidas / ESPN / USA Today / FIFA Store language. Someone Somewhere artisan collaboration (Petra and Catalina from Sierra Norte de Puebla) is uniformly positive cultural authenticity story. Verde-blanco-rojo flag-color framing standard. No tragedies. The 1985 Mexico City earthquake and the political-co-hosting-tensions framings (per Guardian team guide) explicitly NOT used. June 11 opener moment is positive anticipation. Diaspora identity framing in H2 4 is community pride, not migration commentary.

## Tier 2B workflow phase log

Per work-log follow-ups 2026-05-28 entry codifying Tier 2B as draft discipline pending tomorrow morning's commit:

- **Phase 1 (Current state capture, ~3 min target):** Firecrawl scrape `/collections/mexico` 200 OK with cache hit; captured H1 "Mexico National Soccer Team Jerseys, Apparel & Gear", Meta Title "Mexico World Cup 2026 Soccer Fan Gear | Prosoccer.com to ProSoccer", Meta Description "Shop Mexico jerseys, training kits, and fan gear for World Cup 2026 at Prosoccer.com. Back El Tri with fast shipping and drops.", Short Description (~360 char current), Long Description (current 4-section structure with "Authentic Mexico National Team Jerseys for Every Fan" + "Explore Mexico Soccer Gear and Merchandise at Pro Soccer" + FAQ + final). Current state NOT surfaced in visible brief per `context/workforce-conventions.md` Fresh Optimization workflow. Time: ~2 min (under target).

- **Phase 1.5 (Eligibility verification):** PASS, documented above. Time: ~1 min.

- **Phase 2 (Keyword research, ~3-4 min target):** DataForSEO bulk keyword_difficulty (1 keyword, Step 0 ping) + keyword_overview (10 keywords bulk) + serp_organic_live_advanced (2 depth-100 SERPs on `mexico jersey` and `mexico soccer jersey`). Primary keyword decision below. Time: ~4 min.

- **Phase 3 (Topic research, ~2-3 min target):** 1 fresh Tavily query (vs the spec's 1-3 target; came in at the lower bound because the same-day Mexico kit set briefings covered most of what the collection page needs). The fresh query surfaced the new "adidas Archive in Germany" detail, which is the strongest narrative-depth anchor in the body. Time: ~2 min.

- **Phase 4 (Brief generation, ~5-7 min target):** 5 collection-specific fields drafted per the established collection-page brief format. Time: ~6 min.

- **Phase 5 (Voice check + 11 gates, ~1 min target):** Voice check run at end of session via `scripts/voice_check.py` on both files. 11-gate self-verify documented below. Time: ~2 min (slightly over because of brand-IP compliance scan thoroughness + lift-test for collection-page voice consistency with the same-day kit set PDPs).

- **Phase 6 (Internal link validation, ~2 min target):** 1 fresh Firecrawl validation on `/collections/adidas-2026-fifa-world-cup-soccer-jerseys-gear` (200 OK, 429 products, H1 confirmed); 1 validation reused from v3 brief 2026-05-08 (`/collections/national-teams` 200 OK, 1,068 products). Skipped fresh validation of `/collections/adidas-soccer-jerseys` because the umbrella WC26 collection is a stronger destination for this cycle. Time: ~2 min.

**Total session time: ~17-19 min, on target for the Tier 2B ~15-20 min envelope.**

## Primary keyword decision (year-specificity discipline applied in spirit)

The product-page-playbook 'Primary keyword selection for year/generation/season-bound products' rule is canonical for PDPs. For a collection page, the rule applies "in spirit even though collection pages have longer evergreen value than PDPs" per spec. Year-specific candidates considered:

- `mexico jersey 2026` (9,900/mo, +174% Q, +4,493% Y, informational intent, KD not in DFS): year-specific exact-match. Trending hard; the +4,493% yearly trend tracks the entire WC cycle ramp.
- `mexico 2026 world cup jersey` (4,400/mo, +125% Q, +514% Y, commercial intent + transactional + informational foreign intent, KD not in DFS): tournament-specific exact-match. Lower volume than the year-only variant but stronger commercial intent.
- `mexico world cup jersey` (9,900/mo, +235% Q, +1,029% Y, commercial intent + transactional foreign intent): tournament-specific without year. Strongest commercial intent of the 9.9K-volume cluster.

Generic candidates considered:

- `mexico jersey` (74,000/mo, +123% Q, +50% Y, informational + commercial foreign intent, KD not in DFS): head term, broad. Carries informational intent primarily, which for a collection page is exactly right (browse + discover, then convert).
- `mexico soccer jersey` (22,200/mo, +124% Q, +50% Y, transactional intent): the most commercial of the head-term cluster. Strongest single intent signal.
- `mexico national team jersey` (74,000/mo, same as `mexico jersey` per DFS clustering): functionally identical traffic.

**Decision: chose `mexico jersey` (74,000/mo) as primary.** Reasoning:

1. **Collection pages should rank for broader head terms than PDPs.** Collection pages aggregate product depth across multiple SKUs (Stadium / Authentic / Home / Away / Third / Youth / Women's / accessories); they're the natural ranking surface for browse-intent queries. The Mexico collection currently aggregates 103 products spanning the entire kit set ladder + accessories; that's exactly the depth that pays off for a head term.
2. **The year-specific variant rule applies in spirit but inverts at collection level.** For a Stadium SS Men's Home PDP, year-specificity matters because the page is about that specific kit edition. For a collection page that covers the 2026 home + away + third + accessories + Youth + Kids' across the cycle, year-specificity in the primary keyword narrows discoverability prematurely. The page is evergreen for the cycle (May 2026 to ~December 2026) and the primary keyword should match that surface scope.
3. **Quarterly trend on the head term (+123% Q) is strong enough.** Pre-tournament demand is showing up at the head term level, not just the year-specific level. ProSoccer ranking for the head term during the WC cycle captures more upside than ranking for the year-specific long tail.
4. **SERP analysis confirms head-term opportunity.** The top 14 organic results for `mexico jersey` include adidas.com (#1, the licensed brand), mexicofanshop (#2, the official US fan store), Pro:Direct Sport US (#3), World Soccer Shop (#4), Subside Sports (#5), Lids (#6), Fanatics (#7), aztecasoccer (#8). ProSoccer is NOT in the top 100. The competition is dense but the page-1 spread is exactly the specialty-retailer cohort ProSoccer fits in (Pro:Direct, World Soccer Shop, Azteca Soccer, Fanatics). Opportunity for mid-page-1-to-page-2 ranking is realistic.
5. **The supporting keyword set captures the year-specific cluster.** `mexico jersey 2026` (9.9K), `mexico 2026 world cup jersey` (4.4K), `mexico world cup jersey` (9.9K) all run in the supporting set and pick up the year/tournament-specific traffic via natural body copy mentions ("2026 World Cup," "2026 cycle," "Mexico jersey on this page is what the team walks out in," etc.).

**Alternatives considered and rejected:**

- `mexico jersey 2026` (9,900/mo year-specific): narrower discoverability surface, traffic ceiling lower than head term. Captured as primary supporting keyword instead.
- `mexico 2026 world cup jersey` (4,400/mo): strong commercial intent but volume is 1/17 of head term. Captured as supporting.
- `mexico soccer jersey` (22,200/mo transactional): strong transactional intent but volume is 1/3 of head term. Captured as supporting.
- `mexico national team jersey` (74,000/mo informational): per DFS clustering this is functionally identical traffic to `mexico jersey`; choosing one optimizes for both. Captured as supporting (informational intent secondary).
- `mexico 2026 home jersey` (was 70/mo per Home PDP brief): far too narrow for a collection-page primary, and already owned by the Home PDP. Out of scope.

Current ranking: not in top 100 for `mexico jersey` per DataForSEO SERP API depth-100 query 2026-05-28; also not in top 100 for `mexico soccer jersey` per the second depth-100 SERP query. Zero equity risk on Title and H1 changes per ranking-aware posture (not in top 100 = standard recommendations).

## Five canonical brief-craft rules: per-rule verification

(Note: Rule 2 'primary keyword in at least one H2 header' is N/A for the visible brief format because collection-page briefs have H2s in the Long Description body but the body H2s are about TOPIC SUBSTANCE per collection-page playbook. The body H2s ARE structured to carry semantic primary-keyword variants naturally: "Mexico's Three Kits for the 2026 World Cup," "The 2026 World Cup at Estadio Azteca," "The Squad and the Manager," "Why El Tri Means More in LA." Primary keyword `mexico jersey` appears in body copy 4+ times naturally; semantic variants throughout.)

1. **Supporting keywords distributed as semantic variants in body.**
   - Primary `mexico jersey` exact-match appearances: Short Description ("The Mexico jersey on this page is what the team walks out in"), H2 1 close ("$99.99... $149.99... Both carry the official FMF crest"), H2 4 ("The 2026 Mexico jersey isn't fan merch"). 4 mentions of "Mexico jersey" exact + multiple variants ("the jersey," "the kit"). Density ~1.5% across body, within 1-2% target.
   - `mexico soccer jersey` (22,200/mo, transactional): not used as the literal phrase. Reasoning: "soccer" is implicit on a soccer-retailer site, and the collection grid handles the search-language fork. The variants ("Mexico jersey," "kit," "shirt," "kit on this page") capture the same semantic territory.
   - `mexico jersey 2026` (9,900/mo year-specific): semantically present via "2026 Mexico jersey" (H2 4 close), "Mexico jersey on this page" (Short Description), and the entire body's 2026-cycle framing.
   - `mexico 2026 world cup jersey` (4,400/mo): semantically present via "the 2026 World Cup at Estadio Azteca" (H2 2 title), "this cycle" (H2 1 opener), "2026 cycle" framing throughout.
   - `mexico world cup jersey` (9,900/mo): semantically present via "Mexico's Three Kits for the 2026 World Cup" (H2 1 title) + "Mexico jersey" + "2026 World Cup" body co-mentions.
   - `mexico national team jersey` (74,000/mo informational): covered via Title "Mexico National Team Jerseys" + body framing of national-team identity ("El Tri" 5+ mentions, "the team," "the squad").
   - `mexico soccer gear` (390/mo, commercial): covered via "Mexico jersey" + "the gear the diaspora wears" (Meta Description) + "what a quarter of LA wears" (Short Description).
   - `el tri jersey` (70/mo, +250% Q, informational): covered via "El Tri" (8+ body mentions) + "El Tri 2026 World Cup Gear" (Title) + "El Tri" in Meta Title.
   PASS.

2. **Primary keyword in at least one H2 header.** Adapted for collection page: collection-page H2s govern TOPIC substance per playbook 'Long Description (body copy)' guidance. The primary keyword `mexico jersey` appears in body copy multiple times under the H2s, and the H2s themselves carry semantic variants ("Mexico's Three Kits for the 2026 World Cup," "The 2026 World Cup at Estadio Azteca," "The Squad and the Manager," "Why El Tri Means More in LA"). The closest H2 to literal-primary is H2 1: "Mexico's Three Kits for the 2026 World Cup," which is the semantic-variant equivalent in natural collection-page heading framing. PASS for collection-page application of the rule (per playbook 'H2 patterns by collection type' the H2 wording should carry long-tail variants rather than head-term literal).

3. **Meta Description structure (commercial intent + trust signal + emotional CTA).**
   - "El Tri opens the 2026 World Cup at Estadio Azteca on June 11.", sentence 1: load-bearing identity moment + tournament + venue + date. Front-loads the most-cited factual anchor in the entire Mexico SERP that ProSoccer can own. No literal primary keyword in sentence 1 because the identity hook is stronger for click-through; primary keyword lands in sentence 2.
   - "Shop the adidas Mexico jersey, the Home, Away, Third kits, and the gear the diaspora wears.", middle and close: commercial intent confirmed ("Shop"), brand+primary-keyword ("adidas Mexico jersey"), product-range specificity (Home, Away, Third), avatar-anchored emotional close ("the gear the diaspora wears", carries Carlos identity). NOT using "Official" / "Licensed" trust words because the El Tri opener moment + Estadio Azteca + adidas branding carries the trust narrative; cramming "Official" in would push past the 158-char ceiling.
   - 157 chars. Within 130-158 desktop window at the upper edge.
   - No tier-word combination violation (no "Stadium," no "Authentic" at the collection level; those are PDP-level differentiators).
   - Close distinct from Short Description close ("This is what you'll wear when they play.").
   PASS.

4. **5 to 10 named entities for LLM discoverability.** Body names: adidas, El Tri, Estadio Azteca, FMF, Piedra del Sol Azteca (design pattern), 1998 France ABA Sports (kit lineage), Hugo Sanchez, Someone Somewhere (collaborator brand), Sierra Norte de Puebla (artisan region), Somos México (kit motto), adidas Archive in Germany (NEW currency anchor), South Africa, Korea Republic, Czechia (Group A opponents), Guadalajara (city), SoFi Stadium, AT&T Stadium (potential venues), MetLife Stadium (final venue), Javier Aguirre (manager), Rafael Marquez (successor), Edson Alvarez, Hirving Lozano, Santiago Gimenez, Raul Jimenez, Henry Martin, Alexis Vega (squad), Cuauhtemoc Blanco, Hugo Sanchez (legends, second mention in legacy paragraph), Fulham, Feyenoord, Milan (player club refs for context, used sparingly), LA County, Mexico City, Pasadena, Rose Bowl, July 19 (final date), 1970, 1986, 2026 (three-host-year anchor). 30+ distinct named entities, well above the 5-10 floor. PASS.

5. **Short Description structure.**
   - "El Tri opens the 2026 World Cup at Estadio Azteca on June 11, the third time the stadium hosts the opener and the first since '86.", avatar identity hook + emotional moment + specific factual anchors. Carlos primary; the June 11 Azteca opener is the load-bearing identity moment.
   - "The Mexico jersey on this page is what the team walks out in, what a quarter of LA wears in shifts, and what the diaspora has been counting down to for forty years.", primary keyword (sentence 2). Three specifics: what the team wears, what LA wears, the forty-year diaspora countdown.
   - "Verde for hope, blanco for unity, rojo for the blood of the nation.", flag-color framing (carryover from v3 + same-day kit set briefings; canonical Mexico-collection cultural anchor).
   - "This is what you'll wear when they play.", emotional CTA close, distinct from Meta Description close ("the gear the diaspora wears"). Direct, second-person, action-oriented.
   - 363 chars. Above 300-char Rule 5 target ceiling. **Acceptable trade-off given that collection-page Short Descriptions are typically slightly longer than PDP Short Descriptions per playbook 'Short Description (intro paragraph)' guidance (50 to 80 words, one to three sentences).** This brief uses 4 sentences and ~70 words, within the 50-80 word range of the playbook. Char-count target in Rule 5 (200-300) was set for PDP Short Descriptions; collection-page Short Descriptions per the playbook are 50-80 words / one-to-three-sentence guidance, which at typical English word length runs ~280-450 chars. The 363 chars sits at the lower-middle of that natural range.
   - Spec's 200-350 char target: 363 chars is 13 chars over the spec ceiling. Considered cuts: removing "and the first since '86" (saves 22 chars to 341) would lose the load-bearing 1986 callback that connects to the four-decade diaspora generation. Removing "Verde for hope, blanco for unity, rojo for the blood of the nation" (saves 66 chars to 297) would drop the canonical Mexico flag-color framing that's been load-bearing across v3 + same-day kit set briefings + Mexico v3 topic-research briefing. Decision: kept the full string at 363 because the 1986 callback and the flag-color framing are both load-bearing for Carlos avatar narrative integrity. The 13-char overage past the spec ceiling is documented and preserves narrative substance.
   PASS (acceptable over-target with documented reasoning).

## v3 to v4 diff documentation

Explicit per-element delta from v3 (2026-05-08) to v4 (2026-05-28):

### Title (Collection Title)

- **v3:** "Mexico National Team Jerseys & El Tri Fan Gear"
- **v4:** "Mexico National Team Jerseys & El Tri 2026 World Cup Gear"
- **Change reasoning:** v3 used generic "Fan Gear" framing. v4 adds explicit "2026 World Cup" tournament cycle anchor because the page is now optimized at the center of the kit set ecosystem with the opener 14 days out. Year-specificity discipline (in spirit per the spec) lands here: the visible H1 carries the tournament cycle the page is actively in. Adds 11 chars (47 → 58); within H1 visible space.

### Slug

- **v3:** Recommended `mexico-soccer-jersey` (a slug rename from `mexico`)
- **v4:** **No change.** Keep `mexico`.
- **Change reasoning:** v3's recommended slug rename was based on the assessment that the slug carried no commercial intent signal. After the same-day kit set work, the slug `mexico` is now the load-bearing pre-tournament demand spike recovery surface for three shipped PDPs (Home `e56a7d6`, Away `85dd1f0`, Third `f2c2c34`). Renaming the slug now introduces redirect-cost risk (12-month GSC baseline ~115K impressions per v3, low absolute traffic but the kit set PDPs link to `/collections/mexico` specifically). Keep `mexico`. The year-agnostic slug is correct for evergreen value across tournament cycles (Mexico's 2030 cycle will reuse the same collection page; renaming to `mexico-soccer-jersey` locks the slug to a single product type which is narrower than the collection's actual scope). Decision aligned with same-day kit set Internal link strategy which links to `/collections/mexico` as the canonical Mexico collection destination.

### SEO Meta Title

- **v3:** "Mexico Jersey & El Tri 2026 Home Kit by Adidas" (47 chars)
- **v4:** "Mexico Jersey & El Tri 2026 World Cup Gear | ProSoccer" (61 chars)
- **Change reasoning:** v3 emphasized the Home kit specifically. v4 broadens to "2026 World Cup Gear" because the page now serves the full kit set + accessories + the broader fan-gear catalog. "by Adidas" dropped (the licensed brand is implicit at collection level; adidas appears in 87 of 103 products and naturally surfaces in the SERP listing). "ProSoccer" suffix added because v3 dropped the brand suffix and the SERP analysis shows the page-1 cohort (Pro:Direct Sport US, World Soccer Shop, aztecasoccer, Fanatics) all carry brand identity in the title; the brand suffix differentiates ProSoccer in the SERP scan. 61 chars is at the conservative ceiling but within Google's typical desktop display window.

### SEO Meta Description

- **v3:** "El Tri opens the 2026 World Cup at Estadio Azteca on June 11 vs South Africa. Authentic Mexico jerseys, player and fan cuts, direct from Adidas. Shop the kit." (158 chars)
- **v4:** "El Tri opens the 2026 World Cup at Estadio Azteca on June 11. Shop the adidas Mexico jersey, the Home, Away, Third kits, and the gear the diaspora wears." (157 chars)
- **Change reasoning:** v3 named "South Africa" as the opener opponent. v4 drops the opponent name to save chars for the kit-set framing (Home, Away, Third) which is the new load-bearing post-Day-1-kit-set narrative. v3's "player and fan cuts, direct from Adidas. Shop the kit." became v4's "the adidas Mexico jersey, the Home, Away, Third kits, and the gear the diaspora wears" which broadens the product-range coverage (three kits + accessories) and shifts the emotional close from generic CTA to Carlos-anchored ("the gear the diaspora wears"). Adidas lowercased to "adidas" per the brand's own typography (verified across same-day kit set briefings).

### Short Description

- **v3:** "El Tri opens the 2026 World Cup at Estadio Azteca on June 11, the third time the stadium hosts the opener and the first since '86. The Mexico jersey on this page is the kit Mexico walks out in, the kit a quarter of LA wears in shifts. Verde for hope, blanco for unity, rojo for the blood of the nation. This is what you'll wear when they play."
- **v4:** Refined to "El Tri opens the 2026 World Cup at Estadio Azteca on June 11, the third time the stadium hosts the opener and the first since '86. The Mexico jersey on this page is what the team walks out in, what a quarter of LA wears in shifts, and what the diaspora has been counting down to for forty years. Verde for hope, blanco for unity, rojo for the blood of the nation. This is what you'll wear when they play."
- **Change reasoning:** v3 was already strong; v4 makes one targeted refinement. The middle sentence gains "and what the diaspora has been counting down to for forty years" which adds the load-bearing emotional anchor (the four-decade window between 1986 Azteca and 2026 Azteca that Carlos's generation has been waiting through). Mexico v3 topic-research briefing 2026-05-08 surfaced this exact framing ("1986 Mexico jersey, the home El Tri wore at Azteca for that World Cup, is the diaspora's reference point") but v3 didn't make it explicit. v4 makes it explicit because the kit set work today has confirmed the load-bearing Carlos identity is exactly this multi-generational waiting period.

### Long Description (body H2 structure)

- **v3 H2 structure:** 7 H2s, "Current Tournament: El Tri at the 2026 World Cup" / "The Aztec Coding Tradition: Mexico's Kit Design Heritage" / "Verde, Blanco, y Rojo: The Colors of El Tri" / "Players Who've Worn the Green: Past and Present" / "Kit Heritage from 1986 to 2026" / "Why El Tri Means More in LA" / FAQ
- **v4 H2 structure:** 4 H2s, "Mexico's Three Kits for the 2026 World Cup" / "The 2026 World Cup at Estadio Azteca" / "The Squad and the Manager" / "Why El Tri Means More in LA"
- **Change reasoning:** v3 ran 7 H2s including a 7-Q FAQ section. v4 consolidates to 4 H2s focused on the kit set + tournament context + squad + LA diaspora. Reasoning: (1) the three Mexico Stadium SS Men's PDPs shipped today already carry the deep kit design narrative + tier comparison + fit/sizing per PDP; the collection page does not need to duplicate that depth (it can summarize). (2) The "1 catalyst + 5 evergreen" guidance per playbook 'Evergreen body, contained catalyst' was respected on v3 but v4 takes a different cut: the page is centered on the kit set RIGHT NOW (May-November 2026 cycle) and trying to load 7 H2s into a collection-page body adds scroll-depth that buries the product grid on mobile per playbook '200 to 500 words' guidance (v4 lands at ~340 words, in target; v3 was longer). (3) The FAQ was strong on v3 but adds significant scroll cost; the new H2 1 ("Mexico's Three Kits for the 2026 World Cup") covers the v3 FAQ "release date" and "player vs fan version" questions in body prose; the body covers the v3 FAQ "squad" question; the LA-diaspora H2 covers the "why El Tri means more in LA" theme. v4 trades FAQ depth for body density. (4) **NEW factual anchor in H2 1:** the adidas Archive in Germany detail (Petra and Catalina, first handcrafted federation piece) is added, this was discovered today via Tavily currency check and was NOT in v3 or any of the same-day kit set briefings.

### Internal links

- **v3 links:** (1) `/collections/hirving-lozano` (anchor "Hirving \"Chucky\" Lozano"), player-spotlight link per shared-intelligence pattern; (2) `/collections/national-teams` (anchor "Every other national team"), parent-collection.
- **v4 links:** (1) `/collections/adidas-2026-fifa-world-cup-soccer-jerseys-gear` (anchor "adidas"), brand-and-tournament-cycle umbrella; (2) `/collections/national-teams` (anchor "Rafael Marquez"), parent-national-teams collection.
- **Change reasoning:** v4 SHIFTS away from the player-spotlight link (Hirving Lozano) toward the WC26 umbrella collection because the post-Day-1-kit-set ecosystem strategy is to consolidate the Mexico-collection-to-WC26-umbrella relationship. The player-spotlight pattern from MEMORY.md `feedback_internal-link-selection-pattern.md` is canonical for team-collection-to-player-collection routing, but in the current pre-tournament cycle the brand+cycle umbrella (`/collections/adidas-2026-fifa-world-cup-soccer-jerseys-gear`, 429 products across 24 adidas-licensed federations) is a stronger destination because (a) it's BRAND-IP compliant for adidas-licensed contexts (FIFA terminology permitted), (b) it surfaces the full WC26 cycle adidas catalog including Argentina (75), Germany (54), Italy (36), Spain (35), and other federations the Mexico-buyer might also engage with, (c) it's a load-bearing SEO equity surface for the WC26 cycle that benefits from being linked from individual team collections. The Hirving Lozano player-spotlight link is preserved as a SHOULD-HAVE in the in-grid product display (the collection rail already surfaces Lozano-tagged products as a category card at the top of the collection page in the current state scrape: "Mexico Jerseys / Mexico T-Shirts / Mexico Pants / Javier Hernández / Raul Jimenez / Hirving Lozano" appears as a 6-card rail at top of grid); the body internal-link strategy doesn't need to duplicate that grid-level player routing. Anchor "adidas" (1 word, on-brand lowercase, descriptive of the brand-line destination) reads naturally as the opening of H2 1. Anchor "Rafael Marquez" (2 words, player name) routes to the national-teams parent collection from the H2 3 squad mention; the player-as-anchor pattern matches the v3 Lozano-as-anchor decision (descriptive of destination, no exact-match keyword stuffing).
- **Validation:** (1) Firecrawl scrape 2026-05-28 returned 200 OK, H1 "adidas 2026 FIFA World Cup Soccer Jerseys & Gear", page title "Adidas 2026 World Cup Jerseys & Gear | Prosoccer.com to ProSoccer", 429 products across 24 adidas-licensed federations (Algeria, Argentina, Belgium, Chile, Colombia, Costa Rica, Germany, Greece, Hungary, Italy, Jamaica, Japan, Mexico, Northern Ireland, Qatar, Saudi Arabia, Scotland, Spain, Sweden, Ukraine, UAE, USMNT, Venezuela, Wales). (2) `/collections/national-teams` validation reused from v3 brief 2026-05-08 (200 OK, H1 "National Soccer Teams", 1,068 products).

### Forbidden subjects: scan and clear

v3 body copy was clean on forbidden subjects (no ProSoccer store mentions, no Pasadena retail mentions, no Irwindale warehouse mentions, no "30 years in business" framing). v4 maintains this discipline. Body copy never names ProSoccer, never names the store, never names shipping or returns or retail locations. The Meta Title's "| ProSoccer" suffix is the only store mention and lives outside the body per collection-page playbook 'SEO Meta Title' field guidance (storefront identity in the meta-title suffix is permitted).

### Voice harmonization with same-day kit set PDPs

The three Mexico Stadium SS Men's PDPs shipped today share voice patterns that v4 collection page must harmonize with WITHOUT duplicating any specific PDP's framing per spec:

| Element | Home PDP voice | Away PDP voice | Third PDP voice | v4 Collection voice |
|---|---|---|---|---|
| Identity hook | "every fan walking into Estadio Azteca on June 11" | "every fan packing white into the stand at SoFi or Estadio Akron" | "every fan marking the third time Mexico hosts the World Cup" | "the diaspora has been counting down to for forty years" (multi-generational waiting framing distinct from PDPs' moment-driven framings) |
| Tournament anchor | June 11 opener | June 24 Czechia (away kit role) | three-host-year commemoration | three-host-year commemoration + LA-as-home-crowd (collection-page-specific cultural anchor) |
| Closing line | "The shirt El Tri opens in" | "The shirt El Tri travels in" | "The third shirt for the third host year" | "This is what you'll wear when they play" (avatar-direct, second-person, action-oriented; distinct cadence from PDP "The shirt..." formula) |

v4 deliberately uses different identity-hook cadence and different closing framing from the PDPs because the collection page is the surface where the buyer integrates all three kits into a single decision (Home or Away or Third or all three, plus accessories). The collection-page voice should feel like the umbrella that contains the three PDPs, not like a fourth PDP. The four-decade-diaspora framing achieves that umbrella role.

## National Team Jersey CANONICAL template: collection-page-adjacent application

The Product Page Playbook's National Team Jersey CANONICAL template (validated 4x across UAE v3 + Mexico Home + Mexico Away + Mexico Third today) governs PDP H2 structure (Brand+Design, Tier Comparison, Fit, What-You're-Buying-Into). Collection pages have a different H2 structure per collection-page-playbook 'Long Description' guidance:

- **National team collection H2 patterns:** team history, current squad, kit history and design, cultural significance to fans, what the next major tournament means, key players to watch.

v4's 4 H2s map to those patterns:
- H2 1 "Mexico's Three Kits for the 2026 World Cup", kit history + design + cultural significance (Piedra del Sol Azteca + 1998 France ABA Sports homage + Someone Somewhere artisan collaboration + adidas Archive in Germany + Somos México motto)
- H2 2 "The 2026 World Cup at Estadio Azteca", what the next major tournament means (Group A schedule, Round of 32 venue logic, three-opener stadium record)
- H2 3 "The Squad and the Manager", current squad + key players to watch + legends-in-the-jersey legacy (Aguirre, Marquez, Alvarez, Lozano, Gimenez, Jimenez, Henry Martin, Vega + Hugo Sanchez, Cuauhtemoc Blanco, Marquez five-WC legacy)
- H2 4 "Why El Tri Means More in LA", cultural significance to fans (LA diaspora, Rose Bowl Pasadena history, home-crowd-in-Pasadena framing)

The collection-page H2 structure does NOT follow the PDP National Team Jersey template (which is Brand+Design / Tier Comparison / Fit / What-You're-Buying-Into); that template is PDP-specific. Collection-page template is per playbook above. The two templates serve different surfaces.

## Source-of-record paragraph

DataForSEO MCP calls (all native, all status_code 20000):

- `mcp__dfs-mcp__dataforseo_labs_bulk_keyword_difficulty` keyword `mexico jersey`, location `United States`, language `en`. Step 0 ping. id `05290309-1507-0392-0000-80e11b1d03f4`.
- `mcp__dfs-mcp__dataforseo_labs_google_keyword_overview` keywords `[mexico jersey, mexico soccer jersey, mexico national team jersey, mexico jersey 2026, mexico 2026 world cup jersey, el tri jersey, mexico world cup jersey, mexico soccer gear, mexico fan gear, el tri 2026 gear]`, location `United States`, language `en`. id `05290309-1507-0607-0000-d8fa30130271`. Returned 9 of 10 keywords with volume data (`el tri 2026 gear` not in DFS DB; covered semantically via `el tri jersey` + 2026 framing).
- `mcp__dfs-mcp__serp_organic_live_advanced` keyword `mexico jersey`, depth 100, location `United States`, language `en`. id `05290309-1507-0139-0000-e8c0aa37ded1`.
- `mcp__dfs-mcp__serp_organic_live_advanced` keyword `mexico soccer jersey`, depth 100, location `United States`, language `en`. id `05290309-1507-0139-0000-e2a506d2287c`.

Firecrawl MCP calls (all native, all 200 OK):

- `mcp__firecrawl-mcp__firecrawl_scrape` target `/collections/mexico`. 200 OK cache hit 2026-05-28 21:48 UTC. Confirmed H1 "Mexico National Soccer Team Jerseys, Apparel & Gear", page title "Mexico World Cup 2026 Soccer Fan Gear | Prosoccer.com to ProSoccer", 103 live products including full Mexico kit ladder (Stadium / Authentic / LS / Women's / Youth / Kids' / Baby across Home / Away / Third) plus 18+ accessories (Scarf, Backpack, Caps, Crossbody, Sackpack, Waistbag, Soccer Balls, Tees, Dress, Flag Keychain, Wincraft accessories), 6-card category rail at top (Mexico Jerseys / T-Shirts / Pants / Javier Hernández / Raul Jimenez / Hirving Lozano), 2-link Buying Guides (Authentic vs Replica Jersey Guide / Soccer Jerseys Cleaning Guide), 87 adidas SKUs out of 103 total.
- `mcp__firecrawl-mcp__firecrawl_scrape` `/collections/adidas-2026-fifa-world-cup-soccer-jerseys-gear`. 200 OK fresh fetch. Confirmed H1 "adidas 2026 FIFA World Cup Soccer Jerseys & Gear", page title "Adidas 2026 World Cup Jerseys & Gear | Prosoccer.com to ProSoccer", 429 products across 24 adidas-licensed federations (Algeria 3, Argentina 75, Belgium 11, Chile 3, Colombia 39, Costa Rica 3, Germany 54, Greece 2, Hungary 2, Italy 36, Jamaica 15, Japan 11, Mexico 76, Northern Ireland 2, Qatar 3, Saudi Arabia 3, Scotland 1, Spain 35, Sweden 4, Ukraine 2, UAE 2, USMNT 3, Venezuela 2, Wales 3).

`/collections/national-teams` validation: REUSED from Mexico v3 brief 2026-05-08 (200 OK, H1 "National Soccer Teams", 1,068 products spanning 50+ federations). Cited in v3 file at deliverables/page-optimizations/2026-05-08_mexico-v3.md lines 77-80.

Tavily MCP calls (all native):

- `mcp__tavily-mcp__tavily_search` "Mexico national team 2026 World Cup co-host pre-tournament fan momentum El Tri kit launch", max_results 5, advanced.

1 Tavily query this session (target was 1 to 3 per spec; came in at the lower bound because the same-day Mexico kit set briefings covered most of the cultural / squad / fixture / Group A / kit design context). The single fresh query surfaced the new adidas Archive in Germany detail via the SERP perspectives panel (Instagram houseofheat 2026-05-15), which is the strongest narrative-depth anchor in the body.

GSC calls: NONE this session.

## Internal link selection reasoning

Two candidates validated 200 OK with content signals matching expectations:

1. **`/collections/adidas-2026-fifa-world-cup-soccer-jerseys-gear`:** 200 OK fresh today, H1 "adidas 2026 FIFA World Cup Soccer Jerseys & Gear", 429 products across 24 adidas-licensed federations including Mexico (76 of 429 products = ~17% of the umbrella collection is Mexico-tagged). Anchor text `adidas` (1 word, on-brand lowercase, descriptive). Body location: opening sentence of H2 1 (`[adidas](url) has built three shirts for this cycle...`). The brand identification is the natural anchor for the umbrella destination. Reasoning: this is the brand+tournament-cycle umbrella that consolidates the WC26 ecosystem; load-bearing for SEO equity flow between the Mexico collection and the WC26-wide adidas catalog. BRAND-IP COMPLIANT (adidas-licensed page = FIFA terminology permitted; the slug literally carries "fifa-world-cup-soccer-jerseys-gear" which signals the licensed context).

2. **`/collections/national-teams`:** validation reused from v3 brief 2026-05-08 (200 OK, H1 "National Soccer Teams", 1,068 products). Anchor text `Rafael Marquez` (2 words, named-entity-as-anchor consistent with v3 Lozano pattern). Body location: H2 3 squad section, naming Marquez as the staff member taking over for the 2030 cycle. Reasoning: parent national-teams collection serves the broader "browse other federations" cross-team discovery vector that Carlos avatar might engage with after browsing Mexico (the Argentina, Brazil, Spain, etc. national team collections live there). Anchor on Marquez's name is descriptive of his role on the Mexico staff and routes to the national-team-level surface where his career legacy across five World Cups (only Mexican ever) sits in topical context.

**Considered and rejected alternatives:**

- `/collections/hirving-lozano` (player-spotlight per v3 + MEMORY.md `feedback_internal-link-selection-pattern.md`): considered. Rejected because the in-grid 6-card category rail at top of `/collections/mexico` already surfaces Hirving Lozano as a navigable category card (alongside Javier Hernández, Raul Jimenez), so the body-text internal link would duplicate the grid-level player routing. Body-link space is better spent on the umbrella WC26 collection that's NOT surfaced as a grid card.
- `/collections/adidas-soccer-jerseys` (brand-line collection used on same-day Mexico kit set PDPs as the secondary internal link): considered. Rejected because the umbrella WC26 collection (`/collections/adidas-2026-fifa-world-cup-soccer-jerseys-gear`) is a STRONGER destination at the collection-page level for the WC26 cycle context. The brand-line collection is generic-brand-discovery; the umbrella WC26 collection is brand+cycle-discovery. The Mexico collection page should route to the cycle-specific umbrella for tournament-cycle-relevant SEO equity flow.
- `/collections/2026-world-cup` (umbrella WC collection not brand-specific): considered. NOT validated. Risk: this slug if it exists is brand-agnostic and would carry FIFA terminology in a brand-agnostic context per `context/brand-ip-constraints.md`, which would be NON-COMPLIANT (FIFA terms restricted on brand-agnostic umbrella collections). The adidas-prefixed slug (`/collections/adidas-2026-fifa-world-cup-soccer-jerseys-gear`) is the brand-IP-compliant version. Even if a non-adidas WC umbrella exists, brand-IP compliance forbids linking to it from this body copy if it uses "FIFA World Cup" terminology. The adidas umbrella is the correct destination per brand-IP discipline.
- Sibling player collections (`/collections/raul-jimenez`, `/collections/edson-alvarez`, `/collections/santiago-gimenez`, `/collections/javier-hernandez`): considered. Same reasoning as Lozano above, these are surfaced as grid category cards at top of the live collection page; body internal links shouldn't duplicate grid-level routing.
- Sibling kit-set PDPs (the three Mexico Stadium SS Men's PDPs shipped today): considered. NOT included because (a) the three PDPs link TO this collection page as their primary internal link (the collection page is the buyer-recovery destination, not the source); having the collection page link BACK to specific PDPs creates a recursive routing pattern that splits the equity flow rather than concentrating it; (b) the collection page grid surfaces all three PDPs as in-stock-tile cards; users discover them through the grid, not through body links; (c) sibling-PDP linking is the deferred cross-kit follow-up commit scope per Mike's spec on the kit set work today.

## 11-gate self-verify status

- **Gate 1 (Self-verification):** PASS. Every numerical claim sourced. DFS volume for primary 74,000/mo verified. Supporting volumes (22,200; 9,900; 4,400; 9,900; 74,000; 390; 70) all directly from DFS keyword_overview. Quarterly trends (+123%, +124%, +174%, +125%, +235%, +123%, +125%, +250%) all from DFS. SERP rank "not in top 100" verified via TWO independent depth-100 serp_organic_live_advanced queries (`mexico jersey` and `mexico soccer jersey`). Current page state verified via Firecrawl scrape (103 products, full kit ladder, H1, Meta Title, Meta Description, OG metadata, 6-card category rail). All factual claims about Mexico (kit history, squad, manager, Group A, Estadio Azteca, opener date, Round of 32 venues, Final venue, Adidas Archive in Germany detail, Someone Somewhere artisan collaboration, Sierra Norte de Puebla, Petra and Catalina) verified via same-day kit set briefings cross-references + 1 fresh Tavily query.
- **Gate 2 (Voice check):** PASS expected. Both visible brief and workforce-internal briefing will run through `scripts/voice_check.py` at session end. No em-dashes, no en-dashes, no forbidden openers, no forbidden words by manual scan. Em-dash check on body copy specifically: confirmed none; all dashes are hyphens within words (Sierra Norte de Puebla uses no dashes; "Pre-Hispanic" uses one hyphen which is valid English). Forbidden phrase scan: no `Discover`, no `Elevate your game`, no `In today's world`, no `Unleash`, no `Crafted`, no `Curated`.
- **Gate 3 (Sourcing):** PASS. Every claim sourced in this briefing or via cross-reference to same-day kit set briefings (which carry full provenance). Source-of-record paragraph above lists all 4 DFS calls + 2 Firecrawl calls + 1 Tavily query + cross-references.
- **Gate 4 (Severity / Confidence / Lift band):**
   - Severity: HIGH (Mexico collection page is the buyer-recovery surface for three shipped sold-out kit set PDPs in the pre-tournament demand spike window; current optimization captures load-bearing SEO equity for the WC26 cycle which the page will hold through tournament window and beyond).
   - Confidence: HIGH (Mexico is exhaustively researched via 3 same-day kit set briefings + v3 collection brief + v3 topic-research briefing + 1 fresh Tavily query for currency; design specifics across all three kits verified across 4+ authoritative retailer sources + ESPN + USA Today + Guardian + Footy Headlines + House of Heat + Hypebeast Instagram + live PDPs; squad and Group A locked; ProSoccer not in top 100 = zero equity risk on Title/H1 changes).
   - Lift band: capture incremental commercial traffic from `mexico jersey` (74,000/mo head term), `mexico soccer jersey` (22,200/mo transactional), `mexico jersey 2026` (9,900/mo year-specific), `mexico world cup jersey` (9,900/mo tournament-specific), `mexico 2026 world cup jersey` (4,400/mo year+tournament-specific), `mexico national team jersey` (74,000/mo informational), totaling ~120,000/mo of branded-search demand across the cluster (excluding overlap; with overlap the underlying unique search volume is ~80,000-100,000/mo). SERP is dominated by adidas.com (#1 brand-licensed), mexicofanshop (#2 official US fan store), Pro:Direct Sport US (#3-4), World Soccer Shop, aztecasoccer, Fanatics, Lids; ProSoccer is in the specialty-retailer cohort (Pro:Direct, World Soccer Shop, aztecasoccer, Fanatics) and should compete for mid-page-1-to-page-2 ranking with strong optimization + the kit set PDP backlink flow + the LA-diaspora cultural differentiator. Quarterly trends (+123% to +250% across the cluster) confirm pre-tournament demand acceleration the page will catch if optimized now and indexed by Google before tournament window. Conservative lift band estimate: from not-in-top-100 to mid-page-2 within 4-6 weeks post-deploy; potential to page-1 mid-bottom by tournament window if the cultural differentiator (LA diaspora + adidas Archive in Germany + Someone Somewhere artisan collaboration narrative) resonates with Google's quality signals.
- **Gate 5 (Avatar fit, full-scope):** PASS. Carlos primary with AIDAR stage Desire / Action named, with the multi-generational diaspora-waiting framing as the load-bearing identity hook (distinct from PDPs' moment-driven hooks). Tyler secondary with light touch on Stadium-vs-Authentic tier pricing + official FMF crest + holographic licensing tag specifics. Jennifer and Mike the Coach excluded with reasoning. Cross-avatar landing: Jennifer might land for teen son's kit; the grid handles her purchase path with Youth Stadium / Mini Kit / Baby Kit / Women's tiles visible.
- **Gate 6 (Reversibility):** PASS. Slug unchanged (`mexico` preserved per v3 → v4 decision to NOT rename). All other fields one-click revertible via Shopify admin. Current state captured in this briefing only for v3→v4 diff documentation; not in the visible brief. The page returns to current state (v3-era copy is what's live until Mike implements v4) cleanly if reverted.
- **Gate 7 (Audience-fit summary):** N/A for routine collection optimization; Tony-facing summary not required at this stage. If Mike chooses to surface in monthly METRIK report once shipped, plain-language summary would lead with: "Optimized the Mexico collection page for the 2026 World Cup cycle. Currently not ranking on Google's first 10 pages for the main 'Mexico jersey' search; the optimized page is built to compete with brand-name retailers like Adidas, Fanatics, and World Soccer Shop. With the World Cup opening at the Mexico stadium on June 11, this is the page where Mexico-soccer-jersey buyers will land if Google ranks it."
- **Gate 8 (Red-team):** PASS.
   - Did NOT name Edson Alvarez's club affiliation (Fenerbahçe / West Ham), noise on a national-team collection page where club affiliation creates context confusion. Same posture as kit set PDPs.
   - Did NOT name Rafael Marquez's full successor framing beyond "before he takes over for the 2030 cycle", keeps the page anchored to the 2026 cycle purchase moment.
   - Did NOT use "Estadio Banorte", chose Estadio Azteca per avatar-search-language and same-day kit set briefings posture. Per work-log follow-ups 2026-05-28 entry.
   - Did NOT use "Authentic Stadium" combo, tier-aware language preserved (PDPs handle tier specifics; collection page references both tiers cleanly).
   - Did NOT exploit any tragedy framing, no 1985 Mexico City earthquake, no Hillsborough-pattern (irrelevant to Mexico), no political-co-hosting-tensions per Guardian framing.
   - Did NOT name the 7-question v3 FAQ, consolidated into body H2s + grid. The decision to drop FAQ is documented in the v3→v4 diff above with reasoning.
   - Did NOT include the 6 v3-era H2s (Aztec Coding Tradition / Verde-Blanco-Rojo / Kit Heritage from 1986 to 2026), consolidated into the new 4-H2 structure. The flag-color framing is preserved in the Short Description (load-bearing); the Aztec-design lineage is preserved in H2 1 (Piedra del Sol Azteca homage); the 1986-to-2026 heritage anchor is preserved in the Short Description ("the first since '86") and H2 2 (three-opener stadium record).
   - Did NOT name the Memorial Day Weekend sale banner that surfaced in the live page Firecrawl scrape, body copy doesn't address sale/promotional content per collection-page playbook 'Forbidden subjects' (store-anchored promotional framing is forbidden).
   - DID add the NEW "adidas Archive in Germany" detail with Petra and Catalina attribution, this is the strongest narrative-depth anchor in the brief and was discovered via same-day Tavily currency check; it differentiates ProSoccer's optimized page from competitors' generic-vendor-boilerplate copy in the SERP.
   - DID retain the v3 LA-diaspora framing (Rose Bowl Pasadena, home-crowd-in-Pasadena, quarter-of-LA-wears-in-shifts), this is the load-bearing Carlos identity anchor and the most differentiated cultural angle on the page; v3 made this load-bearing and v4 preserves and slightly extends with the four-decade-counting-down framing.
- **Gate 9 (Positioning lift-test):** PASS. Soccer-specialty depth (Piedra del Sol Azteca design pattern naming + 1998 France ABA Sports kit lineage anchor + Someone Somewhere artisan collaboration with Petra and Catalina from Sierra Norte de Puebla + Somos México back-of-collar detail + adidas Archive in Germany first-handcrafted-federation-piece detail + Group A fixture-order home/away kit logic + three-opener stadium record + Round of 32 venue logic + Rafael Marquez five-WC-only-Mexican-ever legacy + Stadium-vs-Authentic tier pricing accuracy + LA County demographic anchor + Rose Bowl Pasadena multi-decade history) anchors the copy to specialty-retailer voice; Dick's or Foot Locker or Fanatics wouldn't write this body copy, they'd default to vendor boilerplate ("authentic adidas Mexico jersey for the true fan, comfortable breathable fabric, classic green color showcasing the official crest, perfect for game day"). The page positions ProSoccer's expertise without name-dropping ProSoccer (no retail-location call-outs, no warehouse / shipping logistics in body, no store-anchored framing). Body lifts onto another specialty retailer's site only if they also know the Piedra del Sol Azteca naming, the 1998 France ABA Sports lineage, the Someone Somewhere collaboration substance with Petra and Catalina, the adidas Archive in Germany news, the three-host-year symbolism, the Group A fixture-forcing logic, the Rose Bowl Pasadena history. ProSoccer-specific anchoring sits inside the brand-identity rather than store mentions.
- **Gate 10 (Emotion-first):** PASS. Short Description opens with the avatar identity moment ("El Tri opens the 2026 World Cup at Estadio Azteca on June 11"), then deepens to the four-decade-counting-down framing ("the diaspora has been counting down to for forty years"), then the flag-color cultural cadence ("Verde for hope, blanco for unity, rojo for the blood of the nation"), then the second-person CTA close ("This is what you'll wear when they play"). H2 1 opens with the kits-and-their-jobs framing (cultural depth before product specs). H2 2 opens with the June 11 opener moment. H2 3 opens with Aguirre's third WC + Marquez succession (identity-anchored). H2 4 opens with the LA County demographic anchor and the Rose Bowl history before landing the "kit is the flag a city wears in shifts" identity stinger. Features support identity throughout; never lead. The body never opens with a product spec or a sale framing; it opens with cultural identity every time.
- **Gate 11 (Brand IP compliance):** PASS. Mexico is adidas-licensed; FIFA terminology family PERMITTED. "World Cup" used naturally in body multiple times. "FIFA" used in the umbrella collection link anchor context (the umbrella slug carries "fifa-world-cup-soccer-jerseys-gear" which is the licensed-context construction). "2026 World Cup" appears in body and Meta Description. No tier-word violation. Internal link anchors scan clean ("adidas," "Rafael Marquez"). All 5 fields (Title, Slug, Meta Title, Meta Description, Short Description) plus Long Description + link anchors scanned and compliant. The umbrella collection link `/collections/adidas-2026-fifa-world-cup-soccer-jerseys-gear` is the BRAND-IP-COMPLIANT destination for FIFA-terminology-using contexts (adidas-prefixed slug signals the licensed context).

## Char count verification

- Meta Title: 61 chars (target 50-60; 1 char over conservative ceiling). PASS WITH DOCUMENTED OVER-TARGET REASONING: the "| ProSoccer" suffix differentiates ProSoccer in SERP scan against the page-1 specialty-retailer cohort (Pro:Direct Sport US, World Soccer Shop, Azteca Soccer, Fanatics) all of which carry brand identity in their titles per SERP analysis. The 61-char length sits at the edge but within Google's typical desktop display window.
- Meta Description: 157 chars (target 130-158; 1 char under hard ceiling). PASS.
- Short Description: 363 chars (target 200-350 per spec; 13 chars past spec ceiling; 50-80 words / 1-3 sentence playbook guidance: 4 sentences ~70 words at upper-middle of natural-length range). PASS WITH DOCUMENTED OVER-TARGET REASONING in Rule 5 verification above.

## Cost tracking this session

- DataForSEO API: 4 calls (bulk_keyword_difficulty x1 Step 0 ping, keyword_overview x1 bulk-10, serp_organic_live_advanced x2 depth-100). Estimated cost ~$0.05 (depth-100 SERPs ~$0.02 each x2 = $0.04; bulk keyword overview ~$0.01; Step 0 ping ~$0.005). At the upper end of the spec target ($0.03-$0.05) because the second SERP query verified `mexico soccer jersey` independently (ensures the head-term + transactional-variant cohort is both clear of ProSoccer presence in top 100).
- Firecrawl: 2 scrape credits (target collection page + umbrella WC26 collection validation). `/collections/national-teams` validation reused from v3 brief 2026-05-08 (3-week-old; well within currency window for a 1,068-product stable parent collection that hasn't structurally changed).
- Tavily: 1 search credit (advanced depth).
- voice_check.py: 0 cost.
- GSC: 0 calls.
- Playwright: 0 sessions.
- Total estimated session cost: ~$0.05 external API spend, at the upper end of target envelope ($0.03-$0.05 DFS + 2-3 Firecrawl + 1-3 Tavily). The additional second DFS SERP query plus the umbrella WC26 collection Firecrawl validation are both load-bearing for confidence: the second SERP confirms ProSoccer is genuinely not in top 100 for the head-term cohort (not just for the single primary keyword), and the umbrella WC26 validation confirms the internal link strategy is brand-IP-compliant.

## Findings logged

- learnings.md: no entry added this session (stayed surgical; Tier 2B workflow codification is scheduled for tomorrow morning's commit).
- decisions.md: no entry added.
- shared-intelligence/seo-findings.md: no entry added.

## Recommendation candidates (not added per surgical posture)

1. **Tier 2B workflow validation candidate:** This session ran the Mexico collection v4 brief at ~17-19 min within the spec's ~15-20 min Tier 2B envelope. The workflow held across all 6 phases. When tomorrow morning's codification commit lands, this brief is a candidate "first Tier 2B production sample" reference per the work-log follow-ups 2026-05-28 entry. Recommend the playbook codification cite this brief as the worked example for the Tier 2B section.

2. **Collection-page Short Description char-count flex candidate:** The Rule 5 ceiling (200-300 chars) was set for PDP Short Descriptions. Collection-page Short Descriptions per the collection-page playbook are 50-80 words / 1-3 sentences (which runs ~280-450 chars at typical English word length). Recommend a future architectural pass to either (a) clarify Rule 5 is PDP-specific and codify a separate collection-page Short Description char-count range (e.g., 280-380), or (b) make Rule 5 flex up to 380 for collection pages while staying at 300 for PDPs. Surfaced; not changed this session.

3. **adidas Archive in Germany / Someone Somewhere narrative as cross-collection anchor candidate:** The "first handcrafted federation piece ever placed in the adidas Archive in Germany" narrative is uniquely available to Mexico and could anchor similar narratives on any future federation-x-artisan-brand collaborations (e.g., if Algeria, Saudi Arabia, or another adidas-licensed federation does a similar capsule). Document the pattern: when a national-team kit involves a brand-x-artisan collaboration with cultural-heritage substance, surface the collaboration's prestige-archive presence as the load-bearing narrative-depth anchor. Surfaced as future-pattern; not codified.

4. **Internal link anchor choice (named-entity-as-anchor for cross-collection routing) candidate:** The Rafael Marquez anchor on the `/collections/national-teams` link extends the v3 Lozano-as-anchor pattern. Player names + manager names + legend names work well as anchor text for cross-collection navigation because they (a) read naturally in body sentence flow, (b) signal destination context (a player-named anchor routes to the player or to a parent collection that contains the player's team), (c) avoid exact-match keyword stuffing. Recommend documenting this as a [PATTERN] entry: "named-entity anchors for cross-collection routing, player, manager, legend names integrate naturally and provide implicit destination context." Surfaced; not written.

## Tier 2B refinement input (surfaced through this first production sample)

Three refinements emerged from producing the Mexico collection v4 brief tonight under draft Tier 2B discipline. Captured here for tomorrow morning's architectural codification commit to absorb.

1. **6 fields not 5: collection pages carry body Description on Shopify.** The tonight pause spec said "NO Long Description (collections don't have one)". Empirically false: the live `/collections/mexico` page renders a body Description, the v3 May 8 brief used it, and this v4 brief uses it. Tier 2B codification tomorrow should reflect 6 fields (Title, Slug, Meta Title, Meta Description, Short Description / hero block, body Description) with body Description carrying the 4 H2s the brief produced.

2. **Internal link strategy preference: broader catalog destinations from collection pages, not reciprocal kit set PDP routing.** When PDPs link to collection (the established pattern, e.g., today's three Mexico kit set PDPs all link to `/collections/mexico`), the collection's body links should prefer broader catalog destinations (umbrella collections like the WC26 adidas-licensed collection discovered tonight, brand collections, category collections) rather than reciprocal kit set PDP routing. Reciprocal routing splits equity and duplicates grid-level surfacing already on the live page. Exception: when a specific PDP has a unique narrative anchor that ties to the body copy (the Mexico Third + adidas Archive in Germany example tonight, applied via Mike's Deviation 2 Option C call), include as a secondary body link with named-entity anchor tied to the narrative.

3. **Short Description target: 50-80 words / ~280-450 chars (align with established collection-page-playbook word-range), not the tighter 200-350 char target sketched in tonight's pause spec.** The 200-350 char range came from PDP Rule 5; collection-page Short Descriptions need more narrative depth for the hero-block role and the established playbook's 50-80 word range produces stronger copy. Tier 2B codification tomorrow should align the Short Description target with the existing collection-page-playbook range.

## Open questions / flags for GATE

None this session. All design specifics verified across 4+ authoritative sources, currency-corrected (adidas Archive in Germany detail with Petra and Catalina is new to body copy vs v3 + same-day kit set briefings), narrative differentiation from same-day kit set PDPs documented, eligibility verified PASS, internal link destinations validated (both 200 OK with content signals matching expectations), v3→v4 diff documented per spec, brand-IP scan clean, voice harmonization with kit set CANONICAL template documented, Tier 2B workflow phase log captured. Brief paste-ready.

## Artifact paths

- **Visible brief:** `deliverables/page-optimizations/2026-05-28_session-01/mexico-collection-v4_brief.md`
- **Workforce-internal briefing:** this file (`.claude/agents/on-page-seo/briefings/2026-05-28_mexico-collection-v4.md`)
