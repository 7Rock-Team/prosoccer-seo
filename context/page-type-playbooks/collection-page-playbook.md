# Collection Page Playbook

_Page-type playbook for any URL under `/collections/*`. Read by SCRIBE on every collection-page brief, ahead of the six copy-writing principles in `context/03-brand-voice.md`. This playbook governs subject matter (what the page is ABOUT). The six principles govern execution quality (HOW the copy reads). Subject first, then voice._

## Subject focus

A collection page is ABOUT the collection's topic. The topic is the team, the player, the brand, or the category. The avatar landed here to learn about and feel connected to that topic. Every word in Title, Meta Title, Meta Description, Short Description, and Long Description serves the avatar's connection to the topic.

ProSoccer the store does not appear on a collection page beyond the Shopify chrome (header, footer, cart). Carlos opened `/collections/mexico` because he wants to feel his connection to El Tri. He didn't open it to read about the Pasadena fitting room or the Irwindale dispatch cutoff. The store is invisible inside the page body because Carlos didn't come for the store.

## Forbidden subjects on collection pages

The following are out of scope for collection-page copy. Any draft that includes them is on weak ground and gets rewritten:

- ProSoccer the store. No Pasadena retail mentions, no Irwindale warehouse mentions, no "30 years in business" framing, no "Why ProSoccer for X" sections.
- Store positioning, brand promotion, "what makes us different" content. The homepage handles store positioning. See `context/page-type-playbooks/homepage-playbook.md`.
- Store logistics. Shipping policies, return policies, fitting-room hours, dispatch cutoffs. These belong on `/pages/shipping`, `/pages/returns`, `/pages/locations`, the cart flow, and the checkout flow. They do not belong in collection-page body copy.
- Store-specific operational detail. Retail hours, store addresses, warehouse location, customer-service phone numbers. Same routing as logistics above.
- Generic e-commerce platitudes. "Shop our wide selection," "find what you need," "the best deals on X." This copy was forbidden anyway under the cognitive-load and human-not-AI rules in `context/03-brand-voice.md`, but flagging it again here because store-anchored copy tends to fall back on it.

## Required subjects on collection pages

The following are in scope and the body copy must serve them:

- The collection's topic in depth. History, culture, identity, key facts, current relevance. For a national team: founding, federation, kit history, signature players, tournament record. For a player: biography, club career, signature moments. For a brand category: brand heritage, signature products, who wears them. For a product category: what the category is, how it differs from adjacent categories, who uses it.
- The avatar's emotional connection to the topic. What does owning gear from this collection mean to the avatar's identity? Apply `context/03-brand-voice.md` 'Emotional Connection Over Feature Selling' to the topic specifically. Carlos's connection to El Tri runs through cultural diaspora, family memory, and matchday ritual; that's the well to draw from for a Mexico page.
- Topic-specific information the avatar's super-fans want to learn or be reminded of. Carlos knows the 2026 World Cup hosts. He may not remember the exact group draw or the kit-supplier history. Useful detail for a super-fan beats generic detail for a casual buyer.
- Product range explanation through the topic lens. "The 2026 home kit, the away kit, and the third drop before kickoff" is product-range explanation through the El Tri lens. "We carry a wide range of Mexico jerseys in many sizes" is product-range explanation through the store lens. The first belongs on the page; the second does not.

## Required pre-write research

ORIN runs topic research before SCRIBE writes. The topic research becomes the substantive backbone of the body copy. Without it, SCRIBE falls back on whatever the model already knows about the topic, which is usually generic and often stale.

For any collection page, ORIN researches:

- The topic's history. Team founding, federation history, player biography, brand origins, category evolution. Five to ten Tavily queries sized to the topic.
- Current cultural and competitive relevance. Current squad or roster, recent achievements, recent kit drops, upcoming tournaments, current brand catalog. Three to five Tavily queries.
- Identity markers. Colors, nicknames, traditions, anthem references, key moments fans reference, signature numbers (Maradona's 10, Messi's 10, Ronaldo's 7). Two to three queries.
- Avatar relationship to the topic. Cultural diaspora connections, fan rituals, identity expression, matchday traditions. Two to three queries.
- Current or upcoming events that anchor emotional urgency. Kit drops, tournaments, milestones, season openers. Two to three queries.

Tavily MCP is the default research tool. Five to fifteen queries per page is normal. Document key findings in SCRIBE's session briefing under `.claude/agents/on-page-seo/briefings/YYYY-MM-DD_<slug>.md`, not in the visible brief Mike reads. The visible brief shows finished copy only.

If the topic is one ORIN already knows deeply (e.g., a third pass at Mexico after running it twice), the research budget can shrink. Default posture is research first; trim only when the existing topic file in the briefing folder is fresh and complete.

## Field-specific rules

Six fields on a Shopify collection page. Each has a different optimization target.

### Title (Collection Title)

The visible H1 on the live collection page. Names the topic specifically. Avatar-search-language specificity is preserved here; the storefront Title doesn't have to lead with the head keyword the way the SEO Meta Title does.

- Mexico: `Mexico National Team Jerseys & El Tri Fan Gear`. Differentiates from Liga MX club content.
- Argentina: `Argentina National Team Jerseys & La Albiceleste Gear`. Differentiates from Argentine club content.
- Adidas Predator: `Adidas Predator Boots, Cleats & Pro Edition Lineup`. Differentiates from generic "soccer cleats" browsing.

Per `.claude/agents/on-page-seo/agent.md` Section 9 'Keyword placement per field', the head keyword sits in the first three words. Brand prefix only when it adds trust.

### SEO Meta Title

Head-keyword-first for SERP discovery. Can be more generic than the storefront Title because the purpose is search ranking, not browsing differentiation.

- Mexico: `Mexico Jersey & El Tri Gear | LA Soccer Specialty Since 1995` (head keyword first; storefront-and-positioning suffix where room).
- Argentina: `Argentina Jersey & La Albiceleste Kit | ProSoccer LA`.
- Adidas Predator: `Adidas Predator Cleats | Pro Edition & Elite Models`.

50 to 60 characters. Front-load the head keyword in the first 30 characters. Mobile cuts around 40 characters; the value-prop sits before that line.

### SEO Meta Description

Speaks to the avatar (the fan), not to the store, and includes a call-to-action that earns the click. Topic-anchored, never store-anchored. The CTA names something the avatar actually wants to do on this page.

Topic-anchored CTAs:

- `Shop the 2026 home kit`
- `Find your El Tri size`
- `Get the 2026 drops first`
- `Pick the player edition or the fan cut`

Store-anchored CTAs (do not use):

- `Shop ProSoccer for the best deals`
- `Find your favorite at our store`
- `Browse our wide selection`

150 to 158 characters desktop. The head keyword sits naturally in the first 100 characters (Google bolds the match). Don't repeat the title verbatim.

### Short Description (intro paragraph)

Emotion-first lead about the topic and what it means to the avatar. Per `context/03-brand-voice.md` 'Emotional Connection Over Feature Selling', the first sentence carries feeling, identity, or moment. Features and product detail come in supporting sentences if at all. By the end of the first paragraph the avatar should feel seen as a fan of the topic.

50 to 80 words. One to three sentences. Does not name the store. Does not name shipping, returns, or retail locations.

### Long Description (body copy)

Four to six H2 sections about the TOPIC, not the store. The topic research from the pre-write step becomes the substance here. 200 to 500 words across all H2 sections combined (Shopify scrolls a long body cleanly; over 500 words tends to bury the products on mobile).

H2 patterns by collection type (these are starting frames, not rigid templates; topic research dictates the actual H2s):

- **National team:** team history, current squad, kit history and design, cultural significance to fans, what the next major tournament means, key players to watch.
- **Player:** biography, career arc, signature moments, current season, what their gear means to fans, kit and boot lineage.
- **Brand category (e.g., Adidas Predator):** brand heritage, signature design elements, who wears them and why, model lineage (gen-by-gen evolution), current top model, who the line is for.
- **Product category (e.g., goalkeeper gloves):** what the category is and isn't, how to choose, who plays in this category, signature brands and models, fit and care basics.

Each H2 should pass the lift test from `.claude/agents/on-page-seo/agent.md` Section 11 Gate 9. If the section could appear unchanged on Soccer.com or any generic retailer's site, it lacks topic depth and gets rewritten.

Per `.claude/agents/on-page-seo/agent.md` Section 9 'Keyword placement per field', long-tail variants belong inside the H2 wording naturally (not "Mexico Jersey FAQs" but "What the 2026 El Tri Home Kit Means for the Diaspora" or similar).

### FAQ section

Topic-specific questions fans actually ask. Not generic store questions. The FAQ is a natural place to capture long-tail queries that don't fit the body H2s.

For Mexico:

- `When does the 2026 home kit release?`
- `What's the difference between the player and fan version of the El Tri kit?`
- `Who's in Mexico's 2026 World Cup squad?`
- `Why does Mexico wear green?`
- `Where can I get a kit with Chicharito's name and number?`

Forbidden FAQ questions (these belong on store-policy pages, not on collection pages):

- `What's your return policy?`
- `How long does shipping take?`
- `Do you have a fitting room?`
- `Can I exchange a jersey?`

Five to seven Q-and-A pairs is the standard range. Each answer is two to four sentences. The schema attaches via VERITAS's FAQPage injection; SCRIBE writes the question-answer copy that the schema surfaces.

## Worked example 1: National team collection (Mexico template)

URL: `/collections/mexico`
Primary avatar: Carlos
Topic-research outputs: El Tri founded 1927; FMF; current head coach; 2026 World Cup co-host; Estadio Azteca opener June 11 2026; recent kit history (1986, 1994, 1998, 2010, 2014, 2018, 2022, 2026); diaspora identity in LA; Adidas as kit supplier since 1999.

```
Title (Collection Title)
Mexico National Team Jerseys & El Tri Fan Gear

SEO Meta Title
Mexico Jersey & El Tri Gear 2026 World Cup Kit
[57 chars]

SEO Meta Description
The 2026 El Tri home kit, the away, and the player and fan cuts. Authentic Adidas Mexico jerseys for the diaspora that bleeds verde, blanco, y rojo. Shop the kit.
[157 chars]

Short Description
El Tri opens the 2026 World Cup at Estadio Azteca on June 11. Mexico is the country LA's diaspora carries on its back every four years, and the kit is how that identity walks down the street. Wear what they wear.

Long Description (H2 sections, topic-anchored, no store mentions in body):

## El Tri at the 2026 World Cup

Mexico co-hosts with the US and Canada. The opener is at Estadio Azteca, the same stadium that hosted the 1970 and 1986 finals. No other country has hosted three Men's World Cups. The squad mixes Liga MX core with Europe-based players: Edson Alvarez, Hirving Lozano, Cesar Montes, Santi Gimenez, Luis Romo. Group draw lands in December 2025.

## The 2026 Home Kit

Adidas keeps the verde primary with a Aztec-coded pattern across the chest and a darker green panel along the shoulders. The crest is centered traditional FMF style. Player version uses Adidas Heat.RDY weave with the closer cut Hugo Sanchez wore in '94 and the squad wears today. Fan version uses softer fabric and a regular fit. Both carry the official tags and holographic.

## The Verde, Blanco, y Rojo

The colors are the flag. The eagle on the crest is from the Mexican coat of arms. Green for hope, white for unity, red for the blood of the nation. Every kit since 1968 has held those colors as primary, with the away alternating in white through most eras and once in red ('98). The 2026 third kit, expected closer to the tournament, traditionally lets Adidas experiment with the deep red or a black variant.

## Players to Watch in 2026

Lozano on the wing for pace and pocket runs. Alvarez in the double pivot, the squad's metronome. Santi Gimenez at striker after his Feyenoord move and now Milan time. Cesar Montes in the back, leading the line out from the back. The wildcard is Marcelo Flores, the dual-eligible Arsenal academy product who chose El Tri.

## Kit History from 1994 to 2026

The 1994 kit (Aztec-pattern home, the bright red away) is the diaspora's favorite. The 1998 home was a clean green with the eagle large across the chest. 2006 and 2010 went black-trim minimalist. 2014 ran a deep red away. 2018 and 2022 leaned modern with thinner crest panels. 2026 is being read as a return-to-tradition design.

## Why El Tri Means More in LA

LA County has more Mexican-Americans than any city outside Mexico City. Estadio Azteca is a six-hour flight; Pasadena's Rose Bowl has hosted El Tri friendlies for forty years. When Mexico plays the US in Pasadena, the green in the stands isn't an away crowd. It's the home crowd. The kit isn't fan merch; it's a flag a quarter of the city wears in shifts.

(FAQ follows as a separate section)
```

Annotation:

- The Long Description never names ProSoccer, Pasadena retail, Irwindale warehouse, or any store-positioning element.
- Every H2 is about Mexico, not about the store.
- Topic-research outputs are visible: founding date, kit-supplier history, current squad, kit history by tournament, cultural diaspora data.
- The avatar (Carlos) is anchored throughout: diaspora identity, matchday ritual, the flag-as-kit framing.
- The lift test (Gate 9) passes: this body copy could not appear unchanged on Soccer.com because it commits to a specific cultural angle Soccer.com avoids.
- Voice rules: no forbidden words, no em-dashes, contractions used, varied sentence lengths, specifics throughout (player names, years, kit details).

## Worked example 2: Player collection (Messi template)

URL: `/collections/lionel-messi-jersey`
Primary avatar: Carlos secondary; Tyler primary if URL emphasizes performance kit; for an Inter Miami fan-jersey URL, Carlos is primary.
Topic-research outputs: Messi born 1987 Rosario; Barcelona 2004 to 2021; PSG 2021 to 2023; Inter Miami 2023 to present; 2022 World Cup winner; eight Ballons d'Or; Argentina cap leader; signature 10; current Inter Miami #10 home and away kits; recent Messi-edition adidas Predator and F50.

```
Title (Collection Title)
Lionel Messi Jerseys & Argentina + Inter Miami Kits

SEO Meta Title
Messi Jersey | Inter Miami #10, Argentina, Barcelona Kits
[58 chars]

Short Description
Messi turned the #10 into a verb. The kits in this collection trace the arc: Argentina's albiceleste from the 2014 final to the 2022 trophy lift, the Inter Miami pink that's redefining MLS, and the Barcelona blaugrana that started it. The same name on the back, in five different colors of his career.

Long Description (H2 sections):

## The 2022 World Cup Final and What the Albiceleste Means Now

Messi lifted the trophy in Lusail on December 18, 2022. The final he'd lost in 2014, in extra time on the same continent, eight years on. The albiceleste he wore that night is the one fans want. The current Argentina home kit carries the three-stars detail above the crest, one for each World Cup, the third earned in Qatar.

## The Inter Miami Era

He chose Miami in summer 2023 over a Saudi offer that would've paid more than every European league combined. Pink and black is a kit no one else in MLS owns the visual of. The #10 home and the black away are the bestselling MLS kits of the modern era. Apple TV broadcasts every match.

## Barcelona, the Beginning

Messi joined La Masia at 13. He debuted for the first team in 2004. By 2009 he was the best player alive. The Barcelona kits across his run, the Qatar Foundation chest in '12, the Rakuten chest in '17, the blaugrana stripes that don't change much except in their accents, are the kits older Messi fans associate with him most.

## What Makes a Messi Kit a Messi Kit

Number 10 on the back. The name in the federation or club font. For Argentina that's the AFA blocky font; for Inter Miami it's the cleaner sans-serif Adidas designed for the league. The crest matters: AFA with the three stars, Inter Miami with the heron silhouette, Barcelona with the cross of Saint George. Authentic kits carry the Adidas climacool or Heat.RDY tech (Argentina, Barcelona) or the league-issued tech (Inter Miami).

## The Boots He Wore

Adidas across his career. The F50 era in his early Barcelona run. The Nemeziz he was the face of from 2017 to 2023. The Adizero F50 since the 2024 relaunch. Each generation tied to a chapter of his career; collectors usually pick by chapter, not by what's current.
```

Annotation:

- Every H2 is about Messi, not about the store.
- Topic-research outputs are visible throughout: the 2022 final detail, the Inter Miami move detail, the boot-generation history.
- Avatar (Carlos primary) anchors the diaspora and matchday emotional language; Tyler shows up in the boot-generation H2 because that's where performance-kit buyers think.
- The body works for Argentina, Barcelona, and Inter Miami fans simultaneously without diluting any of them.
- Lift test passes: the specifics (Lusail 2022, the Saudi-offer detail, the Heat.RDY vs league-tech distinction) commit to angles a generic retailer would avoid.

## Worked example 3: Brand category collection (Adidas Predator template)

URL: `/collections/adidas-predator`
Primary avatar: Tyler (performance buyer)
Secondary avatar: Carlos (collector)
Topic-research outputs: Predator launched 1994 by Craig Johnston; Beckham era; Zidane wore them; controlled-shot rubber elements; relaunched as Predator Accuracy in 2023; Predator 24 Elite is the current top model; the line has gone through seven generations; key signature pros wearing them now (Bellingham, Pedri, Rice).

```
Title (Collection Title)
Adidas Predator Boots, Cleats & Pro Edition Lineup

SEO Meta Title
Adidas Predator Cleats | Pro Edition, Elite & 24 Models
[55 chars]

Short Description
The Predator is the boot Beckham wore for England, Zidane wore for the Real treble, Rice wears for Arsenal now. Thirty years of controlled-shot rubber, redesigned every generation, still the boot for the player who wants the ball to do exactly what they tell it to.

Long Description:

## The Predator Story, 1994 to Now

Craig Johnston, the former Liverpool winger, designed the original in 1994 with rubber strips on the upper to give the ball more spin and control. Adidas bought the design and launched it that year. The Mania era ran through the early 2000s. The Pulse, the Powerswerve, the X, the Predator 18 with the laceless upper, the Accuracy in 2023, and now the Predator 24. Every generation a different take on the same idea: more control, more curve, more shot.

## Who Wears Them Now

Jude Bellingham at Real Madrid. Declan Rice at Arsenal. Pedri at Barcelona. Trent Alexander-Arnold for the long-range crossfield ball that bends like a Predator boot is supposed to make it bend. The Predator is the boot for the midfielder who runs the game with the ball more than the leg.

## Predator 24 Elite vs Predator 24 League

Elite is the pro tier: K-leather upper, knit collar, lighter chassis, stiffer plate. League is the same silhouette and rubber-element design at a lower price, with synthetic upper and a softer plate. Elite for the player who needs the touch at the top level. League for the club player who wants the look and most of the feel without the pro-tier cost.

## Why the Rubber Elements Matter

The rubber strips on the front of the boot grip the ball at impact. More grip means more spin on a struck ball, which means more curve. It's not magic; it's friction. Free-kick takers love them. Long-range passers love them. Strikers who want a controlled-finish over a power-finish prefer them to the F50 or the Mania.

## The Predator at Different Surfaces

Firm ground for natural grass. Artificial grass for the green-plastic surface. Turf for older astroturf. The Predator runs across all three. Pick the plate to match the surface; the upper and the rubber-element design stay the same across the line.
```

Annotation:

- Body copy is about Predator the boot line, not about ProSoccer the store.
- Topic-research outputs visible: launch year, designer, signature pros, generation history, current models.
- Tyler primary: performance specifics, plate-and-surface detail, pro-tier vs league-tier comparison.
- Carlos secondary lands at the generation history (collectors care about which generation a player wore).
- Lift test passes: a Soccer.com page on Predator would avoid the Craig Johnston detail and stay closer to "the Predator is a great boot for control." This page commits.

## How this playbook integrates with the six copy-writing principles

The playbook governs subject matter. The six copy-writing principles in `context/03-brand-voice.md` and `.claude/agents/on-page-seo/agent.md` Section 7 govern execution quality. The order is:

1. Read this playbook. Confirm the page's topic and the forbidden / required subject lists.
2. Run topic research per the 'Required pre-write research' section above.
3. Apply the field-specific rules above to determine WHAT each field is about.
4. Apply the six copy-writing principles to determine HOW each field reads:
   - The "Human, Not AI" Test (rhythm, openers, transitions, closings)
   - Cognitive Load Minimization (lead with the noun, one idea per sentence, scannable specifics)
   - Emotional Connection Over Feature Selling (emotion before feature, avatar-anchored hook, show-them-what-they'll-feel test)
   - Full-Avatar-Scope Discipline (primary, secondary, excluded, cross-avatar landing)
   - Business Context Anchor (the four positioning claims from `context/00-business-overview.md`)
   - Keyword Placement per Field (the table in `.claude/agents/on-page-seo/agent.md` Section 9)
5. Run `voice_check.py` on the staged copy.
6. Self-verify per `.claude/agents/on-page-seo/agent.md` Section 11.

If the playbook and a principle ever conflict (rare; the principles are voice-and-rhythm rules, and the playbook is subject-matter rules, so the surfaces don't overlap much), surface to ORIN before resolving.
