# Handoff: Phase 2 Discovery, Tasks 3 + 4 + Affiliate Context + Synthesis Pending — 2026-04-21

## Status Snapshot

- **Task 1 (national team crawl + inventory):** Done, committed (`2cdae14`). See `deliverables/phase-2-discovery/task-1-inventory.md`.
- **Task 2 (A/B tiering against GSC):** Done, committed (`288b42b`). See `deliverables/phase-2-discovery/task-2-tiering.md`.
- **Task 3 (legacy Magento URL check):** Data collected, not yet written up. Finding persisted below.
- **Task 4 (theme-migration 3-shape analysis):** Data collected, not yet written up. Finding persisted below.
- **`context/08-affiliate-program.md`:** Not created. Spec below.
- **Final synthesis message:** Not composed. Structure below.
- **Approval gate:** still APPROVE-EVERY-ACTION.
- **Chile re-crawl:** Cloudflare 429 blocked on both initial run and retry. Deferred again.

## Task 3 Finding (ready to write as a 1-paragraph deliverable)

Grep of `data/gsc-exports/2025-04-to-2026-04_top-pages.csv` for patterns `index\.php|catalog/product|catalog/category|\.html$|\?id=|magento` (case-insensitive) returned zero matches.

**Interpretation:** No legacy Magento URLs are receiving impressions or clicks from Google in the 12-month GSC window. The 2021-to-2022 Magento-to-Shopify-Plus migration's URL cleanup is, from the GSC-surface view, clean. This does NOT confirm that 301s exist for every historical Magento backlink (GSC only shows indexed URLs receiving impressions); full redirect-map verification would require pulling Magento-era URLs from Ahrefs or the old sitemap and HEAD-checking each. But the headline claim "no legacy-URL traffic leaking" is defensible from the GSC data alone.

**Deliverable location:** write to `deliverables/phase-2-discovery/task-3-magento-legacy.md`. Keep it short (half a page). State the grep query, the zero-result finding, the scope limitation (GSC-only, not full Ahrefs sweep), and the recommendation (full redirect-map audit can be deferred; this is not where the Feb-2026 re-engagement should spend hours).

## Task 4 Finding (ready to write as a 3-shape analysis deliverable)

Weekly performance CSV (`data/gsc-exports/2025-04-2026-04_weekly-performance.csv`) covers 53 weeks. Position trajectory:

| Period | Avg position range | Shape |
|---|---|---|
| Apr-Aug 2025 | 20.1 - 23.5 (flat, ~22) | Baseline plateau |
| Sep 2025 (week of 09-07) | 22.5 → 18.8 → 15.5 → 14.8 → 12.6 | **Sharp improvement** |
| Oct 2025 | 12.2 → 12.1 → 11.4 → 12 | Settled at ~11-12 |
| Nov 2025 - Jan 2026 | 11.4 → 12.5 → 13.3 → 13 → 13.9 → 12.9 → 13.8 → 14 → 14.6 → 15 | **Mild regression, ~3-4 positions worse** |
| Feb-Apr 2026 | 13.7 → 11.8 → 11.3 → 11 → 10.9 → 10.7 → 9.6 → 10 → 10.2 → 10.3 | **Recovery and slight new high** |

**Three-shape verdict:** The data does NOT show a regression cliff aligned with the late-2025 theme migration. But it also is NOT a clean "continued improvement" line. The Nov-2025-through-Jan-2026 wobble, where position drifted from 11.4 back up to 15.0 before recovering in Feb, is the subtle signal worth naming. This is closer to Mike's **"plateau-breaking-trend"** scenario than the simple "continued improvement" call I was leaning toward before re-reading the weekly CSV row-by-row: the site broke the ~22 plateau in Sept, settled at ~12, then had a three-month regression that was arrested and reversed in Feb.

**What the Sep 2025 improvement is NOT:** it predates the 7 Rock re-engagement (Feb 2026) and is captured in the Phase 1 handoff as pre-existing. The driver is unknown. Candidates: the late-2025 theme migration ship (if it shipped in Sep), a Google algorithm update, a seasonality lift from back-to-school + fall soccer season, or inventory/content changes from the other agency. We do NOT know the exact theme-migration ship date yet — that's a question for Mike or for Misha.

**Interpretation for the synthesis:** The theme migration, whenever exactly it shipped, appears to have either helped or been neutral in the SHORT term (Sep-Oct improvement), then showed a three-month drift (Nov-Jan) that could be one of:
1. A delayed theme regression effect (structured data / internal linking / crawl efficiency decay).
2. A typical post-launch learning-period dip that markets recover from.
3. Correlated but not caused — January SEO volatility across the retail category.
4. A content freeze during the late-2025 theme work that starved the site of fresh signals.

Feb 2026 recovery aligns with 7 Rock re-engagement and the AI Overview impression surge (already documented). Attributing the recovery to 7 Rock work would be premature since we haven't shipped anything yet; more likely the AIO surge and/or WC-2026 query growth are pulling the site up.

**Deliverable location:** write to `deliverables/phase-2-discovery/task-4-theme-migration-shape.md`. Include the position table above, the three-shape verdict, and the four candidate explanations for the Nov-Jan wobble. Flag the ship-date question for Mike.

## `context/08-affiliate-program.md` Spec (approved by Mike)

Mike's directive 3, verbatim from startup approval:

> Approved to create context/08-affiliate-program.md at end of session. Capture:
> - 7 Rock manages ProSoccer's affiliate program on AWIN (Affiliate Window)
> - soccertop.com may be an AWIN affiliate — must be cross-referenced against AWIN roster before any disavow recommendation
> - Korean-language backlinks same logic — may be AWIN affiliates in Korean market, Mike doesn't know of any formal Korean partner
> - Operating rule: any backlink audit or disavow recommendation must include AWIN affiliate roster cross-reference as a mandatory step

**Write structure:**
1. Program overview: 7 Rock operates the ProSoccer affiliate program on AWIN. State ownership line (7 Rock manages; ProSoccer owns the relationship).
2. Known open questions (soccertop UAE-cluster status, Korean-anchor-text-cluster status). Label both as "unverified, pending AWIN roster lookup."
3. **Operating rule** (this is the load-bearing section). Phrase as: "Any specialist agent producing a backlink audit, disavow file, or referring-domain quality assessment MUST cross-reference the flagged domains against the AWIN affiliate roster before surfacing the recommendation to Mike. Disavowing an active affiliate destroys a revenue channel. The roster is maintained in AWIN and must be pulled fresh for each audit."
4. Reference pointer: AWIN roster lives in AWIN publisher dashboard (not in this repo). Flag as external-system reference.

Keep it to ~1 page. This is operating doctrine, not analysis.

## Final Synthesis Message (structure, not yet written)

Per the session prompt, after all four tasks, compose a synthesis covering:

**(a) Goal 2 sprint: named pages with proposed changes.** For each of the 6 committed countries, list the URL, the concrete on-page change (title/meta/H1/content block), and the expected GSC lift lever (position climb vs CTR lift). Flag the USMNT URL consolidation precondition. Flag the Mexico rebuild-not-polish scope correction. Recommend whether to swap Argentina or Germany INTO the sprint list given their GSC signal (Task 2 argues "not for the sprint, but yes for Q3 post-WC").

**(b) Month 1 Technical SEO scope.** Merge Phase 1 findings (Lighthouse 51, multi-jQuery, 5,865 missing alts, 2,000 render-blocking, etc.) with Phase 2 findings (el-salvador/honduras broken pages, USMNT cannibalization, spain-jerseys-copy / france-hats-copy leftovers, missing BreadcrumbList schema, three inconsistent title templates). Produce a prioritized Month 1 punch list.

**(c) Surprises.** The Phase 1 handoff's "positions 9-14" claim for country pages was wrong; Mexico is at 28.44, USMNT at 45.84. The Sep 2025 position improvement predates 7 Rock re-engagement and is unexplained. The Nov-Jan regression is real and under-investigated. Lamine Yamal outperforms every country page.

**(d) Questions for Mike.**
1. When exactly did the late-2025 theme migration ship? Knowing the week determines whether the Nov-Jan regression is a delayed-effect theme issue or something else.
2. Does Mike want the Lamine Yamal-pattern player-spotlight template added to the Goal 2 scope, or held for Q3?
3. Does Mike want Ecuador and Peru as net-new collection pages (requires query-side GSC check first)?
4. What's the right scope for the USMNT URL consolidation — a pre-sprint technical workstream or deferred to Month 2?
5. Timeline for pulling the AWIN affiliate roster so the backlink-audit workstream can start without risking a disavow-on-affiliate mistake?

## Known Partial Work Not Done

- **WC hub internal-link graph:** Task 1 spec asked for "internal link density" on the WC hub page. The Node crawl captured WC2026-mention booleans and schema types but did NOT extract the internal-link graph (which pages the WC hub links to, which pages link into it). That requires a second pass, either with Playwright or a more thorough DOM parse. Not critical for the sprint-planning output; flag for Month 1.
- **Chile page crawl:** Still Cloudflare-blocked. Try a different User-Agent string or a 10-second delay on next attempt.
- **Breadcrumb schema audit:** Task 1 parser did not detect BreadcrumbList on any page. This is most likely a parser miss (the crawl only extracted top-level `@type` values, not `@graph` children in all configurations). A cleaner schema audit is a Month 1 item.

## Files Not Yet Read from Phase 1

- `2 - All Ranking Keywords.xlsx` (Drive ID `1_aWt7QsRpowus-UyX9yUn6TywXw0gfVh`) — useful for striking-distance analysis once Month 1 scope lands.
- `7 - Referring Domains Report.pdf` (`1PSe4ADJXUAx5eGn6oAHGFOZn8MOu23G4`) — blocks clean backlink work. Pair with AWIN roster pull.
- `7a - Refering Domains Deep Dive.xlsx` (`1THXH13giJyEQtSRgz2AnEXkcd6SU1Nd8`) — same.

## Startup Protocol for the Fresh Session

1. Read every file in `context/`.
2. Read `.claude/agents/master-strategist/learnings.md`.
3. List `shared-intelligence/` and read anything modified in the last 14 days.
4. Read `strategy/master-strategy.md` and `strategy/sprint-backlog.md` if present.
5. Read this handoff.
6. Read the two committed Task 1 and Task 2 deliverables under `deliverables/phase-2-discovery/`.
7. Confirm readiness and the planned order of work in 4-6 bullets. Wait for Mike's approval before acting.

**Planned order for the fresh session:**
1. Write Task 3 deliverable (short). Commit.
2. Write Task 4 deliverable. Commit.
3. Write `context/08-affiliate-program.md`. Commit.
4. Compose synthesis message. This is a chat deliverable, not a file write unless Mike asks for a doc.
5. (Optional, if time) Retry Chile crawl with adjusted UA / spacing.

Approval gate: still APPROVE-EVERY-ACTION. Mike has not switched to weekly review mode.
