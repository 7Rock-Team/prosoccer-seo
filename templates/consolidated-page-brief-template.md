# Implementation-Ready Page Optimization Brief Template

_Streamlined brief for Mike. Workforce-internal logs preserve full depth (KIRA keyword research, RECON competitor analysis, SCRIBE per-element reasoning, VERITAS schema flags, performance baselines, validation plans, sources, severity, confidence, red-team appendix, implementation checklist). Mike can ask for any of those at any time. Schema flags route to Misha or developer separately, outside this brief. Landmark cases that need the deep version use the archived template at `templates/consolidated-page-brief-template-archive.md`._

## How to use this template

1. Copy this file to `deliverables/page-optimizations/YYYY-MM-DD_<page-slug>.md` (replace YYYY-MM-DD with today's date and `<page-slug>` with the URL slug, e.g., `2026-05-08_mexico.md` for `/collections/mexico`).
2. Fill every field with implementation-ready copy lifted from specialist contributions.
3. Run `scripts/voice_check.py` on the populated brief and on every quoted copy string before holding for Mike approval.
4. Per `context/03-brand-voice.md` 'Emotional Connection Over Feature Selling', Short Description leads with feeling, identity, or moment for the primary avatar. Long Description anchors body copy in emotion with features as support, never the lead.
5. Per `context/03-brand-voice.md` 'Cognitive Load Minimization', lead with the noun, one idea per sentence, short paragraphs, jargon depth matched to avatar fluency.
6. Per `.claude/agents/on-page-seo/agent.md` Section 9 'Keyword placement per field', main keyword anchors Title and Slug; long-tail variants lift Long Description body copy and H2 subheadings.
7. Append the matching row to `deliverables/tracking/collections-master.csv` or `products-master.csv` when Mike approves.

## Template starts below this line

---

# Page Optimization Brief: <page slug>

- **URL:** <full path>
- **Date:** YYYY-MM-DD
- **Sprint phase:** [Wave 1 / Wave 2 / Wave 3 / standalone / post-sprint]

## Keywords

- **Main keyword (head):** <head keyword>
- **Supporting keywords (long-tail):** <variant 1>, <variant 2>, <variant 3>, <variant 4>

## Storefront fields

### Title (Collection Title)

<verbatim title to paste into Shopify Title field>

### Slug (URL Handle)

<url-handle>

### SEO Meta Title

<verbatim meta title>

[NN chars]

### SEO Meta Description

<verbatim meta description>

[NN chars]

### Short Description (intro paragraph)

<emotion-first intro, 1 to 3 sentences. Leading sentence carries feeling, identity, or moment for the primary avatar. Features support the feeling; they never lead.>

### Long Description (body copy)

<emotion-anchored body copy with H2 structure, 200 to 500 words. Features integrated as support, not the lead. H2 subheadings carry long-tail keyword variants.>

## Plain language summary for Tony

<one paragraph, no jargon, leads with the outcome. Drop entirely if the brief never reaches client-side communication.>

## Voice check

- Brief: [PASS / FAIL with line numbers]
- Per-string: Title [PASS/FAIL], Slug [PASS/FAIL], SEO Meta Title [PASS/FAIL], SEO Meta Description [PASS/FAIL], Short Description [PASS/FAIL], Long Description [PASS/FAIL]

---

_Workforce-internal logs preserve the depth on request. Sources, severity, confidence, validation plans, performance baselines, KIRA keyword research, RECON competitor snapshot, SCRIBE per-element reasoning, VERITAS schema findings, implementation checklist, ORIN cross-agent reconciliation, red-team appendix, and master CSV row reference all live in workforce-internal artifacts (specialist briefings under `.claude/agents/<specialist>/briefings/`, ORIN merge notes, master CSV row). Mike can request any of these at any time._
