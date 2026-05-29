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
   - **Collection pages:** SCRIBE pulls current copy via the Firecrawl MCP (`mcp__firecrawl-mcp__firecrawl_scrape`) for context. Current state does NOT appear in the visible brief.
   - **Product pages:** SCRIBE pulls all six fields (Title/H1, slug, Meta Title, Meta Description, Short Description, Long Description) via the Firecrawl MCP scrape of the live PDP. Short Description is rendered as the first paragraph in the description body on ProSoccer's Hyper theme (stored as a Shopify metafield); the scrape captures both Short and Long Description in a single call. Mike does NOT paste PDP body content; the live page is source of truth. If the scrape does not produce a clean Short / Long Description separation, surface as a blocker BEFORE drafting the brief per `context/page-type-playbooks/product-page-playbook.md` 'Current state capture (Shopify Hyper theme on ProSoccer)'. Current state does NOT appear in the visible brief.
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

**Category-specific H2 templates** for 15 product categories ProSoccer sells live in `context/page-type-playbooks/product-page-playbook.md` 'Category-specific H2 templates'. National-team-jersey template is CANONICAL, four-time validated within the 2026 World Cup cycle (UAE 2026 Home + Mexico 2026 Home / Away / Third per commits `e56a7d6`, `85dd1f0`, `f2c2c34`); remaining categories are at various validation stages from DRAFT v1 to CANONICAL per the playbook.

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
- deliverables/page-optimizations/YYYY-MM-DD_session-NN/: implemented YYYY-MM-DD via Shopify admin
- deliverables/page-optimizations/whitelabel-audit/YYYY-MM-DD_session-NN/: superseded by [reference]
- ...
```

The disposition note is the audit trail of why each folder was safely removable.

### Cleanup does NOT apply to

- Agent-specific briefings under `.claude/agents/<agent-name>/briefings/`. Those are agent-internal context that future sessions read; retention is per-agent and managed in the agent's own learnings.md compaction protocol.
- The `templates/` directory.
- Any deliverable file in `deliverables/technical-fixes/`, `deliverables/keyword-research/`, `deliverables/phase-2-discovery/`, or other non-page-optimization deliverable folders. Those have their own retention conventions to be documented separately as they emerge.

## Tool inventory

This section is the canonical truth source for which MCP servers and external tools are operationally available to the workforce today. Agent narrative sections (`## 5. Tools and MCP Connections` in each `.claude/agents/<agent-name>/agent.md`) may reference MCP namespaces aspirationally; this inventory governs what's actually callable. When a narrative description and this inventory disagree, this inventory wins.

Refreshed: 2026-05-26 (Phase C verification round).

### MCP categories (Category A vs Category B)

MCP servers split into two categories based on transport and credential handling. The distinction governs whether a sub-agent can call the MCP directly or must request the parent to fetch and pass data via task context.

**Category A: stdio transport, environment-variable credentials.** Full sub-agent inheritance via Option B `mcpServers:` declarations. When a sub-agent's frontmatter lists a Category A server, the sub-agent receives a native subprocess connection at dispatch and can call `mcp__<server>__*` tools directly. Credentials live in environment variables passed to the subprocess, not in OAuth state. Verified working 2026-05-26 via Phase C sub-agent test dispatches across SCRIBE, VERITAS, and RECON.

Category A servers:

- `dfs-mcp` (DataForSEO; DataForSEO API credentials via env)
- `firecrawl-mcp` (Firecrawl; `FIRECRAWL_API_KEY` via env)
- `tavily-mcp` (Tavily stdio variant; `TAVILY_API_KEY` via env)

**Category B: HTTP transport with OAuth tokens via the claude.ai connector.** OAuth state lives with the top-level Claude Code session that performed the OAuth handshake. When ORIN or any specialist is dispatched as a sub-agent, the `mcpServers:` declaration propagates (the sub-agent knows the server exists) but the OAuth token does not propagate to the sub-agent's MCP client. Direct sub-agent calls fail authentication. The workaround pattern: the parent ORIN session runs the Category B MCP call and passes the fetched data into the specialist's task context as inline data. Specialists treat Category B data as read-from-task-context, not read-from-MCP.

Category B servers:

- `claude_ai_Google_Drive` (Google Drive via claude.ai OAuth connector; reads from the January 2026 audit folder and other shared Drive artifacts)
- `claude_ai_Tavily` (OAuth-authenticated Tavily via claude.ai connector; superseded by Category A `tavily-mcp` for sub-agent use, kept registered at parent session for ORIN's top-level discovery work when full-page extraction is needed)

This category split is structural to current Claude Code architecture. If a future Claude Code release ships OAuth-token inheritance for sub-agents, the category distinction collapses and both classes work natively at sub-agent dispatch. Until that lands, the categories are operationally distinct and the workforce treats them as such.

### Operational (live, callable today)

- **DataForSEO MCP, `mcp__dfs-mcp__*`** (Category A). Pay-per-use API access covering SERP data, keyword research, keyword difficulty, search intent, on-page audit, backlinks, domain analytics, and DataForSEO Labs endpoints. Credentials verified 2026-05-26 (status_code 20000 returned on `mcp__dfs-mcp__serp_locations`). Sub-agent inheritance verified 2026-05-26 via Phase C. Workforce-wide hard cap $100/month per Section 12 of each agent.
- **Firecrawl MCP, `mcp__firecrawl-mcp__*`** (Category A). Single-URL scraping, structured extraction, site mapping, bulk crawling, interactive sessions, monitor and agent endpoints. `FIRECRAWL_API_KEY` in env. Installed 2026-05-26; sub-agent inheritance verified the same session (Phase C: status 200 returned on Liverpool PDP, Predator PDP, Predator collection page from SCRIBE, VERITAS, and RECON respectively).
- **Tavily MCP (stdio), `mcp__tavily-mcp__*`** (Category A). Full-page web search with content extraction, plus extract, crawl, map, and research endpoints. `TAVILY_API_KEY` in env. Installed 2026-05-26 as the sub-agent-compatible replacement for OAuth `claude_ai_Tavily`. Sub-agent inheritance verified the same session (Phase C: three live results returned for a Liverpool jersey query dispatched from SCRIBE).
- **Playwright MCP, `mcp__plugin_playwright_playwright__*`** (Category A in practice; the plugin runs locally and does not depend on claude.ai OAuth). Headless browser automation for live SERP inspection, SPA-rendered content extraction, post-deployment visual validation, and screenshot capture. Read-only posture for all workforce use.
- **Google Drive MCP, `mcp__claude_ai_Google_Drive__*`** (Category B). Reads from the January 2026 audit folder (`1KF1213I-_nf9B04ASKoM_mcv5xydJ3h8`) and other shared Drive artifacts. Free at API level; cost is context-budget consumption. Sub-agents see the declaration in their `mcpServers:` blocks but cannot complete OAuth from the sub-agent context. Parent ORIN fetches Drive content and passes it inline to specialists via task context. Direct sub-agent calls fail; surface the discrepancy in the session briefing if encountered.
- **Tavily MCP (OAuth via claude.ai), `mcp__claude_ai_Tavily__*`** (Category B). Registered at the top-level session for ORIN's parent-only research work. Sub-agents use Category A `tavily-mcp` instead; this OAuth surface is not listed in any sub-agent `mcpServers:` block. Retained at parent session level only.
- **Local file system.** All `data/`, `context/`, `deliverables/`, `strategy/`, `shared-intelligence/`, `work-log/`, and `.claude/agents/<agent>/` paths. Plus the prosoccer theme repo for read-only template inspection (SCRIBE, VERITAS).
- **`scripts/voice_check.py`.** Hard gate on every customer-facing copy proposal and every markdown deliverable. Per the 'Voice check discipline' section below, run on every modified file regardless of change type.

### Install pending (referenced in agent narratives but not yet callable)

- **GSC MCP, `mcp__gsc-server__*`.** Not installed as of 2026-05-26. **Install scheduled as a separate workstream for the 2026-05-27 session.** Expected to be Category A (stdio + OAuth-via-Google-service-account or env-credentialed; transport TBD at install time). Until install lands, fall back paths by use case:
  - **Ranking context per page (primary keyword position lookup):** DataForSEO SERP API via `mcp__dfs-mcp__serp_organic_live_advanced`. This is the canonical ranking-context source for the Fresh Optimization workflow Step 4 (see 'Fresh Optimization workflow' above). Once GSC MCP lands, ranking context shifts to GSC `get_search_analytics` per URL for the source-of-record advantage; DataForSEO SERP remains useful for competitor-context lookups but not for ProSoccer's own ranking baseline.
  - **CTR ceiling diagnostics, query-by-page intersection, indexation state, Rich Results coverage:** CSV exports under `data/gsc-exports/` (12-month `_top-pages.csv`, `_top-queries.csv`, `_search-appearance.csv`). CSV granularity is coarser than the live API: no query-by-page intersection, no live `inspect_url_enhanced`, no Rich Results report, no live coverage-issue inspection. Workable for baseline tracking, CTR ceiling diagnostics at page level, and aggregated query monitoring. Mike refreshes the exports on cadence (target: monthly).

### Implicit-fallback drift (the failure mode this inventory prevents)

Before this inventory existed, agent narratives referenced `mcp__firecrawl-mcp__firecrawl_scrape`, `mcp__gsc-server__get_search_analytics`, and `mcp__claude_ai_Tavily__tavily_search` as if those tools were live. Sessions that depended on those calls silently degraded to whichever tool happened to work, or stalled, or produced briefs that cited tools the workforce couldn't actually run. This implicit fallback hid the install gap from Mike and produced misleading "tool used" lines in session briefings.

The pre-flight tool verification protocol in SCRIBE Section 2 Step 0 (canonical pattern, other agents adopt as added) makes the tool inventory explicit at the start of every session. If an agent intends to use a tool listed under "Install pending" above, the session briefing must log the actual fallback used, not just the intended MCP namespace.

### Sub-agent MCP access matrix

Each workforce agent has explicit MCP server access declared in its `agent.md` frontmatter `mcpServers:` block (per the Option B configuration pattern documented in 'Sub-agent configuration discipline' below). Least-privilege scoping: each agent gets only the MCP servers its core function requires.

The category column reflects the Category A vs Category B distinction documented above. Category A servers grant direct sub-agent MCP access. Category B servers grant declaration-only access; data must be fetched at the parent ORIN level and passed via task context. A cell value of "yes" for a Category B server means the declaration is present in the agent's `mcpServers:` block, not that the sub-agent can complete an OAuth-authenticated call directly.

| Server | Category | master-strategist (ORIN) | on-page-seo (SCRIBE) | keyword-research (KIRA) | competitor-intel (RECON) | technical-seo (VERITAS) |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| dfs-mcp | A | yes | yes | yes | yes | yes |
| firecrawl-mcp | A | yes | yes | no | yes | yes |
| tavily-mcp | A | yes | yes | yes | no | no |
| plugin_playwright_playwright | A | yes | no | no | yes | no |
| gsc-server (install pending) | A (expected) | yes | yes | yes | no | yes |
| claude_ai_Google_Drive | B | yes | yes | yes | yes | yes |
| claude_ai_Tavily | B | parent-only | no | no | no | no |

Rationale per agent (Category A access governs direct callability; Category B access governs the parent-mediated workaround surface):

- **ORIN gets the full set.** Orchestrator role requires the ability to run any specialist's work at the parent level when needed (e.g., the parent-handles-MCP workaround pattern for Category B servers). ORIN holds the only `claude_ai_Tavily` surface in the workforce.
- **SCRIBE has DFS + Firecrawl + tavily-mcp + GSC (pending) + Drive (Category B).** Native Category A access to DFS, Firecrawl, and tavily-mcp covers keyword spot-validation, current-state PDP/collection extraction, and topic research with full-page content. No Playwright (Playwright is RECON's tool for competitor mobile-vs-desktop validation; SCRIBE doesn't need browser automation for copy production).
- **KIRA has DFS + tavily-mcp + GSC (pending) + Drive (Category B).** Keyword research is the core function; native Category A access to DFS and tavily-mcp covers SERP analysis, keyword discovery, and topic research. No Firecrawl (page scraping is SCRIBE/VERITAS work) or Playwright (browser automation is RECON's lane).
- **RECON has DFS + Firecrawl + Playwright + Drive (Category B).** Competitor monitoring needs SERP analysis (DFS), competitor page extraction (Firecrawl), and mobile-vs-desktop SERP rendering checks (Playwright). No tavily-mcp (Tavily is internal topic research, parent ORIN holds the OAuth Tavily for that work) and no GSC (GSC is own-site monitoring, not competitor monitoring).
- **VERITAS has DFS + Firecrawl + GSC (pending) + Drive (Category B).** Technical SEO needs SERP-position validation (DFS), site crawling (Firecrawl), and coverage diagnostics (GSC). No Playwright (covered by Section 8 handoffs to RECON when mobile-rendering checks are needed) and no tavily-mcp.

When a new specialist is built (SAGE Content Writer, METRIK Reporting), add a column to this matrix as part of the agent.md commit and update each agent's `mcpServers:` block to match.

### Update protocol

When an MCP install completes or auth lands:

1. Move the entry from "Install pending" to "Operational" with the verification date and the verification call used.
2. Update affected agent narrative sections to remove the install-pending caveats (the inventory references can stay implicit once the MCP is live).
3. Commit message format: `MCP install: <namespace> live. Tool inventory in workforce-conventions.md updated; agent narratives reference the MCP directly without fallback caveats.`

## Sub-agent configuration discipline

This section codifies the canonical configuration pattern for workforce sub-agents (the `agent.md` frontmatter that determines what tools and MCP servers each sub-agent can actually call). Verified against Claude Code documentation at `code.claude.com/docs/en/subagents` on 2026-05-26.

### Frontmatter pattern (Option B, canonical)

Two independent frontmatter fields govern tool availability:

- **`tools:`** is the allowlist for built-in Claude Code tools (Read, Write, Edit, Glob, Grep, Bash, etc.). If `tools:` is set as an allowlist, only those tools are callable; the sub-agent CANNOT use any MCP tools unless `mcpServers:` is also set. If `tools:` is omitted entirely, the sub-agent inherits every tool from the parent.
- **`mcpServers:`** is the allowlist for MCP servers. Each entry is either a bare server-name reference (e.g., `- dfs-mcp`) to a server configured in the parent session, or an inline server definition keyed by name. This field is the ONLY documented mechanism for scoping MCP access to a sub-agent.

The canonical pattern for ProSoccer workforce agents:

```yaml
---
name: <agent-name>
description: <agent description>
tools: Read, Write, Edit, Glob, Grep, Bash
mcpServers:
  - <server-1>
  - <server-2>
  - <server-N>
---
```

`tools:` carries only built-in capabilities. `mcpServers:` carries the per-agent MCP scope. Both fields are independent allowlists.

### Failure mode this pattern fixes

Before 2026-05-26, agent frontmatter declared MCP servers using invalid syntax in the `tools:` field (e.g., `tools: Read, Write, ..., mcp__dfs-mcp, mcp__firecrawl-mcp, ...`). Per Claude Code documentation (subagents page, line 315): "This example uses `tools` to exclusively allow Read, Grep, Glob, and Bash. The subagent can't edit files, write files, or use any MCP tools." Bare MCP names in the `tools:` field are not valid tool references; they're neither tool names (which follow `mcp__<server>__<tool>` format) nor server references (which belong in the separate `mcpServers:` field).

The visible symptom: sub-agents dispatched via the Agent tool reported their callable tools as `Read, Write, Edit, Glob, Grep, Bash` only, with no MCP tools exposed, despite frontmatter declarations to the contrary. The parent-handles-MCP workaround pattern (ORIN runs MCP calls, hands data to the sub-agent) was a band-aid; this configuration fix is the architectural correction.

### Least-privilege scoping principle

Each agent declares ONLY the MCP servers its core function requires. Master-strategist (ORIN) gets the full set because it orchestrates; specialists get only what they need to do their job. See the 'Sub-agent MCP access matrix' above for the canonical per-agent allocation. When adding a new MCP to the workforce (e.g., a future Ahrefs MCP), update the matrix and each agent's `mcpServers:` block to either include the server or explicitly omit it with a rationale logged here.

### Restart-required behavior

Per Claude Code documentation (subagents page, line 242): "Subagents are loaded at session start. If you add or edit a subagent file directly on disk, restart your session to load it." Editing any `agent.md` frontmatter (or the body) requires a Claude Code restart before the changes take effect in dispatched sub-agents. This is structural to Claude Code; it is not configurable.

Practical implication: when restructuring agent.md files for an architectural change like the Option B fix, the workflow is (1) commit the edits, (2) restart Claude Code, (3) verify the new configuration in dispatched sub-agents, (4) only then proceed with workflows that depend on the fix.

### Step 0 verification at sub-agent dispatch

The SCRIBE Section 2 Step 0 pre-flight tool verification protocol (canonical pattern, other agents adopt as added) verifies the `mcpServers:` block matches the expected per-agent access, with category-aware behavior. The protocol distinguishes Category A (direct health check) from Category B (parent-context verification).

**Category A verification (direct health check):**

1. On dispatch, the sub-agent confirms which Category A MCP server names appear callable in its tool schema (tools prefixed `mcp__<server-name>__*` exist for every Category A server in the `mcpServers:` block).
2. The sub-agent runs a no-cost health check call per Category A server it intends to use this session. Suggested test queries (cheap or free, used only to confirm subprocess connection and authentication):
   - `dfs-mcp`: `mcp__dfs-mcp__serp_locations` (returns location list; no per-call cost). Expected: status_code 20000.
   - `firecrawl-mcp`: a `mcp__firecrawl-mcp__firecrawl_scrape` on a known-stable URL (e.g., the target page if the session is going to scrape it anyway, so the health check doubles as the first real call). Expected: status_code 200.
   - `tavily-mcp`: a `mcp__tavily-mcp__tavily_search` with a low-volume query relevant to the session. Expected: top results returned.
3. If a Category A server listed in `mcpServers:` is not callable (tools missing from schema, or call returns an authentication error), the sub-agent logs the discrepancy in its session briefing and surfaces to ORIN or Mike before proceeding.

**Category B verification (parent-context check):**

1. On dispatch, the sub-agent recognizes that Category B servers (`claude_ai_Google_Drive`, `claude_ai_Tavily`) appear in the `mcpServers:` block as declarations but require parent-mediated data flow.
2. The sub-agent verifies the parent task context contains the Category B data it needs for the session (e.g., Drive file contents already fetched and passed by ORIN). If the data is present in the task context, proceed.
3. If a Category B fetch is needed and the data is not in the task context, the sub-agent does NOT attempt the direct MCP call. The sub-agent surfaces to ORIN: "need <specific Drive file or Tavily query> for <reason>; please fetch and pass via task context."
4. Direct Category B MCP calls attempted from sub-agent context will return OAuth-authentication errors; logging this is fine for diagnostic purposes but the sub-agent should not retry or interpret the failure as a system fault. It is a known architectural constraint.

**Drift detection (both categories):**

1. If a server NOT in the agent's `mcpServers:` block appears callable, log the over-permission as a config drift to be reconciled in the next agent.md commit.
2. If the categorization of a server appears to have changed (e.g., a Category B server starts returning successful direct calls from sub-agent context), surface immediately: this may indicate a Claude Code release shipped OAuth-token inheritance, which would collapse the category distinction.

This catches both under-permission (configuration didn't take effect, restart was skipped, server name typo, OAuth state missing) and over-permission (sub-agent inherited more than scoped) before they corrupt deliverable audit trails.

### Eligibility verification (Mike-pre-vetted at URL submission, updated 2026-05-29)

**Architectural pivot 2026-05-29.** Eligibility responsibility shifted from agent-detected (Firecrawl scrape) to Mike-pre-vetted (Shopify admin) after diagnostic on the Mexico Stadium SS kit set confirmed storefront-rendered signals are systematically unreliable.

**Architectural learning documented (2026-05-29 diagnostic findings):**

- Three different schema.org Offer.availability value formats across three pages of the same Hyper theme on prosoccer.com: bare string `InStock` on Home, full URL `http://schema.org/InStock` on Away, and human-readable `Out of stock` on Third. No internal consistency; format varies per page.
- Dual-schema injection confirmed on Mexico Away (`schema_offers_count: 2`): two competing Offer entries in JSON-LD, presumably one from Shopify core and one from an app (Rebuy, Klaviyo back-in-stock, pre-order/low-stock apps are likely candidates).
- Persistent variant selector "lies" on Home and Third: variant selector shows all sizes sold-out and Add-to-cart button disabled, while schema says InStock and the inventory hint shows real units available (31 on Home, 4 on Third). This is not transient cache; it reproduced today on fresh scrape (maxAge=0).
- The `Available in stock (X)` inventory hint was the only reliable signal across all three pages, accurately matching Mike's Shopify admin observation of stable inventory. This signal had been dismissed on 2026-05-28 as a JSON-extraction artifact because schema + button + variants all contradicted it.
- Mexico kit set application of the pre-tournament demand spike strategic exception (2026-05-28) was triggered by the false-positive triple-signal and baked false reasoning into all three brief deliverables. Fix-forward commit strips that strategic context while preserving substantive optimization content.

**Conclusion: storefront-rendered signals cannot be trusted for eligibility decisions.** Refining detection rules against an architecturally unreliable rendering layer (apps injecting competing schema, theme bugs in variant selector, format inconsistency across pages) is a losing game. Admin remains the source of truth. Human-in-the-loop at URL submission is the most reliable bridge between admin truth and agent workflow.

**Pre-flight pattern, updated:**

1. Step 0: tool exposure check (unchanged; verifies MCP servers callable this session).
2. Step 0.5: eligibility audit-trail step (NEW responsibility): URLs are assumed eligible because Mike pre-vetted in admin before submission; SCRIBE captures the eligibility status verbatim in the brief's strategic context section, including any Mike-flagged strategic exception with reasoning. Agents skip Firecrawl-based detection.
3. Workflow begins (Steps 1 through 11 in SCRIBE's startup protocol; delegation sequence in ORIN's Section 9).

**Strategic exceptions preserved as concepts:** closing-window optimization (sold-out end-of-life / closeout / discontinued-generation pages with retained collector value, no restock expected) and pre-tournament demand spike optimization (sold-out current-cycle pages with imminent tournament and expected restock) remain valid as architectural concepts. Both are now triggered by explicit Mike flag at URL submission, not by agent auto-detection. Codified in `context/page-type-playbooks/product-page-playbook.md` 'Strategic exception' subsections; for collections, seasonal-empty exception preserved similarly.

**Documented exception examples preserved:** Liverpool 2024-25 Nike Away Jersey v2 (commit b7159dc, closing-window) and adidas Predator Accuracy.1 FG Crazyrush Pack v2 (commit d52e56f, closing-window). These were appropriately optimized under closing-window framing per the pages' real end-of-life status and remain canonical examples.

Cross-references:

- `context/page-type-playbooks/product-page-playbook.md` 'Eligibility verification (Mike-pre-vetted at URL submission)' (canonical PDP version)
- `context/page-type-playbooks/collection-page-playbook.md` 'Eligibility verification (Mike-pre-vetted at URL submission)' (collection version)
- `.claude/agents/on-page-seo/agent.md` Section 2 Step 0.5 (audit-trail capture)
- `.claude/agents/master-strategist/agent.md` Section 9 'Candidate eligibility verification at Phase 1 surfacing' (ORIN candidate-handling)

### Eligibility verification as logical extension of Step 0 (added 2026-05-27, superseded 2026-05-29)

Step 0 (tool exposure verification) and eligibility verification (target-page status verification) are two pre-flight gates that share the same architectural pattern: confirm operational preconditions before substantive work begins.

Pre-flight pattern, in order:

1. Step 0: tool exposure check. Can the workforce actually run the MCP calls this session depends on?
2. Step 0.5: eligibility verification. Is the target page worth the optimization effort (in stock, visible, populated, not redirecting)?
3. Workflow begins (Steps 1 through 11 in SCRIBE's startup protocol; delegation sequence in ORIN's Section 9).

Eligibility detection method, default blocker behavior, and strategic exception path are codified in the page-type playbooks. SCRIBE applies the playbook eligibility section as Step 0.5 in `.claude/agents/on-page-seo/agent.md` Section 2. ORIN applies eligibility at the Phase 1 candidate-selection surfacing step in `.claude/agents/master-strategist/agent.md` Section 9.

Strategic exception types codified across the page-type playbooks (expanded 2026-05-28 to two PDP exception types after the Mexico kit set Day 1 production-reality check surfaced a structurally different sold-out pattern):

- **Closing-window optimization** (PDPs). End-of-life, closeout, or discontinued-generation inventory with retained collector or completist value. Restock not expected. Documented examples: Liverpool 2024-25 Nike Away Jersey v2 (commit b7159dc) and adidas Predator Accuracy.1 FG Crazyrush Pack v2 (commit d52e56f), both 2026-05-26 production predating the codification.
- **Pre-tournament demand spike optimization** (PDPs). Current-cycle inventory sold out with imminent tournament or seasonal demand event (typically 60 days or less) and expected restock during or after the event window. SEO equity lead time matters; the page must include strong internal linking to the relevant collection so customers landing on a sold-out PDP can navigate to in-stock alternates. Documented example: Mexico 2026 kit set Stadium SS Home/Away/Third (2026-05-28 codification), 2026 World Cup co-host kickoff June 11, about 14 days out, first documented pre-tournament demand spike override.
- **Seasonal empty collections**. Collection page intentionally empty ahead of product drop or between cycles.

All overrides require explicit Mike approval with the exception type named and strategic reasoning documented in the session briefing or brief production decision. New optimizations going forward default to eligible candidates. Decision-logic summary for choosing between closing-window vs pre-tournament demand spike vs default blocker lives in `context/page-type-playbooks/product-page-playbook.md` 'Decision logic for strategic exceptions'.

Cross-references:

- `context/page-type-playbooks/product-page-playbook.md` 'Eligibility verification (mandatory pre-Phase-1)'
- `context/page-type-playbooks/collection-page-playbook.md` 'Eligibility verification (mandatory pre-Phase-1)'
- `.claude/agents/on-page-seo/agent.md` Section 2 Step 0.5
- `.claude/agents/master-strategist/agent.md` Section 9 'Candidate eligibility verification at Phase 1 surfacing'

### Batch parallel dispatch + single daily batch commit (cross-cutting pattern, added 2026-05-29)

Production workflow runs as batch parallel dispatch with single daily batch commit per Mike's 2026-05-29 operational decision. Mike submits up to a 10-URL batch (eligibility pre-vetted in Shopify admin per the `Eligibility verification (Mike-pre-vetted at URL submission)` pattern). ORIN auto-classifies tier per URL (Tier 1 / 2A / 2B) and dispatches SCRIBE in parallel for all URLs concurrent via simultaneous Agent tool calls in a single message. Each SCRIBE instance runs the full per-tier discipline (research depth, brief drafting depth, field count) with all quality gates intact. After all briefs return, ORIN runs trust-but-verify per brief (read visible brief, independent voice check on both files, confirm gates pass) and then batch-commits all visible briefs + all workforce briefings + any follow-up files as a single atomic commit with comprehensive batch message. Single push.

**Speed target.** 10-URL mixed-tier batch completes in ~25-45 min wall clock vs ~3-4 hours sequential. The slowest individual brief in the batch sets the wall-clock floor; Firecrawl / DataForSEO / Tavily infrastructure response times are the secondary constraint.

**Quality discipline preserved per brief.** Voice check, 11 self-verification gates plus Gate 12 keyword distribution, year-specificity keyword discipline, brand IP compliance, currency check, sensitivity check, fact verification, internal link validation, per-brief workforce briefing audit trail. None of these flex under batch dispatch.

**Operational gates removed (safety gates preserved).** Per-brief Mike gate review replaced by end-of-batch review at single commit gate. Per-brief commit + push cycle replaced by single daily batch commit + push. Tier classification Mike confirmation replaced by ORIN auto-classification with post-batch Mike review of the classifications applied.

**End-of-batch summary.** ORIN surfaces to Mike: brief file paths, tier classifications applied, any quality issues flagged for Mike attention, cost tracking summary, any architectural learnings surfaced through the batch.

Cross-references: `.claude/agents/master-strategist/agent.md` Section 9 'Batch parallel dispatch and single daily batch commit' (ORIN procedural workflow); `.claude/agents/on-page-seo/agent.md` Section 9 'Tiered workflow variants' (per-tier scope SCRIBE applies regardless of dispatch pattern); `context/page-type-playbooks/product-page-playbook.md` 'Tiered workflow architecture for PDP optimization' + `context/page-type-playbooks/collection-page-playbook.md` 'Tier 2B canonical workflow' (per-page-type production workflow now runs under batch parallel dispatch as the production pattern).

### Tiered workflow architecture (cross-cutting pattern, added 2026-05-28)

Per-page brief production runs at one of four tiers depending on page type and strategic role. Tier is named at dispatch by ORIN (Section 9 'Tier classification at candidate dispatch'); SCRIBE adapts research depth, brief drafting depth, and field count accordingly (Section 9 'Tiered workflow variants'). Quality discipline preserved universally across all tiers.

Tier definitions:

| Tier | Page type | Time target | Scope | Proportion |
|---|---|---|---|---|
| Tier 1 | Foundational PDP (template-establishing, hero product, new category first) | ~25 to 35 min | Full SCRIBE workflow: broad Tavily, fresh brief build, all 11 gates | ~5 to 10% of PDPs |
| Tier 2A | Pattern-follow PDP (follows established CANONICAL template) | ~12 to 16 min | Scoped Tavily (currency only), template-fill drafting | ~70 to 80% of PDPs |
| Tier 2B | Collection page | ~15 to 20 min | Full workflow scoped to 6 collection-specific fields (Title, Slug, Meta Title, Meta Description, Short Description / hero block, body Description) | All collection pages |
| Tier 3 | Mike-drafted minimal | ~5 to 10 min | Mike drafts 4 to 6 fields; ORIN runs lightweight QA only | Rare exception |

Universal quality discipline (preserved across all tiers): voice check, 11 self-verification gates (including Gate 12 keyword distribution), brand IP compliance, year-specificity keyword discipline, eligibility verification (Step 0.5), keyword distribution discipline. What flexes per tier: research depth, brief drafting depth, field count.

Validation milestones for canonical templates:

- **National Team Jersey CANONICAL: four-time validated within the 2026 World Cup cycle.** Validation set: UAE 2026 Home Stadium Jersey v3 (foundational), Mexico 2026 Home Stadium SS (commit `e56a7d6`), Mexico 2026 Away Stadium SS (commit `85dd1f0`), Mexico 2026 Third Stadium SS (commit `f2c2c34`). Eligible for Tier 2A on subsequent NTJ work. Promoted 2026-05-28 in commit `44c2f2f`.
- **Club Jersey CANONICAL: Liverpool 2024-25 Nike Away Jersey v2 validation (commit `b7159dc`).** Eligible for Tier 2A on subsequent club jersey work.
- **Soccer Cleats VALIDATED v1: Predator Accuracy.1 FG Crazyrush Pack v2 validation (commit `d52e56f`).** Eligible for Tier 2A on subsequent older-cycle cleat work; pending one current-cycle flagship cleat validation for full CANONICAL promotion.
- **Tier 2B canonical reference: Mexico collection v5 (in production tonight as the first canonical Tier 2B brief under codified discipline; v4 at commit `f3cac86` is the pre-codification sketch that surfaced four template refinements).**

Cross-references:

- ORIN tier classification at dispatch: `.claude/agents/master-strategist/agent.md` Section 9.
- SCRIBE tiered workflow variants: `.claude/agents/on-page-seo/agent.md` Section 9.
- PDP-tier playbook detail (Tier 1, 2A, 3): `context/page-type-playbooks/product-page-playbook.md` 'Tiered workflow architecture for PDP optimization'.
- Collection-tier playbook detail (Tier 2B): `context/page-type-playbooks/collection-page-playbook.md` 'Tier 2B canonical workflow'.

### Plugin-provided MCP servers (caveat)

Per Claude Code documentation, plugin sub-agents (sub-agents loaded from a Claude Code plugin) do NOT support the `mcpServers:`, `hooks:`, or `permissionMode:` frontmatter fields. Our workforce agents live under `.claude/agents/` (project scope, not plugin scope), so this caveat does not apply to us. If a future workforce agent is ever loaded from a plugin, the `mcpServers:` block will be ignored and the agent will inherit the parent session's MCP scope by default; document the constraint in the agent's own agent.md.

## Architectural notes (MCP inheritance, OAuth gap, payload offload)

Three operational architectural facts emerged from the 2026-05-26 work installing Firecrawl + Tavily and verifying sub-agent inheritance. These are recorded here because they shape how the workforce configures and uses MCPs going forward; the underlying behaviors live in Claude Code itself and may shift in future releases.

### Refinement of commit 1ac5701 (partial discovery)

Commit 1ac5701 (2026-05-26 earlier in the day) established the Option B configuration pattern (`tools:` for built-in tools, `mcpServers:` for MCP servers) and verified DataForSEO inheritance at sub-agent dispatch. That commit framed the fix as architectural and complete. The subsequent install work surfaced that the Option B pattern is necessary but not sufficient: for OAuth-authenticated MCP servers (the claude.ai connector class), the `mcpServers:` declaration propagates to sub-agents but the OAuth token does not. The Category A vs Category B distinction codified above is the refinement that completes the picture. Commit 1ac5701 stands as the configuration-pattern fix; this commit refines the discovery with the transport-and-credentialing distinction that determines which servers can be called directly from sub-agent context.

The Liverpool (9eb344d) and Predator (bd309aa) briefs cited in commit 1ac5701 as Phase 6 validation remain valid under the refined model: those briefs were produced with the parent-handles-MCP workaround for the OAuth-class servers, which is exactly the workaround pattern the Category B classification documents. The briefs are not invalidated by the refinement; the architecture documentation just now captures why the workaround was necessary.

### OAuth-token inheritance gap

The mechanism: claude.ai connector MCPs (HTTP transport, OAuth-bearer authentication) maintain their access tokens in the top-level Claude Code session's OAuth state, not in environment variables. When the parent dispatches a sub-agent via the Agent tool, the sub-agent inherits the `mcpServers:` declaration but the OAuth state is not propagated to the sub-agent's MCP client. Direct sub-agent calls to `mcp__claude_ai_*__*` tools return authentication errors.

The architectural implication: until Claude Code ships OAuth-token propagation for sub-agents, any MCP server that depends on the claude.ai connector flow is structurally parent-only. The workaround (parent fetches, passes via task context) is operationally workable but adds a serialization step to multi-agent flows. When evaluating new MCPs for workforce integration, prefer Category A (stdio + env-credential) installations over Category B (OAuth via claude.ai connector) where both options exist for the same underlying service. The Tavily example is instructive: the OAuth `claude_ai_Tavily` worked at top-level but blocked sub-agent dispatch; the stdio `tavily-mcp` (with API key in env) works at every level.

If Claude Code ships OAuth-token inheritance for sub-agents in a future release, the category distinction collapses and both classes become operationally equivalent. The Step 0 drift-detection step is the workforce's early-warning signal for this change.

### Large-payload offload pattern

Observed in the RECON Phase C test (2026-05-26): a `mcp__firecrawl-mcp__firecrawl_scrape` on the Adidas Predator collection page returned a ~98,643-character markdown payload. The Claude Code harness wrote the payload to a tool-results file on disk (path: `<projects-dir>/<session-id>/tool-results/mcp-firecrawl-mcp-firecrawl_scrape-<timestamp>.txt`) rather than inlining the full content into the tool response visible to the sub-agent. The sub-agent received a truncated inline preview plus the file path for follow-up reading.

This is a Claude Code guardrail, not a Firecrawl error. The mechanism is silent (no warning surfaces in the tool result envelope; the agent must notice the response is partial and read the offload file to get the rest). Operational implication for the workforce: large-payload MCP calls (full-site crawls, collection-page scrapes with many product links, bulk DataForSEO endpoints) may land partially inline and partially on disk. Agents should:

1. Treat any unexpectedly short MCP tool response as a candidate for offload-file follow-up; check the tool-results directory for the timestamped file matching the call.
2. When a call is expected to return a large payload (collection page with 100+ products, bulk DFS endpoint, full-site Firecrawl crawl), plan to read the offload file rather than relying on the inline response.
3. Log the offload behavior in the session briefing when it occurs; it is a workflow detail that affects audit-trail reproducibility.

The offload threshold is set by the Claude Code harness and not configurable from agent context. The behavior may change in future Claude Code releases; if the threshold shifts or the mechanism changes, surface in the session briefing for forward documentation.

## Voice check discipline (defense-in-depth)

Run `scripts/voice_check.py` on every modified file regardless of what changed. The voice check tooling is fast; there's no operational reason to skip it on a per-edit basis. Defense-in-depth applies even to YAML frontmatter, configuration files, metadata edits, and internal context docs that aren't customer-facing prose.

The rationale: voice violations enter the codebase through editorial drift (an em-dash slipping into a config comment, an AI cliche phrase landing in a metadata description) just as easily as they enter through brief copy. Running the check universally costs nothing and catches incremental drift before it compounds. The discipline removes the judgment call ("is this file customer-facing enough to warrant checking?") that creates inconsistent enforcement.

Scope: every file the agent modifies in a session gets voice-checked before commit. Pass results are not surfaced in the visible session output; only failures surface to Mike or ORIN. Voice check failures on non-customer-facing files (YAML, configs, internal docs) are still resolved before commit, same as failures on customer-facing copy.

## Cross-references

- `context/brand-ip-constraints.md` documents the FIFA terminology constraint that applies to all page-optimization deliverables produced under this folder structure.
- `.claude/agents/on-page-seo/agent.md` Section 8 ("Handoff Patterns") and Section 13 ("Output Templates") reference this convention for the Fresh Optimization workflow, per-page brief file placement, and the mandatory keyword research block.
- `.claude/agents/on-page-seo/agent.md` Section 2 Step 0 is the canonical SCRIBE pre-flight tool verification protocol referenced under the Tool inventory section above; other agents may adopt the same pattern as added.
- `templates/consolidated-page-brief-template.md` is the canonical brief format for the Fresh Optimization workflow described above, including the '## Keyword research' block.
- `context/page-type-playbooks/product-page-playbook.md` 'Internal links only on product pages' is the canonical PDP link policy referenced above.
