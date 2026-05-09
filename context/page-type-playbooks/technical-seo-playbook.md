# Technical SEO Playbook

_Page-type playbook for technical SEO deliverables that don't sit on a single URL. Read by VERITAS on every technical-fix deliverable; read by ORIN when scoping a technical work request. The playbook governs methodology and structure for technical work. The six copy-writing principles in `context/03-brand-voice.md` still apply to deliverable prose, but the deliverable's substance is technical specification, not customer-facing copy._

## Subject focus

Technical SEO work is about discoverability mechanics. Schema markup, redirects, canonical handling, sitemap discipline, indexation, crawl budget, Core Web Vitals, robots.txt, hreflang, structured-data injection points, server-side rendering, the URL architecture itself.

The reader of a technical deliverable is the implementer (Misha for theme work, the developer for storefront work, Mike for Shopify admin work, VERITAS for ongoing monitoring). The reader is not the avatar. Specifications beat persuasion. Implementer routing beats marketing prose.

## Scope

This playbook governs VERITAS's technical work and ORIN's technical-deliverable scoping. When the workforce produces:

- 404 and 5xx error remediation deliverables
- Schema audit deliverables (Product, FAQ, BreadcrumbList, Review, ItemList)
- Redirect maps
- Sitemap configuration audits
- URL consolidation briefs (e.g., USMNT three-URL split consolidation)
- Canonical audits
- Indexation cleanup briefs
- Core Web Vitals fix briefs
- Robots.txt and crawl-budget recommendations
- Hreflang and locale-architecture briefs

VERITAS reads this playbook for methodology. The deliverable lands at `deliverables/technical-fixes/YYYY-MM-DD_<slug>.md` and gets logged to `deliverables/tracking/technical-seo-log.md` per ORIN agent.md Section 9 'Master tracking update obligation'.

## Forbidden in technical deliverables

- Marketing copy. No avatar voice, no emotional hooks, no Carlos / Jennifer / Tyler / Mike-the-Coach framing. The technical deliverable speaks to the implementer, not to the customer.
- Store positioning. Technical work is platform-level. "Pasadena retail since the 1990s" doesn't belong in a redirect map. Positioning lives in the homepage and on collection-page hero copy, not in technical specs.
- Hand-waving. "Improve indexation" is not a deliverable; "redirect 14 broken product handles to their renamed counterparts; submit fresh sitemap; monitor GSC for 4 weeks" is a deliverable.
- Generic best-practices guidance disconnected from ProSoccer's specific state. The deliverable cites the specific URL pattern, the specific schema field, the specific redirect rule. References to "best practices" without specifics signal the deliverable wasn't written against current state.

## Required in technical deliverables

- Specificity. Exact URL patterns. Exact schema types and field values. Exact redirect paths (source URL, destination URL, redirect type 301 / 302 / 308). Exact file paths in the Hyper theme repo or the storefront repo. Exact timestamps for GSC observations.
- Implementer routing. Each item is tagged with who applies it: Mike (Shopify admin), Misha (theme repo), the developer (storefront repo), VERITAS (ongoing monitoring), Jorge (product-level Shopify admin). Routing is the difference between a deliverable that ships and one that stalls.
- Cost and effort estimates per fix. Time estimate in hours, MCP credit estimate where applicable, blast-radius assessment (single page, single template, site-wide). The estimate makes prioritization possible.
- Priority by impact. High for traffic-recovery work (broken pages with GSC clicks losing revenue). Medium for crawl-budget cleanup and routine maintenance. Low for nice-to-have improvements. The priority drives the implementation order.
- Verification plan. How does the implementer confirm the fix landed correctly? GSC URL inspection? Live HEAD check? Schema validator run? Crawl re-run? Each fix names its verification step.
- Rollback plan where applicable. For high-risk changes (URL migrations, large redirect-rule deployments, sitemap restructures), the deliverable names how to roll back if the fix produces unexpected results.

## Required pre-write data

VERITAS confirms current state before proposing fixes. Sources by deliverable type:

- **404 and 5xx remediation:** GSC `_search-appearance.csv` or live GSC error report, Screaming Frog crawl, Firecrawl spot-checks for live verification.
- **Schema audit:** live page Firecrawl scrape with schema extraction, schema-validator output, theme-template inspection for current schema injection points, GSC Rich Results report for current snippet status.
- **Redirect map:** the source list of broken URLs (404 GSC report, redirect-loop crawl output, broken-internal-link export from Screaming Frog), the destination map (which URL each broken URL should redirect to, sourced from sitemap-state.md and admin product / collection lists).
- **Sitemap configuration audit:** the live `sitemap.xml` index and child chunks, `deliverables/tracking/sitemap-state.md`, the admin product / collection inventory (Mike's Shopify admin export).
- **URL consolidation brief:** the live state of every URL in the consolidation set (Firecrawl scrape per URL), GSC ranking and traffic data per URL, the canonical-and-redirect chain per URL.

The pre-write data is cited inline in the deliverable per the source-citation conventions in ORIN agent.md Section 6.

## Deliverable structure

Standardized structure for every technical-fix deliverable. Variations by type are documented in the worked examples below; the skeleton is constant.

```
# [Deliverable Title]: [scope]

- **Date:** YYYY-MM-DD
- **Author:** VERITAS (with ORIN consolidation note where applicable)
- **Audience:** [Mike / Misha / Developer / Jorge / VERITAS for monitoring]
- **Severity:** [Critical / High / Medium / Low]
- **Confidence:** [High / Medium / Low]

## Summary
[Two to four sentences. What's broken or out of spec. What the fix does. What ships.]

## Current state
[Specific. URL patterns, schema gaps, redirect chains, sitemap deltas. Sourced inline.]

## Recommended fixes
[Itemized. Each fix names: source URL or pattern, destination or change, redirect type if applicable, schema field if applicable, exact theme or storefront file path if applicable, implementer, time estimate, priority, verification step, rollback plan if applicable.]

## Implementer routing summary
[Grouped by implementer: Mike's Shopify-admin items, Misha's theme-repo items, Developer's storefront-repo items, Jorge's product-level items, VERITAS's monitoring items.]

## Verification plan
[How the workforce confirms each fix landed. GSC URL inspection schedule, live HEAD check schedule, schema-validator re-run, crawl re-run, GSC Rich Results report monitoring, etc.]

## Sources cited
[Every URL pattern, every schema field, every redirect rule cited inline. Aggregated here.]

## Open flags for ORIN and Mike
[Items that need cross-agent attention or Mike escalation. Multi-stakeholder decisions, scope-creep risks, items where confidence is Low.]
```

## Worked example 1: Schema audit deliverable

Scope: audit Product schema across 17 Tier 1 collection pages and their associated product pages; flag missing fields; route fixes by implementer.

```
# Schema Audit: Product Schema Across Tier 1 Collections

- **Date:** 2026-05-08
- **Author:** VERITAS
- **Audience:** Mike (review), Misha (theme-repo schema injection points)
- **Severity:** High (Goal 3 Merchant Listings dependency)
- **Confidence:** High (verified against live theme templates and DataFeedWatch feed sample)

## Summary
17 Tier 1 collection pages and their associated product pages are missing two Product schema fields that Merchant Listings requires (`brand`, `gtin13`). Current snippet eligibility is Product Snippets only; fix would unlock Merchant Listings, which delivers approximately 12x click-per-impression vs Product Snippets per Goal 3. Fix is theme-template work in `sections/product-template.liquid` plus DataFeedWatch feed mapping verification. Estimated implementer effort: 4 to 6 hours Misha; 1 hour VERITAS verification.

## Current state
- Product schema injects via `snippets/product-schema.liquid` [theme-repo path verified 2026-05-08].
- Required Merchant Listings fields present: `name`, `image`, `description`, `sku`, `offers.price`, `offers.priceCurrency`, `offers.availability` [Firecrawl scrape 2026-05-08, JSON-LD extracted from `/products/mexico-2026-home-authentic-jersey-adidas`].
- Required Merchant Listings fields MISSING: `brand`, `gtin13` [same scrape, verified across 5 spot-checked products].
- DataFeedWatch feed includes `brand` and `gtin13` per current feed sample [DataFeedWatch CSV export 2026-04-30, columns 14 and 22].
- Gap: theme template is not pulling `brand` and `gtin13` into the product-schema snippet despite the feed having the values.

## Recommended fixes
1. **Add `brand` field to product-schema.liquid snippet.** Source: product metafield `custom.brand` if present, fall back to `vendor`. Destination: schema field `brand.@type` "Brand" plus `brand.name`. Implementer: Misha. Time estimate: 1.5 hours. Priority: High. Verification: Firecrawl scrape on a deployed product page, JSON-LD extracted, `brand` field present and populated. Rollback: revert the snippet edit.

2. **Add `gtin13` field to product-schema.liquid snippet.** Source: product metafield `custom.gtin13` (current source per DataFeedWatch feed mapping). Destination: schema field `gtin13`. Implementer: Misha. Time estimate: 1.5 hours. Priority: High. Verification: same as fix 1. Rollback: revert.

3. **Verify Merchant Listings eligibility shifts after deploy.** GSC Rich Results report; expect Product Snippets count to decrease and Merchant Listings count to increase across affected URLs. Implementer: VERITAS. Time estimate: 1 hour at 14 days post-deploy. Priority: High. Verification: GSC Rich Results report shows the migration; cross-check with `mcp__gsc-server__inspect_url_enhanced` on 5 sample URLs.

## Implementer routing summary
- **Misha (theme repo, `mike-audit` branch):** fixes 1 and 2.
- **VERITAS (monitoring):** fix 3 at 14 days post-deploy.
- **Mike (review and route):** approves Misha brief; routes to Misha; receives VERITAS confirmation at 14 days.

## Verification plan
- Day 0: Misha applies fixes 1 and 2 to `mike-audit` branch.
- Day 1: VERITAS Firecrawl-scrapes 5 sample product pages; confirms schema extraction shows `brand` and `gtin13`.
- Day 2: Mike reviews; if clean, Misha merges to main.
- Day 14 post-merge: VERITAS pulls GSC Rich Results report; confirms Merchant Listings eligibility shift.
- Day 30 post-merge: VERITAS pulls GSC ranking and CTR delta on affected URLs; logs to `deliverables/tracking/technical-seo-log.md`.

## Sources cited
- Theme repo: `snippets/product-schema.liquid`, current state 2026-05-08.
- Live page: `/products/mexico-2026-home-authentic-jersey-adidas`, Firecrawl scrape 2026-05-08, JSON-LD extracted.
- DataFeedWatch feed sample: CSV export 2026-04-30, columns 14 and 22.
- Merchant Listings field requirements: Google Search Central documentation, current as of 2026-04-15.
- Goal 3 click-per-impression ratio: `context/06-business-goals.md` 'Goal 3 Merchant Listings'.

## Open flags for ORIN and Mike
- Confirm `custom.gtin13` metafield is populated for all 13,611 products in the live sitemap before site-wide deploy. If a subset is empty, fix 2 needs a fallback to suppress the field rather than emit empty (an empty `gtin13` is worse than a missing one).
- Schema fix is site-wide because the snippet renders on every product page. The 14-day verification window covers the Tier 1 set; the broader rollout is verified at 30 days.
```

## Worked example 2: Redirect map

Scope: 26 unique one-off URLs from the 2026-05-08 GSC 404 sample needing redirect rules. Mirrors the structure of `deliverables/technical-fixes/2026-05-08_404-5xx-remediation.md`.

```
# Redirect Map: One-off 404s from GSC Sample 2026-05-08

- **Date:** 2026-05-08
- **Author:** VERITAS (consolidated from ORIN's 2026-05-08 404 remediation deliverable)
- **Audience:** Mike (Shopify-admin redirect application)
- **Severity:** High for the 1 URL with GSC clicks; Medium for the 14 broken product handles; Low for the 11 Magento .html and deprecated pages
- **Confidence:** High (each redirect verified against live `sitemap-state.md` for destination existence)

## Summary
26 one-off 404 URLs from the GSC 2026-05-08 sample need redirect rules in Shopify admin. 1 has GSC clicks (High priority traffic recovery). 14 are broken product handles redirecting to renamed product URLs (Medium priority crawl-budget cleanup). 11 are legacy Magento `.html` patterns and deprecated pages routing to current category counterparts (Low priority). Estimated implementer effort: 1 hour Mike (bulk redirect entry in Shopify admin Navigation > URL Redirects).

## Current state
- 26 URLs returning 404 in the GSC sample.
- For each URL, the destination is verified against `deliverables/tracking/sitemap-state.md` to confirm the destination is live.
- 5 of the 26 URLs have inbound external backlinks per Majestic [Majestic backlink report 2026-04-15]; these are flagged for canonical preservation via 301 (not 302).

## Recommended fixes
[Table with 26 rows. Each row: source URL, destination URL, redirect type 301, priority, GSC clicks last 12 months, inbound backlink count, implementer (Mike), time estimate per row (~2 minutes in Shopify admin bulk entry).]

| Source URL | Destination URL | Type | Priority | GSC clicks | Backlinks |
|---|---|---|---|---|---|
| /collections/old-mexico-2014 | /collections/mexico | 301 | High | 47 | 2 |
| /products/messi-jersey-2018 | /products/messi-jersey-inter-miami-2026 | 301 | Medium | 0 | 1 |
| /pages/locations.html | /pages/locations | 301 | Low | 0 | 0 |
| ... 23 more rows | | | | | |

## Implementer routing summary
- **Mike (Shopify admin, Navigation > URL Redirects):** all 26 redirects.
- **VERITAS (monitoring):** 7-day-post-deploy GSC URL inspection on the 5 backlinks-bearing URLs to confirm equity transfer; 30-day post-deploy crawl re-run via Screaming Frog.

## Verification plan
- Day 0: Mike applies all 26 redirects in Shopify admin.
- Day 1: VERITAS spot-checks 5 sample redirects via live HEAD request and Firecrawl scrape; confirms each returns 301 and lands on intended destination.
- Day 7: VERITAS pulls GSC URL inspection on the 5 backlinks-bearing URLs; confirms canonical = destination.
- Day 30: VERITAS runs Screaming Frog crawl on the property; confirms zero of the 26 source URLs surface as 404 in the new crawl.

## Sources cited
- GSC 404 sample 2026-05-08, 1,000 URLs returned per GSC chart.
- `deliverables/tracking/sitemap-state.md` for destination verification.
- Majestic backlink report 2026-04-15 for backlink counts per URL.

## Open flags for ORIN and Mike
- Sample-vs-full-set caveat: GSC reports approximately 13,000 to 14,000 daily affected pages per the GSC chart; the 1,000-URL sample is a partial picture. The 16 systemic patterns in the 2026-05-08 404 deliverable cover most of the rest. Recommend re-pulling the GSC 404 sample after this deliverable ships to size the residual.
```

## Worked example 3: Sitemap configuration audit

Scope: audit the live Shopify sitemap.xml index and child chunks against admin inventory; surface gaps as VERITAS investigation surfaces.

```
# Sitemap Configuration Audit: Public Sitemap vs Admin Inventory

- **Date:** 2026-05-08
- **Author:** VERITAS (rebuilt from ORIN's 2026-05-08 sitemap-state refresh)
- **Audience:** Mike (review), VERITAS (investigation)
- **Severity:** Medium (crawl-budget and discoverability gap, not traffic-recovery)
- **Confidence:** High (sitemap chunks parsed by `scripts/_build_sitemap_state.py`; admin counts from Mike 2026-05-08 reference)

## Summary
The public Shopify sitemap surfaces 662 collections and 13,611 products. The admin inventory shows 1,077 collections (38.5% gap) and 15,381 products (11.5% gap). Both gaps are above the 10% tolerance band ProSoccer treats as routine and need investigation. Estimated investigation effort: 4 hours VERITAS (collection gap is largely explainable per ORIN's 2026-05-08 reconciliation; product gap needs a fresh metafield-aware admin export from Mike to distinguish Online Store sales-channel toggle from SEO-Hidden metafield).

## Current state
- Sitemap chunks: `sitemap.xml`, `sitemap_collections_1.xml`, `sitemap_products_1.xml` through `sitemap_products_7.xml`, `sitemap_pages_1.xml`, `sitemap_blogs_1.xml`, `sitemap_metaobject_pages_1.xml`, `sitemap_agentic_discovery.xml`.
- Collection count in sitemap: 662 [`scripts/_build_sitemap_state.py` parse 2026-05-08].
- Collection count in admin: 1,077 per Mike's reference 2026-05-08.
- Collection gap explanation per ORIN 2026-05-08 reconciliation: 382 `group_*` auto-collections + 32 unpublished + 1 real residual (`backyard-soccer-goals-and-rebounders`).
- Product count in sitemap: 13,611 [same parse].
- Product count in admin: 15,381 per Mike's reference 2026-05-08.
- Product gap: 1,770 products in admin not in sitemap. Cause not yet attributable per current 8-column XLSX export (can't distinguish Online Store sales-channel toggle vs SEO Hidden metafield).
- The collection gap is fully explained.
- The product gap requires a fresh export from Mike with Published Scope, Tags, and metafield columns to attribute.

## Recommended fixes
1. **Reconcile collection gap finding.** Document the 382 auto-collections, 32 unpublished, 1 real residual in `deliverables/tracking/sitemap-state.md`. Flag the 1 residual for Mike's review (publish or de-list decision). Implementer: Mike (decision); VERITAS (documentation). Time estimate: 30 minutes. Priority: Low.

2. **Pull fresh metafield-aware admin product export.** Mike re-exports from Shopify admin with Published Scope, Tags, and metafield columns added. Implementer: Mike. Time estimate: 30 minutes. Priority: Medium (gates the product gap attribution).

3. **Attribute product gap once fresh export lands.** With the fresh export, classify the 1,770-product gap into Online Store sales-channel toggled (intentional) vs SEO Hidden metafield (intentional) vs unintentional. Implementer: VERITAS. Time estimate: 2 hours. Priority: Medium. Verification: every product in the gap maps to an explicit cause; the residual unattributed count is documented and flagged for further investigation.

## Implementer routing summary
- **Mike (admin export, decisions on the 1 residual collection):** fixes 1 (decision), 2.
- **VERITAS (sitemap-state documentation, product gap attribution):** fixes 1 (documentation), 3.

## Verification plan
- Day 0: Mike pulls fresh export.
- Day 1: VERITAS attributes the 1,770-product gap.
- Day 2: VERITAS updates `deliverables/tracking/sitemap-state.md` with both gap reconciliations.
- Day 7: VERITAS confirms downstream impact: any unintentional gaps that should have been in the sitemap get a fix proposal in the next sitemap-config deliverable.

## Sources cited
- Sitemap chunks parsed 2026-05-08 by `scripts/_build_sitemap_state.py`.
- Mike's admin reference 2026-05-08 (1,077 collections, 15,381 products).
- ORIN's 2026-05-08 collection-gap reconciliation in `deliverables/tracking/sitemap-state.md`.

## Open flags for ORIN and Mike
- Locale variants (en-au, en-ca, en-gb, en-es) surfaced in the sitemap chunks need a separate VERITAS hreflang investigation; not in scope for this audit.
- The `sitemap_agentic_discovery.xml` chunk is a Shopify-emitted file VERITAS hasn't inventoried; flag for next-pass investigation.
```

## How this playbook integrates with the six copy-writing principles

The six principles in `context/03-brand-voice.md` and `.claude/agents/on-page-seo/agent.md` Section 7 govern customer-facing copy quality. Technical deliverables don't carry customer-facing copy. The principles still apply to deliverable PROSE (the summary, the open-flags section, the verification plan) for consistency:

- No em-dashes, no forbidden words from the voice-check list, contractions encouraged in prose.
- Lead with the noun in deliverable summaries.
- One idea per sentence in fix descriptions.
- The "Human, Not AI" Test still applies; technical deliverables shouldn't read like generated boilerplate.

What does NOT apply:

- 'Emotional Connection Over Feature Selling' is not a technical-deliverable rule. Technical specs are feature-led by definition.
- 'Full-Avatar-Scope Discipline' is not a technical-deliverable rule. The reader is the implementer, not an avatar.
- 'Business Context Anchor' applies to positioning copy, not redirect maps. Technical deliverables cite ProSoccer-specific state (URLs, schema, theme paths) but don't lean on heritage / geographic moat / curation difference.

In short: technical deliverables are spec documents, not marketing copy. Voice rules cover the prose; the substance is exact technical specification.
