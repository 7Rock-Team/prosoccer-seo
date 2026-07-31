# Input: KB8251 -- adidas Liverpool Men's Authentic Home Long Sleeve 2026-27

_Workforce-internal. ORIN wrote this at Batch 10 pre-dispatch (2026-07-31). SCRIBE reads it and works from it. Dispatched pattern: SCRIBE runs its OWN Phase 0 scrape of the live PDP (SCRIBE-runs variant, architecturally supported), authors the full brief per the section structure below, self-runs `python scripts/batch_gate.py deliverables/page-optimizations/2026-07-31_session-01` and trims to green BEFORE returning. The fenced gate-meta block is authoritative for brand, posture, tier, word band, primary keyword, and forbidden phrasings._

## Identity
- SKU: KB8251
- URL: https://www.prosoccer.com/products/adidas-2026-27-liverpool-mens-authentic-home-ls-soccer-jersey
- Handle: adidas-2026-27-liverpool-mens-authentic-home-ls-soccer-jersey  (NEVER change the handle; flag-only)
- Brand: adidas
- Brand-IP posture: fifa-permitted
- Product category: jersey
- Care H2 required: yes
- Tier (descriptor): authentic-long-sleeve
- Word band: 450-520 (+15 tolerance), full-body INCLUDING FAQ. Hold sibling parity across the club set.

## Phase 0 scrape (SCRIBE-runs; scrape-wins over any hypothesis)
- SCRIBE scrapes the live PDP at the URL above via Firecrawl and pulls colorway, materials, plate/surface, weight (US-first dual notation), fit/sizing signal, existing on-page copy, sibling colorways. Write "not in scrape" for anything absent; never invent.
- No head-start capture; SCRIBE performs the full Phase 0 scrape.

## Keywords (from KIRA; validated, do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | liverpool authentic jersey | 390 |  |
| Secondary | liverpool authentic long sleeve jersey |  |  |
| Secondary | liverpool long sleeve jersey | 1300 |  |

## Primary assignment note
Clears the floor; standard primary assignment.

## Differentiation lane (produce prose from THIS, not from any sibling exemplar)
- Angle of emphasis: player-version authenticity, long-sleeve
- Opening-hook approach: the authentic (match-grade) build in the long-sleeve cut
- Primary metaphor: on-pitch fidelity
- Use-case scenario: the supporter who wants the exact player kit in full sleeve
- Heritage / positioning angle: Liverpool club identity, Shankly-red, qualitative honours (Batch 8 precedent)
- Facet vs siblings: the AUTHENTIC cut; KB8268 already owns 'liverpool long sleeve jersey' so this leads on the authentic axis

## Structure skeleton (mirror STRUCTURE across siblings, never prose)
- H2 sequence: identity/overview hook -> heritage/positioning (club or line) -> use-case (avatar) -> Product Details: [short name] -> Fit Notes -> Care and Maintenance -> FAQs about [short name]
- Field-length targets: Short Description 50-100 words (200-300 chars); Description body 450-520 words full-body incl FAQ; FAQ 2-4 Q&A (conditional-inclusion: only net-new buyer questions)
- Product Details bullet categories: materials/upper, plate/surface (cleats) or fabric/tech (jerseys), fit/sizing, weight (cleats), care
- Meta Title: <=48 chars written, brand at front, NO store name, NO manufacturer-brand pipe suffix. Meta Description: 120-160, full sentences, no colon-fragment opener, what-it-is + benefit + light CTA.

## Claims + brand-IP rules (SKU-specific)
LIVERPOOL claims (inherit Batch 8 precedent): European competition GENERIC, never 'Champions League'; Premier League nameable directly. NO 'most successful'/'record 20' for the English LEAGUE (Liverpool equalled United at 20 = joint record). The one safe superlative is European-scoped and factual: 'England's most successful side in Europe's premier competition' (as KB8256 shipped). Default qualitative honours. Enforced by check_heritage_counts. Sourced-or-qualified only.

<!-- gate-meta is authoritative; batch_gate.py parses it. -->
```gate-meta
{
  "sku": "KB8251",
  "brand": "adidas",
  "brand_ip_posture": "fifa-permitted",
  "tier": "authentic-long-sleeve",
  "word_band": [
    450,
    520
  ],
  "word_band_tolerance": 15,
  "primary_keyword": "liverpool authentic jersey",
  "forbidden_phrasings": {
    "verbatim": [],
    "motifs": [],
    "title_frames": []
  }
}
```
