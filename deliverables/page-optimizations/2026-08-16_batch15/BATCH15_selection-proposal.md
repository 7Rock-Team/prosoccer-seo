# Batch 15 selection proposal, re-ranked by measured GSC impressions

**Built:** 2026-08-16 | **Status:** HELD at the selection gate, awaiting Mike's approval
**Supersedes:** the 8-SKU proposal that was never written to disk (B-REG-04, now closable)
**Method change (Mike, 2026-08-16):** rank by measured GSC impressions, not DFS volume.

---

## 1. What changed and why

The queue in `work-log/2026-08-14_batch15-handoff.md` was ranked by DFS Google Ads volume. This proposal re-ranks it against a new page-level GSC pull.

**The pull.** `sc-domain:prosoccer.com`, dimension `page`, 2026-07-17 to 2026-08-14 (29 days), regex-scoped to the six model families in the queue. 2,362 rows returned against a 25,000 cap, so nothing is truncated. Variant URLs (`?variant=`) were folded into their parent handle: 631 of the first 1,000 rows were variant fragments, and not folding them would have split every page's impressions across several rows.

Live product sitemap fetched the same day: **14,402 products** across 85 sitemap files, consistent with the 14,369 recorded on 2026-08-14.

**Three filters were applied to the raw match, each of which changed the answer:**

1. **Model-line contamination.** `hyperfast`, `messi`, `mbappe` and signature PE pages were excluded from the base F50 and Predator configs. Without this, `adidas f50 pro indoor` ranks on a Hyperfast page, which is a different product.
2. **Audience contamination.** junior, jr, kids, youth excluded from adult terms.
3. **Sub-line separation.** `lv8` and `nu3` treated as distinct from the base line. Without this, `nike phantom 6 high elite fg` ranks on an LV8 page rather than the base Shadow FA25 page.

---

## 2. DFS volume against measured GSC, side by side

Config-level totals (all live pages at that configuration), both 29-day windows.

| GSC rank | Term | DFS/mo | GSC impr | prev 29d | trend | clicks | live pgs | DFS rank | move |
|---|---|---|---|---|---|---|---|---|---|
| 1 | nike tiempo ligera pro fg | 140 | **36,532** | 53,711 | -32% | 61 | 7 | 4 | +3 |
| 2 | nike phantom 6 high elite fg | 210 | 5,194 | 5,577 | -7% | 68 | 7 | 3 | +1 |
| 3 | adidas f50 league indoor | 30 | 3,122 | 3,567 | -12% | 14 | 12 | 8 | **+5** |
| 4 | nike phantom 6 low academy turf | 50 | 2,601 | 2,420 | +7% | 38 | 7 | - | - |
| 5 | nike tiempo ligera pro turf | 320 | 2,245 | 1,199 | +87% | 36 | 3 | 2 | -3 |
| 6 | nike phantom 6 low pro fg | 70 | 2,221 | 2,605 | -15% | 69 | 9 | 6 | 0 |
| 7 | nike vapor 17 elite fg | 30 | 1,711 | 3,437 | -50% | 19 | 3 | 9 | +2 |
| 8 | adidas predator elite ag | 590 | 1,709 | 2,410 | -29% | 33 | 5 | 1 | **-7** |
| 9 | nike phantom 6 low pro turf | 140 | 1,474 | 905 | +63% | 32 | 6 | 5 | -4 |
| 10 | nike vapor 17 pro turf | 10 | 905 | 570 | +59% | 9 | 2 | 13 | +3 |
| 11 | adidas f50 league mid fg | 10 | 866 | 800 | +8% | 2 | 1 | 14 | +3 |
| 12 | nike tiempo maestro academy turf | 30 | 800 | 659 | +21% | 28 | 5 | 10 | -2 |
| 13 | nike phantom 6 high club fg mg | 10 | 632 | 990 | -36% | 24 | 4 | 15 | +2 |
| 14 | nike vapor 17 elite ag | 10 | 549 | 1,764 | -69% | 6 | 2 | 16 | +2 |
| 15 | nike phantom 6 high academy turf | 70 | 364 | 137 | +166% | 7 | 4 | 7 | **-8** |
| 16 | adidas f50 club turf | 20 | 85 | 132 | -36% | 3 | 3 | 11 | -5 |
| 17 | adidas f50 pro indoor | 20 | 62 | 106 | -42% | 3 | 3 | 12 | -5 |
| 18 | nike tiempo maestro club turf | 10 | 40 | 0 | new | 0 | 2 | 17 | -1 |
| 19 | adidas f50 club mid fg mg | 10 | **0** | 0 | - | 0 | 3 | 18 | -1 |

### Where the two metrics disagree most

- **`adidas predator elite ag`: DFS rank 1, GSC rank 8.** The single biggest disagreement. 590/mo of DFS volume, stable across twelve months, but the whole config earns 1,709 impressions and is declining. It was the queue's top row; on measured demand it is eighth.
- **`nike phantom 6 high academy turf`: DFS rank 7, GSC rank 15.** 70/mo claimed; 364 impressions earned.
- **`adidas f50 league indoor`: DFS rank 8, GSC rank 3.** The reverse case. 30/mo claimed, the lowest-but-one volume in the top ten, yet it earns 3,122 impressions across 12 live pages. DFS understates this config badly.
- **`nike tiempo ligera pro fg`: DFS 140/mo, 36,532 impressions.** DFS is not wrong here so much as measuring a different thing: the config earns across hundreds of long-tail queries, not just the head term.

**`adidas f50 club mid fg mg` earns literally zero** across three live pages in both windows. It leaves the queue.

---

## 3. Two findings that change what this batch should do

### 3.1 The Tiempo Ligera Pro FG config is cannibalizing itself

Seven live pages, 36,532 impressions, and the demand is **rotating between four of them** rather than growing:

| Page | Title | prev 29d | cur 29d | change |
|---|---|---|---|---|
| `...-cleats-su26` | Nike Tiempo Ligera Pro Firm Ground Soccer Cleats **(SU26)** | 2,396 | **20,318** | +748% |
| `...-cleats-1` | ... **- Attack Pack (SP26)** | 24,944 | 6,925 | -72% |
| `...-cleats-sp26` | Nike Tiempo Ligera Pro Firm Ground Soccer Cleats **(SP26)** | 13,741 | 4,125 | -70% |
| `...-cleats` (bare) | ...**- Shadow Pack (SP26)** | 8,633 | 3,747 | -57% |

Config total fell 53,711 to 36,532 (-32%) while the winner changed. All four share SKU base **HQ3158** (colorway suffixes -001, -146, -010, -040), so they are genuine distinct products, not duplicates.

The cause is visible in the titles. **Two of the four carry no pack name at all**, only a season code: `(SU26)` and `(SP26)`. Their handles are equally undifferentiated, and `-1` is an auto-suffix Shopify appends on a handle collision. Google has four near-identical signals at one configuration and rotates which it ranks.

This is the single largest demand pool in the queue and pack-qualified metas are the exact mechanism for differentiating it, so it takes three of the ten slots. **But copy alone will not fully fix it:** the handles themselves are the root defect and handles are never changed here. A parallel VERITAS item should assess canonical or 301 consolidation. Filed as B-CANNIB-01.

### 3.2 The live-verify gate rejected four pages, and the registry check rejected four more

Every candidate was fetched live (H1, SKU, price, per-variant availability) and checked against the registry. Both gates fired.

**Rejected on stock:**

| Page | GSC impr | Stock | Verdict |
|---|---|---|---|
| `nike-phantom-6-low-academy-turf-...-erling-haaland-pack-fa25` | 1,256 | **0 of 34 variants** | out of stock entirely; earning traffic it cannot convert |
| `nike-reactx-phantom-6-low-pro-turf-...-shadow-pack-fa25` | 790 | 2 of 30 | sold through |
| `nike-tiempo-maestro-academy-turf-...-attack-pack-sp26` | 480 | 4 of 34 | sold through |
| `nike-reactx-phantom-6-low-pro-turf-...-attack-pack-sp26` | 470 | 2 of 24 | sold through |

The Erling Haaland page is the notable one: it was the top earner in its config and would have been selected on impressions alone.

**Rejected as already optimized** (present in `products-master.csv`, status `shipped`, so not orphaned incumbents at all):

| Page | Registry | Held primary |
|---|---|---|
| `nike-tiempo-ligera-pro-turf-...-shadow-pack-fa26` | IB4477-002, B7 | nike tiempo ligera pro turf shadow |
| `nike-vapor-17-pro-turf-...-shadow-pack-fa26` | IM5811-001, B7 | nike vapor 17 pro turf shadow |
| `nike-vapor-17-elite-firm-ground-...-shadow-fa26` | IF8508-001, B7 | nike vapor 17 elite fg shadow |
| `nike-phantom-6-low-pro-firm-ground-...-breakout-pack-su26` | IQ1886-900 | nike phantom 6 pro |

Ranking on GSC impressions alone would have put all four in the batch. Both gates are load-bearing.

---

## 4. THE PROPOSED TEN

All ten are live-verified 2026-08-16 (H1, SKU, per-variant stock), absent from `products-master.csv`, and sit in a config clearing the 500-impression floor.

| # | SKU | Handle | Proposed primary | DFS/mo | GSC impr | Stock | Note |
|---|---|---|---|---|---|---|---|
| 1 | HQ3158-001 | `nike-tiempo-ligera-pro-firm-ground-soccer-cleats-su26` | **nike tiempo ligera pro fg** | 140 | **20,318** | 14/38 | see §5 open question |
| 2 | HQ3158-010 | `nike-tiempo-ligera-pro-firm-ground-soccer-cleats-sp26` | nike tiempo ligera pro fg sp26 | sub-floor | 4,125 | 14/38 | no pack name to qualify on |
| 3 | HQ3158-040 | `nike-tiempo-ligera-pro-firm-ground-soccer-cleats` | nike tiempo ligera pro fg shadow sp26 | sub-floor | 3,747 | 20/42 | season code separates it from HQ3158-002 (Shadow FA26) |
| 4 | HJ2147-003 | `nike-phantom-6-high-elite-firm-ground-soccer-cleats-shadow-pack-fa25` | **nike phantom 6 high elite fg** | 210 | 1,610 | 14/30 | **blocked on C-FIX row 10** |
| 5 | JR8971 | `adidas-f50-league-indoor-soccer-shoes-born-for-goals-pack-sp26` | adidas f50 league indoor | 30 | 1,469 | 24/28 | see §5 incumbency conflict |
| 6 | JR5899 | `adidas-predator-elite-fold-over-tongue-artificial-grass-soccer-cleats-born-for-goals-pack-sp26` | **adidas predator elite ag** | **590** | 1,256 | 12/18 | **blocked on C-FIX row 12**; per Mike's carried-forward call |
| 7 | (pull at brief) | `nike-tiempo-ligera-pro-turf-soccer-shoes-break-em-pack-fa26` | nike tiempo ligera pro turf break em | sub-floor | 708 | 20/34 | shadow-pack-fa26 is already B7 |
| 8 | (pull at brief) | `nike-phantom-6-low-academy-turf-soccer-shoes-breakout-pack-su26` | nike phantom 6 low academy turf | 50 | 445 | 32/36 | replaces the out-of-stock Haaland page |
| 9 | IB3094-800 | `nike-phantom-6-low-pro-firm-ground-soccer-cleats-erling-haaland-pack-fa25` | **nike phantom 6 low pro fg** | 70 | 363 | 20/30 | **blocked on C-FIX row 11** |
| 10 | IF8508-600 | `nike-vapor-17-elite-firm-ground-soccer-cleats-break-em-pack` | nike vapor 17 elite fg break em | sub-floor | 249 | 28/32 | config decaying -50% |

Ten rows clear the floor, so ten are proposed. Nothing was padded: the next candidates down were rejected on stock (§3.2), and the four configs below the floor (`f50 club turf` 85, `f50 pro indoor` 62, `tiempo maestro club turf` 40, `f50 club mid fg mg` 0) are not worth a brief.

**Sub-floor primaries are mandatory, not failures.** Rows 2, 3, 7 and 10 sit at configurations where a live sibling already holds the unqualified term, so pack succession requires the qualified form. Volumes were pulled and returned zero, which is the sub-floor lock working.

### Pack collision check, per SKU

Run against the live sitemap, not the registry alone. Every row was checked for a concurrent live pack sibling at the same model + tier + cut + surface:

- Rows 1, 2, 3: seven live siblings at Tiempo Ligera Pro FG. Collision is real and is the point of §3.1.
- Row 4: seven live siblings at Phantom 6 High Elite FG. Shadow FA25 is the earliest live; HJ2147-001 (Shadow FA26) is already registered on the qualified form.
- Row 5: twelve live siblings at F50 League Indoor.
- Row 6: five live siblings at Predator Elite AG, all fold-over-tongue. Per Mike, the config token discriminates nothing at that surface, so the row takes the unqualified term.
- Row 7: three live siblings; shadow-pack-fa26 registered (B7), attack-pack-sp26 unregistered but nearly sold through.
- Row 8: seven live siblings; HQ2325 registered at this config, and C-FIX row 9 retargets it to `nike phantom 6 low academy turf shadow`.
- Row 9: nine live siblings.
- Row 10: three live siblings; shadow-fa26 registered (B7).

---

## 5. THREE THINGS THAT NEED MIKE'S DECISION

### 5.1 Three of the ten are blocked behind C-FIX, which is held

C-FIX rows 10, 11 and 12 retarget the exact pages that currently hold the terms rows 4, 9 and 6 need:

| Batch 15 row | Needs term | Currently held by | Registry status | Freed by |
|---|---|---|---|---|
| 4 | nike phantom 6 high elite fg | IH1779-900 (`nike phantom 6 elite fg`, cut-less) | **pending** | C-FIX row 10 |
| 9 | nike phantom 6 low pro fg | IQ1886-900 (`nike phantom 6 pro`) | **shipped** | C-FIX row 11 |
| 6 | adidas predator elite ag | HP9971 (`adidas predator elite ag`) | **pending** | C-FIX row 12 |

This is what the C-FIX document predicted. Your instruction was that C-FIX stays held, and these three rows cannot be briefed on their intended primaries until it imports. Options: release C-FIX first and run all ten; run the seven unblocked rows now and the three after; or brief all ten and hold the three at implementation. **I have not chosen. Rows 4, 6 and 9 are marked blocked, not dropped.**

### 5.2 Which Tiempo Ligera page gets the unqualified term (row 1)

Codified pack succession gives the unqualified term to the earliest-shipped live pack by season code. Three pages here are SP26 and the season code cannot separate them; and B-PACK-02b already recorded, in a different context, that the Shadow SP26 page (HQ3158-040) is "an unregistered incumbent that takes the UNQUALIFIED term."

**Following the rule literally** puts `nike tiempo ligera pro fg` on HQ3158-040, which earns 3,747 impressions, and gives a zero-volume season term to HQ3158-001, which earns 20,318.

**I propose the deviation:** give the unqualified term to HQ3158-001 (su26), the page Google already ranks for that demand. B-PACK-02b's reasoning assumed a clean Shadow SP26 to Shadow FA26 lineage and did not contemplate that two sibling pages carry no pack identity at all, which is what makes the "earliest live pack" tiebreak unresolvable here.

This is a deliberate deviation from a codified rule, so it is yours to approve or refuse. Refusing costs the batch nothing structurally: rows 1 and 3 simply swap primaries.

### 5.3 Incumbency against demand, generally (rows 5, 7, 8, 10)

The queue's premise was "optimize the earliest live incumbent, because demand accrues over a shoe's life." The GSC data contradicts that in most configs: the earning page is usually a **recent** pack, not the earliest.

The starkest case is row 6. The queue named `...-radiant-blaze-pack-fa25` as the Predator Elite AG incumbent; it earns **4 impressions**. The Born For Goals SP26 page earns **1,256**. Same at F50 League Indoor: the named `advancement-pack-fa24` incumbent earns 4, while Born For Goals SP26 earns 1,469.

I selected the earning page in every case. Where that page is not the pack-succession incumbent, it takes the unqualified term only if the incumbent has not registered it. This keeps the batch pointed at real demand, and it is a departure from how the queue was framed, so it is flagged rather than assumed.

---

## 6. Two things found on the way that are not Batch 15

- **`nike tiempo ligera pro` is 2,400/mo and unowned.** Cut-less and surface-less, so not PDP-valid under the keyword hierarchy. It belongs to a Tiempo collection. Larger than every term in this queue combined. Routed to the collection workstream.
- **B-KW-01 still outranks this batch.** From the same corpus, the `f50 hyperfast` cluster earns 4,471 impressions and nobody holds it. That remains true after the re-rank.

---

## 7. Provenance

- GSC page-level pull: `sc-domain:prosoccer.com`, 2026-07-17 to 2026-08-14 and 2026-06-18 to 2026-07-16, dimension `page`, regex-scoped, 2,362 and 2,120 rows, neither capped.
- Live sitemap: 14,402 products, 85 files, fetched 2026-08-16.
- Live page verification: 22 pages fetched, H1 + SKU + per-variant availability parsed from JSON-LD.
- DFS Google Ads US volumes re-pulled 2026-08-16 for every head term in the table.
- Scripts: `load_gsc.py`, `rank.py`, `final_rank.py`, `select.py`, `verify_live.py`, `stock.py`, `stock2.py`, `stock3.py`, `cannib.py` in the session scratchpad.

**Nothing here has been dispatched. No brief has been written. Awaiting approval.**
