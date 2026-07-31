# Input: KC3989 -- adidas Real Madrid Women's Stadium Home 2026-27

_Workforce-internal. ORIN wrote this at Batch 10 pre-dispatch (2026-07-31). SCRIBE reads it and works from it. Dispatched pattern: SCRIBE runs its OWN Phase 0 scrape of the live PDP (SCRIBE-runs variant, architecturally supported), authors the full brief per the section structure below, self-runs `python scripts/batch_gate.py deliverables/page-optimizations/2026-07-31_session-01` and trims to green BEFORE returning. The fenced gate-meta block is authoritative for brand, posture, tier, word band, primary keyword, and forbidden phrasings._

## Identity
- SKU: KC3989
- URL: https://www.prosoccer.com/products/adidas-2026-27-real-madrid-womens-stadium-home-soccer-jersey
- Handle: adidas-2026-27-real-madrid-womens-stadium-home-soccer-jersey  (NEVER change the handle; flag-only)
- Brand: adidas
- Brand-IP posture: fifa-permitted
- Product category: jersey
- Care H2 required: yes
- Tier (descriptor): womens-stadium
- Word band: 450-520 (+15 tolerance), full-body INCLUDING FAQ. Hold sibling parity across the club set.

## Phase 0 scrape (SCRIBE-runs; scrape-wins over any hypothesis)
- SCRIBE scrapes the live PDP at the URL above via Firecrawl and pulls colorway, materials, plate/surface, weight (US-first dual notation), fit/sizing signal, existing on-page copy, sibling colorways. Write "not in scrape" for anything absent; never invent.
- No head-start capture; SCRIBE performs the full Phase 0 scrape.

## Keywords (from KIRA; validated, do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | real madrid women's jersey | 1000 |  |
| Secondary | real madrid womens jersey | 1000 |  |
| Secondary | real madrid women's home jersey |  |  |

## Primary assignment note
Clears the floor; standard primary assignment.

## Differentiation lane (produce prose from THIS, not from any sibling exemplar)
- Angle of emphasis: women's fit / tailored cut for her
- Opening-hook approach: the women's-specific cut and fit
- Primary metaphor: tailored / made for her
- Use-case scenario: the female supporter buying the shirt cut to fit her
- Heritage / positioning angle: Real Madrid white / club identity, qualitative only
- Facet vs siblings: the WOMEN'S cut; distinct from the men's and youth homes

## Structure skeleton (mirror STRUCTURE across siblings, never prose)
- H2 sequence: identity/overview hook -> heritage/positioning (club or line) -> use-case (avatar) -> Product Details: [short name] -> Fit Notes -> Care and Maintenance -> FAQs about [short name]
- Field-length targets: Short Description 50-100 words (200-300 chars); Description body 450-520 words full-body incl FAQ; FAQ 2-4 Q&A (conditional-inclusion: only net-new buyer questions)
- Product Details bullet categories: materials/upper, plate/surface (cleats) or fabric/tech (jerseys), fit/sizing, weight (cleats), care
- Meta Title: <=48 chars written, brand at front, NO store name, NO manufacturer-brand pipe suffix. Meta Description: 120-160, full sentences, no colon-fragment opener, what-it-is + benefit + light CTA.

## Claims + brand-IP rules (SKU-specific)
RM claims: QUALITATIVE ONLY. No European Cup count, no superlative. La Liga nameable. European competition GENERIC, never 'Champions League'. Sourced-or-qualified only. Apostrophe form 'women's' per playbook 'Gender-qualified keyword form'.

<!-- gate-meta is authoritative; batch_gate.py parses it. -->
```gate-meta
{
  "sku": "KC3989",
  "brand": "adidas",
  "brand_ip_posture": "fifa-permitted",
  "tier": "womens-stadium",
  "word_band": [
    450,
    520
  ],
  "word_band_tolerance": 15,
  "primary_keyword": "real madrid women's jersey",
  "forbidden_phrasings": {
    "verbatim": [],
    "motifs": [],
    "title_frames": []
  }
}
```
