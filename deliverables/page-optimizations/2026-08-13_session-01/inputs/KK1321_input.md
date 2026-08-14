# Input: KK1321 -- adidas Junior F50 Hyperfast League Turf Soccer Shoes (Chaos Vs Control Pack, FA26)

_v2 pre-dispatch input. Work from this file only. Mirror the STRUCTURE of the IH7094 exemplar, never its prose._

## Identity
- SKU: KK1321
- URL: https://www.prosoccer.com/products/adidas-jr-f50-hyperfast-league-tf-soccer-shoes-chaos-vs-control
- Brand: adidas (always lowercase in prose)
- Brand-IP posture: cycle-language-only (no FIFA or World Cup language)
- Product category: footwear, SHOES (turf model: says "shoes", never "cleats")
- Care H2 required: yes
- Tier: league, JUNIOR
- Avatar: Jennifer, the parent-buyer. Grade-school player.
- Word band: 280-360 (+/-15 tolerance). Youth band, shorter than the adult SKUs.

## NAMING, read this before writing a word
The HANDLE abbreviates to `jr` and `tf`. The LIVE TITLE spells both out: **"adidas Junior F50 Hyperfast League Turf Soccer Shoes"**. Use **Junior** and **Turf** in all copy. Never "Jr", never "TF", never "kids". Registry convention agrees: every junior row uses "junior" (`adidas junior f50 turf`, `adidas junior f50 club`, `adidas junior f50 league mid`).

## Phase 0 scrape data (source of truth; scrape-wins)
- Live title: adidas Junior F50 Hyperfast League Turf Soccer Shoes - Chaos Vs Control Pack (FA26)
- Colorway: Cloud White / Solar Purple / Solar Turbo
- Upper: Haloskin
- Outsole: turf
- Midsole: lightweight EVA. Fit: regular, adjustable lacing
- Weight: NOT STATED. Do not state one.
- Price: $69.99 -- KEEP OUT of body copy.
- CASING: write Haloskin in title case.

## Keywords (validated, do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | adidas junior f50 league turf chaos vs control | no measurable volume (DFS both endpoints, 2026-08-13; absent from the DFS database entirely) | |
| Secondary (pack) | chaos vs control | 90 | |
| Topical context ONLY (registered to KK1319, do NOT target) | adidas junior f50 turf | GSC override | |

Sub-floor by design and LOCKED. The unqualified `adidas junior f50 league turf` is also unmeasured, and belongs to the earliest live Junior League Turf incumbent (Darkspark FA24 / Vivid Horizon FA24). Do not target it, do not broaden.

## Meta fields (ORIN-set; use exactly)
- Meta Title: `adidas Junior F50 Hyperfast League Turf` (39 chars)
- **PACK DROPPED FROM TITLE BY RULE.** With the pack the string is 56 chars against a 48 cap, and abbreviating "Junior" to "Jr" only reaches 52. Per `product-page-playbook.md` 'Meta title priority ordering, and the generation token', the pack yields.
- **BINDING CONSEQUENCE: the Meta Description MUST name the Chaos vs Control pack explicitly.** Not optional. 120-160 chars, full sentences, no colon-fragment opener.

## Validated internal links (ORIN link-check 2026-08-13; body only)
- https://www.prosoccer.com/collections/youth-soccer-shoes -- anchor "kids' soccer cleats" -- validated live, in refreshed sitemap
- https://www.prosoccer.com/collections/artificial-turf -- anchor "turf soccer shoes" -- validated live, in refreshed sitemap

Place 2 links in different H2 sections.

## Differentiation lane (write prose FROM this)
- Angle: the grade-school player whose season lives on the turf field behind the school, and the parent buying for it.
- Opening hook: the after-school practice on synthetic grass, twice a week, every week.
- Primary metaphor: the everyday workhorse for the surface they are actually on. Do NOT reuse IH7094's reach/access, KJ3409's surface-matching, KK1061's confined-space, or KK1049's precision/materials metaphor.
- Facet vs siblings: JUNIOR sizing + turf. KJ3409 is the adult Club turf. This is the only youth SKU in the adidas five.

## Structure skeleton (mirror STRUCTURE, never prose)
- H2 sequence: identity hook -> what the turf outsole does for a young player -> use-case (practice and small-sided) -> Product Details: -> Fit Notes -> Care and Maintenance -> FAQs about
- Short Description 50-100 words; Description 280-360 (tol 15); FAQ 3 Q&A
- Fit Notes must address growing feet and sizing, per the Jennifer avatar.
- Product Details bullets: upper, outsole + surface, midsole, fit/lacing, colorway

## Forbidden phrasings (barred by the exemplar, KJ3409, KK1061 and KK1049)
- Verbatim: ["without the flagship outlay", "the F50 look", "right tool for the plastic", "the game that never stops moving"]
- Motifs: ["reach and access", "outgrown starter cleats", "surface-matching", "under the lights", "confined space", "precision and materials"]
- Title-frames: ["The player who wants the F50 feel"]

<!-- gate-meta authoritative; batch_gate.py parses it. -->
```gate-meta
{
  "sku": "KK1321",
  "brand": "adidas",
  "brand_ip_posture": "cycle-language-only",
  "tier": "league",
  "word_band": [280, 360],
  "word_band_tolerance": 15,
  "primary_keyword": "adidas junior f50 league turf chaos vs control",
  "forbidden_phrasings": {
    "verbatim": ["without the flagship outlay", "the F50 look", "right tool for the plastic", "the game that never stops moving"],
    "motifs": ["reach and access", "outgrown starter cleats", "surface-matching", "under the lights", "confined space", "precision and materials"],
    "title_frames": ["The player who wants the F50 feel"]
  }
}
```
