# Input: KK1049 -- adidas F50 Hyperfast Pro Indoor Soccer Shoes (Chaos Vs Control Pack, FA26)

_v2 pre-dispatch input. Work from this file only. Mirror the STRUCTURE of the IH7094 exemplar, never its prose._

## Identity
- SKU: KK1049
- URL: https://www.prosoccer.com/products/adidas-f50-hyperfast-pro-indoor-soccer-shoes-chaos-vs-control
- Brand: adidas (always lowercase in prose)
- Brand-IP posture: cycle-language-only (no FIFA or World Cup language)
- Product category: footwear, SHOES (indoor model: says "shoes", never "cleats")
- Care H2 required: yes
- Tier: pro
- Avatar: **Tyler, the athlete/player.** This is the one Pro-tier SKU in the batch. Write to the player, not the parent.
- Word band: 400-450 (+/-15 tolerance). Pro tier carries more spec depth.

## Phase 0 scrape data (source of truth; scrape-wins)
- Live title: adidas F50 Hyperfast Pro Indoor Soccer Shoes - Chaos Vs Control Pack (FA26)
- Colorway: Cloud White / Solar Purple / Solar Turbo
- Upper: Haloskin+ with a grippy coating, covered in Haloshell+ mesh
- Outsole: non-marking rubber for indoor courts
- Midsole: Lightstrike. Cage: Halocage+ TPU skin. Lining: synthetic. Closure: laces. Fit: regular
- **Weight: 214 g. STATE IT US-FIRST as `7.5 oz (214 g)`. The page qualifies it as "UK 8.5"; DROP that qualifier entirely, do not convert it.** A weight at one size is only meaningful if the reader knows the size convention, and converting UK 8.5 to a US size would assert something the scrape does not support. State the weight, omit the size.
- Price: $149.99 -- KEEP OUT of body copy.
- CASING: the live page styles these HALOSKIN+ / HALOSHELL+ / LIGHTSTRIKE / HALOCAGE+. Write them TITLE CASE (Haloskin+, Haloshell+, Lightstrike, Halocage+).

## Keywords (validated, do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | adidas f50 pro indoor chaos vs control | no measurable volume (DFS both endpoints, 2026-08-13) | |
| Secondary (pack) | chaos vs control | 90 | |
| Topical context ONLY (registered to IH4571, do NOT target) | adidas f50 indoor | 320 recorded | |

Sub-floor by design and LOCKED. The unqualified `adidas f50 pro indoor` (20/mo) belongs to the earliest live Pro Indoor incumbent (Vivid Horizon FA24). Do not target it, do not broaden.

## Meta fields (ORIN-set; use exactly)
- Meta Title: `adidas F50 Hyperfast Pro Indoor Chaos vs Control` (48 chars, exactly at the cap; do not add a character)
- Meta Description: 120-160 chars, full sentences, no colon-fragment opener. Must name the Chaos vs Control pack.

## Validated internal links (ORIN link-check 2026-08-13; body only)
- https://www.prosoccer.com/collections/indoor -- anchor "indoor soccer shoes" -- validated 200, H1 "Indoor Soccer Shoes for Men and Women", 53 products
- https://www.prosoccer.com/products/adidas-f50-hyperfast-league-indoor-soccer-shoes-chaos-vs-control -- anchor "League-tier indoor version" -- validated 200 (sibling; tier choice)

DO NOT link `/collections/indoor-soccer-shoes`: H1 is "Kids' Indoor Soccer Shoes", a youth collection, wrong audience for a Pro-tier adult page.

Place 2 links in different H2 sections.

## Differentiation lane (write prose FROM this)
- Angle: the serious indoor player who has decided the court is their game, not their offseason.
- Opening hook: the futsal or indoor league player who wants flagship materials on a hard floor.
- Primary metaphor: precision and top-tier materials at speed. Do NOT reuse IH7094's reach/access, KJ3409's surface-matching, or KK1061's confined-space-grip metaphor.
- Facet vs siblings: PRO tier. Haloskin+ upper, Lightstrike midsole, Halocage+ TPU, 7.5 oz, at roughly 1.7x the League indoor price. KK1061 is the League indoor.

## Structure skeleton (mirror STRUCTURE, never prose)
- H2 sequence: identity hook -> the upper and midsole package -> court use-case -> Product Details: -> Fit Notes -> Care and Maintenance -> FAQs about
- Short Description 50-100 words; Description 400-450 (tol 15); FAQ 3-4 Q&A
- Product Details bullets: upper, outsole + surface, midsole/cage tech, weight, closure/fit, colorway

## Forbidden phrasings (barred by the exemplar, KJ3409 and KK1061)
- Verbatim: ["without the flagship outlay", "the F50 look", "right tool for the plastic", "the game that never stops moving"]
- Motifs: ["reach and access", "outgrown starter cleats", "surface-matching", "under the lights", "confined space"]
- Title-frames: ["The player who wants the F50 feel"]

<!-- gate-meta authoritative; batch_gate.py parses it. -->
```gate-meta
{
  "sku": "KK1049",
  "brand": "adidas",
  "brand_ip_posture": "cycle-language-only",
  "tier": "pro",
  "word_band": [400, 450],
  "word_band_tolerance": 15,
  "primary_keyword": "adidas f50 pro indoor chaos vs control",
  "forbidden_phrasings": {
    "verbatim": ["without the flagship outlay", "the F50 look", "right tool for the plastic", "the game that never stops moving"],
    "motifs": ["reach and access", "outgrown starter cleats", "surface-matching", "under the lights", "confined space"],
    "title_frames": ["The player who wants the F50 feel"]
  }
}
```
