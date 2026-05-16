# SCRIBE Briefing: 2026-national-team-soccer-fan-gear (whitelabel audit + regen)

- **Date:** 2026-05-16
- **Deliverable:** `deliverables/page-optimizations/whitelabel-audit/2026-05-16_2026-national-team-soccer-fan-gear_audit-and-regen.md`
- **Page URL:** `/collections/2026-national-team-soccer-fan-gear`
- **Page type:** Tournament-scoped collection (brand-agnostic umbrella)

## Brand-affiliation classification (per `context/brand-ip-constraints.md`, applied per SCRIBE Section 2 Step 4c)

**Classification: brand-agnostic umbrella.**

**Reasoning:**
The page's subject scope, "2026 National Team Soccer Fan Gear," covers all 48 federations participating in the 2026 tournament. The federations span multiple kit suppliers: 14 Adidas-kitted federations (Argentina, Mexico, Germany, Spain, Belgium, Japan, Algeria, Saudi Arabia, Colombia, Curaçao, Qatar, Scotland, South Africa, Sweden), 12 Nike-kitted federations (USA, Brazil, Canada, England, France, Netherlands, Norway, Croatia, South Korea, Australia, Turkey, Uruguay), 11 Puma-kitted federations (Portugal, Switzerland, Czech Republic, Senegal, Morocco, Ghana, Ivory Coast, Egypt, Austria, New Zealand, Paraguay), and smaller-supplier federations (Reebok for Panama, 7Saber for Uzbekistan, etc.). The 919-product live inventory on this page reflects this multi-brand mix (jersey accessories, hats, scarves, flags from multiple federation-supplier combinations).

**Constraint application:**
Because this is a brand-agnostic umbrella (not an Adidas-only context), the FIFA-trademarked terminology family ("World Cup", "FIFA World Cup", "WC", "FIFA" in commercial promotional contexts, and clear variations) is **FORBIDDEN** across all six customer-facing fields plus internal link anchor text.

The year "2026" alone remains permitted (year reference is not a FIFA trademark invocation).

**Federation-anchored substitution language applied:**

| Restricted (would have appeared in v1 draft) | Federation-anchored substitution used in v2 |
|---|---|
| "2026 World Cup" | "2026 tournament" / "2026 international tournament" |
| "World Cup history" | "international tournament soccer has ever staged" |
| "World Cup scarves" | "Federation scarves" |
| "World Cup branding" | "tournament branding" |
| "World Cup window" | "tournament window" |
| "FIFA's official store" | (removed; reframed without commercial FIFA reference) |
| "World Cup 2026 fan gear" (FAQ) | "2026 fan gear" |
| "post-WC2026" (workforce-internal slug section) | "post-tournament" |

**Gate 11 scan results (per SCRIBE Section 11 Gate 11):**
- Title: clean
- Slug: no change recommended (current slug `2026-national-team-soccer-fan-gear` contains no FIFA terms; "2026" alone is permitted)
- SEO Meta Title: clean
- SEO Meta Description: clean
- Short Description: clean
- Long Description (including FAQ): clean
- Internal link anchor text: both anchors clean ("the official jerseys for the tournament", with "tournament" alone permitted; "Every nation in the field", clean)

**Verbatim quotation exception:** the Phase 1 audit table in the deliverable quotes whitelabel's current live meta description verbatim (which contains "World Cup"). This is audit citation of someone else's published copy, not new ProSoccer copy. Quotation marks and table formatting make the citation context clear. Per Mike's framing, the constraint is on ProSoccer USING the terminology, not on auditors CITING that someone else used it.

## Per-team brand-affiliation verification

For this brand-agnostic umbrella page, per-team verification was less critical than for a single-federation collection page. The relevant verification: confirmation that the multi-brand mix is real (it is, per Tavily research run 2026-05-16 citing nss-sports, footyheadlines, and manofmany sources). Future SCRIBE briefs for single-federation pages (e.g., Mexico, Argentina, USA) need to per-team verify the kit supplier during topic research at brief time, not assume from the reference list in `context/brand-ip-constraints.md`.

## Topic research summary (6 Tavily queries, 2026-05-16)

Key facts grounded in the body copy:
- 2026 international tournament opens June 11 at Estadio Azteca (Mexico vs South Africa); 16 host cities US/Mexico/Canada; 104 matches; final July 19 at MetLife Stadium.
- Adidas 14 federations, Nike 12, Puma 11 (multi-brand mix supports the brand-agnostic umbrella classification).
- Host-city scarves released as collector pieces; Atlanta and Toronto editions reportedly sold out at the official tournament store (referenced in v1 with FIFA framing; reframed in v2).
- Casa México Los Angeles opens June 11 at LA Plaza de Cultura y Artes as official Mexican government hospitality with live viewing parties.
- SoFi Stadium hosts 8 matches including USA opener (June 12 vs Paraguay) and quarterfinal (July 10).
- Rose Bowl in Pasadena historically hosts El Tri friendlies.
- Fan gear culture insight: "Scarves are the heartbeat of soccer fandom" (from ProSoccer's own blog and DFW fan gear guide); fan gear has expanded from matchday-only to everyday identity layer.

## Internal links validated 2026-05-16 via Firecrawl MCP

1. `/collections/2026-national-team-jerseys-apparel`, 200 OK, H1 "2026 National Team Soccer Jerseys & Apparel", 691 products.
2. `/collections/national-teams`, 200 OK, H1 "National Soccer Teams", 1,092 products. Also the proposed post-tournament redirect target.

## Cost log

- Firecrawl credits used this session: ~15 (1 live audit scrape ~5 credits + 2 internal-link validation scrapes ~5 each).
- Tavily search calls: 6.
- Within SCRIBE's monthly Firecrawl envelope (100/month) and within workforce DataForSEO cap.
