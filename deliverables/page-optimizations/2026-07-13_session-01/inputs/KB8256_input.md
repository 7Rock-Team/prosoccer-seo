# Input: KB8256 -- adidas 2026-27 Liverpool Women's Stadium Home Soccer Jersey

_v2 per-SKU input. SCRIBE READS and works from this. The fenced gate-meta block is authoritative._
_CLUB-KIT posture (NOT national-team/FIFA). Club competition-naming policy: Premier League DIRECT; European competition GENERIC; no FIFA/World Cup._

## Identity
- SKU: KB8256
- URL: https://www.prosoccer.com/products/adidas-2026-27-liverpool-womens-stadium-home-soccer-jersey
- Handle: adidas-2026-27-liverpool-womens-stadium-home-soccer-jersey (no change)
- Brand: adidas
- Brand-IP posture: club-kit (Premier League DIRECT; European competition GENERIC; never name Champions League/European Cup; no FIFA/World Cup)
- Product category: jersey (club, women's)
- Care H2 required: yes
- Tier: Stadium (replica; women's cut). Do NOT combine tier words.
- Word band: 450-520 (+15 tolerance). Aim ~480; sibling parity. Draft lean-first (editorial ~250-280, tight FAQ), SELF-RUN `python scripts/batch_gate.py deliverables/page-optimizations/2026-07-13_session-01` to green BEFORE returning.

## Phase 0 scrape data (source of truth; scrape-wins)
- Home/away: HOME.
- Colorway: Burgundy (scrape colorway = "Burgundy"; the Shankly-red home). Long desc (scrape): "Inspired by the bold spirit of the '80s, it reimagines an iconic graphic on a vibrant Shankly-red canvas" and "the sleeve print... crafted to celebrate Liverpool's legacy." The '80s Shankly-red graphic + sleeve print are the design hooks -- verifiable, use them.
- Fabric: 100% polyester (100% recycled). adidas CLIMACOOL ("faster sweat release, absorbency aids cooling"). Doubleknit construction (durability + comfort).
- Fit / neck: Regular fit, crew neck. Regular length. Woven club crest, sleeve print, adidas branding.
- Price: $99.99 -- KEEP OUT of body copy.
- Sizes: Women's XS, S, M, L.
- Stock: ONLY 1 LEFT (near-sold-out) -- PUBLISH-PRIORITY note for Mike's implementation ordering; copy stays evergreen regardless.

## Keywords (validated; do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | liverpool women's jersey | 110 |  |
| Secondary | liverpool womens jersey | 40 |  |
| Secondary | adidas liverpool jersey | 2900 |  |
| Secondary | liverpool home jersey | 1000 |  |

_Primary is women's-qualified (`liverpool women's jersey`, 110/mo). Same women's-cut split pattern as the Batch 5 Croatia Women's Home. Thin niche volume is expected for women's-cut; the audience-qualified term is the correct pick and clears the "not bare generic" rule. Bare "liverpool jersey" CEDED to /collections/liverpool. New PDP -> DataForSEO governs, no GSC-override. Distinct from sibling primaries._

## Validated internal links (do NOT re-validate)
- https://www.prosoccer.com/collections/epl -- anchor e.g. "more Premier League jerseys" -- validated 200, live "Premier League Jerseys & Apparel". Premier League may be named directly.
_Player-spotlight deferred (Salah departing; currency risk). Heritage via retired legends in body copy._

## Differentiation lane (produce prose from THIS; this SKU = WOMEN'S-CUT SUPPORTER)
- Avatar: the women's-cut Liverpool supporter who wants the tailored fit -- same Shankly-red, same Anfield pride, cut for her. (Croatia women's split pattern.)
- Opening hook: the female Red who wants her home shirt cut for her -- the tailored women's fit, no compromise on belonging. (Own this "cut-for-her / tailored women's fit" open; siblings use different anchors.)
- Primary metaphor: the tailored fit that belongs to her; the '80s Shankly-red graphic and sleeve print as the shirt's identity -- belonging without compromising on fit. NOT athletic performance.
- Voice: women's-cut supporter, fit-forward + heritage, confident and inclusive (avoid tokenizing; she's a Red, full stop).
- Facet: women's regular/crew, women's sizing, the sleeve-print + Shankly-red '80s graphic.

## Shared Liverpool identity anchors (evergreen; vary emphasis, don't converge with siblings)
- Nicknames: "The Reds" (safe). Anchors: founded 1892; Anfield since 1892; the Kop.
- Crest/colors/anthem: all-red (Shankly, 1964); Liver Bird crest (since 1892); Shankly Gates + "You'll Never Walk Alone" (safe heritage).
- HILLSBOROUGH -- MEMORIAL-SENSITIVE: the 97 / eternal flames = respectful tribute ONLY, never decorative or a selling point. Lean on Liver Bird + anthem + all-red; do NOT frame the flames as a feature.
- Rivalries (heritage tense ONLY): Manchester United (North West Derby); Everton (Merseyside Derby, 1892 origin). Never current-form.
- Honours: 20 English league titles -- JOINT record with Manchester United (never "outright most"). 18 First Division + 2 Premier League (2019-20, 2024-25); Premier League nameable. European: six-time winner of Europe's premier club competition (GENERIC only; never name it); England's most successful club in it ("six continental titles" safe).
- Brand: adidas current from 2025-26 (return after Nike; not "longtime partner"); 2026-27 is an adidas year. No figures.
- Safe named entities: Shankly, Anfield, the Kop, Liver Bird, "You'll Never Walk Alone", Gerrard, Dalglish. AVOID Salah as "current"; no current manager/standings.

## Structure skeleton (mirror STRUCTURE, never prose)
- H2 sequence: women's-cut belonging hook (sentence case) -> what makes it the women's home shirt / tailored fit + Shankly-red '80s graphic + sleeve print (sentence case) -> for the supporter + Anfield heritage + Premier League internal link (sentence case) -> Product Details: Liverpool Women's Home Jersey (Title Case) -> Fit Notes (Title Case) -> Care and Maintenance (Title Case) -> FAQs about the Liverpool Women's Home Jersey (Title Case)
- Field-length targets: Short Description ~55-70 words (primary kw sentence 1-2; women's-cut hook; CTA distinct from Meta Description); Description body 450-520 (aim ~480); FAQ count 4 (include a women's-fit/sizing question)
- Product Details bullet categories: tier (Stadium women's cut), fit (regular women's, crew), fabric (recycled polyester + CLIMACOOL + doubleknit), design (Shankly-red '80s graphic, sleeve print), crest (woven Liver Bird), supplier (adidas)

## Forbidden phrasings (write AROUND all three tiers)
- Verbatim (IP + fabrication guards, gate-enforced): "champions league", "european cup", "world cup", "reigning champions", "defending champions", "most titles", "more than any other", "longtime partner"
- Motifs: none
- Title-frames: "title defense", "battling for the title", "this season"

```gate-meta
{
  "sku": "KB8256",
  "brand": "adidas",
  "brand_ip_posture": "club-kit-premier-league-direct-european-generic",
  "tier": "Stadium",
  "word_band": [450, 520],
  "word_band_tolerance": 15,
  "primary_keyword": "liverpool women's jersey",
  "forbidden_phrasings": {
    "verbatim": ["champions league", "european cup", "world cup", "reigning champions", "defending champions", "most titles", "more than any other", "longtime partner"],
    "motifs": [],
    "title_frames": ["title defense", "battling for the title", "this season"]
  }
}
```
