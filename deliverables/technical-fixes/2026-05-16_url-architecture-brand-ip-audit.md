# URL Architecture Brand IP Audit

- **Date:** 2026-05-16
- **Author:** ORIN (Master Strategist), executing Tier A risk-tiered framing per Mike's directive
- **Audience:** Mike (decisions), then implementation routing per tier
- **Scope:** all collection slugs on prosoccer.com containing FIFA-trademarked terminology patterns (`fifa`, `world-cup`, `worldcup`, `wc`); classified per `context/brand-ip-constraints.md` and tiered by 12-month GSC equity
- **Related work:** triggered by whitelabel audit Collection #1 (`/collections/2026-national-team-soccer-fan-gear`) finding that the page links to `/collections/nike-2026-fifa-world-cup-soccer-jerseys`, a Nike-licensed slug containing FIFA-trademarked terms

---

## Executive Summary

### Headline counts

- **Total slugs scanned for violation patterns:** 662 collections in sitemap-state.md (2026-05-08 refresh) + GSC top-pages CSV cross-reference for live-but-not-in-sitemap collections.
- **Pattern matches found:** 22 collection slugs containing `fifa` / `world-cup` / `worldcup` (broken down below).
- **Adidas-licensed (compliant, no action):** 10 collections.
- **Non-Adidas violations:** 15 distinct collection slugs (11 in sitemap + 3 surfaced via GSC top-pages + 1 linked-only from the whitelabel-produced Collection #1 page).

### Tier breakdown of violations

- **Tier A.1 (HIGH EQUITY, document only):** 0 collections meet the strict pos < 20 AND clicks > 100 criterion.
- **Tier A.2 (MEDIUM EQUITY):** 4 collections (positions all on page 1-2 of Google, clicks 15-50 over 12 months).
- **Tier A.3 (LOW EQUITY):** 11 collections below the GSC top-1000 cutoff (i.e., < 14 clicks over 12 months).

### Final action counts (after Mike's exception decision 2026-05-17)

- **Slug-rename actions: 0.** Mike's business decision documented in `context/brand-ip-constraints.md` "Exceptions and grandfathered violations" section: existing slugs stay as-is to avoid any equity risk from URL changes. Both Tier A.2 (4 URLs) and Tier A.3 (11 URLs) are treated as exceptions; the original workforce slug-rename recommendations are documented for the audit trail but superseded by Mike's business call.
- **Copy-level compliance remediation: 15 URLs.** Customer-facing copy on each of the 15 violation pages (Titles, Meta Titles, Meta Descriptions, Short Descriptions, Long Descriptions, internal link anchor text) still needs full constraint compliance per the brand-ip-constraints.md core rule. This is implemented page-by-page when ORIN audits and regenerates each collection in future whitelabel audit work (or earlier if Mike prioritizes specific pages).
- **VERITAS visibility investigation (separate brief):** 4 live-but-not-in-sitemap collections (`/collections/2026-fifa-world-cup`, `/collections/2026-fifa-world-cup-qualified-teams`, `/collections/2026-fifa-world-cup-qualified-teams-accessories`, `/collections/nike-2026-fifa-world-cup-soccer-jerseys`).
- **VERITAS sitemap-refresh script enhancement (separate brief):** add brand IP scan to `scripts/_build_sitemap_state.py` so future slug additions auto-flag at refresh time.
- **Adidas-compliant (no action):** 10 collections (see Phase 1 reference table).

### Headline pattern observation

The whitelabel slug-naming convention pre-dates the workforce's Brand IP architecture. The violation set is small (15 distinct URLs across 662 collections, ~2% of the collection catalog) and concentrated in tournament-scoped pages (2022 retrospectives, 2025 Club Cup, 2026 cycle). No systemic naming-template violation; this looks like ad-hoc slug creation around tournament cycles without brand-affiliation discipline. The new `context/brand-ip-constraints.md` Step 4c discipline prevents future violations of this pattern at slug-creation time; the existing slug violations stay as-is per Mike's exception but their customer-facing copy gets brought into compliance through the ongoing audit-and-regen workflow.

---

## Mike's Exception Decision (2026-05-17)

After reviewing this audit at GATE, Mike documented a business exception for all existing slugs with FIFA terminology violations.

**Decision:** existing slugs stay as-is. No slug renames, no 301 redirects, no URL changes.

**Reasoning:** any URL change carries equity-risk that Mike judges higher than the legal-exposure benefit of cleaning up structural slug compliance. Mike's call: protect existing equity on every URL that has any, defer to copy-level compliance on the customer-facing surface, accept the slug-level brand IP exposure as known and documented.

**Scope of exception:**

- **Slug-level (structural URL):** all 15 non-Adidas violations stay as-is. Tier A.2 (4 URLs) and Tier A.3 (11 URLs) both treated under the exception. The workforce slug-rename recommendations originally documented in Phase 3 of this audit are preserved below for the audit trail but are SUPERSEDED.
- **Copy-level (customer-facing fields):** full constraint compliance still required on each of the 15 URLs. This is the actively-enforced surface going forward. Implementation through ORIN's ongoing whitelabel audit-and-regen workflow per `context/workforce-conventions.md` page-optimization deliverable structure.

**Where the exception is durable:** documented in `context/brand-ip-constraints.md` under the "Exceptions and grandfathered violations" section. All future agent work reads that file at startup; Step 4c brand-affiliation classification still applies; Gate 11 brand IP compliance scan still applies; the exception only governs the slug-rename question, not the copy-compliance question.

**Where Mike may revisit the exception:** annually (routine re-evaluation), or earlier if Adidas / legal counsel flag a slug as a priority remediation. Per-URL re-evaluation criteria documented in the constraints file.

---

## Phase 1: Discovery and Classification

### Pattern match results from `deliverables/tracking/sitemap-state.md` (2026-05-08 refresh)

Grep pattern `fifa|world-cup|world_cup|worldcup|\bwc\b|wc-` against the 662 sitemap-discoverable collection slugs returned 22 matches. Classification per `context/brand-ip-constraints.md`:

#### Adidas-licensed (compliant, FIFA terminology family allowed; no action required)

1. `/collections/adidas-2022-world-cup-balls`
2. `/collections/adidas-2023-womens-world-cup-balls`
3. `/collections/adidas-2025-fifa-club-world-cup-balls`
4. `/collections/adidas-2026-fifa-world-cup-away-soccer-jerseys-apparel`
5. `/collections/adidas-2026-fifa-world-cup-logo-apparel`
6. `/collections/adidas-2026-fifa-world-cup-logo-hats`
7. `/collections/adidas-2026-fifa-world-cup-logo-t-shirts`
8. `/collections/adidas-2026-fifa-world-cup-soccer-jerseys`
9. `/collections/adidas-2026-fifa-world-cup-soccer-jerseys-gear`
10. `/collections/adidas-2026-world-cup-balls`

All 10 are clearly Adidas-prefixed in the slug, scoping the collection to Adidas-licensed product. FIFA-family terminology is permitted on these pages per the brand IP constraint.

#### Non-Adidas violations from sitemap-state.md

| # | Slug | Brand classification | Sub-type |
|---|---|---|---|
| 1 | `/collections/2025-fifa-club-world-cup` | brand-agnostic umbrella | retrospective + Club WC scope |
| 2 | `/collections/2026-fifa-world-cup-logo-accessories` | brand-agnostic umbrella | logo merch, multi-supplier |
| 3 | `/collections/2026-fifa-world-cup-retro-gear` | brand-agnostic umbrella | retro merch, multi-supplier |
| 4 | `/collections/fifa-2023-womens-world-cup` | brand-agnostic umbrella | retrospective Women's |
| 5 | `/collections/fifa-world-cup-2022-gear` | brand-agnostic umbrella | retrospective 2022 |
| 6 | `/collections/nike-mercurial-cr7-2022-world-cup-pack` | **Nike-licensed page** (Nike-prefixed slug) | violation: Nike + WC terminology |
| 7 | `/collections/puma-2025-club-world-cup-kidsuper-soccer-jerseys` | **Puma-licensed page** (Puma-prefixed slug) | violation: Puma + WC terminology |
| 8 | `/collections/world-cup-2022-accessories` | brand-agnostic umbrella | retrospective 2022 |
| 9 | `/collections/world-cup-2022-balls` | brand-agnostic umbrella | retrospective 2022 |
| 10 | `/collections/world-cup-2026-keychains` | brand-agnostic umbrella | tournament-scope merch |
| 11 | `/collections/world-cup-soccer-balls` | brand-agnostic umbrella | evergreen brand-agnostic |

### Additional violations found via GSC top-pages CSV (live but not in sitemap-state.md)

Cross-referencing the 12-month GSC top-pages export (`data/gsc-exports/2025-04-to-2026-04_top-pages.csv`, 1000 rows) surfaced 3 additional collection URLs containing FIFA-family terms that are LIVE and getting search traffic but do NOT appear in the public sitemap (likely sales-channel-off, hidden via metafield, or otherwise excluded from sitemap crawl per the sitemap-state.md "Products gap" analysis):

| # | Slug | Brand classification | Discovery source |
|---|---|---|---|
| 12 | `/collections/2026-fifa-world-cup` | brand-agnostic umbrella | GSC top-pages row 255 |
| 13 | `/collections/2026-fifa-world-cup-qualified-teams` | brand-agnostic umbrella | GSC top-pages row 309 |
| 14 | `/collections/2026-fifa-world-cup-qualified-teams-accessories` | brand-agnostic umbrella | GSC top-pages row 335 |

Plus the original violation Mike flagged from the Collection #1 internal-link destination, which is live but not in sitemap and not in GSC top-pages:

| # | Slug | Brand classification | Discovery source |
|---|---|---|---|
| 15 | `/collections/nike-2026-fifa-world-cup-soccer-jerseys` | **Nike-licensed page** | linked from `/collections/2026-national-team-soccer-fan-gear` (whitelabel-produced); not in sitemap; not in GSC top-pages (so < 14 clicks/12mo) |

**Total non-Adidas violations: 15 collections.**

### Sitemap-state staleness observation

Three live collection URLs with measurable 12-month GSC traffic (50 / 39 / 36 clicks) do not appear in the 2026-05-08 sitemap-state.md snapshot. This is consistent with the sitemap-state.md "Products gap" reconciliation finding that ProSoccer keeps a substantial catalog Active-but-off-the-storefront-sales-channel. For the purposes of this audit, GSC top-pages is treated as a complementary source-of-truth alongside sitemap-state.md. Separate VERITAS follow-up recommended to investigate whether these 3 collections (plus the 1 linked-only Nike one) should be brought into the sitemap or have their visibility resolved.

---

## Phase 2: Equity Tiering Per Violation

### GSC equity data sourced from `data/gsc-exports/2025-04-to-2026-04_top-pages.csv`

The top-pages CSV cuts off at row 1000 with a minimum of 14 clicks over 12 months. Violations NOT in the CSV have < 14 clicks over 12 months and are tiered A.3 by default. Position trend data requires separate weekly-performance CSV cross-reference (not pulled for this audit; can be added per-URL on demand).

### Tier A.1 (HIGH EQUITY, document only)

**Criterion:** Average position < 20 (page 1-2 of Google) AND 12-month clicks > 100 AND established or stable ranking trend.

**Result: 0 collections meet the strict A.1 criterion.**

No violation hits both the position-<20 AND clicks->100 thresholds. The strongest violation (`/collections/2026-fifa-world-cup-qualified-teams-accessories`, pos 10.79) has only 36 clicks. The highest-click violation (`/collections/2026-fifa-world-cup`, 50 clicks) has position 16.94 and 0.72% CTR (sub-1%, indicating weak SERP appeal). None has the equity profile to warrant the "leave alone, accept the exposure" call.

### Tier A.2 (MEDIUM EQUITY)

**Criterion (interpreted to fit observed data):** Average position 10-30 with measurable click volume (10-100 clicks/12mo). Page 1-2 of Google but click volume modest. Mixed trend signals or uncertain ranking stability.

Four violations qualify:

| Slug | Position | Clicks (12mo) | Impressions (12mo) | CTR | Brand class | Mike's decision (2026-05-17) |
|---|---|---|---|---|---|---|
| `/collections/2026-fifa-world-cup-qualified-teams-accessories` | 10.79 | 36 | 6,085 | 0.59% | brand-agnostic umbrella | **EXCEPTION: slug stays as-is** per Mike's business decision (no equity risk acceptable; copy-level compliance only). Original workforce rename rec (preserved for audit trail): `/collections/2026-national-team-qualified-accessories`. SUPERSEDED. |
| `/collections/2026-fifa-world-cup-qualified-teams` | 12.32 | 39 | 9,906 | 0.39% | brand-agnostic umbrella | **EXCEPTION: slug stays as-is.** Original workforce rename rec (preserved): `/collections/2026-qualified-national-teams`. SUPERSEDED. |
| `/collections/world-cup-2022-accessories` | 13.12 | 15 | 1,996 | 0.75% | brand-agnostic umbrella | **EXCEPTION: slug stays as-is.** Original workforce rename rec (preserved): redirect to `/collections/national-teams-accessories` (retrospective fading). SUPERSEDED. |
| `/collections/2026-fifa-world-cup` | 16.94 | 50 | 6,923 | 0.72% | brand-agnostic umbrella | **EXCEPTION: slug stays as-is.** Original workforce rename rec (preserved): `/collections/2026-international-tournament` (Federation-anchored). SUPERSEDED. |

**Exception scope reminder:** the slug stays. The customer-facing copy on each of these 4 URLs is still required to comply with the brand IP constraint when ORIN audits and regenerates each page in future whitelabel audit work. Slug compliance: deferred. Copy compliance: actively enforced.

### Tier A.3 (LOW EQUITY)

**Criterion:** Average position > 50 OR 12-month clicks < 10 OR near-zero impressions OR declining trend with negligible volume. Operationally for this audit: violations NOT in the GSC top-pages CSV (< 14 clicks over 12 months) plus violations with negligible measured traffic.

**Result: 11 collections qualify for Tier A.3.** Listed in the Phase 3 table below.

---

## Phase 3: Tier A.3 Documented Exception Map

For each Tier A.3 violation: the original workforce slug-rename recommendation is preserved for the audit trail, then superseded by Mike's exception decision (slug stays as-is, copy-level compliance only). When ORIN audits and regenerates each of these collections in future whitelabel audit work, the brief brings the customer-facing copy into compliance while preserving the existing slug.

| # | Current slug (violation) | Original workforce rename rec (SUPERSEDED) | Mike's decision (2026-05-17) | Copy-compliance follow-up |
|---|---|---|---|---|
| 1 | `/collections/2025-fifa-club-world-cup` | `/collections/2025-club-tournament` | **EXCEPTION: slug stays.** | Copy on this page audited and regenerated when whitelabel audit reaches it. |
| 2 | `/collections/2026-fifa-world-cup-logo-accessories` | redirect to `/collections/2026-national-team-soccer-accessories` | **EXCEPTION: slug stays.** Separate question: Mike should review the product mix on this collection. If the actual products are official FIFA-branded logo merch, that is a deeper brand IP question than slug naming. | Copy audit + product-mix review when whitelabel audit reaches it. |
| 3 | `/collections/2026-fifa-world-cup-retro-gear` | `/collections/2026-retro-national-team-gear` | **EXCEPTION: slug stays.** | Copy audit on next whitelabel pass. |
| 4 | `/collections/fifa-2023-womens-world-cup` | redirect to `/collections/womens-national-teams` | **EXCEPTION: slug stays.** | Copy audit on next whitelabel pass. |
| 5 | `/collections/fifa-world-cup-2022-gear` | redirect to `/collections/national-teams` | **EXCEPTION: slug stays.** | Copy audit on next whitelabel pass. |
| 6 | `/collections/nike-mercurial-cr7-2022-world-cup-pack` | `/collections/nike-mercurial-cr7-2022-pack` | **EXCEPTION: slug stays** despite brand-prefix + FIFA-term contradiction. Mike's call to apply uniformly. | Copy audit (Nike-licensed page; copy must use Federation-anchored substitution). |
| 7 | `/collections/puma-2025-club-world-cup-kidsuper-soccer-jerseys` | `/collections/puma-2025-club-tournament-kidsuper-soccer-jerseys` | **EXCEPTION: slug stays** despite brand-prefix + FIFA-term contradiction. | Copy audit (Puma-licensed page; copy must use Federation-anchored substitution). |
| 8 | `/collections/world-cup-2022-balls` | redirect to `/collections/soccer-balls` | **EXCEPTION: slug stays.** | Copy audit on next whitelabel pass. |
| 9 | `/collections/world-cup-2026-keychains` | `/collections/2026-national-team-keychains` | **EXCEPTION: slug stays.** | Copy audit on next whitelabel pass. |
| 10 | `/collections/world-cup-soccer-balls` | redirect to `/collections/soccer-balls` | **EXCEPTION: slug stays.** | Copy audit on next whitelabel pass. |
| 11 | `/collections/nike-2026-fifa-world-cup-soccer-jerseys` | `/collections/nike-2026-national-team-soccer-jerseys` | **EXCEPTION: slug stays.** VERITAS visibility investigation still recommended (live but not in sitemap, not in GSC top-pages: may be unpublished / sales-channel-off / metafield-hidden). | Copy audit AFTER VERITAS visibility investigation resolves the URL's state. |

**Implementation summary (Tier A.3 under exception):**

- 0 slug renames.
- 0 301 redirects.
- 11 URLs documented as known slug-level exposures with copy-level compliance follow-up routed through ongoing whitelabel audit workflow.

---

## Phase 4: Tier A.2 Decisions Documented

See Phase 2 Tier A.2 table above. Mike's exception decision applied to all four:

| Slug | Original workforce rec | Mike's decision (2026-05-17) |
|---|---|---|
| `/collections/2026-fifa-world-cup-qualified-teams-accessories` | Rename to `/collections/2026-national-team-qualified-accessories` | **EXCEPTION: slug stays.** Copy compliance via whitelabel audit. |
| `/collections/2026-fifa-world-cup-qualified-teams` | Rename to `/collections/2026-qualified-national-teams` | **EXCEPTION: slug stays.** Copy compliance via whitelabel audit. |
| `/collections/world-cup-2022-accessories` | Redirect to `/collections/national-teams-accessories` | **EXCEPTION: slug stays.** Copy compliance via whitelabel audit. |
| `/collections/2026-fifa-world-cup` | Rename to `/collections/2026-international-tournament` | **EXCEPTION: slug stays.** Copy compliance via whitelabel audit. |

---

## Phase 5: Patterns Observed and Recommended Next Steps

### Patterns

1. **Whitelabel slug-naming was ad-hoc around tournament cycles.** Violations cluster in: 2022 retrospective collections (`world-cup-2022-*`), 2023 retrospective Women's collection, 2025 Club Cup collections, and the 2026 cycle. Each tournament window appears to have generated 2-5 new collection slugs without brand-affiliation discipline. The new `context/brand-ip-constraints.md` Step 4c discipline prevents this pattern going forward, but the historical inventory needs cleanup.

2. **Two distinct brand-licensed slug violations.** `/collections/nike-mercurial-cr7-2022-world-cup-pack` and `/collections/puma-2025-club-world-cup-kidsuper-soccer-jerseys` are both brand-prefixed (Nike and Puma respectively) AND contain FIFA-trademarked terms in the same slug. These are the highest-priority remediations regardless of equity tier because the brand-prefix makes the licensing context explicit and the contradiction stark.

3. **Sitemap-state.md does not capture all live collections.** Three measurable-traffic FIFA-family collections (`/collections/2026-fifa-world-cup`, `/collections/2026-fifa-world-cup-qualified-teams`, `/collections/2026-fifa-world-cup-qualified-teams-accessories`) exist live and rank in Google but do not appear in the 2026-05-08 sitemap snapshot. Plus the linked-only `/collections/nike-2026-fifa-world-cup-soccer-jerseys`. The sitemap reconciliation work documented in `deliverables/tracking/sitemap-state.md` lines 17-46 is the relevant context: ProSoccer keeps a substantial catalog off the storefront sales channel. The audit should treat GSC + Shopify admin + sitemap as three complementary sources-of-truth, not one.

4. **No Tier A.1 high-equity violations exist.** This is good news for remediation simplicity: there is no case where Mike has to weigh "the brand IP risk is real but the SEO equity I'd lose is too high to act on." Every violation is either low-equity (A.3, clear rename) or medium-equity (A.2, Mike's call but workforce recommends rename in all 4 cases).

5. **The retrospective collections are double-justified for remediation.** Both `/collections/world-cup-2022-accessories` (A.2) and the 2022/2023 retrospective collections in A.3 have fading topical relevance AND a brand IP violation. The remediation is net-positive on both axes: clean up the brand IP exposure AND consolidate fading equity into evergreen successors.

### Next steps after Mike's exception decision (2026-05-17)

1. **Tier A.2 (4 URLs): RESOLVED.** Exception applied per Mike's business decision; slugs stay as-is. Copy-level compliance routed through ongoing whitelabel audit-and-regen workflow when ORIN reaches each page.
2. **Tier A.3 (11 URLs): RESOLVED.** Exception applied; slugs stay as-is. Copy-level compliance routed through ongoing whitelabel audit-and-regen workflow.
3. **VERITAS visibility investigation (APPROVED, separate brief):** 4 live-but-not-in-sitemap collections (`/collections/2026-fifa-world-cup`, `/collections/2026-fifa-world-cup-qualified-teams`, `/collections/2026-fifa-world-cup-qualified-teams-accessories`, `/collections/nike-2026-fifa-world-cup-soccer-jerseys`). Worth understanding visibility status (unpublished / sales-channel-off / metafield-hidden / other) regardless of the slug-remediation question. Mike approved the VERITAS brief; not blocking on this audit's closure.
4. **VERITAS sitemap-refresh script enhancement (APPROVED, separate brief):** add brand IP scan to `scripts/_build_sitemap_state.py` so future collection slug additions get auto-flagged at refresh time. Defensive automation. Mike approved.
5. **Sitemap-state.md refresh cadence cross-reference with GSC top-pages.** The 2026-05-08 sitemap snapshot missed live collections that GSC sees. Recommend the next sitemap-state.md refresh include a cross-reference pass against the latest GSC top-pages CSV so the "live but not in sitemap" cohort is documented inline rather than discovered audit-by-audit. Routes to VERITAS alongside the script enhancement (#4).
6. **Copy-compliance follow-up for the 15 grandfathered violations.** As ORIN works through whitelabel audit Collections #2, #3, and beyond, copy on any of the 15 violation URLs gets brought into compliance with `context/brand-ip-constraints.md`. The slug stays per exception; the customer-facing fields get Federation-anchored substitution. No standalone remediation pass needed; this rides on the ongoing audit workflow.

---

## Sources cited

- `context/brand-ip-constraints.md` (2026-05-16, the constraint source-of-truth)
- `deliverables/tracking/sitemap-state.md` (2026-05-08 refresh, 662 sitemap-discoverable collections)
- `data/gsc-exports/2025-04-to-2026-04_top-pages.csv` (1000 rows, 12-month aggregated per-URL metrics)
- Live observation 2026-05-16 of `/collections/2026-national-team-soccer-fan-gear` page linking to `/collections/nike-2026-fifa-world-cup-soccer-jerseys` (whitelabel audit Collection #1 finding)
- `deliverables/page-optimizations/whitelabel-audit/2026-05-16_2026-national-team-soccer-fan-gear_audit-and-regen.md` (the upstream audit that triggered this URL-architecture pass)

## Confidence and severity

- **Severity: High.** Brand IP violations create legal exposure regardless of SEO equity. The Tier A framework manages the SEO-equity preservation question; the legal-exposure question is binary.
- **Confidence: Medium-High.** Discovery is comprehensive against the two best available sources (sitemap-state.md and GSC top-pages CSV). Position trend signals (improving / stable / declining) were not pulled from the weekly-performance CSV; for the 4 A.2 violations, Mike may want trend data before making per-URL decisions. Workforce can pull that on request.
- **Expected impact (under Mike's exception decision):** zero SEO impact from slug-level work (no renames, no redirects). Brand IP exposure at the slug level remains and is now documented as a known business-decision exception in `context/brand-ip-constraints.md`. Copy-level legal exposure on the 15 violation URLs gets remediated incrementally as ORIN audits and regenerates each page through the ongoing whitelabel audit workflow.

## Self-verification status

- All claims trace to sourced data (sitemap-state.md, GSC top-pages CSV, live page observation).
- All URL paths in the audit verified against sitemap-state.md and GSC top-pages CSV.
- Brand-affiliation classification per `context/brand-ip-constraints.md` discipline (Adidas-prefix in slug = Adidas-licensed; Nike-prefix = Nike-licensed; Puma-prefix = Puma-licensed; no brand prefix = brand-agnostic umbrella by default).
- Tiering criteria match Mike's specification in the 2026-05-16 directive (with the noted interpretation for the position-<20 + clicks-10-100 cross-zone, which Mike's strict criteria leave ambiguous; flagged transparently in Phase 2).
- Voice check to run on this brief at commit time per workforce discipline.

## Decisions Documented (2026-05-17)

Mike's calls on GATE review:

1. **Tier A.2 (4 URLs):** EXCEPTION applied. Slugs stay as-is. Copy compliance via whitelabel audit workflow.
2. **Tier A.3 (11 URLs):** EXCEPTION applied. Slugs stay as-is. Copy compliance via whitelabel audit workflow.
3. **VERITAS visibility investigation** (4 live-but-not-in-sitemap collections): APPROVED as separate brief.
4. **VERITAS sitemap-refresh script enhancement** (brand IP scan in `scripts/_build_sitemap_state.py`): APPROVED as separate brief.

Audit closed. Slug-level work: complete (exception applied + documented). Copy-level work: ongoing through whitelabel audit-and-regen pipeline.
