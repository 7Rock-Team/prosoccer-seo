# Agent Inventory: ProSoccer SEO Workforce

> **Auto-generated reference.** This file is built from the YAML frontmatter of each `.claude/agents/<agent-name>/agent.md`. Regenerate it whenever an agent's `name:`, `description:`, `tools:`, or `mcpServers:` block changes, or when a new specialist is added to the workforce.
>
> **Generated:** 2026-05-26
> **Last verified:** 2026-06-09 (Phase C: `gsc-server` sub-agent inheritance confirmed; promoted (A\*) to (A)).
> **Category annotations source:** commit `0c6dbb3` (2026-05-26 architecture refinement codifying Category A vs B distinction for MCP sub-agent inheritance).

## Inventory Table

| Agent (`name:`) | Function | Tools (non-MCP) | mcpServers |
|---|---|---|---|
| **master-strategist** | ORIN: Master Strategist. Coordinates the SEO workforce (KIRA, VERITAS, SCRIBE, RECON; SAGE/METRIK when built). Owns consolidated per-page brief production, master tracking infrastructure (`collections-master.csv`, `products-master.csv`, `technical-seo-log.md`), multi-agent workflow sequencing, strategic positioning calls, cross-agent escalation, strategic threat alert routing, and quality gates before deliverables reach Mike. Mike's primary interface. Reports to Mike. | Read, Write, Edit, Glob, Grep, Bash | claude_ai_Google_Drive **(B)**, dfs-mcp **(A)**, firecrawl-mcp **(A)**, gsc-server **(A)**, plugin_playwright_playwright **(A\*)**, tavily-mcp **(A)** |
| **on-page-seo** | SCRIBE: On-Page SEO. Owns title tags, meta descriptions, H1s, intro and body copy on collection pages, schema-aware copy production, voice consistency advisory, and CTR ceiling diagnostics. Reports to ORIN. | Read, Write, Edit, Glob, Grep, Bash | claude_ai_Google_Drive **(B)**, dfs-mcp **(A)**, firecrawl-mcp **(A)**, gsc-server **(A)**, tavily-mcp **(A)** |
| **keyword-research** | KIRA: Keyword Research. Owns the keyword universe, the Category Priority Matrix, search intent mapping, and SERP feature opportunity identification. Feeds target keywords downstream to SCRIBE, SAGE, VERITAS, METRIK, RECON. Reports to ORIN. | Read, Write, Edit, Glob, Grep, Bash | claude_ai_Google_Drive **(B)**, dfs-mcp **(A)**, gsc-server **(A)**, tavily-mcp **(A)** |
| **technical-seo** | VERITAS: Technical SEO. Owns URL architecture, redirect strategy, structured data and schema markup, indexation and crawlability, Core Web Vitals, hreflang, and backlink remediation. Reports to ORIN. | Read, Write, Edit, Glob, Grep, Bash | claude_ai_Google_Drive **(B)**, dfs-mcp **(A)**, firecrawl-mcp **(A)**, gsc-server **(A)** |
| **competitor-intel** | RECON: Competitor Intelligence. Owns cross-competitor monitoring across keyword strategy, on-page tactics, backlink profile analysis, pricing and merchandising signals, content strategy, technical patterns, new competitor detection, and strategic threat alerts. Reports to ORIN. | Read, Write, Edit, Glob, Grep, Bash | claude_ai_Google_Drive **(B)**, dfs-mcp **(A)**, firecrawl-mcp **(A)**, plugin_playwright_playwright **(A\*)** |

## Category Legend

Per 2026-05-26 architecture refinement (commit `0c6dbb3`):

- **(A) Category A**: stdio transport plus env-variable credentials. Full sub-agent inheritance via Option B `mcpServers:` declarations. Explicitly classified in commit `0c6dbb3`: `dfs-mcp`, `firecrawl-mcp`, `tavily-mcp`. Verified working at sub-agent dispatch level during Phase C verification. `gsc-server` promoted from inferred (A\*) to (A): inheritance verified 2026-06-09 via Phase C (parent ORIN and dispatched SCRIBE sub-agent both returned `sc-domain:prosoccer.com`).
- **(B) Category B**: HTTP transport plus OAuth via the claude.ai connector. Sub-agents inherit the `mcpServers:` declaration but **not** the OAuth state; the parent (ORIN) must run the calls and pass data downstream via task context. Explicitly classified in commit `0c6dbb3`: `claude_ai_Google_Drive`, `claude_ai_Tavily` (the latter is the OAuth variant; `tavily-mcp` stdio is its sub-agent-compatible replacement).
- **(A\*) Inferred Category A**: follows the Category A pattern (no `claude_ai_` prefix, stdio-style server) but was not explicitly annotated in commit `0c6dbb3`. Now applies only to `plugin_playwright_playwright` (`gsc-server` was verified 2026-06-09 via Phase C and promoted to (A) above). Inheritance behavior at the sub-agent dispatch level should be verified by test before being relied on operationally. Tracked in `work-log/follow-ups.md`.

## MCP Allocation Matrix

| MCP | ORIN | SCRIBE | KIRA | VERITAS | RECON |
|---|:-:|:-:|:-:|:-:|:-:|
| claude_ai_Google_Drive (B) | x | x | x | x | x |
| dfs-mcp (A) | x | x | x | x | x |
| firecrawl-mcp (A) | x | x | - | x | x |
| gsc-server (A) | x | x | x | x | - |
| tavily-mcp (A) | x | x | x | - | - |
| plugin_playwright_playwright (A\*) | x | - | - | - | x |

## Regeneration Procedure

When an agent definition changes:

1. Re-read the `---` frontmatter block of every `.claude/agents/<agent-name>/agent.md`.
2. Update the inventory table row (name, function from the description, tools, mcpServers).
3. Re-classify any new MCP server entries against the Category A vs B definition above. New `claude_ai_*` HTTP connectors are Category B by default; new stdio-style servers are Category A but should be confirmed via sub-agent dispatch test before being trusted to inherit.
4. Update the MCP allocation matrix.
5. Bump the **Generated** date at the top.
6. If category definitions themselves change, update the commit reference too.

Not meant to be committed standalone; fold into the next architecture-relevant commit, or into the next `context/workforce-conventions.md` update.
