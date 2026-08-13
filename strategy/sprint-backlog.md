# Sprint Backlog

_Owned by Master Strategist. The working queue of tasks. Updated continuously._

## How to Use

Each item is a specialist-sized task (or Master Strategist task, while specialists do not exist). Items move through:

`BACKLOG → READY → IN PROGRESS → IN REVIEW → DONE`

An item is `READY` only when it has an owner, a brief, and all inputs present.

## Current Sprint

**Sprint start:** _YYYY-MM-DD_
**Sprint end:** _YYYY-MM-DD_

| ID | Title | Owner | Status | Brief | Deliverable path | Notes |
|---|---|---|---|---|---|---|
| S-001 | _task_ | Master | READY | _brief link_ | _path_ |   |

## Backlog (Not yet in a sprint)

| ID | Title | Priority | Source (goal or decision) | Notes |
|---|---|---|---|---|
| B-CAT-01 | Retarget category terms sitting on PDPs | Med | Pack-succession analysis 2026-08-04 (Mike: separate pass, not this rule) | UT3FL7NF holds `wide soccer cleats` (2900) and YF3F3V9 holds `youth soccer cleats wide` (1300). Category terms belong on collections, not PDPs. Distinct from pack succession. Meta + primary retarget; find/confirm the receiving collections first. |
| B-PACK-01 | Batch 12 six: qualify-or-grandfather decision | Med | Pack-succession narrower rule, question (c) 2026-08-04 | All six Nike Academy/Club Batch 12 SKUs (HQ2278, HQ2277, HJ4564, IO1494, IM0358, IB1600) have concurrent live senior pack siblings, so under the narrower rule they should have qualified but took unqualified terms (shadow-omission). Missed because incumbents are unregistered. Mike decides: meta-only retarget to pack-qualified (like IQ2388) vs grandfather. Pack terms are zero-volume, siblings unoptimized, so low risk either way. HOLD for Mike. |
| B-COLL-02 | Does `nike-shadow-soccer-cleats` actually target `nike shadow pack`? | Med | Step 2 Batch 13 pre-import review 2026-08-13 (Mike: not a defect, log it) | `nike shadow pack` (260/mo) sits as the secondary on five Batch 13 PDPs (HQ2275, IB4484, IO1486, IO1552, IO1554). That is correct: the hierarchy rule governs primaries, and a pack term legitimately supports a PDP as a secondary. Open question is on the collection side: confirm the `nike-shadow-soccer-cleats` collection page actually holds `nike shadow pack` as its primary, since the pack head term belongs there. Part of the footwear collection dependency already logged for Batch 13. No PDP change. |
| B-MERCH-01 | Model generation/tier collection gaps (for Jorge) | Med | Pack-succession analysis 2026-08-04, decision 2 | Merchandising gaps to flag to Jorge, do NOT invent: `nike-phantom-6`, `adidas-predator-elite`, `adidas-f50-elite`, Nike Vapor/Superfly split under `nike-mercurial`. Interim: land terms on next-broader existing collection. Jorge owns creation; SEO owns the term map once they exist. |

## Done This Quarter

_Rolling archive. Prune to last 90 days during quarterly review._

| ID | Title | Completed | Outcome |
|---|---|---|---|
| B-PACK-02 | 48-char meta title cap vs the pack-qualifier rule (fold-over tongue configs) | 2026-08-13 | RESOLVED by Mike: when the cap cannot hold both a spelled-out config name and the pack qualifier, the PACK QUALIFIER WINS and the config abbreviates, to an abbreviation the store's own live titles already use. Two binding corollaries: never truncate a pack name ("Chaos vs Control" does not become "Chaos"), never drop the brand prefix. Applied to IH4707 (`adidas Predator Elite FO AG Chaos vs Control`, 44) and JP6248 (`adidas Predator Elite FO FG Chaos vs Control`, 44) pre-import. Codified: `context/page-type-playbooks/product-page-playbook.md` 'Meta title precedence when the 48-character cap binds'. Root cause of the cap logged separately as `deliverables/technical-fixes/theme-backlog.md` T-THEME-01. |
