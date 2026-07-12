# Batch 7 audit trail (2026-07-11, first live v2 run)

Workforce-internal. ORIN pre-dispatch record for the first live v2 batch. Companion to the dispatch handoff briefing `.claude/agents/master-strategist/briefings/2026-07-11_batch7-dispatch-handoff.md`.

## Step 0 (Mike's gate) -- both checks passed
- **SCRIBE v2 spec loaded:** `.claude/agents/on-page-seo/agent.md` Section 2 carries `### v2 input-driven flow (added 2026-07-10)` (input-driven, reads per-SKU input file, <= 10 tool uses, no self-scrape/keyword/link-validate). Fresh session loads sub-agent defs from disk, so on-disk presence = loaded. **v2 confirmed loaded.**
- **Permission allowlist active:** `.claude/settings.json` has the `allow` list (git/python/node/file-ops + the 4 MCPs) and the `deny` list (rm -rf, git reset --hard, git push --force, curl, wget).

## Eligibility
All 10 SKUs Mike-pre-vetted "In Progress" in the white-label sheet (Shopify-admin eligibility, per `context/workforce-conventions.md` 'Eligibility verification'). No strategic-exception flags at submission. Live-stock signals captured at scrape are publish-priority notes only, not eligibility gates (see below).

## Tool pre-flight
- Firecrawl MCP: operational (map + 12 scrapes returned status 200 / valid JSON; one 404 on a first-guess URL, re-mapped and resolved). Used for URL resolution + Phase 0 batched pre-scrape + link content-validation.
- DataForSEO MCP: operational (status_code 20000) -- one bulk `dataforseo_labs_google_keyword_overview` call for volumes.
- GSC: not called this batch (primaries pre-locked by Mike's cannibalization resolutions; no CTR-diagnostic scope in a fresh-optimization batch).

## URL resolution (counted in batch cost, not free setup)
Resolved via 3 Firecrawl `map` calls (Shadow collection, turf/ligera+reactx, Jordan collection). One 404 (guessed `...ligera-pro-turf-soccer-shoes-shadow-fa26`) corrected to `...ligera-pro-turf-soccer-shoes-shadow-pack-fa26` via a 4th targeted map. All 10 style codes confirmed against the scrape.

## Phase 0 scrape-wins highlights
- All 9 cleats: colorway Black/Black/Illusion Green (Shadow Pack, FA26). **No weight on any PDP -> weight = "not in scrape" for all, left out (pre-empts the IF8512 fabricated-weight defect).**
- HJ4123 ReactX: **midsole ReactX foam CONFIRMED on-page** -> ReactX language permitted.
- Tiempo Ligera (HQ3158, IB4477): confirmed a genuine new sub-line -- all-new TECHLEATHER + a TRADITIONAL FULL-PLATE (vs Maestro's Maestro360 split plate), positioned "lose the weight without losing your touch" (lightweight value Tiempo). Pro tier.
- Jordan (7651TX1919): **AWAY confirmed** (title + scrape); colorway base **Red** (matches guardrail Away = red/black; the kufiya-diamond is a HOME-shirt feature per the guardrail, so it is NOT foregrounded on this away red). Authentic (match-spec). Live PDP copy currently uses "World Cup 2026" -- our copy must NOT (Kelme non-adidas, cycle-language-only; gate check #5).

## Publish-priority notes (live-stock at scrape; evergreen copy regardless)
- 7651TX1919 Jordan Away: **1 item left** (near-sold-out). Evergreen copy; flag for implementation ordering.
- HQ3158 Tiempo Ligera Pro FG: 1 item left.
- IF8508 Vapor 17 Elite FG: 2 items left.
- HJ4123 ReactX Phantom Low Pro Turf: 2 items left.
All ship normal evergreen optimization; low-stock is an implementation-ordering note for Mike, not an eligibility change.

## Cannibalization (three-way Shadow collision) -- enforced, not re-litigated
Per briefing: Shadow SKUs take pack-specific `...shadow` primaries, ceding the generic model-tier-surface term to the shipped Breakout twin; intra-batch siblings surface-split. Registry 1 claimed generics staged in `inputs/_registry1_primaries.txt`; gate check #9 enforces. No collisions (all Batch 7 primaries add `shadow`/`turf shadow`).

## Wave shape (LOCKED by Mike)
9 Shadow cleats parallelize (established Mercurial/Tiempo/Phantom silos). Jordan (7651TX1919) runs exemplar-first (new first-nation lane, Mike-approved exception criterion 1). Tiempo Ligera new sub-line handled by distinct per-SKU input lanes + Phase 0 scrape + gate check #7, NOT exemplar-first serialization (Mike's call).
