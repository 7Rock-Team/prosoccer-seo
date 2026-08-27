# Input: IH7154 -- adidas Predator League Firm Ground Soccer Cleats - Chaos Vs Control Pack (FA26)

_v2 pre-dispatch input. Work from THIS FILE ONLY. Do not read sibling briefs; the differentiation lane below is what keeps this page distinct._

```gate-meta
{
  "sku": "IH7154",
  "brand": "adidas",
  "brand_ip_posture": "cycle-language-only",
  "tier": "league",
  "word_band": [
    280,
    340
  ],
  "word_band_tolerance": 15,
  "primary_keyword": "adidas predator league fg chaos vs control",
  "forbidden_phrasings": {
    "verbatim": [
      "Nanostrike+"
    ],
    "motifs": [
      "the fold-over tongue as this shoe's striking surface",
      "speed as the point of the shoe",
      "court or turf as this shoe's surface"
    ],
    "title_frames": [
      "the strike that beats the keeper from..."
    ]
  }
}
```

## Identity
- SKU: IH7154
- URL: https://www.prosoccer.com/products/adidas-predator-league-fg-soccer-cleats-chaos-vs-control-pack
- Handle: `adidas-predator-league-fg-soccer-cleats-chaos-vs-control-pack`
- Brand: adidas
- Brand-IP posture: cycle-language-only. **No FIFA or World Cup language anywhere on this page.** adidas holds an event-scoped 2026 World Cup licence only; this is a Chaos vs Control pack release, NOT a World Cup product, so the licence does not reach it.
- Product category: footwear, CLEATS (say "cleats", never the UK term)
- Care H2 required: yes
- Tier: league
- Avatar: the committed amateur who plays weekly on grass; value-conscious but spec-aware
- Word band: 280-340 (+/-15 tolerance). This is THIS SKU's own band. Never inherit a band from an exemplar.

## Phase 0 scrape data (source of truth; scrape-wins, fetched live 2026-08-26, no cache)
- Live H1 and product title: adidas Predator League Firm Ground Soccer Cleats - Chaos Vs Control Pack (FA26)
- Price: $89.99 -- **KEEP OUT of body copy.**
- Stock: **NOT RELIABLY DETERMINABLE.** The size grid renders every option as unavailable to a non-JS fetch, which is a rendering artifact, not real stock. **Make no availability claim of any kind.**
- Size run: M 4 / W 5 through M 13 / W 14 (adult unisex, 18 options) (context only, never stated in copy)
- Live meta description: the theme fallback, echoing the product title. This page has never been optimized.
- Editorial in-body internal links currently on the page: **0.** (The page carries theme boilerplate links only: shipping policy, Get in Touch, and similar. Those are not editorial body links.) The gate hard-fails a body with no internal link.
- Weight: **222 g. Render US-first as 7.8 oz (222 g).**
- Source copy, verbatim, and it is the ONLY sourceable spec material:
  - The regular fit provides a sleek and snug feel for comfort during dynamic movement, while the lace closure offers adjustability for a secure fit. Nanostrike+ technology combines innovative mesh for a featherlight, soft feel with rubber grip elements for striking precision in various conditions. Powerspine technology offers midfoot stability, while the innovative Strikeframe features a lightweight full-length plate for traction during scoring. Non-removable studs add extra grip on firm ground.
  - Regular fit
  - Laces
  - Synthetic and textile upper
  - Textile sockliner
  - Synthetic outsole
  - Floating tongue
  - NANOSTRIKE+ technology  <-- SEE THE CORRECTION BELOW, DO NOT COPY THIS TOKEN
  - Weight: 222 g
  - Non-removable studs

**MANDATORY SOURCE CORRECTION, Mike-approved 2026-08-26.** The live page says "Nanostrike+" in BOTH the paragraph and the spec bullet. **That is a manufacturer-copy error and you must NOT reproduce it. Write `Nanostrike`, with no plus sign.** Nanostrike+ is Elite-tier only; this is a League product. This is the scrape-wins exception: where the live page contradicts a distinction the brand makes, the brand source governs. Same-batch controls confirm the tier rule: the League indoor page reads "Nanostrike mesh" and the Pro page reads "Nanostrike Pro mesh". Rule: `context/page-type-playbooks/product-page-playbook.md`.

## Keywords (validated by ORIN, do NOT re-derive)
| Type | Keyword | Volume |
|---|---|---|
| Primary | adidas predator league fg chaos vs control | no measurable volume (DFS Google Ads + Labs, 2026-08-26). Pack-qualified, sub-floor by design. Context: `adidas predator league firm ground` runs 10/mo on Labs with no Google Ads row. |

**Targeting basis:** Pack-qualified. `adidas predator league fg` is EXACT-held by JP6271 (shipped), which is the FOLD-OVER TONGUE League FG page. **This page is the standard floating-tongue version**, a genuinely different cut. The tongue is the real differentiator, but "standard tongue" is a distinction adidas names only by omission and no searcher types it, so the PACK carries the disambiguation in the primary while the TONGUE does its work in the body copy and the meta description. Recorded so a future reader does not see a pack-qualified term and assume the tongue axis was missed. No pack qualification was strictly forced here (the three other live League standard-tongue pages are FG/MG, a different surface), but the cannibalization block against JP6271 applies regardless.

## Meta fields (ORIN-set; use the title EXACTLY)
- Meta Title: `adidas Predator League Firm Ground Cleats` (41 chars, under the 48 cap)
- Meta Description: write it. 120 to 160 characters, full sentences, no "Product Name: fragment" colon opener, product-anchored call to action. Never end the title or description with a manufacturer brand as a pipe suffix. **The description must name the Chaos vs Control pack**, since the pack was dropped from the title.

## Validated internal links (ORIN link-check 2026-08-26, live H1 + product count verified; body only)
- https://www.prosoccer.com/collections/adidas-predator -- anchor "adidas Predator range" -- validated live 2026-08-26: H1 "Adidas Predator Soccer Cleats for Men, Women, Youth", 104 products
- https://www.prosoccer.com/collections/adidas-chaos-vs-control-soccer-cleats -- anchor "Chaos vs Control pack" -- validated live 2026-08-26: H1 "adidas Chaos vs Control Soccer Cleats", 46 products

Place the 2 links in DIFFERENT H2 sections. Append a transition sentence after a section's closing line rather than rewriting the closing line to fit the link.

## Claims bar (hard constraints)
- adidas always lowercase. "cleats" or "shoes", never "boots". No em dashes.
- Predator identity is CONTROL and PRECISION, never speed. No F50 speed vocabulary.
- Every spec claim must trace to the verbatim source block above. No bare PASS, no invented specs.
- **Write `Nanostrike`, never `Nanostrike+`.** See the mandatory source correction above.

## Differentiation lane (write prose FROM this, never from a sibling)
- Angle: the striker's contact patch at a mid-tier price. Grip elements and a clean lace-through-floating-tongue face, not a fold-over flap
- Opening hook: the player who wants the ball to leave the foot the way they intended, every time
- Primary metaphor: a predictable, repeatable strike face
- Use-case: dry firm natural grass, weekly competitive match play
- Facet vs siblings: **this is the batch's only STANDARD floating-tongue Predator.** The Pro row is fold-over; the indoor row is fold-over. Make the floating tongue and the lace-over-the-laces face an explicit point of difference. Do NOT write a fold-over sentence here.

## Structure skeleton (mirror STRUCTURE, never prose)
- H2 sequence: identity hook -> Nanostrike upper and the floating tongue strike face -> Strikeframe and Powerspine underfoot -> firm-ground use-case -> Product Details: -> Fit Notes -> Care and Maintenance -> FAQs about adidas Predator League Firm Ground Soccer Cleats
