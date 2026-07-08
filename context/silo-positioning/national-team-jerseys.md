# Silo Positioning: National Team Jerseys

Per-SKU prose patterns claimed in shipped briefs for national-team jersey PDPs. Unlike the cleat silos (named by base model line), this silo is keyed by **product class**, not brand: jerseys collide on the shared fan / matchday / national-pride / tournament-cycle prose lane regardless of kit supplier, and each nation is single-brand per cycle (Croatia = Nike, Mexico = adidas, and so on), so a brand-keyed file would scatter unrelated nations. Product-class taxonomy is also durable against kit-supplier changes between cycles. Taxonomy confirmed by Mike 2026-06-10. Format and append protocol: see `README.md`. ORIN reads this file during the pre-dispatch differentiation pass and appends after each batch commits.

Note: club-team jerseys (Real Madrid, Barcelona, etc.) sit in a distinct prose lane (club identity vs national pride) and will get their own silo file (`club-team-jerseys.md`) when that work first batches.

## Pre-dispatch reference / guardrails

Reference notes ORIN reads at the pre-dispatch differentiation pass. Separate from the append-only per-SKU log below.

### Bosnia and Herzegovina (added 2026-06-29, from ORIN research for Batch 5 youth Home + Away)
- **Identity:** "Zmajevi" (The Dragons), applied to the national teams generally, gender-neutral in practice. NO documented women's-specific nickname; do NOT coin "Zmajice." Secondary heritage name: "Zlatni Ljiljani" (Golden Lilies, the fleur-de-lis / golden-lily crest). Kid-friendly dragon imagery is a clean youth hook.
- **Evergreen heritage anchor:** "2014 World Cup debut" (Brazil; first World Cup win 3-1 over Iran). **Do NOT use "first/only World Cup"**: Bosnia qualified for 2026, so "only" is now false. Never appeared at a UEFA Euro through 2024 (evergreen).
- **Colors / motif:** royal/cobalt blue primary + yellow/gold; diagonal row of white stars (flag-derived); golden-lily heritage emblem. Home = blue dominant; away base varies by cycle.
- **Federation:** Football Association of Bosnia and Herzegovina (N/FSBiH); FIFA code BIH; FIFA + UEFA member.
- **Brand / IP:** kit supplier is **Kelme**, TIME-SENSITIVE (not a permanent identity, do not state as evergreen). Kelme is a non-adidas brand, so FIFA / World Cup terminology is FORBIDDEN on these PDPs (federation / cycle language only, mirrors the Nike-Croatia discipline). See `context/brand-ip-constraints.md`.
- **Youth/parent angle:** Bosnian-diaspora heritage pride (large US communities); the jersey as homeland connection, not results-fandom. Keeps framing evergreen.
- Player associations (Dzeko, Pjanic, Begovic) are historical; any active/retired status is TIME-SENSITIVE, avoid current-squad claims.

### Jamaica (added 2026-07-08, from ORIN research for Batch 6 adidas Authentic Away)
- **Identity:** "Reggae Boyz" is the MEN's team nickname (picked up on a 1995 Zambia visit). The women's team is "Reggae Girlz." Use Reggae Boyz for this men's kit; do not apply it to the women's team.
- **Colors / motif:** green, black, gold, drawn from the Jamaican flag (green = land and hope, gold = sunlight and natural wealth, black = the strength and creativity of the people). Evergreen flavor anchor: Jamaica's is one of only two national flags with no red, white, or blue (the other is Mauritania).
- **Federation:** Jamaica Football Federation (JFF, est. 1910); CONCACAF (Caribbean Football Union); FIFA code JAM.
- **Evergreen heritage anchor:** the France 1998 DEBUT (first English-speaking Caribbean nation to qualify) and the 2-1 win over Japan on 26 June 1998 in Lyon, Theodore Whitmore scoring both goals. Gold Cup runner-up in 2015 and 2017.
- **FORBIDDEN: "only World Cup" / "only appearance."** Jamaica did NOT directly qualify for 2026 and sits in the inter-confederation playoff (unresolved), so "only" is falsifiable. Use "debut" / "their first World Cup appearance, at France 1998."
- **Brand / IP:** adidas is the CURRENT supplier (January 2023 through the 2026 cycle, replacing Umbro). TIME-SENSITIVE. adidas is the FIFA commercial licensee, so FIFA / World Cup terminology IS permitted on this PDP. The tournament-status evergreen discipline still applies: no "chasing the trophy," no "qualified for 2026," no live-bracket framing.
- **Tier:** this SKU is Authentic (match-spec). adidas Authentic = HEAT.RDY, tighter player fit, heat-pressed badges; Stadium (replica) = AEROREADY doubleknit, regular fan fit, embroidered badges. Do not combine tier words ("Authentic Stadium"). Verify the specific spec from the SKU's Phase 0 scrape (scrape-wins).

### DR Congo (added 2026-07-08, from ORIN research for Batch 6 Umbro Authentic Home + Away)
- **Identity:** "Les Léopards" (The Leopards), applied to the team generally. The women's team is "Léopards dames" -- do NOT coin a new women's variant. Lower-confidence secondary men's names exist ("La Céleste" / The Skyblue, "Guerriers de l'Équateur"); use with care.
- **Colors / motif:** sky-blue field with gold and red flag accents (the DRC flag is sky blue with a red diagonal stripe bordered yellow and a yellow star). The sky-blue/gold/red palette is evergreen; a specific kit's design is cycle-dependent, so verify the SKU's design from its Phase 0 scrape (scrape-wins).
- **Federation:** Fédération Congolaise de Football-Association (FECOFA); CAF; FIFA code COD (FIFA displays the team as "Congo DR").
- **Evergreen heritage anchors:** two AFCON titles, 1968 (as Congo-Kinshasa, 1-0 over Ghana) and 1974 (as Zaire); and the 1974 finals appearance as Zaire.
- **Brand / IP:** Umbro is the CURRENT supplier (documented back to the 2022/24 cycle; exact contract start not verified, so use "current Umbro kits," not a hard start year). TIME-SENSITIVE. Umbro is non-adidas, so FIFA / "World Cup" terminology is FORBIDDEN (cycle language only), the same discipline as Kelme and Nike. Even historical "World Cup" references use substitution: write "the 1974 finals as Zaire," not "1974 World Cup," on this Umbro page.
- **Tournament note:** DR Congo qualified for the 2026 finals (beat Jamaica 1-0 after extra time on 31 March 2026, a settled fact). On an Umbro page this may surface ONLY via neutral substitution ("sealed their place in the 2026 international tournament," "the 2026 cycle"), never "World Cup." Evergreen-default framing still applies; do not manufacture live-bracket chrome.

### Korea (South Korea / Korea Republic) (added 2026-07-08, from ORIN research for Batch 6 Nike Stadium Home)
- **Identity:** "Taegeuk Warriors" (태극전사), also "the Reds" and "Tigers of Asia," applied to the team generally. No verified women's-specific nickname, so do NOT assert one. FIFA registers the team as "Korea Republic."
- **Colors:** red primary heritage (source of "the Reds"); white and blue secondary (away and crest). The taegeuk (the red-and-blue flag symbol of balance and harmony) is the identity anchor.
- **Federation:** Korea Football Association (KFA); AFC (and the regional EAFF); FIFA code KOR.
- **Evergreen heritage anchors:** the 2002 fourth-place semi-final run on home soil (beat Italy and Spain en route; first team from outside Europe and the Americas to reach that stage); and back-to-back AFC Asian Cup titles in 1956 and 1960 (do not imply a recent Asian Cup title; there has been none since 1960). For consistency, phrase as "one of Asia's most consistent qualifiers" or "a decades-long run of appearances"; do NOT hard-code a consecutive-appearance count (it changes).
- **Brand / IP:** Nike is the CURRENT supplier (listed since 1996). TIME-SENSITIVE (frame as a "long-standing Nike partnership," not an evergreen fact). Nike is non-adidas, so FIFA / "World Cup" terminology is FORBIDDEN (cycle language only). The 2002 result is a historical anchor described without the FIFA / "World Cup" wordmark: write "the 2002 tournament on home soil" or "their semi-final run," not "2002 World Cup," on this Nike page.

## Claimed patterns log

### SKU J000693-CRFT (Nike Croatia Men's Stadium Away 2026)
- Brief: `deliverables/page-optimizations/2026-06-10_session-01/nike-2026-croatia-mens-stadium-away-soccer-jersey_brief.md` (Batch 2, first jersey under the new architecture)
- Date: 2026-06-10
- Opening hook approach: the fan / matchday identity moment, pulling on the deep blue away shirt and being "Croatian for the summer"
- Primary metaphor: belonging / national identity (the anthem-moment supporter feeling); deliberately NO athletic-performance metaphor
- Use case scenario: the Croatia supporter buying the replica away shirt to wear through the summer tournament cycle (watch party, bar, stadium, casual)
- Angle of emphasis: national pride plus the Stadium (replica) tier and the distinct away colorway
- Heritage angle: Croatia's red-and-white checkerboard (sahovnica) rendered in deep royal blue; Nike as Croatia's 2026 (and final) kit supplier before adidas takes over

### SKU J000691-CRFT (Nike Croatia Women's Stadium Home 2026) [Batch 4, women's-cut precedent]
- Brief: `deliverables/page-optimizations/2026-06-17_session-01/J000691-CRFT_nike-2026-croatia-womens-stadium-home-soccer-jersey_brief.md`
- Date: 2026-06-17
- Opening hook approach: the female fan / player identity; "cut for her, not borrowed off the men's rack" -- the women's-cut matchday moment
- Primary metaphor: national pride through a women's lens (the women's-cut identity); deliberately NOT J000693's anthem-moment belonging
- Use case scenario: the female Croatia supporter or player buying the women's-cut HOME shirt for the 2026 cycle (watch party, stadium, casual)
- Angle of emphasis: women's-cut fit (the precedent this sets), the HOME red-and-white sahovnica colorway, the Stadium (replica) tier; evergreen heritage only (no current-events / squad / qualifying claims); gender/team-neutral references ("Croatia" / "the national team", NOT "Vatreni" which is the men's-team nickname)
- Heritage angle: Croatia's red-and-white checkerboard (sahovnica) home identity, from the medieval coat of arms, Sutej 1990; Nike as Croatia's 2026 (and final) kit supplier before adidas takes over

### SKU J000695-CRFT (Nike Croatia Youth Stadium Away 2026) [Batch 4, youth-away precedent]
- Brief: `deliverables/page-optimizations/2026-06-17_session-01/J000695-CRFT_nike-2026-croatia-youth-stadium-away-soccer-jersey_brief.md`
- Date: 2026-06-17
- Opening hook approach: parent-facing; the away kit for your young Croatia fan / youth player
- Primary metaphor: parent / young-fan identity (NOT the adult-fan identity of J000693, NOT the women's-cut identity of J000691)
- Use case scenario: the parent shopping the away kit for a young supporter or youth player; youth sizing YXS-YXL with growth allowance
- Angle of emphasis: youth sizing + growth + durability; the AWAY deep-royal-blue colorway (shares the away color with J000693 men's away, differentiated by the parent/youth lens and age); evergreen and team-neutral; NON-FIFA cycle language (Nike)
- Heritage angle: the sahovnica checkerboard rendered in away royal blue; Nike as Croatia's 2026 (and final) kit supplier before adidas takes over

### SKU J000692-CRFT (Nike Croatia Youth Stadium Home 2026)
- Brief: `deliverables/page-optimizations/2026-06-30_session-01/J000692-CRFT_..._brief.md` (commit a34c7d6, Batch 5; youth-home precedent)
- Date: 2026-06-30
- Opening hook approach: the one your kid points at first; parent / young-fan, the HOME shirt
- Primary metaphor: parent / young-fan identity, the look the world knows Croatia by (NOT J000695's away "flip it to blue" lens)
- Use case scenario: parent buying the HOME youth jersey for a young Croatia fan; on-page Modric 10 customization option
- Angle of emphasis: youth HOME red-and-white sahovnica; Stadium tier; the Modric 10 customization angle (sibling pages did not use); evergreen, team-neutral; Nike non-FIFA cycle language only
- Heritage angle: red-and-white sahovnica from the national coat of arms (evergreen; "Vatreni"/"Kockasti" avoided)

### SKU J000694-CRFT (Nike Croatia Women's Stadium Away 2026)
- Brief: `deliverables/page-optimizations/2026-06-30_session-01/J000694-CRFT_..._brief.md` (commit a34c7d6, Batch 5; women's-cut away precedent)
- Date: 2026-06-30
- Opening hook approach: reach past the red-and-white, the away crowd, on the road
- Primary metaphor: women's-fan away identity through the gender umbrella (NOT J000691's "cut for her, not borrowed off the men's rack" home lens)
- Use case scenario: female Croatia supporter or player buying the women's-cut AWAY shirt for the 2026 cycle
- Angle of emphasis: women's-cut AWAY royal-blue; gender-umbrella primary `women's croatia jersey`; Stadium tier; evergreen, gender/team-neutral
- Heritage angle: the sahovnica checkerboard in away royal blue (evergreen; "Vatreni"/"Lavice" avoided per the women's-cut-replica precedent)

### SKU 7651TX3926 (Kelme Bosnia and Herzegovina Youth Stadium Home 2026) [Batch 5, first Bosnia / first Kelme, exemplar]
- Brief: `deliverables/page-optimizations/2026-06-30_session-01/7651TX3926_..._brief.md` (commit 812b613, Batch 5 Wave 1 exemplar)
- Date: 2026-06-30
- Opening hook approach: there's a kid in your house who claims Bosnia as their own and wants the shirt to prove it
- Primary metaphor: parent / young-fan homeland-heritage identity (diaspora pride), the kid-friendly Dragons hook
- Use case scenario: parent buying the HOME youth jersey for a young Bosnian-diaspora fan
- Angle of emphasis: youth HOME blue; Zmajevi (The Dragons) gender-neutral; golden lily; Kelme (non-FIFA) cycle language only; evergreen
- Heritage angle: Zlatni Ljiljani golden lily / fleur-de-lis, blue + flag white stars, the 2014 World Cup debut (3-1 over Iran) as the evergreen anchor (never "first/only WC")

### SKU 7651TX3927 (Kelme Bosnia and Herzegovina Youth Stadium Away 2026) [Batch 5, youth-away sibling]
- Brief: `deliverables/page-optimizations/2026-06-30_session-01/7651TX3927_..._brief.md` (commit a34c7d6, Batch 5)
- Date: 2026-06-30
- Opening hook approach: the kid who wants the other one, the away shirt
- Primary metaphor: parent / young-fan away-shirt identity (distinct from the Home exemplar's "claims Bosnia as their own")
- Use case scenario: parent buying the AWAY youth jersey for a young Bosnia fan (sizing YL and YXL only per scrape)
- Angle of emphasis: youth AWAY White/Navy (scrape-confirmed, not blue); Zmajevi (The Dragons); Kelme (non-FIFA) cycle language only; evergreen
- Heritage angle: Zlatni Ljiljani golden lily heritage emblem, away white/navy, the 2014 World Cup debut as the evergreen anchor
