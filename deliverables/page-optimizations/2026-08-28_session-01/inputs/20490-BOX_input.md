# Input: 20490-BOX -- Panini 2026 FIFA World Cup Stickers BOX (50 Packs Each)

_v2 pre-dispatch input. Work from THIS FILE ONLY. Do not read sibling briefs; the differentiation lane below is what keeps this page distinct._

```gate-meta
{
  "sku": "20490-BOX",
  "brand": "panini",
  "brand_ip_posture": "fifa-permitted",
  "tier": "collectible",
  "word_band": [
    320,
    380
  ],
  "word_band_tolerance": 15,
  "primary_keyword": "panini sticker box",
  "earned_term": "",
  "earned_term_position": "not-ranking",
  "forbidden_phrasings": {
    "verbatim": [],
    "motifs": [
      "everyone has the same crest on their chest",
      "you can name the fabric",
      "the piece that fails first"
    ],
    "title_frames": [
      "taking the second one"
    ]
  }
}
```

## BRAND-IP RULING, and it is new. Read this first.

**`brand_ip_posture` is set to `fifa-permitted` for Panini. This is an ORIN decision, it extends the
posture beyond adidas for the first time, and it is flagged to Mike in the end-of-batch report.**

The reasoning, recorded so it can be overturned cleanly if Mike disagrees:

`context/brand-ip-constraints.md` keys the FIFA terminology bar on **the brand's FIFA license**, not
on the subject matter, and its list of barred brands is a list of KIT suppliers, all of which
demonstrably hold no license. Panini is not a kit supplier. It is FIFA's sticker licensee, and the
license is asserted in ProSoccer's own live on-page copy, fetched 2026-08-28: **"The official and
exclusive sticker collection of FIFA World Cup 2026!"** The product's live title is
**"Panini 2026 FIFA World Cup Stickers BOX"**, and product titles are never changed by this
workflow. A page whose immutable title names the licensed product cannot be written under a rule
that forbids naming it.

**The permission is narrow, and here is its exact edge:**

- **PERMITTED:** naming the product and the licensed collection as they are named in the live title
  and the source copy. "The official 2026 FIFA World Cup sticker collection" is a sourced statement
  about Panini's license.
- **FORBIDDEN:** any language implying ProSoccer holds a FIFA affiliation, license, endorsement or
  partnership. ProSoccer is a retailer selling a licensed product. Do not write "official retailer",
  "official partner", "FIFA-approved seller" or anything in that family.
- **FORBIDDEN:** tournament commentary of any kind. No fixtures, no favourites, no host cities, no
  dates, no schedule, no predictions. The license covers naming a product, not writing about a
  tournament.

## NO EARNED TERM. Conventional keyword assignment applies.

The page's largest query, `panini sticker box`, is 329 impressions and **1.1% of the page's 29,773**.
That is the worked case that justified the concentration threshold: 29,773 impressions of diffuse
long-tail demand and no term that owns them. `earned_term_position` is the string `"not-ranking"`,
an explicit declaration. No band constraint applies.

## THIS PAGE IS A TEST OF THE PLAYBOOK, AND THE TEST IS WHETHER YOU INVENT ANYTHING

Batch 17's read-outs name this page's failure condition explicitly, and it is not a traffic number:

> "The brief cannot be written without inventing product attributes the scrape does not supply.
> Collectibles have no tier, cut, surface or age band, so the entire configuration tuple the PDP
> playbook rests on is absent. **If SCRIBE reaches for fabricated specifics to fill the template,
> that IS the result.**"

**So: if you cannot source it, leave it out and let the section be short.** A brief that comes in at
the bottom of the band with nothing invented is a PASS. A brief that hits the middle of the band by
inventing an odds ratio is a failure of the whole batch's most interesting question.

**Specifically not in scrape and therefore unwritable:** album page count, sticker dimensions, the
parallel checklist, parallel insertion odds or ratios, the number of stickers needed to complete the
album, print run, release date, country of manufacture, retail packaging dimensions, whether an
album is included (**it is not stated, so do not say either way**), whether stickers are
foil/holographic, any player name, any team name beyond "48 teams".

## Identity
- SKU: 20490-BOX
- URL: https://www.prosoccer.com/products/panini-2026-fifa-world-cup-stickers-box-50-packs-each
- Handle: `panini-2026-fifa-world-cup-stickers-box-50-packs-each`
- Brand: Panini
- Brand-IP posture: fifa-permitted, narrowly. See the ruling above.
- Product category: COLLECTIBLE (stickers). Not apparel, not footwear.
- Care H2 required: **yes, by the gate.** See the section note below.
- Tier: none exists for a collectible. Recorded as `collectible`.
- Avatar: the collector, and the parent buying a box for a kid who has started an album
- Word band: 320-380 (+/-15 tolerance). This is THIS SKU's own band, set for a collectible with a
  real narrative but a thin spec sheet. Never inherit a band.

## SECTION NOTE: the gate requires four structural sections and two of them do not fit a sticker box

`scripts/batch_gate.py check_section_presence` hard-fails a brief missing `## Product Details`,
`## Fit Notes`, `## Care and Maintenance` or `## FAQs about ...`. Those requirements are
unconditional. The product-page playbook, separately, exempts trading cards and stickers from the
Care H2. **The gate wins, because the gate is what actually runs.** Write all four, and fill the two
awkward ones honestly rather than padding them:

- **`## Fit Notes`** (use that exact heading): what is in the box and how far it gets you. 50 packs,
  7 stickers per pack, 350 stickers, 48 teams each with their own spread. That is the buyer's real
  sizing decision on a collectible: box versus single pack.
- **`## Care and Maintenance`**: honest storage. Keep the box out of direct heat and sun, store
  stickers flat, keep unopened packs sealed until you are ready to sort. Nothing about washing,
  nothing invented about archival materials.

This mismatch is logged as a codification candidate in the end-of-batch report. Do not work around
it; write the sections.

## Phase 0 scrape data (source of truth; scrape-wins, fetched live 2026-08-28, no cache)
- Live H1 and product title: Panini 2026 FIFA World Cup Stickers BOX (50 Packs Each)
- Price: $129.99 -- **KEEP OUT of body copy.**
- **Stock: 1 of 1.** Single variant, available. Make no availability claim.
- Live meta title: authored, a verbatim restatement of the product name.
- Live meta description: the first body sentence, 129 characters, machine-cut.
- Editorial in-body internal links currently on the page: **0.**
- Source copy, verbatim, and it is the ONLY sourceable material:
  - Grab the 2026 Panini FIFA World Cup Stickers Box! Each box features 50 packs with 7 stickers per pack for a total of 350 stickers!
  - The official and exclusive sticker collection of FIFA World Cup 2026!
  - 7 Stickers Per Pack
  - A must-have FIFA World Cup collectible ever since the first edition in 1970!
  - Each of the 48 teams participating in the tournament will be featured on its own spread of pages, where collectors can place the stickers of the team's main players!
  - Look for randomly inserted parallels
- **The 1970 first edition is sourced and may be stated as sourced.** It is the only heritage token
  on the page. State it as the first edition of the collection, not as a claim about anything else.
- **"48 teams" is sourced.** So are 50, 7 and 350. Every other number is not.
- **"Look for randomly inserted parallels" is the complete statement about parallels.** Do not
  characterise their rarity, frequency, odds or value.

## Keywords (validated by ORIN, do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | panini sticker box | **1,300/mo, confirmed on BOTH endpoints (Google Ads 1,300, DFS Labs 1,300), 2026-08-28. KD 1. Floor-clearing.** | 1 |
| Secondary | world cup sticker box | 1,600/mo (Google Ads, 2026-08-28) | |

**Targeting basis:** conventional assignment, since the page has no earned term. `panini sticker
box` is brand plus product configuration, and the configuration is the whole decision on this
product: this page is the BOX, not a pack and not an album. That resolves to one product, which is
PDP territory. `panini world cup stickers` carries 60,500/mo and was **rejected**: it is the
category term, satisfied by packs, boxes, albums and Adrenalyn cards alike, and
`/collections/2026-fifa-world-cup-cards-stickers` is live and owns it. Volume never overrides
hierarchy, and a 60,500/mo term is exactly where that rule earns its keep.

## Meta fields (ORIN-set; use the title EXACTLY)
- Meta Title: `Panini 2026 World Cup Sticker Box, 50 Packs` (43 chars, under the 48 cap).
- Meta Description: write it. 120 to 160 characters, full sentences, no colon opener,
  product-anchored call to action. The counts (50 packs, 350 stickers) do a lot of work in a snippet
  and they are sourced.

## Validated internal links (ORIN link-check 2026-08-28, live H1 + product count verified; body only)
- https://www.prosoccer.com/collections/2026-fifa-world-cup-cards-stickers -- anchor "2026 cards and stickers" -- validated live 2026-08-28: H1 "2026 FIFA World Cup Cards & Stickers", 4 products
- https://www.prosoccer.com/collections/trading-cards -- anchor "soccer trading cards" -- validated live 2026-08-28: H1 "Soccer Trading Cards from Topps & Panini", 9 products

Place the 2 links in DIFFERENT H2 sections. Append a transition sentence after a section's closing
line rather than rewriting the closing line to fit the link. **The cards-and-stickers collection
holds four products, so do not describe it as a wide range.**

## Claims bar (hard constraints)
- No em dashes. US spelling. No exclamation marks: the source copy is full of them and the brand
  voice is not.
- **Panini's FIFA license is nameable. ProSoccer's is not, because there isn't one.** See the ruling.
- **No tournament commentary.** No fixtures, hosts, dates, favourites, groups or predictions.
- **No player names, no team names beyond the sourced "48 teams".**
- **No invented specifics.** Re-read the not-in-scrape list above before writing Product Details.
- **No investment, resale, value-appreciation or "collectible worth" framing.** Nothing sources it
  and it is a claim about money.
- No availability claim. No price in body copy.

## Differentiation lane (write prose FROM this, never from a sibling)
- Angle: **the box as the practical way in.** A single pack is seven stickers against an album with
  48 team spreads. The box is what a person buys when they have decided to actually do this, and
  the argument is arithmetic rather than atmosphere.
- Opening hook: an album with a lot of empty spaces, and the difference between chipping at it and
  starting properly.
- Primary metaphor: filling in. Spreads, gaps, swaps.
- Use-case: two buyers. The collector doing it themselves, and the adult buying a box for a kid or
  for a group who will trade duplicates between them. Duplicates are a feature of the format, not a
  defect, and the source's 350-sticker count makes that honest to say without inventing odds.
- Heritage / positioning angle: one sourced token only, the 1970 first edition. Use it once.
- Facet vs siblings: this is the batch's only collectible and its only non-wearable product.
  **Nothing about the apparel or footwear structure applies.** No fabric, no fit, no technology, no
  crest, no allegiance. The temptation on a page with a thin spec sheet is to reach for the register
  of the pages that have one. Do not. The arithmetic and the album are the whole page.

## Structure skeleton (mirror STRUCTURE, never prose)
- H2 sequence: album-and-arithmetic hook -> what a box is versus a pack -> the 48 spreads and the parallels -> Product Details: -> Fit Notes -> Care and Maintenance -> FAQs about the Panini 2026 World Cup Sticker Box
- Field-length targets: Short Description 50-100 words, Description 320-380 words, FAQ 3-4 pairs
- Product Details bullet categories: packs per box, stickers per pack, total stickers, teams
  covered, parallels, the licensed collection. **Six sourced bullets exist. There is no seventh.**
