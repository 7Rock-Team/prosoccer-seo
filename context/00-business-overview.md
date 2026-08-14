# 00 - Business Overview

This file captures the durable strategic frame for ProSoccer.com. It defines positioning, business model, history that matters for SEO interpretation, operational facts, and strategic targets that shape every agent's work. Static content lives here; current operational numbers (revenue, AOV, conversion, inventory snapshots) live in data/ folder exports and are read fresh each session.

Every agent reads this file at startup. This is the first context file any agent reads. Keep it current.

Source: 7 Rock Marketing strategic synthesis from ProSoccer engagement, last updated 2026-04-25.

---

## Identity and Positioning

**ProSoccer is The High-Performance Expert in US soccer retail.**

This positioning is binding for all agent work. ProSoccer chooses NOT to compete on:

- Logistics scale (Amazon owns this)
- Volume and breadth (Soccer.com owns this)
- Convenience for casual buyers (Dick's Sporting Goods owns this)
- Cultural street credibility in the LA Hispanic market (Niky's Sports owns this)

ProSoccer competes and wins on:

- Specialized expertise (Elite-tier inventory, technical depth, authentic gear)
- Solving specific problems (wide feet, growth spurts, turf safety, cleat care)
- Speed and agility (next-day shipping from Irwindale, CA)
- Authentic curation over algorithmic recommendation
- 30-year history as the original soccer specialist in Pasadena

When parents are scared about injury, when serious players need the specific elite boot Dick's doesn't carry, when fans need authentic merch they can trust, ProSoccer is the answer. This is the wedge.

---

## Company Snapshot

- **Company name:** ProSoccer
- **Primary domain:** prosoccer.com
- **Founded:** Approximately 30+ years of operation (Pasadena history)
- **Headquarters:** Pasadena, CA
- **Additional locations:** Irwindale, CA (warehouse with next-day shipping capability)
- **Retail storefronts:** Pasadena and Irwindale
- **Ownership:** Private (Tatikian family)

---

## What They Sell

Top product categories in approximate revenue order. Categories marked with (S) are seasonal.

- Cleats and boots (footwear is the largest revenue category)
- Apparel (jerseys, kits, training apparel)
- Equipment (balls, training gear, accessories)
- Goalkeeper gear (gloves, specialized apparel)
- National team jerseys and country-specific gear
- Training equipment (cones, ladders, balls)
- Referee gear
- Club team fulfillment (S)
- Youth and back-to-school gear (S)

Note: Refer to data/shopify-exports/sales-by-product-type.csv for current revenue distribution. The mix shifts seasonally and over time.

---

## How They Sell

ProSoccer operates as a multi-channel retailer:

- **Online:** Shopify Plus storefront at prosoccer.com (primary focus for SEO work)
- **Physical retail:** Pasadena and Irwindale, California locations
- **Mobile app:** Tapcart-powered mobile app channel
- **Wholesale and team orders:** Limited team and bulk equipment sales (the Coach avatar)

### Warehouse and Fulfillment

- **Primary warehouse:** Irwindale, California
- **Capability:** Next-day shipping in California, fast nationwide shipping
- **Strategic implication:** "Same Day Dispatch" and "Next Day Shipping" are competitive weapons against Soccer.com's slower peak-season fulfillment, especially during Back-to-School season

---

## Who Runs the Business

### Client Side

- **COO:** Tony Tatikian (primary client decision-maker for SEO strategy)
- **Product Setup:** Jorge Cotto (internal Shopify admin; implements approved SEO changes)
- **Retail store:** Lara Tatikian
- **Support tickets:** Louie (ProSoccer employee submitting issues to development)

### 7 Rock Marketing Side

- **Marketing partner and owner:** Mike Hakopyan (leads strategic engagement with Tony, oversees agent workforce; non-technical)
- **Primary external developer:** Misal (handles GitHub commits and Shopify CLI deployments)
- **Theme developer (separate repo):** Misha (GitHub access for theme work)

### Communication Patterns

- Mike communicates strategy and approves work
- Misal handles all production code deployments; Mike does not push to main or team-updates branches
- Jorge handles all Shopify admin tasks (theme editor, app configuration, content updates)
- Tony receives strategic updates and monthly reports; tactical detail goes to Jorge

---

## History That Matters for SEO

### 7 Rock Engagement Timeline

- **2021 to 2022:** 7 Rock Marketing (Mike Hakopyan) took on ProSoccer as a marketing partner and executed the Magento to Shopify Plus platform migration. All migration-era URL mapping, redirects, and schema work originated with 7 Rock.
- **2023 to 2024:** 7 Rock continued as marketing partner through this period.
- **2025:** Another agency managed the account. Late 2025, that agency completed a Shopify theme migration to the current theme (separate from the 2021 to 2022 platform migration).
- **February 2026:** ProSoccer returned to 7 Rock.
- **January 2026 (pre-return):** At the client's request, 7 Rock's whitelabel team produced a full SEO audit as a pre-engagement diagnostic. It was never scoped to include implementation. It is 7 Rock's own team's work, not a previous agency deliverable.

### What This Means for SEO Decisions

- Legacy URL issues flagged in the January 2026 audit that trace back to the 2021 to 2022 Magento to Shopify Plus migration are 7 Rock's own legacy to clean up, and that cleanup should be verified rather than re-scoped.
- Technical regressions that surfaced after the late 2025 theme migration are a separate investigation. That theme work was the other agency's, and any related damage (Core Web Vitals, internal linking, structured data, template-level SEO elements) needs its own diff against the pre-theme-migration state.
- Ranking declines visible in the 24-month trend data should be interpreted with the 2025 management gap and late-2025 theme change as two distinct candidate causes, not one.

### Recent Operating Context

#### Theme Migration (Late 2025)

ProSoccer migrated its Shopify theme in November 2025 (executed by the previous agency). The migration coincided with a regression in SEO performance (avg position dropped from approximately 9 to 20+) and revenue declines through January 2026. Recovery was largely complete by February to April 2026, with avg position improving back to approximately 9.6.

Strategic implication: The theme migration period is a known artifact in historical data. Comparisons that span this window need to acknowledge the regression-and-recovery pattern. Phase 2 discovery surfaced specific orphan pages and broken patterns from this migration that still need remediation (see deliverables/phase-2-discovery/).

#### Meta Ads Blackout (Late 2025)

ProSoccer's Meta Ads account was disabled for approximately 60 days in late 2025, removing top-of-funnel paid traffic. This compounded the theme migration impact on revenue. Restored as of early 2026.

Strategic implication: 2025 baseline traffic and revenue data is not directly comparable to 2026 forward. Use 2024 full-year as the cleaner baseline when possible.

---

## Strategic Targets

These are the durable strategic targets that shape priority decisions. Current actuals come from data/ folder exports, not from this file.

### Average Order Value (AOV)

- **Strategic target:** $120
- **Why it matters:** With approximately 40% gross margins, AOV below $120 leaves very little room for ad spend (CPA) and limits paid acquisition profitability. Bundle recommendations, cross-sells, and upsells that raise AOV are strategically valuable.
- **Current AOV:** Read from data/shopify-exports/ for current state.

### Conversion Rate

- **Strategic target:** 3.0%
- **Why it matters:** Current rate well below target indicates UX, trust, or product-page friction. Improving conversion rate has greater impact than driving more traffic to a leaky funnel.
- **Current rate:** Read from Shopify Analytics for current state.

### Revenue Growth

- **Posture:** Quarter-over-quarter and year-over-year organic revenue growth.
- **Current revenue:** Read from data/shopify-exports/sales-by-month.csv for trailing 12-month picture.

---

## Brand Mix and Margin Structure

Approximate gross margins by major brand (relatively stable; updated when supplier contracts change):

- **adidas:** 43.3%
- **Nike:** 39.5%
- **Joma:** 37.2%

Higher-margin brands (adidas, smaller specialty brands) are more profitable to drive traffic toward. Lower-margin brands (Nike) require more volume to generate equivalent profit. Agents should consider margin context when evaluating priority categories.

---

## Owned Media Assets

ProSoccer maintains substantial owned media that informs cross-channel strategy. SEO is one channel among several; insights from organic traffic should inform email, SMS, and social efforts where natural cross-pollination exists.

### Email (Klaviyo)

- Active subscriber list maintained
- Significant suppressed list represents win-back opportunity
- Out of SEO scope for execution; relevant for context only

### SMS

- Combined online and local subscriber base
- Out of SEO scope for execution; relevant for context only

### Social

- **Instagram:** Largest platform for ProSoccer; strong visual product showcase fit
- **Facebook:** Smaller but stable
- **TikTok:** Underutilized given the Tyler (Athlete) avatar's heavy use of the platform; potential growth area

Current subscriber and follower counts are operational data; they shift continuously. Read from platform analytics when current state is needed.

---

## Current Pain Points (As Tony and Jorge Describe Them)

Add direct quotes here as they emerge from client conversations. If quotes are not yet captured, summarize what was heard in the most recent conversation.

(This section to be populated as ongoing client communication surfaces specific pain points.)

---

## Competitive Position

ProSoccer sits as a specialty soccer retailer competing in a crowded US market. The dominant player is Soccer.com (broad volume and aggressive discounting). Other authority competitors per January 2026 audit Trust Flow data include SoccerPost, WeGotSoccer, SoccerVillage, SoccerZoneUSA, WorldSoccerShop, PeleSoccer, and SoccerWearhouse. Local Hispanic-market threat in LA is Niky's Sports. Brand-direct sites (Nike.com, adidas.com, Puma.com) are an indirect competitive layer, especially for new product drops.

ProSoccer's competitive wedge is specialized expertise, authentic curation, geographic presence in LA, and 30-year history. See context/05-competitors.md for full competitor profiles, attack strategies, and monitoring cadence (when populated).

---

## Tooling and Tech Stack

### Production Stack

- **Shopify Plus** (e-commerce platform)
- **Hyper theme** by FoxEcom (current theme)
- **GitHub** (version control; repository at 7Rock-Team/prosoccer)
- **Shopify CLI** (deployment, used by Misal)
- **Tapcart** (mobile app channel)
- **Klaviyo** (email and SMS marketing; out of SEO scope)
- **DataFeedWatch** (product feed management to Google Shopping and other channels; managed by 7 Rock)
- **Shopify Flow** (3 active flows managing pre-launch product visibility)

### App Stack

ProSoccer runs approximately 44 Shopify apps. Notable ones for SEO context:

- **Rebuy** (Smart Cart and recommendations)
- **BSS B2B** (wholesale and account-based pricing)
- **Hextom** (bulk image and product editing)
- **Shopify Search & Discovery** (predictive search and recommendations; can conflict with Rebuy)

### Workforce Stack

- **Claude Code with Cursor** (Mike's local dev environment)
- **Master Strategist agent** plus growing specialist workforce
- **Voice check enforcement** (scripts/voice_check.py)

---

## Strategic Posture for SEO Work

When agents make strategic recommendations or priority calls, they should anchor to these principles:

1. **Compete where ProSoccer can win.** Do not chase head-term keywords Soccer.com dominates. Find the niches, long-tail, and specific problems where ProSoccer's expertise is the wedge.

2. **Inventory comes first.** Do not prioritize SEO investment on collections without inventory depth to convert resulting traffic.

3. **Move aged inventory.** When the business has stuck inventory and corresponding search demand exists, SEO investment ties directly to revenue movement.

4. **Recovery is the baseline, not the win.** February to April 2026 recovery from theme migration is mostly complete. Future wins are net-new growth, not just regaining lost ground.

5. **Tony's trust is the gating constraint.** Strategic recommendations that get implemented produce results. Strategic recommendations that don't fit Tony's operational reality stay on paper. Practical wins are valuable.

6. **The four avatars define value.** Carlos, Jennifer, Tyler, and Mike the Coach each have different LTV, conversion patterns, and product affinities. Generic "soccer fans" thinking dilutes priorities. See context/04-customer-avatars.md.

7. **Local LA presence is a moat.** Pasadena and Irwindale physical locations plus warehouse proximity create geographic advantages worth defending and amplifying through local SEO and content.

8. **Two-migration framework for trend interpretation.** When reading historical data, distinguish the 2021 to 2022 Magento to Shopify Plus migration (7 Rock's own legacy) from the late 2025 theme migration (previous agency's work). Different root causes, different cleanup strategies.

---

## What This File Does NOT Contain

By design, this file does not include:

- **Current AOV, conversion rate, or revenue figures.** These are operational data that change continuously. Read from data/shopify-exports/ for current state.
- **Current inventory snapshots.** Read from shared-intelligence/inventory-state.md or data/shopify-inventory/ for current state.
- **Current subscriber or follower counts.** Read from platform analytics when needed.
- **Tactical SEO findings.** These live in shared-intelligence/seo-findings.md and deliverables/.
- **Active project status.** Tracked in deliverables/ folders and work-log/follow-ups.md.
- **Detailed competitor profiles.** See context/05-competitors.md (when populated).
- **Customer avatar detail.** See context/04-customer-avatars.md.
- **Brand voice and visual identity rules.** See context/03-brand-voice.md.

This separation prevents stale operational data from leaking into static strategic context. Static context here; current state in data/ and shared-intelligence/.
