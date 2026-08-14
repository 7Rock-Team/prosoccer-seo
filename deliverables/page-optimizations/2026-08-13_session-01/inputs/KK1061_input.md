# Input: KK1061 -- adidas F50 Hyperfast League Indoor Soccer Shoes (Chaos Vs Control Pack, FA26)

_v2 pre-dispatch input. Work from this file only. Mirror the STRUCTURE of the IH7094 exemplar, never its prose._

## Identity
- SKU: KK1061
- URL: https://www.prosoccer.com/products/adidas-f50-hyperfast-league-indoor-soccer-shoes-chaos-vs-control
- Brand: adidas (always lowercase in prose)
- Brand-IP posture: cycle-language-only (no FIFA or World Cup language)
- Product category: footwear, SHOES (indoor model: says "shoes", never "cleats")
- Care H2 required: yes
- Tier: league
- Avatar: Jennifer, the parent-buyer.
- Word band: 340-390 (+/-15 tolerance).

## ORIN note for the brief's Quick Reference (include verbatim)
> Receives canonical consolidation from IH4577 (`userCanonical` points here), which may make this page perform above what its sub-floor primary suggests; watch in GSC after index; see B-TECH-01.

## Phase 0 scrape data (source of truth; scrape-wins)
- Live title: adidas F50 Hyperfast League Indoor Soccer Shoes - Chaos Vs Control Pack (FA26)
- Colorway: Cloud White / Solar Purple / Solar Turbo
- Upper: synthetic and textile Haloskin, wrapped in Haloshell+ engineered mesh
- Outsole: non-marking rubber for indoor courts
- Weight: 7.55 oz (214 g)
- Closure: laces. Fit: regular. Other stated: Sprintgrid forefoot print
- Price: $89.99 -- KEEP OUT of body copy.
- CASING: the live page styles these HALOSKIN / HALOSHELL+ / SPRINTGRID. Write them TITLE CASE (Haloskin, Haloshell+, Sprintgrid) per the brand technology name casing rule.

## Keywords (validated, do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | adidas f50 league indoor chaos vs control | no measurable volume (DFS both endpoints, 2026-08-13) | |
| Secondary (pack) | chaos vs control | 90 | |
| Topical context ONLY (registered to IH4577, do NOT target) | adidas f50 indoor soccer shoes | 480 recorded | |

Sub-floor by design and LOCKED. The unqualified `adidas f50 league indoor` (30/mo) belongs to the earliest live League Indoor incumbent (FA24). Do not target it, do not broaden.

## Meta fields (ORIN-set; use exactly)
- Meta Title: `adidas F50 Hyperfast League Indoor` (34 chars)
- **PACK DROPPED FROM TITLE BY RULE.** Brand + model + generation + configuration + pack is 51 chars against a 48 cap, and no licensed abbreviation exists. Per `product-page-playbook.md` 'Meta title priority ordering, and the generation token', the pack yields.
- **BINDING CONSEQUENCE: the Meta Description MUST name the Chaos vs Control pack explicitly.** This is not optional. Two live pack siblings must not present identically in the SERP, and the buyer needs to see which colorway they are clicking. 120-160 chars, full sentences, no colon-fragment opener.

## Validated internal links (ORIN link-check 2026-08-13; body only)
- https://www.prosoccer.com/collections/indoor -- anchor "indoor soccer shoes" -- validated 200, H1 "Indoor Soccer Shoes for Men and Women", 53 products
- https://www.prosoccer.com/products/adidas-f50-hyperfast-pro-indoor-soccer-shoes-chaos-vs-control -- anchor "Pro-tier indoor version" -- validated 200 (sibling; tier choice)

DO NOT link `/collections/indoor-soccer-shoes`. ORIN checked it: H1 is "Kids' Indoor Soccer Shoes" and it is a youth collection. Wrong audience for this page.

Place 2 links in different H2 sections.

## Differentiation lane (write prose FROM this)
- Angle: the weeknight indoor and futsal regular buying on court feel at a reachable tier.
- Opening hook: the gym floor, the flat court, the game that never stops moving.
- Primary metaphor: court grip and control in a confined space. Do NOT reuse IH7094's reach/access metaphor or KJ3409's surface-matching metaphor.
- Facet vs siblings: LEAGUE tier indoor. KK1049 is the Pro-tier indoor at nearly double the price with a different upper and a Lightstrike midsole.

## Structure skeleton (mirror STRUCTURE, never prose)
- H2 sequence: identity hook -> what the non-marking outsole does on a court -> use-case (weeknight indoor, futsal) -> Product Details: -> Fit Notes -> Care and Maintenance -> FAQs about
- Short Description 50-100 words; Description 340-390 (tol 15); FAQ 3 Q&A
- Product Details bullets: upper, outsole + surface, weight, closure/fit, colorway

## Forbidden phrasings (barred by the exemplar and by KJ3409)
- Verbatim: ["without the flagship outlay", "the F50 look", "right tool for the plastic"]
- Motifs: ["reach and access", "outgrown starter cleats", "surface-matching", "under the lights"]
- Title-frames: ["The player who wants the F50 feel"]

<!-- gate-meta authoritative; batch_gate.py parses it. -->
```gate-meta
{
  "sku": "KK1061",
  "brand": "adidas",
  "brand_ip_posture": "cycle-language-only",
  "tier": "league",
  "word_band": [340, 390],
  "word_band_tolerance": 15,
  "primary_keyword": "adidas f50 league indoor chaos vs control",
  "forbidden_phrasings": {
    "verbatim": ["without the flagship outlay", "the F50 look", "right tool for the plastic"],
    "motifs": ["reach and access", "outgrown starter cleats", "surface-matching", "under the lights"],
    "title_frames": ["The player who wants the F50 feel"]
  }
}
```
