# Input: KC4796 -- adidas 2026-27 Manchester United Youth Stadium Home Soccer Jersey

_v2 per-SKU input. SCRIBE READS and works from this. The fenced gate-meta block is authoritative._
_United sibling; follows the KA6871 EXEMPLAR skeleton. KA6871 owns the "adult belonging / Old Trafford home red" open -> THIS youth brief uses a DIFFERENT anchor (parent-buys-for-kid). CLUB-KIT posture (Premier League + FA Cup direct; European GENERIC; no FIFA/World Cup)._

## Identity
- SKU: KC4796
- URL: https://www.prosoccer.com/products/adidas-2026-27-manchester-united-youth-home-soccer-jersey
- Handle: adidas-2026-27-manchester-united-youth-home-soccer-jersey (no change)
- Brand: adidas
- Brand-IP posture: club-kit (Premier League + FA Cup DIRECT; European competition GENERIC; never name Champions League/European Cup; no FIFA/World Cup)
- Product category: jersey (club, youth)
- Care H2 required: yes
- Tier: Stadium (replica; youth). Do NOT combine tier words.
- Word band: 450-520 (+15 tolerance). Aim ~480; sibling parity with KA6871/KC4773. Draft lean-first (editorial ~250-280, TIGHT FAQ; a leaner first draft -- editorial closer to 250 -- hits band in one pass), SELF-RUN `python scripts/batch_gate.py deliverables/page-optimizations/2026-07-13_session-01` to green BEFORE returning.

## Phase 0 scrape data (source of truth; scrape-wins)
- Home/away: HOME (Stadium, youth).
- Colorway: the United red/white/black home (same 26/27 home kit as the men's). Scrape design note: "bold colours... unmistakably Manchester United... great for young fans who want to show their pride on match day, at school, or out with friends."
- Fabric: 100% polyester (100% recycled). adidas CLIMACOOL (quick-dry; "durable wear and freedom of movement for active days").
- Fit / collar: Regular fit. Flat-knit polo collar, flat-knit cuffs. Woven club crest. adidas branding.
- Price: $79.99 -- KEEP OUT of body copy.
- Sizes: YXS, YS, YM, YL, YXL.
- Stock: in stock.
- Customization: NOT confirmed in scrape -> do NOT claim name/number customization for this SKU (unlike the Liverpool youth). Scrape-wins.

## Keywords (validated; do NOT re-derive)
| Type | Keyword | Volume | Difficulty |
|---|---|---|---|
| Primary | manchester united youth jersey | 210 |  |
| Secondary | manchester united kids jersey |  |  |
| Secondary | adidas manchester united jersey | 2400 |  |
| Secondary | man united home jersey | 390 |  |

_Primary is youth-qualified (`manchester united youth jersey`, 210/mo). "kids" as secondary variant. Bare "manchester united jersey" CEDED to /collections/manchester-united. New PDP -> DataForSEO governs, no GSC-override. Distinct from sibling primaries._

## Validated internal links (do NOT re-validate)
- https://www.prosoccer.com/collections/epl -- anchor e.g. "more Premier League kits" -- validated 200, live "Premier League Jerseys & Apparel". Premier League may be named directly.
_No current-player link (United's live player collections are all former players). Heritage via retired legends in body copy._

## Differentiation lane (produce prose from THIS; this SKU = PARENT-BUYS-FOR-KID; DIFFERENT anchor than the KA6871 exemplar)
- Avatar: the parent buying a young Manchester United fan their home shirt -- the young Red, passed-down loyalty, the kid's home red for match day, school, and out with friends (scrape's own use-case).
- Opening hook: the young United supporter getting their own home red -- loyalty handed down, the first Red Devils shirt that's truly theirs. (Own this "handed-down / young Red / family" open; do NOT reuse KA6871's adult-belonging/Old Trafford open.)
- Primary metaphor: loyalty passed from one generation to the next; the shirt as an inheritance and a beginning for a young Red. NOT athletic performance, NOT current-form.
- Voice: parent-facing, warm, practical (regular youth fit, durable for active days, growth), proud.
- Facet: youth, regular fit, parent buyer, durability + growth; the red/white/black home.

## Manchester United identity guardrail (evergreen; approved block -- SAME as KA6871)
- Nicknames: "The Red Devils" (current; crest since 1970). "The Heathens" (historical). "Busby Babes" -- DO NOT use (barred).
- Anchors: founded 1878 (Newton Heath), renamed 1902; Old Trafford (Greater Manchester), opened 1910. "home at Old Trafford since 1910" / "roots to 1878," NEVER "at Old Trafford since 1878."
- Crest / colours: United red; the crest's red devil with trident + sailing ship (Manchester's maritime heritage), safe to describe.
- Rivalries (heritage tense ONLY): Liverpool (North West Derby); Manchester City (Manchester derby, no current-form); Leeds (optional). In warm youth copy, rivalries are optional -- omit if not additive.
- Honours: 13 Premier League titles (nameable); 20 English top-flight total = 13 PL + 7 First Division (separate); three-time winner of Europe's premier club competition (1968/1999/2008) GENERIC only; FA Cup nameable directly.
- LOAD-BEARING BAR: NO "most successful"/"most titles"/"more than any other" -- JOINT record with Liverpool at 20. Use "one of England's most successful" / "a record 20, shared with Liverpool."
- Brand: adidas current supplier (returned 2015-16); 2026-27 adidas cycle; no figures.
- Safe named entities: Old Trafford, the Red Devils, the devil-and-ship crest; retired legends Charlton, Best, Cantona, Beckham, Rooney. Prefer legends.

## Structure skeleton (mirror the KA6871 STRUCTURE, never its prose)
- H2 sequence: young-Red handed-down hook (sentence case) -> what makes it the youth home shirt / soft durable adidas build + red/white/black home (sentence case) -> for the young supporter + Old Trafford/family heritage + Premier League internal link (sentence case) -> Product Details: Manchester United Youth Home Jersey (Title Case) -> Fit Notes (Title Case) -> Care and Maintenance (Title Case) -> FAQs about the Manchester United Youth Home Jersey (Title Case)
- Field-length targets: Short Description ~55-70 words; Description body 450-520 (aim ~480); FAQ count 4 (include a youth sizing/growth question)
- Product Details bullet categories: tier (Stadium youth), fit (regular, youth sizing YXS-YXL), fabric (recycled polyester + CLIMACOOL quick-dry, durable), crest (woven devil-and-ship), design (red/white/black home), supplier (adidas)

## Forbidden phrasings (write AROUND all three tiers)
- Verbatim (IP + fabrication + anti-convergence, gate-enforced): "champions league", "european cup", "world cup", "most titles", "more than any other", "most trophies", "busby babes", "longtime partner", "which side you're on"
- Motifs: none
- Title-frames: "title defense", "battling for the title", "this season"

```gate-meta
{
  "sku": "KC4796",
  "brand": "adidas",
  "brand_ip_posture": "club-kit-premier-league-fa-cup-direct-european-generic",
  "tier": "Stadium",
  "word_band": [450, 520],
  "word_band_tolerance": 15,
  "primary_keyword": "manchester united youth jersey",
  "forbidden_phrasings": {
    "verbatim": ["champions league", "european cup", "world cup", "most titles", "more than any other", "most trophies", "busby babes", "longtime partner", "which side you're on"],
    "motifs": [],
    "title_frames": ["title defense", "battling for the title", "this season"]
  }
}
```
