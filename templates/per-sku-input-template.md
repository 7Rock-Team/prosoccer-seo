# Input: [SKU] -- [Product Name]

_Workforce-internal. ORIN writes one of these per SKU during the v2 pre-dispatch
step, into `deliverables/page-optimizations/[session]/inputs/[SKU]_input.md`. SCRIBE
READS it and works from it; SCRIBE does NOT re-scrape, re-look-up keywords, or
re-validate links (ORIN owns all three upstream). `scripts/batch_gate.py` parses the
fenced `gate-meta` JSON block at the bottom. The gate-meta block is the machine-readable
AUTHORITATIVE source for brand, brand-IP posture, tier, word band, primary keyword,
and the three-tier forbidden-phrasings lists; SCRIBE and the gate both read it, so
there is one source of truth and no drift._

## Identity
- SKU: [code, exactly as in the white-label sheet / Shopify admin]
- URL: [full https URL]
- Handle: [current slug]
- Brand: [nike | adidas | umbro | kelme | puma | hummel | ...]
- Brand-IP posture: [fifa-permitted (adidas only) | cycle-language-only (every non-adidas brand)]
- Product category: [footwear | jersey | apparel | goalkeeper-gloves | soccer-ball | accessory | flag | small-merch]
- Care H2 required: [yes (footwear/jersey/apparel/gloves/ball) | no (accessory/flag/small-merch)]
- Tier: [elite | pro | league | club  (Nike: Elite>Pro>Academy>Club; adidas: Elite>Pro>League>Club; Nike Academy ~ adidas League)]
- Word band: [lo]-[hi] (+15 tolerance). SKU-SPECIFIC, never inherited from the exemplar.
  Elite 400-450, Pro 340-390, League/Club 280-340.

## Phase 0 scrape data (source of truth; scrape-wins over any dispatch hypothesis)
_Only fields the Firecrawl scrape actually supplied. If the scrape did not supply a
value, write "not in scrape" and SCRIBE leaves it out rather than inventing it._
- Colorway: [exact variant label from scrape]
- Upper / materials: [...]
- Plate / surface: [FG / AG / MG / TF / IC ...]
- Weight: [value with US-first dual notation, e.g. 6.3 oz (180g), OR "not in scrape"]
- Fit / sizing signal: [...]
- Price: [value] -- KEEP OUT of body copy; tier/positioning language only (evergreen discipline)
- Existing on-page copy notes: [anything the scrape shows that SCRIBE should know]
- Sibling colorways / variants: [...]
- Other verified specs: [...]

## Keywords (from KIRA; validated, do NOT re-derive or re-validate)
_Paste this table into the brief's Keywords section. Volume and Difficulty only;
blank cells stay blank (never fabricated). Sub-floor primary on a GSC override
carries the flag `[N]* (GSC override, pos [X])`._

| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | [primary kw] | [vol/mo] | [KD 0-100] |
| Secondary (pack-specific) | [pack/colorway/release long-tail] | [vol or blank] | [diff or blank] |
| Secondary | [supporting kw] | [vol] | [diff] |

## Validated internal links (from ORIN link-check; do NOT re-validate)
_1 to 2 links, already confirmed 200 + content-signal by ORIN. Place each WHERE the
prose authentically references the target; do NOT default both to the same two H2s
(that is a templating footprint). Links live ONLY in the Description body, never the
Short Description._
- [url] -- anchor "[text]" -- validated 200, [content signal, e.g. "166-product Phantom grid"]
- [url] -- anchor "[text]" -- validated 200, [content signal]

## Differentiation lane (from ORIN diff spec; produce prose from THIS, not from the exemplar)
- Angle of emphasis: [...]
- Opening-hook approach: [...]
- Primary metaphor: [...]
- Use-case scenario: [...]
- Heritage / positioning angle: [...]
- Facet vs siblings: [what makes this SKU distinct within the pack]

## Structure skeleton (Mechanism A; mirror STRUCTURE, never prose)
_H2 category labels only; NO actual titles, NO prose, NO metaphors, NO definitional
sentences. Editorial body H2s are sentence case; structural H2s (Product Details:,
Care and Maintenance, FAQs about) are Title Case. No internal-link-position metadata._
- H2 sequence: [e.g. overview/identity-hook -> heritage/positioning -> use-case -> Product Details -> Fit Notes -> Care -> FAQ]
- Field-length targets: Short Description [words], Description [word band], FAQ count [n]
- Product Details bullet categories: [materials, plate, tier features, weight, care]

## Forbidden phrasings (write AROUND all three tiers; authoritative copy is the gate-meta block)
- Verbatim: [exact hooks / H2 titles / definitional sentences / closing lines the exemplar claimed]
- Motifs (barred tokens): [recurring payoff/register words, e.g. gone, invisible, elusive]
- Title-frames (barred frames): [distinctive frame fragments that survive noun-swapping, e.g. "sees coming"]

<!--
gate-meta is the machine-readable authoritative block. batch_gate.py parses it.
brand/posture/tier/word_band/primary_keyword/forbidden_phrasings live HERE once;
the human-readable sections above echo them for SCRIBE's reading convenience, but
THIS block governs. Keep the two in sync at write time (ORIN writes both together).
-->
```gate-meta
{
  "sku": "[SKU]",
  "brand": "[nike|adidas|umbro|kelme|puma|hummel|...]",
  "brand_ip_posture": "[fifa-permitted|cycle-language-only]",
  "tier": "[elite|pro|league|club]",
  "word_band": [340, 390],
  "word_band_tolerance": 15,
  "primary_keyword": "[primary keyword, lowercase]",
  "forbidden_phrasings": {
    "verbatim": [],
    "motifs": [],
    "title_frames": []
  }
}
```
