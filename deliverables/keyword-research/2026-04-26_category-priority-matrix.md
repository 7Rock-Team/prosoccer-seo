# Category Priority Matrix v1.1

**Date:** 2026-04-26
**Author:** KIRA (Keyword Research Agent)
**Status:** v1.1: expanded scope: World Cup contender coverage
**v1 baseline:** committed as `9313965` (28 rows; 8 Tier 1)
**Companion files:**
- `2026-04-26_category-priority-matrix.csv` (the structured matrix; 34 rows in v1.1)
- `2026-04-26_data-quality-note.md` (Shopify, GSC, AWT, DataForSEO data caveats)

## What changed in v1.1

Mike identified a real strategic gap in v1: the original sprint scope included LA-diaspora teams plus South Korea but excluded major World Cup contenders that ProSoccer carries deep inventory for. Argentina, Brazil, France, Portugal, Spain, Germany, Holland, England, Belgium, Colombia, Croatia, Uruguay, Japan, Senegal, Morocco: these 15 teams formed a required floor for v1.1, plus Norway and Jamaica added as candidates worth surfacing.

Two findings drove the v1.1 changes:

1. **DataForSEO volume confirmation rewrote the Tier 2 picture for major contenders.** v1's Tier 2 classifications on Argentina, Brazil, France, Portugal, Spain, Holland, Colombia, Germany, England were based on GSC impression data alone. With head-term volume + WC catalyst trend data from DataForSEO, the framework correctly elevates 9 teams to Tier 1.
2. **17 Tier 1 rows is operationally too many for an 8-week sprint.** Demoting categories that genuinely score Tier 1 to fit operational capacity would misrepresent the data. The fix is a three-wave execution structure within Tier 1.

Two adjustments Mike made on the v1.1 data:

- **England** sits at Tier 1 Medium (Wave 3) rather than borderline Tier 1 High. KD = 5 is real, but unmodeled ceilings (Adidas official-kit DTC dominance, UK retailer SEO competition, lower US commercial intent for non-diaspora country pages) cap realistic upside.
- **Senegal** stays in v1.1 with Tier 3 Legacy Long-Slug classification (existing-but-suboptimal asset). Flagged for VERITAS Technical SEO investigation.

## Executive summary

The v1.1 matrix maps **34 categories** across four tiers, with Tier 1 organized into three execution waves to make operational reality explicit:

- **17 Tier 1 rows** (up from 8 in v1), waved by execution timing:
  - **Wave 1 (active 8-week WC sprint, May to June 2026, 7 pages)**: Mexico, Argentina, Brazil, France, USMNT (gated on URL consolidation), El Salvador, Guatemala
  - **Wave 2 (May to June 2026, parallel after Wave 1 momentum, 6 pages)**: Italy, Spain, Portugal, Holland, Colombia, Germany
  - **Wave 3 (Q3 2026, post-tournament, 4 categories)**: England, Goalkeeper (cross-collection), Futsal, South Korea
- **1 Hypothesis-tier row**: Player-Spotlight Template (Messi-Argentina test page locked; Vinicius-Brazil v2; Norway-Haaland v3)
- **8 Tier 2 rows**: 6 country pages (Belgium, Jamaica, Norway, Japan, Uruguay, Chile) plus 2 v2 cluster candidates (Club Jerseys, Position-Specific Cleats)
- **6 Tier 3 rows**: Honduras (canonical supply-constrained), Austria, Croatia, Morocco, Senegal (legacy long-slug for VERITAS) plus the 6-page legacy long-slug collective
- **2 Hypothesis-Gap rows**: Ecuador and Peru (GSC validation required)

The matrix tells the next 12 months in clean operational language: **Wave 1 hits hard now (sprint), Wave 2 ramps as Wave 1 momentum is established, Wave 3 picks up post-tournament when WC catalyst data is in, Tier 2 cycles into Q3+ optimization, Tier 3 gets meta-only treatment plus VERITAS audit on legacy slugs.**

## How tiers and waves are assigned

The framework hasn't changed from v1: six dimensions, weighted 25 / 25 / 20 / 10 / 15 / 5 (revenue, search opportunity, inventory signal, competitive difficulty, strategic fit, seasonality fit). Score ≥ 70 with inventory and positioning gates passed lands Tier 1; 50 to 69 lands Tier 2; below 50 or failed inventory gate lands Tier 3.

**Waves are operational sequencing within Tier 1, not tier demotions.** A Wave 3 row is still Tier 1; it just executes in Q3 2026 instead of inside the WC sprint.

Wave assignment criteria:
- **Wave 1**: Tier 1 categories where (a) the WC catalyst window is the binding deadline, (b) data strength is highest, and (c) operational feasibility lets us execute inside the 8-week sprint.
- **Wave 2**: Tier 1 categories that benefit from WC catalyst but don't need to ship inside the 8-week sprint to capture value. Execution timing is May to June 2026, parallel as Wave 1 finishes.
- **Wave 3**: Tier 1 categories where execution is better post-tournament (catalyst data is in, no rushed Q2 work). Also covers compounding categories (Futsal, Goalkeeper) that don't tie to WC.

Confidence labels: **High** (three or more independent data points), **Medium** (two data points or named gap), **Low** (one data point or significant uncertainty).

## Tier 1: Wave 1 (active 8-week WC sprint, 7 pages)

The execution core for May to June 2026. Highest data strength + binding WC deadline + operational feasibility.

**Mexico** (`/collections/mexico`). Largest single sprint opportunity unchanged from v1. 119,131 GSC impressions at position 28.44 [`_top-pages.csv` row 93]; 74,000/mo head-term volume +173% quarterly trend [DataForSEO]; 45 active products [Phase 2 Task 1]; LA Mexican-diaspora moat anchored to Carlos avatar [`04-customer-avatars.md`]. Phase 2 reset expectations from Phase 1's claimed position 9 to 14: this is rebuild scope, not polish. **Score: 83.5.**

**Argentina** (`/collections/argentina`). v1.1 Tier 1 promotion. Reigning World Cup champion plus Messi MLS catalyst (Inter Miami creates US-specific search relevance). 138,797 GSC impressions at position 17.56 [`_top-pages.csv` row 80]; 9,900/mo head-term volume +124% quarterly +22% yearly [DFS]; 45 products. **Score: 78.75.**

**Brazil** (`/collections/brazil`). v1.1 Tier 1 promotion. **Highest jersey-query volume in the entire v1.1 batch at 22,200/mo** with +234% quarterly +123% yearly [DFS]; transactional intent (highest commercial signal of any non-USMNT team in the batch). 75,531 GSC impressions at position 22.09 [`_top-pages.csv` row 92]; 5x World Cup winner; Vinicius-Brazil player-spotlight v2 test candidate. **Score: 78.75.**

**France** (`/collections/france`). v1.1 Tier 1 promotion. **Steepest non-USMNT catalyst trend in the batch: +311% quarterly +311% yearly** [DFS]. 82,546 GSC impressions at position 14.66 [`_top-pages.csv` row 71]; 4,400/mo volume; 2018 winner with Mbappé tailwind; 44 products. **Score: 74.75.**

**USMNT** (`/collections/united-states-men-women`). The steepest catalyst on the entire board: head-term volume +395% monthly and +643% yearly [DFS]. The host-country effect is loading in real time. 79,559 impressions at position 45.84 [`_top-pages.csv` row 241]. **Hard blocker before sprint work begins**: 3 overlapping US collection URLs are splitting link equity [Phase 2 Task 1]. Technical SEO must consolidate to one canonical with 301s before any USMNT on-page work pays off. Once consolidated, expect measurable progress inside the sprint, not full recovery from position 45.8. **Score: 69.5.**

**El Salvador** (`/collections/el-salvador`). Lowest-effort highest-return on the sprint board. Page is broken (default Shopify title, empty meta description, bare H1) yet ranks position 10.8 with 76,858 impressions [`_top-pages.csv` row 32]. Volume 5,400/mo with +86% quarterly trend [DFS]. 42 products. Basic optimization pass is the entire scope. **Score: 70.75.**

**Guatemala** (`/collections/guatemala`). Already top of page 1 at position 9.36 with 99,864 impressions [`_top-pages.csv` row 20]. 38 products. Polish-and-publish work scope. The title doesn't carry "World Cup 2026" (Template B per Phase 2 Task 1) which is a small fixable gap if we want to catch sprint-tied queries. Carlos-avatar fit through Copa Oro context. **Score: 70.75.**

## Tier 1: Wave 2 (May to June 2026 parallel, 6 pages)

Tier 1 categories where execution starts as Wave 1 momentum is established. Same WC catalyst window but the work doesn't need to ship inside the 8-week sprint to capture value.

**Italy** (`/collections/italy`). 138,080 GSC impressions at position 13.99 [`_top-pages.csv` row 22]; +125% quarterly volume trend [DFS]. CTR sits at 0.46% which is the lever: meta description rewrite that earns the click, not heavy on-page rebuild. **Score: 74.**

**Portugal** (`/collections/portugal`). v1.1 Tier 1 promotion. 9,900/mo head-term volume +124% quarterly +83% yearly [DFS]; 69,695 GSC impressions at position 18.43 [`_top-pages.csv` row 68]; Cristiano legacy plus Bernardo Silva. The existing `/collections/cristiano-ronaldo` collection at position 19.85 [`_top-pages.csv` row 29] is a positioning tailwind. **Score: 74.**

**Spain** (`/collections/spain`). v1.1 Tier 1 promotion. 2024 European champion. 5,400/mo volume +175% quarterly +83% yearly [DFS]; 85,593 GSC impressions at position 18.73 [`_top-pages.csv` row 78]. The Lamine Yamal anchor page (118,981 impressions at position 10.38 [`_top-pages.csv` row 14]) feeds Spain authority. `/collections/spain-jerseys-copy` duplicate flagged for VERITAS cleanup [Phase 2 Task 1]. **Score: 73.25.**

**Holland** (`/collections/holland`). v1.1 Tier 1 promotion. Already on page 1 at position 10.53 with 127,612 impressions [`_top-pages.csv` row 24]; CTR ceiling is the primary lever. `/collections/netherlands` 301-redirects in but still pulls 103 extra clicks per Phase 2 Task 1. Both URLs healthy. **Score: 72.5.**

**Colombia** (`/collections/colombia`). v1.1 Tier 1 promotion. **v1.1 surprise: 9,900/mo head-term volume matches Argentina and Portugal** [DFS]. v1 had Colombia at Tier 2 Medium based on GSC alone (52,670 impressions). True demand is twice what GSC capture suggested. LA Latin American diaspora moat strong; 46 products. **Score: 72.5.**

**Germany** (`/collections/germany`). v1.1 Tier 1 promotion. 114,857 GSC impressions at position 18.47 [`_top-pages.csv` row 48]; 3,600/mo volume +125% quarterly +23% yearly [DFS]; consistent contender; January audit named approximately $76K opportunity value. **Score: 71.75.**

## Tier 1: Wave 3 (Q3 2026 post-tournament, 4 categories)

Tier 1 categories where execution is better post-tournament. WC catalyst data is in by then; compounding categories don't need to ship inside the sprint.

**England** (`/collections/england`). v1.1 Tier 1 promotion (KD-driven). DataForSEO confirms KD = 5 [`bulk_keyword_difficulty` 2026-04-26]; 1,900/mo volume +175% quarterly +52% yearly [DFS]; 53,522 GSC impressions at position 22.48 [`_top-pages.csv` row 175]. Premier League streaming has grown the US fan base. Wave 3 because of unmodeled ceilings: Adidas (official kit) DTC dominance, UK retailer SEO competition, US commercial intent on "england jersey" lower than diaspora-driven country pages. Tier 1 Medium captures "yes pursue, with realistic expectations." **Score: 71.**

**Goalkeeper** (cross-collection: gloves, jerseys, pants, field-player-gloves, plus the goalkeeper cleats blog). Goal 1 names this category explicitly: "We have real expertise; most competitors don't." A cluster of 5 keeper-related URLs already pulls 3,352 clicks across 512,500 combined impressions [`_top-pages.csv` rows 9, 11, 13, 47, 74]. Reattributed revenue proxy lands $80,000 to $120,000 (face-value $53,768 [`sales-by-product-type.csv` row 6] understates because keeper-tagged products span Apparel and Footwear taxonomies). Tyler's performance fit and Jennifer's safety fit both apply. Wave 3 because compounding asset, not WC-catalyst-driven. **Score: 70.25.**

**Futsal / Indoor Shoes**. Site's single largest non-brand traffic source: `best-futsal-shoes-indoor` blog at 2,227 clicks at position 11.01 [`_top-pages.csv` row 3]. Head-term volume 14,800/mo [DFS]. Goal 1 names futsal explicitly. Compounding asset; Wave 3 placement reflects timing not priority. **Score: 74.75.**

**South Korea** (`/collections/south-korea`). Score-based Tier 2 (64), operational Tier 1 Wave 3 by Mike's strategic call. DataForSEO confirms KD = 3 (lowest difficulty in entire batch); position 12.61 with 1.3% CTR (best of any country page) [Phase 2 Task 2]; +125% yearly volume trend [DFS]. 18 products, marginal pass on the 15-product gate. Wave 3 = "lower priority within Tier 1." **Score: 64.**

## Tier 2: the year-round compounding pool

Tier 2 isn't sprint scope. It's where SEO investment lands when Wave 2 wraps and Wave 3 begins. Q3+ optimization timing.

- **Belgium** (`/collections/belgium`). v1.1 shifted up from Tier 2 Low to Tier 2 Medium-High driven by exceptional **+400% quarterly +340% yearly** trend [DFS]. 49,840 impressions at position 18.35 [`_top-pages.csv` row 166]; 30 products. Catalyst slope is exceptional even if absolute volume is modest. Watch for Q3 promotion to Tier 1 if trend sustains. **Score: 61.5.**
- **Jamaica** (`/collections/jamaica`). New in v1.1. 30 products; 26 GSC clicks at position 20.36 [`_top-pages.csv` row 473]; 2,400/mo volume +238% quarterly +83% yearly [DFS]; Caribbean diaspora; LA has strong Caribbean presence. Title is 84 characters per Phase 2 Task 1: flag for VERITAS title-length cleanup. **Score: 59.**
- **Norway** (`/collections/norway`). New in v1.1. **+494% yearly volume trend** is the single largest yearly trend in the v1.1 batch: Haaland-driven [DFS]. Strong product-level GSC signal: "norway soccer jersey" 36 clicks at position 6.57 [`_top-queries.csv` row 165]; Nike Norway home jersey product page 188 clicks at position 7.76. 20 products. The collection page is absent from the top 1000 GSC pages, suggesting an indexing or content gap. **Norway-Haaland is the v3 player-spotlight test candidate** after Messi-Argentina (v1) and Vinicius-Brazil (v2). **Score: 52.5.**
- **Japan** (`/collections/japan`). New in v1.1. DataForSEO KD = 15 confirmed (moderate; second-highest in batch after Real Madrid jersey KD = 5 from v1); 4,400/mo volume +128% quarterly +50% yearly [DFS]. 20 products. Collection page absent from top 1000 means demand exists but ProSoccer isn't capturing: collection optimization opportunity. **Score: 51.75.**
- **Uruguay** (`/collections/uruguay`). New in v1.1. Inventory passes gate (20 products). +400% quarterly trend [DFS] but small absolute base (1,300/mo). Borderline Tier 2 (score 50.25 just above 50 threshold); reassess Q3. **Score: 50.25.**
- **Chile** (`/collections/chile`). Page 1 at position 10.96 with 23,646 impressions [`_top-pages.csv` row 155]. Phase 2 crawl was Cloudflare-rate-limited, inventory state unknown. Re-crawl needed before firmer tier call; not in v1.1 DFS batch. **Score: 42.**

Plus 2 cluster rows (v2 expansion candidates) that aren't single-collection categories: see V2 expansion section.

## Tier 3: supply-constrained, inventory-light, and legacy

**Honduras** (`/collections/honduras`). Canonical inventory-gate failure. Ranks position 10.7 with a 1.15% CTR on 10,465 impressions [`_top-pages.csv` row 123], which would normally argue Tier 1. But it has only 6 products [Phase 2 Task 1], failing the 15-product threshold. The metadata fix is near-zero-effort and ships inside Wave 1 as a quick win, but heavy investment is wasted until inventory deepens. The right call is one of two things: (a) Tony's team builds out inventory before pursuing the ranking, or (b) we route Honduran-diaspora search demand to a higher-level Hispanic-diaspora category page with deeper inventory. The "searchable but not sellable" rule made tangible. **Score: 43.75.**

**Croatia** (11 products) and **Austria** (10 products) sit in the same pattern as Honduras at smaller audience scales. Croatia ranks page 2 at position 18.35 with 24,330 impressions [`_top-pages.csv` row 94]; Austria ranks page 1 at position 8.84 with 6,424 impressions [`_top-pages.csv` row 256]. Both fail the 15-product gate and both score sub-50 (Croatia 46.5, Austria 38). Treatment: meta polish only.

**Morocco** (`/collections/morocco`). New in v1.1. 8 products, fails 15-product gate. v1.1 finding: post-2022 Atlas Lions surge has faded (-33% quarterly trend [DFS]); the Tier B floor inclusion thesis didn't hold up in current data. No GSC signal in top 1000 pages or queries. Treatment: meta polish only if any. **Score: 41.5.**

**Senegal** (legacy long-slug only at `/collections/senegal-national-soccer-team-jerseys-apparel`). New in v1.1. No short-slug equivalent exists. DataForSEO confirms 1,000/mo volume but **-70% quarterly trend** (post-2022 surge faded sharply). Per Mike's volume threshold logic, 1,000/mo is well below the 5K/mo migration urgency line, suggesting deprecation may be acceptable. **Flagged for VERITAS Technical SEO investigation**: VERITAS to decide migrate-with-301, deprecate, or leave-as-is. The legacy long-slug pattern likely affects other teams too; VERITAS audit of legacy slugs across all national team collections is recommended. **Score: 37.5.**

**Legacy long-slug collective** (Algeria, Ghana, Sweden, New Zealand, Scotland, Australia at `/collections/{country}-national-soccer-team-jerseys-apparel`). 2 to 8 products each. All fail the 15-product gate. VERITAS consolidates to short-slug equivalents where they exist, or noindexes. KIRA flags only.

## Hypothesis tier: the player-spotlight question

**Player-Spotlight Template, anchored by Lamine Yamal**. The single most striking finding on the site: `/collections/lamine-yamal-jersey-fc-barcelona-spain` ranks position 10.38 with 791 clicks across 118,981 impressions [`_top-pages.csv` row 14; `seo-findings.md` 2026-04-21]. That outperforms every national team page on the site, including Mexico, Italy, and the full committed-sprint 6.

The hypothesis: a **player + club + country** template earns more click-per-impression than a country-level template alone, because the search query is more specific and the SERP is less crowded with brand-direct sites.

**Test design (locked).** Build one new player-spotlight page using **Messi-Argentina** as the test player. 49,500 monthly head-term volume [DFS]; Argentina is reigning World Cup champion; Messi's MLS presence (Inter Miami) creates US-specific search relevance; Argentina jersey is already a known revenue line. Build during sprint Weeks 5 to 8; measurement window opens at sprint close.

**v2 and v3 candidates (sequenced).** **Vinicius-Brazil** is the v2 test if Messi-Argentina proves the template generalizes. v1.1 DataForSEO data adds **Norway-Haaland** as the v3 candidate: 720/mo volume but **+494% yearly trend** [DFS], the largest yearly trend in the entire v1.1 batch. Haaland is doing for Norwegian jerseys what Messi did for Argentine ones in 2022.

**Measurement.** 60 days post-launch on the Messi-Argentina test page. Promote to Tier 1 if the new page earns ≥40% of Lamine Yamal's click-per-impression efficiency. Hold at Hypothesis if it underperforms. Do not scale to a third test page without two validated proof points.

## DataForSEO surprises worth Tony's attention

DataForSEO went live earlier today (2026-04-26). Eight findings across the v1 and v1.1 query rounds are material to the matrix and to monthly reporting going forward:

1. **Mexico jersey volume +173% quarterly** [DFS]. The World Cup catalyst is loading hard. Tier 1 Wave 1 placement reinforced.

2. **USMNT jersey +395% monthly +643% yearly** [DFS]. Steepest single catalyst on the entire board. Every week the URL consolidation prerequisite stays unresolved is a week of split equity during the steepest slope. Technical SEO should treat consolidation as Week 1 work, not Week 2.

3. **Brazil jersey at 22,200/mo with +234% quarterly +123% yearly** [DFS]. Highest jersey-query volume in the v1.1 batch: bigger than Argentina (9,900) and on a par with USMNT (33,100) when intent is factored in (both transactional). Tier 1 Wave 1 placement.

4. **France jersey +311% quarterly +311% yearly** [DFS]. Steepest non-USMNT catalyst trend. Mbappé tailwind. Tier 1 Wave 1 placement.

5. **Belgium +400% quarterly +340% yearly on a small base (1,300/mo)** [DFS]. The slope matters even when absolute volume is modest. Belgium gets Tier 2 Medium-High and explicit watchlist status for Q3 promotion to Tier 1.

6. **Real Madrid jersey KD = 5 at 74,000/mo** [DFS]. More reachable than I'd assumed for a top-3 club term. Adidas and Real Madrid Direct hold position 1 to 3, but non-brand retailers can rank reasonably at lower top-10 positions. Bumps the **Club Jersey cluster** higher in the v2 priority order.

7. **South Korea jersey KD = 3** [DFS]. Lowest difficulty in the entire combined batch. Position 12.61 with 1.3% CTR is realistic to crack into top 10. Reinforces Wave 3 inclusion despite framework score sitting at Tier 2.

8. **Norway jersey +494% yearly trend** at 720/mo [DFS]. Single largest yearly trend in v1.1. Haaland-driven. Norway-Haaland becomes the v3 player-spotlight test candidate (after Messi-Argentina v1 and Vinicius-Brazil v2).

**KD coverage gap remained in v1.1 round.** Of 17 keywords queried in the v1.1 batch, DataForSEO returned KD for 2 (England = 5, Japan = 15). The other 15 returned no organic KD value. Combined with v1 (2 of 13 returned KD), the session-cumulative pattern is **4 of 30 keywords returning KD** (13%). DataForSEO-side coverage gap, not a tooling failure. Volume + intent + paid competition came back cleanly on all 30. Documented in the data quality note. Workaround for v2: try alternate phrasings + clickstream data flag.

## V2 expansion candidates

Categories that didn't make v1.1 Tier 1 but should re-enter the matrix in v2:

- **Club jerseys cluster**. Real Madrid, Barcelona, Manchester City, Liverpool, Bayern Munich, PSG, Juventus, plus MLS clubs with LA relevance (LA Galaxy, LAFC, Inter Miami). Goal 1 explicitly names these as compounding. DataForSEO suggests reachability is better than expected via the Real Madrid jersey KD = 5 finding. Splitting into per-club rows in v2 once PDP-readiness is audited.
- **Position-specific cleat content cluster**. The 6-blog cluster (defenders, strikers, midfielders, wide-feet, kids, plus the 2025 field-position roundup) already pulls 3,027 combined clicks across 688,436 impressions at impression-weighted position 13.40 [`_top-pages.csv` rows 15, 18, 22, 30, 36, 40]. Goalkeeper cleats blog is counted in the separate Goalkeeper cluster row. Maintenance posture in v1.1; folds into a Cleats category tier in v2.
- **Cleats (head-term collection)**. ProSoccer ranks position 21.22 on "soccer cleats" [`_top-queries.csv` row 20]. The DataForSEO SERP check confirmed the head term is a dogfight (Adidas, Nike, Dick's, brand-direct DTCs, Soccer.com all dominate page 1). Not a Tier 1 candidate; the High-Performance Expert positioning explicitly chooses NOT to compete on the generic head term. Cleats authority compounds through the position-specific blog cluster, not the head-term collection page.
- **Patches and name-and-number sets**. High-CTR niches at small volume: `name-and-number-sets` page 27 ranks 4.8% CTR at position 10.86 with 1,366 clicks [`_top-pages.csv` row 7]. Maintenance posture; not a strategic priority.

## Gap opportunities annex: Ecuador and Peru

Phase 2 Task 1 confirmed `/collections/ecuador` and `/collections/peru` do not exist on the site. The v1.1 round didn't run DataForSEO volume checks on these because the floor 17-keyword batch focused on existing-page priority shifts. Validation requires GSC query-level filtering on terms like "ecuador" + "ecuadorian" + "tricolor" (Ecuador) and "peru" + "peruvian" + "blanquirroja" (Peru) against the top-queries export, plus a 2-keyword DataForSEO call on the head terms.

**Recommended next step.** 5-minute GSC query check plus 2-keyword DataForSEO volume call. If either crosses a meaningful threshold (1,000+ impressions or 1,000+/month volume), v2 promotes from Hypothesis-Gap to Tier 2 with a "build new page" recommendation. If neither does, both stay deferred in v2.

## Sprint scope recommendation

The 8-week WC sprint scope stays at **7 active pages**, drawn from Tier 1 Wave 1:

1. **Mexico**: heavy lift (rebuild scope)
2. **Argentina**: Tier 1 polish + WC content drop (v1.1 addition)
3. **Brazil**: Tier 1 polish + WC content drop (v1.1 addition)
4. **France**: Tier 1 polish + Mbappé content (v1.1 addition)
5. **USMNT**: gated on URL consolidation; once unblocked, Layer 2 heavy lift
6. **El Salvador**: broken-page metadata fix (lowest effort)
7. **Guatemala**: fast polish, Layer 1

Plus the two non-country sprint pieces previously scoped (LA watch guide, authenticity guide) and the Honduras quick-win meta fix that ships inside the sprint window even though Honduras is Tier 3 supply-constrained.

**The argument for not expanding past 7 pages in the active sprint.** Operational reality. 8 weeks divided across 7 pages plus 2 content pieces plus the Honduras quick-fix is already a tight execution schedule. Adding Italy, Spain, Portugal, Holland, Colombia, Germany to the active sprint dilutes per-page quality and risks shipping six mediocre rewrites instead of three excellent ones. Wave 2 starting in late May / early June 2026 captures the same WC catalyst window without compressing Wave 1 quality.

**The argument for a Wave 2 launch instead of sprint expansion.** Wave 2 (Italy, Spain, Portugal, Holland, Colombia, Germany) ships during May to June 2026 in parallel as Wave 1 finishes. The WC tournament runs June 11 to July 19, 2026, so Wave 2 work that ships by mid-June still captures the in-tournament search surge. Wave 2 is sprint-adjacent, not post-sprint.

**v1.1 sprint scope vs v1 sprint scope:** v1 sprint scope was 7 pages too (Mexico, USMNT, Italy, El Salvador, Guatemala, Honduras, South Korea). v1.1 swaps 4 of those into Wave 2 / Wave 3 (Italy → Wave 2; South Korea → Wave 3; Honduras stays as Wave 1 quick-win meta-only) and brings in Argentina, Brazil, France as Wave 1: the major WC contenders that v1 missed.

## Confidence posture summary

| Tier / Wave | Rows | Confidence | Primary risk |
|---|---|---|---|
| Tier 1 Wave 1 | 7 | High (5) + Medium (2: USMNT consolidation gated, El Salvador / Guatemala data clean) | USMNT URL consolidation timing; Mexico sprint-realism (rebuild not polish) |
| Tier 1 Wave 2 | 6 | High (5) + Medium-High (1: Germany) | All v1.1 promotions; CTR ceilings depend on meta and content quality |
| Tier 1 Wave 3 | 4 | Medium (England Adidas-DTC ceiling, Goalkeeper revenue reattribution, South Korea inventory thin); High (Futsal) | Compounding categories that need Q3 data check before promotion locking |
| Hypothesis | 1 | Medium-High in test design, Low in scaling | Lamine Yamal performance might not generalize |
| Tier 2 | 8 (6 country + 2 cluster) | High (Belgium trend), Medium (Jamaica, Norway, Japan), Low (Uruguay, Chile) | Catalyst trends are real; absolute volumes modest; v2 reassessment possible |
| Tier 3 | 6 | High (Honduras canonical, Senegal flagged) + Medium (Austria, Croatia, Morocco, legacy collective) | Inventory remains the gating constraint |

## Recommended next steps

**Week 1 (April 28 to May 4):**
1. **Technical SEO: USMNT URL consolidation kicks off.** This is the single highest-priority technical task; every week of delay during the +395%-monthly catalyst slope costs us.
2. **On-Page SEO: Honduras and El Salvador metadata fixes.** Lowest-effort highest-return work on the sprint board.
3. **Content Writer: Mexico rebuild brief.** Heavy lift; brief the rebuild scope before drafting.
4. **VERITAS: Senegal legacy long-slug audit.** Decide migrate / deprecate / leave-as-is. Surface broader legacy long-slug pattern for ProSoccer national team collections.

**Weeks 2 to 4 (Wave 1 active):**
5. Argentina, Brazil, France Wave 1 polish and WC content (titles, meta descriptions, intro copy, internal linking, content drop).
6. Guatemala Layer 1 polish.
7. Once Mexico draft lands, Wave 1 heavy lift execution.

**Weeks 5 to 8 (Wave 1 finishing, Wave 2 launching, Hypothesis test):**
8. WC sprint completion plus the two non-country pieces (LA watch guide, authenticity guide).
9. **Wave 2 launches**: Italy, Spain, Portugal, Holland, Colombia, Germany begin polish work in parallel as Wave 1 wraps.
10. Player-Spotlight test page (Messi-Argentina) builds; measurement window opens at sprint close.

**Q3 2026 (Wave 3 + Tier 2 cycle):**
11. **Wave 3 ramps**: England, Goalkeeper, Futsal, South Korea active execution.
12. Tier 2 country pool optimization (Belgium watchlist; Jamaica, Norway, Japan, Uruguay polish where merited).
13. Player-Spotlight test page hits 60-day measurement; promote or hold based on click-per-impression efficiency.
14. v2 matrix refresh: Goalkeeper revenue reattribution (post-DataFeedWatch); Club Jersey cluster expansion; Ecuador and Peru gap validation; Norway-Haaland v3 player-spotlight test if Messi-Argentina v2 holds.

**Ongoing:**
15. DataForSEO budget monitoring (target: <$20/month for KIRA's matrix maintenance and per-keyword priority work feeding On-Page SEO).
16. Quarterly matrix refresh against Q3 2026 inventory state and ranking outcomes.

## Red-team appendix

Where the matrix could be wrong, what would change my mind, and which claims a skeptical reader would push on.

**v1.1 specific challenges:**

**Claim: 8 teams legitimately shifted from Tier 2 to Tier 1 in v1.1.** What a skeptic would ask: did the framework just become more generous because Mike asked for expansion? Acknowledged. The honest test: weights didn't change (25/25/20/10/15/5 same as v1); inventory and positioning gates honored (Croatia, Austria, Morocco, Senegal, Honduras still Tier 3); the shifts came from DataForSEO data v1 didn't have. The expansion is data-driven, not pressure-driven.

**Claim: 17 Tier 1 rows in three waves is honest, not over-tiering.** What a skeptic would ask: 17 of 34 categories are Tier 1; that's 50%: sounds like everything got promoted. Reasonable concern. Counter: of the 17 Tier 1 rows, 12 are national team pages with World Cup catalyst trends running +89% to +643%. Tier 1 status reflects "high commercial priority during this 12-month window." Same matrix in Q4 2027 (post-WC) would tier most of these national pages back to Tier 2 because the catalyst window will have closed. Tier inflation is window-specific; it shrinks back when the WC tailwind fades.

**Claim: South Korea Tier 1 Wave 3 at score 64 is a valid override.** What a skeptic would ask: framework integrity matters; if the score says Tier 2, calling it Tier 1 by override is starting to break the framework. Acknowledged with caveat. The matrix records this override transparently (priority_tier = "Tier 1 (Wave 3)"; confidence_label = "Medium (override; score 64 sub-threshold)"). The override is operational (sprint-eligible per Mike) rather than data-driven. If Wave 3 outcomes don't validate, South Korea drops to Tier 2 in v2 cleanly.

**v1 challenges that still apply (preserved from v1):**

**Claim: Mexico is the largest single sprint opportunity.** What a skeptic would ask: 119,131 impressions at position 28.4 means most of those impressions are on page 3 where users rarely go. Acknowledged. Realistic recovery inside the 8-week sprint moves Mexico from position 28 toward position 11 to 15. At ProSoccer's current 0.66% CTR average for that position band, this converts roughly 1,200 to 2,500 incremental monthly clicks against the 119,131 impression base. Achieving page 1 (positions 1 to 10) would generate roughly 3,500 to 7,000 incremental monthly clicks. Sprint scope realistically targets the page-2-to-page-1 transition; full page-1 capture is a Q3 2026 outcome, not an 8-week outcome. Setting Tony's expectations against position 11 to 15 economics, not against the full impression base, protects the engagement from the standard "we doubled impressions but conversions didn't follow" disappointment that traps SEO retainers.

**Claim: South Korea KD = 3 makes sprint inclusion easy.** What a skeptic would ask: KD = 3 doesn't mean position 1; it means top-10 entry is realistic. From position 12.61 to top 10 is a 2-position gain, not a tier-skipping move. Acknowledged. The realistic outcome is position 8 to 11 by Wave 3 close, not position 1.

**Claim: Goalkeeper Tier 1 Medium is justified by strategic fit even though score is borderline 70.25.** What a skeptic would ask: 95-out-of-100 strategic-fit score is generous. Acknowledged: actual SERP performance (position 13.56 on `best-goalkeeeper-gloves`, 17.69 on `field-player-gloves`) shows we have ranking authority but not dominance. Tier 1 Medium is right; promotion to Tier 1 High waits on visible position gains.

**Claim: Player-Spotlight Hypothesis tier is the right call from one validated page.** Acknowledged. The case for the Hypothesis tier is the agent definition's discipline against false certainty, plus the genuine risk that Lamine Yamal's performance is partly attributable to player-specific late-2025 hype rather than a generalizable template. One controlled test resolves this in 60 days; tolerable cost.

**Claim: Honduras Tier 3 supply-constrained is the right framework call.** Acknowledged. If Tony's team adds 10+ products to the Honduras collection, the page promotes immediately to a Tier 1 reassessment.

**Weakest evidence in the matrix overall.** The inventory signal column remains the load-bearing weakness. v1.1 doesn't change this; DataFeedWatch product-tag data still pending. Inventory-driven opportunity flags stay proxy-based until that lands.

**What would AWT data change.** Backlink and historical position data would refine Tier 2 ordering and per-team competitive context, but doesn't move the Tier 1 wave structure meaningfully. AWT install drops in priority post-DataForSEO availability.

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
- v1 baseline: git commit `9313965` (28 rows, 8 Tier 1)
- DataForSEO MCP `keyword_overview`, run 2026-04-26 (v1 round: 13 keywords; v1.1 round: 17 keywords)
- DataForSEO MCP `bulk_keyword_difficulty`, run 2026-04-26 (v1 round: 13 keywords, KD returned for 2; v1.1 round: 17 keywords, KD returned for 2)
- DataForSEO MCP `serp_organic_live_advanced`, run 2026-04-26 (1 query: "soccer cleats", US desktop)
