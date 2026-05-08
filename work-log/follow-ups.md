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
| 2026-04-26 | mcp-gsc install: REGISTERED but AUTH PENDING. uvx + OAuth setup complete; gsc-server appears in /mcp as connected. First-run browser auth fails with Error 400: redirect_uri_mismatch. Likely cause: OAuth client was created as "Web application" type instead of "Desktop app" type. To resume: (1) delete current OAuth client at console.cloud.google.com/apis/credentials, (2) recreate as Desktop app type, (3) download new JSON, replace ~/.gcp/prosoccer-gsc-oauth.json, (4) restart Claude Code, (5) retry get_capabilities call. Estimated resume time: 10-15 min from fresh state. Paused 2026-04-26 at 2h 45min into install due to compounding infrastructure friction (service account rejection, Microsoft Store Python alias, PATH wrestling, now OAuth client type). Better to resume tomorrow with fresh focus. | Mike to complete OAuth client recreation tomorrow morning before VERITAS work; integration into KIRA agent.md follows | Open |
| 2026-04-27 | Extend voice_check.py to accept a string argument directly (currently accepts file paths only). SCRIBE's pattern for checking individual proposed strings is to stage in a temp file. Tooling improvement, not workforce-blocking. | Master Strategist or Mike to schedule when free | Open |
| 2026-05-08 | Confirm magento1.prosoccer.com subdomain is fully deprecated and redirected. Investigate any URLs still indexed under that subdomain and flag for redirect-strategy work. Surfaced from GSC property inventory 2026-05-08. | VERITAS (Technical SEO Agent) | Open |
| 2026-05-08 | KIRA agent.md uses different section numbering than canonical 13-section pattern (KIRA's Section 13 is First-Session Behavior; KIRA has no separate Output Templates section). Phase 4 of architecture refinement worked around this by appending Contribution to Consolidated Briefs and per-page template as subsections of Section 8. Future consideration: should KIRA be restructured to match the canonical 13-section pattern that VERITAS/SCRIBE/RECON/ORIN follow? Cost: invasive edit; would touch most of KIRA's existing numbering. Benefit: easier cross-agent reference and onboarding for new team members. Decision deferred until clear operational pain emerges. | ORIN proposes; Mike to decide if/when to schedule | Open |

## Closed

| Date opened | Task | Owner | Status |
|---|---|---|---|
| 2026-05-08 | Decide whether prosoccerteamstore.com is in or out of Phase 1 SEO scope. Surfaced from GSC property inventory 2026-05-08. RESOLVED 2026-05-08: prosoccerteamstore.com is out of scope. It's the client's separate Shopify website (likely team sales / wholesale). Not in current SEO engagement. Exclude from KIRA priority work, RECON monitoring, METRIK reporting, and all workforce deliverables. Reference only sc-domain:prosoccer.com and its locale URL-prefix variants going forward. | Mike to advise; ORIN to formalize | Closed |

## Coming Up
| 2026-04-21 | Name all 7 specialist agents with human/memorable names (proposed starting point: ORIN, KIRA, VERITAS, SCRIBE, SAGE, RECON, METRIK, with Mike to review and adjust). Friendly names used everywhere including Tony-facing docs. Rename propagates to agent definition headers, memory file first-person references, context files, progress map SVG labels, and client deliverable references. | Mike | Open |

| 2026-04-21 | Evaluate Firecrawl for agent workforce. Capabilities: AI-optimized web scraping, full-site crawls, clean markdown output, batch SERP inspection. Strongest fit for RECON (competitor monitoring) and SAGE (content research). Free tier available for testing. Paid tier $80-100/month likely if workforce benefits justify. Test during April 22-27 before RECON build on April 28-29. | Mike to sign up for free tier; Master Strategist to evaluate during RECON build | Open |