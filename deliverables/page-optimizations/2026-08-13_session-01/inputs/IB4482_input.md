# Input: IB4482 -- Nike Tiempo Maestro Club Turf Soccer Shoes (Shadow Pack, FA26)

_v2 pre-dispatch input. Work from this file only. Mirror the STRUCTURE of the IB1602 trio anchor, never its prose._

## Identity
- SKU: IB4482-001
- URL: https://www.prosoccer.com/products/nike-tiempo-maestro-club-turf-soccer-shoes-shadow-pack-fa26
- Brand: Nike (capitalized)
- Brand-IP posture: cycle-language-only. **Nike holds NO FIFA license. No FIFA or World Cup language.**
- Product category: footwear, SHOES (turf model: says "shoes", never "cleats")
- Care H2 required: yes
- Tier: club
- Avatar: Jennifer, the parent-buyer.
- Word band: 340-390 (+/-15 tolerance).

## Phase 0 scrape data (source of truth; scrape-wins)
- Live title: Nike Tiempo Maestro Club Turf Soccer Shoes - Shadow Pack (FA26)
- Colorway: Black/Black/Illusion Green
- Upper: synthetic leather, soft touch in wet or dry conditions, molds to the foot
- Outsole: rubber, "traction for the turf"
- Weight: NOT STATED. Do not state one.
- Price: $64.99 -- KEEP OUT of body copy.
- Care material: synthetic upper, no leather conditioner.

## Keywords (validated, do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | nike tiempo maestro club turf shadow | no measurable volume (DFS both endpoints, 2026-08-13) | |
| Secondary (pack) | nike shadow pack | 140 | |
| Topical context ONLY (Academy tier, do NOT target) | nike tiempo maestro academy turf | 20 | |

Pack-qualified because a live Break 'Em FA26 sibling exists at this exact config. NO SEASON CODE: Shadow exists at the Club tier only in FA26. Note the Academy Turf line is crowded and already spoken for: IQ2388 holds `nike tiempo maestro academy turf breakout` (live) and IB4484 holds `nike tiempo maestro academy turf shadow fa26` (Batch 13). Stay on the Club tier token.

## Meta fields (ORIN-set; use exactly)
- Meta Title: `Nike Tiempo Maestro Club Turf Shadow` (36 chars)
- Meta Description: 120-160 chars, full sentences, no colon-fragment opener.

## Validated internal links (ORIN link-check 2026-08-13; body only)
- https://www.prosoccer.com/collections/artificial-turf -- anchor "turf soccer shoes" -- validated live, in refreshed sitemap
- https://www.prosoccer.com/products/nike-tiempo-maestro-club-fg-mg-soccer-cleats-shadow-fa26 -- anchor "firm-ground version" -- validated 200, H1 "Nike Tiempo Maestro Club Firm/Multi Ground Soccer Cleats - Shadow Pack (FA26)" (trio sibling; surface choice)

Place 2 links in different H2 sections.

## Differentiation lane (write prose FROM this)
- Angle: the turf-field regular who still wants a leather-feel touch, not a stiff plastic shoe.
- Opening hook: the artificial pitch where most youth training now happens, and the trap that usually goes wrong on it.
- Primary metaphor: softness on a hard surface. Do NOT reuse IB1602's soft-touch-and-control lane framing verbatim; this lane is specifically the contrast between a forgiving upper and an unforgiving surface.
- Facet vs siblings: TURF with a rubber outsole. IB1602 is FG/MG with studs. IB4486 is indoor and names street and court surfaces.

## Structure skeleton (mirror STRUCTURE, never prose)
- H2 sequence: identity hook -> the rubber outsole on turf -> use-case (training and small-sided) -> Product Details: -> Fit Notes -> Care and Maintenance -> FAQs about
- Short Description 50-100 words; Description 340-390 (tol 15); FAQ 3 Q&A
- Product Details bullets: upper, outsole + surface, feel, colorway

## Forbidden phrasings (barred by the IB1602 anchor)
- Verbatim: ["settles instead of bounces", "a price a club family can say yes to"]
- Motifs: ["soft touch and control", "leather-feel heritage", "the first touch that settles"]
- Title-frames: ["A touch-first cleat for the club player"]

<!-- gate-meta authoritative; batch_gate.py parses it. -->
```gate-meta
{
  "sku": "IB4482",
  "brand": "nike",
  "brand_ip_posture": "cycle-language-only",
  "tier": "club",
  "word_band": [340, 390],
  "word_band_tolerance": 15,
  "primary_keyword": "nike tiempo maestro club turf shadow",
  "forbidden_phrasings": {
    "verbatim": ["settles instead of bounces", "a price a club family can say yes to"],
    "motifs": ["soft touch and control", "leather-feel heritage", "the first touch that settles"],
    "title_frames": ["A touch-first cleat for the club player"]
  }
}
```
