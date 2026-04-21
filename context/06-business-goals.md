# 06 - Business Goals

_Read by: all agents. This file is the single source of truth for what "success" means for ProSoccer SEO. Every recommendation in every deliverable must tie back to a goal listed here. No goal listed, no work done. Reviewed and owned with Tony. Updated quarterly or when commercial priorities shift._

## The Commercial Objective

**Reduce ProSoccer's Google Ads spend dependency and grow online revenue by building compounding organic channels that keep returning value without monthly paid spend to keep them alive.**

Paid ads charge for every click, every month, forever. Organic search assets (well-structured collection pages, technically healthy product listings, content that ranks and gets cited) are built once and keep earning. The goal isn't to kill the ads program. It's to shift the mix, so that a larger share of online revenue comes from channels ProSoccer owns rather than channels ProSoccer rents.

Every goal below exists to serve this commercial outcome. If a proposed piece of SEO work doesn't clearly shift the organic-vs-paid mix or grow compounding organic revenue, it doesn't belong in the plan.

## Why This, Why Now

7 Rock re-engaged with ProSoccer in February 2026. Discovery ran through April. Execution begins late April 2026 with the AI specialist workforce coming online.

Q1 2026 averaged roughly 54 orders/day across all in-scope sales channels (Online Store, Shop, Tapcart, BSS B2B, Redo, and other web channels; excludes Point of Sale, Channable marketplaces, and Draft Orders). Google organic was the single largest referral source on the web channels, contributing approximately 2,397 orders and $225K in Q1 2026 alone. That's both an asset and a risk. It's an asset because the channel is already carrying the single largest share of web orders. It's a risk because two outside forces are about to hit it at the same time: Google's AI Overviews are already compressing click-through rates on shopping queries, and the FIFA World Cup opens in LA on June 12, 2026. One compresses, one inflates. Both demand a response.

For context: the 2024 full year averaged roughly 57 orders/day on the same scope. Q1 2026 tracks slightly below that pace. That delta has a long backstory we aren't going to relitigate here. What matters now is the forward plan.

## What we found

This section captures what showed up when 7 Rock actually looked at the site and the Search Console data over the past two weeks. Findings from Phase 2 discovery, not hypotheses.

**The ranking trajectory is improving.** Average Google position has moved from 20.8 to 9.6 over the past 12 months (weekly GSC data, April 2025 to April 2026). That's not a plateau or a decline. The site is trending up.

**The late-2025 theme migration caused a temporary regression.** Between November 2025 and January 2026, average position slipped 3 to 4 spots, a standard post-theme-swap re-indexing effect. Rankings have since recovered to pre-migration levels across February to April 2026. The recovery coincides with 7 Rock's re-engagement in February, but we haven't shipped any implementation work yet, so natural recovery from the theme damage is the more likely driver. We're not claiming credit for the recovery. What matters for planning is that Month 1 work starts from a recovered position, not a falling one.

**Magento legacy is clean.** A scan of the 12-month GSC top-pages export for `.html`, `?id=`, `/catalog/product`, `/index.php`, and other Magento patterns returned zero matches. No legacy URLs from the 2021 to 2022 Shopify migration are receiving traffic today. That cleanup held up. No follow-up action needed.

**USMNT keyword cannibalization is a newly surfaced technical issue.** Three overlapping US collection URLs (`/collections/united-states-men`, `/collections/united-states-men-women`, and `/collections/united-states-women`) are splitting link equity across the same product set. USMNT currently sits at position 46 despite a 79,559-impression pool in GSC. Canonical URL consolidation, with 301s from the non-canonical variants into one canonical, is a high-priority Month 1 technical fix and a prerequisite for any USMNT on-page sprint work.

**National team pages aren't a single cohort. They're three different patterns.** Four pages already rank in striking distance of page 1: Guatemala 9.4, El Salvador 10.8, South Korea 12.6, and Italy 14.0. Two pages rank near page 1 despite broken or empty metadata (default Shopify titles, empty meta descriptions): El Salvador 10.8 and Honduras 10.7. The metadata fixes alone are the lowest-effort, highest-return work in the sprint. Two pages need heavier intervention than polish: Mexico at 28.4 and USMNT at 45.8. That's why Goal 2 below splits into three layers rather than treating the national team set as a uniform task.

## The 12 months in three phases

**Recover (late April to July 2026).** World Cup sprint execution, USMNT URL consolidation, fast-polish and quick-win national team pages, DataFeedWatch feed audit, Agentic Storefront audit, manual AI citation baseline. Scope is narrow and sprint-shaped. First monthly report lands end of May 2026 as the execution era's first formal deliverable.

**Stabilize (August to December 2026).** Post-World Cup normalization. Tier-B national team pages, to be confirmed by Keyword Research Agent output, enter Goal 1 rotation as compounding assets. Product schema, review schema, and Merchant Listings defense continue. Q4 holiday positioning.

**Grow (January to April 2027).** Compounding categories (club jerseys, goalkeeper, futsal, youth) lead the workstream mix. AI search visibility tool decision revisited against the manual tracking data. Quarterly re-plan against Q1 2027 results.

## Primary Goals (12 months)

These four goals are the how. Each one serves the commercial objective. Each one is measurable and has a specific owner inside the SEO workforce.

### Goal 1: Grow non-branded organic revenue

**The opportunity.** Approximately 3.7M non-branded impressions on queries where ProSoccer already ranks between positions 11 and 30 (pages 2 and 3 of Google). These rankings are in hand. They just don't click yet because they aren't on page 1. Moving a material share of those into the top 10 is the single largest organic lift available to us.

**Target category hypotheses (to be validated in Month 1).** Based on current GSC data and catalog knowledge, these are the categories we expect to prioritize. The final priority order will be set by the Category Priority Matrix (see below), not locked in here.

- **Club team jerseys** (compounding, year-round): Real Madrid, Barcelona, Manchester City, Liverpool, Juventus, Bayern Munich, Paris Saint-Germain, plus MLS clubs with LA relevance (LA Galaxy, LAFC, Inter Miami). Unlike national team jerseys, club kits sell year-round and get refreshed annually on predictable release calendars, which makes them compounding organic assets.
- **Goalkeeper gloves and keeper cleats.** We have real expertise; most competitors don't.
- **Futsal and indoor shoes.** Already ranking (best-futsal-shoes blog pulls 2,227 clicks), with clear GSC upside.
- **Youth cleats and sizing content.** Soccer-mom avatar demand, low competition for honest content.
- **National team jerseys** with LA-area diaspora demand: Mexico, El Salvador, Guatemala, South Korea, Italy, USMNT. Higher priority inside the World Cup sprint (Goal 2); year-round priority below club jerseys.
- **Position-specific cleat content** (defender, striker, midfielder, wide-feet): existing blog posts are already pulling clicks and have room to move up.

**Month 1 deliverable: the Category Priority Matrix.** The final priority order will come out of a matrix built by intersecting three data sets:

1. **Historical sales data** from Shopify (what actually produces revenue)
2. **GSC query and impression data** (what people search for, especially at positions 11 to 30)
3. **Seasonality patterns** (when each category peaks)

The Keyword Research Agent (scheduled for build in the next workforce phase) will own the matrix once live. Until then, the Master Strategist builds the first version.

**Seasonal context that feeds the matrix.** Soccer retail has real seasonality. Spring is club-season start and the spring restock window. Summer is camps, youth club buying, and tournaments. Fall is back-to-school and new-season gear drops. Winter is indoor play and holiday gifting. Nike, Adidas, and Puma cleat releases run on predictable cycles that the category matrix will factor in (typically a major drop every 9 to 12 months per brand, plus limited-edition "packs" tied to the UEFA and World Cup calendar). National team jerseys spike around tournaments; club jerseys release on annual calendars. All of this shapes which categories we attack first, and when.

**Why this is the lead goal.** Branded queries (prosoccer, pro soccer, pro soccer pasadena) already rank at positions 1 to 3 with strong click-through rates. That traffic is healthy and stable. Growth has to come from non-branded. Non-branded is also the traffic that most directly reduces ads dependency, because it brings in customers who weren't already searching for our name.

### Goal 2: Capture World Cup 2026 traffic

**Scope.** A narrow, 8-week content and optimization sprint tied to the FIFA World Cup (June 11 to July 19, 2026). The US hosts 78 of the 104 matches. The opener is at LA Stadium on June 12, 2026, which sits directly inside ProSoccer's home market.

**What we'll do.** Based on the Phase 2 discovery findings (see "What we found" above), the national team collection pages fall into three layers. Each layer has a different workload inside the sprint.

**Layer 1, fast polish (4 pages).** Guatemala (position 9.4), Italy (14.0), South Korea (12.6), and El Salvador (10.8). Standard on-page optimization: title rewrites, meta description updates, H1 polish, intro copy that earns the click. El Salvador's broken-metadata fix is a low-effort pre-step inside this page's optimization pass, not a separate workstream. These four represent the highest-probability page-1 gains available inside the 8-week window.

**Layer 2, heavy lift (2 pages).** Mexico (currently at position 28.4) needs an on-page rewrite plus internal linking support, not polish. USMNT (position 45.8) requires canonical URL consolidation across the three overlapping US collection URLs (see "What we found" above) before any on-page work will pay off. The consolidation is a Technical SEO task and a hard prerequisite for the USMNT content sprint. Mexico carries the bigger opportunity on paper (119,131 GSC impressions vs. USMNT's 79,559) and the LA Mexican diaspora strength; expect measurable progress inside the sprint, not full recovery.

**Layer 3, quick win (1 page).** Honduras currently ranks at position 10.7 with empty metadata and only 6 products in the collection, and still pulls a 1.15% click-through rate from a small impression pool. Writing a proper title and meta description is the entire scope. Lowest-effort, highest-return item on the sprint board.

**Plus two non-country pieces, previously scoped.** One local "where to watch in LA" guide tied to the Pasadena store. One authenticity guide ("how to spot a real vs. replica vs. fake jersey") that converts casual fans.

**One pending follow-up that may reshuffle Layer 1 priority.** Which countries actually play matches at LA Stadium (SoFi) during the tournament is not yet confirmed. Once FIFA publishes the venue-by-venue match schedule, we'll re-check Layer 1 against the LA-hosted countries and may promote or swap pages based on which national teams are actively competing in ProSoccer's home market.

**What we won't do.** We aren't chasing generic "World Cup 2026" queries. FIFA.com, Fox Sports, and ESPN will take that traffic and we'll lose. We stay narrow and close to the catalog.

**Why now.** Search interest around World Cups peaks during match weeks. Standard SEO lead time for events like this is 6 to 12 months. We have 8 weeks. That constrains scope but doesn't eliminate the opportunity: the pages we need are already ranking, they just need work to convert the surge.

### Goal 3: Defend organic revenue against AI Overview click erosion

**What's happening.** Google now shows AI-generated answer summaries (AI Overviews) above traditional search results on a growing share of queries. As of Q1 2026, roughly 14% of shopping queries trigger an AI Overview, up from near zero six months ago (Search Engine Land / Visibility Labs). When an AI Overview appears, the top organic result loses 18 to 39% of its clicks, because users get the answer from the summary and don't click through.

**What we see in our own data.** Weekly impressions roughly doubled between January and March 2026 (about 330,000/week to 700,000+/week). Clicks barely moved. That's the AI Overview pattern: impressions go up, clicks stay flat, click-through rate compresses. Reporting "impressions doubled" as good news would mislead Tony.

**The defensible surface.** Not all Google search surfaces are equally affected. In our data, Google's "Merchant Listings" surface (the shopping results in search) generates a 6.33% click-through rate at position 4.69. Google's "Product snippets" surface generates 0.53% at position 21.4. Merchant Listings are roughly 12 times more click-efficient per impression. The response to AI Overview pressure is to get more of the ProSoccer catalog into Merchant Listings, cleanly.

**The named workstream: Merchant Center Feed Optimization (via DataFeedWatch).** 7 Rock manages ProSoccer's product data feed through DataFeedWatch, which pushes to Google Merchant Center. Every product title, attribute, image, description, GTIN, availability signal, and review integration in that feed is a lever on Merchant Listings performance. This is likely the fastest-win lever on the entire engagement because feed improvements produce measurable Merchant Listings lift within weeks, not quarters.

Month 1 and Month 2 deliverables inside this workstream:

- Full audit of the DataFeedWatch to Merchant Center feed health.
- Identify products with feed quality issues: missing GTINs, weak titles, low-quality or missing images, stale prices, inaccurate availability, missing variant data.
- Implement structured product data (Product schema) and review schema on the ProSoccer theme to match the feed.
- Flag any Merchant Center account warnings or product disapprovals. Surface to Mike for prioritization.
- Baseline current Merchant Listings click share vs. organic Product Snippets click share, then track monthly.

**Why this is defensive, not offensive.** Goal 1 is offense (grow new traffic). Goal 3 is defense (don't lose the traffic we have). Both matter. The AI Overview trend is accelerating; we can't let a Q3 2026 report show "impressions surged, revenue flat" without a planned answer.

### Goal 4: Establish AI search visibility baseline

**What's happening.** AI search engines (ChatGPT, Perplexity, Gemini, Copilot) now handle an estimated 12 to 18% of English informational queries. Shopify reported a 15x increase in AI-originated orders across its merchant base over the past 12 months at the Merchant Partnership Expo (February 2026). ChatGPT is already referring real, paying customers to prosoccer.com: Q1 2026 saw 9 orders for roughly $1,006 (average order value around $112); Q4 2025 saw 10 orders for $1,367. Small numbers, also real, and trending with the broader shift.

**Shopify's AI features (already live, need verification).** In late March 2026, Shopify activated Agentic Storefronts for all stores as part of the Winter '26 Edition. ProSoccer's products are auto-syndicated to Google AI Mode, ChatGPT, Microsoft Copilot, and Perplexity through the Shopify Catalog by default. Direct-checkout toggles per AI channel live in Admin > Settings > Sales Channels. ChatGPT and Google AI Mode orders flow into Shopify admin with AI channel attribution. Perplexity orders go through PayPal and do NOT flow into Shopify admin, so they're invisible to our current referrer reporting.

**What we'll do in Month 1.**

- Audit ProSoccer's Shopify admin for Agentic Storefront status. Confirm which AI channels are enabled (Google AI Mode, ChatGPT, Copilot, Perplexity). Recommend toggles to Mike based on findings.
- Verify store policies (shipping, returns, authenticity claims) are accurate in the Shopify admin, because AI platforms surface these directly.
- Audit product attribute completeness (GTIN, dimensions, materials, variants) because AI platforms match on structured data, not images.
- Build a manual citation tracking sheet for ~20 target prompts across ChatGPT, Perplexity, and Gemini (examples: "where to buy authentic Mexico national team jersey," "best goalkeeper gloves 2026," "soccer store pasadena"). Run weekly. Log presence, position, and whether ProSoccer is cited or linked.

**The AI visibility tools landscape, for context.** We're not buying any of these yet, but Tony and Mike should know what category we mean when we say "AI visibility tool":

- **Profound** ($79 to $299/month). Brand mention and citation tracking across ChatGPT, Perplexity, Gemini.
- **Otterly** ($79 to $199/month). LLM citation tracking, prompt monitoring.
- **Peec.ai** (~$99 to $299/month). AI search visibility monitoring.
- **Ahrefs Brand Radar.** Native inside Ahrefs, useful only if ProSoccer subscribes to Ahrefs.
- **Semrush AI Toolkit.** Native inside Semrush, same caveat.

**The recommendation stays: don't buy yet.** Manual tracking for 90 days establishes which prompts and categories matter. Revisit the tool decision at end of Q3 2026 once we have data.

**Why this goal matters.** We can't report on what we don't measure. If AI search referrals grow from 10 orders/quarter to 100 orders/quarter over the next year, we want to see that curve, not miss it. And Shopify's built-in AI integrations may already be sending traffic we're not attributing correctly.

## Late April to May 2026: execution start

Phase 2 discovery (April 2026) answered most of the diagnostic questions we set at the start of this engagement. We no longer need a Month 1 investigation to tell us whether the traffic problem is real; we need Month 1 execution to act on what we already know. Here's what the data says.

**Traffic trajectory: improving.** Average Google position has moved from 20.8 to 9.6 over the past 12 months. Clicks grew approximately 58% in the same window. Traffic is not the problem.

**Technical integrity: clean on the legacy-URL front.** No Magento-era URLs are receiving impressions or clicks in current GSC data. The 2021 to 2022 migration cleanup held up.

**Theme migration impact: temporary, and resolved.** The late-2025 theme ship caused a 3-to-4 position regression across November 2025 to January 2026. Rankings have since recovered to pre-migration levels. Any residual theme-level SEO issues are now affecting the recovered baseline, meaning fixes produce lift above current position, not just a return to neutral.

**Conversion gap hypothesis: still valid.** Q1 2026 averaged roughly 54 orders per day, below what the current impression trajectory would predict. Q1 2026 Online Store orders dropped 22% versus Q4 2025 even as average position improved. The 5.5-position gap between desktop (19.4) and mobile (13.9) is a plausible contributor, possibly a rendering or template issue specific to desktop. Continued conversion diagnosis and fixes flow into the separate prosoccer-theme CRO project that 7 Rock already manages, not into this SEO scope. The SEO team flags conversion issues the moment the data reveals them; it doesn't own the fixes.

**New technical finding: USMNT keyword cannibalization.** Three overlapping US collection URLs are splitting link equity (see "What we found" above). Canonical consolidation enters the Month 1 technical work list as a named deliverable and a hard prerequisite for any USMNT sprint work.

**Month 1 scope, in light of these findings.** Less "diagnose," more "ship." The technical SEO Month 1 list now explicitly includes USMNT URL consolidation as a high-priority item. Any device-level conversion findings continue to flow to the CRO project via Mike's `mike-audit` branch in the theme repo. The diagnostic is closed as a discrete discovery workstream; what it produced now lives inside Goal 1, Goal 2, and Goal 3 execution.

## The Outcomes We'll Measure

These are the four metrics that lead every monthly report to Tony. Secondary metrics (tracked below) are included for health monitoring; they aren't the lead.

### Primary commercial outcomes

| Metric | Current baseline | 12-month target | Source |
|---|---|---|---|
| Online orders/day (average, in-scope channels) | ~54 | 75 to 85 | Shopify; excludes POS, Channable, Draft Orders |
| Google organic revenue (rolling 12 months, in-scope channels) | ~$950K | $1.2M+ | Shopify "search/google" referrer |
| Google Ads monthly spend reduction | $30K/month baseline | $5K to $8K/month saved (17% to 27%) | Tony's Ads account |
| High-order days per year (90+ orders/day) | ~8 | 50+ | Shopify, in-scope channels |

**About the 75 to 85/day target.** Q1 2026 averaged roughly 54 orders/day. 75/day is the defensible floor we expect to hit, a 39% lift that the 3.7M non-branded impression pool, the World Cup sprint, and Merchant Listings defense should deliver when executed well. 85/day is the stretch. For context, 85/day annualizes to roughly 31,000 in-scope orders, which would exceed ProSoccer's 2024 full-year total, so we're naming it as ambition rather than commitment. Compounding organic channels scale non-linearly once the technical foundation is right and content starts ranking, which makes the stretch credible; it isn't guaranteed. Any conversion-rate fixes delivered through the separate prosoccer-theme CRO project would add upside on top of the range.

**About the $950K to $1.2M revenue target.** $950K is a working estimate based on Q4 2025 plus Q1 2026 "search/google" referrer data annualized, with a conservative adjustment for the Q4 holiday lift. We'll refine the baseline once we have a full trailing 12 months of referrer data (June 2026). The $1.2M target reflects a 26% lift on a conservative baseline.

**About the "150 orders/day" number.** If that figure has come up in conversations, treat it as a 24 to 36 month destination, not a 12-month commitment. Compounding gains in SEO get easier as the foundation matures, so year two and year three typically grow faster than year one. We're not scoping for 150/day this year.

### Secondary SEO metrics reported monthly

These are activity and health metrics, not commercial outcomes. Both layers matter. Commercial outcomes answer "is the business growing?" Secondary metrics answer "is the SEO program healthy?" Tony and Jorge see both in every monthly report.

- **Keyword rankings.** Priority set of 50 to 100 commercial keywords tracked weekly.
- **Organic sessions and organic conversion rate.** GA4, month over month.
- **Indexed pages and technical health status.** Screaming Frog crawl, quarterly.
- **Core Web Vitals scores.** Mobile and desktop, tracked monthly via PageSpeed Insights.
- **Backlink profile changes.** Via whatever tool gets approved; Ahrefs is the preferred default.
- **Merchant Listings click share vs. organic click share.** Google Search Console Search Appearance data, monthly.
- **AI search citation count.** From the manual tracking sheet built in Goal 4.

## What We Will Not Do

Keep this list short. Reference it whenever scope creep shows up.

- No generic "sports store" or "athletic gear" optimization. ProSoccer is soccer-specific; pretending otherwise dilutes everything.
- No bottom-of-funnel discount queries that erode margin ("soccer cleats under $30" and similar).
- No local SEO in markets where ProSoccer has no storefront and no service coverage.
- No generic World Cup content where we'll lose to FIFA.com and major sports media. Specific national team pages, specific LA viewing content, and authenticity content inside the catalog context are all in scope.
- No content published without a clear tie to a goal on this page.
- No replacing Google Ads. The plan reduces its share of the revenue mix; it doesn't kill the program.

## Approval Authority

### 7 Rock side

- Mike approves all agent actions, all drafts, and all scope changes.
- Mike approves blog topics and outlines before drafting begins.
- Angela publishes finalized blog articles to the Shopify blog. Tony and Jorge do not need to approve individual articles after the topic and outline have passed Mike's review.

### Client side

- Tony approves strategy changes, goal adjustments, and budget changes.
- Tony is the final approver on any paid tool purchase, regardless of monthly cost. All tool adds require Tony's knowledge and sign-off.
- **New collection pages:** Tony's internal team creates the page. Jorge finalizes with 7 Rock SEO input before launch.
- **Existing product pages:** Tony's internal team maintains these using the 7 Rock best-practice guide for titles, short descriptions, and long descriptions. 7 Rock optimizes PDPs post-launch as part of ongoing work.
- No strategy documents or monthly reports leave Mike's queue without Mike's explicit approval first.

## Review Cadence

- **Weekly:** Mike reads `work-log/` and flags blockers.
- **Monthly:** Client report delivered to Tony and Jorge from `reports/monthly/`. Leads with the four commercial outcome metrics above; secondary metrics follow.
- **Quarterly:** Strategy review. Update `strategy/master-strategy.md`. Re-confirm or adjust the 12-month targets on this page.

## Open Questions for Tony

### Starting assumptions (confirmed with Mike)

These are the inputs that anchor every target and metric above. If anything has changed since we last aligned, tell us now so we can recalibrate.

- **Google Ads monthly spend baseline:** $30,000/month total, all campaigns.
- **Order volume scope:** all sales channels included EXCEPT Point of Sale, Channable (Amazon/eBay), and Draft Orders. Online Store, Shop, Tapcart, BSS B2B, Redo, and other web-based channels are all counted.
- **High-order day threshold:** 90+ orders per day (using the scope above).
- **Paid tool approval:** always requires Tony's knowledge and sign-off, regardless of dollar amount.
- **Affiliate program operation:** 7 Rock manages ProSoccer's affiliate program on AWIN (Affiliate Window) and uses PayAudit as the pre-AWIN transaction approval system. Any backlink audit or disavow recommendation cross-references both rosters before action.

### Still open (needs Tony's input at kickoff)

1. **Attribution model confirmation.** Our baselines use Shopify's "search/google" referrer as the organic signal. Do you track organic revenue under a specific attribution model we should align with (last-click, assisted, post-view), or should we additionally pull GA4 Organic Search data to triangulate?

2. **World Cup sprint approval model.** We'll ship 7 to 9 new or refreshed pieces inside the 8-week sprint (7 national team pages across the three layers described in Goal 2, plus 1 LA watch guide and 1 authenticity guide). Given the timeline, we'd like to run weekly batch approvals rather than page-by-page sign-off. Does that work for you?

3. **Cadence confirmation.** Monthly reports starting end of May 2026, delivered from `reports/monthly/`. Any format or medium preferences? PDF, Google Doc, live walkthrough?

---

**Next step:** Mike reviews this draft end-to-end. Any changes happen before this goes to Tony. Nothing client-facing leaves the repo without Mike's explicit written approval.
