# Data Folder

_Raw exports from SEO and analytics tools. Agents read from here. Humans (mostly Mike) write to here._

## Folders

### `gsc-exports/`

Google Search Console exports. Format: CSV.

Typical exports:

- `queries-YYYY-MM-DD.csv` - top queries report
- `pages-YYYY-MM-DD.csv` - top pages report
- `coverage-YYYY-MM-DD.csv` - index coverage
- `cwv-YYYY-MM-DD.csv` - Core Web Vitals

### `screaming-frog/`

Screaming Frog crawl exports. Format: CSV or XLSX.

Typical exports:

- `internal-html-YYYY-MM-DD.csv`
- `response-codes-YYYY-MM-DD.csv`
- `page-titles-YYYY-MM-DD.csv`
- `meta-descriptions-YYYY-MM-DD.csv`
- `h1-YYYY-MM-DD.csv`
- `structured-data-YYYY-MM-DD.csv`

### `ahrefs/`

Ahrefs exports. Format: CSV or XLSX.

Typical exports:

- `organic-keywords-YYYY-MM-DD.csv`
- `backlinks-YYYY-MM-DD.csv`
- `site-audit-YYYY-MM-DD.csv`
- `content-gap-<competitor>-YYYY-MM-DD.csv`

### `ga4-exports/`

Google Analytics 4 exports. Format: CSV.

Typical exports:

- `organic-sessions-YYYY-MM.csv`
- `landing-pages-YYYY-MM.csv`
- `conversions-YYYY-MM.csv`
- `ecommerce-YYYY-MM.csv`

## Naming Convention

All files include a date stamp in the filename: `YYYY-MM-DD` for point-in-time crawls, `YYYY-MM` for monthly aggregates.

## What Does Not Live Here

- Customer PII
- Full order history with names
- Credentials of any kind (see `.gitignore`)

## Git and Data Files

Data files (CSV, XLSX, JSON, ZIP) are ignored by git (see `.gitignore`). Only this README is tracked. Large exports stay on Mike's machine or Google Drive.
