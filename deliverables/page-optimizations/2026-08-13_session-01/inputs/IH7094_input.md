# Input: IH7094 -- adidas F50 Hyperfast Club Mid Firm/Multi Ground Soccer Cleats (Chaos Vs Control Pack, FA26)

_v2 pre-dispatch input. SCRIBE reads this and works from it; do NOT re-scrape, re-look-up keywords, or re-validate links (ORIN owns all three). This is the adidas F50 EXEMPLAR: its structure and voice anchor KJ3409, KK1061, KK1049 and KK1321, which mirror STRUCTURE only and take their own lanes._

## Identity
- SKU: IH7094
- URL: https://www.prosoccer.com/products/adidas-f50-hyperfast-club-mid-fg-mg-soccer-cleats-chaos-vs-control
- Handle: adidas-f50-hyperfast-club-mid-fg-mg-soccer-cleats-chaos-vs-control
- Brand: adidas (always lowercase in prose)
- Brand-IP posture: cycle-language-only (NO FIFA or World Cup language. adidas holds only an event-scoped 2026 WC license; this is a Chaos vs Control pack cleat, not a WC product, so the license is not invoked.)
- Product category: footwear, CLEATS (says "cleats", never "shoes")
- Care H2 required: yes
- Tier: club
- Avatar: Jennifer, the parent-buyer. Club tier, entry price, growing player.
- Word band: 340-390 (+/-15 tolerance). SKU-specific.

## Phase 0 scrape data (source of truth; scrape-wins; full record in `_phase0-scrape.md`)
- Live title: adidas F50 Hyperfast Club Mid Firm/Multi Ground Soccer Cleats - Chaos Vs Control Pack (FA26)
- Colorway: Cloud White / Solar Purple / Solar Turbo
- Upper: textile with a debossed texture for ball touch
- Plate: FG/MG tooling. Page states "reliable traction on natural and artificial surfaces"
- Cut: MID
- Fit: regular. Sockliner: textile. Branding: 3-Stripes
- Weight: NOT STATED. Do not state one.
- Closure: NOT STATED. Do not state one.
- Price: $64.99 -- KEEP OUT of body copy (tier and positioning language only)

## Keywords (from KIRA/ORIN; validated, do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | adidas f50 club mid fg mg chaos vs control | no measurable volume (DFS both endpoints, 2026-08-13) | |
| Secondary (pack) | chaos vs control | 90 | |
| Topical context ONLY (registered to IH9375, do NOT target) | adidas f50 club | 210 recorded | |

Sub-floor by design and LOCKED. The unqualified `adidas f50 club mid fg mg` (10/mo) belongs to the earliest live Club Mid FG/MG incumbent (Electric Stealth FA25 / Radiant Blaze FA25), not this page. Do not target it, do not broaden.

## Meta fields (ORIN-set; SCRIBE uses these exactly)
- Meta Title: `adidas F50 Hyperfast Club Mid Chaos vs Control` (46 chars, at or under 48)
- Meta Description: 120-160 chars, full sentences, no colon-fragment opener, product-anchored CTA. Must name the Chaos vs Control pack.
- NOTE on "Hyperfast": the meta title carries the generation token by rule (`product-page-playbook.md` 'Meta title priority ordering, and the generation token'). The PRIMARY deliberately does not. That asymmetry is correct and intentional; do not "fix" it.

## Validated internal links (ORIN link-check 2026-08-13; do NOT re-validate; body only, never Short Description)
- https://www.prosoccer.com/collections/adidas-f50 -- anchor "adidas F50 soccer cleats" -- validated live, in refreshed sitemap
- https://www.prosoccer.com/products/adidas-f50-hyperfast-club-turf-soccer-shoes-chaos-vs-control -- anchor "turf version" -- validated 200, H1 "adidas F50 Hyperfast Club Turf Soccer Shoes - Chaos Vs Control Pack (FA26)" (sibling; helps the buyer choose surface)

Place 2 links naturally in different H2 sections. Do not stack both in one H2.

## Differentiation lane (write prose FROM this, not from any sibling)
- Angle: the first "real" speed cleat for a growing player, on the surface most club soccer actually happens on.
- Opening hook: the kid who has outgrown starter cleats and wants the F50 look without flagship money.
- Primary metaphor: reach and access (the speed line, made reachable). Keep this lane; siblings will bar it.
- Use-case: natural grass Saturday, harder mixed pitch Sunday, one pair for both.
- Facet vs siblings: MID cut + FG/MG. KJ3409 is turf and has NO collar. KK1061 and KK1049 are indoor. KK1321 is junior turf.

## Structure skeleton (Mechanism A; mirror STRUCTURE, never prose)
- H2 sequence: identity hook -> the mid-cut and what it does -> surface use-case -> Product Details: -> Fit Notes -> Care and Maintenance -> FAQs about
- Field-length targets: Short Description 50-100 words; Description 340-390 (tol 15); FAQ 3 Q&A (net-new value only)
- Product Details bullet categories: upper, plate + surface, cut, fit/sockliner, colorway

## Forbidden phrasings (exemplar; none barred yet -- this brief SETS the lane the siblings must avoid)
- Verbatim: []
- Motifs: []
- Title-frames: []

<!-- gate-meta authoritative; batch_gate.py parses it. adidas lowercase caught by voice_check; not listed here. -->
```gate-meta
{
  "sku": "IH7094",
  "brand": "adidas",
  "brand_ip_posture": "cycle-language-only",
  "tier": "club",
  "word_band": [340, 390],
  "word_band_tolerance": 15,
  "primary_keyword": "adidas f50 club mid fg mg chaos vs control",
  "forbidden_phrasings": {
    "verbatim": [],
    "motifs": [],
    "title_frames": []
  }
}
```
