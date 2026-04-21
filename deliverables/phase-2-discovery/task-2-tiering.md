# Phase 2 Task 2: A/B Tiered Priority Ranking

**Session date:** 2026-04-21
**Method:** Cross-reference Task 1 inventory (existing collection pages) against GSC Q1 2026 top-pages + top-queries exports (`data/gsc-exports/`). Rankings shown below are the 12-month averages from the GSC export window (April 2025 to April 2026) because Q1-only slicing requires a separate export Mike hasn't pulled; 12-month average is the closest truthful stand-in and weights heavily toward recent weeks due to the site's Feb 2026 impression surge.

## Sprint Priority A: The Committed 6 Countries

The goals doc commits Goal 2 to Mexico, El Salvador, Guatemala, South Korea, Italy, and USMNT. Reality check below.

| Country | URL | Clicks (12mo) | Impressions (12mo) | CTR | Avg Pos | Recommendation |
|---|---|---|---|---|---|---|
| Guatemala | /collections/guatemala | 652 | 99,864 | 0.65% | **9.36** | **Keep.** Top-of-page-1 already. Small on-page polish plus the Guatemala Copa Oro moment is the whole play. Title doesn't carry "World Cup 2026" (Template B), which is a small fix if we want to catch sprint-tied queries. |
| Italy | /collections/italy | 635 | 138,080 | 0.46% | **13.99** | **Keep.** Strong impression base at 138k. Already on WC2026 template. Low CTR (0.46%) is the lever — meta description mentions "La Azzurra" but page is thin on the LA Italian diaspora hook that would lift CTR. |
| South Korea | /collections/south-korea | 642 | 49,456 | **1.3%** | 12.61 | **Keep.** Best CTR of any country page at 1.3%. Thin on products (18) — adding 2026 WC kit drops as they release is the main product-side task. |
| El Salvador | /collections/el-salvador | 351 | 76,858 | 0.46% | 10.8 | **Keep, urgent fix.** Page is BROKEN (default title, empty meta description, bare H1). Already ranks page 1 despite that. A basic on-page optimization pass should yield material CTR lift. Lowest-effort, highest-lift item on this list. |
| Mexico | /collections/mexico | 156 | **119,131** | **0.13%** | **28.44** | **Keep, but reset expectations.** Phase 1 handoff claimed position 9-14. Reality is 28.44 (page 3). Impression base is huge, CTR is floor-level at 0.13%. This is a bigger project than "sprint polish" — needs content work to recover from whatever cost it the position. Worth it given the 119k impression pool and LA Mexican diaspora strength, but scope it as rebuild, not touch-up. |
| USMNT | /collections/united-states-men-women | 53 | 79,559 | **0.07%** | **45.84** | **Keep only after URL consolidation.** Three US collection URLs exist (see Task 1). Sprint work on any one of them is wasted if link equity stays split across all three. Consolidate to one canonical first (with 301s from the others), then sprint. Also true: USMNT rarely spikes during WC unless the US is winning, and Mexico / Argentina / Brazil jersey queries outearn USA queries in most WC cycles. |

**Verdict on the committed 6.** All 6 stay on the sprint list. But:

1. Three of them (Guatemala, Italy, South Korea) are "polish and publish" work — small changes, fast.
2. El Salvador is "fix the obvious bug" work — empty meta, default title.
3. Mexico is "rebuild" work — it's a bigger, slower project that may not fully deliver inside 8 weeks.
4. USMNT has a hard precondition (URL consolidation) before sprint work will pay off.

## Year-round Priority B: Other National Team Pages With Meaningful GSC Signal

Not in the committed 6, not part of the 8-week sprint, but these are the pages that should feed Goal 1 (non-branded organic growth) as compounding year-round assets. Ranked by Q1 clicks.

| Country | URL | Clicks (12mo) | Impressions (12mo) | CTR | Avg Pos | Note |
|---|---|---|---|---|---|---|
| Holland / Netherlands | /collections/holland | 393 | 127,612 | 0.31% | 10.53 | Page 1 already. Holland is the live URL; /collections/netherlands 301s in but still ranks (103 extra clicks, 19k impressions on the legacy URL). CTR is the lever. |
| Germany | /collections/germany | 266 | 114,857 | 0.23% | 18.47 | Page 2. 114k impressions, ~$76K opportunity value per the Jan audit. Strong candidate for Q3 2026 after the WC sprint wraps. |
| Colombia | /collections/colombia | 252 | 52,670 | 0.48% | 18.11 | Page 2. Solid Latin American diaspora page for LA. |
| Croatia | /collections/croatia | 156 | 24,330 | 0.64% | 18.35 | Page 2. Smaller pool but high-intent. |
| Portugal | /collections/portugal | 207 | 69,695 | 0.3% | 18.43 | Page 2. Cristiano / Seleção queries. |
| France | /collections/france | 197 | 82,546 | 0.24% | 14.66 | Page 2. |
| Spain | /collections/spain | 184 | 85,593 | 0.21% | 18.73 | Page 2. Also note `/collections/spain-jerseys-copy` leftover duplicate (flagged in Task 1). |
| Argentina | /collections/argentina | 181 | 138,797 | 0.13% | 17.56 | Page 2. 138k impressions with Messi tailwind. Likely page-2-to-page-1 candidate. |
| Brazil | /collections/brazil | 157 | 75,531 | 0.21% | 22.09 | Page 2-3. |
| Honduras | /collections/honduras | 120 | 10,465 | **1.15%** | 10.7 | **Page 1 with a BROKEN page.** Same pattern as El Salvador: empty meta, default title, only 6 products. Fix the meta and title, see what happens. |
| Chile | /collections/chile | 88 | 23,646 | 0.37% | 10.96 | Page 1. |
| Belgium | /collections/belgium | 83 | 49,840 | 0.17% | 18.35 | Page 2. |
| England | /collections/england | 79 | 53,522 | 0.15% | 22.48 | Page 2-3. |
| Austria | /collections/austria | 50 | 6,424 | **0.78%** | **8.84** | Page 1. Thin but ranks. |

**Notable non-country collections with LA-diaspora signal:**

| Collection | URL | Clicks | Impressions | CTR | Avg Pos |
|---|---|---|---|---|---|
| Lamine Yamal / Barcelona | /collections/lamine-yamal-jersey-fc-barcelona-spain | **791** | 118,981 | 0.66% | 10.38 |
| Club America | /collections/club-america | 125 | 58,165 | 0.21% | 22.75 |
| Mexico Gold Cup (De Oro) | /collections/adidas-2025-mexico-de-oro | 141 | 15,368 | 0.92% | 12.3 |

The Lamine Yamal page is the single highest-clicking country-adjacent collection on the site. Not a national team page but a player-specific one. Worth flagging as a template: similar player-spotlight collection pages for Messi (Argentina), Vinicius (Brazil), Mbappé (France) could earn similarly, especially with WC tie-ins.

## What Tier-B Work Should Look Like

Inside the 8-week sprint: Tier A only. Attempting Tier B dilutes focus.

After the sprint: Tier B pages are the compounding organic assets that fit Goal 1 (grow non-branded organic revenue). Feed them into Month 2 / Month 3 / Quarter 3 as dedicated workstreams. Priority order by click-per-impression efficiency:

1. Honduras, El Salvador (fix broken pages first — highest CTR gain per hour of work)
2. Austria, Croatia (small pools, page 1 already, polish the margin)
3. Chile, Holland (page 1 but CTR room)
4. Argentina, Germany (big pools, page 2 — content work)
5. Colombia, Portugal, France, Spain, Brazil (page 2 cluster)
6. Belgium, England, others (longer tail)

## Open Questions Feeding Into Synthesis

1. Does the Q1-specific GSC slice look materially different from the 12-month average, or is the 12-month view a fair proxy for sprint planning? (Would need a separate GSC export to confirm.)
2. Should the sprint explicitly add a player-spotlight collection template based on the Lamine Yamal page's performance? That's outside the current Goal 2 scope but the data argues for it.
3. Does Tony want to see /collections/ecuador and /collections/peru as net-new collection pages? GSC data on Ecuadorian / Peruvian diaspora queries would answer that; not checked yet.
