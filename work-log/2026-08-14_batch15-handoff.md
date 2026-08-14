# Handoff: state of play before Batch 15 selection (2026-08-14)

_For a cold agent or a new session. Read this, then `CLAUDE.md`, `SEO_BATCH_PROCESS.md`, and `strategy/sprint-backlog.md`. Mike picks the batch; nothing here is a selection._

**Note on this file's shape:** no format was specified for it in the session that produced it, so the structure below is proposed rather than inherited. The Step 2 per-batch handoff BLOCK (in `SEO_BATCH_PROCESS.md` step 9 flow) is a different artifact and unaffected.

## Where things stand

- `products-master.csv`: **151 rows.** Batches 13 and 14 both appended and both `shipped`, confirmed live in the store.
- Latest commit `186f8e4`, local and origin match, nothing unpushed.
- Sitemap state refreshed 2026-08-14: 14,369 live products, 696 collections.
- Gate and voice check both green across Batch 14; `scripts/test_voice_check.py` 13 tests, `scripts/test_batch_gate.py` 43 tests, all passing.

## The strategic finding that should drive Batch 15

Of 33 pack-qualified pages shipped, only **6 released an unqualified term that another optimized page now holds. 27 are orphaned on live but unoptimized incumbents.** Mike's reading, recorded in B-STRAT-01: pack succession is working, and what it exposed is that batch selection has been backwards. We optimize new pack SKUs carrying no measurable volume while the pages holding real demand sit untouched. Demand accrues to a shoe over its life; packs rotate every few months.

## Candidate incumbent queue, re-verified 2026-08-14

Volumes are DFS Google Ads US, measured. Incumbent URLs are the earliest live pack at that configuration.

| Term | Vol | Incumbent (earliest live) | Evidence |
|---|---|---|---|
| nike tiempo ligera pro turf | **320** | `nike-tiempo-ligera-pro-turf-soccer-shoes-attack-pack-sp26` | sitemap match |
| nike phantom 6 high elite fg | **210** | `...-high-elite-firm-ground-...-shadow-pack-fa25` | sitemap match |
| nike phantom 6 low pro turf | **140** | `nike-reactx-phantom-6-low-pro-turf-...-shadow-pack-fa25` | sitemap match |
| nike tiempo ligera pro fg | **140** | `nike-tiempo-ligera-pro-firm-ground-soccer-cleats-sp26` | sitemap match |
| nike phantom 6 low pro fg | 70 | `...-low-pro-firm-ground-...-scary-good-pack-fa25` | sitemap match |
| adidas predator elite fold over tongue ag | 70 | `...-fold-over-tongue-artificial-grass-...-radiant-blaze-pack-fa25` | **live-verified** |
| nike phantom 6 high academy turf | see note | `...-high-academy-turf-...-scary-good-pack-fa25` | sitemap match |
| nike phantom 6 low academy turf | see note | `...-low-academy-turf-...-max-voltage-pack-ho25` | sitemap match |
| nike vapor 17 elite fg | 30 | `...-vapor-17-elite-firm-ground-...-breakout-pack-su26` | sitemap match |
| nike tiempo maestro academy turf | 30 | `nike-tiempo-maestro-academy-turf-soccer-shoes-attack-pack-sp26` | **live-verified** |
| adidas f50 league indoor | 30 | `adidas-f50-league-indoor-advancement-pack-fa24` | **live-verified** (IH4577) |
| adidas f50 club turf | 20 | `adidas-f50-club-turf-soccer-shoes-electric-stealth-pack-fa25` | sitemap match |
| adidas f50 pro indoor | 20 | `adidas-f50-pro-indoor-vivid-horizon-pack-fa24` | sitemap match |
| adidas f50 club mid fg mg | 10 | `...-club-mid-firm-multi-ground-...-electric-stealth-pack-fa25` | sitemap match |
| adidas f50 league mid fg | 10 | `...-league-mid-firm-ground-...-road-to-glory-pack-sp26` | sitemap match |
| nike phantom 6 high club fg mg | 10 | `...-high-club-firm-multi-ground-...-shadow-pack-fa25` | **live-verified** |
| nike tiempo maestro club turf | 10 | `nike-tiempo-maestro-club-turf-soccer-shoes-break-em-pack-fa26` | sitemap match |
| nike vapor 17 elite ag | 10 | `...-vapor-17-elite-artificial-grass-...-breakout-pack-su26` | sitemap match |
| nike vapor 17 pro turf | 10 | `nike-vapor-17-pro-turf-soccer-shoes-shadow-pack-fa26` | sitemap match |

**Four rows are live-verified**, meaning the page was actually fetched and its H1, price and status read. **The other fifteen rest on the sitemap match alone.** Confirm the incumbent before dispatching any of them. Volumes are measured in every row; it is the URL column that carries the uncertainty.

**Phantom 6 Academy Turf note.** The 40/mo sits on the cut-less parent `nike phantom 6 academy turf`, which is NOT hierarchy-valid: five live High pages and eight live Low pages. It is queued as two cut-qualified terms and each needs its own volume pulled at selection. Do not target the parent.

**Removed from the queue: `nike vapor 17 pro` (70/mo).** Six live products span it across FG, turf, adult and junior, so it does not resolve to one product. There is no Nike Vapor collection; the nearest is `/collections/nike-mercurial`, status `inherited`. Routed to B-MERCH-01, which already names the Vapor/Superfly split.

**Row count provenance: the queue is NINETEEN terms, not the eighteen B-STRAT-01 first listed.** The difference is not drift. `nike phantom 6 academy turf` was found to be cut-ambiguous and split into `nike phantom 6 high academy turf` and `nike phantom 6 low academy turf`, taking 18 to 19. Separately, `nike vapor 17 pro` was removed to B-MERCH-01, so the original eighteen minus one plus two equals nineteen. Anyone reconciling this list against B-STRAT-01's first version should expect exactly that delta and nothing else.

## BATCH 15 SELECTION: required step before any brief is written

**Live-verify the incumbent of every SELECTED term. Only the selected ones, not all nineteen.**

For each term chosen for the batch, fetch the incumbent URL and confirm it by **H1, price, and status**, the same check applied to the four rows already marked live-verified. A term whose incumbent does not confirm **comes out of the batch** and goes back to the queue marked unresolved. It does not get briefed on a guess, and it does not get quietly swapped for a nearby page that happens to match.

**The URL column in the queue above is INDICATIVE, not verified.** Fifteen of the nineteen rows rest on a sitemap handle match alone, including the top four by volume (tiempo ligera pro turf 320, phantom 6 high elite fg 210, phantom 6 low pro turf 140, tiempo ligera pro fg 140). The volumes are measured and reliable; the URLs are inference from handle tokens.

Selecting from this queue without that verification step is precisely the failure mode the step exists to prevent: handle-token matching has already produced one wrong answer in this workstream (see WHAT NOT TO DO item 1), and a wrong incumbent means a brief written against the wrong page, a wrong pack-succession call, and a registry row that poisons the next batch's cannibalization check. The uncertainty in this column must not become certainty by being copied forward.

## Open items, by priority

- **B-KW-01 (High).** Does the generation token belong in F50 primaries, meta titles, and the collection retarget. All seven F50 incumbents earn ZERO impressions on the terms they hold; every impression they do earn is on `hyperfast` queries, one at position 4.4. `f50 hyperfast` runs 4,400 to 8,100/mo with nobody holding it. **Incumbent optimization does not capture this.** The two are complementary, not substitutes.
- **B-STRAT-01 (High).** The batch-selection finding above.
- **B-TECH-01 (High).** IH4577 declares a cross-page canonical pointing at KK1061. Possibly tag-driven grouping affecting an unknown number of pack siblings. Needs a sweep, not a one-page fix.
- **B-FIX-01 (Med).** Correction batch, ships as ONE batch: KK1049 weight, internal-link backfill on KC3952/KB8251/YT3FL1NM, customization-language sweep for Batches 5 to 9, and now B-DUP-03.
- **B-DUP-01/02/03, B-CAT-01/02, B-COPY-01, B-VOICE-01, B-AVATAR-01, B-REG-01, B-COLL-02/03, B-MERCH-01, B-PACK-01.** See the backlog.

## WHAT NOT TO DO

1. **Do not build a config match filter that ignores cut tokens. This has already cost one wrong answer.** On 2026-08-14 a filter matching `nike phantom 6 academy turf` returned ZERO live pages, and the conclusion drawn was that no page existed at that configuration, which would have routed a real 40/mo term to a merchandising-gap backlog item instead of the batch queue. Thirteen live pages existed. Cause: the term carries no cut token, but EVERY handle in the Phantom 6 Academy family carries `high` or `low`, so a filter requiring the term's tokens and excluding the cut tokens excluded the entire family. **Rule: before trusting a zero-match or a single-match result, list the family loosely and look at what tokens the handles systematically carry that the term does not.** Cut is the known case (`high`, `low`, `mid`); also check `laceless`, `lv8`, `nu3`, `reactx`, `flex`, `velcro`, `fold-over`, and signature PE tokens.
2. **Do not test the discriminator across the whole model family. Test it at the term's own tier AND surface.** The same sweep flagged `adidas f50 league indoor` and `adidas f50 club turf` as false matches because `mid` exists in the F50 League and Club families. It does not exist at indoor, and does not exist at Club turf. Both terms were fine. A token existing somewhere in a family says nothing about whether it exists at the configuration in question.
3. **Do not trust a subagent's report of its own output.** Codification checklist item 6. SCRIBE word counts have disagreed with `batch_gate.body_word_count` by up to 23 words. Re-derive any number from the gate before it enters a report, a commit message, or a registry row.
4. **Do not treat a status code as link validation.** Read the H1, the product count, and the AUDIENCE. `/collections/indoor-soccer-shoes` returns 200 with 32 products under the H1 "Kids' Indoor Soccer Shoes"; the adult target is `/collections/indoor`.
5. **Do not accept a gate PASS that also prints a skip.** The Batch 14 gate printed PASS alongside "Registry 1 primaries file absent; cannibalization checked intra-batch only". A check that did not run is not a pass.
6. **Do not push without an instruction.** The per-batch commit is autonomous; the push is Mike's call, every time.
