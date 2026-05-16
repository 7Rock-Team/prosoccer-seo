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
- **Non-Adidas violations requiring action or documentation:** 12 collections in sitemap + 4 additional live-but-not-in-sitemap collections found via GSC = 13 distinct violations (some overlap; see Phase 1 table for full list).

### Tier breakdown of violations

- **Tier A.1 (HIGH EQUITY, document only):** 0 collections meet the strict pos < 20 AND clicks > 100 criterion.
- **Tier A.2 (MEDIUM EQUITY, Mike per-URL decision):** 4 collections (positions all on page 2 of Google, clicks 15-50 over 12 months).
- **Tier A.3 (LOW EQUITY, rename + redirect recommended):** 9 collections below the GSC top-1000 cutoff (i.e., < 14 clicks over 12 months).

### Recommended action counts

- **Mike per-URL decisions needed:** 4 (Tier A.2; see Phase 2).
- **Tier A.3 remediation map ready for implementation:** 9 slugs to rename + 301 redirect (see Phase 3).
- **Adidas-compliant (no action):** 10 (see Phase 1 reference table).
- **Separate VERITAS investigation:** 1 live URL (`/collections/nike-2026-fifa-world-cup-soccer-jerseys`) that does not appear in sitemap-state.md but is linked from a live whitelabel-produced collection page; merits dedicated audit pass to determine whether it is unpublished, sales-channel-off, or otherwise excluded from the sitemap.

### Headline pattern observation

The whitelabel slug-naming convention pre-dates the workforce's Brand IP architecture. The violation set is small (13 distinct URLs across 662 collections, < 2% of the collection catalog) and concentrated in tournament-scoped pages (2022 retrospectives, 2025 Club World Cup, 2026 cycle). No systemic naming-template violation; this looks like ad-hoc slug creation around tournament cycles without brand-affiliation discipline. The new `context/brand-ip-constraints.md` Step 4c discipline prevents future violations of this pattern.

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

### Tier A.2 (MEDIUM EQUITY, Mike per-URL decision)

**Criterion (interpreted to fit observed data):** Average position 10-30 with measurable click volume (10-100 clicks/12mo). Page 1-2 of Google but click volume modest. Mixed trend signals or uncertain ranking stability.

Four violations qualify:

| Slug | Position | Clicks (12mo) | Impressions (12mo) | CTR | Brand class | Recommendation framing |
|---|---|---|---|---|---|---|
| `/collections/2026-fifa-world-cup-qualified-teams-accessories` | 10.79 | 36 | 6,085 | 0.59% | brand-agnostic umbrella | Page 1, weak CTR (sub-1%). The position is good but the click yield is low, suggesting users are seeing it in SERP and choosing other results. Rename + redirect risk is moderate; equity loss could be 30-50 clicks/year if redirect underperforms; equity-preservation worth roughly $X (not quantified, low absolute). |
| `/collections/2026-fifa-world-cup-qualified-teams` | 12.32 | 39 | 9,906 | 0.39% | brand-agnostic umbrella | Page 2 top, very weak CTR. Same posture as #1; the impression volume is high but conversion to clicks is weak. Rename + redirect risk moderate. |
| `/collections/world-cup-2022-accessories` | 13.12 | 15 | 1,996 | 0.75% | brand-agnostic umbrella | Retrospective 2022 page. Page 2 ranking. Click volume tail and declining-by-relevance (2022 tournament is 4 years stale). Lean toward rename + redirect: relevance is fading regardless of brand IP issue. |
| `/collections/2026-fifa-world-cup` | 16.94 | 50 | 6,923 | 0.72% | brand-agnostic umbrella | Page 2, modest clicks. The highest-click violation but position weak. Rename + redirect risk moderate; the page is generic enough that a Federation-anchored successor slug should rank for the same intent. |

**Workforce recommendation per URL (Mike decides):**
- `/collections/2026-fifa-world-cup-qualified-teams-accessories`: **rename now** (modest equity, replaceable with Federation-anchored slug; suggested target slug `/collections/2026-national-team-qualified-accessories` redirected from the current).
- `/collections/2026-fifa-world-cup-qualified-teams`: **rename now** (same logic; suggested target slug `/collections/2026-qualified-national-teams`).
- `/collections/world-cup-2022-accessories`: **rename + redirect to evergreen** (suggested target `/collections/national-teams-accessories` or `/collections/fan-shop-accessories`; the 2022 retrospective is fading anyway).
- `/collections/2026-fifa-world-cup`: **rename now** (suggested target slug `/collections/2026-international-tournament` or `/collections/2026-tournament-soccer`; the Federation-anchored alternative naming captures the same intent).

All four are workforce-recommended for remediation but routed through Mike's per-URL decision per Tier A.2 protocol. Mike's other option per URL: defer remediation, document as known exposure, re-evaluate annually or if Adidas/legal flags.

### Tier A.3 (LOW EQUITY, rename + 301 redirect recommended)

**Criterion:** Average position > 50 OR 12-month clicks < 10 OR near-zero impressions OR declining trend with negligible volume. Operationally for this audit: violations NOT in the GSC top-pages CSV (< 14 clicks over 12 months) plus violations with negligible measured traffic.

**Result: 11 collections qualify for Tier A.3 remediation.** Listed in the Phase 3 remediation map below.

---

## Phase 3: Tier A.3 Remediation Map

For each Tier A.3 violation, the recommended slug rename and 301 redirect target. Implementation via Shopify admin Online Store > Navigation > URL Redirects (same workflow as the May 8 404 remediation). Equity-loss risk is Low across the board for Tier A.3 by definition; below-cutoff GSC traffic means a redirect that consolidates equity into a Federation-anchored successor is net-positive even if some long-tail rankings shift.

| # | Current slug (violation) | Recommended clean slug | 301 redirect target | Equity-loss risk | Implementation notes |
|---|---|---|---|---|---|
| 1 | `/collections/2025-fifa-club-world-cup` | `/collections/2025-club-tournament` | `/collections/2025-club-tournament` | Low | Brand-agnostic umbrella; Federation-anchored successor preserves topical intent. |
| 2 | `/collections/2026-fifa-world-cup-logo-accessories` | (consider deprecation; "logo accessories" implies official FIFA branded merch which IS the FIFA commercial context) | redirect to `/collections/2026-national-team-soccer-accessories` (Collection #2 in current whitelabel audit) | Low | If the collection genuinely sells official FIFA-branded logo merch, the slug AND the product set itself are brand-IP-questionable. Recommend Mike review the actual product mix before remediating. |
| 3 | `/collections/2026-fifa-world-cup-retro-gear` | `/collections/2026-retro-national-team-gear` | `/collections/2026-retro-national-team-gear` | Low | Brand-agnostic; "retro" framing preserved. |
| 4 | `/collections/fifa-2023-womens-world-cup` | `/collections/2023-womens-international-tournament` | `/collections/womens-national-teams` (evergreen successor; 2023 retrospective fading) | Low | Retrospective; recommend redirecting to evergreen women's national teams collection rather than creating a 2023-scoped successor that will also fade. |
| 5 | `/collections/fifa-world-cup-2022-gear` | (deprecate) | `/collections/national-teams` | Low | Retrospective 2022; 4 years stale; redirect to evergreen national-teams umbrella for maximum equity preservation. |
| 6 | `/collections/nike-mercurial-cr7-2022-world-cup-pack` | `/collections/nike-mercurial-cr7-2022-pack` | `/collections/nike-mercurial-cr7-2022-pack` | Low | Nike-prefixed page; removing "world-cup" from the slug eliminates the brand IP violation without changing the product scope. CR7 + Mercurial + 2022 still uniquely identifies the product set. |
| 7 | `/collections/puma-2025-club-world-cup-kidsuper-soccer-jerseys` | `/collections/puma-2025-club-tournament-kidsuper-soccer-jerseys` | `/collections/puma-2025-club-tournament-kidsuper-soccer-jerseys` | Low | Puma-prefixed page; "club-tournament" substitution preserves topical reference without invoking FIFA. |
| 8 | `/collections/world-cup-2022-balls` | (deprecate) | `/collections/soccer-balls` | Low | Retrospective 2022; redirect to evergreen soccer balls collection. |
| 9 | `/collections/world-cup-2026-keychains` | `/collections/2026-national-team-keychains` | `/collections/2026-national-team-keychains` | Low | Federation-anchored substitution. |
| 10 | `/collections/world-cup-soccer-balls` | (deprecate) | `/collections/soccer-balls` | Low | Generic violation slug; redirect to evergreen ball collection. |
| 11 | `/collections/nike-2026-fifa-world-cup-soccer-jerseys` | `/collections/nike-2026-national-team-soccer-jerseys` | `/collections/nike-2026-national-team-soccer-jerseys` | Low | Nike-prefixed page (violation); Federation-anchored successor. **Separate VERITAS investigation needed first** to confirm the current URL's visibility status (live, not in sitemap, not in GSC top-pages: may be unpublished, draft, or sales-channel-off). Resolve visibility before remediation; otherwise the remediation may shift state in an unintended way. |

**Implementation summary for Mike (Tier A.3):**
- 11 slug renames + 301 redirects
- 5 redirects to net-new Federation-anchored slugs (#1, #3, #6, #7, #9)
- 6 redirects to existing evergreen collections (#2, #4, #5, #8, #10, #11 if VERITAS clears it)
- All Low equity-loss risk
- Same Shopify admin URL Redirects workflow as the May 8 404 remediation

---

## Phase 4: Tier A.2 Per-URL Decisions Needed

See Phase 2 Tier A.2 table above. Four violations require Mike's per-URL decision: rename now (with redirect) vs defer (document as known exposure). Workforce recommendation per URL is provided alongside each option.

### Summary table for Mike

| Slug | Workforce recommendation | Mike's decision needed |
|---|---|---|
| `/collections/2026-fifa-world-cup-qualified-teams-accessories` | Rename now → `/collections/2026-national-team-qualified-accessories` | [Rename / Defer] |
| `/collections/2026-fifa-world-cup-qualified-teams` | Rename now → `/collections/2026-qualified-national-teams` | [Rename / Defer] |
| `/collections/world-cup-2022-accessories` | Rename now → redirect to `/collections/national-teams-accessories` (or `/collections/fan-shop-accessories`) | [Rename / Defer] |
| `/collections/2026-fifa-world-cup` | Rename now → `/collections/2026-international-tournament` (or `/collections/2026-tournament-soccer`) | [Rename / Defer] |

---

## Phase 5: Patterns Observed and Recommended Next Steps

### Patterns

1. **Whitelabel slug-naming was ad-hoc around tournament cycles.** Violations cluster in: 2022 retrospective collections (`world-cup-2022-*`), 2023 retrospective Women's collection, 2025 Club Cup collections, and the 2026 cycle. Each tournament window appears to have generated 2-5 new collection slugs without brand-affiliation discipline. The new `context/brand-ip-constraints.md` Step 4c discipline prevents this pattern going forward, but the historical inventory needs cleanup.

2. **Two distinct brand-licensed slug violations.** `/collections/nike-mercurial-cr7-2022-world-cup-pack` and `/collections/puma-2025-club-world-cup-kidsuper-soccer-jerseys` are both brand-prefixed (Nike and Puma respectively) AND contain FIFA-trademarked terms in the same slug. These are the highest-priority remediations regardless of equity tier because the brand-prefix makes the licensing context explicit and the contradiction stark.

3. **Sitemap-state.md does not capture all live collections.** Three measurable-traffic FIFA-family collections (`/collections/2026-fifa-world-cup`, `/collections/2026-fifa-world-cup-qualified-teams`, `/collections/2026-fifa-world-cup-qualified-teams-accessories`) exist live and rank in Google but do not appear in the 2026-05-08 sitemap snapshot. Plus the linked-only `/collections/nike-2026-fifa-world-cup-soccer-jerseys`. The sitemap reconciliation work documented in `deliverables/tracking/sitemap-state.md` lines 17-46 is the relevant context: ProSoccer keeps a substantial catalog off the storefront sales channel. The audit should treat GSC + Shopify admin + sitemap as three complementary sources-of-truth, not one.

4. **No Tier A.1 high-equity violations exist.** This is good news for remediation simplicity: there is no case where Mike has to weigh "the brand IP risk is real but the SEO equity I'd lose is too high to act on." Every violation is either low-equity (A.3, clear rename) or medium-equity (A.2, Mike's call but workforce recommends rename in all 4 cases).

5. **The retrospective collections are double-justified for remediation.** Both `/collections/world-cup-2022-accessories` (A.2) and the 2022/2023 retrospective collections in A.3 have fading topical relevance AND a brand IP violation. The remediation is net-positive on both axes: clean up the brand IP exposure AND consolidate fading equity into evergreen successors.

### Recommended next steps

1. **Mike reviews Tier A.2 (4 URLs).** Per-URL decision: rename or defer. Workforce recommends rename on all 4; Mike's call.
2. **Mike approves Tier A.3 remediation map (11 URLs).** Once approved, implementation routes through Shopify admin URL Redirects same as the May 8 404 remediation workflow.
3. **VERITAS investigates 4 live-but-not-in-sitemap collections** (`/collections/2026-fifa-world-cup`, `/collections/2026-fifa-world-cup-qualified-teams`, `/collections/2026-fifa-world-cup-qualified-teams-accessories`, `/collections/nike-2026-fifa-world-cup-soccer-jerseys`) to determine visibility status (unpublished / sales-channel-off / metafield-hidden / other) before the rename remediations land for those URLs.
4. **VERITAS adds the brand IP scan to the routine sitemap refresh script** (`scripts/_build_sitemap_state.py`) so future collection slug additions get auto-flagged at sitemap refresh time. Routes to a separate VERITAS brief.
5. **Sitemap-state.md refresh cadence cross-reference with GSC top-pages.** The 2026-05-08 sitemap snapshot missed live collections that GSC sees. Recommend the next sitemap-state.md refresh include a cross-reference pass against the latest GSC top-pages CSV so the "live but not in sitemap" cohort is documented inline rather than discovered audit-by-audit.

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
- **Expected impact:** zero direct SEO impact from Tier A.3 remediation (by definition; below-cutoff traffic). Modest equity-shift risk on Tier A.2 (4 URLs, total 140 clicks/year combined, replaceable with Federation-anchored successors). High legal-exposure reduction from consolidating all 15 violations into brand-IP-compliant successors.

## Self-verification status

- All claims trace to sourced data (sitemap-state.md, GSC top-pages CSV, live page observation).
- All URL paths in the audit verified against sitemap-state.md and GSC top-pages CSV.
- Brand-affiliation classification per `context/brand-ip-constraints.md` discipline (Adidas-prefix in slug = Adidas-licensed; Nike-prefix = Nike-licensed; Puma-prefix = Puma-licensed; no brand prefix = brand-agnostic umbrella by default).
- Tiering criteria match Mike's specification in the 2026-05-16 directive (with the noted interpretation for the position-<20 + clicks-10-100 cross-zone, which Mike's strict criteria leave ambiguous; flagged transparently in Phase 2).
- Voice check to run on this brief at commit time per workforce discipline.

## Held at GATE for Mike review

Awaiting Mike's:
1. Decisions on the 4 Tier A.2 per-URL cases.
2. Approval to proceed with the Tier A.3 remediation map (11 URLs).
3. Approval to route the 4 live-but-not-in-sitemap collections to VERITAS for visibility investigation before remediation.
4. Approval to route the routine sitemap-refresh brand IP scan addition to VERITAS as a separate brief.
