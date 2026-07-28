# MANDATORY PDP Brief Template (Batch 9 rebuild) — carried into every input file

Every SCRIBE building a Batch 9 brief MUST produce ALL sections below, in this order. Authoritative source: `context/page-type-playbooks/product-page-playbook.md` ('Description structure', 'Care and Maintenance H2 discipline', 'FAQ for PDPs'). Modeled on the shipped Batch 8 brief `deliverables/page-optimizations/2026-07-13_session-01/KA6871_..._brief.md`. Do NOT ship a shorter shape.

## Required sections (in order)
1. `# <Product Name> -- PDP Optimization` (H1)
2. `## Quick Reference` — SKU, current live Title, URL
3. `## SEO Details` → `### Keywords` — table: `| Type | Keyword | Volume | Difficulty |` (primary + supporting from the input file)
4. `### Title` — the Shopify Title field value
5. `### Short Description` — hero metafield, **50-100 words**, editorial, NO internal links, NO feature-selling
6. `### Description` (body_html), built from named H2 sections **in this reading order**:
   - `## <overview prose H2>` — what it is, the emotional hook
   - `## <build / heritage prose H2>` — how it is built + club/model heritage (qualitative)
   - `## <who it's for prose H2>` — use case + avatar; internal link(s) live here in prose
   - `## Product Details: <name>` — **BULLET H2, specs from the Phase-0 scrape only** (tier, fit, fabric/upper, plate/studs, WEIGHT with dual unit e.g. "6.2 oz (176 g)", crest/design, supplier). This is where specs go, NEVER in prose.
   - `## Fit Notes` — sizing/fit guidance grounded in the scrape (slim/regular/wide, size range). No invented "runs true/size up a half" unless scrape-supported; keep to what the fit data supports.
   - `## Care and Maintenance` — **BULLET H2, REQUIRED for jerseys and cleats.** Temperatures dual-unit (e.g. "Wash cold, 86°F (30°C) or below"). Synthetic uppers get no leather-conditioning note.
   - `## FAQs about <name>` — 3-5 `### question` subheads answering NET-NEW buyer questions (Stadium vs Authentic, colors, true-to-size, is-it-adidas, surface/plate, wide-fit, youth sizing). Answers from scrape/qualitative only.
7. `### Meta Title` — no "ProSoccer" suffix (theme auto-appends)
8. `### Meta Description`
9. `### URL Handle` — existing slug, "(no change)"
10. `### Image Alt Text` — 3-5 bullets, one per gallery view (front, design, crest/detail, colorway)
11. `### Taxonomy Category` — jerseys: `Apparel & Accessories > Clothing > Shirts & Tops`; cleats: `Apparel & Accessories > Shoes > Athletic Shoes`

## Word band (why structure matters)
The band in the gate-meta is calibrated to the FULL structured body (prose H2s + Product Details + Fit Notes + Care + FAQ). Fill it with REAL sections from the scrape. NEVER pad editorial prose to reach the band — that manufactures unsourced performance/durability/comparative claims (the Batch 9 defect this rebuild fixes).

## Hard rules (gate + Layer 3)
- **No em-dashes** (use commas/colons/parentheses). **No en-dashes.**
- **US market: "cleat(s)", never "boot(s)"** ("shoe" ok for variation).
- **No price in the Description body** (prices decay; tier/positioning language only).
- **Specs sourced from the Phase-0 scrape only.** No invented weights, materials, or performance claims. Weight stated exactly, no hedge words near specs.
- **No performance/safety/durability/comparative claims** unless a scrape field supports them (e.g. do not say "holds its shape wash after wash", "narrow cleats let the foot slide", "survives a season", "runs true to size" unless sourced). This is the class the count/superlative gate cannot see — Layer 3 will re-check every sentence.
- **Heritage = qualitative only.** No title/trophy counts, no "most successful/record" superlatives. Jerseys: La Liga / Premier League / FA Cup nameable directly; European club competition GENERIC ("Europe's biggest nights"), never "Champions League".
- **Brand-IP:** New Balance is non-FIFA-licensee → no FIFA/World Cup terms anywhere. Club jerseys carry no FIFA chrome.
- **Internal links:** full HTTPS canonical `https://www.prosoccer.com/...`, in the Description body only (never Short Description), placed where prose references them.
- **Forbidden phrasings:** honor the per-SKU list in the input's gate-meta (cross-sibling motif bars).
- Reuse the claims-verified voice/hooks from the current draft brief where they fit; drop any editorial padding that only existed to hit the band.
