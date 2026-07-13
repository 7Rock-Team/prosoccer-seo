# Input: IH1897 -- adidas Junior F50 Messi Elite Firm Ground Soccer Cleats (El Ultimo Tango Pack)

_v2 per-SKU input. SCRIBE READS and works from this. The fenced gate-meta block is authoritative._
_F50 silo (established; junior lane exemplar = IH4451, parent-facing). This SKU is a MESSI SIGNATURE product -- Messi name/likeness confirmed present on the page (scrape). adidas + Messi is within adidas's athlete license; naming Messi is fine. NOT an IP escalation. Runs established-silo parallel._

## Identity
- SKU: IH1897
- URL: https://www.prosoccer.com/products/adidas-jr-f50-messi-elite-fg-soccer-cleats-el-ultimo-tango
- Handle: adidas-jr-f50-messi-elite-fg-soccer-cleats-el-ultimo-tango (no change)
- Brand: adidas
- Brand-IP posture: standard cleat (no FIFA/World Cup context; Messi signature is adidas-licensed, nameable)
- Product category: soccer cleat (junior)
- Care H2 required: yes
- Tier: Elite (junior). Do NOT combine tier words.
- Word band: 400-450 (+15 tolerance). Elite-tier band by tier-equivalence (junior cleat, Elite tier). Aim ~420. Draft lean-first (editorial ~200-250, tight FAQ), SELF-RUN `python scripts/batch_gate.py deliverables/page-optimizations/2026-07-13_session-01` to green BEFORE returning.

## Phase 0 scrape data (source of truth; scrape-wins)
- Product: adidas Junior F50 Messi Elite Firm Ground Soccer Cleats -- El Ultimo Tango Pack (SP26). MESSI signature/likeness CONFIRMED present on page.
- Colorway: Ivory / Semi Blue Burst / Icey Blue (scrape-confirmed; NOT a dark/blackout look).
- Upper: Hybridtouch+ upper with a Halocage+ precision-placed TPU skin (for rapid cuts + soft touch); Hybridtouch+ lace cover with premium hook-and-loop fastening.
- Plate/outsole: F50 Speedsystem full-length TPU plate with bladed studs (firm ground). Synthetic outsole.
- Sockliner: LIGHTSTRIKEPRO.
- Weight: 156.4 g (junior). If citing weight, US-first dual notation: 5.5 oz (156 g).
- Fit / closure: regular fit, lace closure.
- Surface: firm ground (dry natural grass).
- Price: $149.99 -- KEEP OUT of body copy.
- Stock: 1 item left (near-sold-out) -- PUBLISH-PRIORITY note for Mike; copy stays evergreen.
- "El Ultimo Tango Pack" is the confirmed pack name. The page states the pack name but NOT any "Messi farewell / last dance / retirement" narrative -> do NOT invent one. A light nod to the Argentine tango heritage (Messi is Argentine) is defensible general knowledge; a "final chapter / last dance / farewell" retirement story is NOT scrape-supported and is BARRED.

## Keywords (validated; do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | junior f50 messi |  |  |
| Secondary | messi soccer cleats | 14800 |  |
| Secondary | adidas f50 messi | 1900 |  |
| Secondary | f50 messi | 1600 |  |

_Primary is junior-qualified (`junior f50 messi`); blank measured volume (new junior long-tail, same as Batch 7 blank-vol pack terms) -> never fabricated. The generic `f50 messi` / `adidas f50 messi` are CEDED to the SENIOR F50 Messi Elite El Ultimo Tango PDP; real demand captured via secondaries `messi soccer cleats` (14,800), `adidas f50 messi` (1,900). New PDP -> DataForSEO governs, no GSC-override._

## Validated internal links (do NOT re-validate)
- https://www.prosoccer.com/collections/adidas-f50 -- anchor e.g. "adidas F50 speed cleats" -- the F50 line collection (Registry 1: live, Complete, "adidas F50 soccer cleats"). Place where the prose references the F50 line.
_(One internal link; F50-line collection is the natural, evergreen cross-sell.)_

## Differentiation lane (produce prose from THIS; this SKU = PARENT-FACING JUNIOR MESSI F50)
- Avatar: the parent buying a young player the Messi F50 -- the kid who wants Messi's speed cleat, in the El Ultimo Tango pack, scaled to junior feet.
- Opening hook: the young player who wants to play in Messi's F50 -- the speed line Messi wears, built for junior feet in the El Ultimo Tango pack.
- Primary metaphor: the Messi-signature speed cleat scaled for the young player (aspiration + parent-accessible value); the light, fast F50 speed DNA. Distinct from the prior junior F50s (Road to Glory / value-frame lane, IH4451): THIS one's differentiator is the MESSI signature + El Ultimo Tango pack.
- Use case: the developing young player on firm natural grass who wants the Messi F50 Elite; parent-facing (fit, growth, value per wear, the Messi aspiration).
- Heritage/anchors: F50 launched 2004 as adidas's speed line (F for fast); Messi's long association with the F50/Messi signature line; Elite = the pro-level build, scaled to junior. Scrape specs (Hybridtouch+, Halocage+, F50 Speedsystem plate, LIGHTSTRIKEPRO) are the tech anchors.
- Facet: junior F50 Messi Elite; El Ultimo Tango pack; Ivory/blue colorway; FG.

## Structure skeleton (mirror STRUCTURE, never prose)
- H2 sequence: young-player-wants-Messi's-F50 hook (sentence case) -> what makes it the Messi Elite / speed build + El Ultimo Tango pack (sentence case) -> for the young player + parent value/fit + F50 internal link (sentence case) -> Product Details: F50 Messi Elite (Title Case) -> Fit Notes (Title Case) -> Care and Maintenance (Title Case) -> FAQs about the F50 Messi Elite (Title Case)
- Field-length targets: Short Description ~40-55 words (primary kw sentence 1-2; junior/parent + Messi hook; CTA distinct from Meta Description); Description body 400-450 (aim ~420); FAQ count 3-4 (include a junior-sizing/growth question)
- Product Details bullet categories: tier (Elite, junior), signature (Messi, El Ultimo Tango pack), upper (Hybridtouch+ / Halocage+ TPU skin), plate (F50 Speedsystem, bladed studs, FG), sockliner (LIGHTSTRIKEPRO), colorway (Ivory / Semi Blue Burst / Icey Blue), fit (regular, lace)

## Forbidden phrasings (write AROUND all three tiers)
- Verbatim (fabrication guards, gate-enforced): "last dance", "final chapter", "farewell", "final tango", "retirement", "world cup"
- Motifs: none
- Title-frames: "one last", "final ride"

```gate-meta
{
  "sku": "IH1897",
  "brand": "adidas",
  "brand_ip_posture": "standard-cleat",
  "tier": "Elite",
  "word_band": [400, 450],
  "word_band_tolerance": 15,
  "primary_keyword": "junior f50 messi",
  "forbidden_phrasings": {
    "verbatim": ["last dance", "final chapter", "farewell", "final tango", "retirement", "world cup"],
    "motifs": [],
    "title_frames": ["one last", "final ride"]
  }
}
```
