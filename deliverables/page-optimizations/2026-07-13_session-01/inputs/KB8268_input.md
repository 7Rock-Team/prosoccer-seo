# Input: KB8268 -- adidas 2026-27 Liverpool Men's Stadium Home Long-Sleeve Soccer Jersey

_v2 per-SKU input. SCRIBE READS and works from this. The fenced gate-meta block is authoritative._
_CLUB-KIT posture (NOT national-team/FIFA). Club competition-naming policy: Premier League DIRECT; European competition GENERIC; no FIFA/World Cup._
_NOTE Mike's SKU label was "Men's Home Long Sleeve"; the live product is the STADIUM (replica) men's home long-sleeve (`adidas-2026-27-liverpool-mens-home-long-sleeve-soccer-jersey`), distinct from the Authentic LS also live in the collection._

## Identity
- SKU: KB8268
- URL: https://www.prosoccer.com/products/adidas-2026-27-liverpool-mens-home-long-sleeve-soccer-jersey
- Handle: adidas-2026-27-liverpool-mens-home-long-sleeve-soccer-jersey (no change)
- Brand: adidas
- Brand-IP posture: club-kit (Premier League DIRECT; European competition GENERIC; never name Champions League/European Cup; no FIFA/World Cup)
- Product category: jersey (club, long-sleeve)
- Care H2 required: yes
- Tier: Stadium (replica; men's long-sleeve). Do NOT combine tier words.
- Word band: 450-520 (+15 tolerance). Aim ~480; sibling parity. Draft lean-first (editorial ~250-280, tight FAQ), SELF-RUN `python scripts/batch_gate.py deliverables/page-optimizations/2026-07-13_session-01` to green BEFORE returning.

## Phase 0 scrape data (source of truth; scrape-wins)
- Home/away: HOME, LONG-SLEEVE.
- Colorway: Burgundy (Shankly-red home).
- Fabric: 100% polyester (100% recycled). adidas CLIMACOOL ("Cool. Dry. Ready."; faster sweat release aids cooling). Doubleknit construction.
- Fit / neck: Slim fit, V-NECK (distinct from the short-sleeve men's crew neck -- the V-neck + long sleeve is this cut's signature). Regular length.
- Design detail: embroidered logo, woven club crest, 3-Stripes, sleeve print.
- Price: $109.99 -- KEEP OUT of body copy.
- Sizes: S, M, L, XL, 2XL.
- Stock: in stock.

## Keywords (validated; do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | liverpool long sleeve jersey | 1300 |  |
| Secondary | liverpool long sleeve home jersey | 70 |  |
| Secondary | adidas liverpool jersey | 2900 |  |
| Secondary | liverpool home jersey | 1000 |  |

_Primary is cut-qualified (`liverpool long sleeve jersey`, 1,300/mo, transactional, low competition/backlink rank) -- the strongest of the four Liverpool primaries. Home-qualify in copy; "long sleeve home" as secondary. Bare "liverpool jersey" CEDED to /collections/liverpool. New PDP -> DataForSEO governs, no GSC-override. Distinct from sibling primaries._

## Validated internal links (do NOT re-validate)
- https://www.prosoccer.com/collections/epl -- anchor e.g. "more Premier League home kits" -- validated 200, live "Premier League Jerseys & Apparel". Premier League may be named directly.
_Player-spotlight deferred (Salah departing; currency risk). Heritage via retired legends in body copy._

## Differentiation lane (produce prose from THIS; this SKU = LONG-SLEEVE SUPPORTER)
- Avatar: the supporter who specifically wants the long-sleeve home shirt -- the full-sleeve silhouette, cooler-weather Anfield / autumn-and-winter terraces, the V-neck classic look.
- Opening hook: the supporter choosing the long sleeve -- the full-sleeve home red for the colder end of the season, the V-neck silhouette. (Own this "long-sleeve / cold-weather / V-neck silhouette" open; siblings use different anchors.)
- Primary metaphor: the long-sleeve as the season-spanning / cold-terrace cut; the V-neck classic silhouette; the same Shankly-red carried through autumn and winter. NOT athletic performance.
- Voice: the discerning supporter who deliberately chooses the LS -- season-spanning, considered, a different silhouette from the standard shirt.
- Facet: men's LS, slim/V-neck, cooler-weather, the full-season shirt. Lean into the V-neck + long-sleeve as the point of difference vs the short-sleeve crew sibling.

## Shared Liverpool identity anchors (evergreen; vary emphasis, don't converge with siblings)
- Nicknames: "The Reds" (safe). Anchors: founded 1892; Anfield since 1892; the Kop.
- Crest/colors/anthem: all-red (Shankly, 1964); Liver Bird crest (since 1892); Shankly Gates + "You'll Never Walk Alone" (safe heritage).
- HILLSBOROUGH -- MEMORIAL-SENSITIVE: the 97 / eternal flames = respectful tribute ONLY, never decorative or a selling point. Lean on Liver Bird + anthem + all-red; do NOT frame the flames as a feature.
- Rivalries (heritage tense ONLY): Manchester United (North West Derby); Everton (Merseyside Derby, 1892 origin). Never current-form.
- Honours: 20 English league titles -- JOINT record with Manchester United (never "outright most"). 18 First Division + 2 Premier League (2019-20, 2024-25); Premier League nameable. European: six-time winner of Europe's premier club competition (GENERIC only; never name it).
- Brand: adidas current from 2025-26 (return after Nike; not "longtime partner"); 2026-27 is an adidas year. No figures.
- Safe named entities: Shankly, Anfield, the Kop, Liver Bird, "You'll Never Walk Alone", Gerrard, Dalglish. AVOID Salah as "current"; no current manager/standings.

## Structure skeleton (mirror STRUCTURE, never prose)
- H2 sequence: long-sleeve home-red hook (sentence case) -> what makes it the long-sleeve home shirt / V-neck + adidas build + Shankly-red graphic (sentence case) -> for the supporter + Anfield heritage + Premier League internal link (sentence case) -> Product Details: Liverpool Long-Sleeve Home Jersey (Title Case) -> Fit Notes (Title Case) -> Care and Maintenance (Title Case) -> FAQs about the Liverpool Long-Sleeve Home Jersey (Title Case)
- Field-length targets: Short Description ~55-70 words (primary kw sentence 1-2; long-sleeve hook; CTA distinct from Meta Description); Description body 450-520 (aim ~480); FAQ count 4 (include a long-sleeve vs short-sleeve / when-to-wear question)
- Product Details bullet categories: tier (Stadium LS), fit (slim, V-neck, long sleeve), fabric (recycled polyester + CLIMACOOL + doubleknit), design (embroidered logo, Shankly-red graphic, sleeve print), crest (woven Liver Bird), supplier (adidas)

## Forbidden phrasings (write AROUND all three tiers)
- Verbatim (IP + fabrication guards, gate-enforced): "champions league", "european cup", "world cup", "reigning champions", "defending champions", "most titles", "more than any other", "longtime partner"
- Motifs: none
- Title-frames: "title defense", "battling for the title", "this season"

```gate-meta
{
  "sku": "KB8268",
  "brand": "adidas",
  "brand_ip_posture": "club-kit-premier-league-direct-european-generic",
  "tier": "Stadium",
  "word_band": [450, 520],
  "word_band_tolerance": 15,
  "primary_keyword": "liverpool long sleeve jersey",
  "forbidden_phrasings": {
    "verbatim": ["champions league", "european cup", "world cup", "reigning champions", "defending champions", "most titles", "more than any other", "longtime partner"],
    "motifs": [],
    "title_frames": ["title defense", "battling for the title", "this season"]
  }
}
```
