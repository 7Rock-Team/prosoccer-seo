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
    <slug>_brief.md
    ...
```

### Naming convention

- **Folder name pattern:** `YYYY-MM-DD_session-NN/` where YYYY-MM-DD is the session start date and NN is a zero-padded two-digit session ordinal within the work-unit (e.g., `01`, `02`, `03`).
- **Work-unit boundary:** a "session" is a single ORIN-orchestrated work unit (Mike's prompt to the agent, the agent's execution, and the GATE review or completion). Multi-session work units (e.g., a 3-collection whitelabel audit pilot) get a session folder per session.
- **Examples:**
  - `deliverables/page-optimizations/whitelabel-audit/2026-05-16_session-01/` (whitelabel audit pilot, session 1)
  - `deliverables/page-optimizations/whitelabel-audit/2026-05-17_session-02/` (whitelabel audit pilot, session 2)
  - `deliverables/page-optimizations/2026-06-01_session-01/` (a non-whitelabel batch of per-page briefs)

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
4. **Current ranking lookup via DataForSEO SERP API (mandatory).** Run `mcp__dfs-mcp__serp_organic_live_advanced` for the chosen primary keyword; identify whether the target URL appears in the top 100 organic results; capture position OR "not in top 100." Surface as a one-line `Current ranking:` entry in the visible Keyword research block. Apply the ranking-aware posture (see 'Ranking-aware posture' subsection below) before drafting recommendations. GSC MCP is the long-term ranking source of record; install pending per 'Tool inventory' below, DataForSEO SERP API is the current fallback.
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

## Internal Link Format Discipline (added 2026-06-03)

Every internal link suggestion in a PDP or collection brief must be a full HTTPS URL on the canonical domain. The canonical domain is `https://www.prosoccer.com` (with the `www` subdomain). Never a relative path, never `http://`, never a mangled or partial URL. The rule applies to the brief's `Internal links` sub-section, the brief-format template, and any inline link reference in modeled brief output.

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

A keyword-strategy discipline applied at SCRIBE Phase 2 (research) and Phase 4 (drafting). SCRIBE selects ONE supporting keyword for body-copy use, criterion = highest search volume among the Phase 2 supporting candidates. The selected keyword is woven into the Short Description (1 to 2 mentions) and the Long / body Description (3 to 5 mentions). Other supporting candidates stay in the workforce briefing audit trail (full candidate list with volumes, selected keyword + rationale, placement) but are NOT used in body copy. Primary keyword usage follows Gate 12 unchanged. Exception: two supporting keywords within 10% volume AND semantically distinct (not synonyms) -> include the second minimally (1 to 2 body mentions). Gate 12 sub-criterion (d) verifies ONE supporting keyword at 3 to 5 body mentions, not multiple at shallow density; ORIN sanity-scans at the orchestrator layer.

**Architectural learning note.** Supporting keyword selection discipline (added 2026-06-02): SCRIBE was including multiple supporting keywords throughout Short and Long Descriptions, treating each as coverage opportunity. Result: keyword-targeted copy rather than reader-focused copy, dilute signal for any single supporting term. New rule: SCRIBE selects ONE supporting keyword (highest search volume among candidates) for body copy use (1-2 Short Description mentions, 3-5 Long Description mentions). Other supporting candidates preserved in workforce briefing audit trail but not used in output. Exception: two supporting keywords within 10% volume AND semantically distinct permitted minimally.

Cross-references: both page-type playbooks 'Supporting keyword selection' + 'Keyword distribution discipline', `.claude/agents/on-page-seo/agent.md` Section 9 'Supporting keyword selection' + Gate 12, `.claude/agents/master-strategist/agent.md` Section 9 + Section 11 Gate 12.

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

**Architectural learning note.** Editorial philosophy discipline (added 2026-06-02 after Gate 14 codification): Gate 13 anti-stuffing and Gate 14 specific counts catch structural manifestations of a deeper editorial philosophy gap. SCRIBE was producing structurally-correct copy meeting all gates but lacking emotional resonance, reader-focused clarity, and value-first orientation. Four sub-disciplines codified as Phase 4 self-checks plus workforce-conventions philosophy: (1) Reader-first copy orientation, body copy serves buyer's emotional connection, not algorithm. (2) Cognitive load reduction, sentence length variance, one concept per sentence, concrete over abstract, scan-ability. (3) Value-first sequencing, each H2 follows hook -> connection -> specifics -> action arc. (4) Positive emotional anchoring, use belonging / identity / ritual / anticipation / heritage / place anchors; avoid scarcity / FOMO / status anxiety / hyperbole / false urgency manipulation patterns. These are judgment-dependent disciplines, not pattern-matchable structural rules. They live at SCRIBE Phase 4 application plus ORIN orchestrator sanity scan plus workforce-conventions cross-cutting philosophy. NOT codified as new gates (gates govern structural patterns; editorial philosophy is judgment). NOT script-level enforced (too judgment-dependent for regex). Surfaced from Day 2 batch #1 review where briefs met all 14 gates and the 4 prior Phase 4 disciplines but lacked the editorial layer that drives buyer connection.

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
| Description (body_html, accordion) | tiered by complexity: Simple ~125 to 200 / Standard ~200 to 300 / Complex ~300 to 400 words |
| Meta Title | 60 characters maximum, INCLUDING the Hyper theme brand suffix (so the input field stays under approximately 48 to 50 chars) |
| Meta Description | 160 characters maximum |
| URL handle (slug after `/products/`) | 70 characters maximum |

These are hard limits (FAIL if exceeded), not targets. The tiered Description range supersedes the earlier single "150-word" figure, which is now interpreted as the Short Description metafield, not the Description body. SCRIBE verifies each in Phase 4; ORIN re-checks at the orchestrator layer (Section 11 Gate 13).

### Product complexity classification

Description length is set by product complexity. Classification test: if a buyer needs more than 2 minutes to choose between sibling products in the same family, the product is complex; if they grab and go, it is simple.

- **Simple (~125 to 200 words):** keychains, lapel pins, magnets, decals, stickers, mini balls, basic flags, simple practice cones.
- **Standard (~200 to 300 words):** training and match balls, bags, backpacks, apparel with basic variants, shin guards, single-tier goalkeeper gloves.
- **Complex (~300 to 400 words):** soccer cleats (tier / plate / colorway / generation matrix), authentic jerseys (player versions, kit details), tournament-edition products with a collectibility narrative, technical goalkeeper gloves, anything needing sizing / fit / surface guidance.

### Description structure: prose H2 + "Product Details" bullet H2

The Description splits reader-first prose from technical bullets. Prose H2 sections (overview, use case, identity / belonging, heritage, sizing / fit) carry the WHY; a dedicated "Product Details" H2 bullet list (the exact ProSoccer-native term, per live PDPs like the Nike Superfly 11 Club) carries the WHAT (materials, plate / surface, tier features, weight, care, technology). Never list technical specs in prose. H2 count flexes by complexity (Simple 2 to 3, Standard 3 to 4, Complex 4 to 5); always include "Product Details" when there are specs worth listing.

### FAQ reconciliation across page types

Collection pages keep the conditional FAQ rule (skip unless the FAQ adds net-new value beyond the Long Description, per `context/page-type-playbooks/collection-page-playbook.md`). PDPs RECOMMEND a FAQ, governed by the SAME net-new-value criterion: 3 to 5 Q-and-A pairs that the Description body does not already cover, that real buyers ask (sizing, plate selection, sibling comparison, use-case fit, care / durability), and that add measurable decision value. Skip entirely if fewer than 3 genuinely useful Q-and-As exist. The criterion is identical across page types; only the default posture differs (collections lean skip, PDPs lean include).

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

MCP servers split into two categories based on transport and credential handling. The distinction governs whether a sub-agent can call the MCP directly or must request the parent to fetch and pass data via task context.

**Category A: stdio transport, environment-variable credentials.** Full sub-agent inheritance via Option B `mcpServers:` declarations. When a sub-agent's frontmatter lists a Category A server, the sub-agent receives a native subprocess connection at dispatch and can call `mcp__<server>__*` tools directly. Credentials live in environment variables passed to the subprocess, not in OAuth state. Verified working 2026-05-26 via Phase C sub-agent test dispatches across SCRIBE, VERITAS, and RECON.

Category A servers:

- `dfs-mcp` (DataForSEO; DataForSEO API credentials via env)
- `firecrawl-mcp` (Firecrawl; `FIRECRAWL_API_KEY` via env)
- `tavily-mcp` (Tavily stdio variant; `TAVILY_API_KEY` via env)

**Category B: HTTP transport with OAuth tokens via the claude.ai connector.** OAuth state lives with the top-level Claude Code session that performed the OAuth handshake. When ORIN or any specialist is dispatched as a sub-agent, the `mcpServers:` declaration propagates (the sub-agent knows the server exists) but the OAuth token does not propagate to the sub-agent's MCP client. Direct sub-agent calls fail authentication. The workaround pattern: the parent ORIN session runs the Category B MCP call and passes the fetched data into the specialist's task context as inline data. Specialists treat Category B data as read-from-task-context, not read-from-MCP.

Category B servers:

- `claude_ai_Google_Drive` (Google Drive via claude.ai OAuth connector; reads from the January 2026 audit folder and other shared Drive artifacts)
- `claude_ai_Tavily` (OAuth-authenticated Tavily via claude.ai connector; superseded by Category A `tavily-mcp` for sub-agent use, kept registered at parent session for ORIN's top-level discovery work when full-page extraction is needed)

This category split is structural to current Claude Code architecture. If a future Claude Code release ships OAuth-token inheritance for sub-agents, the category distinction collapses and both classes work natively at sub-agent dispatch. Until that lands, the categories are operationally distinct and the workforce treats them as such.

### Operational (live, callable today)

- **DataForSEO MCP, `mcp__dfs-mcp__*`** (Category A). Pay-per-use API access covering SERP data, keyword research, keyword difficulty, search intent, on-page audit, backlinks, domain analytics, and DataForSEO Labs endpoints. Credentials verified 2026-05-26 (status_code 20000 returned on `mcp__dfs-mcp__serp_locations`). Sub-agent inheritance verified 2026-05-26 via Phase C. Workforce-wide hard cap $100/month per Section 12 of each agent.
- **Firecrawl MCP, `mcp__firecrawl-mcp__*`** (Category A). Single-URL scraping, structured extraction, site mapping, bulk crawling, interactive sessions, monitor and agent endpoints. `FIRECRAWL_API_KEY` in env. Installed 2026-05-26; sub-agent inheritance verified the same session (Phase C: status 200 returned on Liverpool PDP, Predator PDP, Predator collection page from SCRIBE, VERITAS, and RECON respectively).
- **Tavily MCP (stdio), `mcp__tavily-mcp__*`** (Category A). Full-page web search with content extraction, plus extract, crawl, map, and research endpoints. `TAVILY_API_KEY` in env. Installed 2026-05-26 as the sub-agent-compatible replacement for OAuth `claude_ai_Tavily`. Sub-agent inheritance verified the same session (Phase C: three live results returned for a Liverpool jersey query dispatched from SCRIBE).
- **Playwright MCP, `mcp__plugin_playwright_playwright__*`** (Category A in practice; the plugin runs locally and does not depend on claude.ai OAuth). Headless browser automation for live SERP inspection, SPA-rendered content extraction, post-deployment visual validation, and screenshot capture. Read-only posture for all workforce use.
- **Google Drive MCP, `mcp__claude_ai_Google_Drive__*`** (Category B). Reads from the January 2026 audit folder (`1KF1213I-_nf9B04ASKoM_mcv5xydJ3h8`) and other shared Drive artifacts. Free at API level; cost is context-budget consumption. Sub-agents see the declaration in their `mcpServers:` blocks but cannot complete OAuth from the sub-agent context. Parent ORIN fetches Drive content and passes it inline to specialists via task context. Direct sub-agent calls fail; surface the discrepancy in the session briefing if encountered.
- **Tavily MCP (OAuth via claude.ai), `mcp__claude_ai_Tavily__*`** (Category B). Registered at the top-level session for ORIN's parent-only research work. Sub-agents use Category A `tavily-mcp` instead; this OAuth surface is not listed in any sub-agent `mcpServers:` block. Retained at parent session level only.
- **Local file system.** All `data/`, `context/`, `deliverables/`, `strategy/`, `shared-intelligence/`, `work-log/`, and `.claude/agents/<agent>/` paths. Plus the prosoccer theme repo for read-only template inspection (SCRIBE, VERITAS).
- **`scripts/voice_check.py`.** Hard gate on every customer-facing copy proposal and every markdown deliverable. Per the 'Voice check discipline' section below, run on every modified file regardless of change type.

### Install pending (referenced in agent narratives but not yet callable)

- **GSC MCP, `mcp__gsc-server__*`.** Not installed as of 2026-05-26. **Install scheduled as a separate workstream for the 2026-05-27 session.** Expected to be Category A (stdio + OAuth-via-Google-service-account or env-credentialed; transport TBD at install time). Until install lands, fall back paths by use case:
  - **Ranking context per page (primary keyword position lookup):** DataForSEO SERP API via `mcp__dfs-mcp__serp_organic_live_advanced`. This is the canonical ranking-context source for the Fresh Optimization workflow Step 4 (see 'Fresh Optimization workflow' above). Once GSC MCP lands, ranking context shifts to GSC `get_search_analytics` per URL for the source-of-record advantage; DataForSEO SERP remains useful for competitor-context lookups but not for ProSoccer's own ranking baseline.
  - **CTR ceiling diagnostics, query-by-page intersection, indexation state, Rich Results coverage:** CSV exports under `data/gsc-exports/` (12-month `_top-pages.csv`, `_top-queries.csv`, `_search-appearance.csv`). CSV granularity is coarser than the live API: no query-by-page intersection, no live `inspect_url_enhanced`, no Rich Results report, no live coverage-issue inspection. Workable for baseline tracking, CTR ceiling diagnostics at page level, and aggregated query monitoring. Mike refreshes the exports on cadence (target: monthly).

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
| gsc-server (install pending) | A (expected) | yes | yes | yes | no | yes |
| claude_ai_Google_Drive | B | yes | yes | yes | yes | yes |
| claude_ai_Tavily | B | parent-only | no | no | no | no |

Rationale per agent (Category A access governs direct callability; Category B access governs the parent-mediated workaround surface):

- **ORIN gets the full set.** Orchestrator role requires the ability to run any specialist's work at the parent level when needed (e.g., the parent-handles-MCP workaround pattern for Category B servers). ORIN holds the only `claude_ai_Tavily` surface in the workforce.
- **SCRIBE has DFS + Firecrawl + tavily-mcp + GSC (pending) + Drive (Category B).** Native Category A access to DFS, Firecrawl, and tavily-mcp covers keyword spot-validation, current-state PDP/collection extraction, and topic research with full-page content. No Playwright (Playwright is RECON's tool for competitor mobile-vs-desktop validation; SCRIBE doesn't need browser automation for copy production).
- **KIRA has DFS + tavily-mcp + GSC (pending) + Drive (Category B).** Keyword research is the core function; native Category A access to DFS and tavily-mcp covers SERP analysis, keyword discovery, and topic research. No Firecrawl (page scraping is SCRIBE/VERITAS work) or Playwright (browser automation is RECON's lane).
- **RECON has DFS + Firecrawl + Playwright + Drive (Category B).** Competitor monitoring needs SERP analysis (DFS), competitor page extraction (Firecrawl), and mobile-vs-desktop SERP rendering checks (Playwright). No tavily-mcp (Tavily is internal topic research, parent ORIN holds the OAuth Tavily for that work) and no GSC (GSC is own-site monitoring, not competitor monitoring).
- **VERITAS has DFS + Firecrawl + GSC (pending) + Drive (Category B).** Technical SEO needs SERP-position validation (DFS), site crawling (Firecrawl), and coverage diagnostics (GSC). No Playwright (covered by Section 8 handoffs to RECON when mobile-rendering checks are needed) and no tavily-mcp.

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

Production workflow runs as batch parallel dispatch with single daily batch commit per Mike's 2026-05-29 operational decision. Mike submits up to a 10-URL batch (eligibility pre-vetted in Shopify admin per the `Eligibility verification (Mike-pre-vetted at URL submission)` pattern). ORIN auto-classifies tier per URL (Tier 1 / 2A / 2B) and dispatches SCRIBE in parallel for all URLs concurrent via simultaneous Agent tool calls in a single message. Each SCRIBE instance runs the full per-tier discipline (research depth, brief drafting depth, field count) with all quality gates intact. After all briefs return, ORIN runs trust-but-verify per brief (read visible brief, independent voice check on both files, confirm gates pass) and then batch-commits all visible briefs + all workforce briefings + any follow-up files as a single atomic commit with comprehensive batch message. Single push.

**Speed target.** 10-URL mixed-tier batch completes in ~25-45 min wall clock vs ~3-4 hours sequential. The slowest individual brief in the batch sets the wall-clock floor; Firecrawl / DataForSEO / Tavily infrastructure response times are the secondary constraint.

**Quality discipline preserved per brief.** Voice check, 11 self-verification gates plus Gate 12 keyword distribution plus Gate 13 anti-stuffing, year-specificity keyword discipline, brand IP compliance, currency check, sensitivity check, fact verification, internal link validation, per-brief workforce briefing audit trail. None of these flex under batch dispatch.

**Operational gates removed (safety gates preserved).** Per-brief Mike gate review replaced by end-of-batch review at single commit gate. Per-brief commit + push cycle replaced by single daily batch commit + push. Tier classification Mike confirmation replaced by ORIN auto-classification with post-batch Mike review of the classifications applied.

**End-of-batch summary.** ORIN surfaces to Mike: brief file paths, tier classifications applied, any quality issues flagged for Mike attention, cost tracking summary, any architectural learnings surfaced through the batch.

Cross-references: `.claude/agents/master-strategist/agent.md` Section 9 'Batch parallel dispatch and single daily batch commit' (ORIN procedural workflow); `.claude/agents/on-page-seo/agent.md` Section 9 'Tiered workflow variants' (per-tier scope SCRIBE applies regardless of dispatch pattern); `context/page-type-playbooks/product-page-playbook.md` 'Tiered workflow architecture for PDP optimization' + `context/page-type-playbooks/collection-page-playbook.md` 'Tier 2B canonical workflow' (per-page-type production workflow now runs under batch parallel dispatch as the production pattern).

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

## Cross-references

- `context/brand-ip-constraints.md` documents the FIFA terminology constraint that applies to all page-optimization deliverables produced under this folder structure.
- `.claude/agents/on-page-seo/agent.md` Section 8 ("Handoff Patterns") and Section 13 ("Output Templates") reference this convention for the Fresh Optimization workflow, per-page brief file placement, and the mandatory keyword research block.
- `.claude/agents/on-page-seo/agent.md` Section 2 Step 0 is the canonical SCRIBE pre-flight tool verification protocol referenced under the Tool inventory section above; other agents may adopt the same pattern as added.
- `templates/consolidated-page-brief-template.md` is the canonical brief format for the Fresh Optimization workflow described above, including the '## Keyword research' block.
- `context/page-type-playbooks/product-page-playbook.md` 'Internal links only on product pages' is the canonical PDP link policy referenced above.
