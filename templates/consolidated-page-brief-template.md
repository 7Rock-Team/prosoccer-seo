# Page Optimization Brief Template

_Streamlined brief for Mike. Default mode is Fresh Optimization: visible content is the Current state block and the Recommended new SEO setup block, nothing more. Workforce-internal logs preserve full depth (brand-affiliation classification, avatar scope, topic research findings, compliance scan, per-string voice check, 11-gate self-verify, sources, severity, confidence, schema dependency flags, validation plans). Mike can request the briefing at `.claude/agents/on-page-seo/briefings/YYYY-MM-DD_<slug>.md` at any time. Whitelabel audit mode (with comparison narrative) is opt-in per `context/workforce-conventions.md` 'Optional mode: Whitelabel audit'. Landmark cases warranting the full deep brief use the archived template at `templates/consolidated-page-brief-template-archive.md`._

## How to use this template

1. Copy this file to `deliverables/page-optimizations/YYYY-MM-DD_session-NN/<slug>_brief.md` per the session folder convention in `context/workforce-conventions.md`.
2. Identify page type and load the matching playbook from `context/page-type-playbooks/` per `.claude/agents/on-page-seo/agent.md` Section 2 step 4b. Subject matter from the playbook governs WHAT each field is about; the six copy-writing principles in `context/03-brand-voice.md` govern HOW it reads.
3. Capture current state per page type, per `context/workforce-conventions.md` 'Fresh Optimization workflow':
   - **Collection pages:** Firecrawl scrape covers Title, Slug, Meta Title, Meta Description, and the description body.
   - **Product pages:** Firecrawl scrape covers Title, Slug, Meta Title, Meta Description only. Mike supplies the existing Short Description and Long Description directly. Do NOT scrape PDP body content; wait for Mike to provide it.
4. Topic research via Tavily scaled to familiarity: 2 to 5 queries for well-known topics (Mexico, Argentina, major brands), 5 to 10 for unfamiliar. Do not over-research what prior sessions already documented.
5. Fill the brief below. Default visible content is the Current state block and the Recommended new SEO setup block.
6. Validate every proposed internal link via Firecrawl (status code 200, page-type signals confirmed, no soft-404) per the matching playbook's link strategy (1 to 2 max).
7. Run voice check (`scripts/voice_check.py`) and the 11 gates from `.claude/agents/on-page-seo/agent.md` Section 11 silently. Do NOT document results in the visible brief. Capture all results in the workforce-internal briefing at `.claude/agents/on-page-seo/briefings/YYYY-MM-DD_<slug>.md`. Surface a failure to Mike at GATE only if it cannot be resolved silently.
8. Hold at GATE for Mike review.
9. Append the matching row to `deliverables/tracking/collections-master.csv` or `products-master.csv` once Mike approves.

## Optional mode: Whitelabel audit

When Mike explicitly requests a whitelabel audit (not the default), insert a `## Comparison with current state` section between the Current state block and the Recommended new SEO setup block, showing field-by-field deltas with reasoning. Without an explicit request, this section does NOT appear in the brief.

## Template starts below this line

---

# Page Optimization: <page name>

- **URL:** <full path>
- **Date:** YYYY-MM-DD
- **Page type:** <collection / product / service / homepage>
- **Primary keyword:** <head keyword>
- **Supporting keywords:** <long-tail variant 1, variant 2, variant 3>

## Current state

- **Title:** <current>
- **Slug:** <current>
- **Meta Title:** <current> [NN chars]
- **Meta Description:** <current> [NN chars]
- **Short Description:** <current full text; supplied by Mike for PDPs, scraped via Firecrawl for collection pages>
- **Long Description:** <current full text; supplied by Mike for PDPs, scraped via Firecrawl for collection pages>
- **Internal links:** <count and brief note on what they link to>

## Recommended new SEO setup

- **Title:** <new>
- **Slug:** <new OR "no change" with reasoning>
- **Meta Title:** <new> [NN chars]
- **Meta Description:** <new> [NN chars]
- **Short Description:** <new full paste-ready copy>
- **Long Description:** <new full paste-ready copy with H2 sections, FAQ where applicable, internal links embedded inline at natural anchor points>
- **Internal links:** <1-2 validated URLs with anchor text>
- **External links:** <target URL and anchor text where applicable; omit field if not applicable>
