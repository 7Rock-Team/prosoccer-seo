# Input: IO1528 -- Nike Junior Superfly 11 Academy Artificial Grass Soccer Cleats (Shadow Pack, FA26)

_v2 pre-dispatch input. Work from this file only._

## Identity
- SKU: IO1528-001
- URL: https://www.prosoccer.com/products/nike-junior-superfly-11-academy-ag-soccer-cleats-shadow-fa26
- Brand: Nike (capitalized)
- Brand-IP posture: cycle-language-only. **Nike holds NO FIFA license. No FIFA or World Cup language.**
- Product category: footwear, CLEATS (says "cleats", never "shoes")
- Care H2 required: yes
- Tier: academy, JUNIOR
- Avatar: Jennifer, the parent-buyer. Grade-school player.
- Word band: 280-360 (+/-15 tolerance). Youth band.

## THIS SKU IS UNQUALIFIED, AND THAT IS CORRECT
It is the ONLY artificial-grass page among twelve live Superfly 11 Academy products, checked against the sitemap refreshed 2026-08-13. No pack sibling exists at this configuration, so no pack qualifier is owed. Do NOT add one to match the other Nike SKUs in the batch.

## NAMING
Live title spells out **Junior** and **Artificial Grass**. Use "Junior" in copy, never "Jr" or "kids". AG is acceptable as a short form after the surface has been named in full once.

## Phase 0 scrape data (source of truth; scrape-wins)
- Live title: Nike Junior Superfly 11 Academy Artificial Grass Soccer Cleats - Shadow Pack (FA26)
- Colorway: Black/Illusion Green-Black
- Upper: NikeSkin, "puts your foot close to the ball", control when dribbling at speed
- Plate: lightweight, with HOLLOWED studs for traction on artificial surfaces
- Collar: Dynamic Fit collar, "locks you in from first step to full sprint"
- Weight: NOT STATED. Price: $74.99 -- KEEP OUT of body copy.
- Care material: synthetic upper, no leather conditioner.

## Keywords (validated, do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | nike junior superfly 11 academy ag | no measurable volume (DFS both endpoints, 2026-08-13) | |
| Secondary (pack) | nike shadow pack | 140 | |
| Topical context ONLY (adult Academy, do NOT target) | nike mercurial superfly 11 academy | 50 (IO1485) | |

Sub-floor but UNQUALIFIED and hierarchy-clean: resolves to exactly one live product. Fully free in the registry.

## Meta fields (ORIN-set; use exactly)
- Meta Title: `Nike Junior Superfly 11 Academy AG Shadow` (41 chars)
- Meta Description: 120-160 chars, full sentences, no colon-fragment opener.

## Validated internal links (ORIN link-check 2026-08-13; body only)
- https://www.prosoccer.com/collections/youth-soccer-shoes -- anchor "kids' soccer cleats" -- validated live, in refreshed sitemap
- https://www.prosoccer.com/collections/nike-mercurial -- anchor "Nike Mercurial cleats" -- validated live, in refreshed sitemap

Place 2 links in different H2 sections.

## Differentiation lane (write prose FROM this)
- Angle: the young speed player whose home pitch is artificial grass, and the hollowed studs that make that surface survivable.
- Opening hook: the 3G pitch a grade-school team trains on, where the wrong studs jar the knees.
- Primary metaphor: purpose-built traction for artificial grass. Batch 13's IO1552 and IO1554 are Junior Superfly 11 CLUB (FG/MG and turf); this is ACADEMY and AG, a different tier and a different surface. Do not reuse their grade-school-speed framing.
- Facet vs siblings: ACADEMY tier, artificial grass, hollowed studs, Dynamic Fit collar.

## Structure skeleton (mirror STRUCTURE, never prose)
- H2 sequence: identity hook -> what hollowed AG studs do -> the Dynamic Fit collar -> Product Details: -> Fit Notes -> Care and Maintenance -> FAQs about
- Short Description 50-100 words; Description 280-360 (tol 15); FAQ 3 Q&A
- Fit Notes must address growing feet and sizing, per the Jennifer avatar. One FAQ should distinguish AG from firm ground, since that is the most likely parent question.
- Product Details bullets: upper, plate + stud type + surface, collar, colorway

## Forbidden phrasings (Batch 13 Junior Superfly Club pages hold these lanes)
- Verbatim: ["your kid wants to feel fast", "the Superfly look"]
- Motifs: ["grade-school speed on grass", "the cleat they'll want to lace up first"]
- Title-frames: ["Your kid wants to feel fast"]

<!-- gate-meta authoritative; batch_gate.py parses it. -->
```gate-meta
{
  "sku": "IO1528",
  "brand": "nike",
  "brand_ip_posture": "cycle-language-only",
  "tier": "academy",
  "word_band": [280, 360],
  "word_band_tolerance": 15,
  "primary_keyword": "nike junior superfly 11 academy ag",
  "forbidden_phrasings": {
    "verbatim": ["your kid wants to feel fast", "the Superfly look"],
    "motifs": ["grade-school speed on grass", "the cleat they'll want to lace up first"],
    "title_frames": ["Your kid wants to feel fast"]
  }
}
```
