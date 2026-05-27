# Day 1 of 10/day production rhythm: 2026-05-28 startup

## Where we left off (2026-05-27 close)
- Year-specificity keyword refinement committed and pushed to origin/main
- Refined SCRIBE keyword discipline: year-specific exact-match primary keywords for year/cycle/season-bound products
- Refined product-page-playbook.md with the new discipline
- Refined SCRIBE agent.md Section 9 with year-specificity hierarchy
- work-log/follow-ups.md updated with re-keyword obligation for Liverpool v2 and Predator v2 (deferred)

## Tomorrow morning's first task
Begin Mexico kit set: 3 PDPs (Home, Away, Third) as the start of Day 1.

## Mexico kit set: URLs locked in (Phase 1 candidate selection complete from 2026-05-27)
- Home: /products/adidas-2026-mexico-mens-stadium-home-soccer-jersey
- Away: /products/adidas-2026-mexico-mens-stadium-away-soccer-jersey
- Third: /products/adidas-2026-mexico-mens-stadium-third-soccer-jersey

All three are Adidas Stadium tier (fan version), broader appeal than Authentic. All confirmed live on prosoccer.com via Firecrawl. All slugs already match year-specificity rule format.

## Production workflow shifts decided 2026-05-27 (apply going forward)

1. Per-PDP separate commits: preserves clean per-task history; 10 commits per production day
2. Cross-kit internal linking: Home brief ships with /collections/mexico + brand collection links; sibling Home-to-Away + Home-to-Third links added in follow-up commit after all 3 briefs complete
3. Drop per-PDP human gate review: ORIN runs PDPs sequentially without interruption; holds only at blockers; Mike reviews at natural breakpoints (typically end of kit set or end of day)
4. Quality discipline mandatory and non-negotiable: Step 0 tool verification, voice check, 11 internal gates, fact verification, currency check, sensitivity check, brand IP compliance, year-specificity keyword discipline
5. Brief output format unchanged from established minimal one-page pattern

## Mexico-specific context for the kit set

- Mexico is Adidas-licensed: FIFA terminology PERMITTED ("FIFA World Cup 2026", "World Cup 2026", "FIFA" all usable)
- Mexico is 2026 World Cup CO-HOST (along with US and Canada): major cultural anchor for H2 4
- Co-host context: automatic qualification (no qualifying campaign required), Estadio Azteca hosts (first stadium to host three World Cups), first World Cup ever co-hosted by three nations
- Manager: Javier Aguirre (verify still in charge via Tavily; appointed late 2024)
- Squad key players to verify current: Edson Álvarez (West Ham, likely captain), Hirving "Chucky" Lozano, Raúl Jiménez (Fulham), Santiago Giménez (Feyenoord/Milan), Memo Ochoa (may have retired by 2026, verify)
- Cultural references: El Tri, La Verde, FMF (Federación Mexicana de Fútbol)
- Prior Mexico work reference: deliverables/page-optimizations/2026-05-08_mexico-v3.md (collection page brief, NOT a PDP, different work product); companion topic research at .claude/agents/on-page-seo/briefings/2026-05-08_mexico-v3-topic-research.md available as context

## Three kit design details (from Phase 1 surfacing, verify via Tavily for accuracy)

- Home: deep green base
- Away: burgundy/white split with grecas patterns reminiscent of ancient temples
- Third: black colorway with all-over print, federation badge, adidas Trefoil + 3-Stripes "bedecked in the colors of the Mexican flag"

These details came from a WC2026 Top Kits blog (Home + Away) and the live PDP body content (Third). Verify and expand via Tavily research during brief production.

## Candidate selection discipline

Eligibility verification is now permanent workforce discipline per architectural codification in commit 9dd77e8 (2026-05-27). The canonical PDP version lives in `context/page-type-playbooks/product-page-playbook.md` 'Eligibility verification (mandatory pre-Phase-1)'; the collection version in `context/page-type-playbooks/collection-page-playbook.md` 'Eligibility verification (mandatory pre-Phase-1)'; SCRIBE applies it as Step 0.5 in `.claude/agents/on-page-seo/agent.md` Section 2; ORIN applies it at Phase 1 candidate surfacing in `.claude/agents/master-strategist/agent.md` Section 9; cross-reference in `context/workforce-conventions.md` 'Eligibility verification as logical extension of Step 0'.

Day 1 Step 0 of the sequence below applies the codified discipline to the Mexico kit URLs before brief production begins. If any Mexico kit candidate is sold out, surface as BLOCKER and hold at gate; Mike decides whether to swap to an alternative variant (Authentic tier, long-sleeve) or proceed under the closing-window strategic exception with explicit reasoning. The two documented closing-window exception examples (Liverpool 2024-25 Nike Away Jersey v2 at commit b7159dc and adidas Predator Accuracy.1 FG Crazyrush Pack v2 at commit d52e56f) are the only sold-out optimizations under the new discipline; both predate codification.

## Day 1 sequence
0. Step 0 (before Mexico Home dispatch): Firecrawl scrape all three Mexico kit URLs, confirm in-stock status for each, surface findings; Mike decides any swaps needed before brief production begins
1. Dispatch SCRIBE for Mexico Home brief
2. SCRIBE produces brief, commits, no Mike interruption unless blocker
3. Dispatch Mexico Away brief
4. Same pattern
5. Dispatch Mexico Third brief
6. Same pattern
7. After all 3 complete: follow-up commit adds sibling Home-to-Away + Home-to-Third internal links
8. Mike reviews the kit set as a batch; commits + push if approved
9. Continue Day 1 with next team (Argentina kit set) if time allows
10. End-of-day commit covers any remaining work

## Quality discipline checklist per PDP

- Step 0: Verify dfs-mcp + firecrawl-mcp + tavily-mcp exposure in SCRIBE
- Phase 1: Firecrawl scrape with 6-field extraction (Title, Slug, Meta Title, Meta Description, Short Description from metafield, Long Description body)
- Phase 2: DFS keyword research with year-specificity discipline (year-specific PRIMARY, generic SUPPORTING, document specificity reasoning)
- Phase 3: Tavily topic research scaled to product context
- Phase 4: Brief generation applying National Team Jersey CANONICAL template (4 H2s) + 5 canonical brief-craft rules + brand IP + currency check + sensitivity check + fact verification
- Phase 5: Voice check + 11 gates silent
- Phase 6: Hold at commit gate only if blocker found

## Long-term context
- 10 PDPs/day production target starting today
- Personal validation goal for methodology
- Architecture gaps will surface and need addressing as we go (batch dispatch, sheet automation via Drive MCP, GSC MCP install, Tavily paid plan after free tier exhausted day 17)
- Implementation in Shopify admin is parallel workstream; figure out delegation if needed

## Editor's note on this file
Mike's source text contained 6 structural em-dashes that were converted to colons or semicolons during file creation to satisfy voice_check.py. All conversions preserve operational meaning. If reverting to em-dashes is preferred (workforce-internal pragmatic exception per the briefing voice-check follow-up logged 2026-05-27 in work-log/follow-ups.md), restore from Mike's original message in the 2026-05-27 conversation transcript.
