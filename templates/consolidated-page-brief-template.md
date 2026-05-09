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
9. Append the matching row to `deliverables/tracking/collections-master.csv` or `products-master.csv` when Mike approves.

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

- **Current slug:** <current value>
- **SEO assessment:** <too short / generic / appropriate / too long / broken>
- **Recommended slug:** <new slug OR "no change" with reasoning>
- **Migration impact (if change recommended):** <redirect requirement, link equity transfer notes, GSC monitoring period>

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
