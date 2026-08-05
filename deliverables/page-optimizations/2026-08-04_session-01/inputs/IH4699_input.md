# Input: IH4699 -- adidas Predator Elite Firm Ground Soccer Cleats (Chaos Vs Control Pack, FA26)

_v2 pre-dispatch input. SCRIBE reads this and works from it; do NOT re-scrape, re-look-up keywords, or re-validate links (ORIN owns all three). This is the Predator-trio EXEMPLAR: its structure and voice anchor JP6248 and IH4707, which mirror STRUCTURE only and take their own lanes._

## Identity
- SKU: IH4699
- URL: https://www.prosoccer.com/products/adidas-predator-elite-firm-ground-soccer-cleats-chaos-vs-control
- Handle: adidas-predator-elite-firm-ground-soccer-cleats-chaos-vs-control
- Brand: adidas (always lowercase in prose)
- Brand-IP posture: cycle-language-only (NO FIFA / World Cup language. adidas holds only an event-scoped 2026 WC license; this is a Chaos vs Control pack cleat, not a WC product, so the license is not invoked.)
- Product category: footwear
- Care H2 required: yes
- Tier: elite
- Word band: 400-450 (+/-15 tolerance). SKU-specific.

## Phase 0 scrape data (source of truth; scrape-wins)
- Colorway: Cloud White / Solar Turbo / Core Black
- Upper / materials: synthetic and textile; Nanostrike+ mesh with integrated rubber grip elements
- Tongue / fit: STANDARD tongue, regular fit, lace closure (this is the standard-tongue Elite; the fold-over-tongue version is a separate SKU/sibling)
- Plate / surface: firm ground; synthetic outsole; full-length lightweight plate; non-removable studs
- Weight: 6.9 oz (195 g)
- Price: $259.99 -- KEEP OUT of body copy (tier/positioning language only)
- Key tech (scrape): Nanostrike+ (featherlight, soft feel with rubber grip for striking precision); Powerspine (midfoot stability); full-length lightweight plate (traction); non-removable studs (grip)
- Care material: synthetic upper (no leather conditioner; wipe clean)
- Sibling variants (this batch, cross-link): JP6248 fold-over tongue FG; IH4707 fold-over tongue AG

## Keywords (from KIRA/ORIN; validated, do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | adidas predator elite fg chaos vs control | no measurable volume (DFS both endpoints, 2026-08-04) | |
| Secondary (pack) | chaos vs control | 50 | |
| Topical context ONLY (collection-owned, do NOT target as a ranking term) | adidas predator elite | 9900 | KD 2 |

Sub-floor by design: the unqualified `adidas predator elite fg` (1,000/mo) belongs to the earliest live standard-tongue FG incumbent, not this page. Do not target it. Body may reference "Predator Elite" and named techs as natural brand/model context.

## Validated internal links (ORIN link-check; do NOT re-validate; body only, never Short Description)
- https://www.prosoccer.com/products/adidas-predator-elite-fo-tongue-fg-soccer-cleats-chaos-vs-control -- anchor "Predator Elite Fold-Over Tongue" -- validated 200, live purchasable (sibling; helps the buyer choose tongue construction)
- https://www.prosoccer.com/collections/adidas-predator -- anchor "adidas Predator soccer cleats" -- validated 200, H1 "Adidas Predator Soccer Cleats for Men, Women, Youth"
- (optional third if it reads naturally) https://www.prosoccer.com/products/adidas-predator-elite-fo-tongue-ag-soccer-cleats-chaos-vs-control -- anchor "artificial-grass version" -- validated 200 (sibling; surface choice)

Place 2 links naturally in different H2 sections (tongue-choice sibling in a fit/construction context; model collection in a positioning context). Do not stack both in one H2.

## Differentiation lane (write prose FROM this, not from any sibling)
- Angle: the deep-lying creator's control cleat; the player who dictates tempo and strikes with the standard tongue's clean, familiar feel.
- Opening hook: the moment a controlled player sets the pace on firm natural grass.
- Primary metaphor: control and tempo (conducting the game from deep). Keep this lane; siblings will bar it.
- Use-case: firm natural grass, set pieces, the passer/striker who shapes play.
- Positioning: Predator's grip-and-strike heritage via Nanostrike+; standard tongue for the traditionalist.
- Facet vs siblings: STANDARD tongue + FG (JP6248 = fold-over tongue FG; IH4707 = fold-over tongue AG).

## Structure skeleton (Mechanism A; mirror STRUCTURE, never prose)
- H2 sequence: overview / identity hook -> control-and-tempo positioning -> use-case (firm grass, the creator) -> Product Details: -> Fit Notes -> Care and Maintenance -> FAQs about
- Field-length targets: Short Description 50-100 words; Description 400-450 (tol 15); FAQ 3-4 Q&A (net-new value only)
- Product Details bullet categories: upper/materials, plate + studs (surface), tier tech (Nanostrike+, Powerspine), weight, care material

## Forbidden phrasings (exemplar; none barred yet -- this brief SETS the lane the siblings must avoid)
- Verbatim: []
- Motifs: []
- Title-frames: []

<!-- gate-meta authoritative; batch_gate.py parses it. adidas lowercase caught by voice_check; not listed here. -->
```gate-meta
{
  "sku": "IH4699",
  "brand": "adidas",
  "brand_ip_posture": "cycle-language-only",
  "tier": "elite",
  "word_band": [400, 450],
  "word_band_tolerance": 15,
  "primary_keyword": "adidas predator elite fg chaos vs control",
  "forbidden_phrasings": {
    "verbatim": [],
    "motifs": [],
    "title_frames": []
  }
}
```
