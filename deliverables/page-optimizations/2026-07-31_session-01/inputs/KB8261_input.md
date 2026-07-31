# Input: KB8261 -- adidas Liverpool Youth Home Long Sleeve 2026-27

_Workforce-internal. ORIN wrote this at Batch 10 pre-dispatch (2026-07-31). SCRIBE reads it and works from it. Dispatched pattern: SCRIBE runs its OWN Phase 0 scrape of the live PDP (SCRIBE-runs variant, architecturally supported), authors the full brief per the section structure below, self-runs `python scripts/batch_gate.py deliverables/page-optimizations/2026-07-31_session-01` and trims to green BEFORE returning. The fenced gate-meta block is authoritative for brand, posture, tier, word band, primary keyword, and forbidden phrasings._

## Identity
- SKU: KB8261
- URL: https://www.prosoccer.com/products/adidas-2026-27-liverpool-youth-home-long-sleeve-soccer-jersey
- Handle: adidas-2026-27-liverpool-youth-home-long-sleeve-soccer-jersey  (NEVER change the handle; flag-only)
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
| Primary | liverpool youth long sleeve jersey | 0  [SUB-FLOOR] |  |
| Secondary | liverpool youth jersey | 260 |  |
| Secondary | liverpool long sleeve jersey | 1300 |  |

## Primary assignment note
SUB-FLOOR (no measurable volume). Support arrangement mirroring KC4786: LEADS with 'liverpool youth long sleeve jersey' as primary (flagged sub-floor) and carries 'liverpool youth jersey' (260, KB8255's Batch-8 term) as a SECONDARY only. No head or collection term as primary.

## Differentiation lane (produce prose from THIS, not from any sibling exemplar)
- Angle of emphasis: young Kop / youth long-sleeve cover
- Opening-hook approach: the long-sleeve youth cut for the young Liverpool fan
- Primary metaphor: cover for the young Red
- Use-case scenario: parent buying the youth long-sleeve for cooler days
- Heritage / positioning angle: Liverpool club identity through a young-fan lens, qualitative only
- Facet vs siblings: the YOUTH LONG-SLEEVE cut; support arrangement under Batch 8 KB8255

## Structure skeleton (mirror STRUCTURE across siblings, never prose)
- H2 sequence: identity/overview hook -> heritage/positioning (club or line) -> use-case (avatar) -> Product Details: [short name] -> Fit Notes -> Care and Maintenance -> FAQs about [short name]
- Field-length targets: Short Description 50-100 words (200-300 chars); Description body 450-520 words full-body incl FAQ; FAQ 2-4 Q&A (conditional-inclusion: only net-new buyer questions)
- Product Details bullet categories: materials/upper, plate/surface (cleats) or fabric/tech (jerseys), fit/sizing, weight (cleats), care
- Meta Title: <=48 chars written, brand at front, NO store name, NO manufacturer-brand pipe suffix. Meta Description: 120-160, full sentences, no colon-fragment opener, what-it-is + benefit + light CTA.

## Claims + brand-IP rules (SKU-specific)
LIVERPOOL claims (inherit Batch 8 precedent): European competition GENERIC, never 'Champions League'; Premier League nameable. NO league 'most successful'/'record 20'. Qualitative honours default. Sourced-or-qualified only.

<!-- gate-meta is authoritative; batch_gate.py parses it. -->
```gate-meta
{
  "sku": "KB8261",
  "brand": "adidas",
  "brand_ip_posture": "fifa-permitted",
  "tier": "youth-long-sleeve",
  "word_band": [
    450,
    520
  ],
  "word_band_tolerance": 15,
  "primary_keyword": "liverpool youth long sleeve jersey",
  "forbidden_phrasings": {
    "verbatim": [],
    "motifs": [],
    "title_frames": []
  }
}
```
