# Phase 2 Task 3: Legacy Magento URL Audit

**Session date:** 2026-04-21
**Status:** Confirmation document. No action required.

## Objective

Verify no legacy Magento URLs from the 2021-to-2022 Magento-to-Shopify-Plus migration are still receiving traffic or causing SEO issues in current Google Search Console data.

## Method

Greped `data/gsc-exports/2025-04-to-2026-04_top-pages.csv` (12-month window) for common Magento URL patterns:

- `/index.php`
- `/catalog/product`
- `/catalog/category`
- `.html` suffixes on collection paths
- `?id=` and other Magento-style query parameters
- literal `magento`

Case-insensitive, full-path match.

## Result

**Zero matches.** No legacy Magento URLs are receiving impressions or clicks from Google in the 12-month GSC window.

## Interpretation

Two explanations are consistent with the data. Either the 2021-to-2022 migration cleanup was thorough enough that no legacy URLs survived in the index, or Google has long since dropped any lingering Magento URLs from the index through natural crawl decay. Either way, the surface-level outcome is the same: no legacy-URL traffic is leaking today, and no cleanup debt is visible in GSC.

A full redirect-map verification (pulling historical Magento URLs from Ahrefs or the old sitemap and HEAD-checking each) would catch any broken 301s on external backlinks that Google has already stopped surfacing. That's a deeper audit and is not where the February 2026 re-engagement should spend hours. The GSC-surface claim stands without it.

## Follow-up

None. This line item is closed.
