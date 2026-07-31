# Workforce Conventions

This file documents cross-agent operational conventions for the ProSoccer SEO workforce. Conventions here apply to all agents (ORIN, KIRA, VERITAS, SCRIBE, SAGE if built, RECON, METRIK) and are read at startup alongside `context/00-business-overview.md`, `context/03-brand-voice.md`, `context/04-customer-avatars.md`, and `context/brand-ip-constraints.md`.

When a convention in this file conflicts with an agent-specific rule in `.claude/agents/<agent-name>/agent.md`, the convention here is the default; the agent-specific rule overrides only when it is explicit about doing so.

## Page optimization deliverable folder structure

All page-optimization deliverables produced during a session (whitelabel audits, per-page briefs, regenerated briefs, comparison docs) land in a date-stamped session folder under `deliverables/page-optimizations/`. The structure is:

```
deliverables/page-optimizations/
  whitelabel-audit/
    YYYY-MM-DD_session-NN/
      <slug>_audit-and-regen.md
      <slug-2>_audit-and-regen.md
      ...
  YYYY-MM-DD_session-NN/
    <SKU>_<slug>_brief.md
    ...
```

### Naming convention

- **Folder name pattern:** `YYYY-MM-DD_session-NN/` where YYYY-MM-DD is the session start date and NN is a zero-padded two-digit session ordinal within the work-unit (e.g., `01`, `02`, `03`).
- **Work-unit boundary:** a "session" is a single ORIN-orchestrated work unit (Mike's prompt to the agent, the agent's execution, and the GATE review or completion). Multi-session work units (e.g., a 3-collection whitelabel audit pilot) get a session folder per session.
- **Examples:**
  - `deliverables/page-optimizations/whitelabel-audit/2026-05-16_session-01/` (whitelabel audit pilot, session 1)
  - `deliverables/page-optimizations/whitelabel-audit/2026-05-17_session-02/` (whitelabel audit pilot, session 2)
  - `deliverables/page-optimizations/2026-06-01_session-01/` (a non-whitelabel batch of per-page briefs)
- **Brief filename pattern (SKU-first, added 2026-06-15):** `[SKU]_[descriptive-handle]_brief.md`. The SKU LEADS the filename because SKU is the operationally relevant identifier when Mike looks products up in Shopify admin; the descriptive handle is secondary. Example: `IO8225-900_nike-vapor-17-pro-firm-ground-soccer-cleats-breakout-pack-su26_brief.md`. Separator: a single underscore between SKU and handle (matching the existing `_brief.md` suffix convention). SKU formatting: use the SKU exactly as it appears in the white-label sheet / Shopify admin, preserving hyphens, dashes, and suffix variants (`IO8225-900`, `J000693-CRFT`, `JR5386`, `IH4571`); no case conversion, no character substitution. Forward-only: the existing 20 brief files (Day 3 + Batch 2, at `2026-06-08_session-01/` and `2026-06-10_session-01/`) keep their current handle-first filenames; Batch 3 onward complies.

### Session folder creation

The session folder is created at session start if it does not already exist. ORIN creates the folder via the orchestrator's first file write of the session. Specialist agents (SCRIBE, KIRA, etc.) write into the session folder ORIN has established.

### Workforce-internal briefings

Per-page workforce-internal briefings (SCRIBE classification reasoning, KIRA keyword research notes, etc.) continue to live in agent-specific briefings folders: `.claude/agents/<agent-name>/briefings/YYYY-MM-DD_<slug>.md`. These are agent-internal and not part of the page-optimization deliverable folder.

### Historical / pre-convention files

Existing flat-directory deliverables (e.g., `deliverables/page-optimizations/2026-05-08_mexico-v3.md`) stay where they are. Do NOT retroactively move historical files into session folders. The convention applies going forward; the audit trail of the convention transition is the git history.

## Fresh Optimization workflow (default mode, minimal format as of 2026-05-26 round 2)

Fresh Optimization is the default workflow for page-optimization deliverables produced by SCRIBE under ORIN orchestration. The whitelabel audit mode is opt-in and used only when Mike explicitly requests it. **Target: the visible brief fits on one Google Doc page.**

### Workflow steps

1. Load context: page-type playbook matching the page (`context/page-type-playbooks/`), `context/brand-ip-constraints.md`, the six copy-writing principles in `context/03-brand-voice.md`.
2. Read current state for SCRIBE's own context, but do NOT capture it in the brief:
   - **Collection pages:** SCRIBE pulls current copy via the Firecrawl MCP (`mcp__firecrawl-mcp__firecrawl_scrape`) for context. Current state does NOT appear in the visible brief.
   - **Product pages:** SCRIBE pulls all six fields (Title/H1, slug, Meta Title, Meta Description, Short Description, Long Description) via the Firecrawl MCP scrape of the live PDP. Short Description is rendered as the first paragraph in the description body on ProSoccer's Hyper theme (stored as a Shopify metafield); the scrape captures both Short and Long Description in a single call. Mike does NOT paste PDP body content; the live page is source of truth. If the scrape does not produce a clean Short / Long Description separation, surface as a blocker BEFORE drafting the brief per `context/page-type-playbooks/product-page-playbook.md` 'Current state capture (Shopify Hyper theme on ProSoccer)'. Current state does NOT appear in the visible brief.
   - **Mike references Shopify admin directly for current state during implementation.** The brief is forward-looking only.
3. Keyword research via DataForSEO MCP (mandatory, data-backed). The workforce-internal briefing carries the full keyword research workup; the visible brief surfaces only the chosen primary keyword (volume + KD) and the supporting long-tail set as a comma-separated list with optional volume.
4. **Current ranking lookup via DataForSEO SERP API (mandatory).** Run `mcp__dfs-mcp__serp_organic_live_advanced` for the chosen primary keyword; identify whether the target URL appears in the top 100 organic results; capture position OR "not in top 100." Surface as a one-line `Current ranking:` entry in the visible Keyword research block. Apply the ranking-aware posture (see 'Ranking-aware posture' subsection below) before drafting recommendations. GSC MCP is the long-term ranking source of record (installed 2026-06-09, Category A); its Phase 1 workflow integration is deferred to Commit 4, so DataForSEO SERP API remains the current ranking method until then.
5. Topic research via Tavily / WebSearch scaled to familiarity:
   - Well-known topics (Mexico, Argentina, major brands): 2 to 5 queries.
   - Unfamiliar topics: 5 to 10 queries.
   - Do not over-research what prior sessions already documented. Findings live in the workforce-internal briefing, not the visible brief.
6. Generate the optimized brief in the format at `templates/consolidated-page-brief-template.md`. Default visible content is the minimal Keyword research block (including Current ranking line and top-5 WARNING line where applicable) and the Recommended new SEO setup block, nothing more. No Current state section. No Source of record paragraph. No Alternatives considered section. No External links field on PDPs. No LLM ranking field (deferred).
7. Validate every proposed internal link via the firecrawl skill (status code 200, page-type signals confirmed, no soft-404) per the matching playbook's link strategy (1 to 2 max).
8. Run voice check (`scripts/voice_check.py`) and the 11 gates from `.claude/agents/on-page-seo/agent.md` Section 11 silently. Pass results are NOT surfaced in the visible brief; only an unresolvable failure surfaces to Mike. All gate results are documented in the workforce-internal briefing at `.claude/agents/on-page-seo/briefings/YYYY-MM-DD_<slug>.md`.
9. Hold at GATE for Mike review.
10. Append the matching row to `deliverables/tracking/collections-master.csv` or `products-master.csv` once Mike approves.

### Ranking-aware posture

The Current ranking position governs how aggressively SCRIBE iterates on Title and H1 copy.

- **Top 5:** WARNING required in the visible brief. The line reads: "Page currently ranks top 5. Title/H1 changes carry equity risk. Confirm with Mike before shipping changes to these fields." Recommendations preserve exact-match phrasing of the primary keyword in Title and H1; copy iteration leans toward Meta Description, Short Description, and Long Description where equity risk is lower.
- **Top 6 to 20:** Standard recommendations. Current position noted for context. No warning line.
- **Top 21 to 100:** Standard recommendations. Current position noted for context.
- **Not ranking (not in top 100):** Standard recommendations. Treated as opportunity for a fresh ranking attempt.

**LLM ranking is deferred.** LLM visibility tooling (ChatGPT citation rates, Claude / Gemini surfaces, AI Overview presence) is immature today. Revisit in 6 months when the category matures and the tooling becomes practical. Do not include an LLM ranking field in the brief.

### Workforce-internal briefing (preserved scope, current state removed)

The workforce-internal briefing at `.claude/agents/on-page-seo/briefings/YYYY-MM-DD_<slug>.md` continues to capture: brand-affiliation classification, avatar scope, topic research findings, compliance scan results, per-string voice check status, 11-gate self-verify status, cost tracking, data provenance / source-of-record (DataForSEO calls, locations, timestamps, status codes), alternatives considered with rejection reasoning, intent percentages, trend data, per-element expected lift bands, validation plans, severity, confidence, schema dependency flags, cross-agent voice flags, and any other workforce-internal context. Mike can request the briefing on demand at any time. It is not surfaced at gate review by default.

**Current state is not captured in the workforce-internal briefing.** Mike sees current state directly in Shopify admin during implementation; Shopify's own field history preserves the audit trail. Duplicating current state in the briefing adds no audit value.

### Optional mode: Whitelabel audit

The whitelabel audit mode adds a `## Comparison with current state` section to the brief before the Recommended new SEO setup block, showing field-by-field deltas with reasoning. The audit mode is the only context where the brief carries current-state strings inline. This mode is opt-in. Mike must explicitly request "whitelabel audit" (or equivalent phrasing) for the comparison section to appear in the brief. Without an explicit request, Fresh Optimization with no comparison narrative is the default.

### Simplifications baked into Fresh Optimization (round 2, 2026-05-26)

1. Brief target is one Google Doc page; the format is minimal by construction.
2. Current state section removed from visible brief and from workforce-internal briefing.
3. Source of record paragraph removed from visible brief; data provenance lives in workforce-internal briefing only.
4. Alternatives considered with rejection reasoning removed from visible brief; lives in workforce-internal briefing.
5. Keyword research block strips intent percentages and trend data from visible brief; lives in workforce-internal briefing.
6. External links field omitted on PDPs entirely (PDP link policy is internal-only, locked).
7. Topic research scales to familiarity rather than running a fixed query count per page.
8. Voice check and the 11 gates run silently; pass results do not surface; only unresolvable failures get flagged to Mike.
9. No comparison table or audit narrative in the visible brief unless whitelabel audit mode is requested.
10. For batched sessions, context loads once per session, not per page.

## Five canonical brief-craft rules (cross-reference)

Five rules govern every brief SCRIBE produces under the Fresh Optimization workflow. The rules are canonical in both page-type playbooks: `context/page-type-playbooks/product-page-playbook.md` 'Five canonical brief-craft rules' and `context/page-type-playbooks/collection-page-playbook.md` 'Five canonical brief-craft rules'. The five rules sit alongside the prior canonical policies (PDP external link policy, internal-links 1 to 2 target) which remain in force in their existing playbook sections. Quick index:

1. **Supporting keywords distributed as semantic variants in body** (1 to 2 natural appearances per variant from the brief's Keyword research block, no stuffing).
2. **Primary keyword in at least one H2 header** (natural integration; restructure the H2 rather than force the keyword).
3. **Meta description structure** (commercial intent + trust signal + emotional CTA; tier-aware language for branded products: never combine tier words like "Authentic Stadium").
4. **Named entities in body copy serve LLM search discoverability** (5 to 10 specific named entities per page where natural: players, federations, tournaments, signature product lines, signature features, locations, managers).
5. **Short Description structure** (primary keyword in sentence 1 or 2; avatar identity hook in first half; 2 to 3 differentiating specifics; CTA close distinct from Meta Description; 200 to 300 chars target).

Worked example for all five rules: UAE 2026 PDP v3 brief at `deliverables/page-optimizations/2026-05-26_session-01/uae-2026-home-stadium_brief-v3.md`.

**Category-specific H2 templates** for 15 product categories ProSoccer sells live in `context/page-type-playbooks/product-page-playbook.md` 'Category-specific H2 templates'. National-team-jersey template is CANONICAL, four-time validated within the 2026 World Cup cycle (UAE 2026 Home + Mexico 2026 Home / Away / Third per commits `e56a7d6`, `85dd1f0`, `f2c2c34`); remaining categories are at various validation stages from DRAFT v1 to CANONICAL per the playbook.

## Anti-stuffing discipline (Gate 13, cross-cutting)

Anti-stuffing discipline (Gate 13, added 2026-06-02): Quality issue surfaced in Day 2 batch #1 URL #2 (national-team-accessories) Title field "National Team Soccer Accessories: Scarves, Hats, Bags, Flags & Balls". Comma-stacked keyword list pattern reads as keyword stuffing regardless of whether individual items are technically relevant to the page. Signals to Google quality systems (Helpful Content Update, Spam Updates) and degrades user CTR even at same rank position. Workforce discipline: product category breadth belongs in body H2 framework and Long Description body copy, not in Title or Meta Title fields. Each output field should read as natural language a human would write.

**Gate 13 is its own gate, not folded into the Gate 1 / Gate 2 voice check.** The voice check governs prose voice and forbidden characters; Gate 13 governs structural keyword-stuffing patterns. It is also distinct from Gate 12 keyword distribution, which caps over-repetition of a single keyword across fields. Gate 12 catches one keyword repeated too often; Gate 13 catches a single field shaped as a list of many adjacent keywords. Distinct concerns, distinct gates. Gate 13 sits after Gate 12; the workforce gates suite runs 13 gates as of 2026-06-02 (previously 12).

**Applies to ALL output fields, not just titles:** Title, Meta Title, Meta Description, Short Description, Body / Long Description (including H2s and H3s), internal link anchor text, FAQ questions and answers when included.

Seven anti-patterns flagged (1 through 5 apply in any field; 6 and 7 are body-copy patterns added 2026-06-02 with the Gate 13 scope extension):

1. **Comma-stacked keyword lists** (`[Topic]: keyword1, keyword2, keyword3 & keyword4` or `[Topic] - A, B, C, D`). Any field with 3+ comma-separated keywords fails.
2. **Ampersand-terminated lists** (trailing `& [final keyword]` on a comma list).
3. **Synonym stacking** (jerseys / shirts / kits / tops; cleats / `boots` / shoes). One canonical term per field.
4. **Modifier stacking** (audience: Men's / Boys' / Youth / Kids'; product: Authentic / Replica / Stadium / Match-Worn).
5. **Brand stacking in titles** (adidas, Nike, Puma listed in one title when only one or two are relevant).
6. **Price stacking in body copy.** Specific dollar amounts in collection or product page body copy. Surfaced in Day 2 batch #1 URL #1 Long Description pricing block (6 specific dollar amounts: "Caps run around $34.99... Scarves run $24 to $44. Flags run $44.99; Mimi Imports country flags run $19.99... Bags land between $30 and $80."). Use tier / positioning language instead; see 'Content evergreen-ness' below.
7. **Brand stacking in body sentences.** 3+ comma-separated brand names in a single sentence within Body Description. Surfaced in Day 2 batch #1 URL #1 Long Description opening sentence (7 comma-separated brands: "adidas, Nike, Puma, Wincraft, Mimi Imports, Logo Brands, and Fan Ink each carry federation-licensed pieces."). Brand breadth belongs in faceted filters and product cards; body copy mentions individual brands only when narrative justifies (one or two per sentence, with role-specific context).

Defense-in-depth: SCRIBE runs the Gate 13 self-check during Phase 4 (brief drafting) before the Phase 5 voice check and self-revises any failing field; ORIN re-checks at the orchestrator layer (the same defense-in-depth posture as the independent voice check), flagging any field with 3+ comma-separated keywords, any body copy with 3+ dollar amounts, or any body sentence with 3+ comma-separated brands for SCRIBE revision. Collection pages carry particular emphasis because a collection aggregates multiple product categories, brands, and price points by definition and is the page type most prone to comma-stacking, price-stacking, and brand-stacking.

**Fix-forward scope.** Day 2 batch #1 (the 10 collection briefs already shipped 2026-05-29) is NOT fix-forwarded per Mike's call (2026-06-02); Mike applies the disciplines manually during Shopify admin implementation. This codification is forward-applicable to all future batches (Day 3+).

Cross-references: `context/page-type-playbooks/product-page-playbook.md` 'Anti-stuffing discipline (Gate 13, added 2026-06-02)' (canonical version with stuffed-vs-natural examples, pricing discipline, brand mention discipline), `context/page-type-playbooks/collection-page-playbook.md` 'Anti-stuffing discipline (Gate 13, added 2026-06-02)' (collection emphasis), `.claude/agents/on-page-seo/agent.md` Section 11 Gate 13 + Section 9 'Anti-stuffing discipline' (SCRIBE Phase 4 self-check), `.claude/agents/master-strategist/agent.md` Section 9 trust-but-verify + Section 11 Gate 9 (ORIN defense-in-depth re-check). See also 'Content evergreen-ness' and 'Brand styling conventions' below.

## Content evergreen-ness

Content evergreen-ness (added 2026-06-02 with Gate 13 extension): Body copy on collection and product pages should not contain specific prices, specific inventory levels, or other ephemeral data points that decay quickly. Pricing information belongs in PDPs, product cards, and schema markup where Shopify automatically maintains accuracy. Body copy should use tier/positioning language ("entry-level," "mid-tier," "premium," "collector") that remains accurate as catalog prices shift. Same principle applies to brand breadth: brand stacking in body sentences belongs in faceted filters and product cards, not body prose. Body copy mentions individual brands only when narrative justifies (one or two per sentence, with role-specific context).

Why it matters operationally: prices decay fast (sales, retail adjustments, discontinuations); stale prices in body copy create user trust issues (body says $34.99, the PDP shows $39.99); specific prices carry no SEO ranking benefit for category-intent queries; body copy with stacked dollar amounts reads as a price catalog, not editorial; and every price change otherwise ripples into a body-copy maintenance edit. The same decay logic applies to any ephemeral data point (live inventory counts, "currently X in stock," time-bound promo figures).

Cross-references: 'Anti-stuffing discipline (Gate 13, cross-cutting)' anti-patterns 6 and 7 above; `context/page-type-playbooks/product-page-playbook.md` 'Pricing discipline (body copy)' + 'Brand mention discipline (body copy)'; `context/page-type-playbooks/collection-page-playbook.md` same subsections.

## Brand styling conventions

Some brands have non-standard capitalization as part of their official trademark identity. This section is the registry; it accumulates as other brand styling rules surface (eBay, iPhone, DeepL, etc.). Each rule applies to ALL output fields: Title, Meta Title, Meta Description, Short Description, Body Description (H2s, H3s, body prose), internal link anchor text, and FAQ questions and answers.

### adidas (always lowercase)

"adidas" is ALWAYS lowercase, regardless of position in a sentence, including sentence start. The lowercase 'a' is part of adidas's registered trademark identity (Bauhaus design heritage from Adi Dassler). There is no exception: adidas is lowercase even at sentence start. If a sentence-start placement feels awkward, restructure the sentence rather than capitalize.

Correct:

- "adidas snapback caps span the federation roster"
- "Federation gear from adidas, Wincraft, and Mimi Imports anchors the lineup"
- "The 2026 home kits are produced by adidas under FIFA license"
- Sentence-start: "adidas covers the cap and bag categories."

Incorrect (do not use):

- `Adidas snapback caps...` (auto-capitalized at sentence start)
- `ADIDAS Mexico Home Jersey` (all-caps)
- `Adidas, Nike, and Puma...` (auto-capitalized in a list)

Restructure pattern (light-touch; don't force unnatural phrasing just to avoid sentence-start):

- Awkward: "adidas covers cap silhouettes across the federation roster."
- Restructured: "Cap silhouettes from adidas span the federation roster."

Both are valid; pick whichever reads more naturally for the surrounding copy.

Enforcement (defense-in-depth): SCRIBE checks adidas lowercase styling during Phase 4 drafting and restructures sentence-start placements rather than capitalizing; ORIN's orchestrator-layer re-check flags any `Adidas` (capitalized) in any output field; `scripts/voice_check.py` enforces a `\bAdidas\b` = FAIL regex at script level (mirrors the em-dash and forbidden-word checks), which catches the most likely failure mode (sentence-start auto-capitalization, a model-level tendency).

Cross-references: `.claude/agents/on-page-seo/agent.md` Section 9 'Brand styling discipline' + Section 11 brand styling check, `.claude/agents/master-strategist/agent.md` Section 9 trust-but-verify + Section 11 Gate 10, `scripts/voice_check.py` (`\bAdidas\b` regex), both page-type playbooks 'Anti-stuffing discipline' cross-references.

Regex implementation note (`scripts/voice_check.py`): The `\bAdidas\b` capitalization check uses targeted exemptions to avoid false positives on workforce-internal taxonomy compounds (`Adidas-only`, `non-Adidas`, `Adidas-licensed`), pedagogical anti-pattern demonstration lines, and code-fenced or backticked demonstration content. The check catches the primary failure mode (sentence-start auto-capitalization in real output copy) without breaking on legitimate internal references. Implementation: a negative lookbehind for hyphen and backtick, a negative lookahead for hyphen+word char, plus a per-line skip when the line carries a pedagogical marker (INCORRECT, DO NOT USE, anti-pattern, STUFFED:, wrong:, bad example).

Known follow-up (no proactive sweep): the other repo files that contain capitalized `Adidas` (roughly 59 `.md` files outside the five edited in this codification, mostly shipped deliverable briefs Mike chose not to fix-forward) are NOT touched here. The `\bAdidas\b` check catches any violation at the modification point; each file reconciles case-by-case at its next edit per natural editing cycles. No repo-wide rewrite is needed or wanted.

### Architectural learning notes (2026-06-02)

**Brand styling discipline (added 2026-06-02 with Gate 13 extension):** Some brands have non-standard capitalization as part of their official trademark identity. adidas is the canonical example, always lowercase, including sentence-start. Workforce discipline: SCRIBE never auto-capitalizes adidas; if sentence-start would feel awkward, restructure the sentence rather than capitalize. ORIN defense-in-depth re-check flags any `Adidas` (capitalized) in output fields. voice_check.py regex check enforces at script level. As other brand styling rules surface, add to this section.

**Content evergreen-ness (added 2026-06-02 with Gate 13 extension):** Body copy on collection and product pages should not contain specific prices, specific inventory levels, or other ephemeral data points that decay quickly. Pricing information belongs in PDPs, product cards, and schema markup where Shopify automatically maintains accuracy. Body copy should use tier/positioning language ("entry-level," "mid-tier," "premium," "collector") that remains accurate as catalog prices shift. Same principle applies to brand breadth: brand stacking in body sentences belongs in faceted filters and product cards, not body prose. Body copy mentions individual brands only when narrative justifies (one or two per sentence, with role-specific context).

## US Market Language Discipline (added 2026-06-03)

ProSoccer's customer base is predominantly USA, then Canada, then global. Body copy must use US-market soccer language, not UK or global equivalents. This is a market-localization extension of the reader-first principle: the avatar searches with US-market terms (`soccer cleats`, not `football boots`), reads with US-market expectations, and responds to US-market emotional anchors (the Saturday morning club game, the high school season, college recruitment, an MLS aspiration). UK or global conventions in body copy create subtle dissonance that undermines the reader-first orientation codified in commit dcfe6da (see 'Editorial philosophy (added 2026-06-02)' above).

### The footwear-term rule (priority codification)

In body copy on ProSoccer pages, `cleat` / `cleats` is the primary term for soccer footwear. `shoe` / `shoes` is an acceptable secondary term for variation. `boot` / `boots` is FORBIDDEN in body copy when referring to soccer footwear.

The rule applies to every output field: Title, Meta Title, Meta Description, Short Description, Body Description (H2s, H3s, body prose), internal link anchor text, and FAQ questions and answers.

Incorrect (UK/global, do not use):

- `the boot family adidas players wear`
- `the fastest boot Nike has ever built`
- `Nike's flagship boot`
- `football boot`
- `soccer boot`

Correct (US market):

- `the cleat family adidas players wear`
- `the fastest soccer cleat Nike has ever built`
- `Nike's flagship cleat`
- `soccer cleat`
- `soccer shoe` (acceptable for variation)

### H2 title casing and Product Details H2 format (split discipline, added 2026-06-17)

Body Description H2 casing splits by H2 function. **Editorial body H2s (overview/hook, tech-build/heritage, use-case/who-it's-for) use SENTENCE case** -- first word and proper nouns capitalized, "adidas" lowercase even at H2 start, brand abbreviations as-is (FG, AG, MG, IC), everything else lowercase. This is the deliberate editorial voice (Batch 2 house style), restored as standard after Batch 3 drifted to Title Case; it reads as real human writing and aligns with the reader-first principle. **Structural / navigational H2s use Title Case** -- "FAQs about [Short Product Name]", "Product Details: [Short Product Name]", "Care and Maintenance" -- because these are wayfinding landmarks buyers scan for. Title Case lowercases short articles / prepositions / conjunctions mid-title (about, and, the, for, of, to, in, on, by); "adidas" stays lowercase always; abbreviations as-is.

**Product Details H2 format (added 2026-06-17):** `Product Details: [Short Product Name]`. "Product Details" leads as the UX-scannable label; the natural short product name (NOT the full primary keyword, to avoid awkward lowercase brand casing) is appended after a colon for light topical reinforcement (e.g. "Product Details: F50 Elite FG"). H3 bullet structure unchanged.

The split reflects function: editorial prose H2s carry voice (sentence case), structural label H2s carry wayfinding (Title Case). Forward-only from Batch 4. Full rule and examples: `context/page-type-playbooks/product-page-playbook.md` 'H2 title casing: split discipline (added 2026-06-17)' and 'Description structure'.

**Enforcement (three layers, updated 2026-06-29).** (1) SCRIBE Phase 4 self-check and (2) ORIN Gate 15 cover BOTH directions of drift: Title-Case drift in editorial body H2s and sentence-case drift in structural H2s. (3) `scripts/voice_check.py` adds a deterministic backstop for the one direction that surfaced in production: it flags lowercase-initial editorial body H2s (the region between the `### Description` and `## Product Details` markers), with "adidas" the sole exception. The scope limit (lowercase-initial only, "adidas" excepted) is what makes the check brand-safe: it cannot false-positive on brand tokens (F50, Nike, FG, Gripknit), which resolves the original deferral concern. Reverse Title-Case-drift detection stays with the two human-style gates, not the script. Origin: Batch 4 KK3725 shipped 3 lowercase editorial body H2s past both gates while the script backstop was still deferred; see `deliverables/page-optimizations/2026-06-17_session-01/_audit-trail.md` (2026-06-29 entry).

**Scope (added 2026-06-29): applies to PDP body copy AND collection page copy.** Effective Batch 5 onward, any workforce-generated content for collection pages follows the same split rule:

- **Editorial body H2s:** sentence case, first word capitalized ("adidas" exception).
- **Structural H2s** (`Product Details: [name]` where used, "Care and Maintenance", and the FAQ section H2 -- "FAQs about [name]" on PDPs, the bare "Frequently Asked Questions" on collection pages): Title Case.
- **FAQ H3 questions** (where used on collection pages): sentence case, first word capitalized.

Rationale: Mike's 2026-06-29 request to standardize the H2 format across PDPs and collection page copy so the same enforcement gap cannot recur in a different content type. One unified house style reduces ambiguity and simplifies enforcement.

### Brand tier nomenclature (added 2026-06-29)

Nike cleats: Elite > Pro > Academy > Club.
adidas cleats: Elite > Pro > League > Club.

Cross-map: **Nike Academy ≈ adidas League** (the accessible mid/entry tier above the cheapest Club).

Application: the tier-band word counts (Elite 400 to 450, Pro 340 to 390, League/Club 280 to 340; see the SCRIBE Phase 4 self-check and `context/page-type-playbooks/product-page-playbook.md` 'Tier-appropriate length within Complex') apply by tier-EQUIVALENCE regardless of brand. A Nike Academy brief uses the League/Club word band, not the Elite/Pro band. Codified Batch 5 onward.

### Non-FIFA brand language discipline (added 2026-06-29)

FIFA / World Cup terminology keys on the BRAND's adidas FIFA license, not on the nation's FIFA membership. adidas is the FIFA commercial licensee; adidas pages may use the FIFA / World Cup family. **Every non-adidas kit brand (Nike, Kelme, Puma, Umbro, Hummel, and others) is FORBIDDEN from FIFA / "World Cup" / "FIFA World Cup [year]" / "WC" terminology** and uses federation / cycle language only ("2026 cycle", "championship summer", "this cycle", the bare year "2026", verifiable historical results). This is why the Nike-Croatia and Kelme-Bosnia jerseys run cycle-language-only even though Croatia and Bosnia are FIFA members. Canonical rule and substitution table: `context/brand-ip-constraints.md` 'FIFA World Cup Terminology'.

### Fabrication guard and tournament-status discipline (added 2026-06-29)

Surfaced across Batches 3 to 5. Dispatch hypotheses (closure, weight, construction, materials, supplier, player associations) are STARTING POINTS, not facts: SCRIBE verifies every such claim against the SKU's Phase 0 scrape before writing it, and scrape data wins over hypothesis. Never invent a value the scrape did not supply (KD/volume scores, weights, materials, retail/store/operational detail, player names); leave it out rather than guess.

**Tournament-status subtype (evergreen default).** Tournament-cycle products (national-team jerseys especially) default to EVERGREEN framing: verifiable historical results, established heritage, documented specs. Forbidden patterns and variations: "chases the trophy this summer", "still alive in the bracket", "title defense", "group stage form", "heads into the knockout rounds", "best/first/only [tournament] ever" where not verifiable-forever. Two non-default framings exist when a time-sensitive angle is genuinely warranted, each requiring ORIN sign-off: date-stamped copy with an audit-trail note, or explicit pre-tournament framing.

**Scope:** PDP body copy and collection page copy. Time-sensitive marketing channels (Klaviyo, social, paid ads) run a separate discipline and are out of scope here.

**Case studies:** HP9973 (fabricated KD scores), KK1307 (invented retail/store detail), J000691 (unverified Croatia current-cycle/squad claims, caught at gate), KJ6746 (closure hypothesis overridden by scrape at SCRIBE level, the target behavior), Bosnia "only World Cup" (pre-empted at ORIN research 2026-06-29; qualified for 2026, use "2014 World Cup debut"), Copa Pure IV "leather"/"Sprintframe" (pre-empted at ORIN research 2026-06-29; League is synthetic Fusionfeel, plate is Comfort Frame).

**Enforcement:** SCRIBE Phase 4 self-check (`.claude/agents/on-page-seo/agent.md`) + ORIN Gate 15 clause (m) (`.claude/agents/master-strategist/agent.md`). A voice_check.py deterministic detector is not attempted here: legitimate heritage references and historical results would false-positive; enforcement is the self-check plus the gate.

### Broader US/UK distinctions (codify as encountered, not preemptively)

The footwear term is the priority codification. Other US/UK distinctions may surface in production; codify each as a real instance appears rather than preemptively:

- `field` (US) vs `pitch` (UK): US prefers `field`, though `pitch` is sometimes used in soccer-specific contexts. No strict rule yet.
- `game` (US) vs `match` (UK): both are used in US soccer. No strict rule.
- `jersey` (US) vs `kit` (UK): both are widely understood in US soccer. No strict rule.
- `tournament` (US) vs `competition` (UK): both acceptable.
- Spelling: US English throughout (`color` not `colour`, `organize` not `organise`). Already implicit; formalized here.

### Enforcement (defense-in-depth)

SCRIBE scans output for `boot` / `boots` in a soccer-footwear context during Phase 4 drafting and substitutes `cleat` / `cleats` (primary) or `shoe` / `shoes` (variation). ORIN's orchestrator-layer re-check flags any soccer-context `boot` / `boots` in any output field and routes it back to SCRIBE. `scripts/voice_check.py` enforces a `\bboots?\b` = FAIL regex at script level (case-insensitive), the first line of defense, alongside the em-dash, forbidden-word, and `\bAdidas\b` checks.

Regex implementation note (`scripts/voice_check.py`): the `\bboots?\b` check blanks non-soccer phrases (`boot up`, `boot camp`, `boot loader`, `boot sector`, `to boot`, `das boot`, `boots on the ground`) before matching, and `bootstrap` / `reboot` never match because the word boundary requirement excludes them. Backtick and fenced content and pedagogical anti-pattern lines (markers INCORRECT, FORBIDDEN, UK CONVENTION, DO NOT USE, anti-pattern, wrong:, bad example) are exempt, the same exemption pattern the `\bAdidas\b` check uses.

### Architectural learning note

**US market language discipline (added 2026-06-03):** Mike flagged the gap after reviewing chat-sketch work where `boot` was used several times (UK/global convention) when `cleat` is the US-market term. Reader-first orientation extends to market localization: the US/Canadian avatar searches and reads in US-market terms, so UK conventions read as subtle dissonance even when technically correct. Discipline is forward-only: worked examples in the playbooks are fix-forwarded to model the correct term (worked examples must demonstrate the rule so SCRIBE learns the right pattern), and in-flight uncommitted work is fix-forwarded at gate, but shipped briefs are NOT retroactively swept (same standing forward-only policy as the brand-styling codification). Related discipline: 'Editorial philosophy (added 2026-06-02)' (reader-first orientation) and 'Brand styling conventions' (the other script-enforced language-styling rule).

Cross-references: `.claude/agents/on-page-seo/agent.md` Section 9 + Section 11 (SCRIBE Phase 4 US-market self-check), `.claude/agents/master-strategist/agent.md` Section 11 (ORIN defense-in-depth re-check), `scripts/voice_check.py` (`\bboots?\b` regex), both page-type playbooks (worked examples fix-forwarded). Related: 'Editorial philosophy (added 2026-06-02)', 'Brand styling conventions'.

## Measurement Unit Discipline: US-first dual notation (added 2026-06-15)

ProSoccer is a US-market retailer (Pasadena / Irwindale, US shipping). A companion to the US Market Language Discipline above: where that rule governs vocabulary (`cleat`, not `boot`), this one governs units. Any measurement that appears in PDP body copy must LEAD with US imperial units and carry the metric value in parentheses, so the US/Canadian avatar reads in familiar units while the metric stays available.

**Format pattern:** `[US value] ([metric value])`, for example `86°F (30°C)`, or in prose `[US value], or [metric value]`.

**Applications:**

- **Temperature (Care bullets primarily).** Wash: "Wash cold, 86°F (30°C) or below". Tumble dry: "Tumble dry low, 105°F (40°C)". Iron: "Iron warm, 230°F (110°C)". Never the bare metric ("30°C").
- **Weight (Product Details bullets, cleats / footwear primarily).** Cleat weight: "6.3 oz (180g)". Jersey weight (rare): "5.5 oz (155g)". Never the bare metric ("180g").
- **Dimensions (rare, spec bullets).** "11 in (28 cm)" or "11 inches (28 cm)".

**Conversion accuracy.** Round the US value to a sensible whole number or one decimal; do not carry false precision. Common conversions:

| Metric | US (rounded) | Context |
|---|---|---|
| 30°C | 86°F | cold wash |
| 40°C | 105°F | warm wash |
| 60°C | 140°F | hot wash |
| 110°C | 230°F | iron, warm |
| 150°C | 300°F | iron, hot |
| 180g | 6.3 oz | typical FG cleat |
| 220g | 7.8 oz | heavier cleat |
| 150g | 5.3 oz | lightweight cleat |

**Exceptions (sizing, no conversion in body copy):**

- **Shoe sizes:** US sizing convention only (US Men's 9, US Women's 8), no UK / EU conversion in body copy. The size chart handles conversion separately.
- **Jersey / apparel sizes:** US apparel sizing only (S, M, L, XL), no EU equivalent in body copy. The size chart handles conversion.

**Fields this applies to:** Description body prose (when numeric measurements appear), Product Details bullets, Care and Maintenance bullets, and FAQ answers. NOT in Meta Title, Meta Description, or the Short Description hero block: those fields are too brief for dual notation, so use US-only there.

**Voice-check and formatting notes.** The degree symbol `°` is acceptable (it is not an em-dash or en-dash, which the voice check forbids). Use the tight `value°F` / `value°C` pattern: `86°F (30°C)`, never `86 °F` or `86F`. Weight keeps a space before `oz` and may run tight on `g` to match manufacturer spec convention: `6.3 oz (180g)`. The parenthetical metric immediately follows the US value with a single space: `86°F (30°C)`, not `86°F  (30°C)`.

**Enforcement (defense-in-depth).** SCRIBE verifies every temperature, weight, and dimension in the four applicable fields uses US-first dual notation during Phase 4 (`.claude/agents/on-page-seo/agent.md` Section 9). ORIN scans for a solitary metric value with no imperial pairing at Gate 15 and routes it back to SCRIBE (`.claude/agents/master-strategist/agent.md` Section 11). Forward-only: the existing 20 PDPs (Day 3 batch + Batch 2) keep their current units; Batch 3 onward complies. Canonical applications: `context/page-type-playbooks/product-page-playbook.md` 'Measurement unit discipline: US-first dual notation (added 2026-06-15)'. Related: 'US Market Language Discipline (added 2026-06-03)'.

## Jersey taxonomy node (canonical, added 2026-07-11)

The Shopify taxonomy category for every jersey PDP (national-team and club, authentic / replica / stadium / fan) is canonically:

**`Apparel & Accessories > Clothing > Shirts & Tops`**

Mike's call (2026-07-11), closing the Batch 6 jersey-taxonomy-inconsistency follow-up. Chosen over `Apparel & Accessories > Clothing > Activewear` because Shirts & Tops is the more specific node and maps cleanly to the Google product taxonomy. Applies forward to all jersey briefs (the Bosnia / Croatia / DR Congo / Jamaica / Korea set already shipped is not retro-swept; forward-only from Batch 7, starting with the Kelme Jordan jersey). The live "Type" field reading "Apparel" is a separate Shopify field and is not the taxonomy node. Footwear keeps its own node (`Apparel & Accessories > Shoes > Athletic Shoes > Soccer Cleats`). ORIN writes the jersey node into the jersey SKU's input file `Taxonomy Category` and `batch_gate.py` / SCRIBE surface it in the brief.

## Brief Output Structure (added 2026-06-09)

Surfaced from Mike's first production Shopify implementation pass: he implemented 10 PDPs by hand in Shopify admin using the Day 3 re-run briefs (commit 957dc3c) and hit real copy-paste friction. The SEO deliverables (Title, Short Description, Description body, Meta Title, Meta Description, URL handle, image alt text, FAQ, taxonomy) were scattered through each brief and interleaved with workforce-internal audit content; the live product Title was nowhere in the brief, which forced a SKU search in admin instead of a fast title lookup; and audit reasoning the implementer never needs added noise to the paste workflow. The fix splits the two audiences into two artifacts.

**Two artifacts per brief, two audiences.**

1. **The brief file** (`deliverables/page-optimizations/[YYYY-MM-DD_session-XX]/<SKU>_<slug>_brief.md`, SKU-first per 'Naming convention' above, added 2026-06-15) carries ONLY implementer-facing content, ordered for top-to-bottom copy-paste into Shopify admin (plus the clean Keywords table for Mike's at-a-glance tracking). No keyword rationale, no brand-IP reasoning, no sibling differentiation lane, no defense-in-depth notes. The Keywords table (added 2026-06-15) is the one keyword-related element that lives in the brief: it carries Volume and Difficulty only, never the selection rationale, GSC analysis, or "why this keyword" justification, which stay in the audit file.
2. **The per-batch audit file** (`deliverables/page-optimizations/[YYYY-MM-DD_session-XX]/_audit-trail.md`) carries the workforce-internal audit content for every SKU in the batch, in one navigable document. One audit file per batch, not per SKU (easier to maintain than scattered per-SKU files).

**Brief file structure (implementer-facing only):**

```
# [Product Name] -- PDP Optimization

## Quick Reference
- SKU: [code]
- Current live Title (for Shopify admin search): [exact current title from Phase 0 Firecrawl scrape]
- URL: [full URL]

## SEO Details (copy-paste into Shopify)

### Keywords
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | [primary kw] | [vol/mo] | [DataForSEO difficulty 0-100] |
| Secondary (pack-specific) | [pack/colorway/release long-tail] | [vol or blank] | [diff or blank] |
| Secondary | [kw 3] | [vol] | [diff] |
| Secondary | [kw 4] | [vol] | [diff] |

### Title (Shopify "Title" field)
[recommended new title]

### Short Description (metafield, hero block above Add to Cart)
[short description prose -- NO internal links here]

### Description (body_html, accordion below product images)
[full description with H2s, prose, Product Details bullets, internal links -- links live ONLY here]

### Meta Title (Search engine listing)
[meta title]

### Meta Description (Search engine listing)
[meta description]

### URL Handle
[current handle, OR recommended new handle with 301 redirect flag]

### Image Alt Text (apply per gallery image)
- [alt text]
- [alt text]
- ...

### FAQ (paste into Description body; H2 "FAQs about [short product name]", H3 per question, paragraph answers)
## FAQs about [short product name]
### [question 1]
[answer paragraph, 1 to 3 sentences; inline links allowed here, never in Short Description]
### [question 2]
[answer paragraph]
[3 to 5 Q&A pairs total when the FAQ earns inclusion]

### Taxonomy Category (Shopify admin)
[category path]
```

**Per-batch audit file structure:**

```
# Audit Trail -- [Batch Date / Session ID]

## Batch Metadata
- Total SKUs: N
- Brand IP classifications: [summary]
- Dispatch architecture: [parallel/sequential]
- Commit hash: [if known]

## Per-SKU Audit Notes

### SKU [code 1] -- [product name]
- Product complexity classification: [Complex/Standard/Simple, reasoning]
- Keyword research: [primary keyword + volume, supporting keywords + volumes, fallback notes]
- Brand IP classification: [FIFA permitted yes/no, lowercase adidas, etc.]
- Sibling-SKU title uniqueness check: [differentiation analysis]
- Internal links -- validation details: [anchor text + validation evidence + path of file checked]
- Differentiation lane (from ORIN pre-dispatch): [angle, hook, heritage, use case, metaphor]
- Defense-in-depth gate notes: [flags caught + resolutions, if any]
- URL handle flags: [over 70-char flag for Jorge/Misha, if applicable]

### SKU [code 2] -- [product name]
[same structure]
```

**Quick Reference: field order (SKU first, added 2026-06-15).** The Quick Reference block leads with SKU, then the Current live Title, then the URL. SKU is the first field because it is the operationally relevant identifier (and now also leads the brief filename). The Current live Title still surfaces the exact product Title as it renders on the live PDP, captured during the Phase 0 Firecrawl scrape, so Mike can also search Shopify admin by title; the data is already captured in Phase 0. SCRIBE verifies SKU is the first Quick Reference field and reorders if it is not.

**Keywords table (added 2026-06-15).** SEO Details opens with a Keywords table, the first sub-section under SEO Details, before the Title field. It is a clean operational table only (Type, Keyword, Volume, Difficulty): no research rationale, no GSC detail beyond the override flag, no "why this keyword" justification. Purpose: Mike's manual Shopify and Google-sheet tracking needs the targets at a glance, and pulling from the audit trail or KIRA output adds friction. Volume is monthly search volume; Difficulty is the DataForSEO difficulty score (0 to 100). Special cases: (a) sub-floor primary keywords selected on a GSC position override carry a Volume-column flag `[N]* (GSC override, pos [X])`, e.g. `10* (GSC pos 8)`; (b) for any secondary keyword KIRA did not return a difficulty score, leave the Difficulty cell blank, never fabricate one. The keyword selection rationale, GSC analysis, and fallback notes still live in `_audit-trail.md`.

**Pack-specific secondary row (extended 2026-06-15).** When the SKU carries a pack, colorway, or named release, the pack/colorway/release-specific long-tail (per 'Mechanism C: pack/colorway/release-specific secondary keyword discipline') appears as the FIRST secondary row, tagged `Secondary (pack-specific)` in the Type column, so it is visible at a glance during implementation. The `(pack-specific)` notation surfaces the long-tail strategically. Because these terms are inherently long-tail and floor-exempt, their Volume and Difficulty cells are often blank. Worked example:

```
### Keywords

| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | adidas f50 turf | 720 | 45 |
| Secondary (pack-specific) | adidas f50 hyperfast turf road to glory |  |  |
| Secondary | adidas f50 pro turf | 110 | 38 |
| Secondary | f50 turf cleats | 320 | 41 |
```

(Blank Volume / Difficulty cells mean KIRA could not retrieve tool data; they are left empty, never filled with a fabricated number or an em-dash.)

**FAQ H2 wording (revised 2026-06-15).** On PDP briefs the FAQ section H2 follows `FAQs about [short product name]` (for example "FAQs about the F50 Elite FG", "FAQs about the Croatia Jersey 2026"), carrying the product reference for topical signal and snippet eligibility, using the natural short name rather than the full awkward primary keyword. Collection-page briefs keep the bare "Frequently Asked Questions" H2. The H3 question format and paragraph answers are unchanged. Full rule: `context/page-type-playbooks/product-page-playbook.md` 'FAQ heading hierarchy discipline (added 2026-06-09)'.

Enforcement (defense-in-depth): SCRIBE produces the brief file with implementer content only and writes audit content to the batch `_audit-trail.md`; its Phase 4 self-check confirms no audit content leaked into the brief and no internal link sits in the Short Description. ORIN's pre-dispatch pass produces both files, and the Section 11 re-check verifies the brief carries only implementer content, the `_audit-trail.md` exists with per-SKU notes, and no brief's Short Description contains a link.

FORWARD-ONLY: the Day 3 re-run briefs (commit 957dc3c) stay in the old combined structure per Mike's standing forward-only principle. The new structure applies to the next batch dispatch onward. This is the architectural inflection point, auditable by commit hash. The 2026-06-15 additions (Keywords table at the top of SEO Details, `FAQs about [product]` FAQ H2 on PDPs) are likewise forward-only: the existing 20 PDP briefs in the Day 3 batch and Batch 2 keep their current FAQ H2 and carry no Keywords table; Batch 3 onward complies. The next worked-example refresh in the playbooks should model both the new brief structure and the audit-trail structure (standing follow-up; not written in this pass).

Cross-references: `.claude/agents/on-page-seo/agent.md` Section 13 (SCRIBE output template) + Section 9 (Phase 4 self-check), `.claude/agents/master-strategist/agent.md` Section 9 (ORIN produces both files) + Section 11 (structure re-check), both page-type playbooks 'Brief output structure (added 2026-06-09)'. Internal link placement: 'Internal Link Format Discipline' below. Production source: Mike's first 10-PDP Shopify implementation pass on the Day 3 re-run batch (commit 957dc3c).

## Per-SKU input file + batched pre-scrape (v2, added 2026-07-10)

The v2 architecture moves the upstream work SCRIBE used to repeat per dispatch (live PDP scrape, keyword lookup, internal-link validation) UP to ORIN, run ONCE per batch, and writes the results into a per-SKU input file SCRIBE reads. This is the single biggest token cut in v2: under v1 each of ~10 parallel SCRIBEs independently scraped its PDP, re-read the full context set, re-derived keywords ORIN had already locked, and re-validated links, at roughly 270 to 300k tokens and 40+ tool uses each. Under v2 SCRIBE reads one pre-built input file and writes the brief.

### Three parts

**3a. Batched pre-scrape (ORIN, pre-dispatch).** ORIN Firecrawl-scrapes ALL batch URLs once at pre-dispatch and writes each SKU's scrape data (specs, colorway, materials, plate/surface, weight, price, existing copy, sibling colorways) into that SKU's input file under `## Phase 0 scrape data`. One scrape per URL for the whole batch, not one scrape per SCRIBE. Scrape-wins discipline is unchanged: the scrape is the source of truth over any dispatch hypothesis, and a value the scrape did not supply is marked "not in scrape" and left out, never invented.

**3b. Pre-resolved keywords + links (ORIN, from KIRA + ORIN link-check).** KIRA's validated keyword table (primary + secondaries + pack-secondary) and ORIN's validated internal links (already confirmed 200 + content-signal) are written into the same input file. SCRIBE receives them as INPUTS and does not re-derive keywords or re-validate links.

**3c. SCRIBE tool cap.** With inputs pre-loaded, SCRIBE's job is: read its input file, read its silo lane + the differentiation spec, write the brief, run the self-check, write the brief file. Target **<= 10 tool uses**. SCRIBE no longer scrapes, looks up keywords, or validates links; those are ORIN's upstream responsibilities. See `.claude/agents/on-page-seo/agent.md` Section 2 / Section 9 (v2 input-driven flow) and Section 5 (Firecrawl/DataForSEO/GSC now used by ORIN upstream, not per-SCRIBE).

### Input file location, schema, and one source of truth

- **Location:** `deliverables/page-optimizations/[session]/inputs/[SKU]_input.md`. ORIN creates the `inputs/` subfolder at pre-dispatch.
- **Schema / template:** `templates/per-sku-input-template.md`. Sections: Identity (SKU, URL, handle, brand, brand-IP posture, product category, tier, word band), Phase 0 scrape data, Keywords, Validated internal links, Differentiation lane, Structure skeleton (Mechanism A), Forbidden phrasings (three tiers), and a fenced `gate-meta` JSON block.
- **One source of truth:** the fenced ```` ```gate-meta ```` JSON block is the machine-readable AUTHORITATIVE source for brand, brand-IP posture, tier, word band, primary keyword, and the three-tier forbidden-phrasings lists (verbatim / motifs / title-frames). `scripts/batch_gate.py` parses this block; SCRIBE reads it for the barred lists, the tier band, and the brand-IP posture; ORIN writes it. Three consumers, one list, no drift. The human-readable sections above the block echo the same values for reading convenience, written in the same pass so they stay in sync.
- **Tier + word band are SKU-specific, never inherited from the exemplar** (the IF8512 Elite-band-on-a-Pro-SKU defect). The word band comes from the SKU's own tier: Elite 400-450, Pro 340-390, League/Club 280-340 (+15 tolerance).

### Where the deterministic gate reads it

`batch_gate.py` (see 'Voice check discipline' cross-ref and `scripts/batch_gate.py`) reads each SKU's `gate-meta` block for the brand-aware FIFA check (#5), the per-SKU forbidden-phrasings check (#6), the cross-brief motif/title-frame vocabulary (#7), the word-band check (#8), and cannibalization (#9). If an input file is absent, the gate honestly reports which input-dependent checks it skipped for that SKU and still runs FIFA provisionally (a missing input can never hide a leak).

Cross-references: `templates/per-sku-input-template.md` (schema), `scripts/batch_gate.py` (gate-meta consumer), `.claude/agents/master-strategist/agent.md` Section 9 (ORIN pre-dispatch batched pre-scrape + input-file production), `.claude/agents/on-page-seo/agent.md` Section 2 + Section 9 (SCRIBE v2 input-driven flow + tool cap). Forbidden-phrasings three-tier extraction: 'Forbidden-phrasings three-tier scope (v2, added 2026-07-10)' below.

## Forbidden-phrasings three-tier scope (v2, added 2026-07-10)

Mechanism B (the forbidden-phrasings backstop for pack/series batches) used to carry VERBATIM H2 titles and closing lines only. The Batch 6 Shadow set proved that scope too narrow: four independent SCRIBEs, handed only verbatim strings, re-derived a shared "gone" payoff word across all four openers and reused the exemplar's "The pass no one sees coming" H2 as the FRAME "The first step nobody sees coming" (noun-swapped). Neither the motif nor the frame was a verbatim string, so Mechanism B missed both and the convergence surfaced at ORIN's manual gate. This codification widens the scope to three tiers so the workforce stops re-litigating the same convergence class every batch.

**The three tiers (all literal strings; ORIN extracts all three from the validated exemplar into each sibling's input file `gate-meta.forbidden_phrasings`):**

- **Verbatim** (existing): exact hooks, H2 titles, definitional sentences for shared concepts (the FG/AG/tier/plate definitions), opening hook, closing line. Enforced by substring match.
- **Motifs** (new): recurring payoff / register words the exemplar leans on, for example `gone`, `invisible`, `elusive`, `ghost`. Siblings must not reuse them. Enforced by word-boundary match. ORIN extracts a motif when a distinctive, non-generic word carries the exemplar's emotional payoff and would read as convergence if a sibling reused it (skip ordinary connective words; a motif is a claimed register word, not a stopword).
- **Title-frames** (new): the structural template of the exemplar's H2s reduced to its distinctive invariant fragment, for example `sees coming` from "The [noun] [nobody] sees coming". Siblings must not mirror the frame with swapped nouns. Enforced by substring match on the invariant fragment (store the fragment that survives noun-swapping, not the full H2, which is already covered verbatim).

**One source of truth.** The three lists live once, in each SKU's input file `gate-meta` block (`context/workforce-conventions.md` 'Per-SKU input file + batched pre-scrape (v2)'). Three consumers read that one copy: ORIN writes it, SCRIBE is told to write AROUND all three tiers, and `scripts/batch_gate.py` enforces them (check #6 flags a brief reusing its OWN barred phrasing at any tier; check #7 flags a barred motif or title-frame recurring across sibling briefs and near-identical openings/closings via lexical trigram overlap). No separate hardcoded motif dictionary; a dictionary would drift from the per-SKU lists.

**Deterministic vs judgment split.** The lexical checks (verbatim / motif / title-frame greps, opening/closing n-gram overlap) are deterministic and offline, and belong in the script. Conceptual convergence that shares no tokens (two siblings expressing the same idea in fully different words) is a genuine judgment call and escalates to ORIN, by design; it is not forced into the script.

**Companion codification: SKU-own tier-band in the skeleton handoff.** Mechanism A (the structure skeleton) carries the SKU's OWN tier-band, never the exemplar's (the IF8512 Elite-band-on-a-Pro-SKU defect: a Pro SKU inheriting the exemplar's Elite 400-450 band and shipping ~446 words). The band is written per SKU into the input file `gate-meta.word_band` from that SKU's own tier (Elite 400-450, Pro 340-390, League/Club 280-340) and enforced by `batch_gate.py` check #8. See 'Per-SKU input file + batched pre-scrape (v2)' above.

Cross-references: `.claude/agents/master-strategist/agent.md` Section 9 'Exemplar handoff' (Mechanism A/B, three-tier extraction), `.claude/agents/on-page-seo/agent.md` Section 9 'Exemplar handoff' (SCRIBE write-around self-check), `scripts/batch_gate.py` + `scripts/test_batch_gate.py` (checks #6/#7/#8 and the Shadow-convergence regression tests), Batch 6 audit-trail Shadow-set convergence note (`deliverables/page-optimizations/2026-07-08_session-01/_audit-trail.md`).

## Wave collapse: parallel-default dispatch (v2, added 2026-07-10)

v1 dispatched in sequential waves: Wave 1 (exemplars) -> ORIN manual gate -> Wave 2 (siblings). That barrier is pure wall-clock, and under v2 it is mostly unnecessary: the pre-dispatch differentiation spec plus the per-SKU input files (lane, structure skeleton, three-tier forbidden phrasings, tier band) ALREADY carry everything a sibling needs. There is no live exemplar extraction to wait on for a silo the workforce has shipped before.

**Default: single parallel wave.** For any SKU whose silo already has at least one shipped entry with an established lane (recorded in `context/silo-positioning/` Registry 2), ORIN dispatches all such SCRIBEs in parallel in a single wave. Each SCRIBE pulls its lane from the differentiation spec and its silo's existing patterns via the input file. The structure skeleton comes from the silo's established pattern, not from a freshly-extracted live exemplar.

**Exception (narrow): exemplar-first for a genuinely new lane only.** Keep a small exemplar-first sub-wave ONLY when a lane has ZERO precedent: the first-ever club team, the first-ever brand with a new licensing posture, a new product-class needing a new silo. In that case ORIN runs ONE exemplar for the new lane first, gates it, and its skeleton feeds ONLY the siblings in that same new lane. All OTHER SKUs in the batch (established silos) parallelize immediately alongside it; they do NOT wait for the new-lane exemplar.

**ORIN decision rule, per SKU:** "Does this SKU's silo have >= 1 shipped entry with an established lane (Registry 2)? Yes -> parallel now. No -> exemplar-first for that lane only." A batch mixing established and new lanes runs the established SKUs in the parallel wave and the new lane exemplar-first, concurrently.

Safety is preserved by Change 4: the deterministic `scripts/batch_gate.py` runs over the whole session after dispatch and catches the mechanical defect classes (casing, headings, FIFA, forbidden phrasings, cross-brief convergence, word band, cannibalization, price, hedge) that the manual per-wave gate used to catch by eye. Collapsing the human wave-gate is safe because the deterministic gate exists.

Cross-references: `.claude/agents/master-strategist/agent.md` Section 9 'Wave collapse: parallel-default dispatch (v2)', `context/silo-positioning/README.md` (Registry 2, the established-lane record), `scripts/batch_gate.py` (the safety net that replaces the manual wave-gate). Supersedes the sequential Wave 1 -> gate -> Wave 2 default in 'Batch parallel dispatch + single daily batch commit' for silos with established lanes.

## Escalate-on-exception approval mode (v2, added 2026-07-10)

For batch page-optimization runs, the v1 per-checkpoint approval mode (ORIN holds for Mike at Checkpoint 1 keywords, Checkpoint 2 exemplar plan, Checkpoint 2b exemplar review, Checkpoint 3 final review, plus every "surface decision" hold) is replaced by escalate-on-exception: ORIN runs the batch autonomously end-to-end and surfaces ONE end-of-batch report for Mike. This is safe ONLY because the deterministic gate (`scripts/batch_gate.py`, Change 4) catches the mechanical defect classes the human checkpoints used to catch; do not run this mode without the gate.

### What ORIN decides, applies, and logs (does NOT ask)

Everything that resolves from codified rules:

- **Keyword selection** within the codified volume floors + fallback hierarchy + GSC-override rules (`context/workforce-conventions.md` 'Volume-Weighted Primary Keyword Selection Discipline').
- **Exemplar selection and dispatch shape** (parallel-default per 'Wave collapse'; exemplar-first only for a zero-precedent lane).
- **Differentiation lanes** (the pre-dispatch differentiation pass).
- **Gate-caught MECHANICAL fixes**: casing, heading levels, word-count-band trims, keyword-table duplicate rows, motif / title-frame re-voices, price-in-body removals, and the other deterministic `batch_gate.py` FAIL classes. ORIN fixes them (surgically or by a targeted SCRIBE re-dispatch), re-runs the gate to green, and logs the fix.
- **Per-batch commit** and the Registry 2 append.

### The deterministic "is this an exception?" test (ORIN STOPS for Mike only on these four)

ORIN escalates mid-batch ONLY when a decision cannot be resolved from codified rules and falls into one of these four:

1. **A true architectural first with NO silo precedent**: a new brand licensing status, a new product-class requiring a new silo, or a new competition-IP question with no codified answer in `context/brand-ip-constraints.md` or the silo files.
2. **A fabrication trap unresolvable from the Phase 0 scrape**: the scrape contradicts itself, OR a required spec is absent AND load-bearing (the copy cannot be written honestly without it). A merely-absent non-load-bearing spec is not an exception; ORIN omits it per scrape-wins and proceeds.
3. **A cannibalization collision with no clean resolution** under the codified cannibalization discipline (no fallback-hierarchy primary clears the floor with a winnable SERP without colliding).
4. **A cross-brief convergence `batch_gate.py` check #7 flags that ORIN cannot auto-resolve** by a surgical re-voice (a genuine conceptual convergence, not a mechanical motif/frame reuse).

If a situation is not one of these four, it is not an exception: ORIN decides from the codified rule, applies, and logs it for the end-of-batch report. Escalations should be rare.

### The one end-of-batch report to Mike

ORIN produces a single report at batch close containing:

1. **Autonomous decisions** with one-line rationale each: the keyword table (primary + secondaries per SKU), exemplar / dispatch-shape choices, and the differentiation lanes.
2. **Gate-caught defects auto-fixed**: each `batch_gate.py` FAIL and the fix applied.
3. **Exceptions escalated** (should be rare): any of the four criteria that fired, with the specific decision ORIN needs from Mike.
4. **Registry 1 handoff block**: the per-SKU primary-keyword assignments for the white-label team's manual PDPs-tab entry (write ownership stays with them by design).
5. **Commit hashes**.
6. **Publish-priority notes**: sold-out SKUs (evergreen copy ships regardless; flag for Mike's implementation ordering) and any live-page findings.

Mike reviews the ONE report, not every checkpoint. Cross-references: `.claude/agents/master-strategist/agent.md` Section 9 'Escalate-on-exception approval mode (v2)', `scripts/batch_gate.py` (the deterministic gate this mode depends on), `CLAUDE.md` 'Approval mode'.

## Claims verification: heritage honours default to qualitative + source-or-cut (added 2026-07-13)

Every checkable factual claim in a brief (specific numbers -- title/trophy counts, dates, weights, years; superlatives -- "most successful", "record", "first-ever"; named honours) must carry a cited source or be cut. No bare PASS: "ORIN thinks it's fine" is not verification. Three layers enforce this so Batch 9 onward is automatic.

### Layer 1 -- default-to-qualitative (playbook rule)

Heritage honours in jersey body copy DEFAULT TO QUALITATIVE. Specific league/title/trophy counts ("13 Premier League titles", "20 English league titles", "six European crowns") and outright "most"/"record" superlatives ("most successful club", "a record 20", "more than any other") AGE and are CONTESTED, so they must not ship. Use qualitative honours language instead ("one of England's most decorated clubs", "a European pedigree few can match", "a trophy history the fans still replay"). A specific count ships ONLY when it carries a durable cited source (the product's Phase 0 scrape, or a club-site / web citation recorded in the audit trail); absent that, it is cut. Origin: KA6871 (Batch 8) shipped "among England's most successful clubs: 13 Premier League titles, a record 20 English league titles (shared with Liverpool)" in its first draft; Liverpool drew level with Manchester United at 20 English league titles in 2024-25, breaking both the count and the superlative. The same trap hit all six club briefs (United + Liverpool) and was fixed to qualitative before the Batch 8 push. This is the club-jersey analogue of the existing 'Fabrication guard and tournament-status discipline' for national-team jerseys.

### Layer 2 -- deterministic gate check (`scripts/batch_gate.py`)

`check_heritage_counts` flags `heritage-count` (specific league/title/trophy counts) and `heritage-superlative` ("most successful", "most titles", "more than any other", "record N") as FAIL in customer-facing copy. The approved qualitative language ("most decorated", "a European pedigree few can match") is deliberately NOT matched. Regression fixture: `scripts/test_batch_gate.py` `TestKA6871HeritageCounts` proves the KA6871 claim is caught (both counts + both superlatives) AND the qualitative fix passes -- the gate that this claim motivated catches this claim. A shipped brief with a legitimately-sourced count is an explicit ORIN override recorded in the audit trail, not a silent pass.

### Layer 3 -- ORIN claims-extraction pipeline (pre-push verification)

Before the push, ORIN runs a claims-extraction pass over every brief: list every checkable assertion and classify each as PASS-WITH-SOURCE (name the source: SCRAPE field / club-site / web-check), FIX (cut to qualitative or correct), or ESCALATE (cannot source -> surface to Mike, never bare-PASS). Product specs, colorways, weights, and design tributes trace to the per-SKU Phase 0 scrape; founding / stadium / heritage dates trace to a named web / identity-research verification; anything that traces to neither is escalated. Rule: "I'd rather see three escalations than one confident-but-unsourced PASS." Origin: three times in the Batch 8 session a fact got ahead of the files (a fabricated wall-clock figure; an assumed F50 scrape-verify; an assumed United-count propagation) and the claims pass caught each.

Cross-references: `scripts/batch_gate.py` (`check_heritage_counts`), `scripts/test_batch_gate.py` (`TestKA6871HeritageCounts` regression fixture), `context/silo-positioning/club-team-jerseys.md` (competition-naming policy + the United/Liverpool honours guardrails), Batch 8 audit trail (`deliverables/page-optimizations/2026-07-13_session-01/_audit-trail.md` 'Claims-verification pass'). Related: 'Fabrication guard and tournament-status discipline (added 2026-06-29)' above (the national-team analogue).

## Internal Link Format Discipline (added 2026-06-03)

Every internal link suggestion in a PDP or collection brief must be a full HTTPS URL on the canonical domain. The canonical domain is `https://www.prosoccer.com` (with the `www` subdomain). Never a relative path, never `http://`, never a mangled or partial URL. The rule applies to the brief's `Internal links` sub-section, the brief-format template, and any inline link reference in modeled brief output.

**Link placement varies by contextual fit (added 2026-06-17).** Beyond the body-only placement rule, the 1 to 2 internal links go WHERE the prose authentically references the target, NOT at fixed structural H2 positions. Valid placements: both in one H2, in different H2s, one in the body and one in a FAQ answer, one in the intro and one in the close, or clustered early / late by context. ORIN's exemplar skeleton extraction does NOT carry link-position metadata, and ORIN's pairwise sibling comparison flags identical link positions across siblings as a templating footprint (same severity as identical hook phrasings). Gate 15 verifies link count, validation, body-only placement, and contextual fit, NOT position. Full rule: `context/page-type-playbooks/product-page-playbook.md` 'Internal link strategy' (Link placement varies by contextual fit, added 2026-06-17).

**Placement rule (added 2026-06-09): internal links live ONLY in the Description body, never the Short Description metafield.** Internal links appear ONLY in the Description body (long description / body_html). They do NOT appear in the Short Description metafield (hero block above Add to Cart). The hero block is conversion-critical real estate; links would distract the buyer from the Add to Cart action. Description body is the natural location for cross-discovery navigation, after the buyer has read the editorial prose and is exploring whether the product is right for them. Surfaced from Mike's first 10-PDP Shopify implementation pass (Day 3 re-run batch, commit 957dc3c); see 'Brief Output Structure (added 2026-06-09)' above. SCRIBE's Phase 4 self-check confirms no link sits in the Short Description; ORIN's Section 11 re-check backstops it.

Correct format:

- `https://www.prosoccer.com/collections/firm-ground`
- `https://www.prosoccer.com/collections/adidas-copa`
- `https://www.prosoccer.com/products/<handle>`

Incorrect formats (forbidden):

- `/collections/firm-ground` (relative path, no domain)
- `http://www.prosoccer.com/collections/firm-ground` (insecure protocol; ProSoccer is HTTPS-only)
- `http:///collections/firm-ground` (mangled, missing domain segment)
- `www.prosoccer.com/collections/firm-ground` (missing protocol)
- `prosoccer.com/collections/firm-ground` (missing `www` subdomain)

Why it matters:

1. Copy-paste implementation: full URLs paste cleanly into the Shopify rich-text editor when Mike adds cross-page links during implementation; a relative path pastes as a broken link.
2. SEO clarity: a full URL unambiguously documents exactly which page to link to.
3. Audit trail: future readers see precisely what was recommended without reconstructing context.
4. Protocol correctness: ProSoccer is HTTPS-only, so any `http://` reference is wrong on principle, and a relative path can render mangled (the surfacing case rendered `/collections/firm-ground` as `http:///collections/firm-ground`).

Enforcement (defense-in-depth): SCRIBE builds every internal link as a full HTTPS canonical URL during Phase 4 and expands any relative or partial path before brief output; ORIN's orchestrator re-check scans every internal link suggestion for relative paths, missing protocols, missing `www`, and mangled patterns; `scripts/voice_check.py` adds belt-and-suspenders regex coverage for the two worst failure modes (insecure `http://` ProSoccer URLs and mangled `http:///` missing-domain links), scoped to `deliverables/` and `briefings/` files only. The playbooks carry the forbidden patterns as pedagogical INCORRECT examples, so they are out of the script's link-check scope; backtick, fenced, and pedagogical-marker exemptions apply as elsewhere.

Surfacing case: the KI0662 PDP brief (commit 68664ca, in main) used relative paths in its internal links, which rendered as `http:///collections/firm-ground` during Mike's review. Per Mike's decision the KI0662 brief was NOT fix-forwarded (he edits the links manually during Shopify implementation); the rule applies forward only to new briefs. Same forward-only policy as the brand-styling and US-market codifications.

Architectural learning note: the format for internal link suggestions was never explicitly codified, so SCRIBE produced relative or partial URLs and ORIN had no rule to catch them. Codifying the full-HTTPS-canonical form removes the ambiguity and gives all three enforcement layers a concrete pattern to check. Related disciplines: 'US Market Language Discipline (added 2026-06-03)' (commit 499f1e5) and 'Editorial philosophy (added 2026-06-02)' (commit dcfe6da) are the other recent forward-only, defense-in-depth codifications.

Cross-references: `.claude/agents/on-page-seo/agent.md` Section 9 + Section 11 (SCRIBE Phase 4 link-format self-check), `.claude/agents/master-strategist/agent.md` Section 11 (ORIN defense-in-depth re-check), `scripts/voice_check.py` (insecure + mangled URL regex, deliverables/briefings scope), both page-type playbooks 'Internal link strategy'.

## Unsupported specific counts (Gate 14, cross-cutting)

Gate 14 is a separate gate after Gate 13; the workforce gates suite runs 14 gates as of 2026-06-02 (previously 13). It is the same ephemeral-data family as the Gate 13 pricing discipline (see 'Content evergreen-ness' above): body copy must not contain specific counts of catalog items (federations, brands, products, styles, designs, tiers) that are unverified, decay as inventory shifts, or read as SEO ornamentation. Collection pages are most prone to it (a collection aggregates inventory by definition).

Anti-pattern examples: "Ten federations, four brands, one piece of fan kit...", "Six bag styles across the adidas roster", "Twelve scarf designs span the federation lineup". Natural alternatives: positioning language ("the full federation roster"), comparative language ("category leaders across multiple brands"), specific examples without counts ("Argentina, Mexico, USMNT, and more"), "across" / "spanning" / "from X to Y" framing. Exception (counts permitted): tournament structure ("the 48-team 2026 World Cup expansion") from a public canonical source, year / cycle references ("the 2026 cycle", "the 1986 World Cup"), and product-specific verified specs -- each sourced from a verified authoritative reference and noted in the workforce briefing.

Defense-in-depth: SCRIBE self-revises in Phase 4 (Gate 14) before the Phase 5 voice check; ORIN re-checks at the orchestrator layer (Section 11 Gate 11).

**Architectural learning note.** Gate 14 unsupported specific counts (added 2026-06-02): Quality issue surfaced in Day 2 batch #1 URL #3 Short Description "Ten federations, four brands, one piece of fan kit..." Counts are unverified, decay-prone, and read as SEO ornamentation. Same family as Gate 13 pricing discipline. Body copy uses positioning/comparative language rather than specific catalog counts. Exception: tournament structure, year/cycle, or verified product specs.

Cross-references: both page-type playbooks 'Unsupported specific counts (Gate 14, added 2026-06-02)', `.claude/agents/on-page-seo/agent.md` Section 11 Gate 14 + Section 9, `.claude/agents/master-strategist/agent.md` Section 9 + Section 11 Gate 11.

## Image precision (cross-cutting)

A writing-quality discipline applied at SCRIBE Phase 4 (judgment call, not a regex gate). Every evocative sentence in body copy must pass the "what's the actual image?" test: can the reader picture the specific physical motion, is the temporal sequence clear, are cause-and-effect relationships connected? If any fail, SCRIBE revises before the Phase 5 voice check. ORIN sanity-scans at the orchestrator layer (flag obvious muddy imagery). Muddy "It goes up over your head when the anthem starts and doesn't come off 'till the crowd finds its voice" becomes sharper "Raised overhead during the national anthem and held high through the opening chants."

**Architectural learning note.** Image precision discipline (added 2026-06-02): Quality issue surfaced in Day 2 batch #1 URL #3 Short Description "It goes up over your head when the anthem starts and doesn't come off 'till the crowd finds its voice." SCRIBE was reaching for evocative imagery without nailing physical action or temporal sequence. Phase 4 self-check now applies "what's the actual image?" test to evocative sentences. ORIN orchestrator re-check flags muddy imagery. This is a writing quality discipline distinct from Gate 13 structural patterns.

Cross-references: both page-type playbooks 'Image precision discipline', `.claude/agents/on-page-seo/agent.md` Section 9 + Section 11, `.claude/agents/master-strategist/agent.md` Section 9 + Section 11 Gate 12.

## Parallel construction (cross-cutting)

A writing-quality discipline applied at SCRIBE Phase 4 (judgment call, not a regex gate). When listing 3+ examples in parallel, grammatical construction must match across all items: possessive form, article usage, preposition usage, quote marks, descriptor style. Pick one construction and apply it consistently. ORIN sanity-scans at the orchestrator layer (flag inconsistent 3+ example lists).

**Architectural learning note.** Parallel construction discipline (added 2026-06-02): Quality issue surfaced in Day 2 batch #1 URL #3 Short Description "Argentina's albiceleste, Mexico scarf called 'verde', USMNT red-white-blue, Germany's DFB black-red-gold, and Italy's azzurro" (inconsistent possessive/descriptor/quote usage across 5 parallel examples). Phase 4 self-check now verifies parallel grammatical construction across 3+ example lists. ORIN orchestrator re-check flags inconsistent parallel lists.

Cross-references: both page-type playbooks 'Parallel construction discipline', `.claude/agents/on-page-seo/agent.md` Section 9 + Section 11, `.claude/agents/master-strategist/agent.md` Section 9 + Section 11 Gate 12.

## Supporting keyword selection (cross-cutting)

A keyword-strategy discipline applied at SCRIBE Phase 2 (research) and Phase 4 (drafting). SCRIBE selects ONE supporting keyword for body-copy use, criterion = highest search volume among the Phase 2 supporting candidates. The selected keyword is woven into the Short Description (1 to 2 mentions) and the Long / body Description (3 to 5 mentions). Other supporting candidates stay in the workforce briefing audit trail (full candidate list with volumes, selected keyword + rationale, placement) but are NOT used in body copy. Primary keyword usage follows Gate 12 unchanged. Exception: two supporting keywords within 10% volume AND semantically distinct (not synonyms) -> include the second minimally (1 to 2 body mentions). Second carve-out (added 2026-06-15): the pack/colorway/release-specific long-tail (see 'Mechanism C: pack/colorway/release-specific secondary keyword discipline') earns at least ONE natural Description-prose mention IN ADDITION to the volume-selected supporting keyword; it is a deliberate exception, not a 'multiple supporting keywords' violation. Gate 12 sub-criterion (d) verifies ONE volume-selected supporting keyword at 3 to 5 body mentions, not multiple at shallow density; the pack-specific long-tail's single mention is exempt from that count. ORIN sanity-scans at the orchestrator layer.

**Architectural learning note.** Supporting keyword selection discipline (added 2026-06-02): SCRIBE was including multiple supporting keywords throughout Short and Long Descriptions, treating each as coverage opportunity. Result: keyword-targeted copy rather than reader-focused copy, dilute signal for any single supporting term. New rule: SCRIBE selects ONE supporting keyword (highest search volume among candidates) for body copy use (1-2 Short Description mentions, 3-5 Long Description mentions). Other supporting candidates preserved in workforce briefing audit trail but not used in output. Exception: two supporting keywords within 10% volume AND semantically distinct permitted minimally.

Cross-references: both page-type playbooks 'Supporting keyword selection' + 'Keyword distribution discipline', `.claude/agents/on-page-seo/agent.md` Section 9 'Supporting keyword selection' + Gate 12, `.claude/agents/master-strategist/agent.md` Section 9 + Section 11 Gate 12.

## Volume-Weighted Primary Keyword Selection Discipline (added 2026-06-09)

Surfaced from Mike's review of the Day 3 re-run keyword assignments (10 Nike SU26 Breakout Pack SKUs, commit 957dc3c). The year/generation primary-selection rule (commit 52829c6) produced some near-zero-volume primary keywords: 2 SKUs below the DataForSEO floor, 5 more in the 10 to 140/mo range, only 3 above 300/mo (for example the Mercurial Vapor 17 Elite FG primary at 10/mo while its supporting `nike mercurial superfly` term carried 8,100/mo). The logic was sound (a realistic ranking target for an ultra-specific long-tail) but it weighed ranking realism without weighing traffic realism: ranking number 1 for a zero-volume keyword earns zero traffic.

This discipline REFINES, it does not replace, the year/generation rule (commit 52829c6). Year/generation-specific terms remain the starting candidate for current-cycle SKUs; the two mechanisms below are the quality gate that those terms carry real traffic potential, plus a first-party-data layer the workforce gained with the 2026-06-09 GSC install.

**Why a floor at all (the underreporting note).** Keyword tools systematically underreport long-tail volume, because their data sources do not see queries occurring fewer than roughly a dozen times a month. AI search (ChatGPT, Claude, Perplexity, Gemini) now accounts for roughly 56% of traditional search-engine volume and is invisible to DataForSEO and every other keyword tool. A 100/mo DataForSEO floor therefore probably represents 150 to 200/mo of real demand once AI search and underreported long-tail are included. The floor is deliberately conservative for that reason.

### Mechanism A: volume-weighted primary keyword selection

**Step 1: minimum volume floor of 100 searches per month (DataForSEO, US).** 100/mo total searches (not unique users) translates to roughly 5 to 30 clicks per month depending on position (5 to 10 at position 5, 20 to 30 at position 1). At position 5 to 10 with a 2 to 5% transactional conversion that is 0.1 to 0.5 sales per month per page; aggregated across hundreds of PDPs it is meaningful long-tail traffic. Below 100/mo the math degrades to negligible per-page potential. The floor is the codified MINIMUM, not the target: if a SKU's exact-match generation-cut-tier-plate term already clears 500 or 1,000/mo with a winnable SERP, that is the primary and no fallback walk happens.

**Step 2: fallback hierarchy when the exact-match long-tail fails the floor.** KIRA walks DOWN the specificity ladder until a candidate meets the 100/mo floor, dropping the most-droppable attribute first:

1. **Plate (FG / AG), drop first.** A buyer searching "mercurial superfly 11 elite" usually means either plate.
2. **Tier (Elite / Pro), drop second.** Meaningful, but often searched without.
3. **Generation (11 / 17 / 6), drop third, only if necessary.**
4. **Model name, NEVER drop.** Dropping the model collapses intent.

Stop at the LOWEST specificity that meets the floor AND stays realistically rankable.

**Step 3: ranking realism check at the threshold.** Once a candidate meets the floor, verify the SERP is winnable: top 5 fully owned by Nike.com plus major retailers (Dick's, Soccer.com, JD Sports) means step UP to a more specific term; top 5 mixed with smaller or specialty retailers means winnable; ProSoccer already ranking somewhere in the top results (confirm via GSC) means a strong candidate. This preserves the year/generation rule's ranking-realism instinct, now applied at the volume threshold rather than instead of it.

### Mechanism B: GSC integration into KIRA Phase 1

The 2026-06-09 GSC install (Category A, sub-agent inheritance verified via Phase C, commit f3b179a) gives KIRA first-party query data the workforce previously lacked. KIRA layers it on top of Mechanism A. Revised 6-step Phase 1 protocol (canonical detail in `.claude/agents/keyword-research/agent.md` Section 9):

1. **Per URL, KIRA calls `mcp__gsc-server__search_analytics`** with `siteUrl: "sc-domain:prosoccer.com"` (this exact value is required), `dimensions: "query"`, `pageFilter: <the SKU URL>` with `filterOperator: "equals"`, `startDate` 90 days back (28 days for brand-new SKUs with no history), `endDate` today, `rowLimit: 100`. Capture query, impressions, clicks, CTR, position. (This tool takes `dimensions` as a comma-separated string and filters a page via `pageFilter`; there is no `dimensionFilterGroups` argument.)
2. **KIRA calls `mcp__gsc-server__detect_quick_wins`** for the URL. By default it surfaces positions 4 to 10 with CTR at or below 2% and at least 50 impressions (page-1, under-clicked opportunities); to hunt page-2 momentum (positions 11 to 20, ready to push to page 1), pass `positionRangeMin: 11, positionRangeMax: 20`. Both bands are prime primary-keyword candidates: real impressions, real ranking momentum, real upside.
3. **KIRA queries DataForSEO** for volume, KD, and intent on the exact-match long-tail term, the GSC-surfaced queries, the detect_quick_wins queries, and any fallback-hierarchy candidates.
4. **KIRA assembles a candidate set with composite scoring (judgment-based, not a formula):** DataForSEO volume (must clear the 100/mo floor for primary candidacy), GSC existing impressions (real demand even when DataForSEO underreports), GSC current position (positions 5 to 20 are striking distance), intent match (transactional > commercial > informational for PDPs), and ranking realism (winnable SERP).
5. **KIRA recommends a primary keyword to ORIN with rationale:** "Primary candidate: [keyword]. DataForSEO volume: [N]/mo. GSC existing position: [X.X]. GSC impressions last 90 days: [N]. detect_quick_wins flagged: [yes/no]. Composite recommendation: [primary]. Rationale: [why this beats the alternatives]."
6. **KIRA recommends supporting keywords:** higher-volume brand-level terms for body topical relevance, a different volume/intent profile than the primary, not competing for the same SERP slot. Plus (new requirement, added 2026-06-15): at least ONE pack/colorway/release-specific long-tail as the first secondary when the SKU carries a pack, colorway, or named release, exempt from the 100/mo floor (see Mechanism C below).

**New-SKU sparsity.** GSC data for brand-new SU26 SKUs is thin (the Day 3 Phantom 6 High Elite FG returned 2 impressions on 1 query). For new SKUs KIRA falls back to DataForSEO-only with the floor plus fallback hierarchy; for established SKUs (90 days of GSC data) composite scoring weights GSC heavily.

### Mechanism C: pack/colorway/release-specific secondary keyword discipline (added 2026-06-15)

Surfaced from a real-world observation: volume-weighted primary selection (Mechanism A) sometimes lands a primary that reads as tier-level or surface-level, not specific to the exact pack, colorway, or release. Example: "adidas f50 turf" as the primary on the Pro Turf Road to Glory SP26 PDP, accurate for tier-plus-surface but not specific to this pack. The primary correctly carries head-term SEO weight; the gap is that nothing on the page targets the buyer searching for the specific pack or colorway.

**Rule: KIRA's secondary keyword recommendations MUST include at least ONE pack/colorway/release-specific long-tail keyword per SKU, whenever the SKU carries a pack, colorway, or named release.** The pattern:

- **Primary:** unchanged, per Mechanism A (volume-weighted + GSC override, head-term weight).
- **Secondary 1 (new requirement):** the pack/colorway/release-specific long-tail. Examples: "adidas f50 hyperfast turf road to glory", "nike phantom 6 breakout pack su26", "croatia jersey 2026 away".
- **Secondary 2 to N:** semantic variants, intent-aligned long-tails, sibling-differentiation terms (current behavior, unchanged).

**Volume floor exemption.** Pack/colorway/release-specific secondaries are EXEMPT from the 100/mo volume floor; they are inherently long-tail and rarely register measurable tool volume. The floor governs PRIMARY candidacy only (Mechanism A, Step 1); this makes the exemption explicit for the pack-specific term so it is never dropped for thin volume. Document volume and difficulty when KIRA can retrieve them; leave them blank when KIRA cannot (never fabricate).

**Body copy.** SCRIBE weaves the pack/colorway-specific long-tail into the Description prose at least once, naturally. This gives the page topical relevance for both head-term searchers (via the primary) and pack-specific searchers (via the long-tail) without keyword stuffing. This one mention is permitted ALONGSIDE the single volume-selected supporting keyword (see 'Supporting keyword selection (cross-cutting)'); it is a deliberate carve-out, not a Gate 12 'multiple supporting keywords' violation.

**Keywords table.** The pack/colorway-specific long-tail surfaces as the FIRST secondary row in the brief's Keywords table, tagged `Secondary (pack-specific)` in the Type column, so it is visible at a glance during implementation (see 'Brief Output Structure (added 2026-06-09)' plus the 'Keywords table (added 2026-06-15)' note).

When a SKU genuinely has no pack, colorway, or named release (a plain staple product), the requirement does not apply; KIRA notes its absence rather than inventing one.

Cross-references: `.claude/agents/keyword-research/agent.md` Section 9 'Volume-weighted primary keyword selection + GSC integration' (Phase 1 pack-specific research step + supporting-keyword output); `.claude/agents/on-page-seo/agent.md` Section 9 (body-weave self-check) + Section 13 (Keywords table); `.claude/agents/master-strategist/agent.md` Section 9 (lane spec carries the pack-specific secondary) + Section 11 Gate 12 (carve-out) + Gate 15 (Keywords table re-check); `context/page-type-playbooks/product-page-playbook.md` 'Keywords table (added 2026-06-15)'. Forward-only: the existing 20 PDPs (Day 3 batch + Batch 2) keep their current keyword strategy; Batch 3 onward complies.

### Integration with existing disciplines

- **Year/generation rule (commit 52829c6):** REFINED, not replaced. Year/generation-specific terms are still the starting candidate; the floor plus fallback is the traffic-realism gate on them.
- **Cross-brief uniqueness (commit ae42964) and primary-keyword cannibalization:** within a multi-SKU batch each primary must stay unique. If GSC shows two siblings drawing impressions on the same query, KIRA assigns that query to one SKU as primary and steps the other up the fallback hierarchy. ORIN's pre-dispatch differentiation pass already enforces primary-keyword uniqueness; GSC just refines the source data.
- **Dual registry (this morning's commit):** Registry 1 (the white-label keyword sheet, Drive, Category B) is still read by ORIN at the pre-dispatch differentiation pass. KIRA now ALSO reads GSC during Phase 1. Both inform primary selection. The manual sheet handoff (Mike enters approved keywords in the PDPs-tab Primary KW column) stays the permanent pattern; GSC reading does not change registry ownership.

### Enforcement

KIRA owns the GSC reads and the primary-keyword recommendation (Phase 1). ORIN verifies the recommended primary clears the 100/mo floor before assigning it in the lane spec at pre-dispatch, and can spot-check KIRA's GSC reads at the parent level if an anomaly surfaces (GSC is Category A, callable by ORIN directly). SCRIBE works from KIRA's primary-keyword output and does NOT independently call GSC for primary selection unless ORIN specifically tasks a verification. Forward-only: Day 3 re-run briefs (commit 957dc3c) and prior briefs keep their old-rule primary keywords; Mike retains a manual override at white-label-sheet entry time (for example entering `nike mercurial superfly 11` for IO8219-900 instead of the brief's `nike mercurial superfly 11 elite fg` when real-world ranking data favors the broader term). The discipline applies from the next batch dispatch onward.

### KIRA-first routing (mandatory for PDP batches, added 2026-06-09)

For every PDP batch dispatch starting with the next batch, ORIN dispatches KIRA FIRST for keyword research, before SCRIBE. KIRA runs the 6-step Phase 1 protocol and returns per-SKU primary keyword recommendations; ORIN verifies the 100/mo floor, resolves cross-SKU primary collisions (one SKU takes the contested query, the others step up the fallback hierarchy), and folds the approved primaries into the differentiation lane specs before dispatching SCRIBE. SCRIBE works from KIRA's primary and does not select its own. This makes specialist separation explicit: keyword research is dedicated KIRA work with GSC integration, not absorbed into ORIN's parent-level workload. A single-PDP or Tier 3 fast-turnaround case may fold KIRA's protocol into ORIN's parent-level work when a separate dispatch is disproportionate, but the floor plus GSC protocol still applies. ORIN procedure: `.claude/agents/master-strategist/agent.md` Section 9 'KIRA-first keyword research for PDP batches'.

Cross-references: `.claude/agents/keyword-research/agent.md` Section 9 'Volume-weighted primary keyword selection + GSC integration' (canonical 6-step protocol + composite scoring + recommendation format); `.claude/agents/master-strategist/agent.md` Section 9 (volume-floor enforcement at pre-dispatch) + Section 11; `.claude/agents/on-page-seo/agent.md` Section 9 (year-specificity refinement + KIRA input contract); both page-type playbooks 'Primary keyword selection'; 'Tool inventory' (GSC, Category A, `search_analytics` + `detect_quick_wins`); 'Dual Registry Architecture for Cross-Batch Coordination'. Year/generation origin: commit 52829c6.

## Editorial philosophy (added 2026-06-02)

The structural gates (Gate 13 anti-stuffing, Gate 14 specific counts) and the judgment-dependent Phase 4 disciplines (image precision, parallel construction, supporting keyword selection) catch specific failures, but they do not capture the underlying editorial stance the workforce writes from. SCRIBE was producing structurally-correct copy that met all 14 gates and the prior Phase 4 disciplines yet still lacked emotional resonance, reader-focused clarity, and value-first orientation, the qualities that actually move a buying decision. This section is that stance, written for every agent that produces reader-facing copy (SCRIBE primarily; future content agents secondarily).

These four sub-disciplines are judgment-dependent, not pattern-matchable. They live at SCRIBE Phase 4 (drafting-time application), ORIN orchestrator defense-in-depth (sanity scan, flag obvious failures, not strict enforcement), and here as cross-cutting philosophy. They are NOT new gates (the suite stays at 14; gates govern structural patterns, editorial philosophy is judgment) and are NOT script-enforced (too judgment-dependent for `voice_check.py` regex).

The example that surfaced the gap, URL #3 (national-team-scarves) Short Description: "Soccer scarves started on the freezing terraces of early-1900s English grounds, and they never left. Shop World Cup scarves like Argentina's albiceleste, Mexico scarf called 'verde'..." The opening line does emotional work (heritage, ritual, place); the next sentence drops into list-of-products mode and the emotional arc collapses. A reader-first version sustains the emotional thread before transitioning to product specifics.

### 1. Reader-first copy orientation

Body copy serves the buyer's emotional connection to what they are buying. SEO ranking is the byproduct, not the goal; keywords appear because they describe what the reader actually cares about, not because they need to appear. Per-sentence test: does this sentence serve the reader's decision-making, or the algorithm? Would a buyer reading it for the first time find it valuable, or feel they are being marketed to?

Anti-patterns: keyword surfacing without reader value (the "ten federations, four brands" stacking Gate 14 caught was a structural manifestation of this deeper failure); specification listing without emotional context (the "caps $34.99, scarves $24 to $44, flags $44.99" pattern Gate 13 caught was the same); generic positioning that could describe any product ("premium quality", "top-tier selection", "best-in-class"); brand or manufacturer specifications leading the copy ("adidas produces the kit using Heat.RDY moisture-wicking fabric") before reader value is established. Natural alternatives: sentences that describe specific buyer experience or identity ("how fans show up when the anthem starts"), concrete sensory anchors ("colors raised, voices behind them"), place / ritual / heritage tied to buyer identity ("what the Rose Bowl section wears").

### 2. Cognitive load reduction

Body copy is read while the buyer is mid-decision, evaluating brand, color, fit, price, occasion, and alternatives. Copy that adds load loses the sale.

- **Sentence length variance:** short 5 to 10 words for emphasis, transition, or a punctuation moment; medium 15 to 25 words for substance; long 30+ words only when narrative justifies (rare). A short, medium, short rhythm reads cleanly; long sentence after long sentence creates dense paragraph blocks. Avoid the dense block.
- **One concept per sentence:** if a sentence joins two ideas with "and", "but", "while", or "with", consider whether splitting serves the reader. Multiple ideas per sentence force the reader to hold both in working memory.
- **Concrete over abstract:** "fans raise scarves overhead during the anthem" beats "scarves embody the ritual of supporter culture"; "six matches into the tournament cycle" beats "deep into the competition phase". Specific physical actions, specific places, specific times beat abstract framings.
- **Scan-ability:** the first sentence of each paragraph and each H2 carries the value proposition. Most collection-page readers scan; they should get the gist without reading every word. Do not bury the lead.

### 3. Value-first sequencing

Lead with what the buyer cares about, not what the product is technically. Specifications, brand-IP context, and manufacturing details come AFTER the emotional / value anchor. Each body section follows the arc:

1. **HOOK (emotional / identity anchor):** why this matters to the buyer's life. "What fans wear when the anthem starts." "The kit your section will be wearing in June." "Carried home from Mexico '86, carried back for '26."
2. **CONNECTION (specific scenario):** how the buyer uses or experiences this. The specific use case, occasion, or ritual; the concrete sensory or social context; the buyer's actual lived experience.
3. **SPECIFICS (product context):** what is in the collection, brand details, occasion fit. Tier / positioning language without specific prices; brand callouts with narrative justification; material or construction details only where they serve the buyer's decision.
4. **ACTION (clear next step):** implicit ("the full federation roster") or explicit when natural ("shop the lineup before kickoff week"). Avoid pressured CTAs ("buy now", "don't wait").

Anti-pattern, starting with brand or spec data before reader value. INCORRECT: "adidas produces the federation kit lineup using Heat.RDY moisture-wicking fabric in Stadium and Authentic tiers. The 2026 collection includes twelve national teams with..." CORRECT: "The 2026 World Cup brings the federations to a continent that has been waiting forty years for the tournament. The kits arrive in two tiers, Stadium for the everyday and Authentic for match day, across the adidas roster including Argentina, Mexico, Germany, Spain, and more."

### 4. Positive emotional anchoring

Copy evokes the positive emotions associated with the purchase: anticipation, identity, belonging, pride, ritual. It never reaches for manipulation, scarcity, fear, or status anxiety. Positive anchors invite the reader into a community or experience they want to belong to; manipulation pressures the reader through fear or insecurity. The first builds long-term brand affinity; the second extracts a single transaction.

**Positive anchors (use), with phrase examples:**

- **BELONGING:** "how fans show up", "what the section wears", "the colors of your side".
- **IDENTITY:** "colors that say what side you are on", "the crest carried at the shoulder".
- **RITUAL:** "raised when the anthem starts", "held high through the opening chants".
- **ANTICIPATION:** "six matches into the tournament cycle", "with kickoff week ahead".
- **HERITAGE:** "from the 1986 archive to the 2026 Stadium tier", "the legacy carried forward".
- **PLACE:** "the Rose Bowl, the diaspora's home stadium", "the terraces of early-1900s English grounds".

**Manipulation patterns (never use), with phrase examples:**

- **SCARCITY:** "only 5 left", "selling out fast", "limited stock".
- **FOMO:** "don't miss", "before they are gone", "act now".
- **STATUS ANXIETY:** "the kit serious fans wear", "for true supporters only", "what real fans choose".
- **HYPERBOLE:** "the greatest scarf ever made", "the perfect kit", "unmatched quality".
- **FALSE URGENCY:** "limited time", "won't last", "while supplies last".

### 5. Outcome-based copywriting (added 2026-06-03, extends dcfe6da)

Buyers don't buy products. They buy outcomes. The cleat isn't the product. The Saturday morning where their kid plays with confidence is the product. The jersey isn't the product. Wearing their nation's colors during the tournament is the product. Short Description and Description prose paint a concrete picture of the buyer's life AFTER they own the product, showing the desired outcome they are really buying, not the features that produce it. This sub-discipline is the operational technique that delivers on sub-disciplines 1 through 4: it IS reader-first (the outcome is what serves the reader), it uses low-load concrete sentences, it sequences the outcome first and specs after, and it anchors in belonging, identity, ritual, anticipation, heritage, and place. Sub-disciplines 1 to 4 are what to BE; sub-discipline 5 is what to DO.

**Three techniques:**

1. **Future-pacing.** Use sensory description to place the buyer in the moment of using the product. Outcome: "Saturday morning. Your kid's first kick of the day. The grass is still wet, and they're already grinning." Feature (avoid): "Soft padding and easy step-in design."
2. **Show the transformation.** Position the buyer as moving from one state to another: the kid who was uncertain becomes the kid who's confident; the midfielder who couldn't see the field becomes the one who controls it; the parent worried about quality becomes the parent who trusts the gear.
3. **Concrete over abstract.** Outcomes are specific scenes, not abstract claims. Concrete: "The moment you see the gap and take it." Abstract (avoid): "Built for fast sprints." Concrete: "Their first goal in the new cleats. The way they look back at you on the sideline." Abstract (avoid): "Premium comfort and performance."

**What to avoid (translate, don't list):**

- Feature-listing in prose ("Synthetic upper for durability"). Specs belong in the Product Details bullets.
- Spec-recital in prose ("170 grams, FlyWeave Ultra, ZoomX foam"). Specs belong in the bullets.
- Abstract benefit claims ("premium comfort", "built for performance"). Show the comfort or the performance through an outcome scene instead.
- Manufacturer marketing language verbatim. Translate it into buyer-outcome terms.
- Manipulation outcomes (fear, exclusion, status anxiety, FOMO). Forbidden per sub-discipline 4.

**Application by field:**

- **Short Description (50 to 100 words on PDPs, the hero-block equivalent on collections):** entirely outcome-based, no feature mention. The full hook paints the scene the buyer is moving toward. This is the most aggressive application, because the Short Description is the emotional hook above Add to Cart.
- **Description prose H2 sections (PDPs and collections):** each prose H2 opens with the outcome (the scene, the moment, the identity), then connects to the product where natural. The heritage section can use heritage as the outcome ("the cleat family worn on World Cup pitches since 1979"). The use-case section uses the use case as the outcome ("the kid who lives in open space, the runner"). The fit section can frame fit as the outcome ("easy from the first session, broken in by the second").
- **Description Product Details bullet H2:** bullets carry the WHAT (specs). The outcome rule does NOT apply to bullets; they stay technical and scannable.
- **Collection-page prose:** the same principle at the collection level. Not "shop the adidas Copa Pure IV collection" but "the cleat family that lives where touch meets the moment: every tier from Elite to Junior League, every level of player who plays the Copa way."
- **FAQ answers:** apply where the question is about a buyer outcome ("how does this fit", "is this right for my kid"). Do not apply where the question is purely technical ("what's the difference between the Elite and Pro tiers").

Judgment-dependent, not script-enforceable (no regex can tell outcome prose from feature prose). It lives at SCRIBE Phase 4 application plus ORIN orchestrator sanity scan. This extends the editorial philosophy commit dcfe6da; it does not replace it.

**Architectural learning note.** Editorial philosophy discipline (added 2026-06-02 after Gate 14 codification): Gate 13 anti-stuffing and Gate 14 specific counts catch structural manifestations of a deeper editorial philosophy gap. SCRIBE was producing structurally-correct copy meeting all gates but lacking emotional resonance, reader-focused clarity, and value-first orientation. Four sub-disciplines codified as Phase 4 self-checks plus workforce-conventions philosophy: (1) Reader-first copy orientation, body copy serves buyer's emotional connection, not algorithm. (2) Cognitive load reduction, sentence length variance, one concept per sentence, concrete over abstract, scan-ability. (3) Value-first sequencing, each H2 follows hook -> connection -> specifics -> action arc. (4) Positive emotional anchoring, use belonging / identity / ritual / anticipation / heritage / place anchors; avoid scarcity / FOMO / status anxiety / hyperbole / false urgency manipulation patterns. These are judgment-dependent disciplines, not pattern-matchable structural rules. They live at SCRIBE Phase 4 application plus ORIN orchestrator sanity scan plus workforce-conventions cross-cutting philosophy. NOT codified as new gates (gates govern structural patterns; editorial philosophy is judgment). NOT script-level enforced (too judgment-dependent for regex). Surfaced from Day 2 batch #1 review where briefs met all 14 gates and the 4 prior Phase 4 disciplines but lacked the editorial layer that drives buyer connection.

**Extension note (2026-06-03).** A fifth sub-discipline, '### 5. Outcome-based copywriting' (above), was added 2026-06-03 as the operational technique that delivers on the original four: paint the buyer's life after they own the product; show the outcome they are really buying, not the features that produce it. Same judgment-dependent, non-script-enforced, forward-only treatment as the original four. KI0662 PDP brief in main (68664ca) not fix-forwarded per Mike's decision.

Cross-references: both page-type playbooks 'Editorial philosophy disciplines (Phase 4 self-checks, added 2026-06-02)', `.claude/agents/on-page-seo/agent.md` Section 9 'Editorial philosophy disciplines' + Section 11, `.claude/agents/master-strategist/agent.md` Section 9 trust-but-verify + Section 11 Gate 12. Related ephemeral-data-avoidance patterns: 'Content evergreen-ness' (Gate 13 pricing) and 'Unsupported specific counts (Gate 14, cross-cutting)'.

## PDP optimization discipline (cross-cutting)

PDPs and collection pages now have meaningfully differentiated optimization disciplines. PDPs serve product-specific search intent (a buyer searching for one cleat in one tier) rather than the category intent collections serve, which drives field-length constraints by field, cross-SKU title uniqueness, image and taxonomy requirements, and a body structure that splits reader-first prose from technical bullets. The nine PDP-specific disciplines are canonical in `context/page-type-playbooks/product-page-playbook.md` 'PDP-specific SEO discipline (added 2026-06-02)'; they apply to Day 3+ PDP production and sit on top of all shared discipline (Gate 13, Gate 14, the Phase 4 editorial disciplines, brand IP, year-specificity, keyword distribution). The governing operational principle is reader-first: write to the buyer's needs and desires, not Google's algorithm; specs in bullets, never prose; positive emotion, no manipulation; human-written, not AI-generated (per 'Editorial philosophy (added 2026-06-02)' above).

### ProSoccer Shopify field naming (Hyper theme)

ProSoccer's Hyper theme exposes three distinct description-related fields, and they are NOT interchangeable:

- **Title:** the product title field.
- **Short Description (metafield):** renders in the hero block above Add to Cart. A brief reader-first emotional / value-prop hook.
- **Description (body_html):** renders in the collapsible accordion below the product images. The full body content (prose H2 sections + the "Product Details" bullet H2).

(A "Sub Title" metafield also appears in admin with content like "Multi-Color/Black"; whether the theme renders it visibly is unverified, flagged for Mike in `work-log/follow-ups.md`.)

### PDP field length reference (hard limits)

| Field (ProSoccer admin name) | Limit |
|---|---|
| Title | 30 to 100 characters (min AND max) |
| Short Description (metafield, hero block) | 50 to 100 words |
| Description (body_html, accordion) | tiered by complexity: Simple ~125 to 200 / Standard ~220 to 360 / Complex ~320 to 450 words (Standard and Complex raised 2026-06-09 for the Care and Maintenance H2) |
| Meta Title | 60 characters maximum, INCLUDING the Hyper theme brand suffix (so the input field stays under approximately 48 to 50 chars) |
| Meta Description | 160 characters maximum |
| URL handle (slug after `/products/`) | 70 characters maximum |

These are hard limits, not targets. The Description body carries a +15-word tolerance band before FAIL (codified 2026-06-10): Simple 215, Standard 375, Complex 465, counted full-body (editorial prose + Product Details bullets + Fit Notes + Care bullets; FAQ separate). SCRIBE drafts toward the base ceiling (200 / 360 / 450); the band only absorbs a few-word overage at the gate so single-digit counts do not trigger a prose rewrite, and it is not a license to creep past the tolerance line. The tiered Description range supersedes the earlier single "150-word" figure, which is now interpreted as the Short Description metafield, not the Description body. SCRIBE verifies each in Phase 4; ORIN re-checks at the orchestrator layer (Section 11 Gate 13).

### Product complexity classification

Description length is set by product complexity. Classification test: if a buyer needs more than 2 minutes to choose between sibling products in the same family, the product is complex; if they grab and go, it is simple.

- **Simple (~125 to 200 words):** keychains, lapel pins, magnets, decals, stickers, mini balls, basic flags, simple practice cones.
- **Standard (~220 to 360 words):** training and match balls, bags, backpacks, apparel with basic variants, shin guards, single-tier goalkeeper gloves.
- **Complex (~320 to 450 words):** soccer cleats (tier / plate / colorway / generation matrix), authentic jerseys (player versions, kit details), tournament-edition products with a collectibility narrative, technical goalkeeper gloves, anything needing sizing / fit / surface guidance.

(Standard and Complex ceilings raised 2026-06-09 from ~200 to 300 and ~300 to 400 respectively to accommodate the Care and Maintenance H2, which adds ~40 to 60 words of procedural bullets. Simple unchanged. Canonical: `context/page-type-playbooks/product-page-playbook.md` 'Care and Maintenance H2 discipline (added 2026-06-09)'.)

### Description structure: prose H2 + "Product Details" bullet H2

The Description splits reader-first prose from technical bullets. Prose H2 sections (overview, use case, identity / belonging, heritage, sizing / fit) carry the WHY; a dedicated "Product Details" H2 bullet list (the exact ProSoccer-native term, per live PDPs like the Nike Superfly 11 Club) carries the WHAT (materials, plate / surface, tier features, weight, technology). Never list technical specs in prose. H2 count flexes by complexity (Simple 2 to 3, Standard 3 to 4, Complex 4 to 5); always include "Product Details" when there are specs worth listing. For triggering categories (footwear, jerseys, apparel, goalkeeper gloves, soccer balls) a second bullet H2, "Care and Maintenance", follows Fit Notes and carries procedural care bullets; care content lives there rather than as a Product Details bullet. Excluded categories (accessories, flags, small merchandise, trading cards, standalone stickers and patches) carry no Care H2. Canonical: `context/page-type-playbooks/product-page-playbook.md` 'Care and Maintenance H2 discipline (added 2026-06-09)'.

### FAQ reconciliation across page types

Collection pages keep the conditional FAQ rule (skip unless the FAQ adds net-new value beyond the Long Description, per `context/page-type-playbooks/collection-page-playbook.md`). PDPs RECOMMEND a FAQ, governed by the SAME net-new-value criterion: 3 to 5 Q-and-A pairs that the Description body does not already cover, that real buyers ask (sizing, plate selection, sibling comparison, use-case fit, care / durability), and that add measurable decision value. Skip entirely if fewer than 3 genuinely useful Q-and-As exist. The criterion is identical across page types; only the default posture differs (collections lean skip, PDPs lean include). FAQ heading hierarchy (added 2026-06-09; H2 wording scoped by page type 2026-07-27): when a FAQ is included, it uses a single H2, an H3 per question, and paragraph answers. On PDPs the H2 is `FAQs about [short product name]` (REQUIRED; the bare "Frequently Asked Questions" is not used on PDPs); collection pages use the bare "Frequently Asked Questions". Rationale: FAQ schema is generated from the H3 question-and-answer pairs, not the wrapper H2, so naming the product on PDPs costs nothing structurally and reads better mid-page (see `context/page-type-playbooks/product-page-playbook.md` 'FAQ heading hierarchy discipline (added 2026-06-09)', 'Why the product-name H2 is canonical for PDPs'). Codified at the playbook level: `context/page-type-playbooks/product-page-playbook.md` 'FAQ heading hierarchy discipline (added 2026-06-09)' and the matching `context/page-type-playbooks/collection-page-playbook.md` section; SCRIBE Phase 4 self-check and ORIN Section 11 Gate 15 enforce it.

**Architectural learning note.** PDP optimization discipline codification (added 2026-06-02, corrected 2026-06-02): TinySEO PDP analysis surfaced PDP-specific SEO requirements not previously codified. PDPs serve different search intent than collections (product-specific vs category queries) and need different field-length constraints, schema considerations, and content structures. The first codification used a single "Product Description 150 words max" figure; on review this conflated Shopify's two description fields and contradicted 2026 ecommerce ranking data (top-ranking ecommerce pages average 200 to 310 words; complex products competitive at 300 to 400), the playbook's own worked examples (250 to 350 words), and the Mexico v5 canonical (340 words). Corrected: Short Description metafield (hero block) 50 to 100 words; Description body_html (accordion) tiered Simple ~125 to 200 / Standard ~200 to 300 / Complex ~300 to 400. The "150" is interpreted as the Short Description metafield. Nine additions codified: (1) field length constraints split by field using ProSoccer's admin field names, (2) unique titles for pack/series products (tier / plate / colorway / generation), (3) URL handle 70-char constraint, (4) image alt text format, (5) image optimization flags in the workforce briefing, (6) taxonomy category requirement, (7) Description structure with prose H2 sections plus a dedicated "Product Details" bullet H2 (prose = WHY, bullets = WHAT), (8) FAQ recommended with net-new-value criterion, (9) reader-first operational principle reinforced as the governing principle for all PDP copy. FAQ reconciliation: collections stay conditional, PDPs recommended with the same criterion. Collection-page Long Description ceiling unchanged at 500. PDPs and collections now have meaningfully differentiated disciplines. Day 3 PDP batch will be the first production batch under full PDP discipline. Optional script-level length checks in `voice_check.py` deferred to Mike's decision (field-specific length limits do not fit the whole-file regex model the `\bAdidas\b` check uses).

Cross-references: `context/page-type-playbooks/product-page-playbook.md` 'PDP-specific SEO discipline (added 2026-06-02)' (canonical, all 9 additions with examples + reader-first principle), `.claude/agents/on-page-seo/agent.md` Section 9 'PDP-specific Phase 4 self-checks' + Section 11, `.claude/agents/master-strategist/agent.md` Section 9 trust-but-verify + Section 11 Gate 13.

## Brief content requirements (data-backed)

Both PDP and collection-page briefs must surface a minimal data-backed keyword research block and respect the product-page link policy. These are hard requirements, not optional.

### Keyword research surfacing (minimal visible format)

Every visible brief must include a `## Keyword research` block at the top with:

- Primary keyword on one line with monthly search volume and keyword difficulty.
- Supporting long-tail keywords as a comma-separated list with optional volume per term.
- Current ranking on one line: position number for the primary keyword from DataForSEO SERP API, OR "not in top 100." Lookup date included.
- WARNING line (top 5 only): the explicit equity-risk note per 'Ranking-aware posture' above.

Nothing else surfaces in the visible block. No alternatives considered. No rejection reasoning. No intent percentages. No trend data. No source-of-record paragraph. No LLM ranking line. These all live in the workforce-internal briefing as the defensibility audit trail (LLM ranking is deferred entirely per 'Ranking-aware posture' above).

DataForSEO is the source of record. The workforce-internal briefing must document: primary keyword choice with volume + KD + intent (with probabilities from `dataforseo_labs_search_intent` plus main_intent from `dataforseo_labs_google_keyword_overview`), 2 to 3 alternatives considered each with volume + KD + 1 to 2 sentence why-not-chosen reasoning, selection reasoning combining data and avatar fit, supporting long-tail keywords with volume data, and the source-of-record paragraph (calls executed, locations, timestamps, status codes).

Trust-me keyword choices are not acceptable for agency-grade work. The primary keyword selection must be defensible against "why this keyword and not the other one" with concrete data; the workforce-internal briefing is where that defensibility lives. The visible brief stays minimal.

The visible '## Keyword research' block format is canonical in `templates/consolidated-page-brief-template.md` and replicated in `.claude/agents/on-page-seo/agent.md` Section 13.

### Product page link policy: internal only (External links field omitted entirely on PDPs)

PDP body copy includes internal links to ProSoccer collection or product pages ONLY. External links are forbidden on PDPs. The reasoning:

- External links leak link equity off-site during the purchase consideration window.
- They give the customer an exit ramp from the purchase decision.
- Authority signals through external links belong on homepage and blog content, not on PDPs.

If body copy references external tournaments, events, or context (Asian Cup, Champions League, Premier League, etc.), keep the reference as plain text. Do not hyperlink to external sites. If the reference needs a destination, link to an internal ProSoccer page instead (e.g., a related collection).

**The External links field does not appear on PDP briefs at all.** Omitting the field by construction (vs writing "External links: none") is intentional; the visible brief should not carry empty fields. Collection pages may include external links per the collection-page playbook's link strategy; the External links field appears on collection-page briefs only when an outbound link is part of the recommendation.

The PDP internal-link-only policy is canonical in `context/page-type-playbooks/product-page-playbook.md` 'Internal links only on product pages'. Collection-page external-link policy stays under the collection-page playbook's link strategy section.

## Cleanup and retention policy

Page-optimization deliverables are operational artifacts with a finite useful life. The audit trail of who-decided-what lives in commit messages and PR descriptions; the deliverable file itself becomes stale once the recommendation has been implemented and either succeeded or been superseded.

### Retention window

- **Active retention:** 6 to 12 months from session date. The exact window depends on the deliverable type (whitelabel audits clear faster than evergreen brief work) and is decided at quarterly cleanup time, not pre-fixed per file.
- **Long-tail exception:** any deliverable that remains the source-of-truth for a live page's copy stays in the repo indefinitely. The Mexico v3 brief, for example, governs the Mexico page's copy until a v4 supersedes it; v3 stays in the repo until v4 lands.

### Quarterly cleanup pass

Once per quarter, ORIN (or Mike directly) runs a cleanup pass:

1. Enumerate all session folders under `deliverables/page-optimizations/` and `deliverables/page-optimizations/whitelabel-audit/`.
2. For each folder older than 6 months from today: review the contents to confirm the deliverables have been implemented, superseded, or are no longer load-bearing.
3. Folders meeting the retention threshold and review criteria are removed in a dedicated cleanup commit.
4. The cleanup commit message lists every removed folder and the disposition (implemented / superseded / abandoned). This preserves the audit trail even after the file is gone.

### Cleanup commit structure

The cleanup commit is its own commit, not bundled with other work. Commit message format:

```
Quarterly cleanup YYYY-Q[N]: removed N page-optimization session folders past retention window

Folders removed (with disposition):
- deliverables/page-optimizations/YYYY-MM-DD_session-NN/: implemented YYYY-MM-DD via Shopify admin
- deliverables/page-optimizations/whitelabel-audit/YYYY-MM-DD_session-NN/: superseded by [reference]
- ...
```

The disposition note is the audit trail of why each folder was safely removable.

### Cleanup does NOT apply to

- Agent-specific briefings under `.claude/agents/<agent-name>/briefings/`. Those are agent-internal context that future sessions read; retention is per-agent and managed in the agent's own learnings.md compaction protocol.
- The `templates/` directory.
- Any deliverable file in `deliverables/technical-fixes/`, `deliverables/keyword-research/`, `deliverables/phase-2-discovery/`, or other non-page-optimization deliverable folders. Those have their own retention conventions to be documented separately as they emerge.

## Tool inventory

This section is the canonical truth source for which MCP servers and external tools are operationally available to the workforce today. Agent narrative sections (`## 5. Tools and MCP Connections` in each `.claude/agents/<agent-name>/agent.md`) may reference MCP namespaces aspirationally; this inventory governs what's actually callable. When a narrative description and this inventory disagree, this inventory wins.

Refreshed: 2026-05-26 (Phase C verification round).

### MCP categories (Category A vs Category B)

MCP servers split into two categories based on transport and credential handling. The distinction governs CREDENTIAL propagation once a tool is allowlisted, NOT whether a sub-agent can call the MCP (see the controlling rule immediately below).

**Controlling rule (corrected 2026-06-17).** Sub-agent MCP callability requires BOTH halves: (1) the server declared in the agent's `mcpServers:` block, AND (2) the MCP tools allowlisted in the agent's `tools:` field (via a `mcp__<server>__*` wildcard or a bare `mcp__<server>` server token, OR by omitting `tools:` entirely to inherit all parent tools). The `mcpServers:` declaration ALONE does NOT grant callability when `tools:` is a restrictive allowlist that omits the MCP tokens. The Category A / Category B split below is a CREDENTIAL distinction (whether credentials reach the sub-agent once a tool is allowlisted), not a callability distinction; callability is governed by the `tools:` allowlist for every server class.

**Historical correction (2026-06-17).** The earlier framing here held that a `mcpServers:` declaration alone grants Category A sub-agents direct callability, "verified 2026-05-26 via Phase C." That was wrong. Commit `0c6dbb3` (2026-05-26, "Architecture refinement: Category A vs B distinction codified") MOVED the `mcp__*` tokens OUT of each agent's `tools:` field and INTO a new `mcpServers:` block in the same commit, on the incorrect premise that declaration alone suffices. Before `0c6dbb3` (from commit `22f29dc`, 2026-05-08) the `tools:` field carried real `mcp__<server>` tokens, so MCP was genuinely callable; the refactor removed them. The "verified 2026-05-26 via Phase C" claim covered the PRE-refactor config (which still had the tokens in `tools:`); the same-commit refactor invalidated that config without re-test (tested config != shipped config). The result: from 2026-05-26 to 2026-06-17 no sub-agent could call MCP, which is the true origin of the "Category B OAuth inheritance gap" narrative and the all-parent-level execution in Batches 2 to 3. SUPERSEDED by the 2026-06-17 KIRA Phase C re-verification (commit `be7ee36`: KIRA called `gsc-server` `list_sites` + `search_analytics` and `dfs-mcp` `keyword_overview` successfully at sub-agent level once the `tools:` wildcards were restored) plus the workforce-wide allowlist restoration that followed. Record preserved and marked superseded, not deleted.

**Category A: stdio transport, environment-variable credentials.** Credentials live in environment variables and propagate reliably to the sub-agent's MCP client once the tool is allowlisted. When a Category A server is BOTH declared in `mcpServers:` AND allowlisted in `tools:` (per the controlling rule above), the sub-agent can call `mcp__<server>__*` tools directly. (Superseded note: the prior text claimed the `mcpServers:` declaration alone sufficed, "verified working 2026-05-26 via Phase C across SCRIBE, VERITAS, and RECON"; that claim covered the pre-`0c6dbb3` config and did not hold after the same-day refactor stripped the `tools:` tokens. See 'Historical correction (2026-06-17)' above.) Sub-agent callability re-verified 2026-06-17.

Category A servers:

- `dfs-mcp` (DataForSEO; DataForSEO API credentials via env)
- `firecrawl-mcp` (Firecrawl; `FIRECRAWL_API_KEY` via env)
- `tavily-mcp` (Tavily stdio variant; `TAVILY_API_KEY` via env)

**Category B: HTTP transport with OAuth via the claude.ai connector.** These are claude.ai-hosted connectors (e.g. Google Drive). Per Claude Code's documented behavior, a string-referenced server shares the parent session's authenticated connection, so credentials generally DO reach the sub-agent once the tool is allowlisted. The real, narrower caveat: some claude.ai connectors can be unavailable in headless / cron runs, or where the upstream identity provider only accepts claude.ai's OAuth redirect URL (authenticate in claude.ai first). (Superseded note: the prior text asserted OAuth tokens never propagate and direct sub-agent calls always fail authentication; that conflated the missing `tools:` allowlist with an OAuth limitation. See 'Historical correction (2026-06-17)' above.) Operational guidance for Drive is unchanged in practice: ORIN reads the white-label sheet at the parent level and injects rows into specialist task context, because KIRA / SCRIBE do not need Drive and the parent-read keeps the connector caveat off the sub-agent path, not because direct calls are impossible.

Category B servers:

- `claude_ai_Google_Drive` (Google Drive via claude.ai OAuth connector; reads from the January 2026 audit folder and other shared Drive artifacts)
- `claude_ai_Tavily` (OAuth-authenticated Tavily via claude.ai connector; superseded by Category A `tavily-mcp` for sub-agent use, kept registered at parent session for ORIN's top-level discovery work when full-page extraction is needed)

This category split is a CREDENTIAL distinction, not a callability one (see the controlling rule above). Both classes are callable at sub-agent dispatch once the server is declared in `mcpServers:` AND its tools are allowlisted in `tools:`. Category A credentials (env-var) propagate reliably; Category B (claude.ai OAuth) carries the headless / redirect caveat noted above. The earlier claim that the split is "structural" and resolves only via a future OAuth-inheritance release was based on the superseded premise that `mcpServers:` declaration alone governs callability.

### Verification discipline for architecture changes (added 2026-06-17)

A "Verified" claim in any agent definition, playbook, convention, or commit must include: (1) the test METHOD (the specific test executed), (2) a test OUTPUT excerpt (a representative result), and (3) the verification ARTIFACT location (commit hash or file path holding the evidence). A claim that lacks these three is marked "observed-not-verified" and must be re-verified before it is cited in an architectural decision.

**Case study (the rule's origin): commit `0c6dbb3` (2026-05-26).** That commit performed a refactor (moving `mcp__*` tokens from `tools:` into `mcpServers:`) AND recorded its own verification ("Verified 2026-05-26 via Phase C") in the SAME commit. The verification covered the pre-refactor config; the refactor invalidated it without re-test, and the broken state went undetected for ~3 weeks (the all-parent-level execution in Batches 2 to 3). Lesson: **refactor + verification in the same commit is high-risk** because the verification can cover a pre-refactor config the refactor then invalidates. Future verifications must either be SEPARATED from the refactor commit they verify, OR the verification commit must explicitly state which config was tested with the artifact preserved. The 2026-06-17 KIRA fix follows this: the allowlist fix (commit `be7ee36`) and its Phase C verification are recorded with method + output excerpt + the re-verification artifact, separate from the original mislabel.

### Operational (live, callable today)

- **DataForSEO MCP, `mcp__dfs-mcp__*`** (Category A). Pay-per-use API access covering SERP data, keyword research, keyword difficulty, search intent, on-page audit, backlinks, domain analytics, and DataForSEO Labs endpoints. Credentials verified 2026-05-26 (status_code 20000 returned on `mcp__dfs-mcp__serp_locations`). Sub-agent inheritance verified 2026-05-26 via Phase C. Workforce-wide hard cap $100/month per Section 12 of each agent.
- **Firecrawl MCP, `mcp__firecrawl-mcp__*`** (Category A). Single-URL scraping, structured extraction, site mapping, bulk crawling, interactive sessions, monitor and agent endpoints. `FIRECRAWL_API_KEY` in env. Installed 2026-05-26; sub-agent inheritance verified the same session (Phase C: status 200 returned on Liverpool PDP, Predator PDP, Predator collection page from SCRIBE, VERITAS, and RECON respectively).
- **Tavily MCP (stdio), `mcp__tavily-mcp__*`** (Category A). Full-page web search with content extraction, plus extract, crawl, map, and research endpoints. `TAVILY_API_KEY` in env. Installed 2026-05-26 as the sub-agent-compatible replacement for OAuth `claude_ai_Tavily`. Sub-agent inheritance verified the same session (Phase C: three live results returned for a Liverpool jersey query dispatched from SCRIBE).
- **Playwright MCP, `mcp__plugin_playwright_playwright__*`** (Category A in practice; the plugin runs locally and does not depend on claude.ai OAuth). Headless browser automation for live SERP inspection, SPA-rendered content extraction, post-deployment visual validation, and screenshot capture. Read-only posture for all workforce use.
- **GSC MCP, `mcp__gsc-server__*`** (Category A). Google Search Console analytics for the owned property, registered as the domain property `sc-domain:prosoccer.com` (this exact `siteUrl` is required on every call). Auth is a Google service account (`prosoccer-gsc-reader@prosoccer-seo-workforce`, `siteFullUser` read access) whose JSON key is referenced by `GOOGLE_APPLICATION_CREDENTIALS` in env and lives OUTSIDE the repo (`C:\Dev-Projects\.credentials\`), never committed. **Package identity (corrected 2026-06-09):** `npx -y mcp-server-gsc` resolves on the npm registry to `gsc-mcp-server-enhanced` v0.2.0, a fork of `ahonn/mcp-server-gsc` that ships extra tools. Commit 62bbdba documented the package as plain ahonn and listed tool names that don't exist on the installed build; the names below are the real ones, confirmed by a live `tools/list` against the running server. **Tools:** `list_sites` (lists accessible properties; this is the call that returns `sc-domain:prosoccer.com`), `search_analytics` (query performance, with page-level lookups via the `pageFilter` argument plus `dimensions`, since there's no separate by-page tool), `enhanced_search_analytics` (up to 25,000 rows, regex query filters), `detect_quick_wins` (striking-distance detection; default positions 4 to 10 with CTR at or below 2% and at least 50 impressions, parameterizable to positions 11 to 20 for the page-2-to-page-1 push; central to Commit 4's volume-weighted primary keyword selection), `index_inspect` (URL indexation state), and the sitemap tools `list_sitemaps`, `get_sitemap`, `submit_sitemap`. There is no `list_properties`, `get_search_analytics`, or `get_search_by_page_query` despite the original install note. **npx cache troubleshooting (2026-06-09):** the stdio server first failed to connect because the npx package cache was incomplete (`ajv-formats` present but its `ajv` dependency missing, so startup crashed with `Cannot find module 'ajv'` before reaching auth). Fixed by deleting the package's `_npx` cache dir and re-fetching. That's an environment fix, not a repo change. If the server shows "Failed to connect" again, clear the npx cache and re-run before suspecting auth. Installed 2026-06-09, closing the pre-staged drift (the `gsc-server` prefix was already present in `settings.local.json` and in ORIN/SCRIBE/KIRA/VERITAS frontmatter before the server existed). **Verification (2026-06-09):** after the cache fix, a direct subprocess test returned the `sc-domain:prosoccer.com` property with `siteFullUser` permission from `list_sites`, proving credential and property access end to end. MCP-load and sub-agent inheritance (Category A's distinguishing test) were then verified the same day via Phase C (commit f3b179a): a parent-level `list_sites` from ORIN and a `list_sites` from a dispatched SCRIBE sub-agent both returned `sc-domain:prosoccer.com`, proving the env credential inherits to sub-agents with no parent-fetch workaround. **Distinction from Drive MCP:** Drive is Category B (parent-only OAuth); GSC is Category A, so sub-agents (SCRIBE, KIRA, VERITAS) inherit the env credential and call GSC directly, with no parent-fetches-and-passes workaround. **Workflow status:** Phase 1 keyword-research integration LANDED 2026-06-09 (Commit 4, 'Volume-Weighted Primary Keyword Selection Discipline' above). KIRA reads `search_analytics` per URL and runs `detect_quick_wins` in Phase 1; GSC `search_analytics` is now the source of record for ProSoccer's own ranking baseline, while DataForSEO SERP stays useful for competitor-context lookups.
- **Google Drive MCP, `mcp__claude_ai_Google_Drive__*`** (Category B). Reads from the January 2026 audit folder (`1KF1213I-_nf9B04ASKoM_mcv5xydJ3h8`) and other shared Drive artifacts. Free at API level; cost is context-budget consumption. Sub-agents see the declaration in their `mcpServers:` blocks but cannot complete OAuth from the sub-agent context. Parent ORIN fetches Drive content and passes it inline to specialists via task context. Direct sub-agent calls fail; surface the discrepancy in the session briefing if encountered.
- **Tavily MCP (OAuth via claude.ai), `mcp__claude_ai_Tavily__*`** (Category B). Registered at the top-level session for ORIN's parent-only research work. Sub-agents use Category A `tavily-mcp` instead; this OAuth surface is not listed in any sub-agent `mcpServers:` block. Retained at parent session level only.
- **Local file system.** All `data/`, `context/`, `deliverables/`, `strategy/`, `shared-intelligence/`, `work-log/`, and `.claude/agents/<agent>/` paths. Plus the prosoccer theme repo for read-only template inspection (SCRIBE, VERITAS).
- **`scripts/voice_check.py`.** Hard gate on every customer-facing copy proposal and every markdown deliverable. Per the 'Voice check discipline' section below, run on every modified file regardless of change type.

### Install pending (none currently; GSC was the last, installed 2026-06-09)

All referenced MCP servers are now Operational above. GSC MCP, the last pending server, was installed 2026-06-09 (Category A, see Operational), and its Phase 1 keyword-research integration LANDED the same day (Commit 4, 'Volume-Weighted Primary Keyword Selection Discipline' above). The two methods below now read GSC directly where they previously leaned on CSV exports:

- **Ranking context per page (primary keyword position lookup):** GSC `search_analytics` per URL (via `pageFilter`) is now the ranking source of record for ProSoccer's own pages, set by Commit 4. DataForSEO SERP API via `mcp__dfs-mcp__serp_organic_live_advanced` remains useful for competitor-context lookups and SERP-feature checks, but not for ProSoccer's own ranking baseline.
- **CTR ceiling diagnostics, query-by-page intersection, indexation state, Rich Results coverage:** GSC `search_analytics` (page and query dimensions, with `pageFilter` for query-by-page intersection) plus `index_inspect` (indexation state) are now callable for these; the coarse CSV exports under `data/gsc-exports/` (12-month `_top-pages.csv`, `_top-queries.csv`, `_search-appearance.csv`) remain a usable offline baseline. Mike refreshes the exports on cadence (target: monthly).

### Implicit-fallback drift (the failure mode this inventory prevents)

Before this inventory existed, agent narratives referenced `mcp__firecrawl-mcp__firecrawl_scrape`, `mcp__gsc-server__get_search_analytics`, and `mcp__claude_ai_Tavily__tavily_search` as if those tools were live. Sessions that depended on those calls silently degraded to whichever tool happened to work, or stalled, or produced briefs that cited tools the workforce couldn't actually run. This implicit fallback hid the install gap from Mike and produced misleading "tool used" lines in session briefings.

The pre-flight tool verification protocol in SCRIBE Section 2 Step 0 (canonical pattern, other agents adopt as added) makes the tool inventory explicit at the start of every session. If an agent intends to use a tool listed under "Install pending" above, the session briefing must log the actual fallback used, not just the intended MCP namespace.

### Sub-agent MCP access matrix

Each workforce agent has explicit MCP server access declared in its `agent.md` frontmatter `mcpServers:` block (per the Option B configuration pattern documented in 'Sub-agent configuration discipline' below). Least-privilege scoping: each agent gets only the MCP servers its core function requires.

The category column reflects the Category A vs Category B distinction documented above. Category A servers grant direct sub-agent MCP access. Category B servers grant declaration-only access; data must be fetched at the parent ORIN level and passed via task context. A cell value of "yes" for a Category B server means the declaration is present in the agent's `mcpServers:` block, not that the sub-agent can complete an OAuth-authenticated call directly.

| Server | Category | master-strategist (ORIN) | on-page-seo (SCRIBE) | keyword-research (KIRA) | competitor-intel (RECON) | technical-seo (VERITAS) |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| dfs-mcp | A | yes | yes | yes | yes | yes |
| firecrawl-mcp | A | yes | yes | no | yes | yes |
| tavily-mcp | A | yes | yes | yes | no | no |
| plugin_playwright_playwright | A | yes | no | no | yes | no |
| gsc-server | A | yes | yes | yes | no | yes |
| claude_ai_Google_Drive | B | yes | yes | yes | yes | yes |
| claude_ai_Tavily | B | parent-only | no | no | no | no |

Rationale per agent (Category A access governs direct callability; Category B access governs the parent-mediated workaround surface):

- **ORIN gets the full set.** Orchestrator role requires the ability to run any specialist's work at the parent level when needed (e.g., the parent-handles-MCP workaround pattern for Category B servers). ORIN holds the only `claude_ai_Tavily` surface in the workforce.
- **SCRIBE has DFS + Firecrawl + tavily-mcp + GSC (Category A) + Drive (Category B).** Native Category A access to DFS, Firecrawl, and tavily-mcp covers keyword spot-validation, current-state PDP/collection extraction, and topic research with full-page content. No Playwright (Playwright is RECON's tool for competitor mobile-vs-desktop validation; SCRIBE doesn't need browser automation for copy production).
- **KIRA has DFS + tavily-mcp + GSC (Category A) + Drive (Category B).** Keyword research is the core function; native Category A access to DFS and tavily-mcp covers SERP analysis, keyword discovery, and topic research. No Firecrawl (page scraping is SCRIBE/VERITAS work) or Playwright (browser automation is RECON's lane).
- **RECON has DFS + Firecrawl + Playwright + Drive (Category B).** Competitor monitoring needs SERP analysis (DFS), competitor page extraction (Firecrawl), and mobile-vs-desktop SERP rendering checks (Playwright). No tavily-mcp (Tavily is internal topic research, parent ORIN holds the OAuth Tavily for that work) and no GSC (GSC is own-site monitoring, not competitor monitoring).
- **VERITAS has DFS + Firecrawl + GSC (Category A) + Drive (Category B).** Technical SEO needs SERP-position validation (DFS), site crawling (Firecrawl), and coverage diagnostics (GSC). No Playwright (covered by Section 8 handoffs to RECON when mobile-rendering checks are needed) and no tavily-mcp.

When a new specialist is built (SAGE Content Writer, METRIK Reporting), add a column to this matrix as part of the agent.md commit and update each agent's `mcpServers:` block to match.

### Update protocol

When an MCP install completes or auth lands:

1. Move the entry from "Install pending" to "Operational" with the verification date and the verification call used.
2. Update affected agent narrative sections to remove the install-pending caveats (the inventory references can stay implicit once the MCP is live).
3. Commit message format: `MCP install: <namespace> live. Tool inventory in workforce-conventions.md updated; agent narratives reference the MCP directly without fallback caveats.`

## Sub-agent configuration discipline

This section codifies the canonical configuration pattern for workforce sub-agents (the `agent.md` frontmatter that determines what tools and MCP servers each sub-agent can actually call). Verified against Claude Code documentation at `code.claude.com/docs/en/subagents` on 2026-05-26.

### Frontmatter pattern (Option B, canonical)

Two independent frontmatter fields govern tool availability:

- **`tools:`** is the allowlist for built-in Claude Code tools (Read, Write, Edit, Glob, Grep, Bash, etc.). If `tools:` is set as an allowlist, only those tools are callable; the sub-agent CANNOT use any MCP tools unless `mcpServers:` is also set. If `tools:` is omitted entirely, the sub-agent inherits every tool from the parent.
- **`mcpServers:`** is the allowlist for MCP servers. Each entry is either a bare server-name reference (e.g., `- dfs-mcp`) to a server configured in the parent session, or an inline server definition keyed by name. This field is the ONLY documented mechanism for scoping MCP access to a sub-agent.

The canonical pattern for ProSoccer workforce agents:

```yaml
---
name: <agent-name>
description: <agent description>
tools: Read, Write, Edit, Glob, Grep, Bash
mcpServers:
  - <server-1>
  - <server-2>
  - <server-N>
---
```

`tools:` carries only built-in capabilities. `mcpServers:` carries the per-agent MCP scope. Both fields are independent allowlists.

### Failure mode this pattern fixes

Before 2026-05-26, agent frontmatter declared MCP servers using invalid syntax in the `tools:` field (e.g., `tools: Read, Write, ..., mcp__dfs-mcp, mcp__firecrawl-mcp, ...`). Per Claude Code documentation (subagents page, line 315): "This example uses `tools` to exclusively allow Read, Grep, Glob, and Bash. The subagent can't edit files, write files, or use any MCP tools." Bare MCP names in the `tools:` field are not valid tool references; they're neither tool names (which follow `mcp__<server>__<tool>` format) nor server references (which belong in the separate `mcpServers:` field).

The visible symptom: sub-agents dispatched via the Agent tool reported their callable tools as `Read, Write, Edit, Glob, Grep, Bash` only, with no MCP tools exposed, despite frontmatter declarations to the contrary. The parent-handles-MCP workaround pattern (ORIN runs MCP calls, hands data to the sub-agent) was a band-aid; this configuration fix is the architectural correction.

### Least-privilege scoping principle

Each agent declares ONLY the MCP servers its core function requires. Master-strategist (ORIN) gets the full set because it orchestrates; specialists get only what they need to do their job. See the 'Sub-agent MCP access matrix' above for the canonical per-agent allocation. When adding a new MCP to the workforce (e.g., a future Ahrefs MCP), update the matrix and each agent's `mcpServers:` block to either include the server or explicitly omit it with a rationale logged here.

### Restart-required behavior

Per Claude Code documentation (subagents page, line 242): "Subagents are loaded at session start. If you add or edit a subagent file directly on disk, restart your session to load it." Editing any `agent.md` frontmatter (or the body) requires a Claude Code restart before the changes take effect in dispatched sub-agents. This is structural to Claude Code; it is not configurable.

Practical implication: when restructuring agent.md files for an architectural change like the Option B fix, the workflow is (1) commit the edits, (2) restart Claude Code, (3) verify the new configuration in dispatched sub-agents, (4) only then proceed with workflows that depend on the fix.

### Step 0 verification at sub-agent dispatch

The SCRIBE Section 2 Step 0 pre-flight tool verification protocol (canonical pattern, other agents adopt as added) verifies the `mcpServers:` block matches the expected per-agent access, with category-aware behavior. The protocol distinguishes Category A (direct health check) from Category B (parent-context verification).

**Category A verification (direct health check):**

1. On dispatch, the sub-agent confirms which Category A MCP server names appear callable in its tool schema (tools prefixed `mcp__<server-name>__*` exist for every Category A server in the `mcpServers:` block).
2. The sub-agent runs a no-cost health check call per Category A server it intends to use this session. Suggested test queries (cheap or free, used only to confirm subprocess connection and authentication):
   - `dfs-mcp`: `mcp__dfs-mcp__serp_locations` (returns location list; no per-call cost). Expected: status_code 20000.
   - `firecrawl-mcp`: a `mcp__firecrawl-mcp__firecrawl_scrape` on a known-stable URL (e.g., the target page if the session is going to scrape it anyway, so the health check doubles as the first real call). Expected: status_code 200.
   - `tavily-mcp`: a `mcp__tavily-mcp__tavily_search` with a low-volume query relevant to the session. Expected: top results returned.
3. If a Category A server listed in `mcpServers:` is not callable (tools missing from schema, or call returns an authentication error), the sub-agent logs the discrepancy in its session briefing and surfaces to ORIN or Mike before proceeding.

**Category B verification (parent-context check):**

1. On dispatch, the sub-agent recognizes that Category B servers (`claude_ai_Google_Drive`, `claude_ai_Tavily`) appear in the `mcpServers:` block as declarations but require parent-mediated data flow.
2. The sub-agent verifies the parent task context contains the Category B data it needs for the session (e.g., Drive file contents already fetched and passed by ORIN). If the data is present in the task context, proceed.
3. If a Category B fetch is needed and the data is not in the task context, the sub-agent does NOT attempt the direct MCP call. The sub-agent surfaces to ORIN: "need <specific Drive file or Tavily query> for <reason>; please fetch and pass via task context."
4. Direct Category B MCP calls attempted from sub-agent context will return OAuth-authentication errors; logging this is fine for diagnostic purposes but the sub-agent should not retry or interpret the failure as a system fault. It is a known architectural constraint.

**Drift detection (both categories):**

1. If a server NOT in the agent's `mcpServers:` block appears callable, log the over-permission as a config drift to be reconciled in the next agent.md commit.
2. If the categorization of a server appears to have changed (e.g., a Category B server starts returning successful direct calls from sub-agent context), surface immediately: this may indicate a Claude Code release shipped OAuth-token inheritance, which would collapse the category distinction.

This catches both under-permission (configuration didn't take effect, restart was skipped, server name typo, OAuth state missing) and over-permission (sub-agent inherited more than scoped) before they corrupt deliverable audit trails.

### Eligibility verification (Mike-pre-vetted at URL submission, updated 2026-05-29)

**Architectural pivot 2026-05-29.** Eligibility responsibility shifted from agent-detected (Firecrawl scrape) to Mike-pre-vetted (Shopify admin) after diagnostic on the Mexico Stadium SS kit set confirmed storefront-rendered signals are systematically unreliable.

**Architectural learning documented (2026-05-29 diagnostic findings):**

- Three different schema.org Offer.availability value formats across three pages of the same Hyper theme on prosoccer.com: bare string `InStock` on Home, full URL `http://schema.org/InStock` on Away, and human-readable `Out of stock` on Third. No internal consistency; format varies per page.
- Dual-schema injection confirmed on Mexico Away (`schema_offers_count: 2`): two competing Offer entries in JSON-LD, presumably one from Shopify core and one from an app (Rebuy, Klaviyo back-in-stock, pre-order/low-stock apps are likely candidates).
- Persistent variant selector "lies" on Home and Third: variant selector shows all sizes sold-out and Add-to-cart button disabled, while schema says InStock and the inventory hint shows real units available (31 on Home, 4 on Third). This is not transient cache; it reproduced today on fresh scrape (maxAge=0).
- The `Available in stock (X)` inventory hint was the only reliable signal across all three pages, accurately matching Mike's Shopify admin observation of stable inventory. This signal had been dismissed on 2026-05-28 as a JSON-extraction artifact because schema + button + variants all contradicted it.
- Mexico kit set application of the pre-tournament demand spike strategic exception (2026-05-28) was triggered by the false-positive triple-signal and baked false reasoning into all three brief deliverables. Fix-forward commit strips that strategic context while preserving substantive optimization content.

**Conclusion: storefront-rendered signals cannot be trusted for eligibility decisions.** Refining detection rules against an architecturally unreliable rendering layer (apps injecting competing schema, theme bugs in variant selector, format inconsistency across pages) is a losing game. Admin remains the source of truth. Human-in-the-loop at URL submission is the most reliable bridge between admin truth and agent workflow.

**Pre-flight pattern, updated:**

1. Step 0: tool exposure check (unchanged; verifies MCP servers callable this session).
2. Step 0.5: eligibility audit-trail step (NEW responsibility): URLs are assumed eligible because Mike pre-vetted in admin before submission; SCRIBE captures the eligibility status verbatim in the brief's strategic context section, including any Mike-flagged strategic exception with reasoning. Agents skip Firecrawl-based detection.
3. Workflow begins (Steps 1 through 11 in SCRIBE's startup protocol; delegation sequence in ORIN's Section 9).

**Strategic exceptions preserved as concepts:** closing-window optimization (sold-out end-of-life / closeout / discontinued-generation pages with retained collector value, no restock expected) and pre-tournament demand spike optimization (sold-out current-cycle pages with imminent tournament and expected restock) remain valid as architectural concepts. Both are now triggered by explicit Mike flag at URL submission, not by agent auto-detection. Codified in `context/page-type-playbooks/product-page-playbook.md` 'Strategic exception' subsections; for collections, seasonal-empty exception preserved similarly.

**Documented exception examples preserved:** Liverpool 2024-25 Nike Away Jersey v2 (commit b7159dc, closing-window) and adidas Predator Accuracy.1 FG Crazyrush Pack v2 (commit d52e56f, closing-window). These were appropriately optimized under closing-window framing per the pages' real end-of-life status and remain canonical examples.

Cross-references:

- `context/page-type-playbooks/product-page-playbook.md` 'Eligibility verification (Mike-pre-vetted at URL submission)' (canonical PDP version)
- `context/page-type-playbooks/collection-page-playbook.md` 'Eligibility verification (Mike-pre-vetted at URL submission)' (collection version)
- `.claude/agents/on-page-seo/agent.md` Section 2 Step 0.5 (audit-trail capture)
- `.claude/agents/master-strategist/agent.md` Section 9 'Candidate eligibility verification at Phase 1 surfacing' (ORIN candidate-handling)

### Eligibility verification as logical extension of Step 0 (added 2026-05-27, superseded 2026-05-29)

Step 0 (tool exposure verification) and eligibility verification (target-page status verification) are two pre-flight gates that share the same architectural pattern: confirm operational preconditions before substantive work begins.

Pre-flight pattern, in order:

1. Step 0: tool exposure check. Can the workforce actually run the MCP calls this session depends on?
2. Step 0.5: eligibility verification. Is the target page worth the optimization effort (in stock, visible, populated, not redirecting)?
3. Workflow begins (Steps 1 through 11 in SCRIBE's startup protocol; delegation sequence in ORIN's Section 9).

Eligibility detection method, default blocker behavior, and strategic exception path are codified in the page-type playbooks. SCRIBE applies the playbook eligibility section as Step 0.5 in `.claude/agents/on-page-seo/agent.md` Section 2. ORIN applies eligibility at the Phase 1 candidate-selection surfacing step in `.claude/agents/master-strategist/agent.md` Section 9.

Strategic exception types codified across the page-type playbooks (expanded 2026-05-28 to two PDP exception types after the Mexico kit set Day 1 production-reality check surfaced a structurally different sold-out pattern):

- **Closing-window optimization** (PDPs). End-of-life, closeout, or discontinued-generation inventory with retained collector or completist value. Restock not expected. Documented examples: Liverpool 2024-25 Nike Away Jersey v2 (commit b7159dc) and adidas Predator Accuracy.1 FG Crazyrush Pack v2 (commit d52e56f), both 2026-05-26 production predating the codification.
- **Pre-tournament demand spike optimization** (PDPs). Current-cycle inventory sold out with imminent tournament or seasonal demand event (typically 60 days or less) and expected restock during or after the event window. SEO equity lead time matters; the page must include strong internal linking to the relevant collection so customers landing on a sold-out PDP can navigate to in-stock alternates. Documented example: Mexico 2026 kit set Stadium SS Home/Away/Third (2026-05-28 codification), 2026 World Cup co-host kickoff June 11, about 14 days out, first documented pre-tournament demand spike override.
- **Seasonal empty collections**. Collection page intentionally empty ahead of product drop or between cycles.

All overrides require explicit Mike approval with the exception type named and strategic reasoning documented in the session briefing or brief production decision. New optimizations going forward default to eligible candidates. Decision-logic summary for choosing between closing-window vs pre-tournament demand spike vs default blocker lives in `context/page-type-playbooks/product-page-playbook.md` 'Decision logic for strategic exceptions'.

Cross-references:

- `context/page-type-playbooks/product-page-playbook.md` 'Eligibility verification (mandatory pre-Phase-1)'
- `context/page-type-playbooks/collection-page-playbook.md` 'Eligibility verification (mandatory pre-Phase-1)'
- `.claude/agents/on-page-seo/agent.md` Section 2 Step 0.5
- `.claude/agents/master-strategist/agent.md` Section 9 'Candidate eligibility verification at Phase 1 surfacing'

### Batch parallel dispatch + single daily batch commit (cross-cutting pattern, added 2026-05-29)

Production workflow runs as batch parallel dispatch with single daily batch commit per Mike's 2026-05-29 operational decision. Mike submits up to a 10-URL batch (eligibility pre-vetted in Shopify admin per the `Eligibility verification (Mike-pre-vetted at URL submission)` pattern). ORIN auto-classifies tier per URL (Tier 1 / 2A / 2B) and dispatches SCRIBE in parallel for all URLs concurrent via simultaneous Agent tool calls in a single message. Each SCRIBE instance runs the full per-tier discipline (research depth, brief drafting depth, field count) with all quality gates intact. After all briefs return, ORIN runs trust-but-verify per brief (read visible brief, independent voice check on both files, confirm gates pass) and then batch-commits all visible briefs + all workforce briefings + any follow-up files as a single atomic LOCAL commit with comprehensive batch message. The push waits for Mike's go after he reviews the end-of-batch report (v2, 2026-07-10; see 'Escalate-on-exception approval mode (v2)'): the commit is autonomous, the push is not.

**Speed target.** 10-URL mixed-tier batch completes in ~25-45 min wall clock vs ~3-4 hours sequential. The slowest individual brief in the batch sets the wall-clock floor; Firecrawl / DataForSEO / Tavily infrastructure response times are the secondary constraint.

**Quality discipline preserved per brief.** Voice check, 11 self-verification gates plus Gate 12 keyword distribution plus Gate 13 anti-stuffing, year-specificity keyword discipline, brand IP compliance, currency check, sensitivity check, fact verification, internal link validation, per-brief workforce briefing audit trail. None of these flex under batch dispatch.

**Operational gates removed (safety gates preserved).** Per-brief Mike gate review replaced by end-of-batch review. Per-brief commit + push cycle replaced by a single local batch commit with the push held for Mike's go after the end-of-batch report (v2, 2026-07-10; the commit is autonomous, the push is not). Tier classification Mike confirmation replaced by ORIN auto-classification with post-batch Mike review of the classifications applied.

**End-of-batch summary.** ORIN surfaces to Mike: brief file paths, tier classifications applied, any quality issues flagged for Mike attention, cost tracking summary, any architectural learnings surfaced through the batch.

Cross-references: `.claude/agents/master-strategist/agent.md` Section 9 'Batch parallel dispatch and single daily batch commit' (ORIN procedural workflow); `.claude/agents/on-page-seo/agent.md` Section 9 'Tiered workflow variants' (per-tier scope SCRIBE applies regardless of dispatch pattern); `context/page-type-playbooks/product-page-playbook.md` 'Tiered workflow architecture for PDP optimization' + `context/page-type-playbooks/collection-page-playbook.md` 'Tier 2B canonical workflow' (per-page-type production workflow now runs under batch parallel dispatch as the production pattern).

### Parallel dispatch sizing (one SKU per agent + exemplar anchor) (added 2026-06-04)

The fb16909 batch parallel dispatch pattern (above) is refined by a Day 3 PDP batch production lesson (10 Nike SU26 Breakout Pack SKUs, commit 088ae19): per-silo dispatch (2 to 4 briefs per agent) overloaded SCRIBE and only 1 of 10 finished round one. Standing dispatch shape for PDP batches: (1) one SCRIBE agent per SKU, not per silo or per tier; (2) free-form markdown brief output, NOT a structured-output schema (the schema made agents finish without emitting output), and ORIN verifies from the written files; (3) gold-standard exemplar anchor: ORIN has SCRIBE produce and validate one representative brief first, then the remaining SKUs mirror its structure, voice, and outcome-based quality; (4) re-dispatch protocol for transient server-side rate limiting (not usage-based): ORIN re-dispatches failed SKUs as a fresh dispatch (a cached resume returns the cached failures), and briefs already written are not re-run. Production source: Day 3 batch commit 088ae19. Cross-references: `.claude/agents/master-strategist/agent.md` Section 9 'Parallel dispatch sizing'; `.claude/agents/on-page-seo/agent.md` Section 9 (SCRIBE free-form Phase 4 output).

**Clarification (added 2026-06-08): "mirror the exemplar" means STRUCTURAL mirroring only, never prose mirroring.** The Day 3 batch (commit 088ae19) shipped with 70 to 80% prose duplication across pack siblings because the exemplar-anchor instruction was read too literally: SCRIBE mirrored the exemplar's language, not just its shape. Four Phantom 6 SKUs shared identical opening hooks, identical closing lines, identical H2 titles, identical metaphor structures, and near-identical FAQ questions and answers. That outcome is forbidden. Mirror the exemplar's STRUCTURE: same H2 count, same H2 order categories (overview, use case, fit, Product Details), same Product Details bullet structure, same FAQ count, same field-length tiers. Do NOT mirror the exemplar's PROSE: each SKU carries its own opening hook, its own H2 titles (topically related but not identical), its own metaphors and scene framings, and its own FAQ questions and answers (questions may overlap topically across siblings, but every answer is uniquely written). This is a refinement of the exemplar-anchor pattern, not a reversal: the exemplar still proves the structure and anchors batch consistency; it does not license shared language. The three disciplines below operationalize this clarification. Production source: Day 3 batch commit 088ae19 review.

**Exemplar handoff: structure skeleton (primary) plus forbidden phrasings (backstop) (added 2026-06-08).** The Day 3 re-run (commit 957dc3c) showed that the clarification above was necessary but not sufficient: handing siblings the exemplar's FULL PROSE to convey structure also propagates its scaffolding. A verbatim firm-ground definition sentence landed in all 5 FG briefs and the "The Cleat for..." H2 frame in 4, despite the structure-not-prose instruction, because SCRIBE cannot cleanly separate structure from phrasing when reading full prose. ORIN's defense-in-depth caught and corrected both at the gate, and the handoff is now refined into two complementary mechanisms:

- **Mechanism A (primary): structure skeleton only.** After the exemplar SCRIBE produces and ORIN validates the gold-standard brief, ORIN extracts a STRUCTURE SKELETON: H2 category labels (overview / identity-hook, heritage / positioning, use-case, Product Details bullets, fit / sizing), field-length targets (Short Description words, Description words, FAQ count), and the Product Details bullet categories (materials, plate, tier features, weight, care). The skeleton carries NO actual H2 titles, NO prose, NO definitional sentences, NO metaphors. Siblings receive the skeleton, not the exemplar brief, which removes the propagation pathway architecturally.
- **Mechanism B (backstop): forbidden-phrasings list.** ORIN also extracts the exemplar's CLAIMED PHRASINGS (its H2 titles, its definitional sentences for recurring concepts such as the FG / AG / tier / plate definitions, its primary metaphor, its opening hook, its closing line) and adds them to each sibling's lane spec as a forbidden list to write around. The backstop catches propagation that survives skeleton-only handoff, for example when SCRIBE's own silo familiarity gravitates to a similar phrasing independently.

The exemplar still anchors ORIN's quality bar (ORIN reads the full validated exemplar); the skeleton and forbidden list are the OPERATIONAL handoff to siblings. Applies only to pack/series batches. Refines the exemplar anchor (commit 13b0a1a) and the cross-brief prose uniqueness clarification above (commit ae42964). ORIN procedure: `.claude/agents/master-strategist/agent.md` Section 9 'Pre-dispatch differentiation pass for pack/series batches'; SCRIBE side: `.claude/agents/on-page-seo/agent.md` Section 9. Production source: Day 3 re-run gate review, commit 957dc3c.

**Refinement (added 2026-07-08, Batch 6 Shadow-pack gate review).** Batch 6 ran four Shadow-pack cleats (one exemplar plus three mirrors) sharing a deliberate thematic register (playing unseen / blind side per the Registry 2 anti-convergence lane). The skeleton-plus-forbidden-list handoff still let near-identical prose re-emerge: a "gone" payoff word recurred across all four openers, and a mirror reused the exemplar's H2 title FRAME ("The [noun] [nobody] sees coming" -> "The first step nobody sees coming"). ORIN caught and corrected both at gate. Root cause: Mechanism B carried the exemplar's verbatim strings but not its underlying patterns, so independent SCRIBEs re-derived them. Two refinements, forward-applicable to every family-exemplar handoff where siblings share a thematic register:

- **Mechanism B scope expansion.** The forbidden-phrasings list now carries three tiers, not one: (1) verbatim strings (existing: H2 titles, definitional sentences, primary metaphor, opening hook, closing line); (2) recurring MOTIFS extracted from the exemplar (payoff words, register words, thematic nouns, for example the "gone" payoff or a repeated "disguise" noun) that siblings must not all land on; (3) H2 title FRAMES (the structural template of the exemplar's H2 titles, for example "The [noun] [verb phrase] coming"), so a mirror cannot reuse the frame with a swapped noun. ORIN extracts all three tiers from the validated exemplar before dispatching the mirrors.
- **Mechanism A per-SKU tier-band.** The structure skeleton must state each sibling's OWN tier-band word target, not let the sibling inherit the exemplar's. Batch 6's Vapor 17 Pro Shadow (Pro tier, 340 to 390) inherited the High Elite exemplar's Elite band (400 to 450) and came back at ~446; ORIN trimmed it to 386 at gate. The skeleton names the sibling's tier and its band explicitly.

**Heading-level enforcement (added 2026-07-08).** Body_html content headings must render at the intended depth: editorial body H2s and structural H2s at `##`, FAQ questions at `###`. Batch 6's Vapor Shadow brief shipped its body headings at `####`/`#####` and passed voice_check (which is heading-level-agnostic for casing per commit 812b613); ORIN caught it at gate and promoted them. This check stays with the SCRIBE Phase 4 self-check and the ORIN gate, NOT `scripts/voice_check.py`: the script cannot safely distinguish a brief's own structural `##`/`###` labels from body_html content headings without false positives, the same reason the reverse H2-casing-drift detection stayed with the human-style gates rather than the script. SCRIBE verifies heading depth during Phase 4; ORIN re-checks at gate.

### Cross-brief prose uniqueness discipline (added 2026-06-08)

Every brief in a pack or series carries UNIQUE prose. Mirror structure across siblings, never language. This discipline exists for three concrete reasons: Google applies duplicate-content treatment to near-identical sibling pages (filters the duplicates from the index, picks one canonical, demotes the rest); shared prose makes sibling SKUs semantically indistinguishable and feeds keyword cannibalization; and a buyer comparing two siblings who reads the same paragraph twice loses trust in both pages.

Forbidden across any batch of pack/series siblings:

- identical opening hooks (the first sentence of the Short Description or the Description's lead H2)
- identical closing lines
- identical H2 titles repeated across multiple briefs
- identical opening fragments inside prose H2 sections
- identical metaphors or scene structures
- identical FAQ answers (FAQ questions may overlap topically; answers are uniquely written per SKU)

What sibling briefs SHARE by design: H2 count, H2 order categories, Product Details bullet structure, FAQ count, field-length tiers, voice, and the outcome-based editorial quality bar. Technical-bullet overlap is expected and acceptable (siblings genuinely share specs). The uniqueness bar applies to PROSE: hooks, narrative framings, metaphors, transitions, and FAQ answers.

Cross-references: 'Pack/series coordination discipline' (below, ORIN's pre-dispatch differentiation pass that supplies the per-SKU angles), 'Keyword cannibalization discipline' (below), and `context/page-type-playbooks/product-page-playbook.md` 'Unique prose for pack/series products'. Production source: Day 3 batch commit 088ae19 review.

### Pack/series coordination discipline (added 2026-06-08)

Before dispatching SCRIBE for a multi-SKU batch whose SKUs belong to the same pack or series, ORIN runs a PRE-DISPATCH DIFFERENTIATION PASS. ORIN reads all SKUs in the pack first, then drafts a differentiation spec that pre-assigns each SKU a distinct editorial lane, so the briefs come back unique by construction rather than being de-duplicated after the fact.

Per SKU, the differentiation spec assigns:

- a unique angle of emphasis (what this SKU's copy foregrounds)
- a unique opening-hook approach (the framing device the Short Description and lead H2 open on)
- a unique heritage or positioning angle
- a unique use-case scenario (the concrete buyer moment the prose paints)
- a unique primary metaphor or scene framing

SCRIBE produces from ORIN's per-SKU differentiation spec, NOT from the exemplar's prose. The exemplar supplies structure; the differentiation spec supplies each SKU's distinct editorial content. This pass is judgment-based, not script-enforceable: ORIN reads the SKUs, drafts the spec, then dispatches one SCRIBE agent per SKU with that SKU's lane named in the dispatch prompt.

Cross-references: `.claude/agents/master-strategist/agent.md` Section 9 'Pre-dispatch differentiation pass for pack/series batches'; `.claude/agents/on-page-seo/agent.md` Section 9 (SCRIBE produces from the differentiation lane). Production source: Day 3 batch commit 088ae19 review.

### Keyword cannibalization discipline (added 2026-06-08)

Pack/series siblings competing for the same query split their own ranking signal. Three rules keep siblings out of each other's way:

- **Primary keyword unique per SKU within the batch.** Already standing under the keyword-distribution discipline; restated here as the first line of cannibalization defense.
- **Supporting keyword varied within the pack where possible.** When siblings can carry distinct supporting terms, they should. Four Phantom 6 SKUs all targeting `nike phantom 6` as the supporting term is the cannibalization failure mode this rule prevents.
- **Shared supporting keyword requires distinct semantic territory.** When a supporting keyword is necessarily shared (a high-volume brand or silo term every sibling legitimately targets), the surrounding prose must establish a distinct semantic territory per SKU, so the pages read as covering different buyer intents rather than competing for the same one. The pack/series coordination differentiation pass (above) supplies that distinct territory.

Cross-references: 'Supporting keyword selection (cross-cutting)' (the standing one-supporting-keyword-per-body rule) and 'Pack/series coordination discipline' (above). Production source: Day 3 batch commit 088ae19 review.

### Dual Registry Architecture for Cross-Batch Coordination (added 2026-06-08)

The three disciplines above (cross-brief prose uniqueness, pack/series coordination, keyword cannibalization) stop duplication WITHIN a batch. Two registries extend that coordination ACROSS batches, both feeding ORIN's pre-dispatch differentiation pass. They have different owners, different update cadences, and different transport.

**Registry 1: white-label keyword sheet (external, source of truth; ORIN reads, white-label team writes).** A Google Sheet maintained by Mike's white-label team, the authoritative record of keyword status across all ProSoccer SEO work (not just workforce batches), at https://docs.google.com/spreadsheets/d/1H-4Ax8C6IbfqCx2SToVidD4p9GR_rn16PePuvGMSA6Q/edit. Two tabs:

- **Collections tab** columns: Page URL (completed metatags), Complete/In Progress, Meta Title, Meta Description, Long Description, Short Description, Primary KW, Mike H.
- **PDPs tab** columns: PDP SKUs, Page URL (completed metatags), Status, Primary KW, Date.

ORIN reads the sheet during the differentiation pass to check, per SKU, whether a primary keyword is already claimed for another URL (cross-batch cannibalization defense). After the batch commits, ORIN surfaces the primary keyword assigned to each new brief for entry in the Primary KW column; write ownership stays with the white-label team (see 'Division of ownership' below).

**Access pattern: parent-fetches-and-passes.** The sheet is reached through the claude.ai Google Drive connector, a Category B (OAuth-bearer) MCP. Per the documented OAuth-token inheritance gap ('Architectural notes' below), the OAuth token does not propagate to sub-agents, so SCRIBE instances cannot read Drive directly. ORIN (the parent) reads the sheet, parses it, filters to the silo-relevant and exact-URL-matching rows, and injects those rows into each SCRIBE dispatch context. SCRIBE never calls Drive.

**Division of ownership (ORIN reads, the white-label team writes; the handoff is permanent by design).** ORIN reads the sheet directly (read path validated 2026-06-08, structure and access confirmed). ORIN does NOT write to the sheet. The Registry 1 write-back is a MANUAL HANDOFF and that is the standing architecture, not a workaround awaiting tooling: the sheet is owned and maintained by Mike's white-label team (`ppcreporting@gmail.com`), and write ownership stays with them. ORIN surfaces the per-SKU primary keyword assignments in the end-of-batch summary; the white-label team enters them in the sheet. This keeps a single human-owned source of truth for keyword status and avoids two systems writing the same cells. (Mechanically, the claude.ai Drive connector also exposes no granular Sheets cell-update or row-append tool, only whole-file create / copy, so ORIN could not write cells even if asked; but the operational reason the handoff is permanent is ownership, not tooling.)

**Registry 2: silo-positioning files (internal, repo, append-only).** `context/silo-positioning/` holds one file per product silo (`phantom.md`, `mercurial.md`, `tiempo.md`, `copa.md`, `predator.md`, `f50.md`, others as silos see work). Each logs the prose patterns USED in shipped briefs per SKU: opening hook approach, primary metaphor, use-case scenario, angle of emphasis, heritage angle. Workforce-owned, version-controlled, append-only. ORIN reads the relevant silo file during the differentiation pass to avoid reusing a hook or metaphor that already shipped in a prior batch, and appends new entries after each batch commits. Full format and protocol: `context/silo-positioning/README.md`.

**Integration into the pre-dispatch differentiation pass (six steps):**

1. **ORIN reads Registry 1** via the parent-level Drive connector. For each SKU in the batch, find its row (PDPs tab for products, Collections tab for collections) and capture current status, any existing primary-keyword assignment, and date. If the sheet is large, filter to silo-relevant rows (Phantom, Mercurial, Tiempo, and so on) plus exact URL matches.
2. **ORIN reads Registry 2** (the relevant silo-positioning file). Identify each SKU's silo (Phantom 6 to `phantom.md`; Mercurial Superfly and Vapor to `mercurial.md`; Tiempo to `tiempo.md`; Copa to `copa.md`; and so on) and read the claimed hooks, metaphors, use-case scenarios, and angles from prior batches.
3. **ORIN drafts the per-SKU differentiation lane spec.** Unique angle of emphasis, opening-hook approach, heritage/positioning angle, use-case scenario, and primary metaphor, each distinct from both the current-batch siblings AND the prior-batch silo log. Plus a primary-keyword candidate cross-checked against the sheet (avoid keywords already claimed for other URLs), and a reference list of sibling SKUs and recent prior silo work this SKU must differentiate against.
4. **SCRIBE produces the brief from the lane spec.** Unique prose per the spec; mirrors the exemplar's STRUCTURE (per the ae42964 clarification), not its prose or any sibling's prose.
5. **ORIN defense-in-depth at gate.** Pairwise prose comparison across the batch; flag any pair exceeding ~40% prose similarity (per ae42964).
6. **After Mike approves and the batch commits, ORIN updates Registry 2 and hands off Registry 1.** Append per-SKU prose-pattern entries to the silo-positioning file(s) directly (workforce-owned). For the sheet, surface the assigned primary keyword per SKU in the end-of-batch summary for the white-label team to enter in the Primary KW column (manual handoff by design, see 'Division of ownership' above); flag any SKU lacking a PDPs-tab row as a new-row addition for the team.

Both registry writes happen AFTER the batch commits, never before: proposed keywords and patterns can change at gate review, so the registries record only shipped, validated assignments.

Cross-references: `.claude/agents/master-strategist/agent.md` Section 9 'Pre-dispatch differentiation pass for pack/series batches' (the read/write procedure); `context/silo-positioning/README.md` (Registry 2 format); 'Architectural notes' below (the OAuth-token inheritance gap that dictates parent-fetches-and-passes); 'Cross-brief prose uniqueness discipline', 'Pack/series coordination discipline', and 'Keyword cannibalization discipline' above (the disciplines these registries operationalize across batches). Production source: Day 3 batch commit 088ae19 (the cross-batch coordination need); intra-batch coordination commit ae42964.

### Tiered workflow architecture (cross-cutting pattern, added 2026-05-28)

Per-page brief production runs at one of four tiers depending on page type and strategic role. Tier is named at dispatch by ORIN (Section 9 'Tier classification at candidate dispatch'); SCRIBE adapts research depth, brief drafting depth, and field count accordingly (Section 9 'Tiered workflow variants'). Quality discipline preserved universally across all tiers.

Tier definitions:

| Tier | Page type | Time target | Scope | Proportion |
|---|---|---|---|---|
| Tier 1 | Foundational PDP (template-establishing, hero product, new category first) | ~25 to 35 min | Full SCRIBE workflow: broad Tavily, fresh brief build, all 11 gates | ~5 to 10% of PDPs |
| Tier 2A | Pattern-follow PDP (follows established CANONICAL template) | ~12 to 16 min | Scoped Tavily (currency only), template-fill drafting | ~70 to 80% of PDPs |
| Tier 2B | Collection page | ~15 to 20 min | Full workflow scoped to 6 collection-specific fields (Title, Slug, Meta Title, Meta Description, Short Description / hero block, body Description) | All collection pages |
| Tier 3 | Mike-drafted minimal | ~5 to 10 min | Mike drafts 4 to 6 fields; ORIN runs lightweight QA only | Rare exception |

Universal quality discipline (preserved across all tiers): voice check, 11 self-verification gates (including Gate 12 keyword distribution and Gate 13 anti-stuffing), brand IP compliance, year-specificity keyword discipline, eligibility verification (Step 0.5), keyword distribution discipline. What flexes per tier: research depth, brief drafting depth, field count.

Validation milestones for canonical templates:

- **National Team Jersey CANONICAL: four-time validated within the 2026 World Cup cycle.** Validation set: UAE 2026 Home Stadium Jersey v3 (foundational), Mexico 2026 Home Stadium SS (commit `e56a7d6`), Mexico 2026 Away Stadium SS (commit `85dd1f0`), Mexico 2026 Third Stadium SS (commit `f2c2c34`). Eligible for Tier 2A on subsequent NTJ work. Promoted 2026-05-28 in commit `44c2f2f`.
- **Club Jersey CANONICAL: Liverpool 2024-25 Nike Away Jersey v2 validation (commit `b7159dc`).** Eligible for Tier 2A on subsequent club jersey work.
- **Soccer Cleats VALIDATED v1: Predator Accuracy.1 FG Crazyrush Pack v2 validation (commit `d52e56f`).** Eligible for Tier 2A on subsequent older-cycle cleat work; pending one current-cycle flagship cleat validation for full CANONICAL promotion.
- **Tier 2B canonical reference: Mexico collection v5 (in production tonight as the first canonical Tier 2B brief under codified discipline; v4 at commit `f3cac86` is the pre-codification sketch that surfaced four template refinements).**

Cross-references:

- ORIN tier classification at dispatch: `.claude/agents/master-strategist/agent.md` Section 9.
- SCRIBE tiered workflow variants: `.claude/agents/on-page-seo/agent.md` Section 9.
- PDP-tier playbook detail (Tier 1, 2A, 3): `context/page-type-playbooks/product-page-playbook.md` 'Tiered workflow architecture for PDP optimization'.
- Collection-tier playbook detail (Tier 2B): `context/page-type-playbooks/collection-page-playbook.md` 'Tier 2B canonical workflow'.

### Plugin-provided MCP servers (caveat)

Per Claude Code documentation, plugin sub-agents (sub-agents loaded from a Claude Code plugin) do NOT support the `mcpServers:`, `hooks:`, or `permissionMode:` frontmatter fields. Our workforce agents live under `.claude/agents/` (project scope, not plugin scope), so this caveat does not apply to us. If a future workforce agent is ever loaded from a plugin, the `mcpServers:` block will be ignored and the agent will inherit the parent session's MCP scope by default; document the constraint in the agent's own agent.md.

## Architectural notes (MCP inheritance, OAuth gap, payload offload)

Three operational architectural facts emerged from the 2026-05-26 work installing Firecrawl + Tavily and verifying sub-agent inheritance. These are recorded here because they shape how the workforce configures and uses MCPs going forward; the underlying behaviors live in Claude Code itself and may shift in future releases.

### Refinement of commit 1ac5701 (partial discovery)

Commit 1ac5701 (2026-05-26 earlier in the day) established the Option B configuration pattern (`tools:` for built-in tools, `mcpServers:` for MCP servers) and verified DataForSEO inheritance at sub-agent dispatch. That commit framed the fix as architectural and complete. The subsequent install work surfaced that the Option B pattern is necessary but not sufficient: for OAuth-authenticated MCP servers (the claude.ai connector class), the `mcpServers:` declaration propagates to sub-agents but the OAuth token does not. The Category A vs Category B distinction codified above is the refinement that completes the picture. Commit 1ac5701 stands as the configuration-pattern fix; this commit refines the discovery with the transport-and-credentialing distinction that determines which servers can be called directly from sub-agent context.

The Liverpool (9eb344d) and Predator (bd309aa) briefs cited in commit 1ac5701 as Phase 6 validation remain valid under the refined model: those briefs were produced with the parent-handles-MCP workaround for the OAuth-class servers, which is exactly the workaround pattern the Category B classification documents. The briefs are not invalidated by the refinement; the architecture documentation just now captures why the workaround was necessary.

### OAuth-token inheritance gap

The mechanism: claude.ai connector MCPs (HTTP transport, OAuth-bearer authentication) maintain their access tokens in the top-level Claude Code session's OAuth state, not in environment variables. When the parent dispatches a sub-agent via the Agent tool, the sub-agent inherits the `mcpServers:` declaration but the OAuth state is not propagated to the sub-agent's MCP client. Direct sub-agent calls to `mcp__claude_ai_*__*` tools return authentication errors.

The architectural implication: until Claude Code ships OAuth-token propagation for sub-agents, any MCP server that depends on the claude.ai connector flow is structurally parent-only. The workaround (parent fetches, passes via task context) is operationally workable but adds a serialization step to multi-agent flows. When evaluating new MCPs for workforce integration, prefer Category A (stdio + env-credential) installations over Category B (OAuth via claude.ai connector) where both options exist for the same underlying service. The Tavily example is instructive: the OAuth `claude_ai_Tavily` worked at top-level but blocked sub-agent dispatch; the stdio `tavily-mcp` (with API key in env) works at every level.

If Claude Code ships OAuth-token inheritance for sub-agents in a future release, the category distinction collapses and both classes become operationally equivalent. The Step 0 drift-detection step is the workforce's early-warning signal for this change.

### Large-payload offload pattern

Observed in the RECON Phase C test (2026-05-26): a `mcp__firecrawl-mcp__firecrawl_scrape` on the adidas Predator collection page returned a ~98,643-character markdown payload. The Claude Code harness wrote the payload to a tool-results file on disk (path: `<projects-dir>/<session-id>/tool-results/mcp-firecrawl-mcp-firecrawl_scrape-<timestamp>.txt`) rather than inlining the full content into the tool response visible to the sub-agent. The sub-agent received a truncated inline preview plus the file path for follow-up reading.

This is a Claude Code guardrail, not a Firecrawl error. The mechanism is silent (no warning surfaces in the tool result envelope; the agent must notice the response is partial and read the offload file to get the rest). Operational implication for the workforce: large-payload MCP calls (full-site crawls, collection-page scrapes with many product links, bulk DataForSEO endpoints) may land partially inline and partially on disk. Agents should:

1. Treat any unexpectedly short MCP tool response as a candidate for offload-file follow-up; check the tool-results directory for the timestamped file matching the call.
2. When a call is expected to return a large payload (collection page with 100+ products, bulk DFS endpoint, full-site Firecrawl crawl), plan to read the offload file rather than relying on the inline response.
3. Log the offload behavior in the session briefing when it occurs; it is a workflow detail that affects audit-trail reproducibility.

The offload threshold is set by the Claude Code harness and not configurable from agent context. The behavior may change in future Claude Code releases; if the threshold shifts or the mechanism changes, surface in the session briefing for forward documentation.

## Voice check discipline (defense-in-depth)

Run `scripts/voice_check.py` on every modified file regardless of what changed. The voice check tooling is fast; there's no operational reason to skip it on a per-edit basis. Defense-in-depth applies even to YAML frontmatter, configuration files, metadata edits, and internal context docs that aren't customer-facing prose.

The rationale: voice violations enter the codebase through editorial drift (an em-dash slipping into a config comment, an AI cliche phrase landing in a metadata description) just as easily as they enter through brief copy. Running the check universally costs nothing and catches incremental drift before it compounds. The discipline removes the judgment call ("is this file customer-facing enough to warrant checking?") that creates inconsistent enforcement.

Scope: every file the agent modifies in a session gets voice-checked before commit. Pass results are not surfaced in the visible session output; only failures surface to Mike or ORIN. Voice check failures on non-customer-facing files (YAML, configs, internal docs) are still resolved before commit, same as failures on customer-facing copy.

## Matrixify import file

The SEO workforce does not build the Matrixify export filter or the import file. A separate "Step 2" process owns both, working from the briefs and Mike's export; the workforce handoff is the briefs plus the handle list when asked. For reference on the file's shape, see `context/matrixify-import-template.md`: both the seven-column XLSX form (sheet named `Products`, numeric `ID`) and the six-column CSV form (bare metafield names, handle-keyed) import correctly, verified against Batch 9's live pages. XLSX is the documented default because the sheet name auto-resolves the entity and the numeric ID is a stronger match key; the CSV form only differs in that it shows a "Sheets require entity selection" prompt, resolved by picking Products.

## Cross-references

- `context/matrixify-import-template.md` is the reference shape for Matrixify product-import files (two valid forms, XLSX default vs handle-keyed CSV; scope note that Step 2 owns the build).
- `context/page-type-playbooks/product-page-playbook.md` 'Meta Title and Meta Description compliance (added 2026-07-31)' is the canonical rule for Meta Title (48-char written ceiling, no store-name or manufacturer-brand pipe suffix, brand-front) and Meta Description (120 to 160, full sentences, no colon-fragment opener, light CTA), with cleat and jersey exemplars. The theme suffix is the literal `` ` – ProSoccer` `` (en-dash, verified 2026-07-31).
- `context/brand-ip-constraints.md` documents the FIFA terminology constraint that applies to all page-optimization deliverables produced under this folder structure.
- `.claude/agents/on-page-seo/agent.md` Section 8 ("Handoff Patterns") and Section 13 ("Output Templates") reference this convention for the Fresh Optimization workflow, per-page brief file placement, and the mandatory keyword research block.
- `.claude/agents/on-page-seo/agent.md` Section 2 Step 0 is the canonical SCRIBE pre-flight tool verification protocol referenced under the Tool inventory section above; other agents may adopt the same pattern as added.
- `templates/consolidated-page-brief-template.md` is the canonical brief format for the Fresh Optimization workflow described above, including the '## Keyword research' block.
- `context/page-type-playbooks/product-page-playbook.md` 'Internal links only on product pages' is the canonical PDP link policy referenced above.
