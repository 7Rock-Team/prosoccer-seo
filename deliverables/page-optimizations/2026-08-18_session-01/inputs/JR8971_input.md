# Input: JR8971 -- adidas F50 League Indoor Soccer Shoes - Born For Goals Pack (SP26)

_v2 pre-dispatch input. Work from THIS FILE ONLY. Do not read sibling briefs; the differentiation lane below is what keeps this page distinct._

## Identity
- SKU: JR8971
- URL: https://www.prosoccer.com/products/adidas-f50-league-indoor-soccer-shoes-born-for-goals-pack-sp26
- Handle: `adidas-f50-league-indoor-soccer-shoes-born-for-goals-pack-sp26`
- Brand: adidas
- Brand-IP posture: cycle-language-only. **No FIFA or World Cup language anywhere on this page.**
- Product category: footwear, SHOES (say "shoes", never the UK term)
- Care H2 required: yes
- Tier: league
- Avatar: Jennifer, the parent-buyer
- Word band: 280-340 (+/-15 tolerance). This is THIS SKU's own tier band. Never inherit a band from an exemplar.

## Phase 0 scrape data (source of truth; scrape-wins, fetched live 2026-08-18)
- Live H1: adidas F50 League Indoor Soccer Shoes - Born For Goals Pack (SP26)
- Price: $68.00 to $90.00 -- **KEEP OUT of body copy.**
- Stock: 24 of 28 variants in stock (context only, never stated in copy)
- Live meta description: the theme's body-derived fallback. This page has never been optimized.
- In-body internal links currently on the page: **0**. The gate hard-fails a body with no internal link.
- Weight: NOT STATED on the live page. Do not state one.
- Source copy, verbatim, and it is the ONLY sourceable spec material:
  - adidas F50 League Indoor Soccer Shoes - Born For Goals Pack (SP26)
  - Indoor shoes with non-marking rubber outsole for controlled play.
  - The Fiberskin Upper, featuring strategically placed 3D lines, aids ball touch and visual appeal. The lightweight EVA midsole enhances comfort, allowing you to focus on your match without distractions.
  - Synthetic and textile upper
  - Textile sockliner
  - Indoor-specific non-marking outsole
  - Lightweight EVA midsole
  - Suede toe bumper

## Keywords (validated by ORIN, do NOT re-derive)
| Type | Keyword | Volume |
|---|---|---|
| Primary | adidas f50 league indoor | 30 (DFS US 2026-08-18; 70 in July) |

## Meta fields (ORIN-set; use the title EXACTLY)
- Meta Title: `adidas F50 League Indoor Born For Goals` (39 chars, under the 48 cap)
- Meta Description: write it. 120 to 160 characters, full sentences, no "Product Name: fragment" colon opener, product-anchored call to action. Never end the title or description with a manufacturer brand as a pipe suffix.

## Validated internal links (ORIN link-check 2026-08-18, live H1 + product count verified; body only)
- https://www.prosoccer.com/collections/adidas-f50 -- anchor "adidas F50 range" -- validated live 2026-08-18: H1 "Adidas F50 Soccer Cleats for Men, Women, You...", 45 products
- https://www.prosoccer.com/collections/indoor -- anchor "indoor soccer shoes" -- validated live 2026-08-18: H1 "Indoor Soccer Shoes for Men and Women", 29 products. NOTE: this is the ADULT target; /collections/indoor-soccer-shoes is the KIDS page, do not use it

Place the 2 links in DIFFERENT H2 sections. Append a transition sentence after a section's closing line rather than rewriting the closing line to fit the link.

## Differentiation lane (write prose FROM this, never from a sibling)
- Angle: the indoor speed shoe a family can say yes to: F50 pace translated to a flat court
- Opening hook: the quick first step on a gym floor where grip decides everything
- Primary metaphor: speed and court grip. BARRED to row 9.
- Use-case: indoor courts, futsal, winter training
- Facet vs siblings: Born For Goals SP26 colorway. Row 9 is the Coral Blaze FA25 at the same configuration and takes the pack-qualified term.

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

## Forbidden phrasings (three tiers; the gate matches verbatim and title-frame by substring)
- Verbatim (never use this exact string): []
- Motifs (never build the piece around this idea, it belongs to a sibling): ['reliability and season-long wear']
- Title-frames (never open with this shape): ['the indoor block-booking where half the ...']

<!-- gate-meta authoritative; batch_gate.py parses it. -->
```gate-meta
{
  "sku": "JR8971",
  "brand": "adidas",
  "brand_ip_posture": "cycle-language-only",
  "tier": "league",
  "word_band": [
    280,
    340
  ],
  "word_band_tolerance": 15,
  "primary_keyword": "adidas f50 league indoor",
  "forbidden_phrasings": {
    "verbatim": [],
    "motifs": [
      "reliability and season-long wear"
    ],
    "title_frames": [
      "the indoor block-booking where half the ..."
    ]
  }
}
```
