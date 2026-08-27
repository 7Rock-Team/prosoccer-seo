# Input: IH2115 -- adidas Predator Club Turf Soccer Shoes - Chaos Vs Control Pack (FA26)

_v2 pre-dispatch input. Work from THIS FILE ONLY. Do not read sibling briefs; the differentiation lane below is what keeps this page distinct._

```gate-meta
{
  "sku": "IH2115",
  "brand": "adidas",
  "brand_ip_posture": "cycle-language-only",
  "tier": "club",
  "word_band": [
    280,
    340
  ],
  "word_band_tolerance": 15,
  "primary_keyword": "adidas predator club turf",
  "forbidden_phrasings": {
    "verbatim": [
      "Nanostrike",
      "Strikeframe",
      "Powerspine",
      "leather conditioner"
    ],
    "motifs": [
      "premium striking technology as the point of the shoe",
      "speed as the point of the shoe",
      "the indoor court as this shoe's surface"
    ],
    "title_frames": [
      "the strike that beats the keeper from..."
    ]
  }
}
```

## Identity
- SKU: IH2115
- URL: https://www.prosoccer.com/products/adidas-predator-club-turf-soccer-shoes-chaos-vs-control-pack
- Handle: `adidas-predator-club-turf-soccer-shoes-chaos-vs-control-pack`
- Brand: adidas
- Brand-IP posture: cycle-language-only. **No FIFA or World Cup language anywhere on this page.** adidas holds an event-scoped 2026 World Cup licence only; this is a Chaos vs Control pack release, NOT a World Cup product, so the licence does not reach it.
- Product category: footwear, TURF SHOES (say "shoes", never "cleats", never "boots")
- Care H2 required: yes
- Tier: club
- Avatar: the budget-aware adult rec player on artificial surfaces
- Word band: 280-340 (+/-15 tolerance). This is THIS SKU's own band. Never inherit a band from an exemplar.

## Phase 0 scrape data (source of truth; scrape-wins, fetched live 2026-08-26, no cache)
- Live H1 and product title: adidas Predator Club Turf Soccer Shoes - Chaos Vs Control Pack (FA26)
- Price: $64.99 -- **KEEP OUT of body copy.**
- Stock: **NOT RELIABLY DETERMINABLE.** The size grid renders every option as unavailable to a non-JS fetch, which is a rendering artifact, not real stock. **Make no availability claim of any kind.**
- Size run: M 4 / W 5 through M 13 / W 14 (adult unisex, 15 options) (context only, never stated in copy)
- Live meta description: **already non-default:** "The adidas Predator Club Turf Soccer Shoes are designed for comfort and grip on turf, ensuring you perform at your best." That is 113 characters, BELOW the 120 minimum, and it is not ours. Replace it.
- Editorial in-body internal links currently on the page: **0.** (The page carries theme boilerplate links only: shipping policy, Get in Touch, and similar. Those are not editorial body links.) The gate hard-fails a body with no internal link.
- Weight: **271 g. Render US-first as 9.6 oz (271 g).**
- Source copy, verbatim, and it is the ONLY sourceable spec material:
  - The soft synthetic upper delivers high-level comfort and features an innovative textured finish for extra grip, supporting your moves as you drive play forward.
  - A laced floating tongue offers easy step-in and adjustability, so you can focus on the game. The regular fit helps you feel locked in, while the rubber outsole is made for reliable traction on turf, allowing you to stay agile and responsive.
  - Regular fit
  - Lace closure
  - Synthetic upper
  - Textile sockliner
  - Rubber outsole
  - Laced floating tongue
  - Weight: 271 g

## Keywords (validated by ORIN, do NOT re-derive)
| Type | Keyword | Volume |
|---|---|---|
| Primary | adidas predator club turf | 20/mo (DFS Labs, 2026-08-26; NO Google Ads row). Below the volume floor, held deliberately for surface uniqueness. |

**Targeting basis:** **Unqualified, and correctly so.** No concurrent live pack sibling exists at Predator / Club / Turf / ADULT. The four other live Predator Club Turf pages (Ice Cold Precision, Born for Goals, Coral Blaze FA25, Electric Stealth FA25) are all KIDS pages, and age band is part of the configuration tuple, so they are not siblings. The term is below floor but held for surface uniqueness, with an exact precedent in IH7212 (`adidas predator league turf`, 90/mo, same rationale). Its containment against HQ2273's `adidas predator club` is the accepted surface-narrowing pattern, parallel to IH7212 against JP6271.

## Meta fields (ORIN-set; use the title EXACTLY)
- Meta Title: `adidas Predator Club Turf Soccer Shoes` (38 chars, under the 48 cap)
- Meta Description: write it. 120 to 160 characters, full sentences, no "Product Name: fragment" colon opener, product-anchored call to action. Never end the title or description with a manufacturer brand as a pipe suffix. **The description must name the Chaos vs Control pack**, since the pack was dropped from the title. Note the existing live description is 113 chars, under the 120 floor; yours must land in 120-160.

## Validated internal links (ORIN link-check 2026-08-26, live H1 + product count verified; body only)
- https://www.prosoccer.com/collections/adidas-predator -- anchor "adidas Predator range" -- validated live 2026-08-26: H1 "Adidas Predator Soccer Cleats for Men, Women, Youth", 104 products
- https://www.prosoccer.com/collections/artificial-turf -- anchor "turf soccer shoes" -- validated live 2026-08-26: H1 "Turf Soccer Shoes for Men and Women", 108 products

Place the 2 links in DIFFERENT H2 sections. Append a transition sentence after a section's closing line rather than rewriting the closing line to fit the link.

## Claims bar (hard constraints)
- adidas always lowercase. "cleats" or "shoes", never "boots". No em dashes.
- Predator identity is CONTROL and PRECISION, never speed. No F50 speed vocabulary.
- Every spec claim must trace to the verbatim source block above. No bare PASS, no invented specs.
- **Say "shoes", never "cleats".** Turf outsole, no studs.
- This is the CLUB tier: the entry tier. No Nanostrike, no Strikeframe, no Powerspine. **None of those appear in the source block and none may appear in the copy.** The upper is a plain synthetic with a textured finish.
- **Synthetic-leather care guard:** the upper is synthetic, not leather. Care copy must not recommend leather conditioner or leather food.

## Differentiation lane (write prose FROM this, never from a sibling)
- Angle: the surface-specific shoe most rec players actually need, at the entry price
- Opening hook: the player whose league moved to an artificial pitch
- Primary metaphor: grip and comfort over many touches on an unforgiving surface
- Use-case: artificial turf, small-sided and rec league, frequent play
- Facet vs siblings: **the batch's only Club tier and its only turf outsole.** This row must NOT borrow the striking-technology story from the League, Pro or indoor rows: it has none of that hardware. Its story is the textured upper, the laced floating tongue and turf traction. Contrast with the indoor row: that one is a flat court shoe, this one is a turf pattern for outdoor artificial grass.

## Structure skeleton (mirror STRUCTURE, never prose)
- H2 sequence: identity hook -> textured synthetic upper and comfort -> laced floating tongue and lockdown -> turf outsole and the artificial-surface use-case -> Product Details: -> Fit Notes -> Care and Maintenance -> FAQs about adidas Predator Club Turf Soccer Shoes
