# Workforce Conventions

This file documents cross-agent operational conventions for the ProSoccer SEO workforce. Conventions here apply to all agents (ORIN, KIRA, VERITAS, SCRIBE, SAGE if built, RECON, METRIK) and are read at startup alongside `context/00-business-overview.md`, `context/03-brand-voice.md`, `context/04-customer-avatars.md`, and `context/brand-ip-constraints.md`.

When a convention in this file conflicts with an agent-specific rule in `.claude/agents/<agent-name>/agent.md`, the convention here is the default; the agent-specific rule overrides only when it is explicit about doing so.

## Page optimization deliverable folder structure

All page-optimization deliverables produced during a session (whitelabel audits, per-page briefs, regenerated briefs, comparison docs) land in a date-stamped session folder under `deliverables/page-optimizations/`. The structure is:

```
deliverables/page-optimizations/
  whitelabel-audit/
    YYYY-MM-DD_session-NN/
      <slug>_audit-and-regen.md
      <slug-2>_audit-and-regen.md
      ...
  YYYY-MM-DD_session-NN/
    <slug>_brief.md
    ...
```

### Naming convention

- **Folder name pattern:** `YYYY-MM-DD_session-NN/` where YYYY-MM-DD is the session start date and NN is a zero-padded two-digit session ordinal within the work-unit (e.g., `01`, `02`, `03`).
- **Work-unit boundary:** a "session" is a single ORIN-orchestrated work unit (Mike's prompt to the agent, the agent's execution, and the GATE review or completion). Multi-session work units (e.g., a 3-collection whitelabel audit pilot) get a session folder per session.
- **Examples:**
  - `deliverables/page-optimizations/whitelabel-audit/2026-05-16_session-01/` (whitelabel audit pilot, session 1)
  - `deliverables/page-optimizations/whitelabel-audit/2026-05-17_session-02/` (whitelabel audit pilot, session 2)
  - `deliverables/page-optimizations/2026-06-01_session-01/` (a non-whitelabel batch of per-page briefs)

### Session folder creation

The session folder is created at session start if it does not already exist. ORIN creates the folder via the orchestrator's first file write of the session. Specialist agents (SCRIBE, KIRA, etc.) write into the session folder ORIN has established.

### Workforce-internal briefings

Per-page workforce-internal briefings (SCRIBE classification reasoning, KIRA keyword research notes, etc.) continue to live in agent-specific briefings folders: `.claude/agents/<agent-name>/briefings/YYYY-MM-DD_<slug>.md`. These are agent-internal and not part of the page-optimization deliverable folder.

### Historical / pre-convention files

Existing flat-directory deliverables (e.g., `deliverables/page-optimizations/2026-05-08_mexico-v3.md`) stay where they are. Do NOT retroactively move historical files into session folders. The convention applies going forward; the audit trail of the convention transition is the git history.

## Fresh Optimization workflow (default mode, minimal format as of 2026-05-26 round 2)

Fresh Optimization is the default workflow for page-optimization deliverables produced by SCRIBE under ORIN orchestration. The whitelabel audit mode is opt-in and used only when Mike explicitly requests it. **Target: the visible brief fits on one Google Doc page.**

### Workflow steps

1. Load context: page-type playbook matching the page (`context/page-type-playbooks/`), `context/brand-ip-constraints.md`, the six copy-writing principles in `context/03-brand-voice.md`.
2. Read current state for SCRIBE's own context, but do NOT capture it in the brief:
   - **Collection pages:** SCRIBE pulls current copy via the firecrawl skill (or Firecrawl MCP when installed, per 'Tool inventory' below) for context. Current state does NOT appear in the visible brief.
   - **Product pages:** Mike supplies the existing Short Description and Long Description directly as input to the optimization. SCRIBE does NOT scrape PDP body content. Current state does NOT appear in the visible brief.
   - **Mike references Shopify admin directly for current state during implementation.** The brief is forward-looking only.
3. Keyword research via DataForSEO MCP (mandatory, data-backed). The workforce-internal briefing carries the full keyword research workup; the visible brief surfaces only the chosen primary keyword (volume + KD) and the supporting long-tail set as a comma-separated list with optional volume.
4. **Current ranking lookup via DataForSEO SERP API (mandatory).** Run `mcp__dfs-mcp__serp_organic_live_advanced` for the chosen primary keyword; identify whether the target URL appears in the top 100 organic results; capture position OR "not in top 100." Surface as a one-line `Current ranking:` entry in the visible Keyword research block. Apply the ranking-aware posture (see 'Ranking-aware posture' subsection below) before drafting recommendations. GSC MCP is the long-term ranking source of record; install pending per 'Tool inventory' below, DataForSEO SERP API is the current fallback.
5. Topic research via Tavily / WebSearch scaled to familiarity:
   - Well-known topics (Mexico, Argentina, major brands): 2 to 5 queries.
   - Unfamiliar topics: 5 to 10 queries.
   - Do not over-research what prior sessions already documented. Findings live in the workforce-internal briefing, not the visible brief.
6. Generate the optimized brief in the format at `templates/consolidated-page-brief-template.md`. Default visible content is the minimal Keyword research block (including Current ranking line and top-5 WARNING line where applicable) and the Recommended new SEO setup block, nothing more. No Current state section. No Source of record paragraph. No Alternatives considered section. No External links field on PDPs. No LLM ranking field (deferred).
7. Validate every proposed internal link via the firecrawl skill (status code 200, page-type signals confirmed, no soft-404) per the matching playbook's link strategy (1 to 2 max).
8. Run voice check (`scripts/voice_check.py`) and the 11 gates from `.claude/agents/on-page-seo/agent.md` Section 11 silently. Pass results are NOT surfaced in the visible brief; only an unresolvable failure surfaces to Mike. All gate results are documented in the workforce-internal briefing at `.claude/agents/on-page-seo/briefings/YYYY-MM-DD_<slug>.md`.
9. Hold at GATE for Mike review.
10. Append the matching row to `deliverables/tracking/collections-master.csv` or `products-master.csv` once Mike approves.

### Ranking-aware posture

The Current ranking position governs how aggressively SCRIBE iterates on Title and H1 copy.

- **Top 5:** WARNING required in the visible brief. The line reads: "Page currently ranks top 5. Title/H1 changes carry equity risk. Confirm with Mike before shipping changes to these fields." Recommendations preserve exact-match phrasing of the primary keyword in Title and H1; copy iteration leans toward Meta Description, Short Description, and Long Description where equity risk is lower.
- **Top 6 to 20:** Standard recommendations. Current position noted for context. No warning line.
- **Top 21 to 100:** Standard recommendations. Current position noted for context.
- **Not ranking (not in top 100):** Standard recommendations. Treated as opportunity for a fresh ranking attempt.

**LLM ranking is deferred.** LLM visibility tooling (ChatGPT citation rates, Claude / Gemini surfaces, AI Overview presence) is immature today. Revisit in 6 months when the category matures and the tooling becomes practical. Do not include an LLM ranking field in the brief.

### Workforce-internal briefing (preserved scope, current state removed)

The workforce-internal briefing at `.claude/agents/on-page-seo/briefings/YYYY-MM-DD_<slug>.md` continues to capture: brand-affiliation classification, avatar scope, topic research findings, compliance scan results, per-string voice check status, 11-gate self-verify status, cost tracking, data provenance / source-of-record (DataForSEO calls, locations, timestamps, status codes), alternatives considered with rejection reasoning, intent percentages, trend data, per-element expected lift bands, validation plans, severity, confidence, schema dependency flags, cross-agent voice flags, and any other workforce-internal context. Mike can request the briefing on demand at any time. It is not surfaced at gate review by default.

**Current state is not captured in the workforce-internal briefing.** Mike sees current state directly in Shopify admin during implementation; Shopify's own field history preserves the audit trail. Duplicating current state in the briefing adds no audit value.

### Optional mode: Whitelabel audit

The whitelabel audit mode adds a `## Comparison with current state` section to the brief before the Recommended new SEO setup block, showing field-by-field deltas with reasoning. The audit mode is the only context where the brief carries current-state strings inline. This mode is opt-in. Mike must explicitly request "whitelabel audit" (or equivalent phrasing) for the comparison section to appear in the brief. Without an explicit request, Fresh Optimization with no comparison narrative is the default.

### Simplifications baked into Fresh Optimization (round 2, 2026-05-26)

1. Brief target is one Google Doc page; the format is minimal by construction.
2. Current state section removed from visible brief and from workforce-internal briefing.
3. Source of record paragraph removed from visible brief; data provenance lives in workforce-internal briefing only.
4. Alternatives considered with rejection reasoning removed from visible brief; lives in workforce-internal briefing.
5. Keyword research block strips intent percentages and trend data from visible brief; lives in workforce-internal briefing.
6. External links field omitted on PDPs entirely (PDP link policy is internal-only, locked).
7. Topic research scales to familiarity rather than running a fixed query count per page.
8. Voice check and the 11 gates run silently; pass results do not surface; only unresolvable failures get flagged to Mike.
9. No comparison table or audit narrative in the visible brief unless whitelabel audit mode is requested.
10. For batched sessions, context loads once per session, not per page.

## Five canonical brief-craft rules (cross-reference)

Five rules govern every brief SCRIBE produces under the Fresh Optimization workflow. The rules are canonical in both page-type playbooks: `context/page-type-playbooks/product-page-playbook.md` 'Five canonical brief-craft rules' and `context/page-type-playbooks/collection-page-playbook.md` 'Five canonical brief-craft rules'. The five rules sit alongside the prior canonical policies (PDP external link policy, internal-links 1 to 2 target) which remain in force in their existing playbook sections. Quick index:

1. **Supporting keywords distributed as semantic variants in body** (1 to 2 natural appearances per variant from the brief's Keyword research block, no stuffing).
2. **Primary keyword in at least one H2 header** (natural integration; restructure the H2 rather than force the keyword).
3. **Meta description structure** (commercial intent + trust signal + emotional CTA; tier-aware language for branded products: never combine tier words like "Authentic Stadium").
4. **Named entities in body copy serve LLM search discoverability** (5 to 10 specific named entities per page where natural: players, federations, tournaments, signature product lines, signature features, locations, managers).
5. **Short Description structure** (primary keyword in sentence 1 or 2; avatar identity hook in first half; 2 to 3 differentiating specifics; CTA close distinct from Meta Description; 200 to 300 chars target).

Worked example for all five rules: UAE 2026 PDP v3 brief at `deliverables/page-optimizations/2026-05-26_session-01/uae-2026-home-stadium_brief-v3.md`.

**Category-specific H2 templates (DRAFT v1)** for 15 product categories ProSoccer sells live in `context/page-type-playbooks/product-page-playbook.md` 'Category-specific H2 templates'. National-team-jersey template is validated as of UAE v3; remaining 14 categories are DRAFT v1 patterns to be validated through real PDP optimization work.

## Brief content requirements (data-backed)

Both PDP and collection-page briefs must surface a minimal data-backed keyword research block and respect the product-page link policy. These are hard requirements, not optional.

### Keyword research surfacing (minimal visible format)

Every visible brief must include a `## Keyword research` block at the top with:

- Primary keyword on one line with monthly search volume and keyword difficulty.
- Supporting long-tail keywords as a comma-separated list with optional volume per term.
- Current ranking on one line: position number for the primary keyword from DataForSEO SERP API, OR "not in top 100." Lookup date included.
- WARNING line (top 5 only): the explicit equity-risk note per 'Ranking-aware posture' above.

Nothing else surfaces in the visible block. No alternatives considered. No rejection reasoning. No intent percentages. No trend data. No source-of-record paragraph. No LLM ranking line. These all live in the workforce-internal briefing as the defensibility audit trail (LLM ranking is deferred entirely per 'Ranking-aware posture' above).

DataForSEO is the source of record. The workforce-internal briefing must document: primary keyword choice with volume + KD + intent (with probabilities from `dataforseo_labs_search_intent` plus main_intent from `dataforseo_labs_google_keyword_overview`), 2 to 3 alternatives considered each with volume + KD + 1 to 2 sentence why-not-chosen reasoning, selection reasoning combining data and avatar fit, supporting long-tail keywords with volume data, and the source-of-record paragraph (calls executed, locations, timestamps, status codes).

Trust-me keyword choices are not acceptable for agency-grade work. The primary keyword selection must be defensible against "why this keyword and not the other one" with concrete data; the workforce-internal briefing is where that defensibility lives. The visible brief stays minimal.

The visible '## Keyword research' block format is canonical in `templates/consolidated-page-brief-template.md` and replicated in `.claude/agents/on-page-seo/agent.md` Section 13.

### Product page link policy: internal only (External links field omitted entirely on PDPs)

PDP body copy includes internal links to ProSoccer collection or product pages ONLY. External links are forbidden on PDPs. The reasoning:

- External links leak link equity off-site during the purchase consideration window.
- They give the customer an exit ramp from the purchase decision.
- Authority signals through external links belong on homepage and blog content, not on PDPs.

If body copy references external tournaments, events, or context (Asian Cup, Champions League, Premier League, etc.), keep the reference as plain text. Do not hyperlink to external sites. If the reference needs a destination, link to an internal ProSoccer page instead (e.g., a related collection).

**The External links field does not appear on PDP briefs at all.** Omitting the field by construction (vs writing "External links: none") is intentional; the visible brief should not carry empty fields. Collection pages may include external links per the collection-page playbook's link strategy; the External links field appears on collection-page briefs only when an outbound link is part of the recommendation.

The PDP internal-link-only policy is canonical in `context/page-type-playbooks/product-page-playbook.md` 'Internal links only on product pages'. Collection-page external-link policy stays under the collection-page playbook's link strategy section.

## Cleanup and retention policy

Page-optimization deliverables are operational artifacts with a finite useful life. The audit trail of who-decided-what lives in commit messages and PR descriptions; the deliverable file itself becomes stale once the recommendation has been implemented and either succeeded or been superseded.

### Retention window

- **Active retention:** 6 to 12 months from session date. The exact window depends on the deliverable type (whitelabel audits clear faster than evergreen brief work) and is decided at quarterly cleanup time, not pre-fixed per file.
- **Long-tail exception:** any deliverable that remains the source-of-truth for a live page's copy stays in the repo indefinitely. The Mexico v3 brief, for example, governs the Mexico page's copy until a v4 supersedes it; v3 stays in the repo until v4 lands.

### Quarterly cleanup pass

Once per quarter, ORIN (or Mike directly) runs a cleanup pass:

1. Enumerate all session folders under `deliverables/page-optimizations/` and `deliverables/page-optimizations/whitelabel-audit/`.
2. For each folder older than 6 months from today: review the contents to confirm the deliverables have been implemented, superseded, or are no longer load-bearing.
3. Folders meeting the retention threshold and review criteria are removed in a dedicated cleanup commit.
4. The cleanup commit message lists every removed folder and the disposition (implemented / superseded / abandoned). This preserves the audit trail even after the file is gone.

### Cleanup commit structure

The cleanup commit is its own commit, not bundled with other work. Commit message format:

```
Quarterly cleanup YYYY-Q[N]: removed N page-optimization session folders past retention window

Folders removed (with disposition):
- deliverables/page-optimizations/YYYY-MM-DD_session-NN/ — implemented YYYY-MM-DD via Shopify admin
- deliverables/page-optimizations/whitelabel-audit/YYYY-MM-DD_session-NN/ — superseded by [reference]
- ...
```

The disposition note is the audit trail of why each folder was safely removable.

### Cleanup does NOT apply to

- Agent-specific briefings under `.claude/agents/<agent-name>/briefings/`. Those are agent-internal context that future sessions read; retention is per-agent and managed in the agent's own learnings.md compaction protocol.
- The `templates/` directory.
- Any deliverable file in `deliverables/technical-fixes/`, `deliverables/keyword-research/`, `deliverables/phase-2-discovery/`, or other non-page-optimization deliverable folders. Those have their own retention conventions to be documented separately as they emerge.

## Tool inventory

This section is the canonical truth source for which MCP servers and external tools are operationally available to the workforce today. Agent narrative sections (`## 5. Tools and MCP Connections` in each `.claude/agents/<agent-name>/agent.md`) may reference MCP namespaces aspirationally; this inventory governs what's actually callable. When a narrative description and this inventory disagree, this inventory wins.

Refreshed: 2026-05-26.

### Operational (live, callable today)

- **DataForSEO MCP, `mcp__dfs-mcp__*`.** Pay-per-use API access covering SERP data, keyword research, keyword difficulty, search intent, on-page audit, backlinks, domain analytics, and DataForSEO Labs endpoints. Credentials verified 2026-05-26 (status_code 20000 returned on `mcp__dfs-mcp__serp_locations`). Workforce-wide hard cap $100/month per Section 12 of each agent.
- **Playwright MCP, `mcp__plugin_playwright_playwright__*`.** Headless browser automation for live SERP inspection, SPA-rendered content extraction, post-deployment visual validation, and screenshot capture. Read-only posture for all workforce use.
- **Google Drive MCP, `mcp__claude_ai_Google_Drive__*`.** Reads from the January 2026 audit folder (`1KF1213I-_nf9B04ASKoM_mcv5xydJ3h8`) and other shared Drive artifacts. Free at API level; cost is context-budget consumption.
- **Local file system.** All `data/`, `context/`, `deliverables/`, `strategy/`, `shared-intelligence/`, `work-log/`, and `.claude/agents/<agent>/` paths. Plus the prosoccer theme repo for read-only template inspection (SCRIBE, VERITAS).
- **`scripts/voice_check.py`.** Hard gate on every customer-facing copy proposal and every markdown deliverable.

### Install pending (referenced in agent narratives but not yet callable)

- **Firecrawl MCP, `mcp__firecrawl-mcp__*`.** Not installed as of 2026-05-26. Until install lands, fall back in this order: (1) the `firecrawl` skill family (`firecrawl-scrape` for single URLs, `firecrawl-search` for query-first discovery, `firecrawl-map` for URL inventory, `firecrawl-crawl` for bulk extraction, `firecrawl-interact` for dynamic pages) which calls Firecrawl via CLI and ships with this Claude Code build; (2) `WebFetch` for quick single-URL reads when the skill overhead is heavier than needed. Once `mcp__firecrawl-mcp__*` is installed, prefer the MCP tool calls over the skill for lower per-call context overhead.
- **GSC MCP, `mcp__gsc-server__*`.** Not installed as of 2026-05-26. **Install scheduled as a separate workstream for the 2026-05-27 session.** Until install lands, fall back paths by use case:
  - **Ranking context per page (primary keyword position lookup):** DataForSEO SERP API via `mcp__dfs-mcp__serp_organic_live_advanced`. This is the canonical ranking-context source for the Fresh Optimization workflow Step 4 (see 'Fresh Optimization workflow' above). Once GSC MCP lands, ranking context shifts to GSC `get_search_analytics` per URL for the source-of-record advantage; DataForSEO SERP remains useful for competitor-context lookups but not for ProSoccer's own ranking baseline.
  - **CTR ceiling diagnostics, query-by-page intersection, indexation state, Rich Results coverage:** CSV exports under `data/gsc-exports/` (12-month `_top-pages.csv`, `_top-queries.csv`, `_search-appearance.csv`). CSV granularity is coarser than the live API: no query-by-page intersection, no live `inspect_url_enhanced`, no Rich Results report, no live coverage-issue inspection. Workable for baseline tracking, CTR ceiling diagnostics at page level, and aggregated query monitoring. Mike refreshes the exports on cadence (target: monthly).
- **Tavily MCP, `mcp__claude_ai_Tavily__*`.** Registered but unauthenticated as of 2026-05-26. Until auth completes, fall back to `WebSearch` for general topic research, competitor news monitoring, and SERP-feature spot-checks. WebSearch returns snippets only; Tavily would return full-page content. Note the granularity loss in session briefings and surface to ORIN if a brief depends on full-page Tavily extraction.

### Implicit-fallback drift (the failure mode this inventory prevents)

Before this inventory existed, agent narratives referenced `mcp__firecrawl-mcp__firecrawl_scrape`, `mcp__gsc-server__get_search_analytics`, and `mcp__claude_ai_Tavily__tavily_search` as if those tools were live. Sessions that depended on those calls silently degraded to whichever tool happened to work, or stalled, or produced briefs that cited tools the workforce couldn't actually run. This implicit fallback hid the install gap from Mike and produced misleading "tool used" lines in session briefings.

The pre-flight tool verification protocol in SCRIBE Section 2 Step 0 (canonical pattern, other agents adopt as added) makes the tool inventory explicit at the start of every session. If an agent intends to use a tool listed under "Install pending" above, the session briefing must log the actual fallback used, not just the intended MCP namespace.

### Update protocol

When an MCP install completes or auth lands:

1. Move the entry from "Install pending" to "Operational" with the verification date and the verification call used.
2. Update affected agent narrative sections to remove the install-pending caveats (the inventory references can stay implicit once the MCP is live).
3. Commit message format: `MCP install: <namespace> live. Tool inventory in workforce-conventions.md updated; agent narratives reference the MCP directly without fallback caveats.`

## Cross-references

- `context/brand-ip-constraints.md` documents the FIFA terminology constraint that applies to all page-optimization deliverables produced under this folder structure.
- `.claude/agents/on-page-seo/agent.md` Section 8 ("Handoff Patterns") and Section 13 ("Output Templates") reference this convention for the Fresh Optimization workflow, per-page brief file placement, and the mandatory keyword research block.
- `.claude/agents/on-page-seo/agent.md` Section 2 Step 0 is the canonical SCRIBE pre-flight tool verification protocol referenced under the Tool inventory section above; other agents may adopt the same pattern as added.
- `templates/consolidated-page-brief-template.md` is the canonical brief format for the Fresh Optimization workflow described above, including the '## Keyword research' block.
- `context/page-type-playbooks/product-page-playbook.md` 'Internal links only on product pages' is the canonical PDP link policy referenced above.
