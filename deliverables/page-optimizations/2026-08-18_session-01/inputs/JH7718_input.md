# Input: JH7718 -- adidas F50 League Indoor Soccer Shoes - Coral Blaze Pack (FA25)

_v2 pre-dispatch input. Work from THIS FILE ONLY. Do not read sibling briefs; the differentiation lane below is what keeps this page distinct._

## Identity
- SKU: JH7718
- URL: https://www.prosoccer.com/products/adidas-f50-league-indoor-soccer-shoes-coral-blaze-pack-fa25
- Handle: `adidas-f50-league-indoor-soccer-shoes-coral-blaze-pack-fa25`
- Brand: adidas
- Brand-IP posture: cycle-language-only. **No FIFA or World Cup language anywhere on this page.**
- Product category: footwear, SHOES (say "shoes", never the UK term)
- Care H2 required: yes
- Tier: league
- Avatar: Mike, the coach
- Word band: 280-340 (+/-15 tolerance). This is THIS SKU's own tier band. Never inherit a band from an exemplar.

## Phase 0 scrape data (source of truth; scrape-wins, fetched live 2026-08-18)
- Live H1: adidas F50 League Indoor Soccer Shoes - Coral Blaze Pack (FA25)
- Price: $54.00 to $90.00 -- **KEEP OUT of body copy.**
- Stock: 10 of 30 variants in stock (context only, never stated in copy)
- Live meta description: the theme's body-derived fallback. This page has never been optimized.
- In-body internal links currently on the page: **0**. The gate hard-fails a body with no internal link.
- Weight: NOT STATED on the live page. Do not state one.
- Source copy, verbatim, and it is the ONLY sourceable spec material:
  - adidas F50 League Indoor Soccer Shoes - Coral Blaze Pack (FA25)
  - Lightweight boots for all-out pace on flat indoor surfaces.
  - Fiberskin upper with suede toe bumper
  - Non-marking rubber outsole for indoor surfaces

## Keywords (validated by ORIN, do NOT re-derive)
| Type | Keyword | Volume |
|---|---|---|
| Primary | adidas f50 league indoor coral blaze | no measurable volume (DFS both endpoints, 2026-08-18). Sub-floor by design. |

## Meta fields (ORIN-set; use the title EXACTLY)
- Meta Title: `adidas F50 League Indoor Coral Blaze` (36 chars, under the 48 cap)
- Meta Description: write it. 120 to 160 characters, full sentences, no "Product Name: fragment" colon opener, product-anchored call to action. Never end the title or description with a manufacturer brand as a pipe suffix.

## Validated internal links (ORIN link-check 2026-08-18, live H1 + product count verified; body only)
- https://www.prosoccer.com/collections/adidas-f50 -- anchor "adidas F50 range" -- validated live 2026-08-18: H1 "Adidas F50 Soccer Cleats for Men, Women, You...", 45 products
- https://www.prosoccer.com/collections/adidas-indoor-soccer-shoes -- anchor "adidas indoor shoes" -- validated live 2026-08-18: H1 "Adidas Indoor Soccer Shoes for Indoor Courts", 29 products

Place the 2 links in DIFFERENT H2 sections. Append a transition sentence after a section's closing line rather than rewriting the closing line to fit the link.

## Differentiation lane (write prose FROM this, never from a sibling)
- Angle: the dependable indoor shoe for a squad: a coach-facing take on kit that survives a winter season
- Opening hook: the indoor block-booking where half the squad turns up in running shoes
- Primary metaphor: reliability and season-long wear. Do NOT lead on speed or court grip, that is row 3.
- Use-case: indoor courts, futsal, team winter training
- Facet vs siblings: Coral Blaze FA25 colorway. Row 3 is Born For Goals SP26 and holds the unqualified term.

## Structure skeleton (Mechanism A; mirror STRUCTURE, never prose)
- H2 sequence: identity hook -> build and materials -> surface use-case -> Product Details: -> Fit Notes -> Care and Maintenance -> FAQs about adidas F50 League Indoor Soccer Shoes
- Short Description 50-100 words; Description 280-340 words (tolerance 15); FAQ 3 Q&A
- Product Details bullets: upper, outsole or plate + surface, feel or fit, colorway
- The word band counts the FULL body including the FAQ section. Draft to land inside the band on the first pass; do not write long and trim.

## Standing rules that the gate enforces
- No em dashes anywhere. Use commas, colons, parentheses or separate sentences.
- adidas is always lowercase, including at the start of a sentence. Nike and Mizuno are capitalized.
- Brand TECHNOLOGY names in title case: Gripknit, Primeknit, Nanostrike+, Powerspine, Strikeframe, Atomknit, Flyknit, FlyLite, NikeSkin, VNMSkin, Fiberskin, Techleather. Never all caps.
- No price, no stock state, no size runs, no store call to action in the body.
- Every spec or heritage claim must trace to the scrape block above. No bare PASS, no invented weight, no invented heritage count.
- Customization and shipping: name and number customization is selected ON THE PRODUCT PAGE, never "at checkout", and adds 2 to 3 BUSINESS DAYS, never weeks. Most of these are footwear, where customization does not apply; if you do not need the claim, do not make it.

**Thin source copy: 205 characters, 4 lines, the least of the ten.** The page states only: Fiberskin upper with suede toe bumper, non-marking rubber outsole for indoor surfaces, and lightweight boots for all-out pace on flat indoor surfaces. **Do not invent specs to fill the band.** Where you need material, use the adidas F50 League INDOOR platform facts that row 3 also carries (Fiberskin upper, EVA midsole, indoor-specific non-marking outsole, textile sockliner, suede toe bumper) since it is the same shoe at a different colorway, and say nothing that is not on one of those two pages.
- The source copy uses the UK term for cleats. Write shoes.

## Forbidden phrasings (three tiers; the gate matches verbatim and title-frame by substring)
- Verbatim (never use this exact string): []
- Motifs (never build the piece around this idea, it belongs to a sibling): ['speed and court grip']
- Title-frames (never open with this shape): ['the quick first step on a gym floor wher...']

<!-- gate-meta authoritative; batch_gate.py parses it. -->
```gate-meta
{
  "sku": "JH7718",
  "brand": "adidas",
  "brand_ip_posture": "cycle-language-only",
  "tier": "league",
  "word_band": [
    280,
    340
  ],
  "word_band_tolerance": 15,
  "primary_keyword": "adidas f50 league indoor coral blaze",
  "forbidden_phrasings": {
    "verbatim": [],
    "motifs": [
      "speed and court grip"
    ],
    "title_frames": [
      "the quick first step on a gym floor wher..."
    ]
  }
}
```
