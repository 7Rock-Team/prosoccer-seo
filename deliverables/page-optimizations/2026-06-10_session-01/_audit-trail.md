# Audit Trail -- Batch 2 / 2026-06-10_session-01

## Batch Metadata
- Total SKUs: 10 (across 3 categories, 2 brand-IP classes)
- Categories: 8 adidas F50 footwear (cleats/turf/indoor), 1 Nike cleat (Mercurial Vapor 17 Pro FG), 1 Nike jersey (Croatia Men's Stadium Away)
- Brand IP classifications: Nike SKUs (#1 IO8225-900, #2 J000693-CRFT) = FIFA/World Cup terminology FORBIDDEN; adidas SKUs (#3-10, all F50) = FIFA/World Cup terminology PERMITTED (adidas is FIFA licensee)
- Care and Maintenance H2: triggered on ALL 10 (footwear x9 + jersey x1)
- Dispatch architecture: exemplar-first (JR5386) then 9 parallel SCRIBE; one SKU per agent; lane spec + structure skeleton + forbidden-phrasings handoff (NOT exemplar prose)
- Silos: mercurial.md (#1, differentiate vs 4 Batch 1 entries), f50.md (#3-10, empty scaffold -> 8 entries), national-team-jerseys.md (#2, NEW silo file -- taxonomy pending Mike confirm at gate)
- First production batch under full new architecture (commits 3fb0501, 21afdb5, 990de86, 3893e70, 83d9855, b7a00e0)
- Commit hash: [pending]

## KIRA keyword assignments (approved by Mike 2026-06-10; 100/mo floor w/ GSC override)

| # | SKU | Primary KW | Vol/mo | Floor | Notes |
|---|---|---|---|---|---|
| 1 | IO8225-900 | nike mercurial vapor 17 pro | 10 | sub-floor (GSC override, pos 8 live) | Pro tier; differentiate from Batch 1 Elite-tier Vapor FG |
| 2 | J000693-CRFT | croatia jersey 2026 | 390 | clears | pos 4.4 / 58 impr / 1 click; year-specific |
| 3 | JR5386 | adidas f50 elite | 6,600 | clears | EXEMPLAR; owns bare tier term (Option A ratified) |
| 4 | KJ6080 | adidas f50 elite laceless | 1,600 | clears | pos 3 live; laceless separates from #3 |
| 5 | IH9375 | adidas f50 club | 210 | clears | entry tier, unique in batch |
| 6 | IH9345 | adidas f50 pro | 1,600 | clears | Pro FG cleat; watch bleed vs #9 |
| 7 | IH4582 | adidas f50 league turf | 70 | sub-floor (GSC override, pos 1.9 live) | League+Turf unique lane |
| 8 | IH4571 | adidas f50 indoor | 320 | clears | only indoor SKU |
| 9 | IH4567 | adidas f50 turf | 720 | clears | Pro Turf routed up to generic turf; watch bleed vs #6 |
| 10 | KJ6714 | adidas f50 league | 880 | clears | League Mid FG; surface separates from #7 |

Cross-SKU arbitration (ratified): turf/pro split #6 `f50 pro` (FG cleat) / #7 `f50 league turf` / #9 `f50 turf`; Elite split #3 `f50 elite` (laced) / #4 `f50 elite laceless`. SCRIBE holds each page to its assigned lane; siblings link UP to `/collections/adidas-f50` + `/collections/adidas-road-to-glory-pack`, never cross-target.

Cannibalization guardrails (collection-owned, do NOT target as PDP primary): `adidas f50`, `adidas road to glory soccer cleats`, `nike breakout soccer cleats`, `croatia soccer jersey`/`croatia jersey` (head terms -> /collections/croatia), category giants.

## ORIN pre-dispatch differentiation lanes (each SKU: angle / hook / heritage / use case / metaphor direction)

Sharp differentiation required: the 8 F50 SKUs share one model (F50 Hyperfast, Road to Glory pack). Differentiation axes available: tier (Elite/Pro/League/Club), lacing (laced/laceless), surface (FG/MG/turf/indoor), collar (standard/mid). Metaphors must be mutually distinct AND distinct from Batch 1 Mercurial metaphors (sprinter-from-blocks, boxer footwork, cinder-to-synthetic-track sprinter, slalom skier) -- avoid sprinter/track/boxer/skier framings.

### #3 JR5386 -- F50 Hyperfast Elite FG (EXEMPLAR)
- Angle: the pinnacle speed build; pure top-end velocity, the flagship of the line
- Hook: the moment of breaking the last line -- ball played through, the Elite player gone before the defense turns
- Heritage: F50 as adidas' speed lineage (the boot of the fastest attackers); Elite = the pro-level build, lightest plate, full speed package; Road to Glory = the 2026 cycle pack (World Cup terms PERMITTED)
- Use case: the elite-level attacker on dry natural grass in top competition who wins with raw pace
- Metaphor direction: a thoroughbred at full gallop on the open straight (bred for one thing -- speed). SCRIBE writes its own; this is the seed.

### #4 KJ6080 -- F50 Hyperfast Elite Laceless FG
- Angle: the clean, unbroken strike surface; precision through the laceless forefoot
- Hook: the first-touch / strike moment where nothing sits between foot and ball
- Heritage: adidas laceless engineering lineage; Elite-tier laceless = the purest connection adidas builds
- Use case: the elite striker/playmaker who values a flush strike surface and a locked, sock-like fit on grass
- Metaphor direction: a seamless/frictionless surface -- a stone skipping clean water (no notch, no catch). Distinct from #3's velocity framing.

### #5 IH9375 -- F50 Hyperfast Club FG/MG
- Angle: accessible F50 speed + multi-surface versatility; one cleat for wherever the game is
- Hook: the player who plays on whatever pitch is open -- grass one night, synthetic the next
- Heritage: F50 speed DNA brought to the Club (entry) tier; the FG/MG plate's surface range
- Use case: the developing or budget-conscious player who needs one versatile cleat across grass and synthetic
- Metaphor direction: an all-terrain build / one tool that adapts to many grounds. Distinct from speed-purist framings.

### #6 IH9345 -- F50 Hyperfast Pro FG
- Angle: near-elite speed tech for the committed competitor grinding the full season on grass
- Hook: the weekly grind -- the player living the league season, not the highlight reel
- Heritage: F50 speed build at the Pro tier; the performance package a half-step below Elite
- Use case: the serious competitive player who wants the F50 speed game on firm ground at a Pro-tier value
- Metaphor direction: a tuned production performance car (vs #3's race-bred thoroughbred) -- real speed, daily-driven. Hold to FG-cleat lane (do not drift to turf -- that is #9).

### #7 IH4582 -- F50 Hyperfast League Turf
- Angle: F50 speed tuned for the turf surface you actually train and play on, at League value
- Hook: the weeknight turf session under the lights; the surface most players live on
- Heritage: F50 speed translated to a turf-specific outsole; League tier
- Use case: the player whose home surface is turf -- training grounds, small-sided leagues, 3G pitches
- Metaphor direction: the right tire compound for a specific track surface (traction matched to ground). Hold to League+turf lane (distinct from #9 Pro turf and #10 League FG).

### #8 IH4571 -- F50 Hyperfast Pro Indoor
- Angle: F50 speed compressed into the tight, fast indoor/futsal court game
- Hook: the close-quarters indoor moment -- the one-touch give-and-go in a phone booth of space
- Heritage: F50 speed brought to the flat indoor-court sole; Pro tier
- Use case: the futsal / indoor-court player who wins with quick feet in tight space
- Metaphor direction: a squash player's split-step in a tight court (compressed, reactive quickness). Distinct from agility metaphors used elsewhere.

### #9 IH4567 -- F50 Hyperfast Pro Turf
- Angle: F50 Pro-tier speed gripping the synthetic turf surface
- Hook: the cutback and burst on a grippy turf pitch where the studs bite synthetic
- Heritage: F50 speed at Pro tier on a turf outsole; the synthetic-surface speed game
- Use case: the pro-level player whose competitive surface is turf and who wins with pace
- Metaphor direction: a rally car gripping a fast gravel stage (speed on a grippy artificial surface). Hold to generic-turf primary (`adidas f50 turf`); distinct from #7 League turf framing.

### #10 KJ6714 -- F50 Hyperfast League Mid FG
- Angle: the mid-cut collar lockdown; speed with a secured ankle on grass
- Hook: the locked-in feel through a hard sprint -- the collar holding the ankle as the player accelerates
- Heritage: F50 speed at League tier with the mid-cut collar; the supported-ankle build
- Use case: the player who wants ankle containment / the sock-collar feel through fast direction changes on firm ground
- Metaphor direction: a climber's high-cut boot / a gauntlet securing the joint (lockdown + support). Distinct from low-cut speed framings.

### #1 IO8225-900 -- Nike Mercurial Vapor 17 Pro FG (BRAND IP: FIFA FORBIDDEN)
- Angle: the Vapor agility game (close-control burst, change of direction in tight space) at the Pro tier -- near-Elite agility for the committed player
- Hook: the cut in traffic -- escaping a marker in a crowded pocket (must NOT reuse Batch 1 Vapor Elite "stutter/dropped-shoulder/slip-out" hook)
- Heritage: the Vapor agility lineage within Nike's Mercurial line; the Pro build a step below the Elite's full AtomKnit/FlyLite package
- Use case: the attacking mid / winger who wins in tight space on grass and wants the Vapor agility game at Pro-tier value
- Metaphor direction: a pickpocket's sleight of hand (quick, deceptive, close-quarters) -- DISTINCT from Batch 1 Vapor Elite (boxer slipping a punch) and Superfly Elite (sprinter from blocks). Brand IP: zero FIFA/World Cup terms; allowed cycle/era language only ("the 2026 cycle", "summer matches").

### #2 J000693-CRFT -- Nike Croatia Men's Stadium Away Jersey 2026 (BRAND IP: FIFA FORBIDDEN; FIRST JERSEY under new architecture)
- Angle: national pride + matchday/fan identity; the Stadium (replica) tier for the supporter wearing the away colorway
- Hook: the fan/matchday moment -- wearing the checkerboard away kit, the identity of supporting Croatia in the 2026 cycle
- Heritage: Croatia's iconic red-and-white checkerboard (sahovnica); Nike as Croatia's 2026 kit supplier; the away colorway's distinct identity
- Use case: the Croatia supporter / fan buying the replica away shirt to wear for the summer tournament cycle
- Metaphor direction: jersey-appropriate (identity/belonging, not athletic-performance metaphor). Brand IP: zero FIFA/World Cup terms -- use "2026 cycle" / "championship summer" / "summer tournament cycle". Stadium = replica tier (do NOT combine tier words like "Authentic Stadium"). Care H2 = jersey care guidance (cold wash, inside-out, no softener, badge care). FLAG jersey playbook gaps at gate (deferred to post-batch codification per Mike).

## Per-SKU Audit Notes

Common to all: eligibility = Mike-verified at batch submission 2026-06-10; complexity = Complex; Care H2 present; FAQ = H2 "Frequently Asked Questions" + H3-per-question + paragraph (Gate 15 PASS); internal links in Description body only, zero in Short Desc; voice_check PASS per SCRIBE. Source provenance per SKU: Firecrawl PDP scrape + collection-validation scrapes 2026-06-10 + scoped Tavily; DataForSEO SERP where noted.

### JR5386 -- adidas F50 Hyperfast Elite FG (EXEMPLAR)
- Primary `adidas f50 elite` (6,600) across Title/Meta/Short/body; supporting `f50 elite` (5,400). Collection-owned heads not targeted (linked up).
- Brand IP: adidas, World Cup PERMITTED (used 2x). PASS. Internal links: /collections/adidas-f50 (32 products, title-validated) + /collections/adidas-road-to-glory-pack (70 products) -- content-validated. Handle 76 chars >70 (forward-only flag).
- Uniqueness: hook = back-line slip; metaphor = thoroughbred on the open straight; closing = "knock the ball into space and go".
- Gate: ORIN trimmed Care 87->54 words + light Fit trim -> body ~446 (<=450). PASS.

### KJ6080 -- adidas F50 Hyperfast Elite Laceless FG
- Primary `adidas f50 elite laceless` (1,600, pos 3 live); supporting `f50 laceless` (3,600). PASS brand IP (World Cup used). Links validated (108 / 33 products). Handle 85 >70 (flag).
- Uniqueness: hook = first-touch clean strike surface; metaphor = flat stone skimmed across still water; H2s "When nothing sits between..." / "adidas took the laces out on purpose" / "A flush panel on dry grass".
- Gate fix: Short Desc opener changed from "The ball comes in..." (collided with exemplar "The ball slips...") to "Your first touch..." Body 484 -- see word-count concern.

### IH9375 -- adidas F50 Hyperfast Club FG/MG
- Primary `adidas f50 club` (210); supporting `adidas f50 hyperfast` (260). PASS brand IP. Links validated (108 / 33). Handle 81 >70 (flag). og:image http:// noted (Misha).
- Uniqueness: hook = "Grass on Tuesday, synthetic Thursday"; metaphor = all-terrain tool; H2#2 retitled by ORIN to "The speed line, made affordable".

### IH9345 -- adidas F50 Hyperfast Pro FG
- Primary `adidas f50 pro` (1,600, pos 9.6 live); supporting `f50 pro` (1,300). Lane held to FG (no turf drift; FAQ redirects turf intent to IH4567). PASS brand IP. Links validated (89 / 133). Handle 74 >70 (flag).
- Uniqueness: hook = "chasing promotion, a cup run"; metaphor = tuned production car (vs race-bred Elite); H2#2 "F50 speed, tuned for the long haul" (sole retained "F50 speed" opener).

### IH4582 -- adidas F50 Hyperfast League Turf
- Primary `adidas f50 league turf` (70, sub-floor, GSC override pos 1.9 live); turf-shoe lane (not "cleats"). Held off generic `adidas f50 turf` (reserved for IH4567). PASS brand IP. Links validated (110 / 148). Handle 69 (OK). Care 63 words (3 over soft cap, accepted).
- Uniqueness: hook = "weeknight session under the lights"; metaphor = race-team tire compound for a track surface; H2#2 "Speed that started with the legends..." (sole retained "Speed that" opener).

### IH4571 -- adidas F50 Hyperfast Pro Indoor
- Primary `adidas f50 indoor` (320); indoor lane held (no "pro" generic targeting). PASS brand IP. Links validated (110 / 148). Handle 64 (OK). Body 449 (<=450).
- Uniqueness: hook = "the court shrinks the moment the ball arrives"; metaphor = squash player's split-step; "phone booth of space" retained here (removed from IO8225 to de-collide).
- Gate fix: removed Pasadena fitting-room callout from Fit Notes (forbidden subject).

### IH4567 -- adidas F50 Hyperfast Pro Turf
- Primary `adidas f50 turf` (720, pos 7.5 + 1 click); turf-shoe lane. PASS brand IP (World Cup available, unused). Links validated (32 / 70). Handle 66 (OK).
- Uniqueness: metaphor = rally car on a gravel stage; H2s retitled by ORIN ("Pace that grips the synthetic" / "Pro-tier feel, everyday price"); closing "an outsole that keeps up with both".
- Gate fixes: removed Pasadena callouts from Fit Notes AND FAQ#1 (forbidden subject, 2 spots); removed redundant Internal Links audit section from the implementer brief (Gate 15).

### KJ6714 -- adidas F50 Hyperfast League Mid FG
- Primary `adidas f50 league` (880); supporting `adidas f50 hyperfast` (260). Held off `adidas f50 league turf` (IH4582). PASS brand IP (World Cup used). Handle 80 >70 (flag). og:image http:// noted.
- Internal-link note: relied on exemplar's prior validation of the same two URLs rather than independent re-scrape (acceptable, same-batch same-targets; flagged for transparency).
- Uniqueness: hook = "your ankle stays locked the whole way"; metaphor = climber's high-cut footwear / gauntlet for the ankle; H2s retitled by ORIN ("Locked at the ankle, quick off the mark" / "Two decades of pace, League-tier price").

### IO8225-900 -- Nike Mercurial Vapor 17 Pro FG (Breakout Pack) [BRAND IP: FIFA FORBIDDEN]
- Primary `nike mercurial vapor 17 pro` (10, sub-floor, GSC override pos 8 live); supporting `nike mercurial vapor` (8,100). Steered off Elite-tier (Batch 1 claimed) + collection heads.
- Brand IP: Nike non-licensee -> FIFA/World Cup FORBIDDEN. Compliance scan grep-verified ZERO restricted terms; cycle language used ("summer matches of the 2026 cycle"). PASS. (Note: live page chrome shows a "Road to '26 World Cup" banner -- theme chrome, not our copy.)
- Cross-batch differentiation vs 4 Batch 1 Mercurial entries: tier "Pro" (all Batch 1 = Elite); hook = receiving with defender on shoulder / touch-and-turn; metaphor = pickpocket's sleight of hand (distinct from Batch 1 boxer/sprinter/skier and exemplar thoroughbred). Links validated (nike-mercurial + nike-breakout). Handle 62 (OK).
- Gate fix: closing line changed from "You'll feel it the first time you beat a man in a phone booth of space" (reused exemplar's forbidden "You'll feel it the first time" frame + collided with IH4571 "phone booth") to "the half-yard that turns a crowded pocket into a clear path". Body 447 (<=450).

### J000693-CRFT -- Nike Croatia Men's Stadium Away Jersey 2026 [BRAND IP: FIFA FORBIDDEN; FIRST JERSEY]
- Primary `croatia jersey 2026` (390, pos 4.4 / 58 impr / 1 click); supporting `croatia away jersey` (50, +600% qtr). Head terms (croatia soccer jersey 1,600 / croatia jersey 1,300) not targeted -> linked up to /collections/croatia.
- Brand IP: Nike verified as Croatia 2026 supplier (Footy Headlines + Nike.com; note 2026 is the last Nike cycle before adidas). FIFA/World Cup FORBIDDEN. Compliance grep-verified ZERO restricted terms; "summer"/"2026 cycle" used. PASS.
- Jersey adaptation: identity-led (no athletic metaphor); Stadium = replica tier (no tier-word combination); jersey Care (cold wash / inside-out / no softener / badge heat); jersey FAQ (Stadium-vs-Authentic / home-vs-away / customization). Links: /collections/croatia (10 products, validated) + /collections/national-teams (1077 products, validated). Handle 49 (OK).
- Taxonomy FLAG: recommended `Apparel & Accessories > Clothing > Activewear`; needs Mike confirm (no standardized jersey node yet).
- Minor structure note: FAQ block placed after the SEO fields (template-literal order) rather than embedded in the Description like the cleat briefs; H2/H3 hierarchy correct, Mike pastes into Description body. Batch has two FAQ-placement conventions (consistency item, not a violation).

## Gate Review (ORIN defense-in-depth, 2026-06-10)

Defense-in-depth caught issues SCRIBE self-checks missed (parallel agents are blind to each other). All resolved before this hold:

1. **Forbidden subject (store-location callouts in body) -- 2 SKUs, 3 spots.** IH4571 Fit Notes + IH4567 Fit Notes + IH4567 FAQ#1 carried "Pasadena fitting room / our Pasadena store" callouts (playbook 'Forbidden subjects', line 16). Removed, replaced with on-topic fit guidance. Root cause: SCRIBE pulled the live-PDP/store context into a CTA; the forbidden-subjects rule is a SCRIBE Phase-4 self-check that 2 of 9 missed.
2. **Cross-sibling prose convergence the exemplar-forbidden-phrasings handoff did NOT prevent.** The handoff blocks exemplar->sibling copying but not sibling<->sibling convergence on an obvious shared frame. Caught: (a) "F50 speed," opening 4 heritage H2s (IH9375/IH9345/IH4567/KJ6714); (b) "Speed that" opening 3 H2s (IH4567/KJ6714 H2#1 + IH4582 H2#2); (c) "The ball..." opening both Elite Short Descriptions (JR5386/KJ6080 -- the closest-compared pair); (d) "phone booth of space" in both IH4571 and IO8225; (e) IO8225 reusing the exemplar's "You'll feel it the first time you..." closing frame. Fixed via 5 H2 retitles + 2 hook/closing rewrites so every prose-H2 title, hook, and closing line now has a unique opening fragment.
3. **Gate 15 cleanup.** IH4567 had a redundant "### Internal Links" audit section in the implementer brief; removed (links are inline in the body).

ARCHITECTURAL CONCERN A (sibling<->sibling convergence): the forbidden-phrasings handoff should also forbid the OBVIOUS shared frame for the silo (here: opening any prose H2 with "Speed"/"[Model] speed"). Recommend ORIN's pre-dispatch lane spec add a per-batch "reserved-opener" blocklist for the silo's signature word. Candidate for post-batch codification.

ARCHITECTURAL CONCERN B (word-count counting method -- NEEDS MIKE RULING): the playbook Complex ceiling "~320-450" is ambiguous on whether it counts the full Description body (prose + Product Details bullets + Fit + Care) or editorial prose + Care only. SCRIBEs split. Full-body counts (ex-FAQ): Club 528, Elite FG 454, Elite Laceless 484, League Mid 590, League Turf 505, Pro FG 543, Pro Indoor 467, Pro Turf 505, Croatia 506, Vapor 477. Editorial-prose-only counts are ~250-340 (compliant everywhere). Playbook line 84 grounds the ceiling in "editorial prose" (300-400), which argues for the editorial-only reading (all PASS). Pending Mike's ruling; if strict full-body, the long SKUs (League Mid 590, Pro FG 543, Club 528) need a trim pass.

ARCHITECTURAL CONCERN C (jersey playbook gaps -- deferred to post-batch codification per Mike): fit-tier intent mapping (Stadium/replica vs Authentic/match), home/away primary-keyword separation, jersey-sibling internal linking, jersey-specific FAQ bank, jersey taxonomy node. Croatia produced cleanly despite these; gaps are codification items, not blockers.

URL handle flags (forward-only, >70 chars, NOT changed -- 301 risk): JR5386 (76), KJ6080 (85), IH9375 (81), IH9345 (74), KJ6714 (80). Under 70 (OK): IH4582 (69), IH4571 (64), IH4567 (66), IO8225 (62), J000693 (49).

og:image http:// (implementation-side, route to VERITAS/Misha; same class as the open Phantom 6 High Elite FG follow-up): noted on IH9375, IH4582, KJ6714, IO8225, J000693 scrapes.

## Post-Gate Decisions and Actions (Mike, 2026-06-10)

**Decision 1 -- Jersey silo taxonomy:** CONFIRMED `national-team-jerseys.md` (product-class, not brand-class). File created with the Croatia entry. Rationale recorded in the file header. Club-team jerseys reserved for a future `club-team-jerseys.md`.

**Decision 2 -- Jersey Shopify taxonomy node:** PLACEHOLDER `Apparel & Accessories > Clothing > Activewear` applied to the Croatia brief. FLAG: Shopify taxonomy node pending Jorge/Tony confirmation -- first jersey under the new architecture; need to confirm the pattern matches existing ProSoccer jersey categorization before it becomes the standard for all future jerseys. Mike coordinating with Jorge separately. Not a batch blocker.

**Decision 3 -- Word-count counting method (CODIFIED):** the Complex Description-body ceiling (320-450) is the FULL body content word count: editorial prose + Product Details bullets + Care bullets + Fit Notes (FAQ counted separately). Not editorial-prose-only. Rationale: matches what buyers read, reflects total-content SEO weight, prevents bullet/Care creep, forces healthy editorial tradeoffs. Concern B is now resolved by ruling; codification into the playbook + workforce-conventions is follow-up #2 below.

**Path A executed -- full batch trimmed to <=450 full-body content words.** Mike's "three SKUs over" premise came from ORIN's loose initial framing; under the codified full-body content rule, 8 of 10 actually exceeded 450 once markdown markup tokens were excluded from the count. ALL 10 now verified <=450 content words (final: Club 420, Elite FG 435, Elite Laceless 438, League Mid 436, League Turf 448, Pro FG 435, Pro Indoor 450, Pro Turf 449, Croatia 447, Vapor 449). Zero em-dashes batch-wide (re-verified post-trim).

**What was cut (no buyer-critical information lost):**
- Decorative/low-value Product Details bullets dropped or merged: Sprintgrid print-line bullets (KJ6714, IH4582), "Iconic adidas 3-Stripes" (KJ6714), and merged spec bullets (lacing+fit, lining+outsole, weight+colorway, tier+surface) across most F50 SKUs. Bullet counts moved from 9-11 down to 7-8. All functional specs (upper tech, plate/surface, weight, tier, colorway, closure) retained.
- Heritage/metaphor prose tightened: removed the "Messi built half his career in F50s" line (KJ6714), the "1990 match vs the United States" detail and the collector send-off elaboration (J000693), and redundant metaphor clauses (the rally-car, tire-compound, flat-stone, and pickpocket paragraphs were condensed without losing the image).
- Fit Notes condensed (removed restated break-in/collar guidance); Care bullets merged where two said the same thing (no-conditioner folded into the brush bullet; air-dry/heat folded for the jersey).
- Tradeoff confirmed healthy: editorial prose stayed the priority; the cuts came from spec-bullet redundancy and prose verbosity, exactly the discipline the full-body ceiling is meant to force.

**Silo registries appended (post-approval, per the append protocol):** f50.md (+8 entries: JR5386, KJ6080, IH9375, IH9345, IH4582, IH4571, IH4567, KJ6714); mercurial.md (+1: IO8225-900, first Pro-tier Mercurial entry, now 5 total); national-team-jerseys.md (created, +1: J000693-CRFT).

**Codification follow-ups (after this batch commits -- next session):**
1. Concern A (reserved-opener blocklist): add a proactive silo-signature opener blocklist to ORIN's exemplar handoff (F50: "F50 speed", "Speed that"; Phantom: "Some players are quick"; etc.). ~15-20 min.
2. Concern B (full-body word-count rule): make explicit in product-page-playbook + collection-page-playbook + workforce-conventions. ~10 min.
3. Concern C (jersey playbook gaps): already on standing follow-ups; next session.
