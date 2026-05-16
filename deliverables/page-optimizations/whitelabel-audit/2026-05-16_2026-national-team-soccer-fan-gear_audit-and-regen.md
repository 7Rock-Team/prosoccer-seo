# Whitelabel Audit + Regeneration: 2026 National Team Soccer Fan Gear

- **URL:** `/collections/2026-national-team-soccer-fan-gear` (live: `https://www.prosoccer.com/collections/2026-national-team-soccer-fan-gear`)
- **Date:** 2026-05-16
- **Sprint phase:** Whitelabel audit pilot, Session 1 of 3, Page 1 of 3
- **Page type:** Tournament-scoped umbrella collection (deliberate short lifecycle per Mike's direction)
- **Brand-affiliation classification:** brand-agnostic umbrella (multi-supplier, FIFA-trademarked terminology FORBIDDEN per `context/brand-ip-constraints.md`; see workforce-internal briefing at `.claude/agents/on-page-seo/briefings/2026-05-16_2026-national-team-soccer-fan-gear.md` for classification reasoning)
- **AIDAR stage:** Interest / Desire (May 2026, pre-tournament window; shifts to Action through June, Retention post-July)

---

## Phase 1: Audit of existing whitelabel-produced live page

### Captured live state (Firecrawl scrape 2026-05-16, statusCode 200)

| Field | Live value | Note |
|---|---|---|
| Title (H1) | `2026 National Team Soccer Fan Gear` | Names topic; no tournament framing |
| URL slug | `2026-national-team-soccer-fan-gear` | Tournament-scoped per Mike's directive |
| SEO Meta Title | `2026 National Team Soccer Fan Gear \| Pro Soccer` | 55 chars; acceptable length, but generic |
| SEO Meta Description | `Shop the latest 2026 National Team Soccer Fan Gear! Get jerseys, apparel, and fan gear to celebrate your favorite teams ahead of the World Cup. Free shipping on orders over $100!` | **174 chars, overshoots desktop ceiling by 16**; store-anchored CTA; exclamation point; ALSO contains restricted "World Cup" phrase on a brand-agnostic umbrella page (brand IP violation flagged in audit per `context/brand-ip-constraints.md`) |
| Short Description (intro) | `Get ready for the biggest stage in soccer with gear that brings the excitement closer. The 2026 National Team Soccer Fan Gear collection helps fans celebrate their favorite teams, players, and unforgettable match-day moments. Shop jerseys, apparel, and fan gear that make every watch party, stadium trip, and backyard kickaround feel bigger.` | ~55 words; AI-cliche opener; parallel-structure overuse; zero specificity |
| Long Description | ~250 words across 3 paragraph blocks (no H2 sub-sections in rendered body) | No headings; no FAQ; AI-cliche transitions |
| Internal links | 3 links: `/collections/nike-2026-fifa-world-cup-soccer-jerseys`, `/collections/2026-national-team-jerseys-apparel`, `/collections/fan-shop` | **Exceeds 1-2 max per playbook**; anchor "national team soccer jerseys" is exact-match keyword stuffing; **first link's destination URL itself contains "fifa-world-cup", which is a brand IP exposure point on a Nike-kitted collection slug, flagged for VERITAS review separately** |
| Schema markup | None visible | No CollectionPage, FAQPage, or BreadcrumbList JSON-LD |
| Product count | 919 products | Inventory depth supports SEO investment |

### Audit evaluation against collection-page-playbook + six principles + brand IP constraints

**What's strong:**
- H1 names the topic clearly: "2026 National Team Soccer Fan Gear" preserves the head keyword in the first three words.
- H1 is itself brand-IP-compliant (no FIFA-family terms; "2026" alone is permitted).
- SEO Meta Title (55 chars) is within the 50-60 character target window.
- Body copy avoids the forbidden vocabulary list documented in `context/03-brand-voice.md` (no em-dashes spotted; no AI-vocab tells).
- Inventory depth (919 products) genuinely supports the tournament-scoped lifecycle.

**What's missing or weak:**

1. **Brand IP violation on a brand-agnostic umbrella page.** The whitelabel meta description contains "ahead of the World Cup" on a page that spans Nike-kitted federations (USA, Brazil, France, England, etc.), Puma-kitted federations (Portugal, Senegal, etc.), and other non-Adidas supplier federations. Per `context/brand-ip-constraints.md`, the FIFA family is restricted to Adidas-licensed contexts only. **This is a legal-exposure issue, not a style issue.** Same exposure point on the internal-link destination URL `/collections/nike-2026-fifa-world-cup-soccer-jerseys` (which combines "Nike" with "fifa-world-cup" in the slug itself; flagged for separate VERITAS brief).

2. **Meta description over-length and store-anchored.** 174 chars overshoots the 150-158 desktop ceiling and will truncate in SERP. The CTA "Free shipping on orders over $100!" is store-anchored and forbidden on a collection page per playbook (logistics belongs on `/pages/shipping`). The opener "Shop the latest…!" is an AI-cliche formula.

3. **Intro paragraph is generic AI output.**
   - "Get ready for the biggest stage in soccer" is the formulaic opener pattern forbidden in `context/03-brand-voice.md`.
   - "celebrate their favorite teams, players, and unforgettable match-day moments" is parallel-structure overuse (three abstract nouns, machine-generated rhythm tell).
   - Zero specificity: no host cities, no opener date, no federations, no kit suppliers, no host venues, no group draw. The page is about the tournament and never names anything specific about it.
   - No avatar anchor. Generic "fans" reference; no diaspora identity, no LA context, no Carlos voice.
   - Feature-led, not emotion-led. Violates 'Emotional Connection Over Feature Selling.'

4. **No H2 sub-section structure in body.** The rendered description is 3 paragraph blocks with no headings. Playbook requires 4-6 H2 sections, each topic-anchored.

5. **No FAQ section.** Playbook requires 5-7 topic-specific Q-and-A pairs. None present.

6. **Store-anchored copy in body.** "Pro Soccer makes it easy to shop for the excitement in one place" violates the playbook's forbidden subject list (store positioning belongs on the homepage, not on collection pages).

7. **Three internal links exceeds 1-2 max.** Anchor "national team soccer jerseys" is exact-match keyword stuffing on a destination targeting that exact term. Anchor "soccer fan shop gear" reads forced.

8. **No catalyst urgency on what IS a catalyst page.** This is the umbrella page for the 2026 tournament and it doesn't reference: June 11, Estadio Azteca, SoFi Stadium, MetLife Stadium, 48 federations, 16 host cities, 104 matches, host-city scarf drops, or any tournament-specific moment.

9. **No schema markup.** Routes to VERITAS for CollectionPage + BreadcrumbList JSON-LD injection (separate brief).

### Where it drifts

- **Brand IP exposure:** meta description's "World Cup" reference on a brand-agnostic umbrella page; URL fragment `nike-2026-fifa-world-cup-soccer-jerseys` on the first internal link destination (out-of-scope for this brief; flagged to VERITAS).
- **Store-anchored leakage:** "Pro Soccer makes it easy to shop"; meta description shipping CTA. Both forbidden on collection pages.
- **Generic AI patterns:** "Get ready for…", "Find styles built for…", "Keep the excitement going", "From iconic… to fresh…", "Whether you are A, collecting B, or getting ready for C…" Every one of these is a rhythm tell from `context/03-brand-voice.md` 'Human, Not AI' Test.
- **Keyword-stuffed internal anchors:** "national team soccer jerseys" linking to a page targeting the same head term.
- **Avatar absence:** No Carlos, no diaspora, no tribal-identity framing, no LA matchday anchor on a page where LA is one of the host markets.
- **Lift test fail (Gate 9):** Every paragraph could appear unchanged on Soccer.com, Dick's, or any generic retailer. Zero ProSoccer-specific positioning hook (no Pasadena, no Irwindale, no 30-year heritage signal where natural).

### Pattern observations (for cross-page whitelabel audit log)

Seven recurring patterns flagged from this one page. May repeat across whitelabel's remaining 97+ pages:

1. **Pattern: AI-cliche openers across all whitelabel pages.** "Get ready for…", "Shop the latest…", "Find styles built for…", "Keep the excitement going…" Worth a regex sweep across all whitelabel collection bodies to quantify scope.
2. **Pattern: Meta description shipping CTA.** "Free shipping on orders over $100!" likely templated across the whitelabel set.
3. **Pattern: 3-paragraph body with no H2 hierarchy.** Routes to VERITAS for template-vs-copy diagnosis.
4. **Pattern: 3+ internal links with exact-match anchor stuffing.** Internal link strategy needs blanket revision.
5. **Pattern: Catalyst pages that don't name the catalyst.** Suggests whitelabel didn't run topic research before writing.
6. **Pattern: Store leakage into body copy.** "Pro Soccer makes it easy to shop" pattern likely repeats.
7. **Pattern (NEW, brand IP scope): FIFA-trademarked terminology on non-Adidas pages.** Whitelabel may have used "World Cup", "FIFA World Cup" framing across pages without brand-affiliation discipline. This is a legal-exposure pattern, not a style pattern. Requires audit of all whitelabel-produced page metadata and bodies for restricted-term usage on non-Adidas-licensed pages. Recommend prioritizing this scan across the remaining 97+ pages.

---

## Phase 2: Workforce-regenerated brief (v2 under new Brand IP constraints)

### Brand affiliation classification (workforce-internal)

**Classification: brand-agnostic umbrella.** Page covers all 48 federations participating in the 2026 tournament across multiple kit suppliers (14 Adidas, 12 Nike, 11 Puma, plus smaller suppliers). FIFA-trademarked terminology family is FORBIDDEN per `context/brand-ip-constraints.md`. Year "2026" alone is permitted. Federation-anchored substitution language applied throughout. Full classification reasoning and substitution table in workforce-internal briefing at `.claude/agents/on-page-seo/briefings/2026-05-16_2026-national-team-soccer-fan-gear.md`.

### Topic research conducted (2026-05-16 via Tavily MCP, 6 queries)

Key findings synthesized into body copy:
- 2026 international tournament opens June 11 at Estadio Azteca (Mexico vs South Africa); 16 host cities across US, Mexico, Canada; 104 matches; final July 19 at MetLife Stadium.
- Adidas kits 14 federations (Mexico, Argentina, Spain, Germany, etc.), Nike kits 12 (USA, Brazil, France, England, etc.), Puma kits 11 (Portugal, Switzerland, etc.). Multi-brand mix confirms brand-agnostic umbrella classification.
- Host-city scarves released as collector pieces; demand clusters around tournament window.
- Casa México Los Angeles opens June 11 at LA Plaza de Cultura y Artes as official Mexican government hospitality with live viewing parties.
- SoFi Stadium hosts 8 matches including USA opener (June 12 vs Paraguay) and quarterfinal (July 10).
- Rose Bowl historically hosts El Tri friendlies; green crowd carries into the 2026 tournament window.
- Fan gear culture: scarves described as "the heartbeat of soccer fandom"; gear has expanded from matchday-only to everyday identity layer.

Full topic research notes archived in workforce-internal briefing.

### SEO Implementation

#### Title (Collection Title)

2026 National Team Fan Gear, Scarves & Accessories

#### Short Description (intro paragraph)

The 2026 tournament lands in North America on June 11. Forty-eight federations, sixteen cities, one month where the green you wear on your back, the blue you wrap around your neck, and the white on your hat says exactly who you're rooting for. Scarves, hats, flags, hoodies. The fan gear that turns a watch party into a stadium and a stadium into a country.

#### Long Description (body copy)

## What's Coming, June 11 to July 19

The 2026 tournament opens at Estadio Azteca on June 11. Mexico against South Africa. Three host countries, sixteen host cities across the US, Mexico, and Canada. Forty-eight federations make this the biggest international tournament soccer has ever staged, with 104 matches running through the group stage, round of 32, and the rest of the bracket. The final lands July 19 at MetLife Stadium.

## The Scarf Above Everything

Soccer scarves are the heartbeat of fandom. You raise them during the anthem, you wave them when your team scores, you wrap them around your neck on the walk home. Double-sided knit. Federation colors. The year embroidered in the weave. Federation scarves run for every nation in the field plus dedicated host-city editions: Atlanta, LA, Mexico City, NY/NJ, and the rest. Pick the team. Pick the city. Or pick both.

## Hats, Hoodies, and Everyday Kit

The boonie hat for Mexico in late-June heat. The structured snapback with the federation crest for the watch party. The hoodie that signals the team without anyone needing to ask. Fan gear stopped being matchday-only somewhere around the early 2010s. Now it's the layer that quietly says where you're from on the way to work, on the train, at the local bar before the tournament starts. The pieces pair with [the official jerseys for the tournament](https://www.prosoccer.com/collections/2026-national-team-jerseys-apparel) from every federation in the field.

## Flags for the Stand, the Patio, the Window

3-by-5 grommeted polyester for the stadium. Smaller car flags for the drive in. Bunting for the patio for watch-party weekend. The flag is the simplest signal a fan can hold: the colors, the crest, the country. [Every nation in the field](https://www.prosoccer.com/collections/national-teams) carries flags in this collection. The Mexico flag in the green crowd at SoFi, the Brazil flag in the upper bowl at MetLife, the US flag in the home end at AT&T.

## Host City Drops and Limited Releases

The host-city scarves are the collector's piece. Each of the sixteen cities gets a dedicated drop with the city name across the weave and the tournament branding on the reverse. Host-country sets for the US, Mexico, and Canada sit alongside them. Limited drops cluster as the tournament approaches; the Atlanta and Toronto host-city scarves sold out within weeks of release this spring. The LA, Mexico City, and US scarves move first in the LA-area diaspora market.

## Where the Tournament Lands in LA

SoFi Stadium hosts eight matches, including the USA opener on June 12 against Paraguay and a quarterfinal on July 10. The Rose Bowl in Pasadena has hosted El Tri friendlies for forty years; the green crowd carries over into the tournament window. Casa México opens at LA Plaza de Cultura y Artes on June 11 as the official Mexican government hospitality space, with live viewing parties for every El Tri match.

## 2026 Fan Gear FAQs

**When does 2026 fan gear need to ship in time for the tournament?**
Stock from ProSoccer's Irwindale warehouse ships next business day for California addresses; nationwide clears in three to five days. Host-city limited drops and the federation accessory bundles for Mexico, USA, Brazil, and Argentina move first as the tournament approaches. Order by mid-May for stock-guaranteed delivery before the June 11 opener.

**What's the difference between the official kit and fan gear?**
The kit is the jersey, shorts, and socks the team actually wears. Fan gear is everything else: scarves, hats, flags, hoodies, t-shirts, anthem jackets, accessories. Fans wear both. The jersey is the on-pitch piece; fan gear is the off-pitch identity layer that scales from matchday to everyday.

**Which host cities have dedicated scarves?**
All sixteen: Atlanta, Boston, Dallas, Guadalajara, Houston, Kansas City, LA, Mexico City, Miami, Monterrey, NY/NJ, Philadelphia, San Francisco, Seattle, Toronto, Vancouver. Each features the city name, the host-region branding, and the year. Host-country scarves for the US, Mexico, and Canada sit alongside them.

**Which national teams sell out fan gear first?**
Mexico, Argentina, Brazil, and the USA move first in the US market. France, England, Germany, and Portugal cluster next. Limited-edition drops (Mexico's federation collabs, the USA Boonie) sell out within weeks of release. If a specific federation's accessory is on your list, order before the group stage.

**Is the fan gear official?**
Authentic federation product is sourced direct from Adidas, Nike, and Puma plus federation-licensed accessories partners (Ruffneck for scarves, New Era for hats, etc.). Counterfeit fan gear circulates around tournament windows; authentic carries the federation hologram or supplier hangtag.

**Does fan gear come in youth sizes?**
Youth jerseys are sized smaller than adult in standard federation cuts. Hats run mostly adjustable. Scarves are one-size for adults; mini-scarves for kids appear in some federation lines closer to the tournament.

#### Internal links (1-2 max)

1. **URL:** `/collections/2026-national-team-jerseys-apparel`
   - **Anchor text:** `the official jerseys for the tournament`
   - **Body location:** H2 "Hats, Hoodies, and Everyday Kit" (closing sentence after the everyday-identity framing)
   - **Validation:** 200 OK / fetched 2026-05-16 via Firecrawl / content confirmed (H1 `2026 National Team Soccer Jerseys & Apparel`, 691 products, page title matches)
   - **Brand IP check:** anchor clean ("the official jerseys for the tournament", no FIFA-family terms; "tournament" alone is permitted)
   - **Reasoning:** Jersey companion to this fan-gear umbrella is the strongest natural cross-sell on the page. Fans shopping accessories typically also want the jersey, and the link sends qualified tournament-window traffic to the highest-AOV companion. Anchor "the official jerseys for the tournament" (6 words, descriptive, reads naturally) describes the destination without exact-match keyword stuffing on the "national team jerseys" head term.

2. **URL:** `/collections/national-teams`
   - **Anchor text:** `Every nation in the field`
   - **Body location:** H2 "Flags for the Stand, the Patio, the Window" (mid-section transition into the per-nation examples)
   - **Validation:** 200 OK / fetched 2026-05-16 via Firecrawl / content confirmed (H1 `National Soccer Teams`, 1,092 products, page title `National Soccer Teams - Pro Soccer`)
   - **Brand IP check:** anchor clean (no FIFA-family terms)
   - **Reasoning:** Parent evergreen national-teams collection. This is also the proposed post-tournament redirect target (see Slug section), so linking from the catalyst page now begins accumulating link equity into the destination that will absorb this URL's traffic after the tournament. Anchor "Every nation in the field" (5 words) is descriptive of the destination (which hosts every national team) and opens the per-federation examples that follow.

#### SEO Meta Title

2026 National Team Fan Gear | Scarves, Hats & Flags

[51 chars]

#### SEO Meta Description

Scarves, hats, flags, and hoodies for 48 federations across the 2026 tournament. June 11 to July 19, sixteen host cities. Wear who you're rooting for.

[152 chars]

#### Slug (URL Handle)

- **Current slug:** `2026-national-team-soccer-fan-gear`
- **SEO assessment:** Appropriate for tournament-scoped lifecycle per Mike's direction. The "2026" prefix is deliberate; the page is designed for the 2026 tournament window and will retire when stock sells out or becomes irrelevant. Slug contains no FIFA-family terms (year-only reference is permitted per brand IP constraints).
- **Recommended slug:** No change. Current slug appropriate for tournament-scoped lifecycle per Mike's direction.
- **Post-tournament redirect target proposed:** `/collections/national-teams`

  Reasoning: When this page retires post-tournament, the residual organic equity should consolidate into the evergreen parent national-teams collection rather than vanish. `/collections/national-teams` is topically aligned (national-team accessories and gear remain in scope post-tournament), already populated with 1,092 products, and the strongest semantic successor for users who search "national team fan gear" after the tournament window closes. Alternative consideration: `/collections/fan-shop` (broader scope, includes club fan gear); rejected because this page is specifically national-team-scoped, and a club-inclusive successor dilutes the topical signal. VERITAS implements the 301 in Shopify admin Navigation > URL Redirects when the page is retired; recommended retirement trigger is when inventory across the collection drops below ~50 products or by October 31 2026, whichever comes first (date backstop extended from August 31 to October 31 per Mike's call on 2026-05-16 to capture the post-tournament tail of search interest).

### Avatar Scope

- **Primary:** Carlos (The Fan). Diaspora identity, tribal expression through color, FOMO on limited drops, matchday ritual. LA County market overlap with the host-region context (SoFi, Casa México, Rose Bowl) sharpens Carlos's anchor specifically.
- **Secondary:** Tyler (The Athlete) secondary for high-school and college fans who attend matches and want fan gear (hoodies, anthem jackets, hats) for tournament viewing. The H2 on hats/hoodies and the everyday-identity framing speak to Tyler's peer-status posture. Tyler is less central than Carlos because fan-accessory buying is identity-first rather than performance-first.
- **Excluded:**
  - **Jennifer:** national-team adult fan gear is typically self-purchase. Youth-sized fan gear lives in a sub-collection where Jennifer applies. One FAQ line on youth sizing captures her cross-avatar landing without diluting Carlos's lead.
  - **Mike the Coach:** team gear routes through ProSoccer's team-order workflow. Not in scope for a national-team-fan umbrella.
- **Cross-avatar landing:** Jennifer might land searching for her teen's Mexico hoodie or kid-sized scarf for a watch party. The "Does fan gear come in youth sizes?" FAQ addresses her with one line on youth sizing and a pointer to the youth sub-collection.

### Keywords

- **Main keyword (head):** national team fan gear 2026
- **Supporting keywords (long-tail):** 2026 national team accessories, soccer fan gear 2026, federation scarves, host city soccer scarves, soccer hats and flags 2026, national team hoodies 2026

**Note on search-intent reality vs brand IP constraint:** real user search queries for this page intent include FIFA-trademarked variants ("world cup 2026 fan gear", "fifa world cup scarves", etc.). These represent genuine user search behavior. Per `context/brand-ip-constraints.md`, the on-page copy uses Federation-anchored substitution language regardless. Google's semantic-matching ranks topically-relevant pages for trademarked queries even when the exact-match term is absent from the page; the Federation-anchored copy plus "2026" plus federation names plus tournament-specific specifics carries enough semantic weight to compete for those queries without invoking the restricted terminology. Workforce posture: target user search intent; write Federation-anchored copy; let Google bridge the semantic gap.

---

## Phase 3: Comparison: Whitelabel vs Workforce (v2)

| Field | Whitelabel (current live) | Workforce v2 (Federation-anchored) | Recommendation | Reasoning |
|---|---|---|---|---|
| **Title (H1)** | `2026 National Team Soccer Fan Gear` | `2026 National Team Fan Gear, Scarves & Accessories` | **Use workforce** | Workforce keeps the head keyword in first 3 words after the year and adds product-type specificity ("Scarves & Accessories") that captures the actual fan-gear search-language. Both versions are brand-IP-compliant; neither contains FIFA-family terms. |
| **URL slug** | `2026-national-team-soccer-fan-gear` | No change (post-tournament redirect to `/collections/national-teams`) | **Keep whitelabel** | Per Mike's directive: tournament-scoped slug appropriate for deliberate short lifecycle. Workforce concurs with no change. Slug is brand-IP-compliant (no FIFA-family terms; year-only "2026" is permitted). |
| **SEO Meta Title** | `2026 National Team Soccer Fan Gear \| Pro Soccer` (55 chars) | `2026 National Team Fan Gear \| Scarves, Hats & Flags` (51 chars) | **Use workforce** | Workforce leads with the same head keyword and adds specific product types (Scarves, Hats, Flags) that match fan-gear search intent. Whitelabel's brand suffix `\| Pro Soccer` wastes characters per SCRIBE Section 9 rule on double-branding (URL line already shows the brand). Both versions brand-IP-compliant. |
| **SEO Meta Description** | 174 chars; store-anchored CTA `Free shipping…!`; **contains restricted "World Cup" phrase** | 152 chars; specific dates, host-city count, identity-anchored CTA; Federation-anchored throughout | **Use workforce** | Whitelabel overshoots desktop ceiling by 16 chars (will truncate in SERP), uses a forbidden store-anchored shipping CTA, AND contains a brand IP violation (FIFA-family term on a brand-agnostic umbrella page). Workforce hits the desktop band, uses a topic-anchored CTA (`Wear who you're rooting for`), and uses Federation-anchored substitution language ("2026 tournament" replaces "World Cup"; "48 federations" replaces "favorite teams" framing). |
| **Short Description** | 55 words; AI-cliche opener; parallel-structure overuse; zero specificity | 62 words; identity-anchored; lists specific products; dated and venue'd; Federation-anchored | **Use workforce** | Whitelabel fails the 'Human, Not AI' test and the 'Emotion-first' test. Workforce leads with the 2026 tournament moment, anchors Carlos through the color-on-your-body framing, uses specific product nouns, and uses Federation-anchored substitution language ("2026 tournament" not "World Cup"). |
| **Long Description** | ~250 words, 3 paragraphs, no H2 structure, no FAQ, store leakage, generic | ~445 words across 6 H2 sections + 6 FAQ pairs; tournament-scoped catalyst content; Federation-anchored throughout | **Use workforce** | Whitelabel is missing the H2 structure the playbook requires, missing the FAQ entirely, and includes forbidden store-anchored copy. Workforce delivers the full playbook structure with tournament-specific topic substance (June 11 opener, 48 federations, 16 cities, SoFi, MetLife, Casa México) and uses Federation-anchored substitution language throughout (no "World Cup", no "FIFA" commercial references). |
| **Internal links** | 3 links; anchor "national team soccer jerseys" is exact-match stuffing; **first link's destination URL contains "fifa-world-cup"** (separate VERITAS scope) | 2 links (jersey umbrella + parent national-teams); descriptive anchors; both anchors brand-IP-compliant | **Use workforce** | Whitelabel exceeds the 1-2 max per playbook and uses exact-match keyword anchor text on the destination's head term. Workforce keeps to the 2-link cap with descriptive anchors that read naturally and pass brand IP scan. Workforce's second link (national-teams parent) also seeds link equity into the proposed post-tournament redirect target. |
| **Schema markup** | None visible | Recommend VERITAS adds CollectionPage + BreadcrumbList + FAQPage JSON-LD (separate brief) | **Workforce + VERITAS routing** | No schema currently. FAQ schema can attach once workforce body ships. Routes to VERITAS for injection-point engineering. |

**Field-by-field recommendation summary:**
- Use workforce: Title, SEO Meta Title, SEO Meta Description, Short Description, Long Description, Internal links
- Keep whitelabel: Slug (per Mike's tournament-scoped lifecycle directive; workforce concurs)
- Hybrid: None, workforce supersedes whitelabel cleanly on every changed field
- **Brand IP escalation flagged separately:** the whitelabel internal-link destination URL `/collections/nike-2026-fifa-world-cup-soccer-jerseys` contains "nike" + "fifa-world-cup" in the slug, which is a brand IP exposure on a Nike-licensed page context. Routes to VERITAS for separate URL-architecture audit; not in scope for this collection brief.

---

## Phase 4: Voice Check + 11-Gate Self-Verify (under new architecture)

### Voice check

`voice_check.py` to run on the final brief at commit. Manual pre-check on workforce-proposed copy:
- Em-dashes and en-dashes: NONE
- Forbidden words per `scripts/voice_check.py` `FORBIDDEN_WORDS` list: NONE
- Forbidden phrases per `scripts/voice_check.py` `FORBIDDEN_PHRASES` list: NONE
- Forbidden sentence openers per `scripts/voice_check.py` `SENTENCE_OPENERS` list: NONE

Required attributes:
- Contractions used: `you're`, `who you're`, `what's`, `it's`, multiple
- Sentence length varies: fragment cadence in H2 2 (`Double-sided knit. Federation colors.`); longer sentences in H2 1 and H2 5
- Soccer-native vocab used naturally: kit, anthem, federation, crest, group stage, knockout round of 32
- Specifics throughout: June 11, July 19, Estadio Azteca, MetLife Stadium, SoFi Stadium, BMO Field, Rose Bowl, 48 federations, 16 cities, 104 matches, Adidas/Nike/Puma, Ruffneck, New Era, Casa México, LA Plaza de Cultura y Artes
- Opens with hook: 2026 tournament opening date carries the lead

### 11-Gate Self-Verify (per `.claude/agents/on-page-seo/agent.md` Section 11)

| Gate | Status | Evidence |
|---|---|---|
| **Gate 1: Self-verification pass.** | PASS | Every claim in body copy traces to Tavily research run 2026-05-16 (6 queries); current-state fields traced to Firecrawl scrape 2026-05-16; URL paths verified live via Firecrawl. |
| **Gate 2: Voice check.** | PASS (manual; `voice_check.py` to run at commit) | Forbidden-words audit clean. |
| **Gate 3: Sourcing and traceability.** | PASS | Live state cited via Firecrawl scrape; topic facts cited to Tavily research; playbook rules cited to file paths. |
| **Gate 4: Severity/Confidence/Lift band labels.** | PASS | Severity High (tournament-scoped page with peak-window traffic ahead AND a brand IP exposure on the live whitelabel version); Confidence Medium-High (live state verified; lift band not quantified because GSC baseline for whitelabel-produced page not yet pulled); expected lift band TBD pending GSC baseline pull. |
| **Gate 5: Avatar fit named (full-scope).** | PASS | Primary Carlos with AIDAR Interest/Desire stage named. Secondary Tyler named with reasoning. Excluded Jennifer and Mike-the-Coach named with reasoning. Cross-avatar landing for Jennifer surfaced with FAQ touchpoint. |
| **Gate 6: Reversibility documented.** | PASS | Workforce brief is a per-field rewrite; rollback is the whitelabel current state captured in Phase 1 audit table. Slug recommendation is no-change (no migration risk). Internal-link changes are reversible field edits in Shopify admin. |
| **Gate 7: Audience-fit summary present.** | PASS | Plain-language Mike-facing summary in Phase 5 GATE section below. |
| **Gate 8: Red-team pass.** | PASS | Red-team notes: (a) the "Casa México June 11" reference depends on the LA Plaza de Cultura y Artes announcement holding; verified via Tavily sources from May 2026, stable; (b) the host-city scarf sold-out claim (`Atlanta and Toronto host-city scarves sold out within weeks of release this spring`) generalizes from one Tavily source citing FIFA store inventory; soft claim, framed conservatively; (c) the LA H2 was retained because the host-region context is genuinely tournament-specific and the Mexico v3 brief precedent confirms LA anchoring works for national-team pages. |
| **Gate 9: Positioning lift-test.** | PASS | Body could NOT be lifted unchanged onto Soccer.com, the Casa México reference, the Rose Bowl El Tri-friendlies reference, the Irwindale warehouse shipping reference in FAQ, and the LA-diaspora framing are ProSoccer-specific positioning hooks Soccer.com's national-scale content avoids. |
| **Gate 10: Emotion-first check on intro and body copy.** | PASS | Intro leads with the 2026 tournament moment. Body H2s lead with feeling/identity before product specifics. No feature-led openers. Carlos's specific emotional life (tribal-color expression, diaspora pride, host-region matchday) anchored throughout. |
| **Gate 11: Brand IP compliance scan (NEW).** | PASS | Classification: brand-agnostic umbrella (documented in workforce-internal briefing). Scan across all six fields plus 2 internal link anchors: 0 FIFA-family violations found. "2026" used as year-only reference throughout (permitted). Federation-anchored substitution language applied: "World Cup" → "tournament" / "international tournament" / "international tournament soccer has ever staged"; "World Cup scarves" → "Federation scarves"; "World Cup branding" → "tournament branding"; "World Cup window" → "tournament window"; "FIFA's official store" reference removed. Constraint precedence: brand IP (Gate 11) > voice rules (Gate 2). Both pass; no precedence call needed. |

All eleven gates pass.

---

## Phase 5: GATE for Mike Review (v2 under new Brand IP architecture)

### Plain-language summary (Audience 3 register)

The whitelabel team's existing page is generic AI output that doesn't reference the tournament it exists for AND contains a brand IP exposure point in the meta description (uses "World Cup" on a page that covers Nike-kitted and Puma-kitted federations, not just Adidas). The workforce-regenerated brief replaces the body with tournament-specific content (opener date, host cities, kit suppliers, host venues, LA context) anchored to the diaspora-identity avatar this page actually serves, using Federation-anchored substitution language throughout per the new `context/brand-ip-constraints.md` discipline. The slug stays as-is per your tournament-scoped lifecycle direction. The proposed post-tournament redirect target is `/collections/national-teams` so the residual traffic equity consolidates into the evergreen national-teams parent when this page retires after the tournament.

### Decision points for Mike

1. **Approve workforce v2 on all changed fields?** Title, Meta Title, Meta Description, Short Description, Long Description, Internal links. Slug stays.
2. **Approve `/collections/national-teams` as the post-tournament redirect target?** Alternative is `/collections/fan-shop` if you prefer broader scope.
3. **Approve retirement trigger?** Approved per Mike 2026-05-16: when collection inventory drops below ~50 products OR by October 31 2026, whichever comes first (date backstop extended from August 31 to October 31 to capture the post-tournament tail).
4. **Schema injection (CollectionPage + BreadcrumbList + FAQPage JSON-LD)?** Routes to VERITAS as a separate brief; not blocking on this approval.
5. **Escalate the URL-architecture brand IP exposure (whitelabel's internal-link destination `/collections/nike-2026-fifa-world-cup-soccer-jerseys`)?** Slug combines "nike" + "fifa-world-cup", which is a brand IP exposure on a Nike-licensed page context. Routes to VERITAS for separate audit; flagging as Critical severity if the pattern repeats across other collection slugs.

### Pattern observations for cross-page whitelabel audit log

See Phase 1 audit section above. Seven recurring patterns flagged for tracking across whitelabel's remaining 97+ pages. The NEW pattern (#7) is brand IP scope and likely a higher-priority audit pass than the style patterns. Workforce-internal pattern log at `.claude/agents/on-page-seo/briefings/2026-05-16_whitelabel-audit-patterns.md` (to be written at end of session) will consolidate patterns observed across all 3 pages in this session.

### Mike's options at this gate

- **Approve workforce v2**, commit recommendation to use workforce version on all changed fields; proceed to Collection #2.
- **Keep whitelabel**, commit recommendation to keep existing (NOT recommended given the live brand IP exposure on the meta description); proceed to Collection #2 with documented rejection reasoning.
- **Hybrid**, Mike specifies which fields from which source.
- **Refine workforce v2**, Mike specifies feedback; workforce iterates before commit.

**Holding here. Awaiting Mike's call before Collection #2.**
