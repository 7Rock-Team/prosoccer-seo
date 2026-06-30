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
