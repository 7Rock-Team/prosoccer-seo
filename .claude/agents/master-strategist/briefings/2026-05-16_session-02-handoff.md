# ORIN Session 2 Handoff: Whitelabel Audit Pilot Continuation

- **Briefing date:** 2026-05-17 (work date 2026-05-16 reflected in the file name to align with the originating session)
- **From:** ORIN, Session 1 (2026-05-16, this same agent in prior conversation)
- **To:** ORIN, Session 2 (fresh context, picking up Collections #2 and #3)
- **Pilot:** Whitelabel audit + regen, Collections #2 and #3 of the 3-collection session pilot Mike originally scoped on 2026-05-16
- **Mike's instruction:** "Hand off Collections #2-#3 to fresh session. Write handoff briefing now."

This briefing is self-contained. A fresh ORIN session reads only this file (plus the startup-protocol context files it would read anyway) and picks up cleanly without needing the Session 1 conversation transcript.

---

## 1. The pilot in one paragraph

Mike's whitelabel team optimized 100+ collection pages and Mike wants the first 10 audited and regenerated through the workforce architecture as a pilot. Collections are processed one at a time, with GATE review after each. Session 1 covered Collection #1 (`/collections/2026-national-team-soccer-fan-gear`); Session 2 covers Collections #2 (`/collections/2026-national-team-soccer-accessories`) and #3 (`/collections/2026-national-team-soccer-scarves`). After all 3 collections complete, Session 1+2+3 together constitute the first deliverable of the audit pilot. The remaining 7 of the 10-page batch get scheduled separately based on what these 3 reveal.

## 2. What Session 1 produced (committed, unpushed; Mike pushes manually)

Two local commits on `main`, ahead of `origin/main` by 2 as of Session 1 end. Mike's Session 2 instructions in his 2026-05-17 prompt include a third commit covering the exception decision and folder-convention refinement; that commit lands at the end of Session 1's wrap-up before Session 2 starts.

### Commit `5109a52` (pushed by Mike): Brand IP constraint architecture

Mike pushed this commit at end of Session 1's architecture refinement gate. Files:

- `context/brand-ip-constraints.md` (new): hard legal constraint documenting that FIFA-trademarked terminology family ("World Cup", "FIFA World Cup", "WC", "FIFA" in commercial contexts) is restricted to Adidas-licensed page contexts. Federation-anchored substitution table provided. Per-team brand-affiliation verification step required during topic research.
- `context/page-type-playbooks/collection-page-playbook.md` and `product-page-playbook.md`: both gain a `## Brand IP Constraints` section referencing the constraints file.
- `.claude/agents/on-page-seo/agent.md`: Section 2 gains Step 4c (read constraints file, classify brand-affiliation, apply substitution language, run compliance scan); Section 11 Quality Gates gains Gate 11 (Brand IP compliance scan; constraint precedence is brand IP > voice rules because the consequence is legal exposure, not stylistic drift).

### Commit `2cc04fe` (pending Mike push): Whitelabel audit + regen Collection #1

Two files:

- `deliverables/page-optimizations/whitelabel-audit/2026-05-16_2026-national-team-soccer-fan-gear_audit-and-regen.md`: the full audit + regen for Collection #1. Worked example for Session 2. Use as a template. Brand-affiliation classification: brand-agnostic umbrella. Federation-anchored language throughout. 6 H2 + 6 FAQ body. 2 validated internal links. Slug stays per Mike's tournament-scoped lifecycle directive. Post-tournament redirect target: `/collections/national-teams`. Retirement trigger: inventory < ~50 products OR by 2026-10-31, whichever comes first.
- `.claude/agents/on-page-seo/briefings/2026-05-16_2026-national-team-soccer-fan-gear.md`: workforce-internal classification briefing per Step 4c. Documents brand-affiliation reasoning, substitution table applied, Gate 11 scan results, topic research summary, internal link validation, cost log.

**Note on folder location:** Collection #1's deliverable file is in the FLAT location `deliverables/page-optimizations/whitelabel-audit/` rather than the new date-stamped session folder. Session 2 starts using the new folder convention; Collection #1 stays where it is (no retroactive moves per `context/workforce-conventions.md`).

### Commit `ea332e3` (pending Mike push): URL architecture brand IP audit

One file:

- `deliverables/technical-fixes/2026-05-16_url-architecture-brand-ip-audit.md`: tier-classified audit of all collection slugs with FIFA-family terms. 22 slugs scanned (sitemap + GSC top-pages cross-reference). 10 Adidas-licensed (compliant). 15 non-Adidas violations. Tier A.1: 0. Tier A.2: 4. Tier A.3: 11. Original workforce slug-rename recommendations preserved as audit trail but SUPERSEDED by Mike's exception decision (see next commit).

### Next commit (Session 1 wrap-up, pending Mike push at time of this briefing's commit): URL audit exception + folder convention

Per Mike's 2026-05-17 directive. Files:

- `deliverables/technical-fixes/2026-05-16_url-architecture-brand-ip-audit.md`: updated to reflect Mike's exception decision (Tier A.2 and A.3 slugs stay as-is; copy-level compliance only).
- `context/brand-ip-constraints.md`: new `## Exceptions and grandfathered violations` section documents Mike's business decision.
- `.claude/agents/on-page-seo/agent.md`: Section 13 gains a "File path convention" subsection pointing to the new date-stamped session folder structure.
- `context/workforce-conventions.md` (new): folder structure convention + quarterly cleanup retention policy.
- This handoff briefing.

After Mike pushes this combined commit, the architecture state is fully landed and Session 2 can start cleanly.

## 3. State of the constraint architecture

Session 2 ORIN should treat the following as load-bearing context:

### Brand IP constraint (Step 4c + Gate 11)

Source: `context/brand-ip-constraints.md`. Adidas-licensed pages can use the FIFA terminology family. All other pages must use Federation-anchored substitution language. The year "2026" alone is permitted everywhere. Constraint precedence: brand IP > voice rules.

**Substitution table (most-used entries):**

| Restricted | Allowed alternative |
|---|---|
| "2026 World Cup" | "2026 tournament" / "2026 international tournament" / "the 2026 federation cycle" |
| "World Cup history" | "international tournament soccer has ever staged" |
| "World Cup scarves" | "Federation scarves" |
| "World Cup branding" | "tournament branding" |
| "World Cup window" | "tournament window" |
| "FIFA's official store" | (remove or reframe without commercial FIFA invocation) |
| "World Cup squad" | "Federation roster" / "national team squad" |
| "World Cup kit" | "Federation kit" / "national team kit" / "2026 federation jersey" |
| "WC 2026" | "2026" alone |

### Exceptions and grandfathered violations

Source: `context/brand-ip-constraints.md` `## Exceptions and grandfathered violations` section (added per Mike's 2026-05-17 decision). Existing slugs with FIFA terminology violations stay as-is to avoid any equity risk from URL changes. Customer-facing copy on those pages still required to be in compliance.

This means: if Session 2 ORIN encounters Collection #2 or #3 with a FIFA-term slug, the slug stays. Only the customer-facing copy (Title, Meta Title, Meta Description, Short Description, Long Description, internal link anchors) gets brought into compliance.

### Folder structure

Source: `context/workforce-conventions.md`. All Session 2 deliverables land in `deliverables/page-optimizations/whitelabel-audit/2026-05-17_session-02/` (or whatever date Session 2 actually runs; the folder name matches the session start date).

Folder pattern: `YYYY-MM-DD_session-NN/`. Session 2 ORIN creates the folder at session start.

### Workforce-internal briefings

Per-collection workforce-internal briefings (SCRIBE classification reasoning per Step 4c) continue to land in `.claude/agents/on-page-seo/briefings/YYYY-MM-DD_<slug>.md`. NOT in the page-optimization session folder.

## 4. Per-collection workflow (as run for Collection #1)

Five phases per collection. See Collection #1's deliverable for the worked example: `deliverables/page-optimizations/whitelabel-audit/2026-05-16_2026-national-team-soccer-fan-gear_audit-and-regen.md`.

### Phase 1: Audit existing live page

Use Firecrawl MCP `mcp__firecrawl-mcp__firecrawl_scrape` with a targeted JSON schema (not raw markdown; the raw scrape returns 1.6M+ characters and breaks context). Capture: Title, URL slug, SEO Meta Title (with char count), SEO Meta Description (with char count), Short Description, Long Description (verbatim, full text), H2 headings, internal links (with anchor text + destination URLs), schema markup if visible, product count.

JSON-format scrape works in one call; see Collection #1 audit for the schema pattern. Capture brand-affiliation classification of the page (Adidas-only / non-Adidas / brand-agnostic umbrella) immediately upon reading the live state.

Evaluate findings against: collection-page-playbook subject focus rules, six principles, internal link strategy, brand IP constraint compliance scan.

### Phase 2: Regenerate brief from scratch

Topic research via Tavily MCP `mcp__claude_ai_Tavily__tavily_search` (5-15 queries). Use Federation-anchored language throughout if the page is non-Adidas-classified. For Collections #2 (accessories umbrella) and #3 (scarves), classification is likely brand-agnostic umbrella (same as Collection #1).

Generate brief in the simplified format from `templates/consolidated-page-brief-template.md`:

- Title (Collection Title)
- Short Description (emotion-first, 50-80 words)
- Long Description (4-6 H2 sections + FAQ; 200-500 words body)
- Internal links (1-2 max, validated via Firecrawl)
- SEO Meta Title (with char count)
- SEO Meta Description (with char count)
- Slug recommendation (for tournament-scoped 2026 pages: no change recommended; post-tournament redirect target proposed)
- Avatar scope
- Keywords

Output to `deliverables/page-optimizations/whitelabel-audit/YYYY-MM-DD_session-02/<slug>_audit-and-regen.md`.

Workforce-internal briefing to `.claude/agents/on-page-seo/briefings/YYYY-MM-DD_<slug>.md`.

### Phase 3: Side-by-side comparison

Append a field-by-field comparison table (Title, Slug, Meta Title, Meta Description, Short Description, Long Description, Internal links) with: whitelabel current state, workforce proposed, recommendation per field (Use workforce / Keep whitelabel / Hybrid), reasoning.

### Phase 4: Voice check + 11-gate self-verify

`voice_check.py` on the deliverable. Run the 11 SCRIBE Quality Gates per `.claude/agents/on-page-seo/agent.md` Section 11. Gate 11 brand IP scan is the load-bearing addition for tournament-scoped or non-Adidas pages.

### Phase 5: Hold at GATE for Mike review

Surface: audit findings, workforce-regenerated brief, side-by-side comparison, post-tournament redirect target proposal, voice check + gate status, pattern observations.

Mike's options: Approve workforce / Keep whitelabel / Hybrid / Refine workforce.

After approval, commit (don't push). Mike pushes manually.

## 5. Collections #2 and #3: specific context

Per Mike's original Session 1 prompt:

### Collection #2: `/collections/2026-national-team-soccer-accessories`

Live URL: `https://www.prosoccer.com/collections/2026-national-team-soccer-accessories`. Tournament-scoped umbrella. Likely brand-agnostic classification (covers federations across multiple kit suppliers). FIFA terminology family forbidden in customer-facing copy. Slug stays per tournament-scoped lifecycle directive. Post-tournament redirect target likely `/collections/national-teams` (same as Collection #1) or a more specific accessories-evergreen successor; ORIN proposes during Phase 2 brief generation.

### Collection #3: `/collections/2026-national-team-soccer-scarves`

Live URL: `https://www.prosoccer.com/collections/2026-national-team-soccer-scarves`. Tournament-scoped umbrella, scarves-specific. Same brand-agnostic classification expected. Same FIFA terminology constraint. Slug stays per directive. Post-tournament redirect target likely `/collections/scarves` or `/collections/national-teams` depending on what's live and how the evergreen scarves collection is structured; ORIN validates via Firecrawl during Phase 2.

### Known patterns to expect (from Collection #1 audit)

The whitelabel pattern observations Session 1 found will likely repeat:

1. AI-cliche openers ("Get ready for...", "Shop the latest...", "Find styles built for...")
2. Meta description shipping CTA ("Free shipping on orders over $100!")
3. Flat 3-paragraph body with no H2 hierarchy
4. 3+ internal links with exact-match anchor stuffing
5. Catalyst pages that don't name the catalyst
6. Store leakage into body copy ("Pro Soccer makes it easy to shop")
7. FIFA-trademarked terminology on non-Adidas pages (brand IP violation)

Session 2 ORIN watches for all 7 and documents which repeat. Pattern observations log consolidates across all 3 pages in this session, planned for `.claude/agents/on-page-seo/briefings/2026-05-17_whitelabel-audit-patterns.md` at end of Session 2 (per Session 1's original session-deliverable spec).

## 6. Costs and constraints for Session 2

### Firecrawl envelope

100 credits/month for SCRIBE (per `.claude/agents/on-page-seo/agent.md` Section 12). Session 1 used ~15 credits across 3 scrape calls. Session 2 expects ~10-20 credits across the 2 collection audits + 4-6 internal link validation scrapes. Well within envelope.

### Tavily research budget

No hard quota documented; ~6 queries per collection is normal. ~12-15 queries total expected for Session 2.

### Context budget

Session 1 hit context pressure in the final third (post-URL audit). Session 2 starts fresh. Recommended discipline: complete Collection #2 fully (Phases 1-5 + commit) before starting Collection #3. If context pressure builds during Collection #3, write a Session 3 handoff briefing rather than rush.

### Approval mode

APPROVE-EVERY-ACTION per CLAUDE.md. Session 2 ORIN holds at each per-collection GATE for Mike's approval before committing.

## 7. Session 2 startup checklist

Fresh Session 2 ORIN should:

1. Read this briefing in full.
2. Run the SCRIBE startup protocol (`.claude/agents/on-page-seo/agent.md` Section 2 steps 1-11) since per-collection workflow is SCRIBE-led with ORIN orchestrating.
3. Verify the four Session 1 commits are present in local git history: `5109a52` (architecture, pushed by Mike), and the three Session-1 commits pending Mike push: `2cc04fe` (Collection #1), `ea332e3` (URL audit), plus the wrap-up exception+convention commit Session 1 produces just before this handoff lands.
4. Create the Session 2 folder: `deliverables/page-optimizations/whitelabel-audit/YYYY-MM-DD_session-02/` where YYYY-MM-DD is Session 2's actual start date.
5. Confirm with Mike: per-page mode (Collection #2 → GATE → commit → Collection #3 → GATE → commit) is still the workflow, or has Mike changed the cadence.
6. Begin Phase 1 of Collection #2.

## 8. Open follow-ups (not blocking Session 2)

These items routed to VERITAS during Session 1 and remain pending separate VERITAS briefs:

1. **VERITAS visibility investigation** for 4 live-but-not-in-sitemap collections discovered during URL audit (`/collections/2026-fifa-world-cup`, `/collections/2026-fifa-world-cup-qualified-teams`, `/collections/2026-fifa-world-cup-qualified-teams-accessories`, `/collections/nike-2026-fifa-world-cup-soccer-jerseys`). Mike approved as separate brief.
2. **VERITAS sitemap-refresh script enhancement** to add brand IP scan to `scripts/_build_sitemap_state.py`. Mike approved as separate brief.
3. **Schema injection for Collection #1** (CollectionPage + BreadcrumbList + FAQPage JSON-LD). Mike acknowledged as separate VERITAS brief; not blocking.
4. **Copy-compliance follow-up for the 15 grandfathered slug-violation URLs**. Riding on the ongoing whitelabel audit-and-regen workflow; will happen incrementally as ORIN reaches each page. No standalone remediation pass needed.

These are documented for visibility, not for Session 2 action.

## 9. End-of-session deliverable structure (for after all 3 collections complete)

Per Mike's original Session 1 prompt:

- 3 individual audit-and-regen files in the session folders (1 in `whitelabel-audit/` flat per Session 1's pre-convention state, 2 in `whitelabel-audit/YYYY-MM-DD_session-02/` per the new convention)
- Pattern observations log at `.claude/agents/on-page-seo/briefings/YYYY-MM-DD_whitelabel-audit-patterns.md` consolidating findings across all 3 pages
- Session summary ready for Mike to push commits

When Session 2 wraps Collection #3, the 3-collection pilot deliverable is complete. Mike then decides whether to expand the audit to the remaining 7 of the original 10-page batch or pivot to other work.

---

End of briefing.
