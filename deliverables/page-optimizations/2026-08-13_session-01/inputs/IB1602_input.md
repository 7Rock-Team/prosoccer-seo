# Input: IB1602 -- Nike Tiempo Maestro Club Firm/Multi Ground Soccer Cleats (Shadow Pack, FA26)

_v2 pre-dispatch input. Work from this file only. This is the TIEMPO MAESTRO CLUB TRIO ANCHOR: its structure and voice anchor IB4482 and IB4486, which mirror STRUCTURE only and take their own lanes._

## Identity
- SKU: IB1602-001
- URL: https://www.prosoccer.com/products/nike-tiempo-maestro-club-fg-mg-soccer-cleats-shadow-fa26
- Brand: Nike (capitalized)
- Brand-IP posture: cycle-language-only. **Nike holds NO FIFA license. No FIFA or World Cup language anywhere.**
- Product category: footwear, CLEATS (says "cleats", never "shoes")
- Care H2 required: yes
- Tier: club
- Avatar: Jennifer, the parent-buyer.
- Word band: 340-390 (+/-15 tolerance).

## Phase 0 scrape data (source of truth; scrape-wins)
- Live title: Nike Tiempo Maestro Club Firm/Multi Ground Soccer Cleats - Shadow Pack (FA26)
- Colorway: Black/Black/Illusion Green
- Upper: synthetic leather. Page states it "helps provide a consistent touch in wet or dry conditions" and "molds to your foot and gives you better control"
- Plate: bladed and conical studs, traction on artificial and natural grass
- Weight: NOT STATED. Do not state one.
- Price: $64.99 -- KEEP OUT of body copy.
- Care material: synthetic upper, so no leather conditioner. The upper is synthetic LEATHER; do not treat it as real leather in care copy.

## Keywords (validated, do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | nike tiempo maestro club fg mg shadow | no measurable volume (DFS both endpoints, 2026-08-13) | |
| Secondary (pack) | nike shadow pack | 140 | |
| Topical context ONLY (Academy tier, do NOT target) | nike tiempo maestro academy fg mg | 10 (IB1600) | |

Pack-qualified because a live Break 'Em FA26 sibling exists at this exact config. **NO SEASON CODE.** Shadow exists at the Tiempo Maestro Club tier only in FA26; the SP26 Shadow pages are Academy tier, a different configuration. This is why IB4484 (Batch 13, Academy Turf) carries `fa26` and this one does not.

## Meta fields (ORIN-set; use exactly)
- Meta Title: `Nike Tiempo Maestro Club FG/MG Shadow` (37 chars)
- Meta Description: 120-160 chars, full sentences, no colon-fragment opener, product-anchored CTA.

## Validated internal links (ORIN link-check 2026-08-13; body only)
- https://www.prosoccer.com/collections/nike-tiempo-maestro -- anchor "Nike Tiempo Maestro cleats" -- validated live, in refreshed sitemap
- https://www.prosoccer.com/products/nike-tiempo-maestro-club-turf-soccer-shoes-shadow-pack-fa26 -- anchor "turf version" -- validated 200, H1 "Nike Tiempo Maestro Club Turf Soccer Shoes - Shadow Pack (FA26)" (trio sibling; surface choice)

Place 2 links in different H2 sections.

## Differentiation lane (write prose FROM this, not from any sibling)
- Angle: the touch-first cleat at a price a club family can say yes to; Tiempo's leather-feel heritage in the entry tier.
- Opening hook: the first touch that settles instead of bounces, on the grass pitch the team actually plays on.
- Primary metaphor: soft touch and control. Keep this lane; the trio siblings will bar it.
- Use-case: natural grass and mixed pitches, weekend club matches.
- Facet vs siblings: FG/MG with bladed and conical studs. IB4482 is turf with a rubber outsole. IB4486 is indoor.

## Structure skeleton (Mechanism A; mirror STRUCTURE, never prose)
- H2 sequence: identity hook -> the synthetic-leather touch -> surface use-case (FG/MG) -> Product Details: -> Fit Notes -> Care and Maintenance -> FAQs about
- Short Description 50-100 words; Description 340-390 (tol 15); FAQ 3 Q&A
- Product Details bullets: upper, plate + stud shape + surface, feel, colorway

## Forbidden phrasings (trio anchor; none barred yet -- this brief SETS the lane)
- Verbatim: []
- Motifs: []
- Title-frames: []

<!-- gate-meta authoritative; batch_gate.py parses it. -->
```gate-meta
{
  "sku": "IB1602",
  "brand": "nike",
  "brand_ip_posture": "cycle-language-only",
  "tier": "club",
  "word_band": [340, 390],
  "word_band_tolerance": 15,
  "primary_keyword": "nike tiempo maestro club fg mg shadow",
  "forbidden_phrasings": {
    "verbatim": [],
    "motifs": [],
    "title_frames": []
  }
}
```
