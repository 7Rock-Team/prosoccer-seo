# Input: HQ2325 -- Nike Phantom 6 Low Academy Turf Soccer Shoes (Shadow Pack FA26)

_v2 per-SKU input. SCRIBE READS and works from this. The fenced gate-meta block is authoritative._
_Phantom silo (established). FIRST ACADEMY-tier entry in this silo (senior log is Elite/Pro; junior IR4192 was "Low Pro"). Academy ~= adidas League by tier-equivalence -> League/Club WORD BAND. Differentiate against the Batch 7 Low Pro TURF Shadow (HJ4123, Pro tier, ReactX springboard): THIS is Academy (entry tier), NikeSkin/mesh (not VNMSkin), no ReactX. "Shadow" = pack name only, never a disguise metaphor._

## Identity
- SKU: HQ2325
- URL: https://www.prosoccer.com/products/nike-phantom-6-low-academy-turf-soccer-shoes-shadow-fa26
- Handle: nike-phantom-6-low-academy-turf-soccer-shoes-shadow-fa26 (no change)
- Brand: nike
- Brand-IP posture: standard cleat/turf shoe (non-adidas; no FIFA/World Cup)
- Product category: turf soccer shoe
- Care H2 required: yes
- Tier: Academy (entry tier; Nike ladder Elite > Pro > Academy > Club). Do NOT combine tier words.
- Word band: 280-340 (+15 tolerance). League/Club band by tier-equivalence (Nike Academy ~= adidas League). Aim ~310. Draft lean-first (editorial ~180-220, tight FAQ), SELF-RUN `python scripts/batch_gate.py deliverables/page-optimizations/2026-07-13_session-01` to green BEFORE returning.

## Phase 0 scrape data (source of truth; scrape-wins)
- Colorway: Black/Black/Illusion Green (Shadow Pack). Style HQ2325-001 (confirmed).
- Upper: expanded NikeSkin touch zone, powered by engineered mesh (brings foot closer to the ball; control in wet or dry). NOTE: NikeSkin/mesh, NOT the Pro's VNMSkin+Flyknit -- Academy is the accessible touch build.
- Outsole: rubber outsole for quick traction on turf.
- Frame: new natural-fit shoe frame (toe box), cushioned sockliner.
- Surface: turf; shorter, synthetic surfaces.
- Weight: not in scrape -> do NOT cite a weight.
- Price: $94.99 -- KEEP OUT of body copy.
- Stock: in stock.
- Scrape's own framing: "Amplified Touch" (NikeSkin mesh), "Traction for the Turf" (rubber outsole), "Natural Fit."

## Keywords (validated; do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | nike phantom 6 academy turf shadow |  |  |
| Secondary | nike phantom 6 academy | 590 |  |
| Secondary | nike shadow pack | 260 |  |
| Secondary | nike phantom 6 | 12100 | 6 |

_Primary is pack+tier+surface-specific (`nike phantom 6 academy turf shadow`); blank measured volume (new pack term) -> never fabricated. Generic `nike phantom 6 academy` CEDED to model-level pages. Real demand via secondaries `nike phantom 6` (12,100), `nike phantom 6 academy` (590), `nike shadow pack` (260). New PDP -> DataForSEO governs, no GSC-override._

## Validated internal links (do NOT re-validate)
- https://www.prosoccer.com/collections/nike-phantom -- anchor e.g. "Nike Phantom line" -- Registry 1: live, Complete. Place where prose references the Phantom line.
_(One internal link; Phantom-line collection, evergreen cross-sell.)_

## Differentiation lane (produce prose from THIS)
- Avatar: the developing player whose game is on turf / shorter synthetic surfaces, wanting Phantom control touch at an accessible entry (Academy) price -- the small-sided / weeknight-cage / school-turf player.
- Opening hook: Phantom control touch made reachable for the turf player -- the Academy-tier Phantom for the developing player who lives on synthetic surfaces, in the Shadow blackout. (Fresh hook; NOT HJ4123's Pro turf springboard/ReactX, NOT the Batch 6 disguise.)
- Primary metaphor: accessible control/touch on turf at the entry tier (NikeSkin mesh amplifying the touch); value + surface-fit. Deliberately NOT: springboard/ReactX-bounce (HJ4123 Pro Turf), shadow-disguise (Batch 6 Elite), Pro-tier performance framing.
- Use case: the developing/entry player on turf and shorter synthetic surfaces wanting Phantom touch at Academy value.
- Facet: Low Academy Turf Shadow; NikeSkin mesh + rubber turf outsole; entry tier; blackout Shadow colorway. "Shadow" = pack name only.

## Structure skeleton (mirror STRUCTURE, never prose)
- H2 sequence: accessible-turf-touch hook (sentence case) -> what makes it the Academy turf shoe / NikeSkin mesh + rubber outsole (sentence case) -> who it's for + turf surface + Phantom-line internal link (sentence case) -> Product Details: Phantom 6 Academy Turf (Title Case) -> Fit Notes (Title Case) -> Care and Maintenance (Title Case) -> FAQs about the Phantom 6 Academy Turf (Title Case)
- Field-length targets: Short Description ~40-50 words; Description body 280-340 (aim ~310); FAQ count 3
- Product Details bullet categories: tier (Academy, entry), upper (NikeSkin engineered mesh), outsole (rubber, turf), fit (natural-fit frame, cushioned sockliner), surface (turf / shorter synthetic), colorway (Black/Black/Illusion Green, Shadow Pack)

## Forbidden phrasings (write AROUND all three tiers)
- Verbatim (anti-convergence + fabrication guards, gate-enforced): "springboard", "reactx", "disguise", "vnmskin", "world cup"
- Motifs (barred tokens): "gone", "elusive", "bounce"
- Title-frames: "gone before"

```gate-meta
{
  "sku": "HQ2325",
  "brand": "nike",
  "brand_ip_posture": "standard-cleat",
  "tier": "Academy",
  "word_band": [280, 340],
  "word_band_tolerance": 15,
  "primary_keyword": "nike phantom 6 academy turf shadow",
  "forbidden_phrasings": {
    "verbatim": ["springboard", "reactx", "disguise", "vnmskin", "world cup"],
    "motifs": ["gone", "elusive", "bounce"],
    "title_frames": ["gone before"]
  }
}
```
