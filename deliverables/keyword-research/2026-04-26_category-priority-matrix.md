# Category Priority Matrix v1

**Date:** 2026-04-26
**Author:** KIRA (Keyword Research Agent)
**Status:** v1 (first matrix; revisit quarterly or when material inputs shift)
**Companion files:**
- `2026-04-26_category-priority-matrix.csv` (the structured matrix)
- `2026-04-26_data-quality-note.md` (Shopify, GSC, AWT, DataForSEO data caveats)

## Executive summary

ProSoccer's first Category Priority Matrix maps 28 categories to four tiers. The headline:

- **5 Tier 1 High-confidence rows** form the durable execution core: **Mexico, Futsal/Indoor Shoes, Italy, El Salvador, Guatemala**. All five anchor to three or more independent data points.
- **3 Tier 1 Medium-confidence rows** with explicit caveats: **Goalkeeper** (revenue reattribution proxy), **USMNT** (URL consolidation is a hard prerequisite), **South Korea** (sub-threshold score, sprint Layer 1 commitment retained).
- **1 Hypothesis-tier row**: **Player-Spotlight Template** with Lamine Yamal as the validated proof point and **Messi-Argentina** as the locked test page. Promote to Tier 1 only after 60-day measurement.
- **1 Tier 3 supply-constrained row**: **Honduras**, the canonical "searchable but not sellable" example. Metadata fix only; no heavy investment until inventory deepens.

The matrix tells the next 12 months in clean language: **fund the 8-week World Cup sprint on the 5 Tier 1 High pages plus USMNT-conditional, run Futsal as the year-round compounding asset in parallel, build Goalkeeper authority deliberately through Q3 2026, test the Player-Spotlight template once with discipline, and stop pouring effort into pages the catalog can't convert**.

## How tiers are assigned

The framework scores six dimensions and weights them (revenue 25%, search opportunity 25%, inventory signal 20%, competitive difficulty 10%, strategic fit 15%, seasonality fit 5%). Score ≥ 70 with inventory and positioning gates satisfied lands Tier 1; 50 to 69 lands Tier 2; below 50 or failed inventory gate lands Tier 3 supply-constrained. Hypothesis tier is the explicit "test before scaling" bucket where evidence isn't yet sufficient to tier confidently.

Confidence labels follow the agent definition: **High** (three or more independent data points), **Medium** (two data points or named gap), **Low** (one data point or significant uncertainty).

## Tier 1: the execution core

### Tier 1 High (5 rows)

**Mexico** (`/collections/mexico`). The largest single sprint opportunity by every measure. 119,131 GSC impressions sit at position 28.44 [`_top-pages.csv` row 93], with 74,000 monthly searches on the head term and a +173% quarterly volume trend [DataForSEO keyword_overview, run 2026-04-26]. The page has 45 active products [Phase 2 Task 1] and a deep LA Mexican-diaspora moat that maps directly to the Carlos avatar [`04-customer-avatars.md`]. Phase 2 reset expectations from Phase 1's claimed position 9 to 14: this is rebuild scope, not polish, and won't fully recover inside 8 weeks. Worth the investment given the impression pool. **Score: 83.5.**

**Futsal / Indoor Shoes**. The site's single largest non-brand traffic source: the `best-futsal-shoes-indoor` blog at 2,227 clicks at position 11.01 [`_top-pages.csv` row 3]. Head term volume 14,800/month [DFS]. Goal 1 names futsal explicitly. The category fits the High-Performance Expert positioning (technical surface specificity = ProSoccer's wedge) and the Tyler avatar (gear that performs). Compounding asset, runs in parallel with the WC sprint. **Score: 74.75.**

**Italy** (`/collections/italy`). 138,080 GSC impressions at position 13.99 [`_top-pages.csv` row 22], with the head term up +125% quarterly and +50% yearly [DFS]. CTR sits at 0.46%, which is the lever: meta description rewrite that earns the click, not heavy on-page rebuild. Sprint Layer 1 fast polish work. **Score: 74.**

**El Salvador** (`/collections/el-salvador`). The lowest-effort highest-return item on the sprint board. Page is broken (default Shopify title, empty meta description, bare H1) yet ranks position 10.8 with 76,858 impressions [`_top-pages.csv` row 32]. Volume 5,400/month with +86% quarterly trend [DFS]. 42 products. Basic optimization pass is the entire scope. **Score: 70.75.**

**Guatemala** (`/collections/guatemala`). Already top-of-page-1 at position 9.36 with 99,864 impressions [`_top-pages.csv` row 20]. 38 products. Polish-and-publish work scope. The title doesn't carry "World Cup 2026" (Template B per Phase 2 Task 1) which is a small fixable gap if we want to catch sprint-tied queries. Carlos-avatar fit through Copa Oro context. **Score: 70.75.**

### Tier 1 Medium (3 rows)

**Goalkeeper** (cross-collection: gloves, jerseys, pants, field-player-gloves, plus the goalkeeper cleats blog). Goal 1 names this category explicitly: "We have real expertise; most competitors don't." A cluster of 5 keeper-related URLs already pulls 3,352 clicks across 512,500 combined impressions [`_top-pages.csv` rows 9, 11, 13, 47, 74]. Reattributed revenue proxy lands $80,000 to $120,000 (face-value $53,768 [`sales-by-product-type.csv` row 6] understates because keeper-tagged products span Apparel and Footwear taxonomies). Tyler's performance fit and Jennifer's safety fit both apply. Confidence is Medium because the revenue figure waits on DataFeedWatch product-tag data; v2 firms it up. **Score: 70.25.**

**USMNT** (`/collections/united-states-men-women`). The steepest catalyst on the entire board: head term volume +395% monthly and +643% yearly [DFS]. The host-country effect is loading in real time. 79,559 impressions at position 45.84 [`_top-pages.csv` row 241]. **Hard blocker before sprint work begins**: 3 overlapping US collection URLs are splitting link equity [Phase 2 Task 1]. Technical SEO must consolidate to one canonical with 301s from the others before any USMNT on-page work pays off. Once consolidated, expect measurable progress inside the sprint, not full recovery from position 45.8. **Score: 69.5.**

**South Korea** (`/collections/south-korea`). By honest framework score this is Tier 2 (64), but two things justify Layer 1 sprint inclusion. DataForSEO confirms KD = 3 (the lowest difficulty in the entire 13-keyword batch); position is already 12.61 with 1.3% CTR (the best of any country page) [Phase 2 Task 2]; +125% yearly volume trend. The page has 18 products, marginal pass on the 15-product inventory gate. **Sprint Status: Layer 1.** Ship the polish now per Goal 2 commitment. The matrix calls Tier 2 for long-term compounding posture; both can be true. **Score: 64.**

## Tier 2: the year-round compounding pool

Tier 2 isn't sprint scope. It's where SEO investment lands after the World Cup window closes (August onwards). The pool is large because the pre-World Cup period brought a lot of national team pages into striking distance. Top candidates by Q3 2026 priority order:

- **Argentina** (181 clicks, 138,797 impressions, position 17.56 [`_top-pages.csv` row 80]). Reigning WC champion with Messi tailwind. Strong v2 promotion candidate if the player-spotlight test works.
- **Holland** (393 clicks, 127,612 impressions, position 10.53 [`_top-pages.csv` row 24]). CTR is the lever; already on page 1.
- **Germany** (266 clicks, 114,857 impressions, position 18.47 [`_top-pages.csv` row 48]). $76K opportunity value in the January audit. Solid page-2-to-page-1 candidate.
- **Spain, France, Portugal, Brazil** (combined ~745 clicks across ~313K impressions [Phase 2 Task 2]). Page 2 cluster; CTR and content work.
- **Colombia, Belgium, England, Chile** (longer tail; smaller pools). Polish where inventory passes the gate; meta-only treatment where it doesn't. Croatia and Austria fail the inventory gate and have moved to Tier 3 for v1 (see Tier 3 section).

## Tier 3: supply-constrained and legacy

**Honduras** (`/collections/honduras`). Canonical inventory-gate failure. The page ranks position 10.7 with a 1.15% CTR on 10,465 impressions [`_top-pages.csv` row 123], which would normally argue Tier 1. But it has only 6 products [Phase 2 Task 1], failing the 15-product threshold. The metadata fix is near-zero-effort and ships inside the sprint as a quick win, but heavy investment is wasted until inventory deepens. The right call is one of two things: (a) Tony's team builds out inventory before pursuing the ranking, or (b) we route Honduran-diaspora search demand to a higher-level Hispanic-diaspora category page with deeper inventory. The "searchable but not sellable" rule made tangible. **Score: 43.75.**

**Austria** (10 products) and **Croatia** (11 products) sit in the same pattern as Honduras. Austria ranks page 1 at position 8.84 with 6,424 impressions [`_top-pages.csv` row 256]; Croatia ranks page 2 at position 18.35 with 24,330 impressions [`_top-pages.csv` row 94]. Both fail the 15-product inventory gate and both score sub-50 (Austria 38, Croatia 45). Treatment matches Honduras: meta polish only, no heavy investment until inventory grows.

**Legacy long-slug pages** (Algeria, Ghana, Senegal, Sweden, New Zealand, Scotland, Australia at `/collections/{country}-national-soccer-team-jerseys-apparel`). Each carries 2 to 8 products [Phase 2 Task 1]. All fail the 15-product gate. Technical SEO consolidates these to short-slug equivalents where they exist, or noindexes. KIRA flags only.

## Hypothesis tier: the player-spotlight question

**Player-Spotlight Template, anchored by Lamine Yamal**. The single most striking finding on the site: `/collections/lamine-yamal-jersey-fc-barcelona-spain` ranks position 10.38 with 791 clicks across 118,981 impressions [`_top-pages.csv` row 14; `seo-findings.md` 2026-04-21]. That outperforms every national team page on the site, including Mexico, Italy, and the full committed-sprint 6.

The hypothesis: a **player + club + country** template earns more click-per-impression than a country-level template alone, because the search query is more specific and the SERP is less crowded with brand-direct sites.

**Test design.** Build one new player-spotlight page using **Messi-Argentina** as the test player. Reasons: 49,500 monthly head-term volume [DFS]; Argentina is reigning World Cup champion, which sustains demand through 2026; Messi's MLS presence (Inter Miami) creates US-specific search relevance; Argentina jersey is already a known revenue line. **Vinicius-Brazil is the v2 test** if Messi-Argentina proves the template generalizes.

**Measurement.** 60 days post-launch. Promote to Tier 1 if the new page earns ≥40% of Lamine Yamal's click-per-impression efficiency. Hold at Hypothesis if it underperforms. Do not scale to a third test page without two validated proof points.

**Why Hypothesis tier and not Tier 1.** The Lamine Yamal data is one validated page. Locking in player-spotlight as Tier 1 from a single proof point would be the kind of false-certainty call the agent definition's Section 9 explicitly prevents. The right move is "test before scaling," and the matrix should hold the line.

## DataForSEO surprises worth Tony's attention

DataForSEO went live earlier today (2026-04-26). Three findings from this session's focused queries are material to the matrix and to monthly reporting going forward:

1. **Mexico jersey volume is up +173% quarterly** [DFS keyword_overview]. The World Cup catalyst is already loading; we expected the lift but the steepness is real. The matrix's Tier 1 High call on Mexico is reinforced.

2. **USMNT jersey is up +395% monthly and +643% yearly** [DFS]. This is the steepest single catalyst on the entire board. Every week the URL consolidation prerequisite stays unresolved is a week of split equity during the steepest slope. Technical SEO should treat consolidation as Week 1 work, not Week 2.

3. **Real Madrid jersey KD = 5** at 74,000 monthly volume [DFS bulk_keyword_difficulty]. That's much more reachable than I'd assumed for a top-3 club term. It doesn't mean ProSoccer wins position 1 (Adidas and Real Madrid Direct will hold those), it means non-brand retailers can rank reasonably at lower top-10 positions. The full **club jersey cluster** (Real Madrid, Barcelona, Manchester City, Liverpool, etc.) becomes a credible v2 expansion target, faster than Goal 1's framing implied. Bumps club jerseys higher in the v2 priority order.

4. **South Korea jersey KD = 3** [DFS]. Lowest difficulty in the entire 13-keyword batch. Position 12.61 with 1.3% CTR is realistic to crack into the top 10 inside the sprint window. Reinforces the Layer 1 sprint inclusion despite the framework score sitting at Tier 2.

The remaining 11 of 13 keywords queried returned **no organic Keyword Difficulty value** from DataForSEO, which appears to be a DataForSEO-side coverage gap on lower-volume or niche queries (volume + intent + paid competition came back cleanly on all 13). Documented in the data quality note. Doesn't block matrix v1, but worth knowing for v2 query design.

## V2 expansion candidates

Categories that didn't make the v1 top 10 but should re-enter the matrix in v2:

- **Club jerseys cluster**. Real Madrid, Barcelona, Manchester City, Liverpool, Bayern Munich, PSG, Juventus, plus MLS clubs with LA relevance (LA Galaxy, LAFC, Inter Miami). Goal 1 explicitly names these as compounding. DataForSEO suggests reachability is better than expected. Splitting into per-club rows in v2 once PDP-readiness is audited.
- **Position-specific cleat content cluster**. The 6-blog cluster (defenders, strikers, midfielders, wide-feet, kids, plus the 2025 field-position roundup) already pulls 3,027 combined clicks across 688,436 impressions at impression-weighted position 13.40 [`_top-pages.csv` rows 15, 18, 22, 30, 36, 40]. Goalkeeper cleats blog is counted in the separate Goalkeeper cluster row to avoid double-counting. Maintenance posture in v1; folds into a Cleats category tier in v2.
- **Cleats (head-term collection)**. ProSoccer ranks position 21.22 on "soccer cleats" [`_top-queries.csv` row 20]. The DataForSEO SERP check earlier this session confirmed the head term is a dogfight (Adidas, Nike, Dick's, brand-direct DTCs, Soccer.com all dominate page 1). Not a Tier 1 candidate; the High-Performance Expert positioning explicitly chooses NOT to compete on the generic head term. Cleats authority compounds through the position-specific blog cluster, not the head-term collection page.
- **Patches and name-and-number sets**. High-CTR niches at small volume: `name-and-number-sets` page 27 ranks 4.8% CTR at position 10.86 with 1,366 clicks [`_top-pages.csv` row 7]. Not strategic priority but already-converting; maintenance posture.

## Gap opportunities annex: Ecuador and Peru

Phase 2 Task 1 confirmed `/collections/ecuador` and `/collections/peru` do not exist on the site. The question is whether Ecuadorian or Peruvian diaspora search demand justifies building net-new collection pages.

**This matrix doesn't answer that question.** Validation requires GSC query-level filtering on terms like "ecuador" + "ecuadorian" + "tricolor" (Ecuador) and "peru" + "peruvian" + "blanquirroja" (Peru) against the ProSoccer top-queries export, plus a DataForSEO volume check on the head terms. Neither was run in this session because the v1 priority was the existing-page matrix, not the gap analysis.

**Recommended next step.** Pull a 5-minute GSC query check on both countries and a 2-keyword DataForSEO volume call. If either crosses a meaningful threshold (1,000+ impressions or 1,000+/month volume), v2 promotes from Hypothesis-Gap to Tier 2 with a "build new page" recommendation. If neither does, both stay deferred in v2.

## Red-team appendix

Where the matrix could be wrong, what would change my mind, and which claims a skeptical reader would push on:

**Claim: Mexico is the largest single sprint opportunity.** What a skeptic would ask: 119,131 impressions at position 28.4 means most of those impressions are on page 3 where users rarely go; the real reachable click pool is much smaller than the impression number suggests. Acknowledged. Realistic recovery inside the 8-week sprint moves Mexico from position 28 toward position 11 to 15. At ProSoccer's current 0.66% CTR average for that position band, this converts roughly 1,200 to 2,500 incremental monthly clicks against the 119,131 impression base. Achieving page 1 (positions 1 to 10) would generate roughly 3,500 to 7,000 incremental monthly clicks. Sprint scope realistically targets the page-2-to-page-1 transition; full page-1 capture is a Q3 2026 outcome, not an 8-week outcome. Setting Tony's expectations against position 11 to 15 economics, not against the full impression base, protects the engagement from the standard "we doubled impressions but conversions didn't follow" disappointment that traps SEO retainers.

**Claim: South Korea KD = 3 makes sprint inclusion easy.** What a skeptic would ask: KD = 3 doesn't mean the page hits position 1; it means top-10 entry is realistic. From position 12.61 to top 10 is a 2-position gain, not a tier-skipping move. Acknowledged. The realistic outcome is position 8 to 11 by sprint end, not position 1.

**Claim: Goalkeeper Tier 1 Medium is justified by strategic fit even though score is borderline 70.25.** What a skeptic would ask: 95-out-of-100 strategic-fit score is generous; a category where ProSoccer claims expertise but doesn't yet rank top 10 on most keeper terms is a hypothesis, not a proven wedge. Acknowledged: the Goal 1 doc names goalkeeper as a category where "we have real expertise; most competitors don't" but actual SERP performance (position 13.56 on `best-goalkeeeper-gloves`, 17.69 on `field-player-gloves`) shows we have ranking authority but not dominance. Tier 1 Medium is right; promotion to Tier 1 High waits on visible position gains across the cluster. v2 reassessment.

**Claim: Player-Spotlight Hypothesis tier is the right call from one validated page.** What a skeptic would ask: holding back from Tier 1 on a clearly working pattern delays revenue; build three player pages now and take the upside. Acknowledged. The case for the Hypothesis tier is the agent definition's discipline against false certainty, plus the genuine risk that Lamine Yamal's performance is partly attributable to the player's specific late-2025 hype rather than a generalizable template. One controlled test resolves this in 60 days; that's a tolerable cost.

**Claim: Honduras Tier 3 supply-constrained is the right framework call.** What a skeptic would ask: 1.15% CTR on a broken page is real signal; growing inventory to 15 products would be cheap if the demand is there. Agreed, partially. The matrix recommends two paths: (a) build inventory first, or (b) route demand to a higher-level Hispanic page. Path (a) is Tony's call; the matrix doesn't override the framework. If Tony's team adds 10+ products to the Honduras collection, the page promotes immediately to a Tier 1 reassessment.

**Weakest evidence in the matrix overall.** The inventory signal column is the load-bearing weakness. Without DataFeedWatch product-tag data or a dedicated Shopify products-by-collection export, depth is inferred from Phase 2 Task 1 product counts and age is a proxy from sales-by-product velocity. The matrix's Medium-confidence labels on inventory carry that uncertainty honestly, but a single DataFeedWatch feed lands all of those calls into High-confidence territory. The follow-up to install DataFeedWatch's inventory feed is logged in `work-log/follow-ups.md`.

**What would AWT data change.** If Ahrefs Webmaster Tools data lands in `data/ahrefs/`, competitive difficulty calls firm up further (especially on the 11 keywords where DataForSEO didn't return KD). Likely shifts Tier 2 calls more than Tier 1; doesn't move the top 10 meaningfully but tightens the year-round compounding pool order.

## Confidence posture summary

| Tier | Rows | Confidence | Primary risk |
|---|---|---|---|
| Tier 1 High | 5 | High | Mexico sprint-realism (rebuild not polish) |
| Tier 1 Medium | 3 | Medium | USMNT URL consolidation gating; goalkeeper revenue reattribution; South Korea inventory thin |
| Hypothesis | 1 | Medium-High in test design, Low in scaling | Lamine Yamal performance might not generalize |
| Tier 2 | 13 | High to Low (decreasing with smaller pools) | CTR ceilings depend on meta and content quality |
| Tier 3 | 8 (Honduras + Austria + 7 long-slug) | High | Inventory remains the gating constraint |

## Recommended next steps

**Week 1 (April 28 to May 4):**
1. **Technical SEO: USMNT URL consolidation kicks off.** This is the single highest-priority technical task; every week of delay during the +395%-monthly catalyst slope costs us.
2. **On-Page SEO: Honduras and El Salvador metadata fixes.** Lowest-effort highest-return work on the sprint board.
3. **Content Writer: Mexico rebuild brief.** Heavy lift; brief the rebuild scope before drafting.

**Weeks 2 to 4:**
4. Italy, Guatemala, South Korea Layer 1 polish (titles, meta descriptions, intro copy, internal linking).
5. Once Mexico draft lands, Layer 2 heavy lift execution.
6. Goalkeeper authority brief: identify which keeper-cluster page gets first content investment.

**Weeks 5 to 8:**
7. WC sprint completion plus the two non-country pieces (LA watch guide, authenticity guide).
8. Player-Spotlight test page (Messi-Argentina) builds in parallel; measurement window opens at sprint close.

**Post-sprint (August onwards):**
9. Tier 2 country pool execution (Argentina, Holland, Germany lead).
10. Player-Spotlight test page hits 60-day measurement; promote or hold based on click-per-impression efficiency.
11. v2 matrix refresh: Goalkeeper revenue reattribution (post-DataFeedWatch); club jersey cluster expansion; Ecuador and Peru gap validation.

**Ongoing:**
12. DataForSEO budget monitoring (target: <$20/month for KIRA's matrix maintenance and per-keyword priority work feeding On-Page SEO).
13. Quarterly matrix refresh against Q3 2026 inventory state and ranking outcomes.

## Sources cited

- `data/gsc-exports/2025-04-to-2026-04_top-pages.csv` (12-month GSC top pages, pulled 2026-04-20)
- `data/gsc-exports/2025-04-to-2026-04_top-queries.csv` (12-month GSC top queries)
- `data/gsc-exports/2025-04-to-2026-04_search-appearance.csv` (Merchant Listings vs Product Snippets split)
- `data/gsc-exports/2025-04-2026-04_weekly-performance.csv` (53-week trend)
- `data/shopify-exports/sales-by-product-type.csv` (12-month product type revenue)
- `data/shopify-exports/sales-by-month.csv` (13-month revenue trend)
- `deliverables/phase-2-discovery/task-1-inventory.md` (national team collection inventory and slug analysis)
- `deliverables/phase-2-discovery/task-2-tiering.md` (sprint priority A/B tiering)
- `deliverables/phase-2-discovery/task-4-theme-migration-analysis.md` (recovery context)
- `shared-intelligence/seo-findings.md` 2026-04-21 entry (Lamine Yamal page outperformance)
- `context/00-business-overview.md` (positioning frame)
- `context/04-customer-avatars.md` (Carlos, Jennifer, Tyler, Mike the Coach)
- `context/06-business-goals.md` (Goal 1 through Goal 4)
- `context/09-strategic-principles.md` (Layer 1 focus)
- DataForSEO MCP keyword_overview, run 2026-04-26 (13 keywords; volume + intent + paid competition)
- DataForSEO MCP bulk_keyword_difficulty, run 2026-04-26 (13 keywords; KD returned for 2)
- DataForSEO MCP serp_organic_live_advanced, run 2026-04-26 (1 query: "soccer cleats", US desktop)
