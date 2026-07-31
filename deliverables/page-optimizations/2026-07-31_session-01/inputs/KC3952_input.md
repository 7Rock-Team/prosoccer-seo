# Input: KC3952 -- adidas Real Madrid Men's Home Long Sleeve 2026-27

_Workforce-internal. ORIN wrote this at Batch 10 pre-dispatch (2026-07-31). SCRIBE reads it and works from it. Dispatched pattern: SCRIBE runs its OWN Phase 0 scrape of the live PDP (SCRIBE-runs variant, architecturally supported), authors the full brief per the section structure below, self-runs `python scripts/batch_gate.py deliverables/page-optimizations/2026-07-31_session-01` and trims to green BEFORE returning. The fenced gate-meta block is authoritative for brand, posture, tier, word band, primary keyword, and forbidden phrasings._

## Identity
- SKU: KC3952
- URL: https://www.prosoccer.com/products/adidas-2026-27-real-madrid-mens-home-long-sleeve-soccer-jersey
- Handle: adidas-2026-27-real-madrid-mens-home-long-sleeve-soccer-jersey  (NEVER change the handle; flag-only)
- Brand: adidas
- Brand-IP posture: fifa-permitted
- Product category: jersey
- Care H2 required: yes
- Tier (descriptor): long-sleeve
- Word band: 450-520 (+15 tolerance), full-body INCLUDING FAQ. Hold sibling parity across the club set.

## Phase 0 scrape (SCRIBE-runs; scrape-wins over any hypothesis)
- SCRIBE scrapes the live PDP at the URL above via Firecrawl and pulls colorway, materials, plate/surface, weight (US-first dual notation), fit/sizing signal, existing on-page copy, sibling colorways. Write "not in scrape" for anything absent; never invent.
- No head-start capture; SCRIBE performs the full Phase 0 scrape.

## Keywords (from KIRA; validated, do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | real madrid long sleeve jersey | 1600 |  |
| Secondary | real madrid long sleeve home jersey |  |  |
| Secondary | real madrid home jersey | 880 |  |

## Primary assignment note
Clears the floor; standard primary assignment.

## Differentiation lane (produce prose from THIS, not from any sibling exemplar)
- Angle of emphasis: the long-sleeve cut / cooler-weather cover
- Opening-hook approach: the long-sleeve as the layer for autumn and winter fixtures
- Primary metaphor: the cover / the cold-night shift
- Use-case scenario: the supporter who wears the shirt to matches in cooler months, or prefers full-sleeve
- Heritage / positioning angle: Real Madrid white / club identity, qualitative only
- Facet vs siblings: the LONG-SLEEVE cut; distinct from the short-sleeve stadium/authentic homes

## Structure skeleton (mirror STRUCTURE across siblings, never prose)
- H2 sequence: identity/overview hook -> heritage/positioning (club or line) -> use-case (avatar) -> Product Details: [short name] -> Fit Notes -> Care and Maintenance -> FAQs about [short name]
- Field-length targets: Short Description 50-100 words (200-300 chars); Description body 450-520 words full-body incl FAQ; FAQ 2-4 Q&A (conditional-inclusion: only net-new buyer questions)
- Product Details bullet categories: materials/upper, plate/surface (cleats) or fabric/tech (jerseys), fit/sizing, weight (cleats), care
- Meta Title: <=48 chars written, brand at front, NO store name, NO manufacturer-brand pipe suffix. Meta Description: 120-160, full sentences, no colon-fragment opener, what-it-is + benefit + light CTA.

## Claims + brand-IP rules (SKU-specific)
RM claims: QUALITATIVE ONLY. No European Cup count, no superlative. La Liga nameable. European competition GENERIC, never 'Champions League'. Sourced-or-qualified claims only.

<!-- gate-meta is authoritative; batch_gate.py parses it. -->
```gate-meta
{
  "sku": "KC3952",
  "brand": "adidas",
  "brand_ip_posture": "fifa-permitted",
  "tier": "long-sleeve",
  "word_band": [
    450,
    520
  ],
  "word_band_tolerance": 15,
  "primary_keyword": "real madrid long sleeve jersey",
  "forbidden_phrasings": {
    "verbatim": [],
    "motifs": [],
    "title_frames": []
  }
}
```
