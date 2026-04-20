# Content Writer Agent

**Purpose (one line):** Draft articles, buying guides, and sizing content that match the ProSoccer brand voice and target the right keywords.

**Status:** Not yet built. Scheduled for **Phase 1.4** of the rollout. See `CLAUDE.md`.

## Planned Responsibilities

- Write first drafts from briefs produced by the Master Strategist.
- Enforce every rule in `context/03-brand-voice.md` before submitting a draft.
- Output drafts to `deliverables/content-drafts/in-progress/<slug>.md`.
- Include suggested title, meta description, URL slug, internal links, featured image direction, and FAQ schema entries.
- Hand off to the human writer for polish, then to Mike for final review.

## Planned Tools

- Tavily MCP (fact-check, pull recent references)
- Memory MCP (namespace: content-writer)
- File system

## Known Dependencies Before Build

- All four avatar files in `context/02-avatars/` populated
- `context/03-brand-voice.md` populated
- Keyword map exists
- Editorial calendar has at least one scheduled piece
