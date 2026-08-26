# Input: KK1341 -- adidas Kids F50 Hyperfast Club Indoor Soccer Shoes - Chaos Vs Control Pack (FA26)

_v2 pre-dispatch input. Work from THIS FILE ONLY. Do not read sibling briefs; the differentiation lane below is what keeps this page distinct._

## Identity
- SKU: KK1341
- URL: https://www.prosoccer.com/products/adidas-kids-f50-hyperfast-club-in-soccer-shoes-chaos-vs-control
- Handle: `adidas-kids-f50-hyperfast-club-in-soccer-shoes-chaos-vs-control`
- Brand: adidas
- Brand-IP posture: cycle-language-only. **No FIFA or World Cup language anywhere on this page.**
- Product category: footwear, SHOES (say "shoes", never the UK term)
- Care H2 required: yes
- Tier: club
- Avatar: Jennifer, the mom (parent-buyer)
- Word band: 280-340 (+/-15 tolerance). This is THIS SKU's own tier band. Never inherit a band from an exemplar.

## Phase 0 scrape data (source of truth; scrape-wins, fetched live 2026-08-25)
- Live H1 and product title: adidas Kids F50 Hyperfast Club Indoor Soccer Shoes - Chaos Vs Control Pack (FA26)
- Price: $49.99 -- **KEEP OUT of body copy.**
- Stock: 7 of 7 variants in stock
- Size run: Kids 10.5K to 13.5K (context only, never stated in copy)
- Live meta description: the theme's body-derived fallback. This page has never been optimized.
- In-body internal links currently on the page: **0**. The gate hard-fails a body with no internal link.
- Weight: 222 g, stated on the live page. You may use it.
- Source copy, verbatim, and it is the ONLY sourceable spec material:
  - The lightweight floating tongue brings comfort on the move and a classic lace closure lets them dial in the optimum level of lockdown for their game.
  - Regular fit
  - Laces
  - Synthetic upper
  - Textile lining
  - Non-marking rubber outsole for indoor courts
  - Lightweight floating tongue
  - Weight: 222 g

## Keywords (validated by ORIN, do NOT re-derive)
| Type | Keyword | Volume |
|---|---|---|
| Primary | adidas kids f50 club indoor | no measurable volume (DFS Google Ads + Labs, 2026-08-25). Age-qualified configuration term, sub-floor by design. |

**Targeting basis:** Unqualified. No live pack sibling at Kids F50 Hyperfast Club Indoor.

## Meta fields (ORIN-set; use the title EXACTLY)
- Meta Title: `adidas Kids F50 Club Indoor Shoes` (33 chars, under the 48 cap)
- Meta Description: write it. 120 to 160 characters, full sentences, no "Product Name: fragment" colon opener, product-anchored call to action. Never end the title or description with a manufacturer brand as a pipe suffix.

## Validated internal links (ORIN link-check 2026-08-25, live H1 + product count verified; body only)
- https://www.prosoccer.com/collections/indoor-soccer-shoes -- anchor "kids' indoor soccer shoes" -- validated live 2026-08-25: H1 "Kids' Indoor Soccer Shoes", 32 products
- https://www.prosoccer.com/collections/adidas-f50 -- anchor "adidas F50 range" -- validated live 2026-08-25: H1 "Adidas F50 Soccer Cleats for Men, Women, Youth", 112 products

Place the 2 links in DIFFERENT H2 sections. Append a transition sentence after a section's closing line rather than rewriting the closing line to fit the link.

## Differentiation lane (write prose FROM this, never from a sibling)
- Angle: a first indoor pair for the smallest feet in the club: the shoe that makes a gym floor feel normal
- Opening hook: the youngest age group's first indoor session, all stopping and starting on a polished floor
- Primary metaphor: settled footing for a beginner. Keep it smaller in scale than row 1: this is the youngest kids Club shoe, not the junior League one
- Use-case: indoor courts, school gyms, the youngest futsal and winter sessions
- Facet vs siblings: Kids 10.5K to 13.5K at the Club tier. Row 1 (KK1326) is the JUNIOR League indoor shoe and owns the winter-season framing.

## Structure skeleton (Mechanism A; mirror STRUCTURE, never prose)
- H2 sequence: identity hook -> tongue and lockdown -> indoor surface use-case -> Product Details: -> Fit Notes -> Care and Maintenance -> FAQs about adidas Kids F50 Club Indoor Soccer Shoes
- Short Description 50-100 words; Description 280-340 words (tolerance 15); FAQ 3 Q&A
- Product Details bullets: upper, outsole or plate + surface, feel or fit, colorway
- The word band counts the FULL body including the FAQ section. Draft to land inside the band on the first pass; do not write long and trim.

## Standing rules that the gate enforces
- No em dashes anywhere. Use commas, colons, parentheses or separate sentences.
- adidas is always lowercase, including at the start of a sentence.
- Brand TECHNOLOGY names in title case, never all caps: Haloskin, Haloskin+, Haloshell+, Sprintgrid, Sprintweb, Sprintframe Fusion, Sprintplate Fusion, Fusionlast, Primeknit, Nanostrike, Powerspine, Strikeframe. The live page renders several in all caps; write them in title case.
- No price, no stock state, no size runs, no store call to action in the body.
- Every spec or heritage claim must trace to the scrape block above. No bare PASS, no invented weight, no invented heritage count.
- Customization and shipping: name and number customization is selected ON THE PRODUCT PAGE, never "at checkout", and adds 2 to 3 BUSINESS DAYS, never weeks. This is footwear, where name/number customization does not apply. Do not make the claim at all.
- Non-adidas products never use FIFA or World Cup language. This is adidas, but the posture here is cycle-language-only regardless: no FIFA or World Cup language anywhere on this page.

## SKU-specific notes
Source copy is 381 characters across 9 lines, the thinnest of the kids rows. It names the floating tongue, the lace closure, the synthetic upper, the textile lining, the indoor non-marking outsole and 222 g. That is the whole sourceable set. Do not invent a midsole, a plate or a colourway.

## Forbidden phrasings (three tiers; the gate matches verbatim and title-frame by substring)
- Verbatim (never use this exact string): []
- Motifs (never build the piece around this idea, it belongs to a sibling): ['the winter move onto a gym floor', 'getting themselves ready without help', 'the turf-home everyday pitch']
- Title-frames (never open with this shape): ['the first indoor session of the winter...']

<!-- gate-meta authoritative; batch_gate.py parses it. -->
```gate-meta
{
  "sku": "KK1341",
  "brand": "adidas",
  "brand_ip_posture": "cycle-language-only",
  "tier": "club",
  "word_band": [
    280,
    340
  ],
  "word_band_tolerance": 15,
  "primary_keyword": "adidas kids f50 club indoor",
  "forbidden_phrasings": {
    "verbatim": [],
    "motifs": [
      "the winter move onto a gym floor",
      "getting themselves ready without help",
      "the turf-home everyday pitch"
    ],
    "title_frames": [
      "the first indoor session of the winter..."
    ]
  }
}
```
