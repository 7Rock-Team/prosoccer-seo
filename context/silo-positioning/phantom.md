# Silo Positioning: Nike Phantom

Per-SKU prose patterns claimed in shipped briefs for the Nike Phantom silo (the touch-and-control line). Format and append protocol: see `README.md` in this directory. ORIN reads this file during the pre-dispatch differentiation pass and appends after each batch commits.

## Pre-dispatch reference / guardrails

Reference notes ORIN reads at the pre-dispatch differentiation pass. Separate from the append-only per-SKU log below.

### Junior tier (added 2026-07-08, Batch 6, first junior in this silo)
- IR4192-661 (Jr Phantom 6 Low Pro FMG) is the FIRST junior entry in the Phantom silo. The senior log below is all Elite / Pro adult SKUs.
- "Low Pro" is the Pro tier in junior sizing (Nike tier ladder: Elite > Pro > Academy > Club). Junior Pro is the junior equivalent of the senior Pro tier. Confirm the tier and spec from the SKU's Phase 0 scrape (scrape-wins); do not assert tier from the product name alone.
- **Avatar lane:** parent / developing-young-player milestone framing, NOT the senior performance lane. Mirror `copa.md` KI0662 (the Jennifer-parent lane: the child's real cleats framed as a reward earned, sized for growing feet), adapted to the Phantom control DNA rather than Copa touch.
- **Word-count band:** by tier-equivalence, the Pro band (340 to 390) applies unless the SKU's scrape and complexity say otherwise.

### FMG surface (added 2026-07-08, Batch 6, first in this silo)
- FMG = firm-multi-ground: a hybrid stud plate built for firm natural grass plus harder and some artificial surfaces. It is the versatile across-surfaces option, distinct from the silo's dedicated FG (firm natural grass) and AG (artificial-grass-specific) plates already logged below.
- Do not claim a specific stud count; confirm the plate description from the SKU's Phase 0 scrape (scrape-wins).

### Shadow Pack anti-convergence (added 2026-07-08, Batch 6)
The Batch 6 Phantom Shadow SKUs are same-model / same-tier / same-surface COLORWAY re-runs of shipped Batch 1 (2026-06-08) Breakout Pack SKUs, so they MUST differentiate against the prior-batch log below, not just against current-batch siblings:
- **HJ2147-001 (High Elite FG Shadow) vs IH1779-900 (High Elite FG Breakout):** forbidden carry-forward of IH1779's marksman / rehearsed-aim metaphor and its "moment of the strike" hook. Fresh hook, metaphor, and scene.
- **HQ2329-001 (High Elite AG Shadow) vs IQ1869-900 (High Elite AG Breakout):** forbidden carry-forward of IQ1869's "armor at the ankle / fortress at the joint" metaphor and its "week on the turf" hook. Fresh hook, metaphor, and scene.
- **HJ2146-001 (Low Elite FG Shadow):** a new tier-by-surface combo in this silo. Differentiate against IQ1870-900 (Low Elite AG, "surface-matched specialist") and IQ1886-900 (Low Pro FG, "dependable workhorse").
- Pack-secondary keyword ("nike phantom 6 shadow" / "nike shadow pack") pending KIRA Phase 1. Shadow colorway pending Phase 0 scrape (Firecrawl-dependent; see `work-log/follow-ups.md` 2026-07-08).

## Claimed patterns log

### SKU IH1779-900 (Phantom 6 High Elite FG)
- Brief: `deliverables/page-optimizations/2026-06-08_session-01/nike-phantom-6-high-elite-firm-soccer-cleats-breakout-pack-su26_brief.md` (re-run batch 2026-06-08)
- Date: 2026-06-08
- Opening hook approach: the moment of the strike; the reader placed inside a match-deciding finish that lands exactly where aimed
- Primary metaphor: the calm of a trained craft; finishing as repetition that turns a gamble into a habit (a marksman's rehearsed aim, not a weapon)
- Use case scenario: the creative number ten or central forward who creates and finishes on dry natural grass and wants the locked-in high collar
- Angle of emphasis: the rehearsed, repeatable finish; precision as a trained craft at the top tier on the truest surface
- Heritage angle: Phantom as Nike's accuracy line; Gripknit spread across the whole upper (vs the Predator's concentrated striking zones)

### SKU IQ1886-900 (Phantom 6 Low Pro FG)
- Brief: `deliverables/page-optimizations/2026-06-08_session-01/nike-phantom-6-low-pro-firm-ground-soccer-cleats-breakout-pack-su26_brief.md` (re-run batch 2026-06-08)
- Date: 2026-06-08
- Opening hook approach: the step up a rising player earns; outgrowing old cleats, gear that matches the touch you have built, without the top-tier receipt
- Primary metaphor: the dependable, well-made everyday instrument (the trusted workhorse) that does the job week in and week out
- Use case scenario: the developing club or high-school playmaker and finisher on dry natural grass who wants a low cut and strong value
- Angle of emphasis: the same finishing control at an accessible tier; the freedom and simplicity of a low cut
- Heritage angle: Phantom control DNA at the Pro tier made reachable; VNMSkin over Flyknit (contrasted with the Elite's Gripknit)

### SKU IQ1870-900 (Phantom 6 Low Elite AG)
- Brief: `deliverables/page-optimizations/2026-06-08_session-01/nike-phantom-6-low-elite-artificial-grass-pro-soccer-cleats-breakout-pack-su26_brief.md` (re-run batch 2026-06-08)
- Date: 2026-06-08
- Opening hook approach: the quick receive-and-go on artificial grass, gone on the half-turn before the marker sets his feet
- Primary metaphor: gear ground to fit one kind of ground; the surface-matched specialist's tool
- Use case scenario: the playmaker and finisher who plays and trains primarily on artificial grass, wanting the Elite control upper and a low cut for fast release
- Angle of emphasis: elite control tuned for the modern synthetic pitch; low-cut quickness of release
- Heritage angle: Phantom accuracy line; the AG-Pro plate (shorter, denser conical studs) engineered to plant the Gripknit player on synthetic

### SKU IQ1869-900 (Phantom 6 High Elite AG)
- Brief: `deliverables/page-optimizations/2026-06-08_session-01/nike-phantom-6-high-elite-artificial-grass-pro-soccer-cleats-breakout-pack-su26_brief.md` (re-run batch 2026-06-08)
- Date: 2026-06-08
- Opening hook approach: the player whose week is on the turf, committing to every plant on a hard synthetic surface and wanting the ankle wrapped and secure
- Primary metaphor: armor wrapped around the ankle; a fortress at the joint (support and security)
- Use case scenario: the finisher who plays and trains on artificial grass and wants maximum ankle lockdown, weeknight 3G under lights
- Angle of emphasis: the locked-in finisher on artificial grass; ankle support plus a surface-matched plate
- Heritage angle: high-cut Phantom heritage; the Dynamic Fit collar paired with the AG-Pro plate for confidence on demanding artificial pitches

### SKU IR4192-661 (Jr Phantom 6 Low Pro FMG) [Batch 6, first junior + first FMG]
- Brief: `deliverables/page-optimizations/2026-07-08_session-01/IR4192-661_nike-jr-phantom-6-low-pro-fmg_brief.md` (commit f6c3f76)
- Date: 2026-07-08
- Opening hook approach: parent milestone; the season a young player starts shaping real passes and earns the step up
- Primary metaphor: the do-it-all first serious cleat, one pair for whatever surface the weekend brings (NOT a senior single-surface specialist)
- Use case scenario: the developing youth player (Jennifer parent avatar) on mixed firm and artificial surfaces, Saturday club and school, growing feet, low cut
- Angle of emphasis: Phantom control sized for junior feet at the Pro tier without the flagship price; FMG multi-surface versatility
- Heritage angle: Phantom control DNA (VNMSkin + Flyknit, Cyclone 360) at Junior Pro; the FMG plate as the versatile across-surfaces option

### SKU HJ2147-001 (Phantom 6 High Elite FG Shadow) [Batch 6, Shadow-pack exemplar]
- Brief: `deliverables/page-optimizations/2026-07-08_session-01/HJ2147-001_nike-phantom-6-high-elite-fg-shadow_brief.md` (commit f6c3f76)
- Date: 2026-07-08
- Opening hook approach: the creator who shapes one way and plays the other, gone from the defender's picture for the half-second that decides the move
- Primary metaphor: the shadow the defense loses on the blind side; disguise of the pass
- Use case scenario: the creative forward or number ten on dry firm natural grass who wins with disguise and weight of pass, top tier, high collar
- Angle of emphasis: disguise and vision in the final third at the top tier on firm ground (the Shadow-pack pass-disguise facet)
- Heritage angle: Phantom accuracy line; Gripknit across the upper; the Shadow Pack (Black/Black/Illusion Green)

### SKU HJ2146-001 (Phantom 6 Low Elite FG Shadow) [Batch 6, Shadow mirror]
- Brief: `deliverables/page-optimizations/2026-07-08_session-01/HJ2146-001_nike-phantom-6-low-elite-fg-shadow_brief.md` (commit 496ed06)
- Date: 2026-07-08
- Opening hook approach: the low-cut playmaker who takes it on the half-turn, into the space the set defender was guarding before he can shift his weight
- Primary metaphor: disguise of the first step, the movement before the pass; the half-turn a set defender can't read
- Use case scenario: the low-cut playmaker on dry firm natural grass who wins with quickness of release, Elite control
- Angle of emphasis: Elite control in a low cut for the quick first step and release on firm ground (distinct from HJ2147's pass-disguise)
- Heritage angle: Phantom control DNA at the Elite tier in a low cut; Gripknit + Cyclone 360; Shadow Pack colorway

### SKU HQ2329-001 (Phantom 6 High Elite AG Shadow) [Batch 6, Shadow mirror; cedes generic to shipped IQ1869]
- Brief: `deliverables/page-optimizations/2026-07-08_session-01/HQ2329-001_nike-phantom-6-high-elite-ag-shadow_brief.md` (commit 496ed06)
- Date: 2026-07-08
- Opening hook approach: the turn the defender never tracks; the plant-and-go on synthetic under lights, finished before he resets his feet
- Primary metaphor: the elusive cut on the turf, slipping the marker on artificial grass (elusiveness, NOT IQ1869's lockdown/support)
- Use case scenario: the finisher or playmaker who lives on artificial grass (weeknight 3G) and wins by slipping markers, high collar
- Angle of emphasis: elusiveness and disguise on artificial grass at the High Elite tier (distinct from IQ1869's ankle-lockdown framing)
- Heritage angle: high-cut Phantom control on the AG-Pro plate tuned for synthetic; Gripknit; Shadow Pack colorway

### SKU HJ4123-001 (ReactX Phantom 6 Low Pro Turf Shadow) [Batch 7, Shadow pack; first adult Low Pro Turf + first ReactX in this silo]
- Brief: `deliverables/page-optimizations/2026-07-11_session-01/HJ4123-001_nike-reactx-phantom-6-low-pro-turf-shadow_brief.md`
- Date: 2026-07-11
- Opening hook approach: turf beats up your legs; the Phantom answers with a springboard of ReactX bounce underfoot while the clean strike still comes first
- Primary metaphor: a springboard underfoot, the ReactX foam returning some of the energy the hard court takes (deliberately NOT the Batch 6 Phantom Shadow disguise / elusiveness register)
- Use case scenario: the Pro-tier turf or small-sided player (cages, weeknight) wanting Phantom striking touch plus ReactX cushioning
- Angle of emphasis: ReactX responsiveness (scrape-confirmed) + VNMSkin touch at Pro on turf; distinct from IQ1886 FG "workhorse" and from the Batch 6 Elite Shadow disguise lane. "Shadow" used only as the pack name, never as a disguise metaphor.
- Heritage angle: Phantom control at the Pro tier (VNMSkin + Flyknit, NOT the Elite's Gripknit); ReactX foam; rubber turf outsole; Shadow Pack
