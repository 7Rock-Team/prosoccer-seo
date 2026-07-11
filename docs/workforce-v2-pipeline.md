# Workforce v2 Pipeline: a batch, end to end

_What a 10-PDP batch looks like under the v2 architecture (Batch 7 onward). Companion to the build spec in `docs/workforce-v2-refactor-promt.md`. Every stage below cites the convention or script that governs it._

## The goal v2 is built to hit

Cut a 10-PDP batch from roughly 4 to 6 hours wall-clock, 3 to 4M tokens, and 4-plus human checkpoints down to under 90 minutes, ~1 to 1.5M tokens, and 1 to 2 human stop-points, WITHOUT losing quality. Every defect class the human gates caught (casing, headings, FIFA terms, fabrication, cannibalization, convergence) is still caught: moved from human-in-the-loop to a deterministic script plus exception-only escalation.

## Where v1 spent its time and tokens (the targets)

- **~2.8M tokens** in the ten parallel SCRIBE dispatches, most of it DUPLICATED upstream work: every SCRIBE re-scraped its PDP, re-read the full context set, re-derived keywords ORIN had already locked, and re-validated links (~270 to 300k tokens, 40-plus tool uses each).
- **Wall-clock lost to wave serialization**: Wave 2 (siblings) could not start until Wave 1 (exemplars) finished AND ORIN manually gated the exemplar, even though most SKUs were established silos that needed no exemplar.
- **Human round-trips** at Checkpoint 1 (keywords), Checkpoint 2 (exemplar plan), Checkpoint 2b (exemplar review), Checkpoint 3 (final review), plus every surface-decision hold.

## The v2 flow, stage by stage

### Stage 0. Mike submits the batch
Mike hands ORIN up to a 10-URL batch, eligibility pre-vetted in Shopify admin (unchanged from v1). Any strategic-exception flags (sold-out, closing-window) are noted at submission.

### Stage 1. ORIN pre-dispatch (once per batch, at the parent level)
This is where the token cut lives: ORIN does the upstream gathering ONCE and writes it into per-SKU input files, instead of ten SCRIBEs each doing it.

1. **Create `deliverables/page-optimizations/[session]/inputs/`.**
2. **Batched pre-scrape (Change 3a):** Firecrawl-scrape all 10 URLs once. Write each SKU's scrape data (specs, colorway, materials, plate, weight, price, existing copy, sibling colorways) into `inputs/[SKU]_input.md`. Scrape-wins holds: a value the scrape did not supply is marked "not in scrape," never invented.
3. **KIRA keywords (Change 3b):** KIRA's Phase 1 volume-weighted + GSC composite primary, secondaries, and pack-secondary per SKU land in the input file's Keywords table. Validated once; SCRIBE does not re-derive.
4. **Link validation (Change 3b):** ORIN validates the 1 to 2 internal links per SKU (200 + content-signal) and writes them into the input file. SCRIBE does not re-validate.
5. **Differentiation spec + three-tier forbidden phrasings (Change 5):** ORIN builds each SKU's lane (angle, hook, metaphor, use-case, heritage) and extracts the exemplar's barred phrasings at three tiers: verbatim, motifs (`gone`, `invisible`), title-frames (`sees coming`). All of it goes into the input file, and the machine-readable subset into the fenced `gate-meta` JSON block (the one source of truth `batch_gate.py` reads).
6. **Tier band per SKU (Change 5):** each input file carries the SKU's OWN tier band (Elite 400-450, Pro 340-390, League/Club 280-340), never the exemplar's.
7. **Wave decision (Change 2):** per SKU, "does this silo have >= 1 shipped entry with an established lane in Registry 2? Yes -> parallel now. No -> exemplar-first for that lane only."

Schema: `templates/per-sku-input-template.md`. Convention: `context/workforce-conventions.md` 'Per-SKU input file + batched pre-scrape (v2)'.

### Stage 2. Dispatch (parallel by default)
- **Established-lane SKUs** (the common case): all dispatched in ONE parallel wave. Each SCRIBE reads its input file, reads its silo lane + the differentiation spec + the matching playbook, writes the brief, runs `voice_check.py` to green, writes the brief file. Target **<= 10 tool uses** (no live scrape, no keyword lookup, no per-link validation). SCRIBE spec: Section 2 'v2 input-driven flow'.
- **Zero-precedent lane** (narrow exception): one exemplar runs first and is gated; its skeleton + three-tier forbidden list feed only that new lane's siblings. Every established-silo SKU parallelizes immediately alongside it, no waiting.

### Stage 3. Deterministic gate (Change 4)
ORIN runs `python scripts/batch_gate.py deliverables/page-optimizations/[session]` over the whole session in one pass. It checks, per SKU and across the batch:

| # | Check | Severity |
|---|---|---|
| 1 | Body H2 casing (reused from voice_check) | FAIL |
| 2 | Heading levels (## sections, ### FAQ; flag #### / #####) | FAIL |
| 3 | Em-dash / en-dash (reused) | FAIL |
| 4 | Capitalized Adidas + forbidden words (reused) | FAIL |
| 5 | FIFA / World Cup on non-adidas pages (brand from input file) | FAIL |
| 6 | Per-SKU forbidden phrasings: verbatim + motifs + title-frames | FAIL |
| 7 | Cross-brief motifs, title-frames, opening/closing overlap | REVIEW |
| 8 | Word-count band per SKU tier | FAIL |
| 9 | Cannibalization vs Registry 1 + intra-batch | FAIL |
| 10 | Price-in-body | FAIL |
| 11 | Fabrication-hedge markers near specs | REVIEW |

Output: PASS, or FAILURES + REVIEW findings with SKU, line number, and check. Exit 0 clean, 1 review-only, 2 hard FAILs. ORIN reads only the findings, not all ten briefs. Proven against every historical defect class in `scripts/test_batch_gate.py` (KK3725 casing, KI0586 headings, DR Congo FIFA, Shadow motif/frame, IF8512 word-band + hedge) plus negatives (adidas FIFA-permitted, clean batch).

### Stage 4. ORIN acts on findings (autonomous, Change 1)
ORIN fixes the FAIL classes it can resolve from codified rules (casing, headings, word-band trims, keyword-table dupes, motif / frame re-voices, price-in-body removals), surgically or by a targeted SCRIBE re-dispatch, and re-runs the gate to green. It reviews the REVIEW findings (cross-brief convergence, fabrication hedges) and either resolves them or, if genuinely unresolvable, escalates (Stage 6). It does NOT ask Mike for the mechanical fixes; it decides, applies, and logs.

### Stage 5. Commit + registries
Single batch commit + push. Registry 2 (silo files) appended with each SKU's shipped prose patterns. Registry 1 (white-label sheet) handoff surfaced for Mike's team's manual entry (write ownership stays with them by design).

### Stage 6. The one end-of-batch report to Mike (Change 1)
Mike reviews ONE report, not four checkpoints. It carries:
1. Autonomous decisions with one-line rationale (keyword table, exemplar / dispatch choices, differentiation lanes).
2. Gate-caught defects auto-fixed.
3. Any exceptions escalated (should be rare).
4. The Registry 1 handoff block.
5. Commit hashes.
6. Publish-priority notes (sold-out SKUs ship evergreen copy, flagged for implementation ordering; live-page findings).

## The only mid-batch stop-points (the four exception criteria)

ORIN stops for Mike DURING a batch only when a decision cannot be resolved from codified rules and is one of:

1. A true architectural first with NO silo precedent (new brand licensing status, new product-class needing a new silo, new competition-IP question).
2. A fabrication trap unresolvable from the Phase 0 scrape (scrape self-contradicts, or a required spec is absent AND load-bearing).
3. A cannibalization collision with no clean resolution under codified discipline.
4. A cross-brief convergence `batch_gate.py` check #7 flags that ORIN cannot auto-resolve by a surgical re-voice.

Anything else is decided-and-logged, not asked. Full test: `context/workforce-conventions.md` 'Escalate-on-exception approval mode (v2)'.

## What still requires a human touchpoint

- The ONE end-of-batch report (Mike reviews before he implements in Shopify; nothing auto-publishes).
- The four exception criteria above (rare).
- Out-of-batch high-stakes actions: client comms to Tony, strategy-file rewrites, theme-repo drafts, bulk API spend beyond research reads (`CLAUDE.md` 'Approval mode').
- Registry 1 (white-label sheet) entry stays a manual handoff to Mike's team by design (ownership, not tooling).

## Why cutting the human gates is safe

The deterministic gate (Change 4) is the safety net, and it was built and proven BEFORE any human gate was cut (build sequence 6 -> 4 -> 3 -> 5 -> 2 -> 1). `scripts/test_batch_gate.py` encodes every historical defect class as a regression test built from the real Batch 4 to 6 defects; if a class ever stops being caught, the suite fails. A defect class that cannot be caught deterministically keeps a human touchpoint rather than being dropped (the REVIEW-severity findings and the four escalation criteria are exactly that: the judgment calls the script does not force).

## v1 vs v2 at a glance

| | v1 | v2 |
|---|---|---|
| Upstream gathering | each SCRIBE re-scrapes / re-keywords / re-validates | ORIN once, into per-SKU input files |
| SCRIBE tool uses per brief | 40-plus | <= 10 |
| Dispatch | Wave 1 -> manual gate -> Wave 2 (sequential) | single parallel wave (exemplar-first only for zero-precedent lanes) |
| Compliance gate | ORIN reads every brief, reasons every dimension, twice | `batch_gate.py` one pass; ORIN reads failures only |
| Human stop-points | Checkpoints 1, 2, 2b, 3 + surface holds | one end-of-batch report + rare exceptions |
| Forbidden phrasings | verbatim only (Shadow "gone" slipped through) | verbatim + motifs + title-frames, one source of truth |
| Target | ~4 to 6 h, ~3 to 4M tokens | under 90 min, ~1 to 1.5M tokens |

## Build status and first live run

All six changes and the consistency sweep are committed (Changes 6, 4, 3, 5, 2, 1, then step 8). No live batch was run during the build; the gate was proven against existing shipped briefs as fixtures. **The first live v2 batch is Batch 7, after Mike reviews this doc.**
