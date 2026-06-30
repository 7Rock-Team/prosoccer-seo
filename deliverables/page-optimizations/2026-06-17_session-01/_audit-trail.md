# Batch 4 Audit Trail -- 2026-06-17 session-01

Workforce-internal audit content per SKU. One file per batch. Implementer-facing content lives in each `<SKU>_<slug>_brief.md`.

## Batch metadata
- Batch: 4. First batch under the FULLY CORRECTED MCP architecture (today's allowlist + gating fixes): KIRA Phase 1 and all SCRIBE Phase 0 ran at the SUB-AGENT level; ORIN did NOT pre-fetch MCP payloads. Drive stays parent-read by design (ORIN read the white-label sheet).
- SKUs: 10 PDPs. 8 adidas Predator (Road to Glory Pack SP26) + 2 Nike Croatia 2026 jerseys.
- Composition: Predator tiers Elite/Pro/League/Club across FG/Turf/FG-MG; 7 fold-over + 1 standard (KK3725); 2 Junior + 1 Kids + 5 senior. Jerseys: Women's Home + Youth Away.
- Exemplars (dual): JP6237 (Predator Elite Fold-Over FG, sets fold-over-as-table-stakes baseline) and J000691 (Croatia Women's Home, sets women's-cut precedent).
- Brand IP: 8 Predators = adidas, FIFA-licensed (WC/FIFA/tournament/Road to Glory permitted, adidas lowercase). 2 Croatia jerseys = Nike, NON-FIFA (cycle language only; 0 FIFA/WC terms confirmed in both).
- Approval mode: APPROVE-EVERY-ACTION. Mike approved CHECKPOINT 1 (keyword strategy), CHECKPOINT 2 (dual exemplars + skeleton/forbidden-phrasings + J000691 fixes A-D), CHECKPOINT 3 (pre-commit gate, HQ2254 accepted at 333 words).

## Architecture / execution notes (corrected MCP architecture -- first clean run)
- **All 11 sub-agent dispatches (1 KIRA + 10 SCRIBE) succeeded at the sub-agent level.** Every MCP call (GSC, DataForSEO, Firecrawl) resolved at sub-agent context. Zero OAuth/inheritance failures, zero parent-level workaround. Confirms the `tools:` allowlist restoration (KIRA `be7ee36`; SCRIBE/VERITAS/RECON/ORIN `70adb8e`) holds in production. Drive (Category B / OAuth) remained parent-read by design; ORIN read the white-label sheet `1H-4Ax8C6IbfqCx2SToVidD4p9GR_rn16PePuvGMSA6Q`.
- **Fix 2 held (commit `7eddda1`): zero self-denial events across 10 SCRIBE draft writes.** No repeat of the Batch 3 ~244k-token loss. KJ6746's SCRIBE correctly held only its silo append (commit-stage shared-state) for ORIN, while auto-writing its brief + the audit-trail stub.
- **Fabrication guard active and effective.** See Defense-in-depth below. KJ6746's SCRIBE overrode an incorrect ORIN dispatch hypothesis (hook-and-loop closure) using Phase 0 scrape data (standard laces) -- prevention at SCRIBE level, not just gate-catch.
- **Tier-band codification (`49e5959`) working:** three siblings proactively trimmed off the ceiling (HQ2273 518->300, KJ6746 422->325, KK3725 465->389); J000691 exemplar trimmed to ~449. No write-to-ceiling drift.

## Per-SKU primary keyword assignments (for the white-label PDPs tab -- manual entry by Mike; ORIN reads, never writes)
| SKU | Tier / Surface / Audience | Primary keyword | Floor status | Pack/cycle-specific secondary |
|---|---|---|---|---|
| JP6237 | Elite FG, senior (exemplar) | adidas predator elite fold over tongue fg | sub-floor; query-level GSC pos 7.9 (733 impr) on adjacent term -- NOT own-page signal | adidas predator road to glory |
| HQ2254 | Pro Turf, senior | adidas predator pro turf | 260, clears; GSC pos 4.1 (561 impr) -- strongest in batch | adidas predator road to glory |
| JP6271 | League FG, senior | adidas predator league fg | 260, clears; reserved for this SKU in Batch 3 (HP9998 deferred it) | adidas predator road to glory |
| IH7212 | League Turf, senior | adidas predator league turf | 90, just-below-floor, held for surface uniqueness | adidas predator road to glory |
| HQ2273 | Club FG-MG, senior | adidas predator club | 260, clears (stepped up; Club FG 90 + FG-MG 70 both sub-floor) | adidas predator road to glory |
| HQ0007 | Jr League Turf, fold-over | adidas junior predator league turf fold over | 0* (no GSC signal yet) | adidas predator road to glory |
| KK3725 | Jr League Turf, standard | adidas junior predator league turf | 0* (no GSC signal yet) | adidas predator road to glory |
| KJ6746 | Kids Club FG-MG | adidas kids predator club | 0* (no GSC signal yet) | adidas predator road to glory |
| J000691 | Women's Home jersey | croatia womens home jersey 2026 | 0* (no GSC signal yet); KD 14 (base-query) | croatia 2026 home jersey women |
| J000695 | Youth Away jersey | croatia youth away jersey 2026 | 0* (no GSC signal yet); KD 14 (base-query) | croatia 2026 away jersey youth |

Arbitration of record: HQ0007 (fold-over) took the construction-qualified `...turf fold over`; KK3725 (standard) took the clean head `adidas junior predator league turf`. Rationale: append the differentiating attribute to the variant that owns it (mirrors Batch 3 F50 League Mid vs League). Croatia matrix kept clean: men's-away `croatia jersey 2026` (J000693, Batch 2) untouched; women's-home and youth-away qualified to avoid cannibalizing it and the existing women's-away page + future youth-home (J000692, on sheet, not in batch).

## Defense-in-depth: gate items caught / corrected
1. **J000691 fabrication (caught at ORIN CHECKPOINT-2 gate; 3rd fabrication-pattern instance Batch 3->4).** Exemplar draft asserted "best qualifying run in the program's history, a group topped undefeated, with Luka Modric still pulling the strings" -- unverified forward/squad claims. Replaced with evergreen, brand-IP-compliant copy (2018 final, 2022 podium, golden generation). Also neutralized "Vatreni" (verified men's-team nickname; women's team is "Lavice"; product is the Croatia home kit in a women's cut, so gender/team-neutral "Croatia"/"the national team" was used).
2. **J000691 US-spelling + redundancy (ORIN gate).** "colour shown White/Red" (British, copied from Nike global scrape) eliminated by merging the redundant colorway Product Details bullet (7->6); landed body under the 465 tolerance. Single `/collections/croatia` link retained (FAQ); Short-Desc CTA varied from Meta CTA.
3. **KJ6746 closure (PREVENTED at SCRIBE level; 4th fabrication-pattern instance).** ORIN dispatch hypothesized hook-and-loop/easy-on closure per the Kids lane spec. SCRIBE's Phase 0 scrape returned "Lace closure"; SCRIBE overrode the hypothesis, described standard laces accurately, and wrote FAQ 1 honestly around parent-managed lacing. Scrape data wins over dispatch hypothesis -- the discipline the post-batch fabrication codification will formalize.
4. **KJ6746 weight omission (fabrication guard).** No weight on the live PDP -> no weight bullet invented (contrast verified weights on the senior siblings).

All KD/Difficulty cells left blank where DataForSEO returned no value (no fabricated scores; HP9973 Batch-3 failure mode did not recur).

## Internal link validation (content signals, not status codes alone) -- ORIN + per-SCRIBE, 2026-06-17
- `/collections/adidas-predator` -> 200, title "adidas Predator Soccer Cleats..." , ~50-162 product links across validations, hundreds of Predator mentions. VALID. (used by JP6237, HQ2254, IH7212, HQ2273, HQ0007, KJ6746)
- `/collections/adidas-road-to-glory-pack` -> 200, title "adidas Road to Glory Pack Soccer Cleats", 33-148 product links, Road-to-Glory mentions. VALID. (used by HQ2254, JP6271, IH7212, HQ2273)
- `/collections/croatia` -> 200, H1 "Croatia National Soccer Team Jerseys and Gear", 10 products, full Nike Croatia line. VALID, not soft-404. (J000691, J000695)
- PDP->PDP: KK3725 -> HQ0007 live PDP ($79.99, in stock, validated in related-products rail) as the twin comparison cross-link. VALID.
- Confirmed-404 (avoided): `/collections/youth-soccer-cleats`, `/collections/kids-soccer-cleats`.

## Standing flags for Mike
- **URL handles >70 chars on 9 of 10** (J000691 = 51, the lone clean one; KK3725 = 73, barely over; Predators 77-95). All flagged in-brief, none auto-changed (301 equity risk, Misha coordination). Forward-only per standing policy.
- **og:image `http://` theme-level pattern CONFIRMED** across 6+ PDPs (Phantom 6 High Elite + HQ2254 + JP6271 + HQ2273 + HQ0007 + J000691). Theme-level fix candidate, not per-PDP. Escalated to Misha-audit-request in standing follow-ups.
- **NEW theme bug: `<title>` truncation (HQ2254).** Live storefront `<title>` cuts mid-parenthesis at "Pack ("; og:title + twitter:title affected. Theme template likely truncates without escape handling. Misha/VERITAS audit candidate.
- **Image Alt Text** in each brief is best-effort (no live gallery visibility); map to actual gallery slots at publish.
- **Jersey taxonomy node** not standardized; match siblings J000693/J000691 at implementation.

## Token / architecture validation data (first clean sub-agent baseline -- Fix 3 audit input)
- KIRA Phase 1: 13 MCP calls (9 GSC + 4 DataForSEO), all sub-agent-level success; ~90-120k tokens (dominated by 3 verbose DataForSEO `keyword_overview` payloads; `detect_quick_wins` dumped full site 1M chars, correctly offloaded to disk). DataForSEO MTD ~$0.02-0.04.
- SCRIBE (each of 10): ~3 Firecrawl scrapes (1 PDP Phase 0 + ~2 link validations), large collection scrapes offloaded to disk; ~60-95k tokens consumed each (scrape payloads + playbook reads). 0 DataForSEO (keywords pre-approved by KIRA), minimal Tavily.
- Efficiency findings for the Fix 3 audit: (a) DataForSEO `keyword_overview` returns far more than a floor check needs -- lighter call pattern would cut spend; (b) `detect_quick_wins` must be called page-targeted, not site-wide (offload-to-disk already works correctly).

## Post-batch correction -- 2026-06-29: KK3725 body H2 casing

3 violations of the 6/17 codified sentence-case rule (commit `e6bdec9`) corrected in the KK3725 brief: lowercase-initial first words on all 3 editorial body H2s (the/what/who -> The/What/Who). The brief's FAQ H3s and structural H2s ("Product Details:", "Fit Notes", "Care and Maintenance", "FAQs about...") were already correct and unchanged.

Detected during Mike's 6/29 Shopify implementation when manually verifying brief content against codified house style. A full audit of all 10 Batch 4 briefs confirmed KK3725 was the SOLE violator: the other 9 briefs' editorial body H2s are clean sentence case, all FAQ H3 first words are uppercase batch-wide, and no editorial H2 carries reverse Title-Case drift.

Enforcement gap analysis: SCRIBE Phase 4 self-check + ORIN Gate 15 both passed the brief despite the violation (hypothesis: gates checked against Title-Case drift / all-caps rather than an explicit first-character-uppercase test, so a lowercase first word read as sentence-case-adjacent and slipped through). voice_check.py casing detection was deliberately deferred at codification time (`e6bdec9`) citing brand-token false-positive risk; this batch's drift surfaced the gap. Codification reinforcement (collection-page scope) and a scope-limited voice_check.py addition (flag lowercase-initial editorial body H2s, "adidas" excepted -- cannot false-positive on brand tokens because the exception is explicit) follow in the same commit.

Live PDP corrections are operator-driven: Mike is fixing all Batch 4 implementations directly in Shopify admin. No script-side live changes.

## Per-SKU audit notes

### SKU JP6237 -- adidas Predator Elite Fold-Over Tongue FG (PREDATOR EXEMPLAR)
- **Role:** dual exemplar; sets the fold-over-as-table-stakes baseline + the structural skeleton for the 7 Predator siblings.
- **Phase 0:** status 200, clean Short/Long separation. Specs scrape-sourced: Primeknit one-piece, Nanostrike+, Strikeframe FG plate, Powerspine, weight 203g -> 7.2 oz (US-first dual notation). Current live copy carried two language violations (a UK footwear term and an AI-cliche verb); the rewrite removed both.
- **Differentiation:** hook = tempo-setter / conductor ("Some players chase the game. You set it."), DISTINCT from HP9973's lock-picker/Beckham-Zidane. Fold-over framed as Elite-tier-standard, not hero. Heritage beat = "rubber-ribbed originals," avoids HP9973's claimed beats.
- **Links:** 1 placed (`/collections/adidas-predator`, FAQ); pack link held available.
- **Fields:** body 438 words (Elite 400-450). Handle 88 chars (flagged). All 15 gates pass; voice check exit 0.
- **Note:** "No.10 picks the final pass" sits adjacent to HP9973's playmaker territory -- acceptable in exemplar (shared Elite-control avatar, under threshold), added to sibling forbidden list to block propagation.

### SKU HQ2254 -- adidas Predator Pro Fold-Over Turf
- **Phase 0:** 200, clean separation. Specs scrape-sourced: synthetic+textile upper, Nanostrike Pro (not +), Powerspine, Lightstrike, turf outsole dense short studs, 249g -> 8.8 oz. Tech ladder confirmed stepped down from Elite.
- **Differentiation:** "control player who lives on turf" / small-sided-and-fast hook; Pro-tier (near-Elite without Elite price). No tempo/conductor reuse.
- **Links:** 2 (`/collections/adidas-predator`, `/collections/adidas-road-to-glory-pack`), both content-validated.
- **Fields:** editorial prose 333 (7 under Pro 340 floor; ACCEPTED at CHECKPOINT 3 -- complete and tight, no padding added). Handle 84 (flagged). Gates pass. Two in-pass fixes: a UK footwear term swapped to the US term; a capitalized brand token in a quoted validation note lowercased. og:image http:// + `<title>` truncation flagged.

### SKU JP6271 -- adidas Predator League Fold-Over Tongue FG
- **Phase 0:** 200, Short/Long separate. Specs: Nanostrike mesh (not +), no Primeknit, Strikeframe FG plate, Powerspine, 232g -> 8.2 oz. Tech ladder stepped down confirmed.
- **Differentiation:** "the player who shows up every week" weekend-player value hook; League-tier control on firm ground. Claims the Batch-3-reserved primary cleanly.
- **Links:** 2, content-validated (148 + 159 product cards).
- **Fields:** editorial prose 340 (top of League 280-340 band). Handle 89 (flagged). Gates pass.

### SKU IH7212 -- adidas Predator League Fold-Over Tongue Turf
- **Phase 0:** 200, separates. Specs: synthetic+textile upper, Nanostrike+, Powerspine, Strikeframe, turf rubber outsole (many short non-removable studs), 254g -> 9 oz. Stepped down from Elite ($279.99 sibling vs $99.99).
- **Differentiation:** "your pitch is turf, so your shoe should be too" hook; League-value on turf. Differentiated from batch-twin JP6271 by surface (turf vs FG); from HQ2254 by tier (League below Pro).
- **Links:** 2, content-validated (33 + 107 products).
- **Fields:** editorial prose 285 (League band); full body 438. Handle 86 (flagged). Gates pass (one in-pass: the scraped live H1 carried a capitalized brand token inside a validation note, reworded).

### SKU HQ2273 -- adidas Predator Club Fold-Over Tongue FG-MG
- **Phase 0:** 200, separates cleanly. Specs: soft synthetic upper textured grip, fold-over tongue, FG-MG outsole, textile lining, synthetic outsole, 249g -> 8.8 oz. Most-reduced tech ladder confirmed (no Nanostrike+/Strikeframe/Powerspine -> none claimed). $69.99 entry tier.
- **Differentiation:** "first real pair of Predators, or your first in a while" entry/returning-player hook + FG-MG do-it-all outsole; distinct from HP9998 value-pick framing. Owns bare senior `adidas predator club` (kids-qualified term left for KJ6746).
- **Links:** 2, content-validated.
- **Fields:** editorial prose 300 (Club band); full body excl FAQ 458 (<465). Handle 92 (flagged). Gates pass (trimmed from 518). og:image http:// flagged.

### SKU HQ0007 -- adidas Junior Predator League Fold-Over Tongue Turf
- **Phase 0:** 200, separates. Specs: Nanostrike mesh upper + haptic overlay, fold-over tongue, turf (TF) outsole, regular fit + lace closure, textile lining, 175g -> 6.2 oz. Current live copy carried a UK footwear term; corrected to the US term.
- **Differentiation:** parent-facing (ages 9-14); "cleaner surface for the kid who loves to shoot" / step-up build hook. Owns the FOLD-OVER + step-up angle vs batch-twin KK3725 (standard/dependable); differentiated from HP9998 (FG fold-over) by surface; from HP9970 parent-young-striker by hook.
- **Links:** 2, content-validated (162 + 128 refs).
- **Fields:** body 300 (junior League band 280-340). Handle 90 (flagged). Gates pass. Entity "Solar Turbo" = scrape-confirmed colorway. og:image http:// flagged.

### SKU KK3725 -- adidas Junior Predator League Turf (STANDARD construction)
- **Phase 0:** 200, separates. **Closure CONFIRMED standard: "laced floating tongue" + "Lace closure" -- NOT fold-over** (fold-over framing fully avoided). Specs: Nanostrike mesh + haptic overlay, regular fit, textile sockliner, rubber TF outsole, 175g -> 6.2 oz. Colorway Solar Turbo / Thermal Chrome / Core Black. $49.99.
- **Differentiation:** parent-facing dependable-everyday workhorse ("two practices, a Saturday match"); owns the clean head term. Differentiated from twin HQ0007 (fold-over/step-up) by construction + keyword + hook; no convergence.
- **Links:** 1 placed -- PDP->PDP to twin HQ0007's live page (anchor "fold-over tongue turf shoe", FAQ) as comparison cross-link for a comparison-shopping parent; `/collections/adidas-predator` validated + available, held at 1.
- **Fields:** editorial prose 282 (junior League band); full body 389. Handle 73 (just over 70, flagged). Gates pass (trimmed from 465).

### SKU KJ6746 -- adidas Kids' Predator Club Fold-Over Tongue FG-MG (Road to Glory Pack SP26)

**Tier / role:** FIRST-EVER KIDS PDP for the workforce. Tier 1 foundational (sets KIDS-tier positioning precedent). Soccer Cleats category (template VALIDATED v1).

**Eligibility:** Mike-verified in-stock at submission, 2026-06-17 (Shopify admin). Phase 0 scrape confirms live, in stock ("only 3 items left", "Ships within 1-2 business days"), $49.99, sizes 10.5K-13.5K youth.

**Brand-IP classification:** adidas product page = Adidas-licensed context. FIFA-trademarked terminology family ("World Cup", "FIFA", "WC") is PERMITTED here. None used in copy anyway (kept evergreen; year "2026" used once in the size/season-cycle sense via "into the 2026 cycle" was NOT used in final; no FIFA phrase appears). Compliance scan across all six fields + link anchors: clean. adidas lowercase throughout (voice_check `\bAdidas\b` = pass).

**Phase 0 scrape (fabrication guard, active -- caught 3x prior):**
- Status 200, clean Short/Long separation (no blocker).
- **Closure = LACE closure** (live PDP spec bullet "Lace closure"). The dispatch lane-spec hypothesis of hook-and-loop / elastic self-don is FALSE for this SKU. Copy describes standard laces accurately; the easy-on/off angle was NOT used. FAQ 1 honestly addresses "can a young child put these on themselves" given laces (needs a hand the first few times; double-knot before kickoff).
- **Weight = NOT listed** on PDP. NO weight invented; no weight bullet in Product Details (contrast HQ2273 senior, which had a verified 8.8 oz; JP6237 Elite had 7.2 oz). Correct to omit.
- Confirmed specs (live bullets): Regular fit; Synthetic upper (soft, textured); Textile sockliner; Synthetic outsole (FG-MG); Fold-over tongue.
- Colorway: Solar Turbo / Thermal Chrome / Core Black.
- Youth sizes 10.5K-13.5K confirm the 4-8 / youngest-players age band that anchors the lane.

**Keyword selection rationale:**
- Primary `adidas kids predator club` -- KIRA-approved, no GSC signal yet (Volume 0*). Selected as the KIDS-qualified term; the unqualified `adidas predator club` (260/mo) is CLAIMED by senior sibling HQ2273. Audience-qualified primary avoids cannibalizing the senior page (Registry-1 cross-check satisfied via lane spec).
- Secondary (pack-specific) `adidas predator road to glory` -- first secondary row, floor-exempt long-tail, woven into prose (Short Desc + Product Details bullet + Fit/FAQ context, 7 total mentions across fields).
- Supporting (volume-selected, buy-intent density): `adidas predator youth`, `kids predator cleats`. "youth"/"kids" natural variants distributed in body. No KIRA difficulty returned -> Difficulty cells blank (not fabricated).
- Gate 12: primary present across all required fields; body exact-match "predator club" x2 + natural "kids"/"youth" variants, well under stuffing cap.

**Avatar scope:**
- Primary: Jennifer (The Mom), AIDAR Awareness/Interest. Parent of a 4-8 first-time player. Pain frames engaged: "Growth Spurt Tax" (FAQ 2 + Fit Notes, half-size-up-for-runway), "Turf Anxiety" (FAQ 3, FG-MG vs turf surface match), durability worry (FAQ 4). Voice-of-customer "I just want him to stop complaining" maps to the comfort-from-first-kick hook.
- Secondary: the young player themself (Tyler-adjacent but pre-competitive) -- "the Predator look they see the big players wearing" serves the kid's identity desire, but the PARENT is the buyer/decider, so Jennifer leads headline + meta + hook.
- Excluded: Carlos (collector/pack-completionism -- deliberately why the second internal link to the Road to Glory Pack collection was held; a kids first-pair buyer is not on a pack-completion path). Mike the Coach (team-bulk routes through team-orders, not a kids single-pair PDP).
- Cross-avatar landing: a grandparent or gift-buyer might land here; the "their first real pair" + gift-box-friendly framing covers them without diluting Jennifer.

**Differentiation (pack/series + silo):**
- vs HQ2273 (SENIOR Club FG-MG, owns `adidas predator club`): differentiated by AUDIENCE (kids 4-8 vs adult/returning rec player). HQ2273 hook = "First real pair of Predators, or your first in a while?" (adult). KJ6746 hook = "Their first real pair of Predators" (parent-of-young-child, third-person about the kid). No prose overlap.
- vs Batch-3 junior 9-14 lane (HP9970 "kid who loves to strike/shoot"; HP9998 "the one kid who wants the ball near goal"): KJ6746 is a DISTINCT younger lane (4-8 first-cleats / comfort / confidence / parent-managed laces), NOT the competitive-young-striker frame. No reuse of junior hooks.
- Forbidden phrasings honored: no JP6237 tempo/conductor lane; no HP9973 lock-picker/Beckham/Zidane; no laceless (HP9967); no AG framing (HP9971); no Batch-4 junior twin hooks (HQ0007 "kid who loves to shoot"/"step-up build", KK3725 "dependable everyday"). Fresh 4-8 hook centered on ease/confidence/first-cleats.

**Internal links (1, body only, content-signal validated):**
- `https://www.prosoccer.com/collections/adidas-predator` (anchor "Predator line", FAQ answer 5 "when do we move up to Junior"). Validated 2026-06-17: status 200, full collection page returned, 517 "Predator" mentions, 159 product links, correct title "adidas Predator Soccer Cleats for Control" (also independently validated today in HQ2273). Not a soft-404.
- Held second slot at one: Road to Glory Pack collection validated clean (200, 133 "Road to Glory" mentions, 148 product links) but pack-completionism is a Carlos path, not the kids-first-pair parent decision (comfort/fit/surface). MEMORY precedent `feedback_internal-link-selection-pattern.md`: prefer the more committed-buyer / non-duplicate discovery path; the Predator-line "size-up" link is load-bearing, the pack link is not. Available if Mike wants it added.
- Did NOT link `/collections/youth-soccer-cleats` or `/collections/kids-soccer-cleats` per dispatch (both 404).

**Field lengths (PDP hard limits):** Title 84 (30-100, pass). Short Desc 52 words / 295 chars (50-100 word band, pass). Description body 325 content words excl H2 headings (Club/kids target band 280-340, pass; trimmed from initial 422 over-write via Path A prose-tightening, the Batch-3 write-to-ceiling anti-pattern avoided). Meta Title input 39 chars (under ~48-50, pass). Meta Desc 156 (<=160, trimmed from 167->163->156). URL handle 95 chars (>70: FLAGGED, no auto-change, 301/Misha coordination).

**Gates self-check (failures only):** none. All 14 gates + Phase 4 editorial/image-precision/parallel-construction/measurement disciplines pass. Voice check PASSED (no em/en-dash, no forbidden words/openers, adidas lowercase, no UK `boots`). H2 casing split correct (editorial sentence case; structural Title Case). FAQ hierarchy correct (H2 "FAQs about the Kids Predator Club" + H3 per question). No prices/counts/brand-stacking in body. No measurements (none on PDP -> none invented).

**Tool/token data:** Firecrawl 3 scrapes this SKU (KJ6746 PDP = 1 credit; 2 link-validation collection scrapes already validated same-day for HQ2273, marginal). DataForSEO: 0 (keywords arrived pre-approved from KIRA). voice_check.py: 3 runs, all pass.

**KIDS-tier precedent set (recorded in silo):** parent-of-younger-child (4-8) lane, anchored on "their first real pair," comfort-from-first-kick, confidence -- distinct from both senior adult Club and Junior (9-14) competitive-young-striker frames. Ease/closure features must be scrape-confirmed per SKU, never assumed (this Club uses standard laces, so FAQ 1 honestly addresses parent-managed lacing rather than self-don).

### SKU J000691 -- Nike 2026 Croatia Women's Stadium Home Soccer Jersey (JERSEY EXEMPLAR)
- **Role:** dual exemplar; sets the women's-cut positioning precedent + the jersey skeleton for J000695.
- **Phase 0:** 200, clean Short/Long separation. Women's cut, Stadium replica tier, red-and-white sahovnica home colorway, Dri-FIT 100% polyester. og:image http:// flagged.
- **Brand IP:** Nike = NON-Adidas; FIFA/WC forbidden. 0 restricted terms confirmed; cycle language only.
- **Differentiation:** "cut for her, not borrowed off the men's rack" women's-cut identity, home red/white checkerboard; distinct from J000693 men's-away anthem-moment.
- **ORIN gate fixes applied:** Fix A (fabrication -> evergreen 2018-final/2022-podium rewrite, "Vatreni"->gender-neutral); Fix B (colour->color via bullet merge); Fix C (body ~470->~449, under 465); Fix D (single `/collections/croatia` link, varied CTAs). Re-ran voice check: pass; 0 residual Vatreni/colour/FIFA.
- **Links:** 1 (`/collections/croatia`, FAQ), content-validated (H1, 10 products). Handle 51 (clean). Gates pass.

### SKU J000695 -- Nike 2026 Croatia Youth Stadium Away Soccer Jersey
- **Phase 0:** 200. **Away colorway CONFIRMED: Deep Royal Blue / Hyper Royal / White** with sahovnica. Youth sizes YXS-YXL, Stadium tier, Dri-FIT 100% polyester, customizable, $84.99.
- **Brand IP:** Nike = NON-Adidas; FIFA/WC forbidden. 0 restricted terms confirmed across all 6 fields + anchor; cycle/evergreen language only. Note: the live `/collections/croatia` page uses "World Cup"/"Vatreni" in its OWN copy (pre-existing, out of scope); the PDP brief + anchor stay compliant and team-neutral.
- **Evergreen discipline (applied the J000691 lesson):** only verifiable facts (2018 final, 2022 podium, sahovnica/coat-of-arms, Kockasti, Nike-before-adidas); no invented roster/squad/current-events; "Vatreni" NOT used (team-neutral framing).
- **Differentiation:** parent-buying-for-young-fan away hook; distinct from J000693 (adult men's away) via parent/youth lens; from J000691 (women's home) via age + away-blue colorway. Youth sizing focus.
- **Links:** 1 (`/collections/croatia`, FAQ), content-validated. US-first dual notation on care temps (86°F (30°C)); youth sizes US-only. Body ~292 words + bullets (<465). Gates pass; voice check exit 0. Taxonomy node flagged (match siblings).
