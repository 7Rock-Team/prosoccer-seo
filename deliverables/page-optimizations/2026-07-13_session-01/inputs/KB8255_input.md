# Input: KB8255 -- adidas 2026-27 Liverpool Youth Stadium Home Soccer Jersey

_v2 per-SKU input. SCRIBE READS and works from this. The fenced gate-meta block is authoritative._
_CLUB-KIT posture (NOT national-team/FIFA). Club competition-naming policy: Premier League DIRECT; European competition GENERIC; no FIFA/World Cup._

## Identity
- SKU: KB8255
- URL: https://www.prosoccer.com/products/adidas-2026-27-liverpool-youth-stadium-home-soccer-jersey
- Handle: adidas-2026-27-liverpool-youth-stadium-home-soccer-jersey (no change)
- Brand: adidas
- Brand-IP posture: club-kit (Premier League DIRECT; European competition GENERIC; never name Champions League/European Cup; no FIFA/World Cup)
- Product category: jersey (club, youth)
- Care H2 required: yes
- Tier: Stadium (replica; youth). Do NOT combine tier words.
- Word band: 450-520 (+15 tolerance). Aim ~480; held for sibling parity with the men's/women's/LS cuts. Draft lean-first (editorial ~250-280, tight FAQ), SELF-RUN `python scripts/batch_gate.py deliverables/page-optimizations/2026-07-13_session-01` to green BEFORE returning.

## Phase 0 scrape data (source of truth; scrape-wins)
- Home/away: HOME.
- Colorway: Burgundy / Shankly-red (same 26/27 home as the men's; '80s-inspired graphic reimagined on Shankly-red).
- Fabric: 100% polyester (100% recycled). adidas CLIMACOOL. Doubleknit construction ("soft, durable feel that stands up to the adventures kids take on").
- Fit: Regular fit (youth). Youth customizable (name/number).
- Price: $79.99 -- KEEP OUT of body copy.
- Sizes: YXS, YS, YM, YL, YXL.
- Stock: in stock.
- Existing copy is thin/generic ("adventures kids take on") -- replace with real parent-facing Liverpool copy; scrape-wins on specs only.

## Keywords (validated; do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | liverpool youth jersey | 260 |  |
| Secondary | liverpool kids jersey |  |  |
| Secondary | liverpool youth home jersey |  |  |
| Secondary | adidas liverpool jersey | 2900 |  |

_Primary is youth-qualified (`liverpool youth jersey`, 260/mo, transactional, low competition/backlink rank). Home-qualify in copy; "kids"/"youth home" as secondary variants. Bare "liverpool jersey" CEDED to /collections/liverpool. New PDP -> DataForSEO governs, no GSC-override. Distinct from sibling primaries._

## Validated internal links (do NOT re-validate)
- https://www.prosoccer.com/collections/epl -- anchor e.g. "more Premier League kits" -- validated 200, live "Premier League Jerseys & Apparel". Premier League may be named directly.
_Player-spotlight deferred (Salah departing; currency risk). Heritage via retired legends in body copy._

## Differentiation lane (produce prose from THIS; this SKU = PARENT-BUYS-FOR-KID)
- Avatar: the parent (or grandparent) buying a young Liverpool fan their home shirt -- passed-down loyalty, the kid's first "proper" Reds shirt, growing into the club. Mirror the parent-facing lane of the Chelsea Youth brief (II1663-453) and the copa.md Jennifer-parent lane, framed through CLUB allegiance (family loyalty handed down, the young Red) NOT national pride.
- Opening hook: the young supporter getting their home red -- loyalty handed down a generation, the first Liverpool shirt that's truly theirs. (Own this "handed-down / young Red / family" open.)
- Primary metaphor: loyalty passed from one generation to the next; the shirt as an inheritance and a beginning. NOT athletic performance.
- Voice: parent-facing, warm, practical (durability, growth, youth customizable name/number), proud.
- Facet: youth, regular fit, parent buyer, durability + customization + growth allowance.

## Shared Liverpool identity anchors (evergreen; vary emphasis, don't converge with siblings)
- Nicknames: "The Reds" (safe). Anchors: founded 1892; Anfield since 1892; the Kop.
- Crest/colors/anthem: all-red (Shankly, 1964); Liver Bird crest (since 1892); Shankly Gates + "You'll Never Walk Alone" (the Kop's anthem, safe heritage).
- HILLSBOROUGH -- MEMORIAL-SENSITIVE: the 97 / eternal flames = respectful tribute ONLY, never decorative or a selling point. Lean on Liver Bird + anthem + all-red; do NOT frame the flames as a feature. (Especially important in warm parent-facing copy -- keep it away from the sales angle entirely.)
- Rivalries (heritage tense ONLY): Manchester United (North West Derby); Everton (Merseyside Derby, 1892 origin). Never current-form.
- Honours: 20 English league titles -- a JOINT record with Manchester United (never "outright most"). 18 First Division + 2 Premier League (2019-20, 2024-25); Premier League nameable. European: six-time winner of Europe's premier club competition (GENERIC only; never name it).
- Brand: adidas current from 2025-26 (a return after Nike; not "longtime partner"); 2026-27 is an adidas year. No deal figures.
- Safe named entities: Shankly, Anfield, the Kop, Liver Bird, "You'll Never Walk Alone", Gerrard, Dalglish. AVOID Salah as "current"; no current manager/standings.

## Structure skeleton (mirror STRUCTURE, never prose)
- H2 sequence: young-Red handed-down hook (sentence case) -> what makes it the youth home shirt / soft durable adidas build + customizable (sentence case) -> for the young supporter + family heritage + Premier League internal link (sentence case) -> Product Details: Liverpool Youth Home Jersey (Title Case) -> Fit Notes (Title Case) -> Care and Maintenance (Title Case) -> FAQs about the Liverpool Youth Home Jersey (Title Case)
- Field-length targets: Short Description ~55-70 words (primary kw sentence 1-2; parent-facing hook; CTA distinct from Meta Description); Description body 450-520 (aim ~480); FAQ count 4 (include a youth-fit/sizing-and-growth question and a customization question)
- Product Details bullet categories: tier (Stadium youth), fit (regular, youth sizing), fabric (recycled polyester + CLIMACOOL + doubleknit soft/durable), customization (name/number), crest (woven Liver Bird), supplier (adidas)

## Forbidden phrasings (write AROUND all three tiers)
- Verbatim (IP + fabrication guards, gate-enforced): "champions league", "european cup", "world cup", "reigning champions", "defending champions", "most titles", "more than any other", "longtime partner"
- Motifs: none
- Title-frames: "title defense", "battling for the title", "this season"

```gate-meta
{
  "sku": "KB8255",
  "brand": "adidas",
  "brand_ip_posture": "club-kit-premier-league-direct-european-generic",
  "tier": "Stadium",
  "word_band": [450, 520],
  "word_band_tolerance": 15,
  "primary_keyword": "liverpool youth jersey",
  "forbidden_phrasings": {
    "verbatim": ["champions league", "european cup", "world cup", "reigning champions", "defending champions", "most titles", "more than any other", "longtime partner"],
    "motifs": [],
    "title_frames": ["title defense", "battling for the title", "this season"]
  }
}
```
