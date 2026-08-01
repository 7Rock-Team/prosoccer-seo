# Input: KC3947 -- adidas Real Madrid Youth Home Long Sleeve 2026-27

_Workforce-internal. ORIN wrote this at Batch 10 pre-dispatch (2026-07-31). SCRIBE reads it and works from it. Dispatched pattern: SCRIBE runs its OWN Phase 0 scrape of the live PDP (SCRIBE-runs variant, architecturally supported), authors the full brief per the section structure below, self-runs `python scripts/batch_gate.py deliverables/page-optimizations/2026-07-31_session-01` and trims to green BEFORE returning. The fenced gate-meta block is authoritative for brand, posture, tier, word band, primary keyword, and forbidden phrasings._

## Identity
- SKU: KC3947
- URL: https://www.prosoccer.com/products/adidas-2026-27-real-madrid-youth-home-long-sleeve-soccer-jersey
- Handle: adidas-2026-27-real-madrid-youth-home-long-sleeve-soccer-jersey  (NEVER change the handle; flag-only)
- Brand: adidas
- Brand-IP posture: fifa-permitted
- Product category: jersey
- Care H2 required: yes
- Tier (descriptor): youth-long-sleeve
- Word band: 450-520 (+15 tolerance), full-body INCLUDING FAQ. Hold sibling parity across the club set.

## Phase 0 scrape (SCRIBE-runs; scrape-wins over any hypothesis)
- SCRIBE scrapes the live PDP at the URL above via Firecrawl and pulls colorway, materials, plate/surface, weight (US-first dual notation), fit/sizing signal, existing on-page copy, sibling colorways. Write "not in scrape" for anything absent; never invent.
- No head-start capture; SCRIBE performs the full Phase 0 scrape.

## Keywords (from KIRA; validated, do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | real madrid youth long sleeve jersey | 20  [SUB-FLOOR] |  |
| Secondary | real madrid youth jersey | 590 |  |
| Secondary | real madrid long sleeve jersey | 1600 |  |

## Primary assignment note
SUB-FLOOR (no measurable volume). Support arrangement mirroring Batch 9 KC4786: this page LEADS with its own exact term 'real madrid youth long sleeve jersey' as primary (flagged sub-floor) and carries 'real madrid youth jersey' (590, KC3993's) as a SECONDARY only. Does NOT take the youth head term as primary or any collection/sibling term.

## Differentiation lane (produce prose from THIS, not from any sibling exemplar)
- Angle of emphasis: youth long-sleeve / active-kid cover
- Opening-hook approach: the long-sleeve youth cut for cooler days and active kids
- Primary metaphor: cover for the young player
- Use-case scenario: parent buying the youth long-sleeve for cooler weather
- Heritage / positioning angle: Real Madrid club identity through a young-fan lens, qualitative only
- Facet vs siblings: the YOUTH LONG-SLEEVE cut; support arrangement under KC3993

## Structure skeleton (mirror STRUCTURE across siblings, never prose)
- H2 sequence: identity/overview hook -> heritage/positioning (club or line) -> use-case (avatar) -> Product Details: [short name] -> Fit Notes -> Care and Maintenance -> FAQs about [short name]
- Field-length targets: Short Description 50-100 words (200-300 chars); Description body 450-520 words full-body incl FAQ; FAQ 2-4 Q&A (conditional-inclusion: only net-new buyer questions)
- Product Details bullet categories: materials/upper, plate/surface (cleats) or fabric/tech (jerseys), fit/sizing, weight (cleats), care
- Meta Title: <=48 chars written, brand at front, NO store name, NO manufacturer-brand pipe suffix. Meta Description: 120-160, full sentences, no colon-fragment opener, what-it-is + benefit + light CTA.

## Claims + brand-IP rules (SKU-specific)
RM claims: QUALITATIVE ONLY. No European Cup count, no superlative. La Liga nameable. European competition GENERIC, never 'Champions League'. Sourced-or-qualified only.

<!-- gate-meta is authoritative; batch_gate.py parses it. -->
```gate-meta
{
  "sku": "KC3947",
  "brand": "adidas",
  "brand_ip_posture": "fifa-permitted",
  "tier": "youth-long-sleeve",
  "word_band": [
    450,
    520
  ],
  "word_band_tolerance": 15,
  "primary_keyword": "real madrid youth long sleeve jersey",
  "forbidden_phrasings": {
    "verbatim": [],
    "motifs": [],
    "title_frames": []
  }
}
```
