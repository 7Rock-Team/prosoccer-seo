# Batch 7 dispatch handoff (v2 first live run + measurement)

_Written 2026-07-11 by ORIN in the build session, for the FRESH session that runs Batch 7. This session predates the v2 agent-def edits, so a restart was required to load the v2 SCRIBE spec. Mike approved Path A (fresh session). Read this at startup; it carries everything Batch 7 needs. The pre-flight triage is already done and both real exceptions are cleared (Jordan first-nation, approved; session-def, resolved by this restart). From here it is decide-and-log per v2 escalate-on-exception unless something genuinely new surfaces._

## Step 0: verify v2 actually loaded BEFORE dispatch (Mike's explicit gate)

Do this first. If either check fails, STOP and tell Mike; he would rather a second restart than a confounded run.

1. **SCRIBE v2 spec loaded:** Read `.claude/agents/on-page-seo/agent.md` Section 2 and confirm the `### v2 input-driven flow (added 2026-07-10)` subsection is present (input-driven, reads the per-SKU input file, <= 10 tool uses, no self-scrape/keyword/link-validate). Since a fresh session loads sub-agent defs from disk at startup, on-disk presence = loaded.
2. **Permission allowlist active:** Read `.claude/settings.json` and confirm the `permissions.allow` list (git/python/node/file-ops/the 4 MCPs) and the `deny` list (rm -rf, git reset --hard, git push --force, curl, wget). Routine ops should auto-approve this session.

If both pass, proceed. Report "v2 confirmed loaded" in the run.

## The batch (10 SKUs, all eligibility pre-vetted, "In Progress" in the sheet)

| # | SKU | Product | Silo | Wave |
|---|---|---|---|---|
| 1 | IF8508-001 | Nike Vapor 17 Elite FG Shadow FA26 | Mercurial (Vapor) | PARALLEL |
| 2 | HQ3157-001 | Nike Tiempo Maestro Elite FG Shadow FA26 | Tiempo (Maestro) | PARALLEL |
| 3 | HQ3158-002 | Nike Tiempo Ligera Pro FG Shadow FA26 | Tiempo (Ligera, new sub-line) | PARALLEL |
| 4 | 7651TX1919 | Kelme 2026 Jordan Men's Authentic Away Jersey | National-team jerseys | EXEMPLAR-FIRST |
| 5 | IB4477-002 | Nike Tiempo Ligera Pro Turf Shadow FA26 | Tiempo (Ligera, new sub-line) | PARALLEL |
| 6 | IM5811-001 | Nike Vapor 17 Pro Turf Shadow FA26 | Mercurial (Vapor) | PARALLEL |
| 7 | IO4252-001 | Nike Vapor 17 Elite AG Shadow FA26 | Mercurial (Vapor) | PARALLEL |
| 8 | HJ4123-001 | Nike ReactX Phantom 6 Low Pro Turf Shadow FA26 | Phantom | PARALLEL |
| 9 | IM2513-001 | Nike Zoom Superfly 11 Elite AG Shadow FA26 | Mercurial (Superfly) | PARALLEL |
| 10 | IB4469-001 | Nike Tiempo Maestro Elite AG Shadow FA26 | Tiempo (Maestro) | PARALLEL |

**Wave shape LOCKED by Mike:** 9 Shadow cleats parallelize on established silos; Jordan runs exemplar-first for the new first-nation lane. If wave logic tries to send any established-silo cleat to exemplar-first, that is a wave-logic leak: call it out in the report (measurement ask). Note: the Tiempo Ligera pair (#3, #5) is a genuine new SUB-LINE, but Mike's call is that all 9 cleats parallelize (established Tiempo silo; the Ligera new-ness is handled by distinct per-SKU input-file lanes + Phase 0 scrape for construction + batch_gate check #7 as the convergence backstop, not by exemplar-first serialization).

## Step 1: resolve the 10 product URLs (fold the cost into the totals, honestly)

The sheet gave SKUs + names, not URLs. Resolve them via a Firecrawl map of the Shadow + Jordan collections, or Shopify search. This resolution is part of the real batch cost: count its tokens and wall-clock in the totals, do NOT treat it as free setup.

## Cannibalization resolutions (three-way Shadow collision; enforce, do not re-litigate)

Same discipline as Batch 6: Shadow SKUs take pack-specific `...shadow` primaries, ceding the generic model-tier-surface term to the shipped Breakout twin; surface-split intra-batch siblings. Registry 1 (white-label sheet) cross-check runs at pre-dispatch; Registry 2 precedent is in `context/silo-positioning/{mercurial,tiempo,phantom}.md`. batch_gate.py check #9 enforces at the gate.

| Batch 7 SKU | Generic term (claimed by) | Resolved primary |
|---|---|---|
| IF8508 Vapor 17 Elite FG Shadow | `nike vapor 17 elite fg` (IO1560 Breakout) | `nike vapor 17 elite fg shadow` |
| IM5811 Vapor 17 Pro Turf Shadow | `nike vapor 17 pro` (IO8225 Breakout + IF8512 Batch 6 Shadow FG) | `nike vapor 17 pro turf shadow` (surface-split from IF8512 FG) |
| IO4252 Vapor 17 Elite AG Shadow | `nike vapor 17 elite ag` (IM5806 Breakout) | `nike vapor 17 elite ag shadow` |
| IM2513 Superfly 11 Elite AG Shadow | `nike zoom superfly 11 elite ag` (IO8221 Breakout) | `nike zoom superfly 11 elite ag shadow` |
| HQ3157 Tiempo Maestro Elite FG Shadow | `nike tiempo maestro elite fg` (IH1776 Breakout) | `nike tiempo maestro elite fg shadow` |
| IB4469 Tiempo Maestro Elite AG Shadow | `nike tiempo maestro elite ag` (IQ2383 Breakout) | `nike tiempo maestro elite ag shadow` |
| HJ4123 Phantom 6 Low Pro Turf Shadow | Phantom Low Pro (IQ1886 FG, IR4192 Jr FMG); no adult Low Pro Turf | `nike phantom 6 low pro turf shadow` |
| HQ3158 Tiempo Ligera Pro FG Shadow | Ligera unclaimed (new sub-line) | `nike tiempo ligera pro fg shadow` |
| IB4477 Tiempo Ligera Pro Turf Shadow | Ligera new; sibling of HQ3158 | `nike tiempo ligera pro turf shadow` (surface-split from HQ3158) |
| 7651TX1919 Kelme Jordan Away | first Jordan; no NT collision | `jordan away jersey 2026` (evergreen; KIRA verifies volume/floor; render per home-vs-away scrape) |

Each Shadow brief also differentiates PROSE against its Breakout twin's logged metaphor/hook (Registry 2) and against the Batch 6 Shadow entries (IF8512, HJ2147/2146, HQ2329). Pack-secondary `nike shadow pack` per SKU where applicable.

## Scrape-verify watch items (scrape-wins; escalate ONLY if absent AND load-bearing AND self-contradictory)

- **HJ4123 ReactX (Phantom 6 Low Pro Turf):** ReactX is a real Nike foam, but confirm THIS SKU's midsole is genuinely ReactX from the Phase 0 scrape before writing any ReactX spec language. Scrape confirms -> write it; scrape silent -> omit it (no fabrication).
- **Tiempo Ligera (HQ3158, IB4477):** Ligera is a new Tiempo sub-line (absent from tiempo.md; Maestro/Legend are the established lines). Confirm its construction/positioning (lightweight speed-oriented Tiempo?) from the scrape; do not assert from the name. Distinct per-SKU lanes for the FG vs Turf siblings.

## Jordan (7651TX1919) specifics

- Guardrails: `context/silo-positioning/national-team-jerseys.md` 'Jordan (added 2026-07-11)'. Al-Nashama (glossed, gender-neutral), Kelme non-FIFA cycle-language only, 2026 first-appearance in CYCLE LANGUAGE (never "World Cup"; qualification sealed 3-0 over Oman is a verifiable evergreen detail; 2023 AFC Asian Cup runners-up as a FIFA-free secondary anchor), colors white/red/black/green + kufiya diamond motif per scrape, JFA/AFC, Kelme supplier time-sensitive.
- **Home-vs-away scrape check (Mike):** the sheet says "Away," but the live Jordan collection anchors Home on white (red kufiya-diamond sleeves) and Away on red/black. Confirm home-vs-away and the exact colorway from the Phase 0 scrape and write what the SKU actually shows; do NOT inherit the sheet label if the scrape disagrees. Scrape wins.
- Taxonomy node (Mike's Batch 7 call, codified): `Apparel & Accessories > Clothing > Shirts & Tops`. Put it in the Jordan input file.
- batch_gate.py check #5 (FIFA-grep) guards the Kelme non-FIFA rule; brand `kelme`, posture `cycle-language-only` in the gate-meta block.

## Measurement instrumentation (the end-of-batch report MUST carry all of this)

- **Wall-clock total** (target < 90 min) and where the time concentrated.
- **Token total** (target ~1 to 1.5M vs v1 ~3 to 4M baseline), INCLUDING the URL-resolution cost. Label measured-vs-estimated honestly; do not fabricate a precise number.
- **Per-SCRIBE tool-use count, each agent listed** (target <= 10). THE HEADLINE NUMBER. Flag any agent that exceeded 10 and why (an over-10 count is the signal that an input file was incomplete and SCRIBE fell back to self-gathering).
- **Parallel-vs-exemplar breakdown:** confirm all 9 cleats went parallel and only Jordan went exemplar-first. Any established silo triggering exemplar-first = wave-logic leak, call it out.
- **Cannibalization resolutions:** the three-way Shadow collision (Batch 7 vs Batch 6 Shadow vs Batch 1/2 Breakout) and how each resolved.
- **Decide-and-log calls** with one-line rationale each.
- **Registry 1 handoff block** (per-SKU primaries for Mike's white-label sheet entry).
- **Commit hashes** (local, unpushed brief commits).

## Push discipline (report-before-push)

Run batch_gate.py over the session, auto-fix and log the mechanical FAIL classes, re-run to green, then COMMIT LOCALLY. Do NOT push the Batch 7 brief commits. Surface the instrumented end-of-batch report and HOLD; Mike reviews the report, then clears the push. The report is Mike's gate on the push (v2 escalate-on-exception + push-on-Mike's-go). The taxonomy (4758558) and Jordan-guardrail (630457f) commits were already pushed at Mike's go in the build session.

## Standing v2 references

- Pipeline: `docs/workforce-v2-pipeline.md`. Per-SKU input schema: `templates/per-sku-input-template.md`. Gate: `scripts/batch_gate.py` (+ `scripts/test_batch_gate.py`). Conventions: `context/workforce-conventions.md` 'Per-SKU input file + batched pre-scrape (v2)', 'Wave collapse', 'Escalate-on-exception approval mode (v2)', 'Forbidden-phrasings three-tier scope (v2)', 'Jersey taxonomy node'.
