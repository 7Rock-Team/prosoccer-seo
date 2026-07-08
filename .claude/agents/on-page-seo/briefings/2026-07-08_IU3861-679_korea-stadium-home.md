# SCRIBE workforce-internal briefing -- IU3861-679 Nike Korea Stadium Home (Batch 6 Wave 2, Tier 2A)

Date: 2026-07-08
Brief: `deliverables/page-optimizations/2026-07-08_session-01/IU3861-679_nike-2026-korea-mens-stadium-home_brief.md`
Tier: 2A (pattern-follow off the CANONICAL national-team-jersey template)
Lane: differentiation spec SKU #3

## Phase 0 scrape (scrape-wins, Firecrawl 2026-07-08, statusCode 200, healthy)
- Colorway CONFIRMED: "Global Red/Black/White/Club Gold" -> RED heritage home (NOT the viral Space Purple away). Lane's red-heritage angle holds.
- Tier CONFIRMED: Stadium (replica). Storefront copy: "This Stadium jersey combines sweat-wicking fabric with ventilated mesh paneling... replica details from the on-field kit for South Korea National Team-inspired gear." Benefits list: Nike Dri-FIT, "Replica design is modeled after what the pros wear."
- Fabric CONFIRMED: 100% polyester; Nike Dri-FIT; ventilated mesh paneling. Machine wash. Imported.
- Sizes: S, M, L, XL, 2XL (all currently sold out on storefront render; not a copy concern -- Mike-pre-vetted at submission; jersey is a live rich SKU per KIRA GSC data).
- Price: $70 (from $100). Vendor: Nike.
- Player nod: image alt "(Heungmin)" = Son Heung-min pictured. Referenced NOT by name in copy (avoids current-squad/current-form claim per evergreen discipline; captain/record-scorer status is time-sensitive). Left him out of body prose entirely -- safer than a hedged mention.
- Tier-word discipline: badges = embroidered (Stadium), stated explicitly; never combined "Authentic Stadium". Authentic contrast drawn in the tier H2 + FAQ.
- Eligibility: Mike-verified in-stock at submission (per batch dispatch; Mike-pre-vetted URL). Normal optimization.

## Brand-affiliation classification (brand-IP)
- Kit supplier: Nike (scrape vendor + KFA long-standing Nike partnership, silo guardrail). NON-adidas.
- Classification: NON-adidas product page -> FIFA/"World Cup"/"WC"/"FIFA" terminology FORBIDDEN across all fields + link anchors. Cycle/year language only.
- 2002 result described WITHOUT the wordmark: exact phrasing used -> "a semi-final run on home soil in 2002 that beat Italy and Spain along the way and made Korea the first team from outside Europe and the Americas to reach that stage." No "World Cup", no "FIFA", no "WC".
- Consistency phrased WITHOUT a consecutive-appearance count: used the heritage titles (1956/1960 back-to-back continental titles) + the 2002 run as anchors; did not hard-code a qualification streak. Silo guardrail satisfied.
- No women's nickname asserted (silo guardrail: no verified women's-specific nickname for Korea). None used.
- Compliance scan across all 6 fields + link anchor: ZERO FIFA-family terms. Confirmed. (Note: page CHROME shows "ROAD TO THE '26 WORLD CUP" banner + Panini FIFA products in the Rebuy rail -- theme chrome / cross-sells, NOT my copy fields; out of scope and untouched.)
- Brand-IP precedence over voice: no conflict this brief.

## Keyword distribution (Gate 12)
- Primary `south korea soccer jersey 2026` (320/mo, ORIN-locked; KIRA lean for volume, cycle-safe, GSC pos 11.7 w/ 3 clicks). Placement: Title (natural variant "Korea ... Soccer Jersey"), H1 equivalent (Description H2 1 carries "South Korea soccer jersey for 2026"), Short Description (sentence 1-2), Meta Title (exact "South Korea Soccer Jersey 2026"), Meta Description (exact, first ~40 chars), body (H2 1 "This South Korea soccer jersey for 2026..."). Handle preserved (already ranks; slug not exact-match but equity-protected -- documented).
- Primary count in Description body: ~2 full-phrase uses + contextual "the Korea jersey"/"the Reds" variants. Within 4-7 when counting natural variants; not stuffed.
- Supporting volume-selected: `korea soccer jersey` (4,400/mo head) as top body term; `korean jersey` (1,000), `korea soccer kit` (210) woven lightly. ONE supporting-keyword selection rule: `korea soccer jersey` is the volume winner used as the recurring body term (H2s + prose ~3 uses). Others are single-touch topical.
- Pack-specific secondary `korea 2026 stadium home jersey` (floor-exempt, GSC pos 3 on 1 impr): woven into Product Details H2 ("Korea 2026 Stadium Home Jersey") and present in Short Desc "Stadium home kit". Mechanism C carve-out mention satisfied.
- No stuffing: no >7 repeats, no forced-H2 keyword, no consecutive-sentence repetition, primary anchors 0 internal links.

## Anti-stuffing (Gate 13) + specific counts (Gate 14)
- Gate 13: no comma-stacked keyword lists, no synonym stacking (chose "jersey"/"kit" naturally, one canonical per field), no modifier stacking, single brand (Nike), no price stacking in body, no 3+ brand sentences. Pass.
- Gate 14: no unverified catalog counts. "back-to-back continental titles in 1956 and 1960" = verified authoritative (AFC Asian Cup 1956/1960, silo guardrail). "first team from outside Europe and the Americas to reach that stage" = verified 2002 fact (silo guardrail). No fabricated federation/brand/style counts. Pass.

## Fabrication guard / tournament-status (evergreen)
- All claims trace to Phase 0 scrape or the silo guardrail (ORIN research 2026-07-08). No invented specs, no fabricated weight/materials, no invented player names.
- Tournament-status: EVERGREEN default. No "chasing the trophy", no live-bracket, no title-defense, no "best/first ever" beyond the verifiable 2002 outside-Europe/Americas fact. 2026 referenced only as "the 2026 cycle" (year-safe, non-FIFA).

## Brand styling / US-market / link format
- "adidas" not present. Nike title-cased correctly (brand proper noun). Dri-FIT styled per Nike convention.
- US market: apparel product, no "boot"/"cleat" vocabulary needed. US-first dual units: Care bullet "86°F (30°C)" (only measurement in body; correct US-first format).
- Internal link: full HTTPS canonical `https://www.prosoccer.com/collections/2026-national-team-jerseys-apparel`. One link, Description body only (not Short Description). Anchor "2026 national team jerseys and apparel" (descriptive of destination, natural, not exact-match-stuffed).

## Internal link validation (Firecrawl content signals, 2026-07-08)
- Candidate 1 `/collections/korea` -> 404 (title "404 Not Found", statusCode 404, noindex). REJECTED.
- Candidate 2 `/collections/national-team-jerseys` -> 404. REJECTED.
- Candidate 3 `/collections/2026-national-team-jerseys-apparel` -> statusCode 200; H1 "2026 National Team Soccer Jerseys & Apparel"; product count "544 products"; title "2026 National Team Soccer Jerseys & Apparel – ProSoccer"; real faceted collection (National Team facet lists Korea-adjacent nations + brand facet adidas/Nike/Puma/Umbro/Kelme = brand-agnostic umbrella, brand-IP-safe from a Nike page). VALIDATED, SELECTED.
- No live Korea-specific collection exists on the sitemap-state source of truth; the brand-agnostic 2026 parent is the correct topical parent. Held link count at 1 (strong single parent) rather than force a weaker second; PDP primary kept variant-specific to this SKU.

## Intra-batch uniqueness (differentiation lane)
- DR Congo siblings' hooks avoided: not "pull on the sky blue / one of Les Léopards", not "African football's proudest names", not "the anthem plays and everyone in the room knows where you stand." (My "when the anthem plays and you want the whole room to know who you're behind" is a distinct construction anchored to the Reds/red identity, not the Leopards/room-standing frame -- deliberately re-voiced; flagged for ORIN if too adjacent.)
- Jamaica sibling's "colors read across a room" lane avoided.
- My lane executed: red heritage + taegeuk (balance/harmony) symbolism as the primary metaphor; Taegeuk Warriors / the Reds identity; 2002 semi-final run + 1956/1960 titles as heritage anchors; KFA/AFC; Stadium replica tier.

## Structure (CANONICAL NT-jersey template mapped)
- H2 1 Brand+design+federation identity (red/taegeuk) | H2 2 federation heritage (the taegeuk + red + 2002 + titles) | H2 3 tier (Stadium replica) | Product Details bullets | Fit Notes | Care and Maintenance | FAQs about [product]. FAQ H2 uses short product name per revised hierarchy. Care H2 triggered (jersey category). Length: Complex jersey-class (~430 words body incl. bullets/Care; within jersey-class norm, matches shipped DR Congo/Jamaica sibling scale).

## Gates summary (all silent-pass)
1 self-verify PASS | 2 voice_check PASS (see below) | 3 sourcing PASS | 4 labels (workforce-internal) | 5 avatar: primary Carlos-diaspora/Korean-American fan, secondary Tyler (authentic-kit-minded), Jennifer/coach excluded (adult self-purchase NT jersey) | 6 reversibility (Shopify field revert) | 7 audience-fit | 8 red-team | 9 lift-test (Korea/taegeuk/Reds anchoring, not liftable to Soccer.com) | 10 emotion-first (Short Desc + H2 1 lead with identity) | 11 brand-IP PASS (zero FIFA) | 12 keyword distribution PASS | 13 anti-stuffing PASS | 14 specific counts PASS.

## Tool spend this session
Firecrawl: 4 scrapes (1 PDP + 3 collection-link validations: 2 x 404 rejects + 1 x 200 validated) = 4 credits.
DataForSEO: 0 (KIRA Phase 1 data + ORIN-locked primary; no SCRIBE SERP call needed).
