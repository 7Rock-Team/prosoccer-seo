# Shopify Data Exports

Sales data exports from Shopify for ProSoccer, scoped to online web channels only (Online Store, Shop, Tapcart, BSS B2B, Redo). Excludes Point of Sale, Channable (Amazon/eBay), and Draft Orders.

## Purpose

Raw sales data used by agent sessions for category prioritization, keyword research, and monthly reporting. Files are gitignored per the project's data hygiene policy (raw data stays local, only documentation tracks in git).

## Expected Files (not tracked in git)

These files should exist locally for agent sessions to read. Re-export from Shopify if missing.

### 12-month files (April 2025 to April 2026)

- `sales-by-product-type.csv`: revenue by product type
- `sales-by-product.csv`: revenue by individual product
- `sales-by-month.csv`: monthly revenue trend

### Quarterly files (existing baseline data)

- `Total sales by sales channel - YYYY-QQ.csv`: channel breakdowns per quarter
- `Total sales by referrer - YYYY-QQ.csv`: referrer breakdowns per quarter

Referrer files contain the "search/google" rows which are the organic Google traffic baseline for SEO work.

## Data Scope

- Date range: April 2025 to April 2026 (for the 12-month files)
- Sales channels included: Online Store, Shop, Tapcart, BSS B2B, Redo (web channels only)
- Excluded: Point of Sale, Channable (Amazon/eBay), Draft Orders
- Filter rule: always exclude POS, Channable, and Draft Orders when analyzing SEO performance

## How Agents Use This Data

When analyzing performance, agents filter to Online Store channel first, then segment by referrer (organic search vs other). The 12-month files are the primary input for the Keyword Research Agent's Category Priority Matrix.