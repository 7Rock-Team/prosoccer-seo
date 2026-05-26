# SCRIBE session briefing 2026-05-26: UAE 2026 Men's Home Stadium Jersey

**Session goal:** Phase B test of the Fresh Optimization workflow on a live PDP. Produce visible brief plus workforce-internal briefing for `/products/adidas-2026-united-arab-emirates-mens-stadium-home-soccer-jersey`.

**Status:** Drafted, holding at GATE for Mike review.

## Brand-affiliation classification

- **Page type:** product (PDP)
- **Brand:** adidas (licensed UAEFA kit supplier for the 2026-2028 cycle)
- **Classification:** Adidas-licensed product page. Per `context/brand-ip-constraints.md`, this page is in the "FIFA terminology family allowed" set (Adidas product pages, Adidas-only national-team kit product pages).
- **Strategic choice:** terminology family is legally permitted but NOT used. UAE did not qualify for the 2026 World Cup (eliminated by Iraq in AFC Round 5 playoffs, November 2025). Using "World Cup" terminology on a non-qualifying team's product page would create an intent mismatch in SERPs and miscue the customer's expectations. Federation-anchored language ("UAEFA", "Al-Abyad", "AFC Asian Cup 2027") carries the page instead.
- **Compliance scan:** swept Title, Slug, Meta Title, Meta Description, Short Description, Long Description, and internal-link anchor for the restricted terminology family. No occurrences. Clean.

## Avatar scope

- **Primary:** Carlos (the Fan / diaspora). Emirati expats and Middle Eastern soccer fans in the US. The LA market has meaningful Middle Eastern diaspora; UAE diaspora skews professional and Gulf-connected. Carlos drives the headline copy (identity-anchored lead, federation visual identity, Al-Abyad nickname, qualifying-run honesty).
- **Secondary:** Tyler (the player / collector buying an AFC kit because it's adidas with credible tech). Tyler shows up in the Stadium-vs-Authentic H2 and the fit-and-sizing detail.
- **Excluded:** Jennifer (adult national-team jerseys are typically self-purchase, not parent-purchase); Mike the Coach (team uniforms route through `/pages/team-orders`, not PDPs).
- **Cross-avatar landing:** a US-based Middle East follower searching for AFC kits in general may land here; the body copy serves them via the AFC Asian Cup 2027 framing in the final H2.
- **AIDAR stage:** Desire / Action. PDPs are point-of-decision pages; the buyer is in active consideration.

## Topic research (Tavily / web search, 2026-05-26)

UAE was less familiar than the well-known set (Mexico, Argentina) so research ran on the deeper end of the familiarity scale (4 web search queries, all under "AFC + UAE + 2026" scope; well-known-topic minimum is 2 to 5, unfamiliar floor is 5 to 10). Outputs:

1. **2026 World Cup qualification status:** UAE eliminated. Lost 2-1 to Qatar in group play, finished second in their group, advanced to AFC Round 5, lost 2-1 aggregate to Iraq in November 2025 on a stoppage-time penalty. Iraq advanced to the intercontinental playoff. UAE will NOT be at the 2026 World Cup. (Sources: beIN Sports, The National, Bolavip, Gulf News.)
2. **adidas kit supplier confirmed for 2026-2028 cycle.** White base, red V neck, red shoulder stripes, sleeve patterning lifted from the UAEFA Arabic-script logomark. Doubleknit construction. Climacool weave on main panels. Red and subtle grey graphics. (Sources: Football Shirt Culture, Football Fashion, adidas.com.)
3. **Notable players for 2026:** Ali Mabkhout (top scorer, 52 goals in 103 caps as of 2025). Fabio Lima (recent qualifier hero, scored 4 in a 5-0 win over Qatar in earlier rounds). Younger generation: Khalifa Al Hammadi, Ali Saleh, Mohamed Al Shamsi, Yahya Al Ghassani. Coach: Paulo Bento (Portuguese). FIFA ranking around 67th. Omar Abdulrahman ("Emirati Messi") retired 2022, not on the active roster. (Sources: Tribuna, 365scores, FOX Sports, Wikipedia.)
4. **AFC Asian Cup 2027:** hosted in Saudi Arabia, 7 January to 5 February 2027. UAE qualified, drawn into Group E with South Korea, Vietnam, and Lebanon/Yemen. 24-team tournament across Riyadh, Jeddah, Al Khobar. (Sources: Wikipedia, asiancup2027.sa, The National, Inside World Football.)
5. **UAE nickname:** "Al-Abyad" (the Whites). Anchored in the kit color across decades.

Topic substance integrated across H2s: kit-supplier history, federation visual identity, Stadium-vs-Authentic distinction (worked-example pattern from product-page-playbook), fit-and-sizing, forward-looking AFC Asian Cup 2027 frame.

## Field-by-field reasoning

### Title (Product Title): `adidas United Arab Emirates 2026 Men's Home Stadium Soccer Jersey`

Minor reorder from current (`adidas 2026 United Arab Emirates Men's Stadium Home Soccer Jersey`). Country before year reads more naturally for the avatar's search language. "Home" before "Stadium" follows product-hierarchy convention (the kit is the Home kit; "Stadium" is the edition tier). "Men's" stays as the gender qualifier (the collection carries Women's and Youth variants under the same federation, so the tier marker is informative). 64 characters, well within Shopify Product Title norms.

### Slug: no change

Existing slug `adidas-2026-united-arab-emirates-mens-stadium-home-soccer-jersey` is descriptive, contains both "united arab emirates soccer jersey" and "adidas" head-term variants, and has been live long enough to carry inbound link equity. Migration risk and 301 management overhead not justified for a slug already serving the primary keyword cleanly.

### Meta Title: `UAE Soccer Jersey 2026 | adidas Stadium Home Kit` [48 chars]

Primary keyword "UAE Soccer Jersey" front-loaded for SERP discovery. Year qualifier "2026" right behind. Pipe-separated brand + edition tail. 48 characters fits the 50 to 60 desktop target with margin to spare; mobile cut around 40 chars still surfaces "UAE Soccer Jersey 2026 | adidas Stadi" which is recognizable.

Brand convention: lowercase "adidas" matches the brand's official treatment and the product page's existing H1 voice.

**Expected lift band:** the page currently has NO custom SEO Meta Title (Shopify fallback emits the verbose product title plus shop name, around 77 chars, getting truncated). A custom meta title that front-loads the head term plus avoids truncation is a routine +0.3 to +0.8 CTR percentage point lift on a page with existing impressions. Without a live GSC reading on this URL, the band is best-estimate.

### Meta Description: `UAE 2026 home soccer jersey by adidas. White-and-red UAEFA federation design, Climacool ventilation, doubleknit build. Pick up the Emirati supporters' kit.` [155 chars]

155 chars sits in the 150 to 158 target. Primary keyword in first 38 characters (Google bolds the match). Federation-anchored language ("UAEFA federation"), real product detail ("Climacool ventilation", "doubleknit build"), and a product-anchored CTA ("Pick up the Emirati supporters' kit") that speaks to Carlos directly rather than to the store.

**Expected lift band:** the page currently has empty meta description. Broken-state-to-competent-state on a PDP with existing impressions typically lifts CTR +0.4 to +1.0 percentage points. The exact landing depends on GSC baseline (currently unknown for this URL); SCRIBE flags GSC inspection as a Mike-side validation step.

### Short Description

Old copy fails on five voice-rule vectors: marketing-cliche opener ("Step onto the pitch with pride"), vague filler ("embodies the spirit of the team"), AI-cliche close ("Embrace the game with confidence and style"), generic "piece of football history" overreach, no avatar anchoring. The whole paragraph is brand-swappable to any country's jersey, which fails Gate 9 (positioning lift-test).

New copy leads with identity ("the supporter whose flag carries the red, black, white, and green"), grounds in specific product detail (white base, red V neck, sleeve patterning from the federation's Arabic-script logomark), drops in the federation nickname Al-Abyad as the close. 46 words, within 40 to 80 target. Features support the feeling and never lead (Gate 10 Emotion-first check passes).

### Long Description

Old copy is a feature dump with no H2 structure, no brand story, no federation context, no fit guidance. Misses the product-page-playbook H2 pattern for premium kit jerseys entirely.

New copy follows the playbook's premium-kit-jersey H2 pattern:
- adidas and the UAEFA (brand + federation context, design story)
- Stadium Edition vs the Authentic Cut (edition tier distinction)
- Fit and Sizing (avatar-anchored fit guidance)
- What You're Buying Into (forward-looking context, avatar's emotional anchor)

Word count approximately 330, sits inside the 200 to 400 product-page body target. Primary keyword "UAE soccer jersey" appears twice exact-match (intro of first H2, intro of final H2) plus multiple topical variants ("UAE home", "UAE shirt", "the kit", "Stadium edition"). Density inside the 1% to 2% target.

The final H2 is the highest-risk paragraph (mentions the qualifying-run elimination). Strategic call: Emirati supporters know UAE is out; pretending otherwise would feel inauthentic. The forward-looking AFC Asian Cup 2027 frame turns the disappointment into continued-support context, which is exactly Carlos's emotional anchor for buying the kit in a non-tournament year.

### Internal link

One link selected: `/collections/adidas-soccer-jerseys`. Anchor `adidas's federation kit lineup` in the final H2 "What You're Buying Into". Topically relevant (adidas brand-line collection where this product sits), live-validated 200 OK with 437 products and the correct H1 "Adidas Soccer Jerseys" on 2026-05-26.

**Skipped candidates:**
- `/collections/uae`: 404 (does not exist).
- `/collections/united-arab-emirates`: 404 (does not exist).
- `/collections/2026-national-team-soccer-fan-gear`: live 200 OK with 935 products, but already in the page breadcrumb; adding a body link would duplicate. Skipped to avoid redundancy.
- `/collections/2026-national-qualified-teams`: live but intent-mismatched (UAE is not a qualified team for the 2026 World Cup). Skipping for accuracy.
- `/collections/adidas-2026-fifa-world-cup-soccer-jerseys`: live Adidas WC umbrella; UAE is not in that tournament; intent-mismatched on this PDP. Skipping.

**Flag for VERITAS:** no UAE-specific collection page exists on ProSoccer (`/collections/uae` and `/collections/united-arab-emirates` both 404). Other AFC nations may face the same gap. If UAE search demand justifies it, a collection-page creation request belongs in VERITAS's URL architecture queue.

### External link

One outbound link: `https://www.asiancup2027.sa/` (official AFC Asian Cup 2027 tournament site). Anchor `AFC Asian Cup in Saudi Arabia`. Federation-tier authoritative source, topical to the final H2's forward-looking framing. Single outbound link on a product page is within reasonable e-commerce convention; risk of link-equity leak is small relative to the topical credibility it adds for the AFC-focused reader.

## Voice check status (per-string)

- Title: PASS (no forbidden words, no dashes)
- Slug: PASS (unchanged)
- Meta Title: PASS
- Meta Description: PASS
- Short Description: PASS
- Long Description: PASS
- Brief file as a whole: PASS (will run `scripts/voice_check.py` before commit)

## 11-gate self-verify

- Gate 1 Self-verification: numerical claims sourced (FIFA ranking ~67, AFC Round 5 result, Group E composition for Asian Cup 2027, kit color scheme, doubleknit + Climacool spec). Current state verified against live WebFetch of the PDP.
- Gate 2 Voice check: pass on every staged string and the brief file.
- Gate 3 Sourcing and traceability: web search citations logged above.
- Gate 4 Severity, Confidence, Expected Lift Band: severity HIGH (empty meta description on a live product), confidence MEDIUM (no GSC baseline for this URL yet; baseline-relative lift band is best-estimate).
- Gate 5 Avatar fit named (full-scope): Carlos primary with AIDAR Desire/Action, Tyler secondary, Jennifer and Mike the Coach excluded with reasoning, cross-avatar AFC follower noted.
- Gate 6 Reversibility: any field change is restorable by reverting to the captured Current state strings above.
- Gate 7 Audience-fit summary: brief reads cleanly for Mike. No client-adjacent layer needed for Tony.
- Gate 8 Red-team pass: weakest link is the "qualifying run ended" line in the final H2. Tony might challenge it on commercial grounds. Counter: Emirati supporters know the result; honesty plus a forward-looking 2027 frame is more credible than glossing. Optional fallback wording on Mike's call: replace "The qualifying run ended in the AFC playoffs against Iraq, but" with "Heading past the qualifying cycle," (softer, still forward-looking, less specific).
- Gate 9 Positioning lift-test: the brief includes specific federation detail (UAEFA Arabic-script logomark, Al-Abyad nickname, 2026-2028 cycle specificity, AFC Asian Cup 2027 Group E composition). Could not be lifted onto Soccer.com unchanged; the depth signals ProSoccer's High-Performance Expert positioning rather than volume-retailer copy.
- Gate 10 Emotion-first check: Short Description opens with identity ("the supporter whose flag carries the red, black, white, and green") and Long Description closes on emotional anchor ("the kit they pull on for that"). Features support throughout.
- Gate 11 Brand IP compliance scan: clean. World Cup terminology family scanned across all six fields plus internal and external link anchors; no occurrences. Strategic choice, not a legal blocker.

## Sources cited

- WebFetch `https://www.prosoccer.com/products/adidas-2026-united-arab-emirates-mens-stadium-home-soccer-jersey` (2026-05-26): current Title, slug, H1, meta description absence, breadcrumb, price, internal links.
- WebFetch `https://www.prosoccer.com/collections/adidas-soccer-jerseys` (2026-05-26): validated 200 OK, H1 "Adidas Soccer Jerseys", 437 products.
- WebFetch `https://www.prosoccer.com/collections/uae` (2026-05-26): 404.
- WebFetch `https://www.prosoccer.com/collections/united-arab-emirates` (2026-05-26): 404.
- WebFetch `https://www.prosoccer.com/collections/2026-national-team-soccer-fan-gear` (2026-05-26): validated 200 OK, 935 products.
- WebSearch 2026-05-26: UAE 2026 World Cup qualification status (eliminated by Iraq, AFC Round 5).
- WebSearch 2026-05-26: UAE kit supplier confirmed adidas, 2026-2028 cycle, design detail.
- WebSearch 2026-05-26: UAE roster, Ali Mabkhout / Fabio Lima / Paulo Bento, FIFA ranking ~67.
- WebSearch 2026-05-26: AFC Asian Cup 2027 in Saudi Arabia, UAE in Group E with South Korea / Vietnam / Lebanon-or-Yemen, dates 7 Jan to 5 Feb 2027.
- Product description content supplied by Mike (2026-05-26 chat message): existing Short and Long Descriptions verbatim.

## Cost tracking

- Firecrawl credits used: 0 (this session used WebFetch and WebSearch rather than firecrawl-mcp tools).
- DataForSEO estimated spend: $0.
- Playwright sessions: 0.
- Web search queries: 4 (UAE WC qualification, UAE kit supplier, UAE roster, AFC Asian Cup 2027).
- WebFetch calls: 5 (1 PDP scrape + 4 internal-link validations).
- voice_check.py runs: 1 planned on the brief file pre-commit.

## Open questions for Mike

1. The qualifying-run line in the final Long Description H2 acknowledges the elimination directly. If you prefer a softer treatment, swap "The qualifying run ended in the AFC playoffs against Iraq, but" with "Heading past the qualifying cycle,". Flag your call.
2. No UAE collection page exists (`/collections/uae` and `/collections/united-arab-emirates` both 404). If demand justifies it, that's a VERITAS URL-architecture task; let me know if you want me to draft the brief for ORIN.
3. External link to `asiancup2027.sa` on a PDP is a small departure from typical e-commerce convention. Federation-tier authoritative source justifies it; flag if you'd rather keep PDPs entirely internal.
4. Expected lift bands are best-estimate without GSC data on this URL. If GSC MCP auth lands or you want me to pull GSC manually for this URL, the bands tighten.

## Self-verification status

Pass. All numerical claims sourced, all internal-link URLs live-validated, all citations match observed live state on 2026-05-26.
