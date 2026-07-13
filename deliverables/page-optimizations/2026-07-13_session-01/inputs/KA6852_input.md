# Input: KA6852 -- adidas 2026-27 Liverpool Men's Stadium Home Soccer Jersey

_v2 per-SKU input. SCRIBE READS and works from this. The fenced gate-meta block is authoritative._
_CLUB-KIT posture (NOT national-team/FIFA). adidas is the maker, but this is a CLUB page: do NOT use World Cup / FIFA / cycle-language. Governing IP rule = club competition-naming policy (Premier League named directly; European competition GENERIC only). See `context/silo-positioning/club-team-jerseys.md`._

## Identity
- SKU: KA6852
- URL: https://www.prosoccer.com/products/adidas-2026-27-liverpool-mens-stadium-home-soccer-jersey
- Handle: adidas-2026-27-liverpool-mens-stadium-home-soccer-jersey (no change)
- Brand: adidas
- Brand-IP posture: club-kit (Premier League DIRECT; European competition GENERIC "Europe's premier club competition / European nights / continental honours"; never name Champions League or European Cup; no FIFA/World Cup chrome at all; club crest/likeness OK as factual description)
- Product category: jersey (club)
- Care H2 required: yes
- Tier: Stadium (replica fan cut; distinct from the Authentic match-spec sibling also live in the collection). Do NOT combine tier words.
- Word band: 450-520 (+15 tolerance). Club-jersey band aligned to the shipped jersey class (Jordan authentic 440-520). Aim ~480. Held across all four Liverpool cuts for sibling parity. Draft lean-first: editorial prose ~250-280, TIGHT FAQ (1-2 sentences each), so the FULL body (editorial + Product Details + Fit Notes + Care + FAQ) lands in band. SELF-RUN `python scripts/batch_gate.py deliverables/page-optimizations/2026-07-13_session-01` and trim to green BEFORE returning.

## Phase 0 scrape data (source of truth; scrape-wins)
- Home/away: HOME (title + scrape)
- Colorway: Burgundy / "Shankly-red" base. This 26/27 home reimagines an iconic 1980s graphic on a vibrant Shankly-red canvas (scrape-confirmed on the sibling PDPs). The '80s-inspired graphic + Shankly-red is the distinctive design hook -- verifiable, use it.
- Fabric: 100% polyester (100% recycled). adidas CLIMACOOL (moisture wicking, "faster sweat release aids cooling"). Doubleknit construction.
- Fit / neck: Slim fit, crew neck. Regular length.
- Design detail: laid-on 3-Stripes, woven club crest, heat-applied sign-off, piping.
- Price: $99.99 -- KEEP OUT of body copy.
- Sizes: S, M, L, XL, 2XL, 3XL.
- Stock: in stock.

## Keywords (validated; do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | liverpool home jersey | 1000 | 8 |
| Secondary | adidas liverpool jersey | 2900 |  |
| Secondary | liverpool home kit | 1000 |  |
| Secondary | liverpool mens home jersey |  |  |

_Primary is home-qualified (NOT the bare "liverpool jersey" / "liverpool soccer jersey" head term at 18,100 -- those are CEDED to /collections/liverpool per the cannibalization split). `liverpool home jersey` (1,000/mo, KD 8) is winnable and matched to the flagship home PDP. Decide-and-log: new PDP, no ranking history -> DataForSEO governs, no GSC-override. Distinct from sibling primaries (youth / women's / long-sleeve)._

## Validated internal links (do NOT re-validate; place where prose authentically references it)
- https://www.prosoccer.com/collections/epl -- anchor e.g. "Premier League home kits" / "more Premier League jerseys" -- validated 200, live "Premier League Jerseys & Apparel" (342 products). Premier League may be named directly.
_Player-spotlight link DEFERRED this set: Salah is departing Liverpool (end of 2025-26, announced 24 Mar 2026) so the obvious pick is a currency trap; other current players unverified for evergreen copy. Use the evergreen Premier League link; carry heritage via retired-legend named entities in body copy (Shankly, Gerrard, Dalglish)._

## Differentiation lane (produce prose from THIS; this SKU = the FLAGSHIP ADULT SUPPORTER)
- Avatar: the adult Liverpool supporter buying their own home shirt -- the Kop, matchday at Anfield or the watch party, the shirt you wear to belong.
- Opening hook: the grown supporter pulling on the home red -- belonging, the Kop, the shirt as the supporter's own colors. (Own this "adult belonging / the Kop matchday" open; siblings use different anchors.)
- Primary metaphor: the home shirt as the supporter's uniform of belonging; the '80s-inspired Shankly-red graphic threading eras of Reds together. NOT athletic-performance.
- Voice: adult fan, first-person allegiance, heritage weight, confident.
- Facet: flagship adult, slim/crew, the closest-to-generic (but home-qualified) home shirt.

## Shared Liverpool identity anchors (evergreen; all four cuts draw from these -- vary emphasis, don't converge)
- Nicknames: "The Reds" (safe, current). When copy would be ambiguous with United, say "Liverpool" not just "the Reds."
- Anchors: founded 1892; Anfield, Liverpool's home since the club's founding in 1892 (do NOT imply the stadium was built in 1892). The Kop (Spion Kop) = the famous home end.
- Crest / colors / anthem: all-red heritage (Bill Shankly introduced the all-red kit in 1964); the Liver Bird crest (on the badge since 1892); the Shankly Gates bearing "You'll Never Walk Alone"; YNWA is the Kop's anthem (safe heritage).
- HILLSBOROUGH memorial -- MEMORIAL-SENSITIVE: the 97 and the eternal flames on the crest commemorate the 97 who died in 1989. NEVER decorative, never a design flourish, never a selling point. Safest: lean on the Liver Bird + the anthem + the all-red heritage; do NOT frame the flames as a feature.
- Rivalries (heritage tense ONLY, never current-form): Manchester United (the North West Derby); Everton (the Merseyside Derby; Liverpool FC was founded in 1892 out of the Anfield/Everton split). Never "battling X this season."
- Honours: 20 English league titles -- a JOINT record, level with Manchester United (never "outright most" / "more than any other"). Split: 18 First Division (pre-1992) + 2 Premier League (2019-20, 2024-25) -- keep separate; Premier League may be named directly. European: six-time winner of Europe's premier club competition (GENERIC only -- NEVER "Champions League" / "European Cup"); Liverpool is England's most successful club in that competition ("six continental titles" is safe).
- Brand: adidas is the current supplier from 2025-26 -- a RETURN/reunion after Nike (do NOT call adidas a "longtime partner"); 2026-27 is an adidas year. No deal figures. Time-bound framing ("the 2026-27 adidas Liverpool home kit").
- Safe evergreen named entities: Bill Shankly, Anfield, the Kop, the Liver Bird, "You'll Never Walk Alone", the Merseyside/North West derby, Steven Gerrard, Kenny Dalglish. AVOID: Salah as "current"; naming a current manager as evergreen fact; any current-form/standings claim.

## Structure skeleton (mirror STRUCTURE, never prose)
- H2 sequence: adult-belonging home-red hook (sentence case) -> what makes it the home shirt / adidas build + Shankly-red '80s graphic (sentence case) -> who it's for + Anfield/heritage + Premier League internal link (sentence case) -> Product Details: Liverpool Home Jersey (Title Case) -> Fit Notes (Title Case) -> Care and Maintenance (Title Case) -> FAQs about the Liverpool Home Jersey (Title Case)
- Field-length targets: Short Description ~55-70 words (primary kw in sentence 1-2; adult-supporter hook; CTA close distinct from Meta Description); Description body 450-520 (aim ~480); FAQ count 4
- Product Details bullet categories: tier (Stadium replica fan cut), fit (slim/crew), fabric (recycled polyester + CLIMACOOL + doubleknit), crest (woven Liver Bird), design (laid-on 3-Stripes, Shankly-red '80s graphic), supplier (adidas, current)

## Forbidden phrasings (write AROUND all three tiers)
- Verbatim (IP + fabrication guards, gate-enforced): "champions league", "european cup", "world cup", "reigning champions", "defending champions", "most titles", "more than any other", "longtime partner"
- Motifs: none
- Title-frames: "title defense", "battling for the title", "this season"

```gate-meta
{
  "sku": "KA6852",
  "brand": "adidas",
  "brand_ip_posture": "club-kit-premier-league-direct-european-generic",
  "tier": "Stadium",
  "word_band": [450, 520],
  "word_band_tolerance": 15,
  "primary_keyword": "liverpool home jersey",
  "forbidden_phrasings": {
    "verbatim": ["champions league", "european cup", "world cup", "reigning champions", "defending champions", "most titles", "more than any other", "longtime partner"],
    "motifs": [],
    "title_frames": ["title defense", "battling for the title", "this season"]
  }
}
```
