# Consolidated Page Optimization Brief Template

_ORIN uses this template for every per-page optimization brief. File the populated brief at `deliverables/page-optimizations/YYYY-MM-DD_<page-slug>.md`. Per ORIN agent.md Section 13._

## How to use this template

1. Copy this file to `deliverables/page-optimizations/YYYY-MM-DD_<page-slug>.md` (replace YYYY-MM-DD with today's date and `<page-slug>` with the URL slug, e.g., `2026-05-08_mexico.md` for `/collections/mexico`).
2. Replace every `<placeholder>` and `[bracketed instruction]` with actual content lifted from specialist contributions or pulled from data sources.
3. Skip sections that don't apply (mark them "skipped: <reason>" rather than deleting; auditability matters).
4. Run `scripts/voice_check.py` on the populated brief before holding for Mike approval.
5. Run the self-verification checklist (ORIN Section 11) before commit.
6. Append the matching row to `deliverables/tracking/collections-master.csv` or `products-master.csv` when Mike approves.

## Template starts below this line

---

# Consolidated Page Optimization Brief: <page slug>

**Date:** YYYY-MM-DD
**Author:** ORIN (merging KIRA + RECON + SCRIBE + VERITAS contributions)
**Audience:** Mike (Gate); routing to [Misal / Misha / Jorge] post-approval
**Workflow severity:** [Sprint-blocking / High / Medium / Low]
**Confidence (overall):** [High / Medium / Low]
**Status:** [draft for Mike review / approved / implementing / shipped / validated / monitoring / complete / regressed]

## Page identifier

- **URL:** <full path>
- **Page type:** [collection / product / blog / homepage]
- **Sprint phase:** [Wave 1 / Wave 2 / Wave 3 / post-sprint / standalone]
- **Matrix tier:** [Tier 1 / Tier 2 / Tier 3 / Hypothesis]
- **Avatar fit (primary):** [Carlos / Jennifer / Tyler / Mike the Coach]
- **Avatar fit (secondary if relevant):** [...]

## Performance baseline (matches master CSV row)

| Metric | Value | Source |
|---|---|---|
| Baseline impressions (12mo) | N | [GSC MCP get_search_analytics YYYY-MM-DD] |
| Baseline clicks (12mo) | N | [same source] |
| Baseline avg position | N.N | [same source] |
| Baseline CTR | N.NN% | [same source] |

## KIRA findings: keyword scope and strategic priority

[Lifted from KIRA's per-page contribution wrapper. Keyword scope, intent classification, target tier rationale, avatar fit, SERP feature flags, expected lift hypothesis. Sources cited inline.]

**KIRA confidence:** [High / Medium / Low]
**KIRA open flags for ORIN:** [items needing cross-agent attention or Mike escalation, OR "none"]

## RECON findings: competitor snapshot

[Lifted from RECON's per-page contribution wrapper. 3-to-5 competitor on-page audit, pattern annotation, threat-level note. Skipped entirely if RECON wasn't in this brief's sequence; note "RECON skipped: [reason]" if so.]

**RECON confidence:** [High / Medium / Low]
**RECON threat level (if applicable):** [High / Medium / Low / Watch]
**RECON open flags for ORIN:** [items, OR "none"]

## SCRIBE findings: per-element on-page proposals

[Lifted from SCRIBE's per-page contribution wrapper. Per-element (title / meta / H1 / intro / body) current state, proposed state, reasoning, expected lift band, validation plan. Voice check status per proposed string.]

**SCRIBE confidence:** [High / Medium / Low]
**SCRIBE severity:** [Critical / High / Medium / Low]
**SCRIBE voice check (per-string):** [list each proposed string and exit status]
**SCRIBE open flags for ORIN:** [items, OR "none"]

## VERITAS findings: technical foundation

[Lifted from VERITAS's per-page contribution wrapper. Schema state, canonical, redirects, render integrity, indexation. Severity and confidence per finding. Skipped if not in sequence; note "VERITAS skipped: [reason]" if so.]

**VERITAS confidence:** [High / Medium / Low]
**VERITAS severity:** [Critical / High / Medium / Low]
**VERITAS open flags for ORIN:** [items, OR "none"]

## Implementation checklist

| Change | Implementer | File / Surface | Severity | Status |
|---|---|---|---|---|
| [Title rewrite] | [Jorge / Misal / Misha] | [Shopify admin / collection.liquid line N] | [Critical / High / Medium / Low] | [pending Mike approval / approved / shipped / validated] |
| [Meta description rewrite] | [Jorge] | [Shopify admin] | [...] | [...] |
| [H1 update] | [...] | [...] | [...] | [...] |
| [Schema injection] | [Misha] | [theme.liquid snippets/X] | [...] | [...] |
| [URL canonical] | [Misal / Misha] | [...] | [...] | [...] |

## ORIN summary

[One paragraph. What ships, why, expected outcome, sequencing rationale across the four specialist contributions. ORIN's added value: where the specialists' findings reinforce each other; where they conflict and how ORIN resolved; where Mike should focus attention during review.]

## Plain-language summary for Tony (when client-adjacent)

[One paragraph. No jargon. Lead with the outcome. Drop entirely if the brief never reaches client-side communication.]

## Voice check status

- Brief voice_check.py exit: [0 (clean) / specific failures]
- Per-string voice_check.py runs (proposed copy): [list each, exit status]

## Sources cited (aggregated)

[All sources from KIRA, RECON, SCRIBE, VERITAS contributions, deduplicated. Plus ORIN-specific sources: GSC MCP baseline pull, master CSV existing-row reference if relevant.]

## Red-team appendix

[Skeptical review across the merged brief. Which claims would Mike challenge? Where do specialist contributions disagree, and how is the disagreement resolved or acknowledged? What's the weakest link?]

## Master CSV row reference

- File: `deliverables/tracking/collections-master.csv` (or `products-master.csv`)
- Row appended: YYYY-MM-DD HH:MM
- Status: <status value>
