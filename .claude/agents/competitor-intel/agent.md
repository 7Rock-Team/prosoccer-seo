# Competitor Intel Agent

**Purpose (one line):** Track competitor SERP positions, new content, backlinks, and schema changes so we can respond before they take share.

**Status:** Not yet built. Scheduled for **Phase 1.5** of the rollout. See `CLAUDE.md`.

## Planned Responsibilities

- Maintain a watch list of competitors (from `context/05-competitors.md`).
- Monitor SERP movement for our top 50 target keywords against the watch list.
- Track new content publication on competitor domains.
- Track backlink changes (when Ahrefs data refreshes).
- Alert the Master Strategist when a competitor makes a move worth responding to.

## Planned Tools

- Tavily MCP (SERP and content monitoring)
- Memory MCP (namespace: competitor-intel)
- File system

## Known Dependencies Before Build

- `context/05-competitors.md` populated
- Keyword map exists
- A target keyword set is defined
