# Phase 2 Task 1: National Team Collection Inventory

**Session date:** 2026-04-21
**Method:** HTTP status sweep of 34 candidate URLs + Shopify collections sitemap lookup + Node HTML parse of 38 actual collection pages. Raw JSON at `data/crawl-2026-04-21_national-team-collections.json` and `_retry.json`. Crawl scripts in `scripts/`.

## Headline Finding

Mike's 20 candidate URL patterns were wrong. Actual Shopify slug pattern is `/collections/{country}` (single slug, no `-soccer-jerseys` suffix). Only 2 of 34 candidate URLs returned 200: `/collections/2026-fifa-world-cup` and `/collections/holland` (which 301-redirects from `/collections/netherlands`).

From the collections sitemap (655 total collections), I found **21 main country landing pages** (single-slug pattern), **3 USA variants** (cannibalization risk, see below), **7 legacy long-slug pages** on the `{country}-national-soccer-team-jerseys-apparel` pattern, plus **~30 sub-collection pages** under `{country}-jerseys`, `{country}-t-shirts`, `{country}-hoodies`, `{country}-hats`, and `mexico-pants`.

Ecuador and Peru do NOT have collection pages at any slug.

## Inventory Table

Columns: Title char count, H1, DOM product-card count (heuristic), WC2026 mention in HTML, schema types present, state assessment.

| URL | Title chars | H1 | Products | WC2026 | Schema | State |
|---|---|---|---|---|---|---|
| /collections/2026-fifa-world-cup | 58 | 2026 FIFA World Cup Fan Gear | 43 | Yes | CollectionPage, Organization | heavily optimized hub |
| /collections/mexico | 71 | Mexico National Soccer Team Jerseys, Apparel & Gear | 45 | Yes | CollectionPage, Organization | heavily optimized (WC template) |
| /collections/argentina | 74 | Argentina National Soccer Team Jerseys, Apparel & Gear | 45 | Yes | same | heavily optimized |
| /collections/brazil | 64 | Brazil National Soccer Team Jerseys, Apparel & Gear | 44 | Yes | same | heavily optimized |
| /collections/england | 65 | England National Soccer Team Jerseys, Apparel & Gear | 44 | Yes | same | heavily optimized |
| /collections/germany | 72 | Germany National Soccer Team Jerseys, Apparel & Gear | 45 | Yes | same | heavily optimized |
| /collections/france | 71 | France National Soccer Team Jerseys, Apparel & Gear | 44 | Yes | same | heavily optimized |
| /collections/portugal | 66 | Portugal National Soccer Team Jerseys, Apparel & Gear | 44 | Yes | same | heavily optimized |
| /collections/spain | 63 | Spain National Soccer Team Jerseys, Apparel & Gear | 46 | Yes | same | heavily optimized |
| /collections/italy | 63 | Italy National Soccer Team Jerseys, Apparel & Gear | 42 | Yes | same | heavily optimized |
| /collections/netherlands | 76 | Netherlands National Soccer Team Jerseys, Apparel & Gear | 42 | Yes | same | heavily optimized (title over 70) |
| /collections/colombia | 73 | Colombia National Soccer Team Jerseys, Apparel & Gear | 46 | Yes | same | heavily optimized |
| /collections/uruguay | 66 | Uruguay National Soccer Team Jerseys, Apparel & Gear | 20 | Yes | same | heavily optimized, thin inventory |
| /collections/japan | 63 | Japan National Soccer Team Jerseys, Apparel & Gear | 20 | Yes | same | heavily optimized, thin inventory |
| /collections/croatia | 72 | Croatia National Soccer Team Jerseys and Gear | 11 | Yes | same | heavily optimized, thin |
| /collections/austria | 72 | Austria National Soccer Team Jerseys, Apparel & Gear | 10 | Yes | same | heavily optimized, thin |
| /collections/belgium | 65 | Belgium National Soccer Team Jerseys & Gear | 30 | Yes | same | heavily optimized |
| /collections/canada | 71 | Canada National Soccer Team Jerseys, Apparel & Gear | 35 | Yes | same | heavily optimized |
| /collections/morocco | 61 | Morocco National Soccer Team Jerseys, Apparel & Gear | 8 | Yes | same | optimized, thin inventory |
| /collections/switzerland | 76 | Switzerland National Soccer Team Jerseys, Apparel & Gear | 8 | Yes | same | optimized (title over 70), thin |
| /collections/norway | 73 | Norway National Soccer Team Jerseys, Apparel & Gear | 20 | Yes | same | optimized (title over 70) |
| /collections/south-korea | 74 | South Korea National Soccer Team Jerseys, Apparel & Gear | 18 | Yes | same | optimized (title over 70, diff template) |
| /collections/jamaica | 84 | Jamaica National Soccer Team Jerseys, Apparel & Gear | 30 | Yes | same | optimized but title 84 chars (SERP truncation) |
| /collections/guatemala | 55 | Guatemala Soccer Jerseys and Fan Gear | 38 | Yes | same | optimized (diff template, no WC hook in title) |
| /collections/el-salvador | **29** | **El Salvador** | 42 | Yes | same | **BROKEN: default title, empty meta description, bare H1** |
| /collections/honduras | **26** | **Honduras** | 6 | Yes | same | **BROKEN: default title, empty meta, bare H1, 6 products** |
| /collections/chile | 429 | — | — | — | — | Cloudflare rate-limited during crawl; retry next session |
| /collections/united-states-men | **88** | United States Men | 45 | Yes | same | optimized (title 88 over limit); H1 too thin |
| /collections/united-states-men-women | 68 | USA National Soccer Team Jerseys, Apparel & Gear | 45 | Yes | same | heavily optimized (this is the URL that ranks, barely) |
| /collections/united-states-women | **90** | United States Women \| USA Women's Soccer Jerseys, Apparel & Gear | 50 | Yes | same | optimized but title 90 chars |
| /collections/algeria-national-soccer-team-jerseys-apparel | 67 | Algeria National Soccer Team Jerseys & Apparel | 4 | Yes | same | optimized long-slug legacy page, 4 products |
| /collections/ghana-national-soccer-team-jerseys-apparel | 65 | Ghana National Soccer Team Jerseys & Apparel | 6 | Yes | same | same pattern |
| /collections/senegal-national-soccer-team-jerseys-apparel | 67 | Senegal National Soccer Team Jerseys & Apparel | 6 | Yes | same | same pattern |
| /collections/sweden-national-soccer-team-jerseys-apparel | 66 | Sweden National Soccer Team Jerseys & Apparel | 8 | Yes | same | same pattern |
| /collections/new-zealand-national-soccer-team-jerseys-apparel | 64 | New Zealand National Soccer Team Jerseys & Apparel | 6 | Yes | same | same pattern |
| /collections/scotland-national-soccer-team-jerseys-apparel | 68 | Scotland National Soccer Team Jerseys & Apparel | 2 | Yes | same | same pattern, only 2 products |
| /collections/australia-national-soccer-team-jerseys-apparel | 69 | Australia National Soccer Team Jerseys & Apparel | 8 | Yes | same | same pattern |
| /collections/usa-national-soccer-team-denim-apparel | 58 | USA National Soccer Team Denim Apparel | 10 | Yes | same | not-MNT; USA-themed denim sub-collection |

## Patterns Worth Flagging

**Three title templates in active use**, none consistently applied:
- Template A: `{Country} World Cup 2026 Fan Gear | Prosoccer.com – ProSoccer` — used on 17 pages
- Template B: `{Country} Soccer Jerseys | Official National Team Gear – ProSoccer` — used on South Korea, Jamaica
- Template C: `{Country} Soccer Jerseys & Gear | Prosoccer.com – ProSoccer` — used on all 7 long-slug legacy pages
- Template D (default Shopify, broken): `{Country} – ProSoccer` — el-salvador, honduras

**USMNT cannibalization.** Three near-identical URLs all returning ~45 products with overlapping H1s and schema:
- `/collections/united-states-men` (title 88ch, thin H1 "United States Men")
- `/collections/united-states-men-women` (this is the one that ranks, at position 45.84)
- `/collections/united-states-women` (title 90ch)
Plus `/collections/usa-national-soccer-team-denim-apparel` as a denim sub-angle.
Plus five apparel sub-collections: `/collections/usa-jerseys`, `/collections/usa-t-shirts`, `/collections/usa-hoodies`, `/collections/usa-hats`.
Plus one long-slug: `/collections/usa-national-soccer-team-denim-apparel`.
Google is almost certainly splitting link equity across these. Consolidation to one canonical URL with 301s should come BEFORE any USMNT sprint work.

**Leftover theme-migration duplicates.** `/collections/spain-jerseys-copy` and `/collections/france-hats-copy` exist in the live collections sitemap. Both are stale "copy" variants left over from someone duplicating collections during the late-2025 theme migration. They need canonical review and likely removal or noindex.

**Netherlands / Holland redirect.** `/collections/netherlands` still gets 103 clicks / 19,078 impressions in Q1 2026 despite being a 301 to `/collections/holland`. Users and bots are hitting the legacy URL, the redirect is in place, and both positions are healthy. No action needed but worth knowing.

**Missing pages.** Ecuador and Peru do NOT have collection pages. If either has GSC signal on queries, that is a net-new page opportunity, not an optimization one.

## WC2026 Mention: Universal, Not Always in Title

Every page I successfully crawled returned `wcMention=true`. That reflects site-wide hub links in nav or footer rather than deep WC2026 content on the page body. Pages with WC2026 in the title template (A) are the ones positioned for the sprint; pages without it in the title (Guatemala, South Korea, Jamaica, the legacy long-slug pages, and the two broken pages) are getting surface-level WC association only.

## Schema Consistency

Every successful crawl returned `CollectionPage` + `Organization` JSON-LD. No page returned BreadcrumbList or ItemList schema at the top-level JSON-LD pass my parser caught. That is a likely miss; full schema audit in Month 1 should confirm whether BreadcrumbList is present in a format my regex didn't catch, or whether it's absent everywhere.

## Data Artifacts

- `data/crawl-2026-04-21_national-team-collections.json` — main crawl (38 URLs, 37 with HTML parse)
- `data/crawl-2026-04-21_national-team-collections-retry.json` — retry of 8 rate-limited URLs (7 succeeded on retry; Chile still 429)
- `scripts/crawl-national-team-collections.js` — the crawl script
- `scripts/crawl-retry.js` — retry script with spacing
