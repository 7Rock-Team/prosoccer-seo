# Input: KJ3409 -- adidas F50 Hyperfast Club Turf Soccer Shoes (Chaos Vs Control Pack, FA26)

_v2 pre-dispatch input. Work from this file only. Mirror the STRUCTURE of the IH7094 exemplar, never its prose._

## Identity
- SKU: KJ3409
- URL: https://www.prosoccer.com/products/adidas-f50-hyperfast-club-turf-soccer-shoes-chaos-vs-control
- Brand: adidas (always lowercase in prose)
- Brand-IP posture: cycle-language-only (no FIFA or World Cup language)
- Product category: footwear, SHOES (turf model: says "shoes", never "cleats")
- Care H2 required: yes
- Tier: club
- Avatar: Jennifer, the parent-buyer.
- Word band: 340-390 (+/-15 tolerance).

## Phase 0 scrape data (source of truth; scrape-wins)
- Live title: adidas F50 Hyperfast Club Turf Soccer Shoes - Chaos Vs Control Pack (FA26)
- Colorway: Cloud White / Solar Purple / Solar Turbo
- Upper: speed-focused synthetic with a debossed texture
- Outsole: turf
- Other stated: lightweight floating tongue for comfort and a secure feel
- **CUT: THIS IS NOT A MID.** The page carries no mid-cut, collar or ankle language anywhere; ORIN checked explicitly. DO NOT write a collar, a mid cut, or ankle lockdown into this brief. Its FG/MG sibling IH7094 is the mid; this one is not.
- Weight: NOT STATED. Price: $64.99 -- KEEP OUT of body copy.

## Keywords (validated, do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | adidas f50 club turf chaos vs control | no measurable volume (DFS both endpoints, 2026-08-13) | |
| Secondary (pack) | chaos vs control | 90 | |
| Topical context ONLY (registered to IH9375, do NOT target) | adidas f50 club | 210 recorded | |

Sub-floor by design and LOCKED. The unqualified `adidas f50 club turf` (20/mo) belongs to the earliest live Club Turf incumbent (Electric Stealth FA25 / Radiant Blaze FA25). Do not target it, do not broaden.

## Meta fields (ORIN-set; use exactly)
- Meta Title: `adidas F50 Hyperfast Club Turf Chaos vs Control` (47 chars)
- Meta Description: 120-160 chars, full sentences, no colon-fragment opener. Must name the Chaos vs Control pack.

## Validated internal links (ORIN link-check 2026-08-13; body only)
- https://www.prosoccer.com/collections/artificial-turf -- anchor "turf soccer shoes" -- validated live, in refreshed sitemap
- https://www.prosoccer.com/products/adidas-f50-hyperfast-club-mid-fg-mg-soccer-cleats-chaos-vs-control -- anchor "firm-ground version" -- validated 200, H1 "adidas F50 Hyperfast Club Mid Firm/Multi Ground Soccer Cleats - Chaos Vs Control Pack (FA26)" (sibling; surface choice)

Place 2 links in different H2 sections.

## Differentiation lane (write prose FROM this)
- Angle: the weeknight turf regular at club level; the shoe for the surface youth soccer actually trains on.
- Opening hook: the short synthetic pitch under the lights, where the first step decides the play.
- Primary metaphor: surface-matching (right tool for the plastic). Do NOT reuse IH7094's reach/access metaphor.
- Facet vs siblings: TURF, low-cut, no collar. IH7094 is mid-cut FG/MG.

## Structure skeleton (mirror STRUCTURE, never prose)
- H2 sequence: identity hook -> what the turf outsole does -> use-case (weeknight small-sided) -> Product Details: -> Fit Notes -> Care and Maintenance -> FAQs about
- Short Description 50-100 words; Description 340-390 (tol 15); FAQ 3 Q&A
- Product Details bullets: upper, outsole + surface, tongue/fit, colorway

## Forbidden phrasings (barred by the IH7094 exemplar)
- Verbatim: ["without the flagship outlay", "the F50 look"]
- Motifs: ["reach and access", "outgrown starter cleats", "one pair for both surfaces"]
- Title-frames: ["The player who wants the F50 feel"]

<!-- gate-meta authoritative; batch_gate.py parses it. -->
```gate-meta
{
  "sku": "KJ3409",
  "brand": "adidas",
  "brand_ip_posture": "cycle-language-only",
  "tier": "club",
  "word_band": [340, 390],
  "word_band_tolerance": 15,
  "primary_keyword": "adidas f50 club turf chaos vs control",
  "forbidden_phrasings": {
    "verbatim": ["without the flagship outlay", "the F50 look"],
    "motifs": ["reach and access", "outgrown starter cleats", "one pair for both surfaces"],
    "title_frames": ["The player who wants the F50 feel"]
  }
}
```
