# Input: IB4486 -- Nike Tiempo Maestro Club Indoor Soccer Shoes (Shadow Pack, FA26)

_v2 pre-dispatch input. Work from this file only. Mirror the STRUCTURE of the IB1602 trio anchor, never its prose._

## Identity
- SKU: IB4486-001
- URL: https://www.prosoccer.com/products/nike-tiempo-maestro-club-indoor-soccer-shoes-shadow-pack-fa26
- Brand: Nike (capitalized)
- Brand-IP posture: cycle-language-only. **Nike holds NO FIFA license. No FIFA or World Cup language.**
- Product category: footwear, SHOES (indoor model: says "shoes", never "cleats")
- Care H2 required: yes
- Tier: club
- Avatar: Jennifer, the parent-buyer.
- Word band: 340-390 (+/-15 tolerance).

## THIS SKU IS UNQUALIFIED, AND THAT IS CORRECT
It is the ONLY Tiempo Maestro indoor page on the store at any tier, checked against the sitemap refreshed 2026-08-13 and confirmed on the live storefront. No pack sibling exists at this configuration, so no pack qualifier is owed and the primary is the plain configuration term. This is one of three genuine no-sibling cases in Batch 14 and the first the pack rule has produced at the Nike Club tier. Do NOT add a pack qualifier to the primary to "match" its trio siblings.

## Phase 0 scrape data (source of truth; scrape-wins)
- Live title: Nike Tiempo Maestro Club Indoor Soccer Shoes - Shadow Pack (FA26)
- Colorway: Black/Black/Illusion Green
- Upper: synthetic leather, soft touch in wet or dry conditions, molds to the foot
- Outsole: rubber
- **Surfaces named on the page: STREET, COURT, and INDOOR.** This is sourced, not invented, and it is the differentiation hook. Use it.
- Other stated: cushioned sockliner
- Weight: NOT STATED. Price: $64.99 -- KEEP OUT of body copy.
- Care material: synthetic upper, no leather conditioner.

## Keywords (validated, do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | nike tiempo maestro club indoor | no measurable volume (DFS both endpoints, 2026-08-13) | |
| Secondary (pack) | nike shadow pack | 140 | |

Sub-floor but UNQUALIFIED and hierarchy-clean: the term resolves to exactly one live product. Fully free in the registry against exact, containment and token-subset checks.

## Meta fields (ORIN-set; use exactly)
- Meta Title: `Nike Tiempo Maestro Club Indoor Shadow` (38 chars). The pack appears here because it fits and helps the buyer, even though the primary does not need it.
- Meta Description: 120-160 chars, full sentences, no colon-fragment opener.

## Validated internal links (ORIN link-check 2026-08-13; body only)
- https://www.prosoccer.com/collections/indoor -- anchor "indoor soccer shoes" -- validated 200, H1 "Indoor Soccer Shoes for Men and Women", 53 products
- https://www.prosoccer.com/products/nike-tiempo-maestro-club-turf-soccer-shoes-shadow-pack-fa26 -- anchor "turf version" -- validated 200 (trio sibling; surface choice)

DO NOT link `/collections/indoor-soccer-shoes`: H1 is "Kids' Indoor Soccer Shoes", a youth collection, wrong audience.

Place 2 links in different H2 sections.

## Differentiation lane (write prose FROM this)
- Angle: the one shoe in the trio that goes where the game goes, court to street to gym, not just one pitch.
- Opening hook: the game that carries on after practice, on whatever flat surface is available.
- Primary metaphor: versatility across hard flat surfaces. This is the lane the scrape hands us and neither sibling can use it, because neither page names street or court.
- Facet vs siblings: INDOOR, rubber outsole, street and court and indoor. IB1602 is FG/MG studs. IB4482 is turf.

## Structure skeleton (mirror STRUCTURE, never prose)
- H2 sequence: identity hook -> the flat rubber outsole across surfaces -> use-case (indoor, court, street) -> Product Details: -> Fit Notes -> Care and Maintenance -> FAQs about
- Short Description 50-100 words; Description 340-390 (tol 15); FAQ 3 Q&A
- Product Details bullets: upper, outsole + surfaces, sockliner, colorway

## Forbidden phrasings (barred by IB1602 and IB4482)
- Verbatim: ["settles instead of bounces", "a price a club family can say yes to", "softness on a hard surface"]
- Motifs: ["soft touch and control", "leather-feel heritage", "the first touch that settles", "forgiving upper on an unforgiving surface"]
- Title-frames: ["A touch-first cleat for the club player"]

<!-- gate-meta authoritative; batch_gate.py parses it. -->
```gate-meta
{
  "sku": "IB4486",
  "brand": "nike",
  "brand_ip_posture": "cycle-language-only",
  "tier": "club",
  "word_band": [340, 390],
  "word_band_tolerance": 15,
  "primary_keyword": "nike tiempo maestro club indoor",
  "forbidden_phrasings": {
    "verbatim": ["settles instead of bounces", "a price a club family can say yes to", "softness on a hard surface"],
    "motifs": ["soft touch and control", "leather-feel heritage", "the first touch that settles", "forgiving upper on an unforgiving surface"],
    "title_frames": ["A touch-first cleat for the club player"]
  }
}
```
