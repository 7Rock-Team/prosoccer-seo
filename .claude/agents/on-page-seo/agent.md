# On-Page SEO Agent

**Purpose (one line):** Optimize titles, meta descriptions, headings, internal links, and body copy on priority pages.

**Status:** Not yet built. Scheduled for **Phase 1.3** of the rollout. See `CLAUDE.md`.

## Planned Responsibilities

- Audit priority pages against the keyword map.
- Draft new title tags and meta descriptions into `deliverables/meta-optimizations/`.
- Recommend H1 and heading structure changes.
- Propose internal link improvements (collection to product, content to collection).
- Enforce brand voice rules from `context/03-brand-voice.md` on every rewrite.

## Planned Tools

- Tavily MCP (inspect live pages)
- Memory MCP (namespace: on-page-seo)
- File system

## Known Dependencies Before Build

- Keyword map exists at `strategy/keyword-map.md`
- `context/03-brand-voice.md` populated
- Priority URL list from Master Strategist
