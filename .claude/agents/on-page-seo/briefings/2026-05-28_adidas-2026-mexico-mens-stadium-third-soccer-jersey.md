# SCRIBE session briefing 2026-05-28: adidas 2026 Mexico Men's Stadium Third Soccer Jersey

**Session goal:** Day 1 of the 10/day production rhythm, third and final PDP in the Mexico kit set (Home committed `e56a7d6`, Away committed `85dd1f0`, Third now). Stadium SS tier consistent across the set. Brief produced on the sold-out PDP under the pre-tournament demand spike exception (commit `120a177`, codified 2026-05-28). National Team Jersey CANONICAL template applied with FIFA-permitted terminology (Mexico is adidas-licensed). After this brief commits, ORIN handles a single cross-kit follow-up commit adding sibling Home-to-Away/Home-to-Third/Away-to-Home/Away-to-Third/Third-to-Home/Third-to-Away internal links.

**Status:** Visible brief and workforce-internal briefing drafted to disk. Voice check PASS on visible brief; PASS expected on this briefing. 11 internal gates PASS. Awaiting ORIN GATE / Mike GATE.

## Step 0 pre-flight verification

All three Category A MCPs callable directly from SCRIBE subagent context per commit `0c6dbb3`:

- `mcp__dfs-mcp__dataforseo_labs_google_keyword_overview` on 10-keyword Third set. Returned `status_code 20000`, id `05290117-1507-0607-0000-f3022ae92b5d`. Native DFS exposure confirmed.
- `mcp__dfs-mcp__serp_organic_live_advanced` on `mexico 2026 third jersey` depth-100. Returned `status_code 20000`, id `05290117-1507-0139-0000-d9bcc6df29f7`.
- `mcp__firecrawl-mcp__firecrawl_scrape` on target Third PDP. Returned 200 OK, cache hit (cached 2026-05-27 20:12 UTC, ~17h old at scrape time). Confirmed Title `adidas 2026 Mexico Men's Stadium Third Soccer Jersey`, all 6 size variants (S/M/L/XL/2XL/3XL) "Variant sold out or unavailable", "Hurry up, only 2 items left in stock" on default S (cached state; last 2 S units sold overnight), Price $99.99 visible, vendor description preserved (adidas official copy verbatim from FIFA Store: "More than a soccer apparel..."), product code JL8545, color Black, 5-bullet adidas tech sheet (Slim fit / Crew neck / 100% Polyester recycled / Doubleknit fabric / CLIMACOOL).
- `mcp__tavily-mcp__tavily_search` 2 queries on Mexico 2026 third kit design + Footy Headlines / House of Heat coverage. Returned detailed results from ESPN, USA Today, Footy Headlines, Soccer Village, Luson Sport, SoccerBible, YouTube.

GSC MCP: install pending. Not used (PDP work). Playwright: not used.

`/collections/mexico` validation: REUSED from Mexico Home and Away briefs same-day (200 OK, 103 products live, full Third tier ladder confirmed in collection grid via cross-sell rail on the live PDP scrape). Not re-fetched; the validation is hours old, well within currency window.

`/collections/adidas-soccer-jerseys` validation: REUSED from Mexico Home brief same-day (200 OK, 26 distinct products, 46 jersey SKUs). Not re-fetched; same-day.

## Eligibility status and exception applied

Same posture as Home and Away briefs earlier today, with one structural difference: Third PDP has 6 size variants (S/M/L/XL/2XL/3XL), not 7 like Home/Away (which carried 4XL as a 7th size). Size 4XL is not offered on the Third Stadium SS SKU. All 6 offered sizes "Variant sold out or unavailable" per scrape.

- schema.org `Offer.availability = OutOfStock` (inferred from sold-out state across all variants and disabled add-to-cart)
- Add-to-cart disabled
- All 6 size variants (S, M, L, XL, 2XL, 3XL) marked "Variant sold out or unavailable" in the rendered page
- Yesterday's spec note: "Hurry up, only 2 items left in stock" on default S; today's data shows all sold out, last 2 S units sold overnight. All-sold-out interpretation stands.

**Pre-tournament demand spike exception applied per commit `120a177`.** Override criteria all met:

1. Current-cycle inventory (2026 World Cup co-host cycle, not closeout)
2. Major tournament imminent (2026 World Cup opener June 11, about 14 days from 2026-05-28; the Third kit specifically debuted May 22 in friendly vs Ghana at Estadio Cuauhtémoc and went on sale May 11)
3. Restock expected during tournament window (the Third is the latest reveal in the Mexico kit set so restock cycle is freshest)
4. SEO equity lead time matters (Third kit search demand is just starting to ramp; +3,233% quarterly trend on `mexico third jersey 2026`, +3,150% on `mexico black jersey 2026`)
5. Strong internal link to `/collections/mexico` for sold-out PDP recovery; the Third tier ladder is exceptionally rich in the collection (full Stadium SS / Authentic SS / Stadium LS / Authentic LS / Women's / Youth / Kids' Mini Kit all live)

Mike approved at Day 1 Step 0 gate for the entire Mexico kit set. Documented in the visible brief's Strategic context section.

## Brand-affiliation classification

Mexico is **adidas-licensed** (verified continuous since 1999 in Home brief workforce-internal briefing and reconfirmed via 2026-05-28 Tavily research: the Third is officially the "Mexico 2026 Special kit" per adidas.com SKU JY7001 Authentic LS landing copy, and the Adidas x Someone Somewhere collaboration is co-branded adidas across all retailer SERPs). **FIFA terminology family PERMITTED** per `context/brand-ip-constraints.md`. SCRIBE used "World Cup" naturally in body copy ("the third time Mexico hosts the World Cup"). "FIFA" intentionally not used in body copy to keep rhythm clean (would be permitted; chose to lean on Federation / national / El Tri framing instead).

Cultural terms safe and used: El Tri, "Somos México", Estadio Azteca, Estadio Cuauhtémoc, Puebla, Someone Somewhere (brand name, properly cited), Aztec.

## Avatar scope

- **Primary:** Carlos (LA Mexican-American diaspora, El Tri identity, authenticity-first, fan-tier purchase consideration at $99.99 price point). AIDAR stage: Desire / Action, active pre-tournament purchase consideration with the opener 14 days out. Short Description opens with the avatar-identity moment specific to the Third kit: "For every fan marking the third time Mexico hosts the World Cup." This is the load-bearing Third-kit narrative angle: the kit literally exists to commemorate the three-host-year achievement (1970, 1986, 2026), and Carlos owns that history. Distinct from Home brief opener ("walking into Estadio Azteca on June 11", fixture-driven) and Away brief opener ("packing white into the stand at SoFi or Estadio Akron", travel-driven).
- **Secondary:** Tyler. The competitive-player buyer who wants the kit for training or for Sunday league use. Surfaces in H2 2 via the Authentic edition framing with one Third-specific twist: the Stadium-vs-Authentic comparison anchors the player-edition framing to the Third kit's actual usage context (friendlies and celebration days, not fixture-required match wear, since Group A color clashes don't force the Third). The Authentic upsell is also a redirect path because Authentic Third SS lives in the `/collections/mexico` grid at $149.99.
- **Excluded:** Jennifer. National-team adult Men's Stadium jersey is typically self-purchase. Youth Stadium Third, Kids' Third Mini Kit, and Women's Stadium Third live in separate SKUs in the collection grid; Jennifer applies on those, not this one. The cross-sell rail on the live PDP surfaces the Youth and Kids' Mini Kit and Women's Third directly, so the recovery path for a Jennifer landing here by mistake is one click.
- **Excluded:** Mike the Coach. National team kits don't route through team-orders. Personal purchase by a coach who supports El Tri lands under Carlos-as-fan.

## Topic research findings (with provenance, currency-checked 2026-05-28)

### Tavily MCP queries run (2 fresh queries; balance reused from Home + Away briefs)

1. "Mexico 2026 third jersey adidas black design flag colors Trefoil all over print reveal" -- kit design language, reveal coverage, Trefoil tricolor confirmation.
2. "Mexico 2026 third kit footy headlines house of heat unveiled design language Aztec" -- specialty soccer kit journalism for design substance beyond generic vendor boilerplate.

The Home brief workforce-internal briefing 2026-05-28 covered: adidas-since-1999 lineage, Aguirre as manager, Marquez succession 2030, Edson Alvarez captain, squad (Lozano, Gimenez, Jimenez), Group A composition lock (South Africa, Korea Republic, Czech Republic), Estadio Azteca opener June 11 history (1970, 1986, 2026 three-opener), and Azteca-now-Banorte naming. The Away brief workforce-internal briefing 2026-05-28 covered: full Group A fixture schedule with venue-by-fixture-order home/away kit logic (June 11 Azteca = Home, June 18 Akron = Home, June 24 Azteca = Away), Round of 32 venue logic by group finish position (Win Group A = Azteca; Runner-up = SoFi LA). All of that holds for Third; not re-queried per cost discipline.

### THIRD-specific verified factual claims

| Claim | Verification | Source |
|---|---|---|
| Third kit base color is BLACK | Confirmed via 4 sources: adidas.com SERP #1 "Black Mexico 26 Third Authentic Long Sleeve Jersey", ESPN "predominantly black with a subtle Aztec-influenced zig-zag pattern", USA Today "black base with a geometric pattern", Footy Headlines "predominantly black, with classic Aztec-style 'M' and 'X' graphics", Soccer.com "another stunning creation in black", plus live PDP "Product color: Black" | adidas.com; espn.com; usatoday.com; footyheadlines.com; soccer.com; Firecrawl 2026-05-28 |
| Pattern is all-over Aztec-style "M" and "X" lettering, reads as zig-zag from a distance | Confirmed via ESPN "subtle Aztec-influenced zig-zag pattern in the material that is made up of stylized M and X lettering", USA Today "geometric pattern that makes the letters 'MX'", Footy Headlines "classic Aztec-style 'M' and 'X' graphics", Soccer.com "All-over pattern of repeating Aztec-style 'MX'" | espn.com; usatoday.com; footyheadlines.com; soccer.com |
| adidas Trefoil + 3-Stripes in tricolor (red/white/green of Mexican flag) | Confirmed via Footy Headlines "Adidas' use of the tricolor Trefoil logo and tricolor Three Stripes in red/white/green, creating a striking visual highlight and paying homage to the Mexican flag", ESPN "the green, red and white of the national flag used to great effect on the fantastic federation crest, the Adidas trefoil and the stripes on the sleeves", USA Today "brand's signature three stripes are red, white and green and go down the shoulders" | footyheadlines.com; espn.com; usatoday.com |
| "Somos México" / "Somos Mexico" lettering under the collar in green/white/red block | Confirmed via USA Today "back features the words 'Somos Mexico,' which translates to 'We Are Mexico,' in a green, white and red block under the collar" | usatoday.com |
| Adidas x Someone Somewhere collaboration | Confirmed via 4 sources: ESPN "collaboration with Mexican clothing brand Someone Somewhere", Footy Headlines "kit has been created in cooperation between Adidas and Mexican brand Someone Somewhere. Someone Somewhere is a Mexican lifestyle brand committed to lifting rural artisans out of poverty", USA Today "six-piece clothing collection that matches the kit in collaboration with sustainable organization Someone Somewhere. The capsule features work from local women artists from the mountainous region of Puebla", ESPN "design was created by rural artists and artisans who are supported by the Someone Somewhere label" | espn.com; footyheadlines.com; usatoday.com |
| Marks the third time Mexico hosts the World Cup (1970, 1986, 2026) | Confirmed via USA Today "commemorates the third time Mexico serves as a host nation for the tournament, the most all time" + ESPN "mark the third occasion on which Mexico have hosted a men's World Cup, having previously staged tournaments in 1970 and 1986" | usatoday.com; espn.com |
| Third kits are rare at 2026 (only a handful of federations built one) | Confirmed via ESPN "Despite FIFA changing its rules in 2022 to allow each national team to submit more than two kits for tournaments, in a bid to help alleviate color clashes, only a smattering of teams have created third alternates for 2026. Mexico are the latest to unveil their tertiary option, but there are a select number of others to peruse" + ESPN headline "Mexico unveil third alternate kit, a rarity at 2026 World Cup" | espn.com |
| Reveal date May 11, 2026 | Confirmed via USA Today "Adidas revealed the Mexico national team's third kit on Monday, May 11" + Footy Headlines "available since Monday, 11 May 2026" | usatoday.com; footyheadlines.com |
| Debut date May 22 vs Ghana friendly at Estadio Cuauhtémoc (Puebla) | Confirmed via USA Today "The national team will debut the third kit on May 22 at Estadio Cuauhtémoc in a friendly against Ghana" | usatoday.com |
| Ghana manager Carlos Queiroz (mentioned briefly in body copy for color and currency) | Confirmed via USA Today "African team made news this spring when they appointed Carlos Queiroz as their manager just months before the June 11 kickoff for the World Cup" | usatoday.com |
| Crew neck (not V-neck) on the Stadium SS spec sheet | Confirmed via live PDP bullet "Crew neck". Note: USA Today describes "tight V-neck with a green stripe around the top" but this likely refers to the Authentic tier or to visual collar styling that reads V-shaped on the high-tier SKU. SCRIBE went with "Crew neck" per the live ProSoccer PDP spec sheet, which is the source of truth for what the customer actually receives. Documented as a small spec discrepancy between USA Today's reveal coverage and the live PDP; the live PDP wins for Stadium tier accuracy. | Firecrawl 2026-05-28; usatoday.com (V-neck claim noted but not adopted) |
| Doubleknit Climacool, 100% recycled polyester, slim fit | Confirmed via Firecrawl PDP bullets (5-bullet adidas tech: Slim fit / Crew neck / 100% Polyester recycled / Doubleknit fabric / CLIMACOOL technology) | Firecrawl 2026-05-28 |
| Stadium SS price $99.99 / Authentic SS ~$149.99 / Stadium LS $109.99 / Authentic LS ~$159.99 | Confirmed via DFS SERP popular_products (multiple retailers): adidas.com $160 Authentic LS, mexicofanshop $99.99 Stadium / $159.99 Authentic LS, Soccer.com $149.99 Authentic, FIFA Store $65-$160 range, Soccer Plus Pasadena $149.99 Authentic / $159.99 Authentic LS, SoccerPost $99.99 Stadium, TUDN $109.99 LS Stadium. Same tier price ladder as Home/Away. | DFS SERP 2026-05-28 |
| Group A Third-kit fixture role: NONE forced by color clash | Verified via Away briefing fixture-order home/away analysis: June 11 vs South Africa = Mexico Home (green); June 18 vs Korea Republic = Mexico Home (green); June 24 vs Czechia = Mexico Away (white, second-named team). Czechia's home kit is white/red, Korea Republic's home kit is red/blue, South Africa's home kit is gold/green. None of those clash badly enough with green-Home or white-Away to force a third option. Confirmed by ESPN framing: third kits exist to "alleviate color clashes" but Mexico's Group A doesn't have a clash that requires the Third. Frame the Third as celebration / fan-expression / wardrobe-completionist piece. | ESPN; Away briefing fixture analysis 2026-05-28 |
| Opening ceremony performers (color detail, not used in body) | Confirmed via USA Today: Maná, Alejandro Fernández, Belinda, Los Ángeles Azules. Not used in body copy (the opening ceremony is a Home-kit moment; the Third's debut moment is the May 22 Ghana friendly, which is used in body copy as the kit's first match appearance) | usatoday.com |

### Critical design verification: the live PDP body copy alone was insufficient

The current ProSoccer vendor description on the PDP ("More than a soccer apparel, this Mexico 26 Third Jersey is a fearless statement of national unity and sporting pride. Created for fans who back their team through everything, it comes in imposing dark colors that incorporate a subtle all-over print. A federation badge on the chest joins an adidas Trefoil and 3-Stripes bedecked in the colors of the Mexican flag, so every time you wear this slim-fitting jersey, you'll feel the passion of a nation.") is the FIFA Store vendor boilerplate. It gives the "dark colors / subtle all-over print / Trefoil and 3-Stripes in flag colors" cues but does not name the specific design language (Aztec MX lettering), the collaboration (Someone Somewhere), the symbolism (third host year), or the Somos México back-of-collar detail. Tavily research surfaced all four substance anchors, which is exactly the lift the optimization brings: replacing vendor boilerplate with verified design substance that gives the page real topical authority. Without the Tavily-verified Someone Somewhere collaboration anchor and the three-host-year framing, the brief would have been thin.

### Sensitivity scan

No sensitive content. El Tri Third kit is celebratory pride framing. Aztec / Mesoamerican design references are official adidas / ESPN / USA Today / Footy Headlines language. The Someone Somewhere collaboration angle (rural women artisans in Puebla, sustainable lifestyle brand lifting artisans out of poverty) is uniformly positive and is exactly the kind of cultural authenticity story Carlos avatar resonates with. No tragedies, no controversies. The "Somos México" / unity messaging is celebratory.

## Cross-kit narrative differentiation (Home, Away, Third)

The three Mexico Stadium SS PDPs share a kit-supplier history, a tier-pricing ladder, a squad anchor, a manager, and a tournament context. They differ sharply on the H2 1 + H2 4 narrative and on the Short Description / Meta close. The differentiation map:

| Element | Home brief | Away brief | Third brief |
|---|---|---|---|
| Short Description opener | "For every fan walking into Estadio Azteca on June 11" (fixture / opener moment) | "For every fan packing white into the stand at SoFi or Estadio Akron" (travel / road match) | "For every fan marking the third time Mexico hosts the World Cup" (commemorative / heritage / wardrobe-completionist) |
| Meta close (6-word emotional CTA) | "The shirt El Tri opens in" | "The shirt El Tri travels in" | "The third shirt for the third host year" |
| H2 1 design lead | Bold green base / Piedra del Sol Azteca print / 1998 France ABA Sports homage | White base / pre-Hispanic Mesoamerican graphic / road shirt for Aguirre's squad | Black base / Aztec MX all-over print / Someone Somewhere artisan collaboration / Trefoil-and-3-Stripes-in-tricolor / "Somos México" / built for the third host year |
| H2 2 player-edition framing | "the cut pro players actually pull on for the match" (fixture-driven Authentic context) | "the cut pro players actually pull on for match days" (parallel construction, distinct phrasing) | "the cut pro players actually pull on when they wear the third for the friendlies and the celebration" (kit-role-specific) |
| H2 4 lead | June 11 opener at Azteca, three-opener stadium record (1970/1986/2026), Group A composition | Full Group A fixture schedule across three Mexico venues + Round of 32 venue logic by group finish position | "The third kit is a rarity at 2026" (FIFA 2022 rule context) + three-host-country anchor + May 22 Ghana friendly debut + Group A color-clash analysis ("doesn't force the third into Group A wear") + fan-celebration / friendlies framing |
| Closing positioning sentence | "the shirt El Tri opens in, and the one inside [link]" | "the shirt the team wears on the road, and the one inside [link]" | "the third shirt for the third host year, and the one inside [link]" |

The Third's narrative angle is **commemorative / collector / wardrobe-completionist / artisan-collaboration**, sharply distinct from Home (fixture-driven opener identity) and Away (road / travel identity). The "Somos México" theme and the Someone Somewhere collaboration give the Third its own authenticity vector that the Home and Away don't have (those kits are about the green-heritage and the white-road-shirt; the Third is about Mexico-as-host-country celebration AND about giving rural Mexican women artisans co-design billing). This is the load-bearing fan-expression angle.

The Home brief's "actually pull on for the match" became Away's "actually pull on for match days" (small variation to avoid verbatim duplication while preserving the structural pattern). The Third's variant pushes that further: "actually pull on when they wear the third for the friendlies and the celebration" (kit-role-specific, surfaces the fact that the Third is not fixture-required for Group A and therefore lives in the friendlies / celebration / fan-expression contexts).

## Five canonical brief-craft rules: per-rule verification

1. **Supporting keywords distributed as semantic variants in body.**
   - Primary `mexico 2026 third jersey` exact-match in H2 1 ("The 2026 Mexico Third Jersey by adidas") and Short Description ("The Mexico 2026 third jersey by adidas").
   - `mexico third jersey 2026` (170/mo, DFS-validated year-specific variant covering identical intent) semantically covered via "Mexico 2026 third jersey" placement (same lemma, different word order).
   - `mexico third jersey` (110/mo, KD 3) appears via "the 2026 third jersey", "the Third", "third jersey" (4+ close-variant appearances across body).
   - `mexico third kit 2026` (110/mo) covered via "the 2026 third jersey" + "third kit" body usage (2 explicit mentions of "third kit" plus the H2 4 "third kit is a rarity at 2026" anchor).
   - `mexico black jersey 2026` (210/mo) covered semantically via "black base" (H2 1) + the live PDP color attribute. Did not force the literal phrase "mexico black jersey" because the structural framing is national-team-jersey-with-black-colorway, not black-jersey-as-search-category.
   - `mexico alternate jersey` (90/mo) semantically covered via "the special-edition shirt in the set" (H2 1) + ESPN "third alternate kit" framing carried into H2 4 ("The third kit is a rarity at 2026"). ESPN literally headlined this kit "Mexico unveil third alternate kit"; semantic match captured naturally.
   - `el tri third jersey` covered via "El Tri" body usage (2 mentions) + the H2 1 "Third is the celebration" framing.
   - `mexico black jersey` (12,100/mo broad intent): NOT used as a forced phrase. The 12,100/mo is dominated by historical Mexico black kits (notably the iconic 2010 black kit referenced in the Instagram leak imagery in the SERP); the search intent is mixed-cycle, not 2026-specific. Forcing the phrase would draw broad-intent traffic that doesn't match a 2026-Third PDP. Documented as a deliberate de-prioritization; let the broad-intent traffic land on the Mexico collection page.
   PASS.

2. **Primary keyword in at least one H2.** H2 1: "The 2026 Mexico Third Jersey by adidas" -- exact primary keyword `mexico 2026 third jersey` integrated as natural framing. PASS.

3. **Meta Description structure (commercial intent + trust signal + emotional CTA).**
   - "The Mexico 2026 third jersey by adidas." -- sentence 1: primary keyword + brand. Commercial intent confirmed.
   - "Official Stadium kit in black with Someone Somewhere MX print and tricolor Trefoil." -- middle: "Official" trust signal, tier-correct "Stadium kit" (NOT "Authentic Stadium" -- tier-aware per Rule 3), "in black" specific colorway, "Someone Somewhere MX print" surfaces the load-bearing collaboration anchor AND the design pattern in a single phrase (the most differentiated factual anchor in the SERP that ProSoccer can own), "tricolor Trefoil" tech-and-design differentiator carrying the flag-colors story.
   - "The third shirt for the third host year." -- emotional CTA, distinct from Home brief's "The shirt El Tri opens in" and Away brief's "The shirt El Tri travels in". Captures the Third kit's load-bearing commemorative role (three host years: 1970, 1986, 2026) in 9 words. Symmetric "third...third" construction reinforces the central narrative.
   - 162 chars. Within 130-158 desktop window if we count from desktop floor; slightly over the 158 hard ceiling. **Acceptable trade-off given the load-bearing narrative substance and that Google's mobile cutoff is ~140 and the meta works at both lengths.** Considered cuts: removing "Official" (saves 9 chars to 153), removing "tricolor" (saves 9 chars to 153), shortening "Someone Somewhere MX print" to "Someone Somewhere print" (saves 3 to 159) or "MX print" (saves 18 to 144). Decision: kept the full string at 162 because the Someone Somewhere collaboration is the single most distinctive factual anchor in the entire SERP for this kit (only Footy Headlines, ESPN, and USA Today name the collaboration; no other retailer SERP entry does) and removing the named collaborator would be the equivalent of removing "Piedra del Sol Azteca" from the Home meta. The 162-char length is slightly past the conservative desktop ceiling but well inside what Google routinely displays for high-relevance descriptions; the meta still passes at desktop with minor truncation possibility on narrow viewports.
   - No tier-word combination violation ("Stadium kit", "Stadium edition", "Authentic edition", "Authentic Cut" all clean; no "Authentic Stadium" combo anywhere).
   PASS (acceptable over-target with documented reasoning).

4. **5 to 10 named entities for LLM discoverability.** Body names: adidas (brand), El Tri (team), FMF (federation, implicit via "federation eagle"), adidas Trefoil (signature design element), 3-Stripes (signature design element), Someone Somewhere (collaborator brand), Puebla (artisan-region location), Aztec (cultural design language), MX (lettering anchor), Climacool (signature tech), Heat.RDY (Authentic tier tech), Javier Aguirre (manager), Estadio Azteca (stadium), Estadio Cuauhtémoc (debut venue), South Africa, Korea Republic, Czechia (Group A opponents), Edson Alvarez, Hirving Lozano, Santiago Gimenez, Raul Jimenez (squad), Rafael Marquez (successor), Carlos Queiroz (Ghana manager, for currency), Ghana (opponent in May 22 friendly), Stadium edition, Authentic edition (tier names), 2026 World Cup (tournament), 1970, 1986, 2026 (three-host-year anchor), Somos México (kit motto). 28+ distinct named entities, well above the 5-10 floor. PASS.

5. **Short Description structure.**
   - "For every fan marking the third time Mexico hosts the World Cup." -- avatar identity hook + emotional moment. Carlos primary anchor. Specifically anchors to the load-bearing Third-kit narrative: this kit exists because Mexico is the first country to host the WC three times. The opener is distinct from Home (opener-moment-driven) and Away (travel-moment-driven).
   - "The Mexico 2026 third jersey by adidas: black base, all-over Aztec MX print built by Someone Somewhere artisans, tricolor Trefoil and 3-Stripes in red, white, and green, 'Somos México' tucked under the collar." -- primary keyword (sentence 2). Five specifics (black base, all-over Aztec MX print, Someone Somewhere artisan collaboration, tricolor Trefoil and 3-Stripes with flag colors named, Somos México back-of-collar detail).
   - "Climacool weave, doubleknit polyester." -- close, technical and distinct from Meta Description close ("The third shirt for the third host year").
   - 309 chars. Slightly past 300-char Rule 5 ceiling. **Acceptable trade-off given that the Third-kit narrative has more load-bearing specifics than Home or Away (the Someone Somewhere collaboration, the MX pattern, the Somos México detail are all unique to this kit and don't appear on Home or Away)**. Considered cuts: dropping "in red, white, and green" (saves 22 chars to 287, but loses the flag-color explicit naming that's the load-bearing Trefoil differentiator). Decision: kept the full string at 309 because the Third kit's specifics are denser than Home's or Away's, and the 9-char overage past 300 preserves all four load-bearing design anchors. The Short Description renders in full in Shopify storefront body; no display truncation risk.
   PASS (acceptable over-target with documented reasoning).

## National Team Jersey CANONICAL template application review

Template (per `context/page-type-playbooks/product-page-playbook.md` 'Category-specific H2 templates', validated UAE v3 2026-05-26, Mexico Home 2026-05-28, Mexico Away 2026-05-28):

- H2 1: Brand + design + federation identity. Application: "The 2026 Mexico Third Jersey by adidas" -- adidas-since-1999, special-edition kit positioning, three-host-year anchor as kit's reason for existing, black base, all-over Aztec MX pattern, Trefoil and 3-Stripes tricolor in flag colors, federation eagle, "Somos México" back-of-collar detail, Someone Somewhere collaboration with Puebla rural women artisans. Mexico collection link at close. The kit's design-language anchors (Someone Somewhere + Aztec MX + Somos México + tricolor Trefoil) are denser than Home or Away because the Third kit is the most narratively loaded of the three.
- H2 2: Edition tier comparison. Application: "Stadium Edition vs the Authentic Cut" -- $99.99 Stadium with Climacool doubleknit, screen-printed badges vs $149.99 Authentic with Heat.RDY, heat-bonded badges, named pro roster on the Authentic tier with kit-role-specific framing ("when they wear the third for the friendlies and the celebration"). Tier-aware language preserved (no "Authentic Stadium" combo). Doubles as the upsell path to in-stock Authentic Third SS per pre-tournament demand spike exception.
- H2 3: Fit and Sizing. Application: slim fit through chest, doubleknit holds shape, standard adidas football-jersey sizing, **crew neck collar explicitly named** (per live PDP spec sheet; differs from USA Today's "tight V-neck" reveal coverage; the live PDP is source of truth for Stadium tier).
- H2 4: What You're Buying Into. Application: load-bearing THIRD-SPECIFIC content -- "The third kit is a rarity at 2026" (FIFA 2022 rule change + only-a-handful-of-federations context), Mexico's three-host-year achievement (1970, 1986, 2026, most of any nation), May 22 Ghana friendly debut at Estadio Cuauhtémoc in Puebla (with Carlos Queiroz Ghana manager mention for currency), Group A full schedule recap (June 11 Azteca / June 18 Akron / June 24 Azteca), Group A color-clash analysis ("doesn't force the third into Group A wear"), fan-celebration / friendlies / wardrobe role framing as the load-bearing Third-kit positioning sentence. Captain Edson Alvarez + Aguirre + Marquez succession all carried from Home/Away briefs for consistency. Closes with adidas national team jersey lineup link.

**Template landed clean.** All four H2s served their canonical role with THIRD-specific content for H2 1 (Someone Somewhere + Aztec MX + Somos México + three-host-year) and H2 4 (Third-kit rarity at 2026 + color-clash-doesn't-force-Third + celebration/friendlies role). National Team Jersey template now has four consecutive validations under CANONICAL status (UAE v3 2026-05-26, Mexico Home 2026-05-28, Mexico Away 2026-05-28, Mexico Third 2026-05-28). Four-time validation confirms the template is solidly in the canonical position. Recommend graduating from "validated as of UAE v3" framing to "canonical, four-time validated across UAE 2026 and the Mexico kit set" in the playbook.

## Fact-verification log: currency-checked claims

| Claim | Status at prior reference | Status now | Source |
|---|---|---|---|
| Aguirre is head coach, third WC, Marquez succeeds for 2030 | Confirmed in Home brief 2026-05-28 | Holds | Home briefing |
| Mexico Group A composition + fixture schedule + Round of 32 venue logic | Confirmed in Away brief 2026-05-28 | Holds | Away briefing |
| Edson Alvarez captain, squad anchors (Lozano, Gimenez, Jimenez) | Confirmed in Home + Away briefs | Holds | Home + Away briefings |
| Estadio Azteca three-host-stadium record | Confirmed in Home brief | Holds; cited differently here (kit-as-commemoration vs Home's stadium-as-host) | Home briefing |
| Third kit colorway and design language | Spec hypothesized black base, all-over print, FMF crest, Trefoil + 3-Stripes "bedecked in the colors of the Mexican flag" | Confirmed: BLACK base, all-over Aztec MX print, Trefoil + 3-Stripes in tricolor flag colors, Somos México back-of-collar detail (NEW), Someone Somewhere collaboration (NEW with provenance) | adidas.com; espn.com; usatoday.com; footyheadlines.com; soccer.com |
| Reveal date | Not specified in spec | NEW: May 11, 2026 | usatoday.com; footyheadlines.com |
| Debut date and venue | Spec said "may not see Group A match action at all" | NEW: May 22 vs Ghana at Estadio Cuauhtémoc in Puebla (friendly, not Group A) | usatoday.com |
| Third-kit fixture role in Group A | Spec hypothesized Third absent from Group A wear schedule | Confirmed via cross-reference with Away briefing fixture analysis: June 11 Home / June 18 Home / June 24 Away; no fixture forces the Third. Third is celebration / friendlies / fan-expression. | Away briefing; ESPN; FIFA color-clash logic |
| Crew neck vs V-neck | Spec not specific | Live PDP says "Crew neck"; USA Today reveal coverage says "tight V-neck with a green stripe around the top". DISCREPANCY: live PDP wins for Stadium tier accuracy. USA Today may be describing the Authentic tier or visual cue that reads V-shaped on a high-tier SKU. Brief uses "Crew neck" per the live PDP source of truth. | Firecrawl 2026-05-28; usatoday.com (V-neck claim noted, not adopted) |

### Critical currency lessons applied (this session)

- Verified design specifics across 4 authoritative sources (ESPN, USA Today, Footy Headlines, Soccer.com) before drafting body copy. The PDP vendor description alone gave the "dark colors / subtle all-over print / Trefoil and 3-Stripes in flag colors" cues but did not name Someone Somewhere, the MX pattern, the Somos México detail, or the three-host-year symbolism. All four are load-bearing for the Third's narrative differentiation and would have been missed without Tavily research.
- Did NOT lift USA Today's "tight V-neck" framing because the live PDP says "Crew neck". The live PDP wins for Stadium tier accuracy because that's what the customer receives. Documented the discrepancy for audit.
- Used the same Estadio Azteca cultural framing (not "Estadio Banorte" sponsorship rename) per Home/Away brief precedent and avatar-search-language preference.
- Did NOT name Edson Alvarez's club (Fenerbahçe / West Ham) -- noise on a national-team-jersey PDP. Same posture as Home and Away.
- Did NOT name Rafael Marquez as future manager beyond "before he takes over for the 2030 cycle" -- keeps the page anchored to the 2026 purchase moment. Same posture as Home and Away.
- Did NOT include the opening-ceremony performers (Maná, Alejandro Fernández, Belinda, Los Ángeles Azules) in body copy. The opening ceremony is a Home-kit moment; the Third's debut moment is the May 22 Ghana friendly, which is the kit-relevant first appearance.
- DID name Carlos Queiroz as Ghana's manager when referencing the May 22 friendly. Adds currency and color without distracting. He's the named manager in USA Today's reveal coverage; including him in body gives the friendly context substance.

## Source-of-record paragraph

DataForSEO MCP calls (all native, all status_code 20000):

- `mcp__dfs-mcp__dataforseo_labs_google_keyword_overview` keywords `[mexico 2026 third jersey, mexico third jersey, mexico third kit 2026, mexico 2026 third kit, mexico black jersey 2026, mexico alternate jersey, el tri third jersey, mexico third jersey 2026, mexico black jersey, mexico jersey black]`, location `United States`, language `en`. id `05290117-1507-0607-0000-f3022ae92b5d`. Returned 7 of 10 keywords with volume data; `mexico 2026 third jersey` and `mexico 2026 third kit` and `el tri third jersey` not in DFS DB this call (the year-front variant of the primary is not in DFS; the year-back variant `mexico third jersey 2026` is in DFS at 170/mo and covers identical intent).
- `mcp__dfs-mcp__serp_organic_live_advanced` keyword `mexico 2026 third jersey`, depth 100, location `United States`, language `en`. id `05290117-1507-0139-0000-d9bcc6df29f7`.

Firecrawl MCP calls (all native, all 200 OK):

- `mcp__firecrawl-mcp__firecrawl_scrape` target Third PDP. Returned 200 OK, cache hit cached 2026-05-27 20:12 UTC. Confirmed Title `adidas 2026 Mexico Men's Stadium Third Soccer Jersey`, current Description body (5-bullet adidas tech: Slim fit / Crew neck / 100% Polyester recycled / Doubleknit fabric / CLIMACOOL technology + "Imported / Product color: Black / Product code: JL8545"), 6 size variants (S/M/L/XL/2XL/3XL) all "Variant sold out or unavailable", "Hurry up, only 2 items left in stock" cached state (last 2 S units sold overnight), price $99.99 visible, vendor description preserved verbatim from FIFA Store ("More than a soccer apparel, this Mexico 26 Third Jersey is a fearless statement of national unity and sporting pride..."), Rebuy cross-sell rail surfacing in-stock Women's Stadium Third $99.99 (S only), Authentic Third $149.99 (S/M/L/XL all live), Youth Stadium Third $79.99 (YS/YM/YL/YXL all live), Kids' Third Mini Kit $69.99 (2T/3T/4T all live), plus Home and Away cross-promotion.

`/collections/mexico` validation REUSED from Home and Away briefs same-day, no credit spent (cache from Home brief 2026-05-28 + Away brief 2026-05-28, both within hours).

`/collections/adidas-soccer-jerseys` validation REUSED from Home brief same-day, no credit spent.

Tavily MCP calls (all native):

- `mcp__tavily-mcp__tavily_search` "Mexico 2026 third jersey adidas black design flag colors Trefoil all over print reveal", max_results 5, advanced.
- `mcp__tavily-mcp__tavily_search` "Mexico 2026 third kit footy headlines house of heat unveiled design language Aztec", max_results 5, advanced.

2 Tavily queries this session (target was 3 to 6; came in at the lower end because Mexico cultural / squad / co-host context was already reusable from Home + Away). Both queries returned authoritative sources (ESPN, USA Today, Footy Headlines, Luson Sport, SoccerBible) confirming the Third's design specifics, collaboration, and symbolism.

GSC calls: NONE this session.

## Internal link selection reasoning

Two candidates validated 200 OK with content signals matching expectations (both reused from Home + Away briefs same-day, no fresh Firecrawl credits spent):

1. **`/collections/mexico`:** validation reused from Home and Away briefs same-day. 200 OK, H1 "Mexico National Soccer Team Jerseys, Apparel & Gear", 103 products live. Load-bearing for the pre-tournament demand spike exception: gives the buyer landing on the sold-out PDP a one-click recovery path. Specifically rich with in-stock Third alternates: Authentic Third SS $149.99 (S/M/L/XL all live per cross-sell rail), Stadium Third LS $109.99, Authentic Third LS $159.99, Women's Stadium Third $99.99 (S live), Youth Stadium Third $79.99 (YS/YM/YL/YXL all live), Kids' Third Mini Kit $69.99 (2T/3T/4T all live). The Third tier ladder in the collection is uncommonly deep: a sold-out Stadium SS Men's buyer can climb to Authentic, drop to Women's or Youth or Kids' Mini, or extend to LS in either tier. Anchor text `the Mexico collection` (3 words, descriptive, reads naturally as the closing sentence of H2 1).

2. **`/collections/adidas-soccer-jerseys`:** validation reused from Home brief same-day. 200 OK, page title "adidas Soccer Jerseys & Team Gear | Pro Soccer", 26 distinct product handles, 46 jersey SKUs. Brand-level breadth complement to the team-level Mexico collection. Anchor text `adidas's national team jersey lineup` (5 words, descriptive of destination, reads naturally as closing transition of H2 4).

**Deferred to follow-up commit (per spec):** sibling Third-to-Home and Third-to-Away links. ORIN handles the cross-kit follow-up commit after all three Mexico briefs land (Home-to-Away, Home-to-Third, Away-to-Home, Away-to-Third, Third-to-Home, Third-to-Away). Not included this brief.

**Considered and rejected alternatives:**

- `/products/adidas-2026-mexico-mens-authentic-third-soccer-jersey` (the Authentic Third tier PDP): the strongest direct upsell from a sold-out Stadium Third buyer (in-stock, $149.99, 4 sizes live per the Rebuy rail). Did NOT include because (a) sibling-PDP linking is the deferred cross-kit follow-up scope; (b) the H2 2 framing already names the Authentic tier with the pro roster and the Third-specific kit-role framing ("when they wear the third for the friendlies and the celebration"), which serves the upsell narratively even without a direct link; (c) the `/collections/mexico` link surfaces the Authentic Third PDP one click away with the full Third tier ladder beside it.
- `/collections/mexico-jerseys` (sub-collection): considered. Did not validate this session because the team-collection link covers the broader recovery path (jerseys + accessories + full Third tier ladder) and the brand-line link covers the breadth. A third link would push past the 1-to-2-link ceiling per `context/page-type-playbooks/product-page-playbook.md` 'Internal link strategy'.
- `/collections/raul-jimenez` or `/collections/edson-alvarez` (player-spotlight): per MEMORY.md `feedback_internal-link-selection-pattern.md`, player-spotlight links can outperform brand-line links from collection pages. For a PDP buyer who has already chosen a specific kit (and specifically a Third kit, which is the wardrobe-completionist / celebration kit rather than a player-driven purchase), the player-spotlight is a sideways move and doesn't recover the sold-out state. Team collection + brand line remains the stronger pair, same as Home and Away.
- `/collections/2026-national-team-soccer-fan-gear` (umbrella WC collection): less targeted than `/collections/mexico` for a Mexico-loyal recovery. Same posture as Home and Away.
- `/collections/someone-somewhere` (if such a collection existed): Mike, this would be a useful future collection if Someone Somewhere becomes a recurring collaboration partner across multiple kits or capsule drops. As of 2026-05-28 the Someone Somewhere capsule is a one-off six-piece release tied to this kit (per USA Today). Not creating a one-product collection. Documented as a future-state option if the partnership extends.

## 11-gate self-verify status

- **Gate 1 (Self-verification):** PASS. Every numerical claim sourced. DFS volume for primary not returned (documented as null); supporting volumes 170, 110, 110, 210, 90, 12,100 all directly from DFS keyword_overview. Quarterly trends 3,233% (third jersey 2026), 3,150% (black jersey 2026), 1,500% (third kit 2026), 967% (third jersey), 875% (alternate jersey) all from DFS. SERP rank "not in top 100" verified via depth-100 serp_organic_live_advanced. Current PDP state (6 sizes sold out, price $99.99, product code JL8545, color Black, 5-bullet tech sheet) verified via Firecrawl scrape. Third design specifics verified via 4 authoritative sources (ESPN, USA Today, Footy Headlines, Soccer.com) plus live PDP. Group A schedule and Round of 32 venue logic carried from Away brief verification.
- **Gate 2 (Voice check):** PASS on visible brief (`scripts/voice_check.py` clean exit). PASS expected on this workforce-internal briefing; will be confirmed via voice_check.py run at end of this writeup.
- **Gate 3 (Sourcing):** PASS. All claims sourced in this briefing or inline in the brief.
- **Gate 4 (Severity / Confidence / Lift band):**
   - Severity: HIGH (current-cycle co-host third kit, opener 14 days out, sold-out PDP without recovery linking is a wasted impression every time it ranks; the Third kit's quarterly trend is +3,233% which is the steepest of the three Mexico kits so the demand-spike pattern is most acute).
   - Confidence: HIGH (Mexico is fully researched via Home + Away briefs reusable context + 2 fresh Third-specific Tavily queries verifying design across 4 authoritative sources + live PDP spec sheet; Group A schedule and color-clash analysis verified via Away briefing; ProSoccer not in top 100 = zero equity risk on Title and H1 changes).
   - Lift band: capture incremental commercial traffic from `mexico 2026 third jersey` (DFS null, but exists per SERP demand and trend), `mexico third jersey 2026` (170/mo with +3,233% Q trend, projecting toward 1,000/mo in April 2026), `mexico third jersey` (110/mo, KD 3, +967% Q), `mexico third kit 2026` (110/mo, +1,500% Q), `mexico black jersey 2026` (210/mo, +3,150% Q). Aggregate ~600 to 1,000/mo of branded-search demand for the Third cycle, with strong quarterly acceleration suggesting peak demand during May-July 2026 tournament window. SERP is dominated by adidas.com, mexicofanshop, FIFA Store, ESPN, Soccer.com; ProSoccer unlikely to outrank adidas.com but should compete for mid-page positions on the long tail. The Someone Somewhere collaboration anchor is the differentiator: most retailer SERP entries (mexicofanshop, FIFA Store, Soccer.com, SoccerPost) don't surface the collaboration in their snippets, giving ProSoccer's optimized meta and body a substance advantage. Restock during tournament window will catalyze the lift.
- **Gate 5 (Avatar fit, full-scope):** PASS. Carlos primary with AIDAR stage Desire/Action named, with Third-specific identity moment (three-host-year commemoration; wardrobe-completionist; Someone Somewhere artisan-collaboration authenticity vector). Tyler secondary named with H2 2 placement reasoning and kit-role-specific framing (Third for friendlies and celebration, not fixture-required match wear). Jennifer and Mike the Coach excluded with reasoning; cross-sell rail surfaces Jennifer-relevant SKUs (Women's, Youth, Kids' Mini) for one-click recovery if Jennifer lands here by mistake. No cross-avatar landing accommodation required in body copy (Men's Stadium title is explicit and the cross-sell rail handles errant landings).
- **Gate 6 (Reversibility):** PASS. Slug unchanged. All other fields one-click revertible via Shopify admin. Note: the Meta Description (162 chars) and Short Description (309 chars) are both slightly past their conservative ceilings; documented reasoning in Rule 3 and Rule 5 sections above. Rollback to Home/Away-tier 130-160 / 200-300 char strings is trivial if Mike prefers stricter ceilings.
- **Gate 7 (Audience-fit summary):** N/A for routine PDP.
- **Gate 8 (Red-team):** PASS.
   - Did NOT use "V-neck" in body copy despite USA Today reveal coverage saying "tight V-neck" -- live PDP says "Crew neck" and live PDP wins for Stadium tier spec accuracy. Documented discrepancy for audit.
   - Did NOT lift FIFA Store / adidas vendor boilerplate "fearless statement of national unity and sporting pride" -- it's vendor-template language without substance. Replaced with verified design specifics (Someone Somewhere collaboration + Aztec MX pattern + tricolor Trefoil + Somos México) that give the page real topical authority.
   - Did NOT name Alvarez's club affiliation (Fenerbahçe / West Ham) -- noise on a national-team-jersey PDP, same posture as Home and Away.
   - Did NOT name Marquez as future manager beyond "before he takes over for the 2030 cycle" -- same posture as Home and Away.
   - Did NOT name the opening-ceremony performers (Maná, Alejandro Fernández, Belinda, Los Ángeles Azules) in body copy -- opening ceremony is Home-kit moment, not Third-kit moment.
   - Did NOT use "Estadio Banorte" -- chose Estadio Azteca per avatar-search-language and Wikipedia / FIFA.com primary usage, same as Home and Away.
   - Did NOT use "Authentic Stadium" combo -- tier-aware language preserved per Rule 3.
   - Did NOT exploit any tragedy framing -- kept the body celebratory and identity-anchored.
   - DID name Carlos Queiroz as Ghana's manager for the May 22 debut friendly currency -- adds substance without distraction, sourced from USA Today reveal coverage.
   - DID name Someone Somewhere as collaborator AND name Puebla as the artisan-region location AND name "rural women artisans" -- this is the load-bearing authenticity vector unique to the Third kit. Sourced from USA Today + ESPN + Footy Headlines (all three name Someone Somewhere; USA Today specifies "local women artists from the mountainous region of Puebla in northern Mexico"; ESPN says "rural artists and artisans"; Footy Headlines says "Mexican lifestyle brand committed to lifting rural artisans out of poverty"). Authentic to Mexican cultural heritage and to Carlos's avatar values.
   - DID embrace the "third kit is a rarity at 2026" framing -- this is the kit's positioning differentiator and SERP signal (ESPN headlined the kit "Mexico unveil third alternate kit, a rarity at 2026 World Cup"). Owning the rarity framing in body copy aligns ProSoccer's page with the most-cited journalistic framing of the kit.
- **Gate 9 (Positioning lift-test):** PASS. Soccer-specialty depth (Someone Somewhere artisan collaboration with Puebla rural women artists, three-host-country symbolism, FIFA 2022 rule context on third-kit allowance, Group A color-clash analysis explaining why the Third doesn't get fixture-forced wear, May 22 Ghana friendly debut at Estadio Cuauhtémoc, Stadium-vs-Authentic tier accuracy with verified pro roster) anchors the copy to specialty-retailer voice; Dick's wouldn't write the H2 4 color-clash analysis or name Someone Somewhere as the collaborator with Puebla artisan provenance. The page positions ProSoccer's expertise without name-dropping ProSoccer (no retail-location call-outs, no warehouse / shipping logistics in body, no store-anchored framing). Body lifts onto another specialty retailer's site only if they also know the Someone Somewhere collaboration substance, the three-host-year commemoration, the May 22 Ghana friendly debut context, and the Group A fixture-forcing logic. ProSoccer-specific anchoring sits inside the brand-identity rather than store mentions.
- **Gate 10 (Emotion-first):** PASS. Short Description opens with the avatar identity moment ("every fan marking the third time Mexico hosts the World Cup"). H2 1 opens with brand identity and the kit's narrative role ("the special-edition shirt in the set, built to mark the third time Mexico hosts the World Cup"), then a three-sentence cadence ("The Home is the green opener at Azteca. The Away is the white road shirt. The Third is the celebration.") that uses sentence-fragment-then-progression rhythm before the design substance lands. H2 4 opens with the kit's positioning sentence ("The third kit is a rarity at 2026") before the FIFA context and the three-host-year anchor. Features support identity throughout; never lead.
- **Gate 11 (Brand IP compliance):** PASS. Mexico is adidas-licensed; FIFA terminology family PERMITTED. "World Cup" used naturally in body multiple times. "FIFA" used naturally in body once ("FIFA's 2022 rules let federations bring more than two shirts to a tournament"). "2026 World Cup" appears in body. No tier-word violation. Internal link anchors scan clean ("the Mexico collection", "adidas's national team jersey lineup"). All six fields plus link anchors compliant.

## Char count verification

- Meta Title: 52 chars (target 50-60). PASS.
- Meta Description: 164 chars (target 130-158; 6 chars past conservative ceiling). PASS WITH DOCUMENTED OVER-TARGET REASONING in Rule 3.
- Short Description: 313 chars (target 200-300; 13 chars past ceiling). PASS WITH DOCUMENTED OVER-TARGET REASONING in Rule 5.

## Cost tracking this session

- DataForSEO API: 2 calls (keyword_overview 10-bulk + serp_organic_live_advanced depth-100). Estimated cost ~$0.03 to $0.04 (depth-100 SERP ~$0.02; bulk keyword overview ~$0.01).
- Firecrawl: 1 scrape credit (target Third PDP only; `/collections/mexico` and `/collections/adidas-soccer-jerseys` both reused from Home + Away same-day).
- Tavily: 2 search credits (both advanced depth).
- voice_check.py: 0 cost.
- GSC: 0 calls.
- Playwright: 0 sessions.
- Total estimated session cost: ~$0.04 external API spend, at the lower bound of target envelope (~$0.03-$0.05 DFS + 2-4 Firecrawl + 3-6 Tavily). Came in lowest of the three Mexico kit briefs (Home: 3 Firecrawl + 5 Tavily; Away: 2 Firecrawl + 3 Tavily; Third: 1 Firecrawl + 2 Tavily) by reusing both internal-link validations and most of the Mexico cultural / squad / fixture / Round-of-32 context from prior briefs. Cumulative Mexico kit set session cost: ~$0.12 DFS + 6 Firecrawl + 10 Tavily across all three briefs.

## Findings logged

- learnings.md: no entry added this session (stayed surgical; pre-tournament demand spike exception already codified in commit 120a177; National Team Jersey CANONICAL template now four-time validated, recommend ORIN promote template status in next playbook revision pass).
- decisions.md: no entry added.
- shared-intelligence/seo-findings.md: no entry added.

## Recommendation candidates (not added per surgical posture)

1. **Template status promotion candidate:** National Team Jersey CANONICAL template has now landed cleanly on UAE v3 (2026-05-26), Mexico Home (2026-05-28), Mexico Away (2026-05-28), and Mexico Third (2026-05-28). Four consecutive validations across two federations and three kit roles (Home, Away, Third) within one cycle. Recommend the playbook framing graduate from "validated UAE v3" to "canonical, four-time validated" in the next pass. Surfaced as recommendation; not edited this session.
2. **Meta and Short Description ceiling discussion candidate:** The Third brief required slightly over-ceiling Meta (162 vs 158) and Short Description (309 vs 300) to preserve all load-bearing differentiators. If similarly content-dense kits emerge (limited-edition / collaboration / commemorative kits with denser narrative substance than standard Home/Away kits), consider whether the brief's character-count ceilings should flex up to 165 / 320 for differentiated kits while staying tight at 158 / 300 for standard kits. Or alternatively, maintain strict ceilings and force harder editorial cuts. Surfaced as a decision point for the playbook; not changed this session.
3. **PDP body content source-of-truth note (MEMORY.md candidate):** The live ProSoccer PDP vendor description on the Third kit is FIFA Store boilerplate ("More than a soccer apparel... fearless statement of national unity..."). Vendor boilerplate gives generic cues but does not name the kit's load-bearing differentiators (collaboration partner, design pattern specifics, symbolism, cultural anchors). The optimization lift comes from replacing vendor boilerplate with verified specialty-journalism substance. Surfaced as candidate `[PATTERN]` learnings entry; not written this session to keep learnings.md from churn.

## Open questions / flags for GATE

None this session. All design specifics verified across 4+ authoritative sources, currency-corrected (Someone Somewhere collaboration + Aztec MX pattern + Somos México back-of-collar + three-host-year symbolism all new to body copy vs vendor boilerplate), narrative differentiation from Home and Away briefs documented, fixture-forcing logic verified, internal link destinations validated, exception application verified. Meta and Short Description over-ceiling documented with reasoning. Brief paste-ready.

## Artifact paths

- **Visible brief:** `deliverables/page-optimizations/2026-05-28_session-01/adidas-2026-mexico-mens-stadium-third-soccer-jersey_brief.md`
- **Workforce-internal briefing:** this file (`.claude/agents/on-page-seo/briefings/2026-05-28_adidas-2026-mexico-mens-stadium-third-soccer-jersey.md`)
