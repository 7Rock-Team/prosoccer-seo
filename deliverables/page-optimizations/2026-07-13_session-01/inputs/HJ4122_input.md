# Input: HJ4122 -- Nike Phantom 6 Low Pro Firm Ground Soccer Cleats (Shadow Pack FA26)

_v2 per-SKU input. SCRIBE READS and works from this. The fenced gate-meta block is authoritative._
_Phantom silo (established). Shadow-pack COLORWAY re-run: MUST differentiate against the shipped Batch 1 Breakout Low Pro FG (IQ1886, "workhorse") AND the Batch 7 Low Pro TURF Shadow (HJ4123, "springboard/ReactX") AND the Batch 6 Elite Shadow "disguise" lane. "Shadow" is the PACK NAME only, never a disguise metaphor._

## Identity
- SKU: HJ4122
- URL: https://www.prosoccer.com/products/nike-phantom-6-low-pro-firm-ground-soccer-cleats-shadow-fa26
- Handle: nike-phantom-6-low-pro-firm-ground-soccer-cleats-shadow-fa26 (no change)
- Brand: nike
- Brand-IP posture: standard cleat (non-adidas; no FIFA/World Cup terminology -- moot on a cleat anyway)
- Product category: soccer cleat
- Care H2 required: yes
- Tier: Pro. Do NOT combine tier words.
- Word band: 340-390 (+15 tolerance). Pro-tier band. Aim ~365. Draft lean-first (editorial ~200-250, tight FAQ), SELF-RUN `python scripts/batch_gate.py deliverables/page-optimizations/2026-07-13_session-01` to green BEFORE returning.

## Phase 0 scrape data (source of truth; scrape-wins)
- Colorway: Black/Black/Illusion Green (the Shadow Pack colorway).
- Upper: Nike VNMSkin (grippy control over the striking area) + Flyknit (brings the foot closer to the ball). NO ReactX on this SKU (ReactX is the Turf sibling HJ4123 -- do NOT carry the springboard/bounce framing here).
- Traction: Cyclone 360 circular traction pattern (forefoot) for plant-and-pivot.
- Frame: new natural-fit shoe frame (toe box), cushioned sockliner.
- Surface: firm ground, dry natural grass.
- Weight: not in scrape -> do NOT cite a weight.
- Price: $159.99 -- KEEP OUT of body copy.
- Stock: in stock.
- Scrape's own framing: "Touch for Clean Strikes" (VNMSkin), "Traction for the Field" (Cyclone 360), "Natural Fit."

## Keywords (validated; do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | nike phantom 6 low pro fg shadow |  |  |
| Secondary | nike phantom 6 low pro | 480 |  |
| Secondary | nike shadow pack | 260 |  |
| Secondary | nike phantom 6 | 12100 | 6 |

_Primary is pack-specific (`nike phantom 6 low pro fg shadow`); blank measured volume (new pack term, same as all Batch 7 Shadow SKUs) -> never fabricated. The generic `nike phantom 6 low pro` / `...low pro fg` are CEDED to the shipped Breakout IQ1886. Real demand via secondaries `nike phantom 6` (12,100), `nike phantom 6 low pro` (480), `nike shadow pack` (260, +929% yr). New PDP -> DataForSEO governs, no GSC-override._

## Validated internal links (do NOT re-validate)
- https://www.prosoccer.com/collections/nike-phantom -- anchor e.g. "Nike Phantom line" -- Registry 1: live, Complete, "Nike Phantom soccer cleats". Place where prose references the Phantom line.
_(One internal link; the Phantom-line collection is the natural evergreen cross-sell. Optionally the Shadow collection, but keep to one to reduce templating.)_

## Differentiation lane (produce prose from THIS)
- Avatar: the Pro-tier player on dry firm natural grass who wins with a clean striking touch -- the number 10 / creator / finisher who wants Phantom control at a reachable tier, in the blackout Shadow look.
- Opening hook: the clean strike off a grippy touch on firm ground -- the Pro-tier Phantom for the player whose game is control and finishing, in the Shadow blackout. (Fresh hook; NOT IQ1886's "workhorse step-up," NOT HJ4123's turf springboard, NOT the Batch 6 Elite disguise.)
- Primary metaphor: the pure striking touch / clean contact on firm ground (VNMSkin grip on the ball). Deliberately NOT: workhorse/dependable-instrument (IQ1886), springboard/ReactX-bounce (HJ4123), shadow-disguise/elusiveness (Batch 6 Elite).
- Use case: the Pro-tier control player on dry natural grass wanting Phantom touch + Cyclone 360 traction at the Pro tier.
- Facet: Low Pro FG Shadow; VNMSkin + Flyknit + Cyclone 360; blackout Shadow colorway. "Shadow" = pack name only.

## Structure skeleton (mirror STRUCTURE, never prose)
- H2 sequence: clean-strike/touch hook (sentence case) -> what makes it the Pro control cleat / VNMSkin + Cyclone 360 build (sentence case) -> who it's for + FG surface + Phantom-line internal link (sentence case) -> Product Details: Phantom 6 Low Pro FG (Title Case) -> Fit Notes (Title Case) -> Care and Maintenance (Title Case) -> FAQs about the Phantom 6 Low Pro FG (Title Case)
- Field-length targets: Short Description ~40-55 words; Description body 340-390 (aim ~365); FAQ count 3
- Product Details bullet categories: tier (Pro), upper (VNMSkin + Flyknit), traction (Cyclone 360, FG), fit (natural-fit frame, cushioned sockliner), surface (dry natural grass), colorway (Black/Black/Illusion Green, Shadow Pack)

## Forbidden phrasings (write AROUND all three tiers)
- Verbatim (anti-convergence + fabrication guards, gate-enforced): "workhorse", "springboard", "reactx", "disguise", "world cup"
- Motifs (barred tokens): "gone", "elusive", "bounce"
- Title-frames: "step up", "gone before"

```gate-meta
{
  "sku": "HJ4122",
  "brand": "nike",
  "brand_ip_posture": "standard-cleat",
  "tier": "Pro",
  "word_band": [340, 390],
  "word_band_tolerance": 15,
  "primary_keyword": "nike phantom 6 low pro fg shadow",
  "forbidden_phrasings": {
    "verbatim": ["workhorse", "springboard", "reactx", "disguise", "world cup"],
    "motifs": ["gone", "elusive", "bounce"],
    "title_frames": ["step up", "gone before"]
  }
}
```
