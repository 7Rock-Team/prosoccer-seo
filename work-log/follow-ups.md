# Follow-Ups

_Lightweight tracker for open items awaiting action from Mike, a specialist agent, or an external party. Weekly narrative logs still live in `YYYY-WW.md` files per the README._

## Format

| Date opened | Task | Owner | Status |
|---|---|---|---|

## Open

| Date opened | Task | Owner | Status |
|---|---|---|---|
| 2026-04-21 | Verify Korean-market affiliates in AWIN and PayAudit. May or may not explain the Korean-anchor-text backlink cluster. Deferred from 2026-04-21 discovery closeout. | Mike | Pending |
| 2026-04-21 | Run soccertop.com forensic review and prepare disavow file. Confirmed non-affiliate (see `shared-intelligence/seo-findings.md`); origin investigation needed before disavow submission. | Technical SEO Agent (not yet built) | Pending |
| 2026-04-21 | Add "plain language for Tony-facing documents" rule to `context/03-brand-voice.md`. Current voice rules catch em-dashes and AI-cliche phrases but don't catch industry jargon ("attribution model," "triangulate," "organic signal," etc.) that's unclear to non-specialist readers. Define a rule scoped to client-facing deliverables and add a corresponding check to `scripts/voice_check.py`. | Mike (or Master Strategist in a future session) | Open |
| 2026-04-21 | Migrate strategy/keyword-map.md to strategy/keyword-map.csv with structured columns (keyword, intent, volume, difficulty, target URL, current position, priority tier, notes, last reviewed date). Current md is a starter scaffold; CSV is the scalable format. | Keyword Research Agent (during or after first matrix production) | Open |
| 2026-04-21 | Configure DataFeedWatch feed for inventory intelligence: product ID, title, collection, stock level, product type, vendor, price, days since created, days since last sale, inventory age signal, movement signal, overstocked flag. Output as CSV to a location KRA can read (data/shopify-inventory/). Extends the existing DataFeedWatch account 7 Rock already manages. | Mike to configure; Master Strategist to wire into workflow | Open |
| 2026-04-21 | Build shared-intelligence/inventory-state.md infrastructure: template with collection-level rollups, monthly update mechanism, cross-agent startup protocol references. Master Strategist summarizes DataFeedWatch feed output into this file for all agents to consume. | Master Strategist in future session | Open |
| 2026-04-21 | Interim inventory approach: manual Shopify inventory export (product title, collection, stock level, date created, last sale date) to data/shopify-inventory/. Use until DataFeedWatch feed is configured. First matrix can rely on this interim data. | Mike to export one-time; KRA to consume | Open |
| 2026-04-22 | Inventory classification methodology deferred until DataFeedWatch feed lands or dedicated Shopify products-by-collection export is available. KIRA matrix v1 uses sales-by-product.csv as Medium-confidence proxy for inventory signals. When data is available, define formal Hero/Mid/Zombie thresholds with Mike based on operational reality, not assumed numbers. | Mike to advise; Master Strategist to formalize when data lands | Open |

## Closed

| Date opened | Task | Owner | Status |
|---|---|---|---|
| 2026-04-26 | Install mcp-gsc (Google Search Console MCP) before VERITAS build. Provides live GSC data access for METRIK reporting and tactical work between matrix refreshes. Resolved 2026-04-26: installed via uvx with OAuth user authentication; service account approach hit GSC user-grant rejection so OAuth path was used instead. MCP registered in local project-scope Claude Code config (`C:\Users\Ashot\.claude.json` under project entry for prosoccer-seo). First-run browser auth pending; triggers on first MCP call after Claude Code restart. Setup took approximately 2 hours total due to Microsoft Store Python alias issue and service account email rejection by GSC; documented for future MCP installs that need OAuth. | Mike (installed); Master Strategist to integrate during METRIK build | Closed (resolved 2026-04-26) |

## Coming Up
| 2026-04-21 | Name all 7 specialist agents with human/memorable names (proposed starting point: ORIN, KIRA, VERITAS, SCRIBE, SAGE, RECON, METRIK, with Mike to review and adjust). Friendly names used everywhere including Tony-facing docs. Rename propagates to agent definition headers, memory file first-person references, context files, progress map SVG labels, and client deliverable references. | Mike | Open |

| 2026-04-21 | Evaluate Firecrawl for agent workforce. Capabilities: AI-optimized web scraping, full-site crawls, clean markdown output, batch SERP inspection. Strongest fit for RECON (competitor monitoring) and SAGE (content research). Free tier available for testing. Paid tier $80-100/month likely if workforce benefits justify. Test during April 22-27 before RECON build on April 28-29. | Mike to sign up for free tier; Master Strategist to evaluate during RECON build | Open |