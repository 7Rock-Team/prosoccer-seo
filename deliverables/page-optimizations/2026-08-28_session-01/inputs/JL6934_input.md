# Input: JL6934 -- adidas 2026 Italy Men's Authentic Home Soccer Jersey

_v2 pre-dispatch input. Work from THIS FILE ONLY. Do not read sibling briefs; the differentiation lane below is what keeps this page distinct._

```gate-meta
{
  "sku": "JL6934",
  "brand": "adidas",
  "brand_ip_posture": "cycle-language-only",
  "tier": "authentic",
  "word_band": [
    450,
    520
  ],
  "word_band_tolerance": 15,
  "primary_keyword": "italy authentic jersey",
  "earned_term": "",
  "earned_term_position": "not-ranking",
  "forbidden_phrasings": {
    "verbatim": [],
    "motifs": [
      "everyone has the same crest on their chest",
      "the shirt they wear away from home",
      "you can name the fabric"
    ],
    "title_frames": [
      "taking the second one",
      "what authentic actually buys you"
    ]
  }
}
```

## NO EARNED TERM. Conventional keyword assignment applies.

The page's largest query, `italy world cup jersey`, holds 4.5% of its impressions and 512 term
impressions over 90 days. That fails both halves of the concentration condition (15% of the page
AND 1,000 term impressions), so **this page has no earned term** and takes a conventionally derived
primary. `earned_term_position` is set to the string `"not-ranking"`, which is an explicit
declaration, not an omission. No band constraint applies.

## Identity
- SKU: JL6934
- URL: https://www.prosoccer.com/products/adidas-2026-italy-mens-authentic-home-soccer-jersey
- Handle: `adidas-2026-italy-mens-authentic-home-soccer-jersey`
- Brand: adidas (always lowercase)
- Brand-IP posture: **cycle-language-only, set deliberately below adidas's default.** adidas does
  hold the 2026 FIFA World Cup license, so the terminology would be permitted here on brand grounds.
  **It is barred on this page on FACTUAL grounds instead: Italy did not qualify for the 2026
  tournament.** Any World Cup framing on an Italy 2026 page is either false or invites the reader to
  infer something false. Do not name the 2026 tournament in any field. The bare year is fine.
- Product category: apparel, JERSEY
- Care H2 required: yes
- Tier: **Authentic.** Slim fit, on-pitch specification.
- Avatar: the supporter who buys the shirt for the shirt, and notices how it is made
- Word band: 450-520 (+/-15 tolerance). This is THIS SKU's own band.

## Phase 0 scrape data (source of truth; scrape-wins, fetched live 2026-08-28, no cache)
- Live H1 and product title: adidas 2026 Italy Men's Authentic Home Soccer Jersey
- Price: $98.00 -- **KEEP OUT of body copy.**
- **Stock: 5 of 6.** 3XL is out; S through 2XL are available. Make no availability claim either way.
- Size run: S, M, L, XL, 2XL, 3XL (context only, never stated in copy)
- Live meta title: **authored and ending `| Pro Soccer`, which is a store-suffix violation.** The
  replacement below fixes it.
- Live meta description: a 329-character body dump that opens "Crafted for on-pitch match usage,
  these **shorts** feature..." on a jersey page.
- Editorial in-body internal links currently on the page: **0.**
- Source copy, verbatim:
  - Crafted for on-pitch match usage, these shorts feature sweat-wicking materials engineered into high-sweat zones to help you feel cool and dry.
  - The jersey incorporates adidas' Climacool+ technology. Advanced cooling. With Climacool+, superior engineering and advanced materials unite for a cool, dry, and distraction-free performance.
  - Slim fit
  - Collar
  - Knit
  - CLIMACOOL+ technology
  - adidas branding elements
  - Lenticular heat-transfer club crest
- **Note the technology name: Climacool+, WITH the plus.** The Spain page in this batch carries
  plain Climacool. They are different technologies. Write `Climacool+` here.
- Colorway: **not in scrape.** Do not name a colour. Weight: not applicable to apparel.

## TWO DEFECTS IN THE SOURCE COPY. Correct them; do not carry them forward.

1. **"these shorts feature sweat-wicking materials engineered into high-sweat zones" is on a jersey
   page.** The claim about sweat-wicking materials in high-sweat zones is usable and sourced; the
   noun is wrong. Write it about the jersey. Do not write the word "shorts" anywhere on this page.
2. **"Lenticular heat-transfer club crest" describes a national-team kit.** Italy is a federation,
   not a club. Keep "lenticular heat-transfer", which is a real and sourced spec and is the most
   distinctive thing on this page. Write it as the federation crest, the national-team crest, or
   simply the crest. **Do not write "club crest" on this page.**

Both defects are live on the page today. Fixing them is part of the deliverable.

## Keywords (validated by ORIN, do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | italy authentic jersey | **70/mo, confirmed on BOTH endpoints (Google Ads 70, DFS Labs 70), 2026-08-28. SUB-FLOOR, deliberate.** | |
| Secondary | italy home jersey | 170/mo (Google Ads, 2026-08-28) | |

**Targeting basis: the authentic-versus-stadium precedent, now six instances deep and unanimous.**
KA6868 (Man United), JZ7218 (Real Madrid), KB8251 (Liverpool), JZ3070 (Bayern), JZ3165 (Arsenal)
and 18281 (Cruz Azul) are all men's-authentic-HOME pages holding `<team> authentic jersey`
unqualified. This page follows that pattern exactly.

`italy soccer jersey` (5,400/mo) and `italy jersey 2026` (1,000/mo) were **rejected**.
`italy soccer jersey` is the head term and belongs to `/collections/italy`, which is live with 40
products. `italy jersey 2026` is nation-plus-year, which under the registry's own precedent
(`croatia jersey 2026`, `bosnia jersey 2026`) belongs to the mass-market Stadium page, not the
Authentic. Volume never overrides hierarchy; the tier is what makes this page resolve to one
product.

## Meta fields (ORIN-set; use the title EXACTLY)
- Meta Title: `adidas 2026 Italy Authentic Home Jersey` (39 chars, under the 48 cap). This replaces
  a live title that ends `| Pro Soccer`. Never type the store name; the theme appends it.
- Meta Description: write it. 120 to 160 characters, full sentences, no colon opener,
  product-anchored call to action. **It must not say "shorts" and must not name a tournament.**

## Validated internal links (ORIN link-check 2026-08-28, live H1 + product count verified; body only)
- https://www.prosoccer.com/collections/italy -- anchor "Italy collection" -- validated live 2026-08-28: H1 "Italy National Soccer Team Jerseys, Apparel & Gear", 40 products
- https://www.prosoccer.com/collections/2026-national-team-soccer-fan-gear -- anchor "2026 national team apparel" -- validated live 2026-08-28: H1 "2026 National Team Soccer Apparel & Fan Gear", 637 products

Place the 2 links in DIFFERENT H2 sections. Append a transition sentence after a section's closing
line rather than rewriting the closing line to fit the link. **Use these exact URLs.** The slug
`/collections/2026-fifa-world-cup` 301-redirects to the second one and must not be used.

## Claims bar (hard constraints)
- adidas always lowercase. No em dashes. US spelling.
- **No FIFA, no World Cup, no WC, no "the tournament", no "this summer", in any field.** See the
  posture note above: the bar here is factual, not licensing.
- **No tournament-status claim in either direction.** Do not say Italy qualified. Do not say Italy
  missed out, failed to qualify, or is absent. Do not gesture at it. The page sells a jersey.
- **No honours, no title counts, no "four-time" anything, no historical results, no player names.**
  The page carries Bastoni, Raspadori, Barella and Tonali tags; none is sourced copy and none goes
  in. Heritage defaults to qualitative and this page has no sourced heritage at all, so it has none.
- **Authentic means the on-pitch specification.** Slim fit, collar, knit, Climacool+, lenticular
  heat-transfer crest, sweat-wicking materials in high-sweat zones. All sourced. Nothing beyond.
- **This product carries the `customize` tag, so name and number ARE offered.** If you mention it:
  ON THE PRODUCT PAGE, never "at checkout", and it adds 2 to 3 BUSINESS DAYS against the standard
  1 to 2, never weeks. A fully personalized jersey is a separate 5 to 10 business day tier.
  See `context/shipping-customization-facts.md`.
- No availability claim. No price in body copy.

## Differentiation lane (write prose FROM this, never from a sibling)
- Angle: **the detail you only see up close.** The lenticular heat-transfer crest is the single most
  distinctive sourced spec anywhere in this batch, and nothing else on the page competes with it.
- Opening hook: a crest that does something when the light or the angle changes, on a shirt you
  otherwise wear without thinking about it.
- Primary metaphor: close inspection. The thing you notice holding it, not the thing you notice
  across a room.
- Use-case: the supporter who keeps shirts, hangs them, looks at them.
- Heritage / positioning angle: none sourced, none written, and none available given the
  tournament-status bar. Position entirely on the garment.
- Facet vs siblings: this is the batch's only lenticular crest and its only Climacool+ jersey with a
  collar rather than a crewneck. **The up-close visual detail is yours alone.** Paraguay owns the
  materials breakdown, Spain owns the away-versus-home choice, Club America owns allegiance,
  Guatemala owns belonging. Do not open on fabric composition; open on the crest.

## Structure skeleton (mirror STRUCTURE, never prose)
- H2 sequence: crest-detail hook -> the authentic cut and the collar -> Climacool+ and sweat zones -> name and number on the back -> Product Details: -> Fit Notes -> Care and Maintenance -> FAQs about the adidas Italy Authentic Home Jersey
- Field-length targets: Short Description 50-100 words, Description 450-520 words, FAQ 3-5 pairs
- Product Details bullet categories: fit, collar, construction, technology, crest, branding
