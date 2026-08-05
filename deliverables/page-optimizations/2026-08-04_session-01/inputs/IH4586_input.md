# Input: IH4586 -- adidas F50 Hyperfast League Mid Turf Soccer Shoes (Chaos Vs Control Pack, FA26)

_v2 pre-dispatch input. TURF shoe: say "shoes", surface turf/synthetic. Sibling of IH7090 (FG cleat); differ only on surface, so keep the turf lane distinct from IH7090's firm-grass lane._

## Identity
- SKU: IH4586
- URL: https://www.prosoccer.com/products/adidas-f50-hyperfast-league-mid-turf-soccer-shoes-chaos-vs-control
- Handle: adidas-f50-hyperfast-league-mid-turf-soccer-shoes-chaos-vs-control
- Brand: adidas (lowercase)
- Brand-IP posture: cycle-language-only (no FIFA / World Cup language)
- Product category: footwear; Care H2 required: yes
- Tier: league; Word band: 340-390 (+/-15)

## Phase 0 scrape data (scrape-wins)
- Colorway: Cloud White / Solar Purple / Solar Turbo
- Upper: HALOSKIN (flexible minimal, great touch); HALOSHELL+ engineered mesh (weight reduction)
- Cut: MID-CUT ankle height
- Plate: turf-specific rubber outsole (grip on short synthetic blades)
- Weight: not in scrape
- Price: $89.99 -- KEEP OUT of body
- Tech (scrape): Haloskin (touch, lightweight); Haloshell+ (weight/speed); rubber turf outsole (reliable grip on short-blade synthetic); adjustable lacing (lockdown)
- Care: synthetic; damp cloth
- Sibling (cross-link): IH7090 League Mid FG (firm-ground version)

## Keywords (validated; do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | adidas f50 league mid turf chaos vs control | no measurable (pack sub-floor by design) | |
| Secondary (pack) | chaos vs control | 50 | |
| Topical context (do NOT target; incumbent-owned) | adidas f50 league turf | | |

Sub-floor by design. The unqualified `adidas f50 league turf` belongs to the incumbent IH4582 (same mid-cut config, RTG SP26), not this page. Do not target it.

## Validated internal links (body only, two different H2s)
- https://www.prosoccer.com/products/adidas-f50-hyperfast-league-mid-fg-soccer-cleats-chaos-vs-control -- anchor "firm-ground version" -- validated 200 (sibling; surface choice)
- https://www.prosoccer.com/collections/artificial-turf -- anchor "turf soccer shoes" -- validated 200, H1 "Turf Soccer Shoes & Cleats for Adults"

## Differentiation lane (write FROM this)
- Angle: the same F50 speed built for turf; grip for short synthetic blades on weeknight small-sided pitches.
- Opening hook: the turf regular who plays midweek fives and needs grip on the plastic.
- Primary metaphor: speed for the turf game / grip on the short blade.
- Use-case: turf and small-sided; the player whose home surface is synthetic.
- Positioning: Haloskin lightweight; turf rubber outsole.
- Facet vs siblings: TURF (IH7090 = same League Mid on firm ground).

## Structure skeleton (mirror STRUCTURE only)
- H2 sequence: overview / identity hook -> turf-surface fit & grip -> use-case (small-sided turf) -> Product Details: -> Fit Notes -> Care and Maintenance -> FAQs about
- Field lengths: Short Description 50-100 words; Description 340-390 (tol 15); FAQ 3
- Product Details bullets: upper (Haloskin/Haloshell+), outsole (turf rubber), cut (mid), care (weight not in scrape, omit)

## Forbidden phrasings
- Verbatim: ["Some players chase the game. You conduct it."]
- Motifs: ["conduct", "tempo", "dictate", "set the pace"]
- Title-frames: ["sets the pace"]

```gate-meta
{
  "sku": "IH4586",
  "brand": "adidas",
  "brand_ip_posture": "cycle-language-only",
  "tier": "league",
  "word_band": [340, 390],
  "word_band_tolerance": 15,
  "primary_keyword": "adidas f50 league mid turf chaos vs control",
  "forbidden_phrasings": {
    "verbatim": ["Some players chase the game. You conduct it."],
    "motifs": ["conduct", "tempo", "dictate", "set the pace"],
    "title_frames": ["sets the pace"]
  }
}
```
