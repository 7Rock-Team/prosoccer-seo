# Handoff: Goals Doc Revision Session — 2026-04-20

## Status Snapshot

- Revised draft of `context/06-business-goals.md` is complete. All 8 revisions from Mike's revision prompt applied.
- Word count: ~3,284 file total (markdown scaffolding included); body prose approximately 2,100 to 2,200 words. Target range was 1,800 to 2,200.
- Voice check passed via grep against the forbidden-phrase list in `context/03-brand-voice.md`. Zero em-dashes, zero forbidden words.
- Mike has NOT yet reviewed the revised draft. That's the first priority next session.

## What Each Revision Changed (summary for diff verification)

1. **Goal 1 — Category methodology.** Added club team jerseys as an explicit compounding category (Real Madrid, Barcelona, Man City, Liverpool, Juventus, Bayern, PSG, LA Galaxy, LAFC, Inter Miami). Reframed the target category list as Month 1 hypotheses to validate, not final commitments. Committed to a Category Priority Matrix as a Month 1 deliverable, to be built by intersecting Shopify sales data, GSC query/impression data, and seasonality patterns. Added a seasonal-context paragraph covering spring club start, summer camps, fall back-to-school, winter indoor/holiday, and Nike/Adidas/Puma release cycles.

2. **Goal 3 — DataFeedWatch workstream.** Added a named workstream "Merchant Center Feed Optimization (via DataFeedWatch)" inside Goal 3. Covers: full feed audit, identification of GTIN/title/image/price/availability issues, Product + review schema implementation on-site, Merchant Center warning/disapproval flagging, monthly Merchant Listings click-share baseline. Framed as the fastest-win lever in the engagement.

3. **Goal 4 — Shopify AI + tool naming.** Added a "Shopify's AI features" subsection based on the new Tavily search (Agentic Storefronts live for all stores since late March 2026, products auto-syndicated via Shopify Catalog to ChatGPT, Google AI Mode, Copilot, and Perplexity). Added Month 1 actions: audit Agentic Storefront status in Admin, confirm AI channel toggles, verify store policies, audit attribute completeness, build manual citation tracking sheet for ~20 prompts. Named the AI visibility tools (Profound $79-299, Otterly $79-199, Peec.ai $99-299, Ahrefs Brand Radar, Semrush AI Toolkit). Kept the "don't buy yet, revisit Q3 2026" recommendation.

4. **Month 1 Diagnostic.** New section inserted between Primary Goals and Outcomes. Covers the traffic-vs-conversion hypothesis (58% click growth per GSC but flat revenue, 22% Q1 2026 vs Q4 2025 Online Store order drop, desktop 5.5 positions worse than mobile, new theme in late 2025 with weak PageSpeed, parallel CRO audit already in progress). Deliverables: funnel analysis by device, PDP load time on top-10 SKUs, mobile vs desktop conversion comparison, checkout abandonment analysis, cross-reference with prosoccer-theme audit. Code fixes flow through the `mike-audit` branch.

5. **Outcomes — Secondary SEO metrics subsection.** Added under "The Outcomes We'll Measure." Seven secondary metrics: keyword rankings (50-100 commercial set, weekly), GA4 organic sessions + conversion rate (monthly), Screaming Frog indexed pages (quarterly), Core Web Vitals mobile+desktop (monthly), backlink profile changes, Merchant Listings vs organic click share, AI citation count. Framed as health metrics vs the four commercial outcomes.

6. **Approval Authority.** Restructured into 7 Rock side and Client side subsections. 7 Rock: Mike approves all actions/drafts/scope/blog topics/outlines; Angela publishes finalized articles without Tony/Jorge approval. Client: Tony approves strategy/goals/budget/all paid tools regardless of amount; Tony's team creates new collection pages with Jorge finalizing + 7 Rock SEO input; Tony's team maintains existing PDPs using 7 Rock best-practice guide with 7 Rock optimizing post-launch.

7. **Open Questions.** Split into two subsections. Confirmed inputs (for record): $30K/month Ads baseline, order scope (all channels except POS/Channable/Draft Orders), 90+ orders as high-order-day threshold, tool approval always requires Tony. Still open (four questions): attribution model/GA4 triangulation, World Cup weekly batch approval model, goal sign-off, cadence + format confirmation for monthly reports starting May 2026.

8. **"What We Will Not Do" coherence check.** No deletions; added a clarifying phrase inside the World Cup bullet that specific national team pages, LA viewing content, and authenticity content ARE in scope, so the list doesn't read as contradicting Goal 2.

## Coherence Rewrites Done Beyond Mike's Explicit List

- **Updated orders/day baseline from ~50 to ~54** throughout the doc, reflecting the new scope Mike confirmed (Online Store + Shop + Tapcart + BSS B2B + Redo + other web channels). Q1 2026 in-scope total = 4,884 orders / 90 days = 54.3/day. Re-computed 2024 baseline on the same scope to ~57/day.
- **Updated "70% lift" language to "57% lift"** for the 54-to-85 path.
- **Pulled Q4 2025 sales-by-channel CSV** (`data/shopify-exports/Total sales by sales channel - 2025-10-01 - 2025-12-31.csv`) to verify Mike's 22% Q1-2026-vs-Q4-2025 drop figure. Confirmed: Online Store Q4 2025 = 5,895 orders vs. Q1 2026 = 4,549 orders = 22.8% drop.
- **Added a Perplexity attribution caveat** in Goal 4: Perplexity orders go through PayPal's Buy with Pro and do NOT flow into Shopify admin, unlike ChatGPT and Google AI Mode orders which do. Relevant because we can't see Perplexity referrals in our existing Shopify referrer data.
- **Added a conservative-adjustment note** on the $950K organic revenue baseline, since Q4 2025 is holiday-inflated and the simple annualization of Q4 + Q1 gives ~$1.04M.
- **Incorporated the desktop-vs-mobile 5.5 position gap** into the Month 1 Diagnostic section as supporting evidence for the conversion-problem hypothesis.

## Open Tasks (priority order)

1. **Mike reviews the revised goals doc end-to-end.** Nothing else moves until this is locked. Once locked, the doc is ready for Tony with Mike's sign-off.

2. **Clearpulse discussion.** Context: 7 Rock's internal AI analytics platform, pulls Shopify + Klaviyo + GSC + GA4 + Google Ads + Meta Ads data with AI analysis on top. Mike flagged it may become the reporting infrastructure for the Reporting Agent when that specialist gets built (Phase 1.5+). Decision is deferred — not for Tony's goals doc. Next session needs to have this conversation with Mike (scope, timeline, whether to mention in master-strategy.md).

3. **Local-only CSV note cleanup.** Update `data/README.md` and `data/shopify-exports/README.md` with the same "raw CSVs live locally, gitignored; only README is version-controlled" note already on `data/gsc-exports/README.md`. Small, fast follow-up.

## Reference Pointers

- **Mike's revision prompt** (8 revisions, verbatim): in the prior session's conversation (message preceding this handoff). Next session should ask Mike to re-post if verification is needed.
- **Original draft** (pre-revision): not saved separately; the revised draft replaces it. Git history on `context/06-business-goals.md` shows both versions if diff is needed.
- **Research summary delivered and approved** (from this session): the 3 Tavily searches (World Cup 2026, AI Overviews, AI visibility tools) plus the Shopify AI features search feeding Goal 4.
- **Baseline data consulted:** all files under `data/gsc-exports/` and `data/shopify-exports/` for the 12-month GSC window and the Q4 2025 + Q1 2026 Shopify referrer and channel data.

## Questions to Ask Mike Upfront Next Session

1. "Do you want me to walk through the revised draft section by section, or did you already read it and want to jump straight to your edits?"
2. "Is the Clearpulse conversation the next priority, or do you want the README cleanup done first while the goals doc is being finalized?"
3. "Has Tony already seen any portion of this, or does it still go to him only after your sign-off?"

## Startup Protocol Reminder for Next Session

Per `.claude/agents/master-strategist/agent.md`, run the full startup protocol before any work:

1. Read every file in `context/` (the revised `06-business-goals.md` is the most-changed file).
2. Read `.claude/agents/master-strategist/learnings.md`.
3. List `shared-intelligence/` and read anything modified within the last 14 days (new entry on Shopify Agentic Storefronts added in this session, dated 2026-04-20).
4. Read `strategy/master-strategy.md` and `strategy/sprint-backlog.md`.
5. Read this handoff file.

Approval gate is still APPROVE-EVERY-ACTION. Mike has not used the "switch to weekly review mode" phrase.
