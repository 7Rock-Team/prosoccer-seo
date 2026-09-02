# Batch 17 pre-import baselines

**Captured:** 2026-09-02
**Window:** 2026-06-05 to 2026-09-02 inclusive, 90 days, trailing to the day of capture
**Source:** Google Search Console, `sc-domain:prosoccer.com`, Search type web, no device or country filter
**Scope:** canonical product URL only. Locale-prefixed and `?variant=` rows excluded. See "What was excluded" below.
**Captured by:** ORIN, before the Batch 17 Matrixify import. **The import has not run.**

**This is the first batch in the programme with baselines recorded before import.** Why that matters is in `work-log/2026-09-02_batch17-baselines.md`.

---

## 1. Page-level baselines, as written to `products-master.csv`

These four figures are written to `baseline_impressions`, `baseline_clicks`, `baseline_ctr` and `baseline_position` on each SKU's row. All four are **page-scope** and comparable with each other.

**The earned-term positions in section 2 are written to a separate column, `baseline_term_position`** (added 2026-09-02, Mike's ruling). It is term-scope and it is the figure the follow-up measures. The two position columns are never substituted for each other and never averaged.

| SKU | Handle | Impressions | Clicks | CTR | Position |
|---|---|---|---|---|---|
| 20490-BOX | `panini-2026-fifa-world-cup-stickers-box-50-packs-each` | 29,834 | 92 | 0.3084% | 9.80 |
| UUM1GUAJ525101-U10 | `umbro-2025-2026-guatemala-mens-home-soccer-jersey` | 24,725 | 19 | 0.0768% | 5.96 |
| JN4397 | `adidas-2026-spain-mens-stadium-away-soccer-jersey` | 23,052 | 98 | 0.4251% | 6.38 |
| HQ2332-800 | `nike-phantom-6-low-elite-firm-ground-soccer-cleats-erling-haaland-pack-fa25` | 22,484 | 28 | 0.1245% | 6.15 |
| 783301-01 | `puma-2026-paraguay-mens-authentic-home-soccer-jersey` | 18,065 | 37 | 0.2048% | 6.00 |
| DH6621 | `nike-strike-sleeves-socks` | 14,707 | 72 | 0.4896% | 8.50 |
| KB9024 | `adidas-2026-27-club-america-mens-authentic-home-soccer-jersey` | 11,861 | 3 | 0.0253% | 5.39 |
| JL6934 | `adidas-2026-italy-mens-authentic-home-soccer-jersey` | 10,621 | 10 | 0.0942% | 10.87 |
| IB4855-410 | `nike-2026-27-usmnt-mens-stadium-home-shorts` | 9,795 | 24 | 0.2450% | 12.29 |
| **Batch total** | | **165,144** | **383** | **0.2319%** | |

`position` is the GSC average across every query the page appeared for. It is **not** the number the ranking bands key on. The band figure is the earned-term position in section 2.

## 2. Term-level baselines: the earned term per page

The follow-up has to be measured on the term each page was optimized for, not only on page totals, because page totals aggregate every query the page appears for and most of them are not the one the copy targets.

| SKU | Earned term | Term impr | Term clicks | Term CTR | Term position | Share of page impr |
|---|---|---|---|---|---|---|
| KB9024 | `america jersey 2026` | 4,271 | 1 | 0.0234% | **3.40** | **36.01%** |
| 783301-01 | `paraguay jersey` | 5,193 | 2 | 0.0385% | **4.89** | **28.75%** |
| UUM1GUAJ525101-U10 | `guatemala soccer jersey` | 6,157 | 0 | 0.0000% | **4.93** | **24.90%** |
| JN4397 | `spain jersey 2026` | 5,969 | 0 | 0.0000% | **5.50** | **25.89%** |
| HQ2332-800 | `haaland cleats` | 4,262 | 0 | 0.0000% | **6.08** | **18.96%** |
| IB4855-410 | `usmnt shorts` | 1,588 | 4 | 0.2519% | **10.55** | **16.21%** |
| DH6621 | `nike sleeve socks` | 368 | 1 | 0.2717% | **9.07** | **2.50%** |
| JL6934 | none, not-ranking | | | | | |
| 20490-BOX | none, not-ranking | | | | | |

**Guatemala's earned term is CEDED to `/collections/guatemala`** and is recorded here as the measurement target, not as a claim. The collection takes 8,131 impressions and all 180 clicks at position 5.62 on that term while the PDP takes zero clicks at a marginally better position, which is why the hierarchy amendment handed it over. Measure it anyway: if the PDP's copy changes its clicks on a term where it currently gets none, that is worth knowing.

### The recorded band positions hold up

The `earned_term_position` values written into the briefs at Phase 0 were measured on a different 90-day window (ending 2026-08-27). Re-measured on this window they are essentially unchanged, which means the band assignments in the briefs were correct at the time and remain correct now.

| SKU | Recorded in gate-meta | Measured 2026-09-02 | Drift |
|---|---|---|---|
| KB9024 | 3.50 | 3.40 | -0.10 |
| UUM1GUAJ525101-U10 | 4.88 | 4.93 | +0.05 |
| 783301-01 | 4.89 | 4.89 | 0.00 |
| JN4397 | 5.50 | 5.50 | 0.00 |
| HQ2332-800 | 6.08 | 6.08 | 0.00 |
| DH6621 | 9.38 | 9.07 | -0.31 |
| IB4855-410 | 10.57 | 10.55 | -0.02 |

No page crossed a band boundary. KB9024 remains the only page under position 5.

### The concentration condition, re-tested on this window

`context/workforce-conventions.md` requires an earned term to hold **at least 15% of page impressions AND at least 1,000 term impressions**.

| SKU | Share | Term impr | 15% test | 1,000 test | Verdict |
|---|---|---|---|---|---|
| KB9024 | 36.01% | 4,271 | pass | pass | **PASS** |
| 783301-01 | 28.75% | 5,193 | pass | pass | **PASS** |
| JN4397 | 25.89% | 5,969 | pass | pass | **PASS** |
| UUM1GUAJ525101-U10 | 24.90% | 6,157 | pass | pass | **PASS** |
| HQ2332-800 | 18.96% | 4,262 | pass | pass | **PASS** |
| IB4855-410 | 16.21% | 1,588 | pass | pass | **PASS** |
| DH6621 | **2.50%** | **368** | **fail** | **fail** | **FAIL BOTH** |

**Six of seven pass cleanly. DH6621 fails both thresholds by a wide margin, on fresh data, exactly as B-RANK-01 records.** Its band is held at 5-to-10 by Mike's disposition of 2026-09-02, on the grounds that recording `not-ranking` for a page measured at position 9.07 would be a false record. This capture is independent confirmation of the problem rather than a new finding: the term genuinely ranks and the term genuinely fails the selection condition, which is why B-RANK-01 argues the one condition is doing two different jobs. **DH6621 is the page to watch in the follow-up**, because it is the only one whose band rests on a judgment call rather than a rule.

## 3. What was excluded, and one finding from the exclusions

Canonical-only was the instruction and is the right scope for a before-and-after, because the import changes the canonical page. Two classes of row were excluded.

**Locale-prefixed URLs.** GSC reports `/en-au/`, `/en-gb/` and `/en-ca/` paths as separate pages. Across the nine SKUs they add **2,897 impressions and 42 clicks**.

| | Impressions | Clicks | CTR |
|---|---|---|---|
| Canonical, what is recorded above | 165,144 | 383 | **0.2319%** |
| Locale-prefixed, excluded | 2,897 | 42 | **1.4498%** |

**The locale URLs are 1.7% of impressions and 9.9% of clicks, at more than six times the canonical CTR.** This is the same shape as the canonical-versus-variant split found on 2026-08-27, where variant URLs were 3.6% of impressions and 29.5% of clicks. Two independent slices of traffic that the canonical-only measurement does not see, both converting far better than the canonical page.

That does not invalidate the baseline. It does mean **a canonical-only follow-up measures a minority of this batch's clicks**, and any click-based conclusion should say so. The largest single case is the Nike Strike Sleeves: 1,077 locale impressions and 14 locale clicks against 14,707 canonical impressions and 72 canonical clicks, so roughly 16% of that page's clicks sit outside the measured scope. Logged for the follow-up rather than acted on here.

**`?variant=` URLs**, excluded by the same rule and for the same reason as the 2026-08-27 ruling.

## 4. How to re-run this

The follow-up must use the identical method or the comparison is worthless.

1. Same property, `sc-domain:prosoccer.com`. Search type web. No device or country filter.
2. Page level: `dimensions=page`, filter `includingRegex` on the nine handles anchored with `$`, which is what excludes locale and variant rows.
3. Term level: one call per page, `pageFilter` **equals** the full canonical URL and `queryFilter` **equals** the earned term, no dimensions.
4. Window: 90 days trailing, matching the length used here. **Do not compare a 90-day pre-window against a 30-day post-window.**
5. Report page-level and term-level separately. Never average them.

**Read `work-log/2026-08-14_gsc-analysis-results.md` before interpreting any result.** It is the record of a cohort comparison on this corpus that could not detect an effect in either direction, where two pages out of fifty-one flipped the sign of the headline finding. This batch has the same exposure: the Panini box, Guatemala and Spain are each above 23,000 impressions in a World Cup year and are all capable of dominating a cohort mean. **Report per-page paired changes, not a cohort average.**

**The control.** DH6621 was selected as the batch's evergreen control: no season tag, no tournament exposure, no seasonal story. If every World Cup page moves and the sleeves do not, the movement was the calendar. If the sleeves move too, the copy did something. That design is the reason this batch is worth measuring at all, and it is also why DH6621's band being a judgment call is awkward: the control page is the one carrying the open rule question.
