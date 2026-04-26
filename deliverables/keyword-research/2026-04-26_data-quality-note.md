# Data Quality Note: Category Priority Matrix v1

**Date:** 2026-04-26
**Author:** KIRA (Keyword Research Agent)
**Companion to:** `2026-04-26_category-priority-matrix.csv` and `.md`
**Purpose:** Document material data quirks that shape the matrix's confidence labels, plus the upstream fixes Mike can hand to Shopify admin so the next quarterly matrix lands cleaner.

This note is the honest accounting of "what we know we don't know cleanly," and where the data could be better. It's separate from the matrix narrative on purpose: the matrix tells Tony what to prioritize; this note tells Mike what to fix in the data plumbing so the next matrix is sharper.

## Section 1: Shopify exports (5 material quirks)

### 1.1 Blank product type row, $146,024

The 12-month export at `data/shopify-exports/sales-by-product-type.csv` row 5 carries $146,024 in revenue with no product type populated. That's roughly 6.3% of the $2.32M 12-month total. We don't know which products contributed.

**Why it matters for the matrix:** any category-level revenue rollup understates by up to that amount, depending on which categories the unlabeled products belong to. Most likely Apparel or Footwear by sheer share of the catalog, but we're guessing.

**Confidence impact:** revenue figures for the top three categories (Footwear $978K, Apparel $813K, Equipment $254K [`sales-by-product-type.csv` rows 2-4]) are best-read as floors, not exact figures. Tier 1 calls don't change because the relative ordering holds.

**Upstream fix Mike can hand to Shopify admin:** identify the products with no product type in Shopify admin, assign types per the existing taxonomy. Estimated effort: 2 to 4 hours of bulk product editing depending on catalog size of the unassigned set.

### 1.2 Service SKU `return,package_protection`, $44,042

`sales-by-product-type.csv` row 7 lists "return,package_protection" at $44,042. That's the Redo app's return-and-package-protection SKU; not retail revenue.

**Why it matters:** any revenue total that includes this row inflates by ~1.9%. A "Footwear $978K + Apparel $813K = $1.79M" rollup is honest; a "12-month total revenue" rollup that includes this $44K is misleading.

**Upstream fix:** in the Shopify admin product type field, change "return,package_protection" to a non-retail prefix like "service: redo" so it's filterable out of retail rollups by anyone reading the export.

### 1.3 Mixed taxonomy depth (flat vs breadcrumb)

The same export carries both flat top-level types ("Footwear", "Apparel", "Equipment", "Goalkeeper") and full breadcrumb paths ("Apparel - Men's Apparel - Socks", "Apparel - Youth Apparel - Goalkeeper Shirt"). They aren't sub-rollups of the top-level types; they're parallel rows representing different products.

**Why it matters for the matrix:** goalkeeper category revenue sits at face-value $53,768 [row 6] but products tagged with breadcrumb-path types like "Apparel - Youth Apparel - Goalkeeper Shirt" don't roll up into that face value. The reattributed proxy ($80K to $120K) acknowledges this; firming up the number requires either DataFeedWatch product-tag data or a one-time Shopify admin cleanup.

**Confidence impact:** Goalkeeper Tier 1 Medium label carries this caveat. Same risk applies in lighter form to any cross-cutting category (e.g., a Nike-specific or wide-fit-specific rollup pulled from this export will undercount).

**Upstream fix:** pick one taxonomy depth and apply consistently. Either flat top-level (drop the breadcrumb-path values; products keep their existing breadcrumb in collections, just not in product type) OR full breadcrumb (deepen the flat values; "Footwear" becomes "Footwear - Men's - Firm Ground" et al.). Consistency matters more than which approach. Recommendation: stay with flat top-level for product type (matches Shopify-native conventions) and use collection memberships for sub-categorization.

### 1.4 Gift card and `wrapin` service SKUs in product type list

`sales-by-product-type.csv` includes:
- `GIST_GIFT_CARD` $2,722 [row 9]
- `Online Gift Cards` $0 [row 31]
- `wrapin` $0 [row 32]
- `Gift Option` $632 [row 12]

These are not retail products. They're service or gift-card SKUs.

**Why it matters:** small absolute dollars but they appear in any product-type rollup, signal taxonomy hygiene issues, and could trip up monthly reporting if any of them grow unexpectedly.

**Upstream fix:** prefix non-retail SKUs in the product type field (e.g., "service: gift-card", "service: gift-option", "service: wrapin"). Same approach as Section 1.2; one consistent prefix lets future analysis filter cleanly.

### 1.5 Partial April 2026 month

`sales-by-month.csv` row 14 shows April 2026 at $111,140.78. The 12 months prior averaged approximately $184,000 per month (sum of April 2025 through March 2026 monthly figures divided by 12; raw sum is $2,212,624). The export was pulled mid-month [data pull date 2026-04-21 per `data/gsc-exports/README.md`; Shopify export pulled the same window per `data/shopify-exports/README.md`]; April is partial, not declining.

**Why it matters:** any year-over-year or month-over-month comparison that treats April 2026 as a complete month will misread the trend. Q1 2026 ($139,810 Jan + $126,489 Feb + $197,444 Mar = $463,743) is a clean comparable; April-to-date is not.

**Upstream fix:** none needed (this is normal mid-month data state). Process fix: every monthly report should explicitly state the export pull date and call out partial months. That's a Reporting Agent (METRIK) discipline, not a Shopify admin task.

## Section 2: GSC file naming mismatch

The agent definition Section 2 step 8 references the Shopify exports under stable names like `_top-queries.csv`, `_top-pages.csv`, `_weekly-performance.csv`. The actual files in `data/gsc-exports/` use a 12-month-window prefix:

- Spec name: `_top-queries.csv`
  Actual file: `2025-04-to-2026-04_top-queries.csv`
- Spec name: `_top-pages.csv`
  Actual file: `2025-04-to-2026-04_top-pages.csv`
- Spec name: `_weekly-performance.csv`
  Actual file: `2025-04-2026-04_weekly-performance.csv` (note: also a hyphen variant in this one)

**Why it matters:** the agent's reads worked (file content is clean), but any literal-path reference in the agent definition or downstream documentation is wrong. Future agents (SCRIBE, METRIK, RECON) inherit the same mismatch unless either the agent definitions are updated or the files are renamed.

**Recommended fix (low priority, low effort):** standardize on one of two patterns:
- Pattern A: drop the date prefix. Files become `top-queries.csv`, `top-pages.csv`, etc. Simplest to reference.
- Pattern B: keep the date prefix and update the agent definitions to use the actual filenames. More accurate to the export reality.

Pattern B is safer because it preserves the date stamp on the export, which becomes important when multiple windows are stored side-by-side. Pattern A is simpler if files are always rolled to the latest 12-month window in place.

## Section 3: AWT data gap (now partially mitigated by DataForSEO)

The agent definition Section 2 step 10 directs KIRA to check `data/ahrefs/` for current Ahrefs Webmaster Tools (AWT) export. The directory is empty (only `.gitkeep`). No keyword list, no backlink snapshot.

**Pre-DataForSEO state.** Competitive difficulty calls would have defaulted to "pending AWT confirmation, Medium-Low confidence" per the agent definition. That posture would have applied to all 28 matrix rows.

**Post-DataForSEO state (live as of 2026-04-26).** Competitive difficulty calls now route through DataForSEO Keyword Difficulty as primary source, with fallback to inferred-from-SERP analysis where DataForSEO doesn't return a value. Confidence improves from Medium-Low to Medium-High where DataForSEO returns KD; stays Medium where it doesn't. Net effect: no Tier 1 call in the matrix is gated on AWT data anymore.

**What AWT would still add.** Backlink data (referring domains, anchor text, link velocity), historical position tracking, and Ahrefs-specific metrics (Domain Rating, URL Rating). Backlink data is Technical SEO and Competitor Intel scope; KIRA doesn't need it for the keyword matrix. Historical position tracking is METRIK scope. Domain Rating could refine Tier 2 ordering but doesn't move Tier 1 calls.

**Recommendation:** AWT install drops in priority. Useful when Technical SEO and Competitor Intel agents go live, not blocking KIRA's matrix work.

## Section 4: DataForSEO KD coverage gap

The DataForSEO `bulk_keyword_difficulty` endpoint returned a Keyword Difficulty value for **only 2 of 13** keywords queried in this matrix session:

| Keyword | KD returned |
|---|---|
| real madrid jersey | 5 |
| south korea jersey | 3 |
| mexico jersey | (not returned) |
| guatemala soccer jersey | (not returned) |
| italy soccer jersey | (not returned) |
| el salvador jersey | (not returned) |
| honduras soccer jersey | (not returned) |
| usmnt jersey | (not returned) |
| best goalkeeper gloves | (not returned) |
| goalkeeper jerseys | (not returned) |
| lamine yamal jersey | (not returned) |
| messi argentina jersey | (not returned) |
| futsal shoes | (not returned) |

**Working theory** (not confirmed with DataForSEO documentation): the `bulk_keyword_difficulty` endpoint appears to skip KD calculation on keywords below a volume or recency threshold, or where SERP composition is highly mixed (many SERP feature types blocking a clean organic top-10 read). The 2 keywords that returned KD are both clean organic SERPs with high volume and stable intent.

**The workaround actually used.** The `keyword_overview` endpoint returned **volume, intent, and paid competition** for all 13 keywords in the same batch. That gave us:
- Volume confirmation (the matrix's Tier 1 calls reference these volumes)
- Intent classification (informational / commercial / transactional)
- Paid competition score (0 to 1, where most jersey queries scored 0.95 to 1.0 = HIGH)
- Monthly trend data (the +395%/+643% USMNT spike was visible here)

For competitive difficulty inference on the 11 keywords without KD, the matrix uses:
- The DataForSEO paid competition score as a directional input
- SERP composition observation from the `serp_organic_live_advanced` test query on "soccer cleats" earlier in the session (Adidas, Nike, DICK's, Soccer.com pattern)
- Existing GSC ranking data (if ProSoccer already ranks position 10 to 20, organic difficulty is inferred Medium)
- Phase 1 audit Trust Flow data on the verified peer set (soccerpost, soccer.com, prosoccer, wegotsoccer, soccervillage, soccerzoneusa, worldsoccershop, pelesoccer, soccerwearhouse [`shared-intelligence/seo-findings.md` 2026-04-21]).

**Confidence impact:** competitive difficulty calls in the matrix carry these labels:
- **High** (DataForSEO KD confirmed): 2 keywords (real madrid jersey, south korea jersey)
- **Medium-High** (DataForSEO inferred from volume + paid competition + SERP pattern): the rest of the Tier 1 candidates
- **Medium-Low** (no DataForSEO query, inferred from existing GSC rank data): Tier 2 country pages

**Recommendation for v2 query design.** Try alternate keyword phrasings that may carry KD data: "mexico jersey adidas" instead of "mexico jersey"; "best goalkeeper gloves 2026" instead of "best goalkeeper gloves". Also try `dataforseo_labs_google_keyword_overview` with `include_clickstream_data=true` (not used in v1; might surface KD on more keywords). Test in a small batch (5 keywords) before scaling.

## Section 5: Theme migration orphan collections

Phase 2 Task 1 surfaced two stale "copy" variants of live collection pages, present in the live Shopify collections sitemap:

- `/collections/spain-jerseys-copy`
- `/collections/france-hats-copy`

**Origin:** almost certainly leftovers from someone duplicating collections during the late-2025 theme migration (the prior agency's work). Never cleaned up.

**Why it matters for the matrix:** these don't appear as priority candidates; the matrix doesn't tier them. They're flagged here because cannibalization detection (Section 9 of the agent definition) requires watching for split equity across overlapping URLs. If either stale "copy" page accumulates impressions over time, it splits link equity from the live page.

**Status:** Technical SEO follow-up. KIRA flags; doesn't fix. Recommended fix: canonical review (likely point them at the live equivalents), then noindex or delete based on whether either page has accumulated any backlinks worth preserving.

**Related Phase 2 finding worth flagging here too.** `/collections/chile` was Cloudflare-rate-limited (HTTP 429) on both initial crawl and retry [Phase 2 Task 1; Phase 2 Task 4]. Inventory state for Chile is unknown; the page exists and ranks position 10.96 with 88 clicks [`_top-pages.csv` row 155], so it's not blocked from Google. The matrix lists Chile as Tier 2 Low confidence with this caveat. Re-crawl with a different user-agent or longer delay is a Technical SEO follow-up.

## Section 6: DataForSEO API spend transparency

| Metric | Value |
|---|---|
| API calls this matrix session | 3 |
| Endpoints used | `serp_organic_live_advanced` (1 query), `keyword_overview` (1 batch of 13 keywords), `bulk_keyword_difficulty` (1 batch of 13 keywords) |
| Total keywords analyzed | 14 unique |
| Estimated spend | ~$0.05 |
| Session cap target | $5 |
| Project cap target (matrix v1 scope) | $20 |
| Cap utilization | <1% |

**Cost discipline going forward.** Per the agent definition Section 5, KIRA targets <$20 in API spend for matrix work. v1 used <$1; v2 budget is the remaining $19. Per-keyword priority work feeding On-Page SEO is the largest expected ongoing spend; rough estimate of 50 to 100 keywords per quarter at ~$0.005 per keyword combined volume + KD = $0.50 to $1.00 per quarter. Well within budget.

**Per the agent definition: bulk operations require explicit Mike approval.** None used in this session. If a future analysis would benefit from a bulk SERP scan (say, top-100 SERP results across 50 keywords for competitor visibility), KIRA surfaces the request with cost estimate before running.

## Section 7: Recommended upstream fixes (sorted by impact per hour of effort)

Bundled list of what Mike can hand to Shopify admin (Jorge) and to the developer pipeline. Sorted by impact-per-hour-of-effort:

| # | Fix | Owner | Effort | Impact |
|---|---|---|---|---|
| 1 | Categorize the $146,024 blank product type rows in Shopify admin | Jorge | 2-4 hours | High (firms up Tier 1 revenue floors and goalkeeper reattribution) |
| 2 | Prefix service SKUs (`return,package_protection`, gift cards, `wrapin`, `Gift Option`) with `service:` in product type field | Jorge | 30 minutes | Medium (prevents service revenue inflating retail rollups in monthly reports) |
| 3 | Standardize product type taxonomy: pick flat top-level OR full breadcrumb, apply consistently | Jorge + Mike (decision) | 4-8 hours after decision | Medium-High (firms up goalkeeper revenue, keeper-tagged Apparel reattribution, and any future segment analysis) |
| 4 | Resolve theme migration orphan collections (spain-jerseys-copy, france-hats-copy): canonical or noindex or delete | Misal + Misha | 1-2 hours | Low to Medium (prevents future link equity split; small immediate impact) |
| 5 | Re-crawl /collections/chile with delay or alternate user-agent | Mike or Technical SEO Agent (when built) | 30 minutes | Low (informational completion; page already performs) |
| 6 | Configure DataFeedWatch inventory feed (logged separately in `work-log/follow-ups.md`) | Mike + DataFeedWatch | 4-8 hours | High (lifts goalkeeper Tier 1 Medium to High; firms up all inventory-driven opportunity flags; lifts matrix v2 confidence broadly) |

**The DataFeedWatch inventory feed (item 6) is the single highest-impact upstream fix on this list.** It moves the matrix's largest confidence weakness (the inventory signal column) from Medium to High across most rows. Currently logged in `work-log/follow-ups.md` 2026-04-21 entry as Mike-to-configure plus Master-Strategist-to-wire-into-workflow.

## Section 8: What changes in matrix v2

Tightening these data sources changes the v2 matrix in specific, predictable ways:

- **Goalkeeper revenue moves from $80K-$120K proxy to firm figure.** Tier 1 Medium → Tier 1 High likely.
- **Inventory depth signals firm up across all rows.** Honduras stays Tier 3 unless inventory builds; Austria, Croatia, the legacy long-slug pages all get firm-confidence Tier 3 calls. Inventory-driven opportunity flags become reliable rather than proxy.
- **Mexico revenue contribution becomes traceable** (currently buried inside Apparel $813K). Lets us model sprint ROI in dollars per click rather than just incremental click volume.
- **Per-collection revenue tracking enables tier defense.** Today the matrix doesn't have per-country revenue to back up Tier 1 calls; v2 with cleaner taxonomy makes Tony-facing reporting more concrete.
- **DataForSEO KD coverage may broaden** with v2 query design (alternate phrasings, clickstream data flag). 
- **AWT data, if installed, refines Tier 2 ordering** but doesn't move the top 10.

**v2 trigger:** quarterly cadence (next refresh approximately end of July 2026), OR earlier if the DataFeedWatch feed lands and changes inventory state materially, OR earlier if a sprint outcome contradicts a Tier 1 call.

## Sources cited

- `data/shopify-exports/sales-by-product-type.csv`
- `data/shopify-exports/sales-by-month.csv`
- `data/shopify-exports/README.md`
- `data/gsc-exports/README.md`
- `data/gsc-exports/2025-04-to-2026-04_top-pages.csv`
- `data/gsc-exports/2025-04-to-2026-04_top-queries.csv`
- `data/gsc-exports/2025-04-to-2026-04_search-appearance.csv`
- `data/gsc-exports/2025-04-2026-04_weekly-performance.csv`
- `deliverables/phase-2-discovery/task-1-inventory.md`
- `deliverables/phase-2-discovery/task-2-tiering.md`
- `deliverables/phase-2-discovery/task-4-theme-migration-analysis.md`
- `shared-intelligence/seo-findings.md`
- `work-log/follow-ups.md`
- `.claude/agents/keyword-research/agent.md`
- DataForSEO MCP `serp_organic_live_advanced`, run 2026-04-26
- DataForSEO MCP `keyword_overview`, run 2026-04-26
- DataForSEO MCP `bulk_keyword_difficulty`, run 2026-04-26
