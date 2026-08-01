# Input: YF3F3V9 -- New Balance Kid's Furon Team V9 Wide FG - Neon Tide (FA26) [LITTLE-KID]

_Workforce-internal. ORIN wrote this at Batch 10 pre-dispatch (2026-07-31). SCRIBE reads it and works from it. Dispatched pattern: SCRIBE runs its OWN Phase 0 scrape of the live PDP (SCRIBE-runs variant, architecturally supported), authors the full brief per the section structure below, self-runs `python scripts/batch_gate.py deliverables/page-optimizations/2026-07-31_session-01` and trims to green BEFORE returning. The fenced gate-meta block is authoritative for brand, posture, tier, word band, primary keyword, and forbidden phrasings._

## Identity
- SKU: YF3F3V9
- URL: https://www.prosoccer.com/products/new-balance-kids-furon-team-v9-wide-fg-soccer-cleats-neon-tide
- Handle: new-balance-kids-furon-team-v9-wide-fg-soccer-cleats-neon-tide  (NEVER change the handle; flag-only)
- Brand: new balance
- Brand-IP posture: cycle-language-only
- Product category: footwear
- Care H2 required: yes
- Tier (descriptor): team-kids
- Word band: 300-360 (+15 tolerance), full-body INCLUDING FAQ. Hold sibling parity across the club set.

## Phase 0 scrape (SCRIBE-runs; scrape-wins over any hypothesis)
- SCRIBE scrapes the live PDP at the URL above via Firecrawl and pulls colorway, materials, plate/surface, weight (US-first dual notation), fit/sizing signal, existing on-page copy, sibling colorways. Write "not in scrape" for anything absent; never invent.
- No head-start capture; SCRIBE performs the full Phase 0 scrape.

## Keywords (from KIRA; validated, do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | kids soccer cleats wide | 0  [SUB-FLOOR] |  |
| Secondary | youth soccer cleats wide | 1300 |  |
| Secondary | new balance kids furon |  |  |

## Primary assignment note
SUB-FLOOR (no measurable volume). Takes exact qualified 'kids soccer cleats wide' as primary (flagged sub-floor). Carries 'youth soccer cleats wide' (1300, the Junior YF3F3V9's term) as a SECONDARY only. Does NOT take 'kids soccer cleats' (18,100) which is a category head term OWNED by /collections/youth-soccer-shoes (ceded there, verified 2026-07-31; the sub-floor primary is correct BECAUSE the head term belongs to an existing collection, not because no owner exists) or 'wide soccer cleats' (UT3FL7NF). WATCH: semantically overlaps the Junior; differentiate on SIZE RANGE in copy.

## Differentiation lane (produce prose from THIS, not from any sibling exemplar)
- Angle of emphasis: little-kid first wide cleat; the SIZE distinction carries the page
- Opening-hook approach: the little-kid wide fit (feet that don't fit standard-width cleats)
- Primary metaphor: room to grow / the wide little foot
- Use-case scenario: parent buying a wide-fit firm-ground cleat for a little kid, sizes 11K-13.5K
- Heritage / positioning angle: New Balance Furon speed line, little-kid scaling and wide fit
- Facet vs siblings: KID'S / LITTLE-KID (sizes 11K-13.5K), distinct life stage from the Junior grade-school (1-6). Copy MUST lean hard on little-kid vs grade-school so the two pages do not read as siblings and do not cannibalize (see the watch item).

## Structure skeleton (mirror STRUCTURE across siblings, never prose)
- H2 sequence: identity/overview hook -> heritage/positioning (club or line) -> use-case (avatar) -> Product Details: [short name] -> Fit Notes -> Care and Maintenance -> FAQs about [short name]
- Field-length targets: Short Description 50-100 words (200-300 chars); Description body 300-360 words full-body incl FAQ; FAQ 2-4 Q&A (conditional-inclusion: only net-new buyer questions)
- Product Details bullet categories: materials/upper, plate/surface (cleats) or fabric/tech (jerseys), fit/sizing, weight (cleats), care
- Meta Title: <=48 chars written, brand at front, NO store name, NO manufacturer-brand pipe suffix. Meta Description: 120-160, full sentences, no colon-fragment opener, what-it-is + benefit + light CTA.

## Claims + brand-IP rules (SKU-specific)
NB NON-FIFA: NO FIFA/World Cup language, neutral cycle terms only. SCRIBE runs Phase 0 scrape of the live PDP (this is the little-kid page, distinct from the Junior); scrape-wins on colorway, weight, sizes, materials. Sourced-or-qualified only, no bare PASS.

<!-- gate-meta is authoritative; batch_gate.py parses it. -->
```gate-meta
{
  "sku": "YF3F3V9",
  "brand": "new balance",
  "brand_ip_posture": "cycle-language-only",
  "tier": "team-kids",
  "word_band": [
    300,
    360
  ],
  "word_band_tolerance": 15,
  "primary_keyword": "kids soccer cleats wide",
  "forbidden_phrasings": {
    "verbatim": [],
    "motifs": [],
    "title_frames": []
  }
}
```
