# Input: JZ7218 -- adidas Real Madrid Men's Authentic Home 2026-27

_Workforce-internal. ORIN wrote this at Batch 10 pre-dispatch (2026-07-31). SCRIBE reads it and works from it. Dispatched pattern: SCRIBE runs its OWN Phase 0 scrape of the live PDP (SCRIBE-runs variant, architecturally supported), authors the full brief per the section structure below, self-runs `python scripts/batch_gate.py deliverables/page-optimizations/2026-07-31_session-01` and trims to green BEFORE returning. The fenced gate-meta block is authoritative for brand, posture, tier, word band, primary keyword, and forbidden phrasings._

## Identity
- SKU: JZ7218
- URL: https://www.prosoccer.com/products/adidas-2026-27-real-madrid-mens-authentic-home-soccer-jersey
- Handle: adidas-2026-27-real-madrid-mens-authentic-home-soccer-jersey  (NEVER change the handle; flag-only)
- Brand: adidas
- Brand-IP posture: fifa-permitted
- Product category: jersey
- Care H2 required: yes
- Tier (descriptor): authentic
- Word band: 450-520 (+15 tolerance), full-body INCLUDING FAQ. Hold sibling parity across the club set.

## Phase 0 scrape (SCRIBE-runs; scrape-wins over any hypothesis)
- SCRIBE scrapes the live PDP at the URL above via Firecrawl and pulls colorway, materials, plate/surface, weight (US-first dual notation), fit/sizing signal, existing on-page copy, sibling colorways. Write "not in scrape" for anything absent; never invent.
- No head-start capture; SCRIBE performs the full Phase 0 scrape.

## Keywords (from KIRA; validated, do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | real madrid authentic jersey | 1000 |  |
| Secondary | real madrid authentic home jersey |  |  |
| Secondary | adidas real madrid jersey |  |  |

## Primary assignment note
Clears the floor; standard primary assignment.

## Differentiation lane (produce prose from THIS, not from any sibling exemplar)
- Angle of emphasis: player-version / match-spec authenticity (the shirt the squad actually wears)
- Opening-hook approach: the authenticity distinction (authentic vs replica) without disparaging the stadium cut
- Primary metaphor: on-pitch fidelity / what the players wear
- Use-case scenario: the supporter who wants the exact player-grade kit, matchday and collection
- Heritage / positioning angle: Real Madrid white / club identity, qualitative honours only
- Facet vs siblings: the AUTHENTIC (player) cut; distinct from Batch 9 JZ7206 stadium/replica home

## Structure skeleton (mirror STRUCTURE across siblings, never prose)
- H2 sequence: identity/overview hook -> heritage/positioning (club or line) -> use-case (avatar) -> Product Details: [short name] -> Fit Notes -> Care and Maintenance -> FAQs about [short name]
- Field-length targets: Short Description 50-100 words (200-300 chars); Description body 450-520 words full-body incl FAQ; FAQ 2-4 Q&A (conditional-inclusion: only net-new buyer questions)
- Product Details bullet categories: materials/upper, plate/surface (cleats) or fabric/tech (jerseys), fit/sizing, weight (cleats), care
- Meta Title: <=48 chars written, brand at front, NO store name, NO manufacturer-brand pipe suffix. Meta Description: 120-160, full sentences, no colon-fragment opener, what-it-is + benefit + light CTA.

## Claims + brand-IP rules (SKU-specific)
RM claims: QUALITATIVE ONLY. No European Cup count, no 'most successful'/superlative. La Liga nameable. European competition GENERIC, never 'Champions League'. adidas may reference 2026 World Cup in past tense but it is not needed for a club shirt. Every heritage/spec claim sourced to the Phase 0 scrape or qualified; no bare PASS.

<!-- gate-meta is authoritative; batch_gate.py parses it. -->
```gate-meta
{
  "sku": "JZ7218",
  "brand": "adidas",
  "brand_ip_posture": "fifa-permitted",
  "tier": "authentic",
  "word_band": [
    450,
    520
  ],
  "word_band_tolerance": 15,
  "primary_keyword": "real madrid authentic jersey",
  "forbidden_phrasings": {
    "verbatim": [],
    "motifs": [],
    "title_frames": []
  }
}
```
