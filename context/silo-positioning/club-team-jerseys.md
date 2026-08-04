# Silo Positioning: Club Team Jerseys

Per-SKU prose patterns claimed in shipped briefs for club-team jersey PDPs (Chelsea, Liverpool, Real Madrid, Barcelona, and so on). Like `national-team-jerseys.md`, this silo is keyed by **product class**, not brand: club jerseys collide on a shared prose lane (club identity, city and stadium heritage, league and continental competition, passed-down family loyalty) regardless of kit supplier, and each club is single-brand per cycle, so a brand-keyed file would scatter unrelated clubs.

Why a separate file from `national-team-jerseys.md`: club jerseys sit in a **distinct prose lane** from national-team jerseys. National-team copy runs on national pride, heritage, and the tournament cycle; club copy runs on club allegiance (family passed-down loyalty, city identity), stadium heritage, domestic-league and continental-competition context, and club rivalries. Different buyer emotion, different named entities, different guardrails. This split was pre-committed in `national-team-jerseys.md` and confirmed by the product-class-keyed taxonomy Mike approved 2026-06-10.

File created 2026-07-08 (Batch 6, triggered by the first club jersey under the Registry 2 silo architecture: Chelsea Youth Stadium Home). The shipped Liverpool 2024-25 Away brief (commit b7159dc, 2026-05-26) predates Registry 2 and is backfilled below so the club prose log is complete from its true first shipment.

Format and append protocol: see `README.md`. ORIN reads this file during the pre-dispatch differentiation pass and appends after each batch commits.

## Pre-dispatch reference / guardrails

Reference notes ORIN reads at the pre-dispatch differentiation pass. Separate from the append-only per-SKU log below.

### Competition-naming IP policy (added 2026-07-08, Mike Decision 2, Batch 6; precedent for all future club work)

Club body copy may reference competition names under these rules. This is a legal-risk-reduction posture, not a legal opinion; a ProSoccer-counsel sign-off can upgrade it (see the optional path below).

- **Premier League: direct reference PERMITTED.** Body copy may name "Premier League" and "top-flight English football" as plain descriptive fact. The kit supplier (Nike, and so on) does not own Premier League IP; a retailer naming the league its product is worn in is standard nominative use.
- **UEFA Champions League: default to GENERIC framing.** Use "European competition," "continental campaign," "Europe's premier club competition," "European nights," and similar. ORIN research (Batch 6) surfaced no explicit UEFA / Champions League retail-copy permission, only the general US nominative-fair-use defense, which is jurisdiction and fact specific. Per Mike Decision 2, default generic unless a licensing check confirms direct reference is permitted.
- **Forbidden in every field (Title, Meta Title, Meta Description, Short Description, body, anchors, FAQ):** Premier League or UEFA logos, stylized wordmarks, competition badge imagery; and any phrasing implying official status ("official Premier League product," "Champions League edition," "endorsed by"). The line is descriptive factual word-use (low risk) versus mark-use or implied license (do not).
- **Forward-only:** if a licensing-enforcement issue surfaces later, adjust future briefs; do not retro-edit shipped club copy.
- **Optional upgrade path:** a one-time ProSoccer-counsel sign-off on direct Champions League naming would let future club briefs name it directly; tracked in `work-log/follow-ups.md` (2026-07-08).

### Heritage honours default to qualitative (added 2026-07-13, claims gate)

Specific league / title / trophy counts and outright "most" / "record" superlatives in club body copy AGE and are CONTESTED (Liverpool drew level with Manchester United at 20 English league titles in 2024-25, breaking the "record 20" / "most successful" claims KA6871 shipped in its first draft). Default to qualitative honours ("one of England's most decorated clubs", "a European pedigree few can match"); a specific count ships only with a durable cited source, otherwise it is cut. Enforced deterministically by `scripts/batch_gate.py` `check_heritage_counts` (regression fixture: `TestKA6871HeritageCounts`) and codified in `context/workforce-conventions.md` 'Claims verification: heritage honours default to qualitative'.

### Tier posture for club jerseys (added 2026-07-08)

The Club Jersey template is **CANONICAL** (validated on Liverpool 2024-25 Nike Away, commit b7159dc). Subsequent club-jersey work is **Tier 2A** (pattern-follow, currency-check Tavily, template-fill), not a foundational Tier 1 build. Youth club jerseys add the parent / young-fan sizing-and-growth dimension on top of the canonical structure, framed through club allegiance (family loyalty passed down, city identity), not national pride.

### Chelsea FC (added 2026-07-08, from ORIN research for Batch 6 Nike Youth Stadium Home)

- **Identity:** "The Blues" (current, primary; from the consistent blue home kit, in common use by the mid-1960s). "The Pensioners" (historical, from the original crest depicting a Chelsea Pensioner of the nearby Royal Hospital Chelsea; dropped as the primary identity in the early 1950s). Frame "The Pensioners" explicitly as historical. Royal / Chelsea blue is the home identity.
- **Club anchors (evergreen):** founded 10 March 1905; home at Stamford Bridge, in Fulham, west London. ("Home since 1905" is accurate for the club; the ground itself opened 1877 as an athletics venue, so avoid implying the stadium dates to the club's founding.)
- **Rivalries (heritage framing, not current-form):** Arsenal (London title-era rivalry), Tottenham / Spurs (the most fan-felt London rivalry, traced to the 1967 all-London FA Cup final), and historically Leeds United (the heated 1970 FA Cup final). Fulham is a geographic west-London-derby neighbor but not a primary rivalry, so do not overstate it. Never use current-form framing ("battling X for the title this season").
- **Honors (evergreen results, phrase per the naming policy above):** two-time winner of Europe's premier club competition (2012 and 2021) -- use generic Champions League framing; five Premier League titles (Premier League may be named directly). Do not conflate "five Premier League titles" with "six English league titles" (the sixth is a pre-Premier-League 1954-55 First Division title); pick one framing.
- **Brand / IP:** Nike is the CURRENT kit supplier, from 2017-18. TIME-SENSITIVE (do not state as evergreen). Nike is non-adidas, so FIFA / "World Cup" terminology is forbidden by the brand rule, but this is moot for club framing (no national-tournament chrome belongs on a club page anyway).
- **This SKU (II1663-453) is Youth Stadium Home:** replica tier for young fans; parent / young-fan avatar lane (family-passed-down Chelsea loyalty, the young supporter's first real shirt), youth sizing with growth allowance. Stadium (replica) versus Authentic distinction applies as on other Nike Stadium jerseys.

### Club head-term cede policy (added 2026-07-31, Batch 10)

Bare club head terms belong to the club's `/collections/<club>` page, not to any PDP: a searcher on "real madrid jersey" wants the club's full kit range, which is a collection intent by the hierarchy rule, so no PDP takes it. PDPs take model + tier + cut + gender + age qualified terms only. Ceded head terms, recorded in `deliverables/tracking/ceded-terms.csv` and on each collection row's `ceded_from` in `deliverables/tracking/collections-master.csv`:

- **Real Madrid:** `real madrid jersey`, `real madrid soccer jersey` to `/collections/real-madrid`
- **Barcelona:** `barcelona jersey`, `barcelona soccer jersey` to `/collections/barcelona`
- **Liverpool:** `liverpool jersey`, `liverpool soccer jersey` to `/collections/liverpool`
- **Manchester United:** `manchester united jersey`, `manchester united soccer jersey`, `man united jersey` to `/collections/manchester-united`
- **Arsenal:** `arsenal jersey`, `arsenal soccer jersey` to `/collections/arsenal` (added 2026-08-03, Batch 11; `/collections/arsenal` live-verified, 44 products, smart collection on tag `comp_club-team_arsenal`)
- **Bayern Munich:** `bayern munich jersey`, `bayern jersey` to `/collections/bayern-munich` (added 2026-08-03, Batch 11; `/collections/bayern-munich` live-verified, 38 products. Bundesliga club, so the term pair is `bayern munich jersey` + the short-form `bayern jersey`, not the `<club> soccer jersey` shape used for the La Liga / Premier League clubs above.)

Add a club's cede here and to both registry files before its first PDP is assigned a primary, so no PDP reaches for the head term. Real Madrid and Barcelona entered as new lanes in Batch 10; their cedes were written before assignment for exactly this reason. Arsenal and Bayern Munich entered as new lanes in Batch 11, cedes written before assignment.

### Manchester United FC (added 2026-07-13, Batch 8; FIRST United entry, Mike-approved criterion-1 escalation; guardrail approved as-is)

- **Identity:** "The Red Devils" (current / primary; on the crest since 1970). "The Heathens" (historical only, Newton Heath era). "Busby Babes" -- MEMORIAL-SENSITIVE (1958 Munich air disaster); do NOT use decoratively.
- **Anchors (evergreen):** founded 1878 as Newton Heath, renamed Manchester United in 1902; home at Old Trafford (Greater Manchester / Trafford), opened 1910. Write "home at Old Trafford since 1910" or "roots dating to 1878," NEVER "at Old Trafford since 1878" (club predates the ground).
- **Crest / colours:** United red home identity; crest = red devil with a trident + the sailing ship above (Manchester's maritime / trade heritage), safe to describe factually.
- **Rivalries (heritage framing, not current-form):** Liverpool (the North West Derby, principal; inter-city rivalry predating football); Manchester City (the Manchester derby -- usable as heritage, NO current-form given City's recent dominance); Leeds (cross-Pennine Roses rivalry, optional / lower-profile).
- **Honours (evergreen, per the competition-naming policy above):** 13 Premier League titles (Premier League nameable directly). 20 English top-flight titles total = 13 PL + 7 pre-1992 First Division -- keep SEPARATE, do not call all 20 "Premier League." Three-time winner of Europe's premier club competition (1968, 1999, 2008) -- GENERIC only, never name it. FA Cup nameable directly.
- **LOAD-BEARING fabrication bar:** NO "most successful club" / "most titles" / "more than any other" -- Liverpool EQUALLED United at 20 English league titles (2024-25), so it is a JOINT record. Use "one of England's most successful clubs" / "a record 20 English league titles, shared with Liverpool." This bar binds the Liverpool pages symmetrically.
- **Brand / IP:** adidas is the CURRENT supplier (returned 2015-16; TIME-SENSITIVE, not "longtime partner"); 2026-27 is an adidas cycle. No deal figures in copy. Club-IP posture (no FIFA / World Cup chrome on a club page).
- **Internal links:** no live United CURRENT-player collection (the live player collections -- Ronaldo, Pogba, Pique -- are all former players). Use /collections/epl + retired-legend body mentions (Charlton, Best, Cantona, Beckham, Rooney), NOT a current-player link.

### Real Madrid CF (added 2026-07-22, Batch 9; FIRST Real Madrid entry, Mike-approved criterion-1 escalation; first live heritage-jersey run through the claims gate)

- **Identity:** "Los Blancos" (the whites, primary; the all-white home kit is the club's core identity). "the white of Madrid" is approved qualitative shorthand. "Galacticos" usable as a historical-era reference, not current-squad framing.
- **Anchors (evergreen):** founded 1902; home at the Santiago Bernabeu, Madrid, the Spanish capital. Founding date 1902 traces to web/identity verification (Layer 3), not bare-asserted; omit if not load-bearing.
- **Crest / colours:** all-white home identity; the 2026-27 adidas kit draws detailing from the "diamonds and pearls of the crown" with a darker green on sleeves/collar (scrape-sourced design tribute; safe to describe factually).
- **LOAD-BEARING claims bar (the RM trap):** NO European Cup / continental count ("15 European Cups", "15-time European champions") -- overtakeable, hits `heritage-count` FAIL. NO "most successful club" / "most decorated" / "more than any other" -- hits `heritage-superlative` FAIL. NO La Liga title count (e.g. "36 La Liga titles"). Default to QUALITATIVE: "Europe's most storied club", "a European pedigree few can rival", "the white of Madrid", "a fixture at the sharp end of La Liga", "a regular on Europe's biggest nights."
- **Competition naming:** La Liga NAMEABLE directly (plain descriptive fact, same basis as Premier League). European Cup / Champions League -> GENERIC only ("Europe's biggest nights", "the continental stage"), never named. PDP sells a "Champions League Patch Set" add-on -- a site product option, NOT license to name the competition in copy.
- **Brand / IP:** adidas is the CURRENT supplier; 2026-27 is an adidas cycle (time-sensitive). Club-IP posture: no FIFA / World Cup chrome on a club page. (adidas's FIFA permission is a specific 2026 World Cup license, event-scoped and past-tense; it does not apply to club pages at all.) No deal figures.
- **Internal links:** /collections/real-madrid (live, map-confirmed) + Stadium-vs-Authentic sibling cross-links.
- **Avatar:** Stadium = replica = Carlos/Fan (city + Bernabeu heritage, passed-down loyalty). Authentic tier is the on-pitch upsell.

## Claimed patterns log

### SKU (not recorded; pre-SKU-first naming) Nike Liverpool Men's Stadium Away 2024-25 [backfilled 2026-07-08; the club silo's first shipment]
- Brief: `deliverables/page-optimizations/2026-05-26_session-01/nike-2024-25-liverpool-mens-stadium-away-jersey_brief-v2.md` (commit b7159dc; shipped 2026-05-26, before Registry 2 existed; backfilled 2026-07-08). SKU not captured in the v2 brief (pre-SKU-first naming); identify from the white-label sheet if a re-run is needed.
- Date: 2026-05-26 (shipped) / 2026-07-08 (backfilled)
- Opening hook approach: the traveling supporter on the road ("for the Anfield supporter on the road in any city"); the away-end / away-day identity moment
- Primary metaphor: "the title kit" -- the shirt a title was won in, a season's record you can wear; club-memory / supporter identity, deliberately NOT an athletic-performance metaphor
- Use case scenario: the Liverpool supporter buying the Stadium (replica) away shirt to wear on the road, in the away end, and on the high street
- Angle of emphasis: the Stadium (replica) tier versus Authentic; the away Night Forest colorway; the season-record narrative (the title-winning debut campaign); and the Hillsborough eternal-flames tribute detail
- Heritage angle: the Liver Bird crest; the Hillsborough 97 eternal-flames tribute (crossed torches, the 97 numerals); the debut-season title that equaled the all-time English league-title record; and Nike's farewell as supplier before the club moved to adidas from 2025-26

### SKU II1663-453 (Nike Chelsea Youth Stadium Home 2026-27) [Batch 6, first club under Registry 2]
- Brief: `deliverables/page-optimizations/2026-07-08_session-01/II1663-453_nike-2026-27-chelsea-youth-stadium-home_brief.md` (commit f6c3f76)
- Date: 2026-07-08
- Opening hook approach: parent / young-fan; the kid who chose Chelsea (passed down or through their own hero) getting the home blue that makes it official
- Primary metaphor: club belonging claimed or passed down (the young Blue); distinct from national-pride jersey lanes AND from Liverpool's "title kit" away lens
- Use case scenario: a parent buying the youth home Stadium shirt for a young Chelsea fan; youth sizing with growth; watch party and wearing to play
- Angle of emphasis: youth club loyalty plus the Stadium (replica) tier; Premier League named directly, Champions League as generic "two-time European champions"
- Heritage angle: The Blues; Stamford Bridge (Fulham, west London), founded 1905; royal blue; five Premier League titles; Nike supplier; Cole Palmer player-spotlight internal link

### SKU KA6852 (adidas Liverpool Men's Stadium Home 2026-27) [Batch 8; Liverpool adidas-HOME lane, avatar-split set 1 of 4]
- Brief: `deliverables/page-optimizations/2026-07-13_session-01/KA6852_adidas-2026-27-liverpool-mens-stadium-home-soccer-jersey_brief.md`
- Date: 2026-07-13
- Avatar / lane: flagship ADULT supporter (own your own home red)
- Opening hook: "Some shirts you wear. This one you belong to" -- adult belonging, the Kop, matchday
- Primary metaphor: the home shirt as the supporter's own colors; the '80s-inspired Shankly-red graphic threading eras
- Angle: primary `liverpool home jersey`; slim/crew; scrape-confirmed Shankly-red '80s graphic; internal link /collections/epl
- Heritage: Anfield since 1892, the Kop, Liver Bird, YNWA, Shankly (all-red 1964), Gerrard/Dalglish; joint-20 (not asserted); European = generic; adidas reunion 2025-26; Hillsborough respectfully omitted

### SKU KB8255 (adidas Liverpool Youth Stadium Home 2026-27) [Batch 8, set 2 of 4]
- Brief: `deliverables/page-optimizations/2026-07-13_session-01/KB8255_adidas-2026-27-liverpool-youth-stadium-home-soccer-jersey_brief.md`
- Date: 2026-07-13
- Avatar / lane: parent-buys-for-kid ("first proper Reds shirt," handed-down loyalty, grow-into-it)
- Primary metaphor: loyalty passed a generation; the shirt as inheritance and beginning
- Angle: primary `liverpool youth jersey`; regular youth fit; name/number customization (scrape-confirmed for LFC youth); /collections/epl
- Heritage: same LFC anchors, parent-facing; Hillsborough fully out of the warm copy

### SKU KB8256 (adidas Liverpool Women's Stadium Home 2026-27) [Batch 8, set 3 of 4]
- Brief: `deliverables/page-optimizations/2026-07-13_session-01/KB8256_adidas-2026-27-liverpool-womens-stadium-home-soccer-jersey_brief.md`
- Date: 2026-07-13
- Avatar / lane: women's-cut supporter ("cut for her," tailored fit, "you're a Red, full stop"); Croatia-women's split pattern
- Primary metaphor: the tailored fit that belongs to her; the '80s Shankly-red graphic + sleeve print
- Angle: primary `liverpool women's jersey`; women's regular/crew; safe honours claim used ("England's most successful side in Europe's premier competition"); /collections/epl. NEAR-SOLD-OUT (1 left)

### SKU KB8268 (adidas Liverpool Men's Home Long-Sleeve 2026-27) [Batch 8, set 4 of 4]
- Brief: `deliverables/page-optimizations/2026-07-13_session-01/KB8268_adidas-2026-27-liverpool-mens-home-long-sleeve-soccer-jersey_brief.md`
- Date: 2026-07-13
- Avatar / lane: long-sleeve supporter (full-sleeve, V-neck, cold-terrace/winter, "some supporters wait for the long sleeve")
- Primary metaphor: the long-sleeve as the season-spanning cut; V-neck classic silhouette
- Angle: primary `liverpool long sleeve jersey` (strongest LFC term, 1,300/mo); slim/V-neck; joint-20 stated correctly ("level with Manchester United"); European = "six European crowns" generic; /collections/epl

### SKU KA6871 (adidas Manchester United Men's Stadium Home 2026-27) [Batch 8; United-lane EXEMPLAR, avatar-split set 1 of 3]
- Brief: `deliverables/page-optimizations/2026-07-13_session-01/KA6871_adidas-2026-27-manchester-united-mens-home-soccer-jersey_brief.md`
- Date: 2026-07-13
- Avatar / lane: flagship ADULT supporter; "the red you wear to say which side you're on" (United owns this open; siblings differ)
- Primary metaphor: the home red as belonging; striped red/white/black design + devil-and-ship crest
- Angle: primary `manchester united home jersey`; slim/striped polo collar; scrape-confirmed striped red/white/black; /collections/epl
- Heritage: Old Trafford 1910/roots 1878, Red Devils, devil-and-ship; "among England's most successful," record 20 shared with Liverpool; European = generic "European nights"; FA Cup named; adidas current; retired legends Charlton/Best/Cantona/Beckham/Rooney (no current-player link)

### SKU KC4796 (adidas Manchester United Youth Stadium Home 2026-27) [Batch 8, set 2 of 3]
- Brief: `deliverables/page-optimizations/2026-07-13_session-01/KC4796_adidas-2026-27-manchester-united-youth-home-soccer-jersey_brief.md`
- Date: 2026-07-13
- Avatar / lane: parent-buys-for-kid ("first proper Red Devils shirt," handed-down); DIFFERENT anchor than the exemplar
- Angle: primary `manchester united youth jersey`; regular youth fit; NO name/number customization (not scrape-confirmed for this SKU); joint-20 shared with Liverpool; /collections/epl

### SKU KC4773 (adidas Manchester United Men's Home Long-Sleeve 2026-27) [Batch 8, set 3 of 3]
- Brief: `deliverables/page-optimizations/2026-07-13_session-01/KC4773_adidas-2026-27-manchester-united-mens-home-ls-soccer-jersey_brief.md`
- Date: 2026-07-13
- Avatar / lane: long-sleeve + the scrape-confirmed 1976/77 FA Cup 50th-anniversary striped-collar tribute; plain "Mufc Red" base (contrast vs the SS striped body)
- Angle: primary `manchester united long sleeve jersey` (880/mo, strongest United term); slim/LS; FA Cup named directly (opponent not foregrounded); joint-20; /collections/epl
