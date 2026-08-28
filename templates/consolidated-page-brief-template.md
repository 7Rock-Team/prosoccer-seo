# Page Optimization Brief Template

_Minimal brief for Mike. Target: fits on one Google Doc page. Visible content is the Keyword research block (primary plus supporting only) and the Recommended new SEO setup block, nothing more. Mike references Shopify admin directly for current state during implementation; current state is no longer captured in the brief or in the workforce-internal briefing. Workforce-internal briefing at `.claude/agents/on-page-seo/briefings/YYYY-MM-DD_<slug>.md` preserves the rest of the audit trail (data provenance, alternatives considered with rejection reasoning, full keyword research including intent percentages and trend data, brand-affiliation classification, avatar scope, topic research findings, compliance scan, per-string voice check, 11-gate self-verify, sources, severity, confidence, schema dependency flags, validation plans, cost tracking). Mike can request the briefing at any time. Landmark cases warranting the full deep brief use the archived template at `templates/consolidated-page-brief-template-archive.md`._

## How to use this template

1. Copy this file to `deliverables/page-optimizations/YYYY-MM-DD_session-NN/<slug>_brief.md` per the session folder convention in `context/workforce-conventions.md`.
2. Identify page type and load the matching playbook from `context/page-type-playbooks/` per `.claude/agents/on-page-seo/agent.md` Section 2 step 4b. Subject matter from the playbook governs WHAT each field is about; the six copy-writing principles in `context/03-brand-voice.md` govern HOW it reads.
3. **Keyword research via DataForSEO (mandatory, data-backed).** Pull volume and keyword difficulty for the primary keyword candidate plus 2 to 3 alternatives. The visible brief surfaces only the chosen primary keyword (volume + KD) and the supporting long-tail set as a comma-separated list with optional volume per term. Alternatives considered, rejection reasoning, intent percentages, trend data, and the full candidate set live in the workforce-internal briefing.
4. **Current ranking lookup via DataForSEO SERP API (mandatory).** For the chosen primary keyword, run `mcp__dfs-mcp__serp_organic_live_advanced` and identify whether the target URL appears in the top 100 organic results. If yes, capture position. If no, mark "not in top 100." Surface as a one-line `Current ranking:` entry in the visible Keyword research block. Apply the ranking-aware posture below before drafting recommendations.
5. **Ranking-aware posture (v2, 2026-08-27). Canonical text: `context/workforce-conventions.md` 'Ranking-aware posture (v2)'.** Bands key on the **earned-term position** supplied by ORIN in `gate-meta` (`earned_term`, `earned_term_position`), never the page-average position. `scripts/batch_gate.py` `check_ranking_input` FAILS the batch when the input is absent.
   - **Under 5:** WARNING required. The visible brief includes the line "Page currently ranks top 5. Title/H1 changes carry equity risk. Confirm with Mike before shipping changes to these fields." Preserve exact-match phrasing of the earned term in Title and H1; copy changes lean toward Meta Description, Short Description and Long Description.
   - **5 to 10:** Title and H1 may be improved but MUST retain the earned term in exact-match form. No Mike gate. State the earned term and its position in the brief.
   - **10 to 20:** Standard recommendations. Carry the earned term into the Title where it fits naturally.
   - **Over 20, or not ranking:** Standard recommendations. Fresh attempt.
6. Topic research via Tavily / WebSearch scaled to familiarity: 2 to 5 queries for well-known topics (Mexico, Argentina, major brands), 5 to 10 for unfamiliar. Do not over-research what prior sessions already documented. Findings live in the workforce-internal briefing, not the visible brief.
7. For PDPs, Mike supplies the existing Short Description and Long Description directly as input to the optimization. SCRIBE does not scrape PDP body content. For collection pages, SCRIBE pulls current copy via the firecrawl skill / Firecrawl MCP for context but does not surface it in the visible brief; reference Shopify admin during implementation.
8. Fill the brief below. Default visible content is the Keyword research block (including Current ranking line) and the Recommended new SEO setup block. No Current state section. No Source of record section. No Alternatives considered section. No External links field on PDPs. No LLM ranking field (LLM visibility tooling is immature; revisit in 6 months).
9. Validate every proposed internal link via the firecrawl skill / WebFetch (status code 200, page-type signals confirmed, no soft-404) per the matching playbook's link strategy (1 to 2 max). For PDPs, external links are forbidden per `context/page-type-playbooks/product-page-playbook.md` 'Internal links only on product pages'; the External links field does not appear on PDP briefs at all.
10. Run voice check (`scripts/voice_check.py`) and the 11 gates from `.claude/agents/on-page-seo/agent.md` Section 11 silently. Do NOT document results in the visible brief. Capture all results in the workforce-internal briefing. Surface a failure to Mike at GATE only if it cannot be resolved silently.
11. Hold at GATE for Mike review.
12. Append the matching row to `deliverables/tracking/collections-master.csv` or `products-master.csv` once Mike approves.

## Optional mode: Whitelabel audit

When Mike explicitly requests a whitelabel audit (not the default), insert a `## Comparison with current state` section before the Recommended new SEO setup block showing field-by-field deltas with reasoning. The audit mode is the only context where the brief carries current-state strings inline; otherwise current state is reference-only via Shopify admin. Without an explicit audit request, the comparison section does NOT appear.

## Template starts below this line

---

# Page Optimization: <page name>

- **URL:** <full path>
- **Date:** YYYY-MM-DD
- **Page type:** <collection / product / service / homepage>

## Keyword research

- **Primary keyword:** `<head keyword>` ([volume]/mo, KD [X])
- **Supporting keywords:** `<variant 1>` ([volume]/mo), `<variant 2>` ([volume]/mo), `<variant 3>` ([volume]/mo)
- **Current ranking:** position #[X] for `<head keyword>` (DataForSEO SERP, [YYYY-MM-DD]) OR not in top 100
- **WARNING (top 5 only):** Page currently ranks top 5. Title/H1 changes carry equity risk. Confirm with Mike before shipping changes to these fields.

## Recommended new SEO setup

- **Title:** <new>
- **Slug:** <new OR "no change">
- **Meta Title:** <new> ([NN chars])
- **Meta Description:** <new> ([NN chars])
- **Short Description:** <new paste-ready copy>
- **Long Description:** <new paste-ready copy with H2 sections, FAQ where applicable, internal links embedded inline at natural anchor points>
- **Internal links:** <1 to 2 validated destinations with anchor text>
