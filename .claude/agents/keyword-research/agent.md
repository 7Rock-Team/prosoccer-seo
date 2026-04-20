# Keyword Research Agent

**Purpose (one line):** Build and maintain the keyword map that drives every content and on-page decision.

**Status:** Not yet built. Scheduled for **Phase 1.1** of the rollout (first specialist). See `CLAUDE.md` for rollout order.

## Planned Responsibilities

- Pull GSC, Ahrefs, and GA4 exports from `data/` and cross-reference with product catalog.
- Maintain `strategy/keyword-map.md` as the canonical keyword-to-URL mapping.
- Identify gaps (intent with no URL) and cannibalization (multiple URLs for the same intent).
- Score keywords by revenue potential, not just volume.
- Propose quarterly keyword targets to the Master Strategist.

## Planned Tools

- Tavily MCP (SERP inspection)
- Memory MCP (namespace: keyword-research)
- File system (read `data/`, write `strategy/keyword-map.md`)
- Planned: Google Search Console MCP when available.

## Known Dependencies Before Build

- `context/00-business-overview.md` populated
- `context/04-product-catalog-overview.md` populated
- `context/05-competitors.md` populated
- `context/06-business-goals.md` populated
- At least one export in `data/gsc-exports/` and `data/ahrefs/`
