# Handoff: Discovery Session, Phase 1 Complete, Phase 2 and 3 Pending — 2026-04-20

## Status Snapshot

- **Phase 1 (Jan 2026 audit read):** Complete. 14 of 18 files read in full. 1 file partial (head + tail only). 3 files unread. Strategic conclusions compressed below.
- **Phase 2 (Playwright crawl of World Cup + national team collections):** Not started. Deferred to this next session to run with fresh context.
- **Phase 3 (context file touch-ups for Tony role + Plain language rule):** Not started. Deferred.
- **Approval gate:** still APPROVE-EVERY-ACTION.

## Framing Correction, Read This First

The January 2026 SEO audit was produced by **7 Rock's own whitelabel team** as a pre-engagement diagnostic at the client's request. It was always scoped as diagnosis, not implementation. Do NOT frame it as a prior-agency deliverable or as "diagnosis that failed to become implementation." 7 Rock did the 2021 to 2022 Magento to Shopify Plus migration. A different agency ran the account in 2025 and completed a theme migration in late 2025. The client returned to 7 Rock in February 2026. See `context/00-business-overview.md` History section for the full timeline.

That framing matters for Phase 2 task scoping. It changes which migration the legacy-URL investigation is pointed at (see Phase 2 instructions below).

## Three Unread Audit Files (Phase 1 holdbacks)

Drive folder: `1KF1213I-_nf9B04ASKoM_mcv5xydJ3h8`

| File | Drive ID | Priority | Why held back |
|---|---|---|---|
| `2 - All Ranking Keywords.xlsx` | `1_aWt7QsRpowus-UyX9yUn6TywXw0gfVh` | Medium | Full ranking keyword set. Useful once striking-distance and opportunity analysis is underway. Not blocking Phase 2. |
| `7 - Referring Domains Report.pdf` | `1PSe4ADJXUAx5eGn6oAHGFOZn8MOu23G4` | Low | 69,450 characters, exceeded read budget last session. Summary-level backlink signal already captured via Exec Summary + Backlinks Summary. Only read if Mike wants the full per-domain breakdown before disavow planning. |
| `7a - Refering Domains Deep Dive.xlsx` | `1THXH13giJyEQtSRgz2AnEXkcd6SU1Nd8` | Low | Same reasoning. Pair read with #7 when Mike schedules the disavow workstream. |

Also partial: `9 - Keyword Competition Analysis 2026 - Final.xlsx` (`1mD1ntAfZUDHKIqDoF48zGaInrvW6fnQY` — ID from prior session, verify in Drive before re-reading). Head + tail read, middle rows skipped. Full payload saved to disk last session at `mcp-claude_ai_Google_Drive-read_file_content-1776794826434.txt` if it still exists, else re-pull from Drive.

## Compressed Phase 1 Conclusions

### Technical

- **Site audit (Serpstat-style):** 19,633 pages crawled, score 79/100. 2,724 errors, 5,912 warnings. Heaviest items: 2,000 large pages, 2,000 render-blocking, 2,000 low-content, 2,000 deprecated HTML, 2,000 duplicate meta, 1,999 pages with no internal links, 1,169 long titles, 5,865 missing alt attributes, 636 duplicate content, 583 slow pages, 56 duplicate titles, 29 duplicate descriptions. Several of the "2,000" counts look like hard-capped report buckets rather than exact measurements. Flag for re-crawl via our own Screaming Frog in Month 1 to get clean numbers.
- **Lighthouse mobile:** Performance 51, SEO 92, Accessibility 73. Load 27.61s, TTI 13.6s, TBT 6,720ms, Max FID 3,440ms. Payload 9,196 KiB. Savings available: 1,515 KiB unused JS, 221 KiB unused CSS, 952 KiB image opt, 667 KiB cache policy, 94 KiB legacy JS. Main thread 23.1s. Accessibility fails: heading hierarchy, touch targets, contrast, label/name mismatch.
- **Technology (BuiltWith snapshot):** Shopify Plus, Klaviyo, Rebuy, Loop Returns, Gorgias, Searchanise, Tapcart, Cloudflare. Multiple jQuery versions loaded concurrently (3.6.0, 3.6.4, 3.7.1) — likely a theme-app conflict from the late-2025 theme, worth a targeted check. BuiltWith lists the platform move "from Magento" with a date that does NOT match the actual 2021 to 2022 migration; likely a re-detection artifact or a BuiltWith misread of the late-2025 theme swap. Don't cite the BuiltWith date as fact.

### Keyword

- **Targeted set (file 3):** 479 tracked keywords. Striking distance (positions 11-20) includes: soccer ball size 5, soccer ball bag, soccer hoodies, shin guards soccer, cr7 cleats, brazil soccer jersey, alex morgan jersey, soccer shin guards, nike soccer shoes, mexico soccer jersey. "Not found" (not ranking) on high-value head terms: soccer cleats, cleats, soccer jerseys, mexico soccer, real madrid jersey, adidas predator, custom soccer jerseys, manchester united jersey, usmnt jersey.
- **Opportunity scoring (file 9, partial):** top annual-SEO-value rows: soccer ($407K), brazil national team ($278K), pumas ($147K), soccer ball ($81K), mexico national football team ($76K), fifa world cup 2025 ($69K), soccer cleats ($48K). Full middle of the file not yet read.

### Competitor

- **Direct competitor set (file 8):** soccerpost.com TF46/CF44, soccer.com TF40/CF46/8,095 LD, prosoccer.com TF34/CF35/2,204 LD, wegotsoccer.com TF27/CF31, soccervillage.com TF24, soccerzoneusa.com TF22, worldsoccershop.com TF20/3,567 LD (more linking domains than ProSoccer at lower TF), pelesoccer.com TF16, soccerwearhouse.com TF13. ProSoccer sits mid-pack on authority, ahead on TF of several peers but losing on absolute link count to at least one lower-TF site.
- **Top 100 competitors by relevance (file 8a):** soccerwearhouse.com 0.21, aztecasoccer.com 0.18, worldsoccershop.com 0.18. Outlier: ussoccer.com, relevance 0.02 but 1.3M organic traffic — this is a link-worthy authority site, not a competitor. Target for outreach on USMNT / national team content.

### Authority

- **Backlinks (Majestic):** 14.8M total backlinks, 4.9K referring domains, 1,590 follow ref domains, 7,046 new in 120 days, TF 34%, CF 35%. Net 30 days: **-571 domains**, i.e. the profile is bleeding domains faster than it's gaining.
- **soccertop.com skew:** 90%+ of total backlinks (16M+) trace to soccertop.com, a UAE domain, low quality. This single referring domain distorts the aggregate backlink count upward without providing proportional value.
- **Korean anchor text cluster:** 미국 축구용품 전문 종합쇼핑몰 ("American Soccer Gear Specialty Mall"), 프로 사커 ("Pro Soccer"), plus Korean-script renderings of adidas/아디다스 and puma/퓨마. Unclear source. Either a real Korean market referral channel, a scraped aggregator, or a foreign SEO spam pattern. Ask Mike.

### Executive Summary

- 24-month ranking decline on Top 3 and Top 10 visibility.
- 4-pillar retainer pitch from whitelabel team: technical cleanup, content, authority, measurement. Reasonable framing but generic. The specific Month 1 actions below are tighter.

## Phase 2 Instructions (next session to execute, after Mike's approval)

### Task A: Playwright crawl of World Cup + national team collections

Mike's original URL list:

- `/collections/2026-fifa-world-cup`
- Plus ~20 national team collection URLs (list in prior session; re-confirm with Mike at session start — Brazil, Argentina, Mexico, USA, Germany, France, Spain, Portugal, England, Italy, Netherlands, Belgium, Colombia, Uruguay, Japan, South Korea, Morocco, Ghana, Nigeria, Canada were the likely set given the 2026 WC participant pool).

For each URL collect: title, meta description, H1, H2 set, product count, breadcrumb structure, internal link density, load time (Lighthouse), presence of unique intro copy vs. template-only, schema markup present, canonical tag, indexability status.

Cross-reference against: `data/gsc-exports/` (12-month query and page CSVs). Flag any URL in the crawl set that GSC shows impressions/clicks for but which the crawl reveals has thin content, missing meta, or weak internal linking.

Output: priority table, one row per URL, columns = URL / GSC impressions / GSC clicks / GSC avg position / crawl-surfaced issue / fix priority (high/med/low).

### Task B: Verify 2021 to 2022 Magento to Shopify Plus migration URL cleanup

**Framing, re-read before starting:** 7 Rock did this migration. The task is to verify the quality of our own prior work, not to audit someone else's failure.

Check for:
- Any remaining legacy Magento URL patterns still being crawled or indexed (e.g., `?id=`, `/catalog/product/view/id/`, `.html` product URLs with numeric IDs, old `/index.php` paths).
- 301 redirect map completeness — pull URLs from Ahrefs / GSC / internal link audit and check redirect status codes for any Magento-era URL surviving in external backlinks.
- Canonical tag consistency across current Shopify URLs.

This is legacy cleanup, not migration damage-control. Any broken redirect is a 7 Rock bug to fix, not evidence of a bad handoff.

### Task C: Separate investigation, late-2025 theme migration regressions

This IS the other agency's work. Different scope than Task B.

Check for:
- Core Web Vitals deltas pre- vs post-theme-migration (use CrUX data or Lighthouse history if accessible; otherwise establish a clean post-migration baseline).
- Internal linking patterns changed by the theme (nav, footer, cross-sell blocks, related-products modules).
- Template-level SEO elements: title template, meta template, schema markup, canonical logic, pagination handling, collection pagination SEO, product variant URL handling.
- Any regression in structured data (Product, BreadcrumbList, Organization schema).

### Task D: Month 1 recommendations (synthesis from Phase 1 + Phase 2)

Write up after Phase 2 crawl lands. Should merge audit findings with crawl findings into a single prioritized list.

## Priority Questions to Ask Mike Before Phase 2 Starts

1. **"Do you recognize soccertop.com as a legitimate referring relationship, or should we plan the disavow workstream assuming it's hostile/artificial?"** The 90%+ skew from that single UAE domain is the biggest aggregate-vs-real backlink gap to resolve before any authority-building strategy.
2. **"Is there a Korean market channel, partnership, wholesale relationship, or Korean-language site we should know about?"** The Korean-anchor-text cluster in the backlink profile is either a genuine traffic source to protect or spam to disavow — we need to know which.

**Dropped from the original question set:** the "March 2025 Shopify Plus migration" question. That migration did not happen in March 2025. 7 Rock did the Magento to Shopify Plus swap in 2021 to 2022. The BuiltWith date was misleading. Do not re-ask.

## Phase 3 Instructions (deferred, lower priority than Phase 2)

Two context-file touch-ups Mike requested earlier in the original 3-phase plan:

1. **`context/00-business-overview.md`:** Tony's role clarification. The 7 Rock history section was added in this session, but Mike also wanted a separate clarification of Tony's approval scope and COO-vs-operational-lead role. Confirm the exact wording with Mike before writing.
2. **`context/03-brand-voice.md`:** Add a new "Plain language rule" section. Mike did not send the rule body in-session; ask him for the text, don't invent it.

Both are fast edits but both require Mike's exact wording before commit.

## Files Modified This Session

- `context/00-business-overview.md` — added 7 Rock engagement timeline and History section (commit dated 2026-04-20).
- `.claude/agents/master-strategist/briefings/2026-04-20_discovery-handoff-phase2-pending.md` — this file.

No changes yet to: `shared-intelligence/industry-updates.md` (the incorrect "diagnosis without implementation" observation from the Phase 1 chat report was never persisted to the file, so there was nothing to remove).

## Startup Protocol Reminder for Next Session

1. Read every file in `context/` — the updated `00-business-overview.md` is the most-changed.
2. Read `.claude/agents/master-strategist/learnings.md`.
3. List `shared-intelligence/` and read anything modified in the last 14 days.
4. Read `strategy/master-strategy.md` and `strategy/sprint-backlog.md` if present.
5. Read this handoff AND `.claude/agents/master-strategist/briefings/2026-04-20_goals-doc-revision-handoff.md`.

Approval gate: still APPROVE-EVERY-ACTION. Mike has not switched to weekly review mode.
