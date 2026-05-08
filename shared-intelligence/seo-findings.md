# SEO Findings

_Cross-agent intelligence on site-specific SEO patterns surfaced during discovery or ongoing work. Any agent can read. The Master Strategist is the default writer. Relevant to: Keyword Research, Content Writer, On-Page SEO, Competitor Intel._

## How to Use

Log site-specific SEO observations that should shape future strategy, content templates, or keyword targeting. Not for industry news (use `industry-updates.md`), algorithm updates (use `algorithm-updates.md`), or tool changes (use `tool-changelog.md`). This file is for things we learn about ProSoccer's own search surface.

## Format

```
### YYYY-MM-DD - Short headline

**Finding:** one sentence.
**Evidence:** data source, file path, or measurement.
**Strategic implication:** the lesson or action this suggests.
```

## Entries

### 2026-04-21 - Player-spotlight page outperforms national team collections

**Finding:** `/collections/lamine-yamal-jersey-fc-barcelona-spain` ranks at position 10.4 with 791 clicks on 118,981 impressions (12-month GSC), outperforming every national team collection page on the site including Mexico, Italy, and the full committed-sprint 6.
**Evidence:** `data/gsc-exports/2025-04-to-2026-04_top-pages.csv`, cross-referenced in Phase 2 Task 2 deliverable.
**Strategic implication:** Player-spotlight templates (single player tied to club + country) may be a higher-yield content type than country-level collections. Worth testing with Messi (Argentina), Vinicius (Brazil), Mbappé (France), Haaland (Norway) post-WC sprint. Keyword Research Agent should validate query volume on player-name searches before scoping.

### 2026-04-21 - soccertop.com backlink concentration

**Finding:** ~16M backlinks from a single UAE domain (soccertop.com), over 90% of ProSoccer's total backlink profile. Confirmed NOT an AWIN affiliate and NOT in PayAudit per Mike's verification.
**Evidence:** Majestic backlink report (Phase 1 audit, file 7). AWIN roster and PayAudit cross-reference by Mike, 2026-04-21.
**Strategic implication:** High-priority disavow candidate for Technical SEO Agent Month 1 work. Origin investigation (scrape, mirror, or negative SEO) is a separate follow-up. Korean backlink cluster still pending AWIN/PayAudit verification.

### 2026-05-08 - Subagent MCP runtime gap surfaced during Mexico Wave 1 consolidated brief

**Finding:** Specialist agent MCPs declared in agent.md frontmatter (KIRA's GSC, RECON's DataForSEO + Firecrawl + Tavily, SCRIBE's Firecrawl + DataForSEO + GSC, VERITAS's Firecrawl + DataForSEO + GSC) did not surface in the subagent tool roster when invoked via the Agent tool during the 2026-05-08 Mexico run. Symptom: each subagent reported its tool inventory was limited to Read/Write/Edit/Glob/Grep/Bash. Confirmed for KIRA and RECON via explicit "execution blocker" returns from those agents; SCRIBE and VERITAS were briefed proactively with inline data to work around the same expected gap.

**Evidence:** KIRA's per-page contribution open flag #1 ("GSC MCP not surfaced in this session's tool roster"); RECON's per-page contribution surfaced an explicit "EXECUTION BLOCKER" section listing missing MCPs and offered two paths to ORIN; ORIN absorbed the data gathering for all four specialists in the main thread (4 GSC MCP calls, 1 DataForSEO SERP scan, 5 Firecrawl scrapes plus 1 JSON-extraction scrape) and supplied results inline to SCRIBE and VERITAS at delegation time. Specialist-vs-ORIN token ratio reached approximately 1:3 (ORIN-heavy) for the session, well above the 1:1 ratio implied by a "coordinate-don't-execute" architecture per ORIN agent.md Section 12.

**Strategic implication:** Affects every multi-agent run, not just Mexico. At Wave 2 scale (20+ pages) the gap becomes the dominant ORIN coordination cost surface and breaks the consolidate-don't-fragment posture. Two paths to resolve: (a) investigate Claude Code subagent MCP-inheritance configuration (frontmatter, settings, Agent tool subagent_type runtime contract) to fix the propagation; (b) shift to a streamlined ORIN-with-playbooks architecture where ORIN executes data gathering by design and specialists become opinionated processors of pre-gathered data. Path (b) is in design as of 2026-05-08. Streamline signal triggered for architectural reason rather than ORIN coordination overhead. Decision pending architecture build; tracked in `work-log/follow-ups.md`.

### 2026-05-08 - GSC property inventory and canonical reporting choice

**Finding:** ProSoccer.com has 8 GSC properties: one Domain property (sc-domain:prosoccer.com), two root URL-prefix properties (https://prosoccer.com/, https://www.prosoccer.com/), four locale URL-prefix variants (en-au, en-ca, en-gb, en-es), one legacy subdomain (sc-domain:magento1.prosoccer.com), and one separate domain (https://prosoccerteamstore.com/). The Domain property is the only one that aggregates www, non-www, and locale subpaths into a single search-surface view. Note: prosoccerteamstore.com out of scope per Mike 2026-05-08; workforce focuses exclusively on prosoccer.com properties.
**Evidence:** gsc-server list_properties call, 2026-05-08. 25 total properties returned across all 7 Rock client accounts; 8 belong to the ProSoccer footprint.
**Strategic implication:** Workforce-wide reporting (METRIK, ORIN, RECON) defaults to sc-domain:prosoccer.com for aggregated metrics. Locale URL-prefix properties (en-au, en-ca, en-gb, en-es) are used only when locale-segmented data is specifically needed, e.g., regional ranking deltas, hreflang QA, or locale-specific keyword tracking. magento1.prosoccer.com (legacy subdomain, deprecation status unconfirmed) tracked in work-log/follow-ups.md.
