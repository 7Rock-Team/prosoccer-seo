# Implementation-Ready Page Optimization Brief Template

_Streamlined brief for Mike. Workforce-internal logs preserve full depth (KIRA keyword research, RECON competitor analysis, SCRIBE per-element reasoning, VERITAS schema flags, performance baselines, validation plans, sources, severity, confidence, voice check status, red-team appendix, implementation checklist). Mike can ask for any of those at any time. Schema flags route to Misha or developer separately, outside this brief. Landmark cases that need the deep version use the archived template at `templates/consolidated-page-brief-template-archive.md`._

## How to use this template

1. Copy this file to `deliverables/page-optimizations/YYYY-MM-DD_<page-slug>.md` (replace YYYY-MM-DD with today's date and `<page-slug>` with the URL slug, e.g., `2026-05-08_mexico.md` for `/collections/mexico`).
2. Identify page type and load the matching playbook from `context/page-type-playbooks/` per `.claude/agents/on-page-seo/agent.md` Section 2 step 4b. Subject matter from the playbook governs WHAT each field is about; the six copy-writing principles govern HOW it reads.
3. Fill every field with implementation-ready copy lifted from specialist contributions.
4. Run `scripts/voice_check.py` on the populated brief and on every quoted copy string before holding for Mike approval. Voice check is a workforce-internal gate; the result lives in the workforce-internal logs, not in the visible brief.
5. Per `context/03-brand-voice.md` 'Emotional Connection Over Feature Selling', Short Description leads with feeling, identity, or moment for the primary avatar. Long Description anchors body copy in emotion with features as support, never the lead.
6. Per `context/03-brand-voice.md` 'Cognitive Load Minimization', lead with the noun, one idea per sentence, short paragraphs, jargon depth matched to avatar fluency.
7. Per `.claude/agents/on-page-seo/agent.md` Section 9 'Keyword placement per field', main keyword anchors Title and Slug; long-tail variants lift Long Description body copy and H2 subheadings.
8. Slug Optimization Discipline: aggressive default. Recommend a slug change when the current slug is genuinely underoptimized for SEO (too generic, too short, missing primary keyword). Document migration impact for high-traffic pages so Mike can weigh the cost. Always require 301 redirect setup if change is recommended.
9. Brief structure: SEO Implementation H2 surfaces all paste-ready fields up top in the order Mike pastes them into Shopify admin (Title -> Short Description -> Long Description body -> SEO Meta Title -> SEO Meta Description -> Slug). Workforce-internal reference (Avatar Scope, Keywords) drops below the implementation block.
10. Append the matching row to `deliverables/tracking/collections-master.csv` or `products-master.csv` when Mike approves.

## Template starts below this line

---

# Page Optimization Brief: <page slug>

- **URL:** <full path>
- **Date:** YYYY-MM-DD
- **Sprint phase:** [Wave 1 / Wave 2 / Wave 3 / standalone / post-sprint]
- **AIDAR stage:** [Awareness / Interest / Desire / Action / Retention; note current cycle and expected shift]

## SEO Implementation

### Title (Collection Title)

<verbatim title to paste into Shopify Title field>

### Short Description (intro paragraph)

<emotion-first intro, 1 to 3 sentences, ~50-80 words. Leading sentence carries feeling, identity, or moment for the primary avatar. Features support the feeling; they never lead. Head keyword integrated naturally where it doesn't force the lead.>

### Long Description (body copy)

<emotion-anchored body copy with H2 sub-sections, 200 to 500 words. Features integrated as support, not the lead. H2 sub-sections carry long-tail keyword variants where natural. Per `context/page-type-playbooks/collection-page-playbook.md` 'Evergreen body, contained catalyst', body must be predominantly evergreen with one clearly-framed catalyst section that survives 12+ months without rewrites. FAQ section lives as a body sub-block at the end (same Shopify Description body field as the rest of Long Description).>

(Body sub-sections render as H2 in the live page; paste as-is from this brief into Shopify Description body.)

## H2 Sub-section 1 (catalyst section, current-cycle framing)

<body copy>

## H2 Sub-section 2 (evergreen)

<body copy>

## H2 Sub-section 3 (evergreen)

<body copy>

## H2 Sub-section 4 (evergreen)

<body copy>

## H2 Sub-section 5 (evergreen)

<body copy>

## H2 Sub-section 6 (evergreen)

<body copy>

## <Topic> FAQs

<5-7 topic-specific Q-and-A pairs. Each answer 2-4 sentences. NOT generic store-policy questions.>

### Internal links (1-2 max)

<Per `context/page-type-playbooks/collection-page-playbook.md` 'Internal link strategy' (or `product-page-playbook.md` equivalent for product pages). Each link must be live-validated via Firecrawl MCP before inclusion (200 OK, content matches expected page type, no soft-404). Anchor text 2 to 5 words, descriptive, reads naturally.>

1. **URL:** /collections/<slug>
   - **Anchor text:** <exact phrase used in body>
   - **Body location:** <H2 sub-section name where the link appears>
   - **Validation:** 200 OK / fetched YYYY-MM-DD via Firecrawl / content confirmed (<H1 of destination> / <product count> / <other observed signal>)
   - **Reasoning:** <why this link, why this anchor>

2. **URL:** /collections/<slug>
   - **Anchor text:** <exact phrase used in body>
   - **Body location:** <H2 sub-section name>
   - **Validation:** 200 OK / fetched YYYY-MM-DD via Firecrawl / content confirmed
   - **Reasoning:** <why this link, why this anchor>

(If a candidate failed live validation, replace the entries above with `### Skipped link (validation failure)` and document the URL, the specific failure reason (404 / 301 redirect to <other> / soft-404 returns homepage / other), and the alternative selected (or `none` if total stayed at 1-2).)

### SEO Meta Title

<verbatim meta title>

[NN chars]

### SEO Meta Description

<verbatim meta description>

[NN chars]

### Slug (URL Handle)

- **Current slug:** <current value>
- **SEO assessment:** <too short / generic / appropriate / too long / broken>
- **Recommended slug:** <new slug OR "no change" with reasoning>
- **Migration impact (if change recommended):** <redirect requirement, link equity transfer notes, GSC monitoring period, rollback condition>

## Avatar Scope

- **Primary:** <avatar with reasoning anchor>
- **Secondary:** <avatar with reasoning, OR "none" with reasoning>
- **Excluded:** <avatars named with reasoning, not omitted silently>
- **Cross-avatar landing:** <if a non-primary avatar might still land via search, note it; otherwise "none">

## Keywords

- **Main keyword (head):** <head keyword>
- **Supporting keywords (long-tail):** <variant 1>, <variant 2>, <variant 3>, <variant 4>
