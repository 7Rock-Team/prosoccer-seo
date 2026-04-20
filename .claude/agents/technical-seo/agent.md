# Technical SEO Agent

**Purpose (one line):** Audit and maintain site technical health so rankings are not capped by crawl, index, or performance problems.

**Status:** Not yet built. Scheduled for **Phase 1.2** of the rollout. See `CLAUDE.md`.

## Planned Responsibilities

- Run and interpret Screaming Frog crawls from `data/screaming-frog/`.
- Monitor Core Web Vitals (LCP, INP, CLS) and flag regressions.
- Audit schema markup (Product, Review, BreadcrumbList, Organization, LocalBusiness for both stores).
- Track indexation against expected index (Shopify collection and product pages).
- Identify orphaned pages and crawl traps in Shopify's faceted navigation.
- Draft theme code changes into `deliverables/technical-fixes/` for Mike to apply via `mike-audit` branch of the theme repo.

## Planned Tools

- Tavily MCP (verify live behavior)
- Memory MCP (namespace: technical-seo)
- File system (`data/screaming-frog/`, `deliverables/technical-fixes/`)
- Planned: Shopify MCP (read-only), GSC MCP.

## Known Dependencies Before Build

- `context/07-operational-context.md` populated (theme workflow)
- Screaming Frog access confirmed
- At least one baseline crawl in `data/screaming-frog/`
