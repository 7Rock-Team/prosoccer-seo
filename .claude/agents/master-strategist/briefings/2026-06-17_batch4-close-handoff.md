# Session-close handoff -- Batch 4 (2026-06-17)

Batch 4 (10 PDPs: 8 adidas Predator Road to Glory SP26 + 2 Nike Croatia 2026 jerseys) shipped and pushed to origin/main: commit `3d73894` (10 briefs + consolidated `_audit-trail.md` + Registry 2 silo appends). Full per-SKU detail in `deliverables/page-optimizations/2026-06-17_session-01/_audit-trail.md`.

**First batch under the fully corrected sub-agent MCP architecture.** All 11 sub-agent dispatches (1 KIRA Phase 1 + 10 SCRIBE) ran their own MCP work at the sub-agent level; every call succeeded. ORIN orchestrated without pre-fetching payloads; Drive stayed parent-read. Fix 2 held (zero self-denial across 10 draft writes). Architectural validation: confirmed in production.

## Standing follow-ups for next session opening

### RESOLVED 2026-06-29 -- Sentence-case H2 enforcement gap closed + collection-page scope added

Triggered by KK3725: Batch 4's standard-construction Junior League Turf brief shipped 3 lowercase-initial editorial body H2s, violating the 6/17 sentence-case codification (`e6bdec9`), and passed BOTH SCRIBE Phase 4 and ORIN Gate 15. Surfaced during Mike's 6/29 Shopify implementation. Closed in a single coherent codification commit (2026-06-29):

- **Enforcement gap CLOSED.** `scripts/voice_check.py` now flags lowercase-initial editorial body H2s (region between `### Description` and `## Product Details`, "adidas" excepted). Scope-limited so it cannot false-positive on brand tokens, which retires the original deferral concern; reverse Title-Case drift stays with the two human-style gates. Unit tests: `scripts/test_voice_check.py` (4 spec cases + 2 scoping guards, all green). All 10 Batch 4 briefs pass under the new check.
- **Collection page copy scope ADDED.** The split-casing discipline now explicitly covers collection page copy (editorial body H2s sentence case, structural H2s Title Case, FAQ H3 questions sentence case), effective Batch 5 onward, per Mike's 6/29 request. Codified in `context/workforce-conventions.md` 'H2 title casing and Product Details H2 format'.
- **KK3725 brief CORRECTED** in `deliverables/page-optimizations/2026-06-17_session-01/` (3 H2 capitalizations + 2026-06-29 `_audit-trail.md` entry). Audit confirmed KK3725 was the SOLE violator across all 10 Batch 4 briefs; the other 9 were already clean.
- **Live PDP corrections: Mike-owned.** Mike is fixing all Batch 4 implementations directly in Shopify admin. Not a script-side concern.

### RESOLVED 2026-06-29 (B) -- Batch 5 pre-dispatch codification + silo guardrails

Batch 5 (11 URLs: 5 Copa Pure IV senior, 1 Superfly 11 Pro FG, 1 Tiempo Maestro Academy Turf, 4 jerseys [Croatia Youth Home J000692-CRFT, Croatia Women's Away J000694-CRFT, Bosnia youth Home 7651TX3926, Bosnia youth Away 7651TX3927]) prepared. Pre-flight triage corrected three "firsts" framings (Superfly / Maestro / Copa silos already exist) and pre-empted three fabrication traps before any brief was written. Pre-dispatch single commit shipped:
- **Fabrication-mode codification (the standing HIGH-PRIORITY item below): DONE.** SCRIBE Phase 4 self-check (scrape-data-wins + tournament-status forbidden patterns) + ORIN Gate 15 clause (m) + `context/workforce-conventions.md` 'Fabrication guard and tournament-status discipline'. Six case studies incl. two Batch 5 pre-empts (Bosnia "only WC", Copa "leather"/"Sprintframe").
- **Nike tier nomenclature** codified (Elite > Pro > Academy > Club; Nike Academy maps to adidas League; Academy uses the League/Club word band).
- **Non-FIFA brand language discipline** codified (Kelme, like Nike, runs cycle-language-only; FIFA terms key on the adidas license). Kelme added to `brand-ip-constraints.md` affiliation reference.
- **Silo guardrails (NOT per-SKU log entries):** new "Pre-dispatch reference / guardrails" sections added to copa.md, national-team-jerseys.md (Bosnia), mercurial.md (Superfly Pro), tiempo.md (Maestro Academy Turf). The append-only per-SKU log stays pure and gets Batch 5 entries post-ship per protocol. KI0662 Bernardo Silva entry left untouched (historical record).
- Croatia Women's Away SKU J000694-CRFT verified via Shopify Admin API; still missing from the white-label sheet (Mike to add the row).
- NEXT: dispatch KIRA Phase 1 on the 11 URLs; hold at Checkpoint 1.

### Wave 1 gate / Checkpoint 2b (2026-06-30) -- exemplars + codification maturation

Wave 1 exemplars: KI0586 Copa Pure IV Elite (Copa-family) + 7651TX3926 Bosnia Youth Home. The ORIN gate caught a real defect in KI0586 before skeleton extraction (prevented 5-brief propagation):
- **Casing codification maturation cycle:** 6/17 sentence-case rule (`e6bdec9`) -> 6/29 voice_check.py `##`-level deterministic backstop (`ea39bcf`) -> 6/30 heading-level-agnostic backstop. KI0586 used `####` body headers (one level too deep) with lowercase first words, which the `##`-only check missed; voice_check.py now detects lowercase editorial body headers at ANY heading level (`##` .. `#####`), with a TDD regression test built from KI0586's exact original headers (fails pre-patch = gap proof, passes post-patch, stays in suite forever). Same maturation pattern as the original KK3725 surface: the rule gets stronger under production load.
- Fabrication discipline validated on first live test: KI0586 SCRIBE caught the copa.md "Solar Red" guardrail error against the live scrape ("Solar Turbo / Ivory / Core Black") and applied scrape-wins; copa.md guardrail corrected.
- Bosnia exemplar passed clean (2014 WC debut anchor, Zmajevi gender-neutral, Kelme TIME-SENSITIVE, cycle-language-only, identity prose).

STANDING ITEMS surfaced (carry to next Tony sync):
- **Bosnia men's jersey PDP gap (sharpened from Checkpoint 1):** the men's Bosnia Home jersey PDP EXISTS, is in stock, and is NOT tracked in the white-label sheet; it currently absorbs the 1,600-9,900/mo Bosnia head-term demand unoptimized. Recommendation: add a men's Bosnia jersey to a future SEO batch + add the sheet row. Actionable, not speculative.
- **Bosnia-specific collection** `/collections/bosnia-and-herzegovina-national-soccer-team-jerseys-apparel` validated live (H1 + 3 products); now the internal-link target for the Bosnia briefs (applied to the Home exemplar; Wave 2 Away sibling to use it).
- **White-label sheet rows pending (Mike-side):** J000694-CRFT Croatia Women's Away; men's Bosnia Home PDP.

### Batch 5 close (2026-06-30) -- escalations + standing items

**ESCALATION (Tony + Misha) -- theme-level brand-IP exposure.** Found during Batch 5 SEO production; 4 separate SCRIBE quality gates flagged it. The live storefront renders sitewide chrome banners "ROAD TO THE '26 WORLD CUP" / "IT'S WORLD CUP TIME, BABY!" on NON-FIFA-licensed brand PDPs (Nike, Kelme). Brand-license restrictions follow the BRAND, not the storefront: ProSoccer is not FIFA-licensed, so Nike/Kelme pages cannot display World Cup promotional chrome any more than the body copy can use FIFA terms. This is real legal-compliance exposure (FIFA enforcement watches exactly this), and it NEGATES the brief-copy discipline we codified (no FIFA/WC on non-adidas pages) at the theme layer. **Frame for Tony:** brief copy discipline is being undermined by sitewide chrome on those same pages; needs theme-level conditional logic preventing tournament chrome on non-FIFA-licensed vendor pages, regardless of WC timing. **Misha:** implementation. **Standing convention (permanent, codify regardless of cycle):** tournament/WC chrome renders ONLY when the product vendor is FIFA-licensed (adidas family for current tournaments), NEVER on Nike/Kelme/other non-FIFA-licensed vendor pages. Misha audit-request stack is now: og:image `http://`, `<title>` truncation, AND this theme-level brand-IP conditional logic.

**Bosnia men's PDP gap (sharpened, Tony sync):** men's Bosnia Home/Away PDPs EXIST (the Bosnia collection shows 3 live men's products), are in stock, and are NOT tracked in the white-label sheet; they currently absorb the 1,600-9,900/mo Bosnia head-term demand unoptimized. Add a men's Bosnia jersey to a future SEO batch + add the sheet rows.

**Closed this batch (codification maturation):**
- Copa silo guardrail refined to the tier x surface matrix (calfskin FG Elite/Pro only; Fusionfeel synthetic on Pro Turf + both League; Comfort Frame vs Comfort Plate TPU vs rubber turf; tongue tier-variable). Scrape-wins applied at the guardrail layer, same pattern as the Wave 1 Solar Red -> Solar Turbo correction.
- Croatia jersey word-count tension closed: national-team-jersey length precedent codified in the product-page-playbook (jerseys measured full-body, run above the generic Complex 465 ceiling, hold sibling parity within a nation set). J000692 accepted at 534.

**White-label sheet rows to add (Mike-side):** J000694-CRFT Croatia Women's Away; men's Bosnia Home PDP.
**Implementation notes (Mike-side):** J000694 gallery image mislabel ("Croatia Men's Away (Modric)" on the women's-away page) -- apply the brief's corrected alt text. URL handles over 70 on KI0586 (75) + KI0653 (75) -- 301 equity risk, Misha coordination only if Mike opts in.

### HIGH PRIORITY -- post-Batch-4 codification commits

- **Fabrication-mode SCRIBE Phase 4 self-check codification.** **RESOLVED 2026-06-29** (folded into the Batch 5 pre-dispatch commit; see 'RESOLVED 2026-06-29 (B)' above). Original urgency note (4th pattern instance; trigger from Batch 3 close ACTIVATED): Four case studies now: (1) HP9973 fabricated KD scores [Batch 3]; (2) KK1307 invented retail/store detail [Batch 3]; (3) J000691 unverified current-events / squad / qualifying claims [Batch 4, caught at gate]; (4) KJ6746 closure hypothesis [Batch 4, PREVENTED at SCRIBE level by Phase 0 scrape verification]. Codification scope:
  - No fabricated KD scores (blank if not retrieved) -- existing rule, formalize.
  - No fabricated retail / store / operational / policy specifics unless in source data.
  - No fabricated current-events / squad / qualifying / tournament-status claims; prefer evergreen (verifiable historical results, established product specs, documented heritage).
  - **Dispatch-hypothesis verification (the KJ6746 lesson):** ORIN dispatch hypotheses (closure type, weight, construction, features) are starting points, NOT facts. SCRIBE MUST verify against Phase 0 scrape data before writing. If scrape contradicts the hypothesis, scrape wins and SCRIBE rewrites accordingly.
  - Tournament-status subtype: forbidden patterns for active-tournament progression / "best run ever" superlatives / present-tense squad claims (preventive for future tournament-relevant national-team batches).
  - Mechanism: SCRIBE Phase 4 self-check + ORIN gate clause; consider whether any of this is script-enforceable (most is not -- it is a judgment discipline).

- **Fix 3: token-efficiency audit -- baseline NOW AVAILABLE (first clean sub-agent run).** Run the audit using Batch 4 data (below). Specific targets surfaced:
  - DataForSEO `keyword_overview` returns far more per-keyword detail than a floor check needs; a lighter call pattern (or post-filter) would cut KIRA spend materially.
  - `detect_quick_wins` must be called page-targeted; site-wide it dumps ~1M chars (2,508 rows). Offload-to-disk already works correctly.
  - Parallel sub-agent dispatch trades token efficiency for wall-clock + architectural correctness: each of the 10 SCRIBE agents independently re-loaded playbooks + exemplar + ran its own Phase 0 scrape (no shared context across parallel sub-agents). Quantify the redundant-context-load cost vs the old parent-level approach.

### Misha / VERITAS coordination (EXPANDED from flag to audit-request)

- **og:image `http://` -- theme-level pattern CONFIRMED across 6+ PDPs:** Phantom 6 High Elite (Day 3) + HQ2254 + JP6271 + HQ2273 + HQ0007 + J000691 (Batch 4). Theme code for og:image protocol handling needs an audit; likely affects significantly more PDPs not yet checked. Request a Misha theme-level audit + fix rather than per-PDP correction. (Supersedes the prior "only Phantom 6 og:image open" note.)
- **NEW theme bug: `<title>` truncation (HQ2254).** Live storefront `<title>` cuts mid-parenthesis at "Pack ("; og:title + twitter:title affected. Theme template likely truncates without escape handling. Recommend Misha audit the theme template `<title>` rendering.

### Croatia jersey matrix completion mini-batch (NOTED for backlog)

Run as a focused 2-SKU pair AFTER Batch 4 closes: Women's Away (existing SKU with a live GSC signal, pos 6.0 on `women's croatia jersey`) + Youth Home (J000692-CRFT, on the sheet, not yet batched). Do NOT fold these into a larger generic batch; reserve them for coherent home/away + gender/age matrix completion. Current matrix: men's-away `croatia jersey 2026` (J000693, done); women's-home (J000691, Batch 4); youth-away (J000695, Batch 4); women's-away + youth-home pending.

### Workforce briefing artifacts discipline (NEW codification for a future session)

All 3 Batch 4 briefings are now committed: KIRA Phase 1 (`.claude/agents/keyword-research/briefings/2026-06-17_batch4-phase1.md`) and the 2 exemplar SCRIBE briefings (`2026-06-17_JP6237.md`, `2026-06-17_J000691-CRFT.md`, delinted -- verbatim quotes of live-page violations rewritten as descriptive references; the J000691 briefing also records the ORIN Fix-A evergreen decision).

CODIFY (small, future session): Phase 1 keyword-research briefings (KIRA), exemplar SCRIBE briefings, and gate-review briefings that document architectural decisions are committed alongside the batch they support. Delint quoted-violation references descriptively (per the 2026-06-17 exemplar-briefing pattern); never weaken voice_check to accommodate documentation-quotes. Apply uniformly going forward. Rationale: working-notes-vs-committed-artifacts ambiguity is exactly the architectural drift the verification-discipline convention is meant to prevent -- uncommitted connective tissue disappears, and the batch handoff already references these files.

## Carry-forward from Batch 3 close (still open)

### CODIFICATIONS pending
- Jersey playbook (fit-tier / home-away / club-vs-national taxonomy) -- partially advanced by the Batch 4 women's-cut + youth-away + home/away precedents now in `national-team-jerseys.md`.
- Mizuno silo.
- Kelme FIFA research.
- Reserved-opener blocklist.
- Full-body word-count rule made explicit.
- Worked-example refresh (model the new brief + audit-trail structure).
- voice_check.py casing detection -- RESOLVED 2026-06-29 (scope-limited backstop shipped; see 'RESOLVED 2026-06-29' under Standing follow-ups above). Correction to this note as originally written: Batch 4 H2 casing was NOT clean -- KK3725 carried 3 lowercase editorial body H2s, surfaced during Mike's 6/29 implementation, and that drift is exactly what closed the deferral.

### PRODUCTION
- Mike's 20-PDP Shopify implementation queue (now +10 from Batch 4 = pending implementation).
- White-label PDPs-tab keyword entries: Batch 2 + Batch 3 + Batch 4 primaries are surfaced in their respective `_audit-trail.md` files for Mike's manual entry (ORIN reads, white-label team writes -- permanent handoff by design).

## Token / architecture baseline (Batch 4 -- Fix 3 input)

Sub-agent tokens (harness-measured, incl. reasoning + tool I/O):
- KIRA Phase 1: 160,752 (13 MCP calls: 9 GSC + 4 DataForSEO).
- SCRIBE exemplars: JP6237 250,361; J000691 286,329.
- SCRIBE siblings: HQ2254 186,326; JP6271 178,310; IH7212 226,004; HQ2273 263,189; HQ0007 195,799; KK3725 242,342; KJ6746 281,300; J000695 208,600.
- 11 dispatches total ~2.48M sub-agent tokens; ~225k avg per SCRIBE. DataForSEO MTD cost ~$0.02-0.04 (KIRA only; SCRIBEs made 0 DataForSEO calls).
- Load distribution shifted decisively to sub-agents (vs the Batch 2-3 parent-level workaround), which is the architecturally correct posture and the real Fix 3 baseline.
