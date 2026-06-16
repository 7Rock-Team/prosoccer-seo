# Batch 3 Audit Trail -- 2026-06-15 session-01

## Batch metadata
- Batch: 3 (first batch under the full refined architecture; all six 2026-06-15 codifications active)
- SKUs: 10 PDPs. 5 adidas F50 Hyperfast + 5 adidas Predator, all Road to Glory Pack SP26.
- Exemplars (dual): IH4451 (junior F50, sets junior precedent) and HP9973 (Predator, populates the empty predator.md silo).
- Brand IP: all adidas, FIFA-licensed. World Cup / FIFA / tournament / "Road to Glory" terminology permitted. No constraint issues on any SKU. adidas lowercase enforced; no UK "boots" in body copy.
- Approval mode: APPROVE-EVERY-ACTION. Mike approved at CHECKPOINT 1 (keyword strategy), CHECKPOINT 2 (exemplars + skeleton/forbidden phrasings), and CHECKPOINT 3 (pre-commit, with re-trim authorization).

## Architecture / execution notes
- **KIRA MCP inheritance gap (Category B):** the keyword-research and on-page-seo sub-agents carry no MCP tools, and GSC/DataForSEO/Drive/Firecrawl OAuth does not propagate to sub-agents. ORIN ran Phase 0 (Firecrawl scrape), Phase 1 (GSC + DataForSEO keyword research), and Phase 4 (gate verification) at the PARENT level per the codified fallback. Consequence: parent-level token spend is higher than the Batch 2 pattern. Standing follow-up: KIRA MCP inheritance fix prioritized for next session / the token-efficiency audit.
- **Registry 1 (white-label sheet) write-back:** manual handoff by design (ORIN reads, never writes). Per-SKU primary keyword assignments for Mike to enter on the PDPs tab are listed below.
- **Registry 2 (silo files):** appended this batch. f50.md +5 entries (IH4451, IH4577, KK1307, KK1315, KK1319). predator.md populated from empty scaffold to 5 entries (HP9973, HP9967, HP9970, HP9971, HP9998).

## Defense-in-depth: gate failures caught and corrected at the ORIN gate
1. **Fabricated Difficulty (KD) scores -- FIRST occurrence of this failure mode (observation).** The HP9973 exemplar's Keywords table shipped invented KD values (45/52/48/60); ORIN supplied no KD in dispatch and DataForSEO returned only sparse/low KD for these terms. Blanked all Difficulty cells to match IH4451's correct treatment and keep the two exemplars consistent. Per Mike's CHECKPOINT-2 direction: observe this batch; codify a "no fabricated KD; blank if not retrieved" SCRIBE Phase-4 self-check only if it recurs. (Status: observed once.)
2. **Broken internal link (soft-404 class).** The IH4451 exemplar linked `/collections/youth-soccer-cleats`, which returns a hard 404 (redirects to /404, noindex). Repointed to `/collections/adidas-road-to-glory-pack` (validated live; spans FG/turf/indoor, adult + youth; pack-relevant). `/collections/kids-soccer-cleats` also confirmed 404.
3. **Invented retail specific (fabrication mode, second instance).** KK1307's wide-feet FAQ contained an unverified "our fitting room in Pasadena is open until 8 pm" claim with no source. Removed and replaced with a generic try-before-you-buy line. Scanned all 10 briefs; this was the only instance.
4. **Sub-floor flag wording.** KK1315 and HP9998 used "GSC override" with no GSC signal; corrected to "0* (no GSC signal yet)" (the override format is reserved for SKUs with an actual GSC position to cite, e.g. IH4451 pos 7).

## Internal link validation (content signals, not status codes alone) -- ORIN, 2026-06-15
- `/collections/adidas-f50` -> 200, title "Adidas F50 Soccer Cleats & Shoes", live collection. VALID. (F50 briefs)
- `/collections/adidas-predator` -> 200, title "Adidas Predator Soccer Cleats & Shoes", live collection. VALID. (Predator briefs)
- `/collections/adidas-road-to-glory-pack` -> 200, title "adidas Road to Glory Pack Soccer Cleats", live pack collection. VALID. (both silos; pack-relevant second link)
- `/collections/youth-soccer-cleats` -> 404. INVALID. `/collections/kids-soccer-cleats` -> 404. INVALID.

## Word-count discipline (write-to-content-need, not write-to-ceiling)
Mike's CHECKPOINT-3 operational catch: League/Club-tier SKUs should land below Elite-tier. Three League briefs over-wrote to the 465 ceiling and were re-trimmed (Path A: spec-bullet redundancy first, prose padding second; hook / differentiation lane / FAQ / Care scope preserved).

| SKU | Tier | Pre-trim | Final |
|---|---|---|---|
| IH4577 | League indoor | 465 | 387 |
| KK1315 | Jr League Mid | 457 | 386 (+ density fix) |
| HP9998 | Jr League Fold-Over | 465 | 365 (+ density confirmed) |
| KK1307 | Jr Club | 374 | density fix only (now 3x "adidas f50 youth"); fabrication removed |
| Elite/Pro (HP9967 464, HP9971 465, HP9970 450, HP9973 ~456, IH4451 465) | Elite | -- | held (tier-appropriate for premium) |
| KK1319 | Jr League Turf | 378 | held (already tier-appropriate) |

Codification follow-up (separate commit after this batch pushes): tier-appropriate word-count bands as a SCRIBE Phase-4 self-check + ORIN Gate 15 check.

## Per-SKU keyword assignments (for the white-label PDPs tab -- manual entry by Mike)
| SKU | Primary keyword | Floor status | Pack-specific secondary |
|---|---|---|---|
| IH4451 | adidas junior f50 elite fg | sub-floor, GSC pos 7 | adidas f50 road to glory (390) |
| IH4577 | adidas f50 indoor soccer shoes | 480 (clears) | adidas f50 road to glory (390) |
| KK1307 | adidas junior f50 club | sub-floor, GSC pos 10 | adidas f50 road to glory (390) |
| KK1315 | adidas junior f50 league mid | sub-floor, no GSC signal | adidas f50 road to glory (390) |
| KK1319 | adidas junior f50 turf | sub-floor, GSC pos 1 | adidas f50 road to glory (390) |
| HP9973 | adidas predator elite fg | 1,000 (clears) | adidas predator road to glory (GSC-validated) |
| HP9967 | adidas predator elite laceless | 390 (clears) | adidas predator road to glory |
| HP9970 | adidas junior predator elite fg | sub-floor, no GSC signal | adidas predator road to glory |
| HP9971 | adidas predator elite ag | 590 (clears) | adidas predator road to glory |
| HP9998 | adidas junior predator league | sub-floor, no GSC signal | adidas predator road to glory |

Junior-keyword strategy (ratified CHECKPOINT 1): every junior-qualified exact term returned zero DataForSEO volume; juniors carry unique sub-floor `junior`-qualified primaries (flagged with GSC override where signal exists, "no GSC signal yet" otherwise) rather than sharing the floor-clearing model term, to preserve uniqueness and avoid cannibalizing the senior siblings' claimed terms. Junior density supporting term = model+youth (`adidas f50 youth` / `adidas predator youth`, buy intent), NOT the collection-class `adidas youth soccer cleats` (browse intent, routes to a collection page). "youth" outperforms "junior"/"kids" in measured volume; titles stay "Junior" for product/SKU accuracy.

## Per-SKU notes
- **Complexity:** all 10 are soccer cleats -> Complex category (5 H2s, Care H2 required). Word budgets set per tier per the write-to-content-need discipline above.
- **Sibling-title uniqueness:** all 10 Meta Titles / Titles distinct; junior vs senior and tier/surface/construction differentiate. F50 siblings differentiated against the 8 Batch-2 f50.md entries (no opener/metaphor reuse); the four juniors differentiated against their senior counterparts by positioning lane.
- **Predator construction (Phase 0 verified):** HP9973 standard laced + floating tongue (NOT fold-over, NOT laceless); HP9967 laceless + Primeknit collar; HP9971 fold-over tongue + AG; HP9970 junior Elite fold-over (Nanostrike Pro); HP9998 junior League fold-over (Nanostrike base). Nanostrike tech ladder (+ / Pro / base) tracks the price ladder.
- **HP9998 reservation:** `adidas predator league fg` (260) left for the future senior JP6271 SKU (on the sheet, not in this batch); the junior took the `junior`-qualified term.

## Standing flags for Mike
- **All 10 URL handles exceed 70 chars.** Flagged in every brief, none auto-changed (301 equity risk, Misha coordination). Forward-only per Mike's decision; SP26 pack pages keep current handles.
- **Image Alt Text** in each brief is best-effort (no live gallery visibility this session); map to actual gallery slots at publish.

## Addendum (Batch 3 close)
Consolidates the audit items confirmed at session close.

- **Parent-level Phase 0/1/4 (KIRA MCP inheritance gap, Category B).** ORIN ran Firecrawl (Phase 0), GSC + DataForSEO (Phase 1), and gate verification (Phase 4) at the parent level because the sub-agents carry no MCP tools and OAuth does not propagate. Parent token spend ran higher than the Batch 2 pattern. Standing follow-up (HIGH): KIRA MCP inheritance fix + token-efficiency audit, prioritized for next session.
- **~244k tokens wasted on the HP9973 first dispatch.** The first HP9973 exemplar SCRIBE fully drafted and self-verified the brief, then self-denied its own Write under APPROVE-EVERY-ACTION (treating a draft-folder write as a gated action). SendMessage was unavailable to resume the agent, so recovery required a full re-dispatch (~247k more). Follow-up (HIGH): tweak the SCRIBE dispatch prompt so SCRIBE self-gates only on commit-stage / publish actions, never on writing a draft brief into the deliverables folder.
- **Fabrication mode observed TWICE in one batch (first batch occurrence of either).** (1) HP9973 invented Keywords-table Difficulty scores; (2) KK1307 invented a "Pasadena fitting room open until 8 pm" retail detail with no source. Both caught and corrected at the ORIN gate. Pattern to watch in Batch 4. If either recurs once more, codify a SCRIBE Phase 4 self-check: "No fabricated specifics: leave KD blank if not retrieved; no store / retail / policy details unless present in source data." (Not codified yet; observing.)
- **Tier-appropriate word-count codification is now ACTIVE (commit 49e5959).** Applies Batch 4 onward: within the Complex band the body scales to tier (Elite 400 to 450, Pro 340 to 390, League/Club 280 to 340); the +15 tolerance is for genuine substance overflow, not the default. Added as a SCRIBE Phase 4 self-check and an ORIN Gate 15 clause (i), with the substantive rule in the product-page playbook.
