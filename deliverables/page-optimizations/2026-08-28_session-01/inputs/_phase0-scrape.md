# Batch 17 Phase 0 scrape record

**Fetched live 2026-08-28, no cache (`maxAge: 0`), via `mcp__firecrawl-mcp__firecrawl_scrape`.**
Two passes per SKU: the Shopify product JSON (`/products/<handle>.js`) for title, SKU, price,
variants and source copy, and the rendered PDP for H1, `<title>` and `meta description`.

**Scrape-wins discipline.** Every value below came off one of those two responses. A field the
scrape did not supply is written "not in scrape" and does not appear in any input file.

---

## Head-tag baseline: what a searcher sees today

The read-outs describe the metas as machine output. Confirmed, and the shape varies more than
expected. Three distinct failure modes across nine pages:

| # | SKU | `<title>` (theme suffix ` – ProSoccer` appended) | meta description | chars |
|---|---|---|---|---|
| 1 | Guatemala | product name (theme fallback) | the product name, nothing else | 49 |
| 2 | Spain | product name (theme fallback) | product name + body dump, mid-word truncation | 310 |
| 3 | Paraguay | product name (theme fallback) | product name + body dump, contains the raw entity `&amp;` | 310 |
| 4 | Italy | authored, ends `\| Pro Soccer` (brand-suffix violation) | body dump opening "these **shorts**" on a jersey page | 329 |
| 5 | Haaland | product name, **truncated mid-word at 69 chars** by the theme | authored, generic "Shop the ..." | 136 |
| 6 | Club America | authored, equals the product name | body dump, first sentence only | 162 |
| 7 | USMNT shorts | authored, equals the product name | product name + first bullet | 161 |
| 8 | Panini | authored, equals the product name | first body sentence | 129 |
| 9 | Socks | authored, equals the product name | first body sentence | 148 |

**None of the nine has a written meta title.** Four have no `title_tag` metafield at all and fall
through to the theme; the five that have one restate the product name. Every meta description is
either the product name or an unedited slice of `body_html`.

**Two theme-level defects re-confirmed on this batch, both already logged, neither in scope here:**
`og:image` is emitted as `http://` on all nine, and the `<title>` truncates mid-word (Haaland:
"...Erling Haaland Pa – ProSoccer"). Misha audit items.

---

## Per-SKU scrape data

### 1. UUM1GUAJ525101-U10 -- `umbro-2025-2026-guatemala-mens-home-soccer-jersey`
- Live title / H1: **Umbro 2025-2026 Guatemala Men's Home Soccer Jersey**
- Vendor Umbro | type Apparel | $62.00 | season_2025 | tagged `clearance`
- Option: Men's Apparel Size. **Stock 2 of 6, and the two are 2XL and 3XL.** S, M, L, XL all out.
- Source body copy, complete: **the product title and nothing else.** No materials, no fit, no
  neck, no technology, no colorway. This is the thinnest source in the batch by a wide margin.
- Colorway: not in scrape. Materials: not in scrape. Fit: not in scrape. Weight: n/a.
- Tags of note: `collections_2025-concacaf-gold-cup`, `comp_national-team_guatemala`,
  `official-licensed-jerseys`. No `customize` tag.

### 2. JN4397 -- `adidas-2026-spain-mens-stadium-away-soccer-jersey`
- Live title / H1: **adidas 2026 Spain Men's Stadium Away Soccer Jersey**
- Vendor adidas | type Apparel | $99.99 | season_2026
- **Stock 1 of 6, and the one is 2XL.** S, M, L, XL, 3XL all out.
  (The 2026-08-27 candidate sheet recorded 3 of 8 from a `products.json` count taken that day.
  Today's live read is 1 of 6. Scrape wins; the sheet is a day stale.)
- Source copy, verbatim: "The slim fit offers a modern silhouette and streamlined movement. The
  interlock construction brings a smooth feeling against the skin. Cool. Dry. Ready. Climacool
  wicks and disperses sweat for cool, dry performances with fewer distractions, even during
  high-intensity moments." Bullets: Slim fit / Crewneck / 100% polyester (100% recycled) /
  Interlock fabric / CLIMACOOL technology.
- Colorway: not in scrape. Weight: n/a.
- Tags of note: `customize` (name/number IS offered), `comp_player_lamine-yamal`,
  `comp_player_pedri`.

### 3. 783301-01 -- `puma-2026-paraguay-mens-authentic-home-soccer-jersey`
- Live title / H1: **Puma 2026 Paraguay Men's Authentic Home Soccer Jersey**
- Vendor Puma | type Apparel | $98.00 | season_2026 | tagged `clearance`
- **Stock 5 of 5. Every size available** (S, M, L, XL, 2XL).
- Source copy, verbatim: "MOISTURE MANAGEMENT: Technical dryCELL fabrics wick moisture away from
  the skin to help keep you dry and comfortable" / "Made with at least 50% recycled materials." /
  "Fit: Pro fit" / "Main material type: Dobby" / "Neck: Crew neck" / "Short sleeves" / "PUMA
  branding details" / "Shell: 50% Polyester, 50% Elastomultiester" / "Inserts: 100% Polyester" /
  "Rib: 100% Polyester".
- Colorway: not in scrape. Weight: n/a. No `customize` tag.

### 4. JL6934 -- `adidas-2026-italy-mens-authentic-home-soccer-jersey`
- Live title / H1: **adidas 2026 Italy Men's Authentic Home Soccer Jersey**
- Vendor adidas | type Apparel | $98.00 | season_2026 | tagged `clearance`
- **Stock 5 of 6.** 3XL out.
- Source copy, verbatim: "Crafted for on-pitch match usage, these **shorts** feature sweat-wicking
  materials engineered into high-sweat zones to help you feel cool and dry. The jersey
  incorporates adidas' Climacool+ technology. Advanced cooling. With Climacool+, superior
  engineering and advanced materials unite for a cool, dry, and distraction-free performance."
  Bullets: Slim fit / Collar / Knit / CLIMACOOL+ technology / adidas branding elements /
  Lenticular heat-transfer **club** crest.
- **Two defects in the source itself, both live on the page today and both must be corrected in
  the brief rather than copied forward:** it says "these shorts" on a jersey, and it says "club
  crest" on a national-team kit.
- Colorway: not in scrape. Weight: n/a. Tag `customize` present.

### 5. HQ2332-800 -- `nike-phantom-6-low-elite-firm-ground-soccer-cleats-erling-haaland-pack-fa25`
- Live title / H1: **Nike Phantom 6 Low Elite Firm Ground Soccer Cleats - Erling Haaland Pack (FA25)**
- Vendor Nike | type Footwear | $162.00 | tagged `clearance`, `footwear-pack_nike-erling-haaland-pack-fa25`
- Colorway (single): **Laser Orange/Blue Void/Lemon Venom**
- **Stock 2 of 15, and both are at the small end of the run: M 4.5 / W 6 and M 5.5 / W 7.**
  Everything from M 6 upward is out.
- Source copy, verbatim: the inner-blaze colour story (blue in heel and core, transitioning to red
  and yellow) / "Nike Gripknit, a sticky texture that provides grip where you need it... equal grip
  in wet or dry conditions" / "Cyclone 360 circular traction pattern" strategically placed in the
  forefoot / "A new shoe frame gives you a more natural fit, especially in the toe box."
- **Weight: not in scrape.** Upper material beyond Gripknit: not in scrape. Plate: not in scrape
  (the surface is Firm Ground, from the live title).

### 6. KB9024 -- `adidas-2026-27-club-america-mens-authentic-home-soccer-jersey`
- Live title / H1: **adidas 2026-27 Club America Men's Authentic Home Soccer Jersey**
- Vendor adidas | type Apparel | $159.99 | season_2026 | `club-teams`
- **Stock 6 of 6. Every size available.** (3XL sits on a different variant SKU, KB9016-3XL.)
- Source copy, verbatim: "Made from lightweight, quick drying fabric, it manages sweat
  efficiently, while adidas Climacool+ technology delivers advanced cooling to keep you dry and
  focused." / "Crafted for performance, the slim silhouette offers a streamlined feel, and the
  updated collar adds contemporary style and comfort. Distinctive touches, including the adidas
  logo, perforated 3-Stripes tape and club crest, showcase your allegiance." Bullets: Slim fit /
  Collar / 100% polyester (100% recycled) / CLIMACOOL+ technology / AEROREADY technology / Club crest.
  (The source punctuates that second sentence with em-dashes. Rendered here with commas; the
  em-dash never reaches copy.)
- Colorway: not in scrape. Weight: n/a. No `customize` tag.

### 7. IB4855-410 -- `nike-2026-27-usmnt-mens-stadium-home-shorts`
- Live title / H1: **Nike 2026 USMNT Men's Stadium Home Shorts**
- **HANDLE / TITLE MISMATCH, flagged not fixed.** The handle reads `2026-27`; the live title, H1,
  `og:title` and `<title>` all read **2026**. Live title governs (SEO_BATCH_PROCESS.md §2), so the
  page is written as a 2026 product and the handle is restated verbatim and left alone.
- Vendor Nike | type Apparel | $53.00 | season_2026 | tagged `clearance`, `shorts`
- **Stock 4 of 4. Every size available** (S, M, L, XL).
- Source copy, complete: "Nike Dri-FIT technology moves sweat away from your skin for quicker
  evaporation, helping you stay dry and comfortable." / "Replica design gives you details modeled
  after what the team wears."
- Colorway: not in scrape. Materials: not in scrape. No `customize` tag.

### 8. 20490-BOX -- `panini-2026-fifa-world-cup-stickers-box-50-packs-each`
- Live title / H1: **Panini 2026 FIFA World Cup Stickers BOX (50 Packs Each)**
- Vendor Panini | type Stickers | $129.99 | season_2026
- **Stock 1 of 1.** Single variant, available.
- Source copy, verbatim: "Grab the 2026 Panini FIFA World Cup Stickers Box! Each box features 50
  packs with 7 stickers per pack for a total of 350 stickers!" Bullets: "The official and
  exclusive sticker collection of FIFA World Cup 2026!" / "7 Stickers Per Pack" / "A must-have
  FIFA World Cup collectible ever since the first edition in 1970!" / "Each of the 48 teams
  participating in the tournament will be featured on its own spread of pages, where collectors
  can place the stickers of the team's main players!" / "Look for randomly inserted parallels".
- **Everything else is not in scrape:** no album page count, no parallel odds, no print run, no
  release date, no card dimensions, no checklist.

### 9. DH6621 -- `nike-strike-sleeves-socks`
- Live title / H1: **Nike Strike Sleeves Socks**
- Vendor Nike | type Apparel | $13.99 | no season tag (evergreen)
- Options: Color (Blue, Black, White, Red, Navy) x Sock Size (S/M, L/XL) = 10 variants.
- **Stock 6 of 10.** Available: Blue S/M, Black S/M, Blue L/XL, White L/XL, Red S/M, Red L/XL.
  Out: White S/M, Black L/XL, Navy S/M, Navy L/XL.
- Source copy, complete: "These sleeves show off your soccer fandom, while the sweat-wicking
  technology and stretch fabric will help keep you dry and comfortable on the pitch." / "Nike
  Dri-FIT technology moves sweat away from your skin for quicker evaporation, helping you stay dry
  and comfortable." / "Stretch design fits comfortably over your shin guard."
- Tags place it in `shin-guard-accessories` and `equipment-type_shin-guards`. **These are footless
  sleeves worn over a shin guard, not full socks**, and the source says so.
- Materials: not in scrape. Weight per variant is listed as 227 g in the variant record, which is a
  shipping weight, not a product spec. Not usable in copy.

---

## Internal-link validation

All targets fetched live 2026-08-28. Standard is 200 **plus** content signals (H1 and product
count), never a status code alone.

| URL | H1 | Products | Verdict |
|---|---|---|---|
| `/collections/guatemala` | Guatemala Soccer Jerseys and Fan Gear | 13 | PASS |
| `/collections/2025-concacaf-gold-cup` | 2025 Concacaf Gold Cup Soccer Jerseys, Apparel, & Gear | 72 | PASS |
| `/collections/spain` | Spain National Soccer Team Jerseys, Apparel & Gear | 31 | PASS |
| `/collections/italy` | Italy National Soccer Team Jerseys, Apparel & Gear | 40 | PASS |
| `/collections/paraguay-national-soccer-team-jerseys-apparel-gear` | Paraguay National Soccer Team Jerseys, Apparel & Gear | 3 | PASS (thin but real) |
| `/collections/national-teams` | National Soccer Teams | 738 | PASS |
| `/collections/2026-national-qualified-teams` | 2026 National Team Soccer Gear | 635 | PASS |
| `/collections/2026-national-team-soccer-fan-gear` | 2026 National Team Soccer Apparel & Fan Gear | 637 | PASS |
| `/collections/nike-haaland-pe-pack` | Erling Haaland Soccer Cleats | 9 | PASS |
| `/collections/erling-haaland` | Erling Haaland | 32 | PASS |
| `/collections/club-america` | Club America Soccer Jerseys, Apparel, & Gear | 53 | PASS |
| `/collections/club-teams` | Soccer Club Teams | 1140 | PASS |
| `/collections/united-states-men-women` | USA National Soccer Team Jerseys, Apparel & Gear | 100 | PASS |
| `/collections/shorts` | Men's Soccer Shorts | 75 | PASS |
| `/collections/2026-fifa-world-cup-cards-stickers` | 2026 FIFA World Cup Cards & Stickers | 4 | PASS |
| `/collections/trading-cards` | Soccer Trading Cards from Topps & Panini | 9 | PASS |
| `/collections/soccer-socks` | Soccer Socks | 38 | PASS |
| `/collections/shin-guards` | Soccer Shin Guards | 56 | PASS |
| `/collections/soccer-shorts` | 404 Page not found | 0 | **REJECTED, 404.** Replaced with `/collections/shorts` |

**Two FIFA-named collection slugs 301-redirect to federation-named destinations, and the brief must
use the destination:**

- `/collections/2026-fifa-world-cup-qualified-teams` -> `/collections/2026-national-qualified-teams`
- `/collections/2026-fifa-world-cup` -> `/collections/2026-national-team-soccer-fan-gear`

That rename is convenient beyond tidiness: the destination slugs and anchors carry no FIFA token,
so they are safe to link from a Nike, Puma or Umbro page, which the source slugs were not.

**`/collections/club-teams` product count moved from 1,118 (Batch 16, two days ago) to 1,140.**
Cheap evidence that re-validating rather than reusing a two-day-old signal is the right posture.
