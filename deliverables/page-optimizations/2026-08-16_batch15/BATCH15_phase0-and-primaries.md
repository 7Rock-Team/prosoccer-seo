# Batch 15: Phase 0 scrape and primaries proposal

**Built:** 2026-08-18 | **Status:** HELD for Mike's approval. Nothing dispatched, no brief written.
**Selection:** the ten approved 2026-08-18, with rows 9 and 10 confirmed (JH7718, IQ2162-900).

---

## 1. Phase 0 scrape: all ten fetched live 2026-08-18

Every page fetched with full TLS verification (see §5). SKUs for rows 5 and 6 were unknown at selection and are now resolved: **IB4477-101** and **IQ2399-900**.

| # | SKU | Handle | Price | Stock | Source copy |
|---|---|---|---|---|---|
| 1 | HQ3158-001 | `nike-tiempo-ligera-pro-firm-ground-soccer-cleats-su26` | $120.00 to $150.00 | 10/37 | 481 ch, 5 lines |
| 2 | HJ2147-003 | `nike-phantom-6-high-elite-firm-ground-soccer-cleats-shadow-pack-fa25` | $192.00 to $295.00 | 12/30 | 726 ch, 5 lines |
| 3 | JR8971 | `adidas-f50-league-indoor-soccer-shoes-born-for-goals-pack-sp26` | $68.00 to $90.00 | 24/28 | 449 ch, 8 lines |
| 4 | JR5899 | `adidas-predator-elite-fold-over-tongue-artificial-grass-soccer-cleats-born-for-goals-pack-sp26` | $210.00 to $280.00 | 10/18 | 829 ch, 11 lines |
| 5 | IB4477-101 | `nike-tiempo-ligera-pro-turf-soccer-shoes-break-em-pack-fa26` | $139.99 | 18/34 | 423 ch, 5 lines |
| 6 | IQ2399-900 | `nike-phantom-6-low-academy-turf-soccer-shoes-breakout-pack-su26` | $94.99 | 32/36 | 453 ch, 5 lines |
| 7 | IB3094-800 | `nike-phantom-6-low-pro-firm-ground-soccer-cleats-erling-haaland-pack-fa25` | $102.00 to $170.00 | 20/30 | 884 ch, 6 lines |
| 8 | IF8508-600 | `nike-vapor-17-elite-firm-ground-soccer-cleats-break-em-pack` | $259.99 | 28/32 | 451 ch, 5 lines |
| 9 | JH7718 | `adidas-f50-league-indoor-soccer-shoes-coral-blaze-pack-fa25` | $54.00 to $90.00 | 10/30 | **205 ch, 4 lines** |
| 10 | IQ2162-900 | `nike-phantom-6-high-club-firm-multi-ground-soccer-cleats-breakout-pack-su26` | $69.99 | 26/30 | 488 ch, 5 lines |

**All ten are confirmed raw white-label**, which is exactly what an unoptimized incumbent should look like and confirms the selection:
- Meta description is the theme's body-derived fallback on **10 of 10** (it opens by repeating the product title).
- In-body internal links: **0 of 10.** Every one will need the internal link the gate hard-fails on.

**Row 9 has thin source copy**, 205 characters across 4 lines, roughly a quarter of row 7's. SCRIBE will have less to build specs from and may need to lean on the adidas F50 League platform facts shared with row 3 rather than page-specific detail. Flagged in the dispatch, not a blocker.

### Two scrape artifacts SCRIBE must not carry through

1. **Row 4's manufacturer copy opens with `Football boots with Nanostrike technology`.** The standing rule is "cleats" or "shoes", never the UK term. Source text, not ours, and it must be rewritten.
2. **Rows 3, 4 and 9 render brand technology in all caps** (POWERSPINE, NANOSTRIKE, PRIMEKNIT). The casing rule requires title case: Powerspine, Nanostrike+, Primeknit.

Both are in the input, so both will be stated as forbidden in each dispatch.

---

## 2. Proposed primaries

Volumes are DFS Google Ads US, pulled 2026-08-18. GSC is the page's own measured impressions, 29 days to 2026-08-14.

| # | SKU | Proposed primary | DFS/mo | Jul | GSC impr | Basis |
|---|---|---|---|---|---|---|
| 1 | HQ3158-001 | `nike tiempo ligera pro fg` | 140 | 590 | 20,318 | v3 incumbent, and see §3.1 |
| 2 | HJ2147-003 | `nike phantom 6 high elite fg` | **210** | 720 | 1,610 | v3 incumbent, top of 7 |
| 3 | JR8971 | `adidas f50 league indoor` | 30 | 70 | 1,469 | v3 incumbent, top of 12 |
| 4 | JR5899 | `adidas predator elite ag` | **590** | 1,300 | 1,256 | v3 incumbent; Mike's carried-forward ruling |
| 5 | IB4477-101 | `nike tiempo ligera pro turf break em` | sub-floor | | 708 | Shadow FA26 is B7-registered on the unqualified term |
| 6 | IQ2399-900 | `nike phantom 6 low academy turf breakout` | sub-floor | | 445 | **not the incumbent, see §3.2** |
| 7 | IB3094-800 | `nike phantom 6 low pro fg` | 70 | 210 | 363 | **OPEN, see §3.3** |
| 8 | IF8508-600 | `nike vapor 17 elite fg break em` | sub-floor | | 249 | Shadow FA26 is B7-registered on the unqualified term |
| 9 | JH7718 | `adidas f50 league indoor coral blaze` | sub-floor | | 698 | row 3 holds the unqualified term as incumbent |
| 10 | IQ2162-900 | `nike phantom 6 high club fg mg` | 10 | 20 | 241 | v3 incumbent, top of 4 |

Five rows take an unqualified term because they are the measured incumbent at their configuration. Five take a pack-qualified sub-floor term, which is mandatory under pack succession, not a fallback failure.

### Cannibalization check: 0 exact collisions

Run against the registry **as it will be after C-FIX Group 2 imports**, not as it is today. Full output in `cannib_final.py`.

- **0 exact collisions. 0 intra-batch duplicates.**
- Seven rows carry a registered NARROWER term (a pack-qualified sibling). That is the correct direction and is what pack succession produces.
- **Two rows flagged REVIEW, rows 3 and 9.** `adidas f50 league` (KJ6714, 880/mo) and `adidas f50 indoor` (IH4571, 320/mo) are strict token-subsets of `adidas f50 league indoor`. My read is proceed: the proposed term is more specific than both and resolves to a distinct configuration. Worth noting that both blocking terms sit on **Hyperfast** pages, a different model line, which is the B-KW-01 pattern of generic F50 demand parked on Hyperfast SKUs. Flagged rather than passed silently.

---

## 3. Three things needing a decision

### 3.1 Row 1's brief must say the primary is not the point

Per Mike's instruction. `nike tiempo ligera pro fg` earned **one impression in 29 days** while 31,131 sat on the cut-less `tiempo ligera pro`, which no PDP can own. Row 1 is briefed because HQ3158-001 is the demand holder at that configuration and therefore the likely consolidation target for B-CANNIB-01. The copy investment pays when the sibling handles are consolidated into it, not through the primary term. That reasoning goes in the brief so a later reader does not mistake the primary for the justification.

### 3.2 Row 6 takes a qualified term, a direct consequence of stock-independent incumbency

The v3 incumbent at Phantom 6 Low Academy Turf is the **Erling Haaland FA25** page at 1,256 impressions. It is out of stock on all 34 variants and was rejected from selection on that basis, but Mike ruled incumbency is stock-independent, so it still holds the unqualified `nike phantom 6 low academy turf` (50/mo).

IQ2399-900 is rank 2 at 445 impressions, so it takes `nike phantom 6 low academy turf breakout`, sub-floor.

This is the ruling working as written, and it costs a real 50/mo term to a page that cannot currently convert. If Mike would rather the in-stock page take the unqualified term, that is a deliberate exception to the stock-independence clause and needs saying explicitly. **I have not taken it.**

### 3.3 Row 7 conflicts with C-FIX Group 2 row 11, and the fix is free

Under v3 the incumbent at Phantom 6 Low Pro FG is **IQ1886-900** (Breakout SU26, 523 impressions). C-FIX Group 2 row 11 retargets it to `nike phantom 6 low pro fg breakout`, a pack-qualified term. That assignment was made under the old season-earliest rule. Under v3 the incumbent should keep the unqualified `nike phantom 6 low pro fg` (70/mo).

Two ways to resolve:

- **(a) As proposed.** IQ1886-900 takes the breakout term; row 7 (IB3094-800, rank 2 at 363) takes the unqualified term. Ships as built, but the number-two earner holds the head term.
- **(b) v3-consistent.** IQ1886-900 keeps `nike phantom 6 low pro fg`; row 7 takes `nike phantom 6 low pro fg erling haaland`, sub-floor.

**The import file does not change either way.** Row 11's shipped meta title is "Nike Phantom 6 Low Pro FG Breakout", which names model, tier, cut, surface AND pack, so it reads correctly under both. Only the registry `primary_keyword` differs. Group 2 can import today regardless; this is a registry decision, not a copy decision.

I lean (b) for consistency with the rule Mike just made, but (a) is defensible on the grounds that C-FIX was already approved. **Mike's call.**

---

## 4. Also found, not Batch 15

Two more cut-less or surface-less terms with four-figure July volume, same class as the three already logged in B-KW-01:

- **`nike vapor 17 elite`, 320/mo, 2,400 in July.** No cut, no surface.
- **`nike phantom 6 high club`, 170/mo, 320 in July.** No surface.

Both are collection terms. Not added to B-KW-01 as separate items since the pattern is already recorded there; noted so the collection workstream has them.

---

## 5. Provenance and one correction

- Phase 0: 10 pages fetched live 2026-08-18, `phase0b.py`. H1, title tag, meta description, SKU, brand, per-variant availability and price, product description block, in-body links.
- **A first-pass scrape was discarded.** It reported an identical 239-character body on all ten, which was the store's chatbot boilerplate, not product copy, and its "internal links" were the global nav. Both would have poisoned every brief with false ground truth. `phase0b.py` extracts the `product__block--description` container by tag-depth counting instead, and the results now vary per page as they should.
- **TLS:** an earlier "certificate has expired" error was investigated rather than worked around. The cause was local: this Python had no CA bundle at all (`cafile=None`, `capath=None`, certifi absent), so it could not verify any host. **prosoccer.com's own certificate is valid.** certifi was installed and every fetch in this document ran with full verification.
- Volumes: DFS Google Ads US, 2026-08-18, all fifteen terms in one call each. Four pack-qualified terms returned no volume, which is the sub-floor lock working as designed.
- Cannibalization: `cannib_final.py`, run against the post-C-FIX-Group-2 registry state.

**Nothing dispatched. Awaiting approval on §3.2 and §3.3, then SCRIBE.**
