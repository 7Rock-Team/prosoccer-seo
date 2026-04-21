# Phase 2 Task 4: Late-2025 Theme Migration SEO Impact

**Session date:** 2026-04-21
**Status:** Analysis complete. Shape is plateau-breaking-trend, not a cliff. Site has since recovered.

## Objective

Determine whether the late-2025 Shopify theme migration by the prior agency damaged organic SEO performance, and if so, whether the damage persists or has resolved.

## Method

Analyzed 53 weeks of Google Search Console weekly-performance data (`data/gsc-exports/2025-04-2026-04_weekly-performance.csv`) covering April 2025 to April 2026. Focused on average position as the cleanest signal (clicks and impressions are also pulled upward by the Feb 2026 AI Overview impression surge, which would muddy any binary "before/after" read on a position change).

Mike confirmed the theme shipped in **October 2025**.

## Finding: Plateau-Breaking-Trend

Not a binary cliff. Not a clean continued-improvement line. A three-phase shape.

| Period | Avg position range | Shape |
|---|---|---|
| Apr - Aug 2025 | 20.1 to 23.5 (flat around 22) | Baseline plateau |
| Sep 2025 | 22.5 → 18.8 → 15.5 → 14.8 → 12.6 | Sharp improvement (predates theme swap, unrelated) |
| Oct 2025 | 12.2 → 12.1 → 11.4 → 12.0 | Settled at ~11-12 |
| Nov 2025 - Jan 2026 | 11.4 → 12.5 → 13.3 → 13.0 → 13.9 → 12.9 → 13.8 → 14.0 → 14.6 → 15.0 | Regression, 3 to 4 positions worse |
| Feb - Apr 2026 | 13.7 → 11.8 → 11.3 → 11.0 → 10.9 → 10.7 → 9.6 → 10.0 → 10.2 → 10.3 | Recovery to pre-regression levels |

## Timeline Read With the October 2025 Ship Date

- **September 2025:** position improvement from ~22 to ~11 predates the theme swap. Driver is unknown (candidates: algorithm update, seasonal back-to-school lift, inventory or content work from the prior agency). Not theme-driven.
- **October 2025:** theme ships. Site settles at position ~11-12 in the immediate weeks after launch.
- **November 2025 - January 2026:** 3-to-4-position regression. Timing aligns with the typical 4-to-6-week Google re-indexing lag after a theme change. Most likely cause: theme-level SEO regressions (structured data, internal linking, template changes) compounding through the re-crawl cycle.
- **February 2026:** 7 Rock re-engagement begins.
- **February - April 2026:** rankings recover to pre-damage levels (position ~10-11). Recovery coincides with 7 Rock re-engagement but 7 Rock has not yet shipped technical fixes; the recovery is more likely driven by natural re-stabilization and the AI Overview impression surge pulling higher-position queries into the average.

## Interpretation

The theme migration caused a temporary ranking regression. That regression has been arrested and reversed. Current rankings reflect a recovered state, not an active-damage situation.

This means:

- Current GSC position data is a truthful baseline for Month 1 planning. We aren't looking at in-progress decay.
- Any residual theme-level SEO issues are now affecting the recovered baseline. Meaning: fixing them produces lift above current position, not just a return to pre-theme levels.
- We will not be able to cleanly attribute any Month 1 position gains to 7 Rock work vs. ongoing natural recovery. That attribution fog should be stated in the first monthly report to Tony, not glossed over.

## Residual Theme-Migration Debt for Technical SEO Agent (Month 1 Scope)

Theme-migration artifacts surfaced during Phase 2 Task 1 that the Technical SEO Agent should address when it goes live:

- **`/collections/spain-jerseys-copy`** and **`/collections/france-hats-copy`.** Orphan "copy" variants of live collection pages, present in the live Shopify collections sitemap. Almost certainly duplicates created during the theme-migration content-copy process and never cleaned up. Canonical review, then noindex or delete.
- **BreadcrumbList schema re-audit.** The Task 1 crawl parser did not detect BreadcrumbList on any page, which is likely a parser miss rather than a universal absence. A clean schema audit via Screaming Frog or a DOM-level re-crawl should confirm whether BreadcrumbList is present in a format the Task 1 regex didn't catch, or whether it is genuinely missing everywhere. If missing, implementing it is a Month 1 technical-fix deliverable.
- **Chile collection page re-crawl.** `/collections/chile` was Cloudflare-rate-limited (HTTP 429) on both the initial crawl and the retry. Needs a different user-agent or a longer delay to capture its true state. Chile ranks at position 10.96 with 88 clicks, so the page is real and performing; the crawl failure is the issue, not the page.

## Note on Measurement Going Forward

The Feb 2026 AI Overview impression surge is visible in both the impression and click trends across this window. Reports for Tony should lead with average position (less distorted by AIO impression inflation) and Merchant Listings click share (most commercially actionable under AIO pressure), rather than raw impressions. This is already reflected in the secondary-metrics block of `context/06-business-goals.md`.
