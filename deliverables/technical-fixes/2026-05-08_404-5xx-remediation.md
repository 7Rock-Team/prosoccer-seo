# 404 and 5xx Error Remediation: Workforce Health Pass

**Date:** 2026-05-08
**Owner:** ORIN (Master Strategist), executing VERITAS-scope work in main thread
**Source data:** `data/gsc-exports/2026-05-08_404-table.csv` (1,000-URL sample from GSC UI Coverage > Not found export)
**Full set size per GSC Chart:** 13K to 14K affected pages daily (sample is approximately 7% of total)
**Companion artifacts:**
- Classified output: `data/gsc-exports/2026-05-08_404-classified.csv`
- Classifier script: `scripts/_classify_404_table.py`
- Pattern summary: `data/gsc-exports/2026-05-08_404-systemic-summary.txt`

## Headline Finding

**95.8% of the 404 sample is systemic, not one-off.** Mike does not need to add 1,000 individual redirects in Shopify admin. Sixteen distinct systemic patterns account for 958 of the 1,000 URLs. Fix the patterns, and the redirect map for individual URLs collapses to roughly 26 unique entries that Mike can implement in 15 to 20 minutes.

The systemic findings split between three implementer routes: Misha (theme or app code), Mike (single Shopify admin redirect rules that cover many URLs each), and a VERITAS hreflang investigation that needs separate scoping. None of the 1,000 sampled URLs are 5xx, since the GSC export Mike pulled is 404-specific. A 5xx review needs a separate export.

## Sample-vs-full-set caveat

This sample is the first 1,000 rows of the GSC UI Coverage export, capped at the GSC export limit. The full affected-pages count from the GSC Chart is 13K to 14K daily. The systemic-pattern percentages in this sample (95.8% systemic) should hold across the full set, but the absolute one-off count will scale: if the full set has the same 3.5% one-off rate, that's roughly 350 to 500 unique one-off URLs across the full population, not 26. The 26 unique one-offs identified here cover the most-crawled tail of the long-tail distribution; deeper pulls would surface more.

## Classification Summary

### Systemic (95.8%, 958 of 1,000): fix as patterns, not individual redirects

| Pattern | Count | Implementer | Fix type |
|---|---:|---|---|
| systemic-locale-other (`/en-XX/...` 404s, non-`/es/`) | 228 | VERITAS | Locale routing investigation; tied to hreflang follow-up |
| systemic-es-locale (`/es/...`, `/es-es/...`) | 173 | VERITAS | Spanish locale routing; non-canonical prefix |
| systemic-types-collection (`/collections/types?page=N`) | 133 | Mike + theme | Single 410 or remove all internal links to `/collections/types` |
| systemic-locale-discovery-widget (Rebuy widget on `/en-XX/`) | 99 | Misha | Rebuy app config: don't generate locale-prefixed URLs |
| systemic-asset-template-var (`{seek_to_start_number}` not substituted) | 81 | Misha | Theme bug: video template variable not interpolated |
| systemic-video-stream-app (third-party video CDN URLs) | 81 | Misha | Video app generating non-resolving stream URLs; audit app or robots.txt block |
| systemic-duplicated-locale (`/en-au/en-au/...`) | 56 | Misha | Theme bug: locale prefix duplicated in routing |
| systemic-numeric-product-id (`/products/<numeric>`) | 40 | Mike | Single rewrite rule: numeric ID URLs to handle URLs (or 410) |
| systemic-wpm-sandbox (`/wpm@.../sandbox/...`) | 26 | Misha | Web Pixel Manager sandbox URLs; needs `robots.txt` block |
| systemic-magento-legacy (`/customer/account/...`, `/catalog/...`) | 11 | Mike | Single redirect: all Magento legacy paths to `/account/login` or 410 |
| systemic-discovery-widget (Rebuy widget on canonical) | 8 | Misha | Same Rebuy app fix as locale variant |
| systemic-pagination (`?page=N` deep) | 6 | Mike + theme | Cap pagination or canonical to page 1 |
| systemic-variant-on-dead-product (5 occurrences of one ball SKU) | 5 | Mike | One redirect for the bare handle covers all variant URLs |
| systemic-blog-duplicated-path (`/blogs/footwear/footwear/...`) | 4 | Misha | Theme bug: blog path segment duplicated |
| systemic-encoded-handle (replacement char in product handle) | 4 | Mike | Source: corrupted inbound link; 410 the mangled handles |
| systemic-nested-variant-canonical (live product, nested path) | 3 | Misha | Apply rel=canonical to bare product handle |

**Subtotal: 958 URLs covered by 16 fixes.**

### One-off (3.5%, 35 of 1,000): individual redirects after dedup

After deduplicating nested-collection-product variants of the same broken handle, the actual unique URL count is **26**:

- 14 unique broken product handles (some appear at multiple `/collections/X/products/Y` paths)
- 12 non-product one-offs (Magento `.html` URLs, deprecated pages, miscellaneous junk)

### Excluded (0.7%, 7 of 1,000): Name Set products

Seven URLs match Name Set / customization-template patterns. Per prior agency configuration, these are intentionally noindexed. No remediation needed.

### Priority signal from 90-day GSC impressions

Of the 35 one-off URLs, only **1 has measurable GSC traffic in the last 90 days** (the USMNT youth jersey, 2 clicks / 61 impressions). The remaining 34 have zero recorded clicks or impressions in the 90-day window. Interpretation: the 404 surface is mostly crawl-budget waste, not active equity loss. The biggest payoff sits in the systemic fixes, not the individual redirects.

## Redirect Map: Individual URLs

Format: ready to paste into Shopify admin > Online Store > Navigation > URL Redirects.

### High priority (had GSC clicks in last 90 days)

| From URL | To URL | Reason | Priority |
|---|---|---|---|
| /products/nike-2026-27-usmnt-youth-authentic-home-nn-soccer-jersey | /collections/usa-jerseys | discontinued or unpublished USMNT youth product; 2 clicks / 61 imp last 90d | High |

### Medium priority (broken product handles, no measured GSC traffic but multiple inbound paths)

These 14 unique broken product handles surface at one or more `/collections/X/products/<handle>` paths. Adding one redirect on the bare handle covers every nested variant automatically (Shopify routes nested-collection paths through the bare handle). Verify each target collection in Shopify admin before saving.

| From URL | To URL | Reason | Priority |
|---|---|---|---|
| /products/adidas-juventus-third-club-soccer-ball | /collections/juventus | discontinued ball SKU; appears in 5 collection paths | Medium |
| /products/addias-24-referee-jersey | /collections/referee | typo handle ("addias"); appears in 3 collection paths; corrected handle not present in sitemap, route to parent collection | Medium |
| /products/nike-zm-superfly-10-elite-fg-shadow-pack-fa24 | /collections/nike-shadow-pack-fa24 | typo handle ("zm" should be "zoom"); appears in 3 paths; route to parent pack collection | Medium |
| /products/adidas-f50-elite-fg-messi-truinfo-estelar-messi-pack-ho24 | /collections/adidas-triunfo-estelar-messi-pack | typo ("truinfo" should be "triunfo"); appears in 2 paths; route to canonical pack collection | Medium |
| /products/adidas-bayern-munich-third-club-soccer-ball | /collections/bayern-munich | discontinued ball SKU | Medium |
| /products/adidas-real-madrid-home-club-soccer-ball | /collections/real-madrid | discontinued ball SKU | Medium |
| /products/adidas-2023-mls-league-nfhs-size-4-ball-and-bag-bundle-1 | /collections/adidas-2024-mls-balls | superseded by 2024 MLS bundle | Medium |
| /products/nike-zoom-vapor-15-elite-fg-black-smoke-grey | /collections/nike-mercurial | discontinued cleat | Medium |
| /products/new-balance-tekela-v4-pro-rare-force-pack | /collections/new-balance-tekela | discontinued pack | Medium |
| /products/kwik-goal-futsal-clipboard | /collections/kwik-goal-products | discontinued accessory | Medium |
| /products/tf-bra-15 | (410) | malformed handle, no clear referent | Low |
| /products/new- | (410) | truncated handle (broken inbound link) | Low |
| /products/kwik-goal-kwik- | (410) | truncated handle (broken inbound link) | Low |
| /products/gared-touchline*-* (4 SKUs with replacement char) | (410) | encoding-corrupted handles (™ symbol mangled in URL); already grouped under systemic-encoded-handle | Low |

### Low priority (other one-offs)

| From URL | To URL | Reason | Priority |
|---|---|---|---|
| /pages/shop-instagram | /pages/about-us | deprecated Instagram shop page | Low |
| /apparel/ym.html | /collections/youth-apparel | Magento youth apparel category | Low |
| /equipment/shoe_care.html | /collections/leather-conditioner | Magento shoe-care category | Low |
| /equipment/linesman_flags.html | /collections/referee-accessories | Magento linesman-flag category | Low |
| /shop-goalkeeper-apparel/shorts.html | /collections/goalkeeper-shorts | Magento GK-shorts category | Low |
| /footwear/women-s-soccer-shoes.html | /collections/womens-soccer-cleats-shoes | Magento women's-shoes category | Low |
| /footwear/adult/lacrosse.html | (410) | lacrosse, out of catalog scope | Low |
| /nike-2020-21-nigeria-home-jersey-white-green.html | /collections/national-teams | Nigeria not a separate collection in current sitemap | Low |
| /nike-2021-22-psg-df-pre-match-jersey-black.html | /collections/paris-saint-germain | discontinued PSG SKU | Low |
| /nike-phantom-gt-elite-df-fg-black-red.html | /collections/nike-phantom | discontinued Phantom GT SKU | Low |
| /localization | (no fix) | Shopify localization endpoint; verify whether this is supposed to resolve | Low |
| /sikph.html.hu (HTTP, not HTTPS) | (410) | random crawler junk; HTTP-only scheme | Low |

**Total individual redirect entries: 26 unique URLs.**

## Systemic Findings: Misha-Routed (theme or app)

These need code or app-config changes, not Shopify admin URL Redirects. Routed to Misha for theme repo work. ORIN can draft Liquid or schema changes into `deliverables/technical-fixes/` if Mike requests follow-up.

### 1. Asset template variable not substituted (81 URLs)

Pattern: `https://www.prosoccer.com/assets/video/<hash>.mp4?t={seek_to_start_number}`

The literal string `{seek_to_start_number}` appears in URLs that should resolve to numeric values. A Liquid template variable isn't being interpolated. Likely root cause: a video player block in the theme is rendering its template variable raw instead of evaluating it. Misha to grep for `{seek_to_start_number}` and `{seek_to_start_time}` in `prosoccer/sections/`, `prosoccer/snippets/`, and any video-related blocks.

### 2. Third-party video stream app generating non-resolving URLs (81 URLs)

Patterns: `/content/stream/*.mp4`, `/v/media/storage/*.mp4`, `/static/uploads/v/*.mp4`, `/assets/content/v/*.mp4`, `/upload/media/video/*.mp4`, `/media/mp4/*.mp4`, `/assets/video/*.mp4`, `/assets/mp4/v/*.mp4`, `/public/video/*.mp4`, plus `/player?id=N`. Eight distinct path prefixes, all 404, all video-themed.

This pattern matches a third-party storefront video app (Reels-style or product-video integration) that generates many path variants for the same video, only one of which actually serves. Misha to identify which app is installed (look in Shopify admin > Apps for video / reels / Tolstoy / Videowise / Vimeo Shopify), then either: (a) configure the app to suppress non-canonical URLs, or (b) add `Disallow:` rules in `robots.txt` for the affected path prefixes.

### 3. Duplicated locale prefix (56 URLs)

Pattern: `/en-au/en-au/products/...`, `/en-ca/en-ca/...`, etc.

The locale prefix is being prepended twice. Likely root cause: a Liquid filter or third-party translation app (Langshop, Weglot) is double-applying its prefix when the request already carries a locale cookie. Misha to check the language switcher snippet and any `linklist` filters for double `localize_url` invocations.

### 4. Rebuy Discovery widget × locale routing (99 URLs locale-prefixed + 8 canonical = 107 total)

Pattern: query string contains `_rdiscovery-handle=...&_rdiscovery-widget=...`, often with `variant=...`. The Rebuy Smart Recommendations / Discovery app generates these URLs as click destinations from its widget; on locale-prefixed paths they 404 because Rebuy doesn't know how to localize. Misha to either: (a) enable the locale-aware setting in Rebuy admin, or (b) add `Disallow: *_rdiscovery-handle=*` to `robots.txt`.

### 5. Web Pixel Manager sandbox URLs indexed (26 URLs)

Pattern: `/wpm@<version>@<hash>w<hash>p<hash>m<hash>/web-pixel-shopify-custom-pixel@<id>/sandbox/products/<handle>`

Shopify's Web Pixel Manager exposes Custom Pixel sandbox URLs that should never be indexed. Misha to add `Disallow: /wpm@*` in `robots.txt` and add `<meta name="robots" content="noindex">` if the sandbox view is theme-renderable.

### 6. Blog path segment duplicated (4 URLs)

Pattern: `/blogs/footwear/footwear/best-nike-soccer-cleats`. Blog category appears twice in the path. Same theme-bug class as the duplicated-locale issue. Misha to grep for blog-link generation in section/snippet files.

## Systemic Findings: Mike-Routed (Shopify admin URL Redirects)

These can be fixed in Shopify admin without theme changes. Each entry is a single rule that covers many URLs.

### 1. `/collections/types?page=N` (133 URLs)

`/collections/types` doesn't exist as a real collection but pagination links to `?page=1` through `?page=400+`. Source: an internal link or sitemap reference treats `/collections/types` as a real route. Two-step fix:

1. Audit theme: search `prosoccer/` repo for any internal link to `/collections/types`. Replace with a real collection or remove.
2. In Shopify admin URL Redirects: add `/collections/types` redirect (target: `/collections/all` or 410). The redirect catches the bare path and Shopify's pagination handler returns the same target for all `?page=N` variants.

### 2. Numeric Shopify product ID URLs (40 URLs)

Pattern: `/products/9458073075967` (purely numeric path). These are Shopify internal product IDs leaking into search results, possibly from a third-party app or old Shopify Markets configuration that generates ID-based URLs.

In Shopify admin URL Redirects, individual entries don't scale (40 redirects in the sample, likely 500+ in the full 13K). Two-path fix:

1. **Preferred:** Misha or Mike investigates root source. If a single app is generating these URLs (check apps that integrate with the storefront, e.g., Recharge, Bold, Aftership), disable that URL pattern. Alternatively: add a Liquid redirect rule in `theme.liquid` that catches `/products/<numeric>` and 301s to the corresponding handle URL using the Shopify product API.
2. **Bandaid:** add `Disallow: /products/[0-9]*$` in `robots.txt` so Google stops crawling new ID URLs while the root cause is resolved.

### 3. Magento legacy paths (11 URLs)

Patterns: `/customer/account/login/referer/<base64>`, `/catalog/product_compare/...`, `/catalog/product/view/...`. Old Magento 1 URLs still being crawled, likely from external backlinks or stale third-party site indexes.

In Shopify admin: add four URL redirect rules covering the path prefixes:

| From | To |
|---|---|
| `/customer/account/login` (and any path beneath) | `/account/login` |
| `/catalog/product/view` (any beneath) | `/products` (Shopify auto-handles unknown product IDs as soft-404; 410 is also acceptable) |
| `/catalog/product_compare` (any beneath) | `/` |
| `/catalog/category/view` (any beneath) | `/collections` |

### 4. Deep pagination (6 URLs)

`?page=395+` on real collections is wasted crawl budget (no products that deep). Misha to add `<link rel="canonical" href="/collections/<handle>">` on paginated collection pages where `page > 10`, or use Shopify's built-in `paginate by` to cap pagination at the actual product count.

## Systemic Findings: VERITAS-Routed (locale and hreflang investigation)

### Locale-prefixed 404s (228 + 173 = 401 URLs combined)

Two patterns:

- `systemic-es-locale` (173): `/es/`, `/es-es/`, `/es-mx/`, `/es-co/` paths returning 404. ProSoccer's canonical Spanish locale prefix is `/en-es/`. Either inbound links or app integrations are generating non-canonical Spanish prefixes.
- `systemic-locale-other` (228): `/en-XX/` paths returning 404 for various reasons (deprecated handles, locale-routing failures, app-generated URLs).

This work belongs to VERITAS as part of the existing hreflang follow-up (logged in `work-log/follow-ups.md`, 2026-05-08 entry). Combined with the Rebuy × locale finding, this is the next major VERITAS work surface after the SCRIBE Mexico Wave 1 sprint completes.

Recommended VERITAS scope:

1. Enumerate the locale URL-prefix GSC properties for prosoccer.com (`en-es`, `en-au`, `en-ca`, `en-gb`) and pull their independent Coverage > Not found data.
2. Confirm what URL-generation source produces `/es/` (vs `/en-es/`) prefixes. Likely Langshop or Shopify Markets locale config.
3. Decide the canonical Spanish prefix and add bulk redirects for the non-canonical variants.
4. Audit the existing hreflang implementation: are `/en-es/` mirrors of `/en-au/`, `/en-ca/`, `/en-gb/` adequately maintained, or are they stale?

## 5xx Error State

The GSC export Mike pulled is filtered to "Not found (404)". Zero 5xx URLs are in this dataset. A 5xx review needs a separate GSC UI export (Coverage > Server error). When Mike pulls that:

- Spot-check a sample with `mcp__gsc-server__inspect_url_enhanced` to confirm current 5xx state vs transient.
- Look for path patterns. Persistent 5xx on a specific path prefix (e.g., all `/products/<vendor>-*` URLs) signals a theme or app issue routed to Misha.
- Repeat the systemic-vs-one-off classification using the same script.

The classifier in `scripts/_classify_404_table.py` works on any GSC URL list; it'll handle a 5xx CSV with a column rename or a small input adapter.

## Implementation Plan

### Mike: Shopify admin URL Redirects (15 to 20 minutes)

1. Open Shopify admin > Online Store > Navigation > URL Redirects > Add URL redirect.
2. Add the 1 High row first (USMNT youth jersey).
3. Add the 14 Medium product-handle rows (some are 410-equivalent: leave the To URL blank to remove from search; otherwise paste the suggested target).
4. Add the 12 Low rows (Magento `.html` paths and deprecated pages).
5. Add the systemic Mike-routed rules: `/collections/types`, the four Magento path prefixes, and the numeric-product-ID pattern (if a Liquid-based fix isn't deployed first).
6. Optional: skip Low-priority 410s if you'd rather let them age out naturally.

The 14 nested-product variants (e.g., `/collections/X/products/<broken-handle>`) don't need individual entries; Shopify routes them through the bare `/products/<handle>` redirect.

### Misha: theme repo work (separate scoping)

ORIN to draft theme-level fixes into `deliverables/technical-fixes/` if Mike requests follow-up. The six Misha-routed systemic patterns (asset template var, video stream app, duplicated locale, Rebuy widget, Web Pixel Manager, blog duplicated path) need investigation in the actual theme code before drafts can be precise.

Routing pattern (per CLAUDE.md): drafts go into this repo's `deliverables/technical-fixes/` folder. Mike applies them to a `mike-audit` branch on the prosoccer theme repo. Misha merges.

### VERITAS: hreflang investigation (separate phase)

Logged in `work-log/follow-ups.md`, 2026-05-08 entry. Next major VERITAS work surface after Mexico Wave 1 sprint dispatch.

## Items needing Mike judgment

- **`/products/addias-24-referee-jersey`:** the typo correction `/products/adidas-24-referee-jersey` doesn't resolve in the current sitemap either. Is there a current adidas referee jersey on the site that this should redirect to, or should it route to `/collections/referee` as a generic catch?
- **Numeric Shopify product ID URLs (40 in sample, likely 500+ in full set):** preferred fix is a Liquid redirect rule in the theme rather than 500 individual URL Redirects. Confirm Misha can take this on, or fall back to the `robots.txt` bandaid.
- **`/collections/types`:** confirm this isn't an active Mike-built collection that should resolve. If it is, ORIN can investigate why the handle isn't in the sitemap; if it isn't, the 410 stands.
- **Video stream app:** which app is installed (Reels, Tolstoy, Videowise, Vimeo Shopify, etc.)? The app identity determines whether the fix is config-side or robots.txt.
- **Pulling more 404 data:** the 13K-14K full set is roughly 13x this sample. The systemic-vs-one-off ratio should hold, but the long-tail one-off count grows. Worth one more GSC UI export with a different sort (oldest crawl date, or grouped by path prefix) to surface any patterns hiding in the unsampled tail.

## Self-verification checklist

- All 30 redirect target URLs verified against `deliverables/tracking/sitemap-state.md`. One target (`/collections/nigeria`) was rejected and fell back to `/collections/national-teams`.
- Name Set patterns (7 URLs in sample) excluded from the actionable redirect map per prior agency configuration.
- Priority assignments in the redirect map are grounded in 90-day GSC impressions data (`mcp__gsc-server__get_advanced_search_analytics` results, 2026-02-08 to 2026-05-08).
- Misha-routed items (theme or app code) are flagged in their own section, separate from Mike-routed items (Shopify admin URL Redirects).
- VERITAS-routed work (locale and hreflang) is flagged in its own section and tied to the existing follow-up entry.
- 5xx data not in the source export; gap documented and a path for Mike to pull it is included.
- Sample-vs-full-set caveat surfaced at top.
