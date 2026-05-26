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

## Fresh Optimization workflow (default mode)

Fresh Optimization is the default workflow for page-optimization deliverables produced by SCRIBE under ORIN orchestration. The whitelabel audit mode is opt-in and used only when Mike explicitly requests it.

### Workflow steps

1. Load context: page-type playbook matching the page (`context/page-type-playbooks/`), `context/brand-ip-constraints.md`, the six copy-writing principles in `context/03-brand-voice.md`.
2. Capture current state per page type:
   - **Collection pages:** Firecrawl scrape covers Title, Slug, Meta Title, Meta Description, and the description body.
   - **Product pages:** Firecrawl scrape covers Title, Slug, Meta Title, Meta Description only. Mike supplies the existing Short Description and Long Description directly. SCRIBE does NOT scrape PDP body content; SCRIBE waits for Mike to provide it.
3. Topic research via Tavily scaled to familiarity:
   - Well-known topics (Mexico, Argentina, major brands): 2 to 5 queries.
   - Unfamiliar topics: 5 to 10 queries.
   - Do not over-research what prior sessions already documented.
4. Generate the optimized brief in the format at `templates/consolidated-page-brief-template.md`. Default visible content is the Current state block and the Recommended new SEO setup block, nothing more.
5. Validate every proposed internal link via Firecrawl (status code 200, page-type signals confirmed, no soft-404) per the matching playbook's link strategy (1 to 2 max).
6. Run voice check (`scripts/voice_check.py`) and the 11 gates from `.claude/agents/on-page-seo/agent.md` Section 11 silently. Pass results are NOT surfaced in the visible brief; only an unresolvable failure surfaces to Mike. All gate results are documented in the workforce-internal briefing at `.claude/agents/on-page-seo/briefings/YYYY-MM-DD_<slug>.md`.
7. Hold at GATE for Mike review.
8. Append the matching row to `deliverables/tracking/collections-master.csv` or `products-master.csv` once Mike approves.

### Workforce-internal briefing (preserved, not surfaced by default)

The workforce-internal briefing at `.claude/agents/on-page-seo/briefings/YYYY-MM-DD_<slug>.md` continues to capture brand-affiliation classification, avatar scope, topic research findings, compliance scan results, per-string voice check status, 11-gate self-verify status, cost tracking, and any other workforce-internal context. Mike can request this briefing on demand at any time. It is not surfaced at gate review by default.

### Optional mode: Whitelabel audit

The whitelabel audit mode adds a `## Comparison with current state` section to the brief between the Current state block and the Recommended new SEO setup block, showing field-by-field deltas with reasoning. This mode is opt-in. Mike must explicitly request "whitelabel audit" (or equivalent phrasing) for the comparison section to appear in the brief. Without an explicit request, Fresh Optimization with no comparison narrative is the default.

### Speed optimizations baked into Fresh Optimization

1. Topic research scales to familiarity rather than running a fixed query count per page.
2. Voice check and the 11 gates run silently; pass results do not surface; only unresolvable failures get flagged to Mike.
3. No comparison table or audit narrative in the visible brief unless whitelabel audit mode is requested.
4. Workforce-internal briefing stays a separate file and is not surfaced at gate review by default.
5. For batched sessions, context loads once per session, not per page.

## Brief content requirements (data-backed)

Both PDP and collection-page briefs must surface keyword research data and respect the product-page link policy. These are hard requirements, not optional.

### Keyword research surfacing (mandatory on every brief)

Every visible brief must include a `## Keyword research` block above the Current state block with:

- Primary keyword with monthly search volume and keyword difficulty, intent classification (informational, commercial, transactional). DataForSEO is the source of record.
- 2 to 3 alternative candidates evaluated, each with volume and KD plus a 1 to 2 sentence why-not-chosen reasoning that references the data and avatar fit.
- Selection reasoning: 1 to 2 sentences combining the data, the avatar fit, and the page-level competitive context.
- Supporting long-tail keywords with volume data.

Trust-me keyword choices are not acceptable for agency-grade work. The primary keyword selection must be defensible against "why this keyword and not the other one" with concrete data.

The visible '## Keyword research' block format is canonical in `templates/consolidated-page-brief-template.md` and replicated in `.claude/agents/on-page-seo/agent.md` Section 13.

### Product page link policy: internal only

PDP body copy includes internal links to ProSoccer collection or product pages ONLY. External links are forbidden on PDPs. The reasoning:

- External links leak link equity off-site during the purchase consideration window.
- They give the customer an exit ramp from the purchase decision.
- Authority signals through external links belong on homepage and blog content, not on PDPs.

If body copy references external tournaments, events, or context (Asian Cup, Champions League, Premier League, etc.), keep the reference as plain text. Do not hyperlink to external sites. If the reference needs a destination, link to an internal ProSoccer page instead (e.g., a related collection).

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
- **GSC MCP, `mcp__gsc-server__*`.** Not installed as of 2026-05-26. Until install lands, fall back to CSV exports under `data/gsc-exports/` (12-month `_top-pages.csv`, `_top-queries.csv`, `_search-appearance.csv`). CSV granularity is coarser than the live API: no query-by-page intersection, no live `inspect_url_enhanced`, no Rich Results report, no live coverage-issue inspection. Workable for baseline tracking, CTR ceiling diagnostics at page level, and aggregated query monitoring. Mike refreshes the exports on cadence (target: monthly).
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
