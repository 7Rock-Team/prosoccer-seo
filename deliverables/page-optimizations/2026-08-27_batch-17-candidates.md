# Batch 17 candidate proposal, drawn from the detection gap

**Date:** 2026-08-27  |  **Source:** `detection-gap-2026-08-27.csv`  |  **Status: AWAITING MIKE APPROVAL**

Replaces the ten SKUs previously queued. Nothing is dispatched until Mike approves this list.

## How the pool was cut

| step | pages left |
|---|---|
| untracked products over 1,000 impressions | 1,280 |
| criterion 1: 10k to 100k band, giants excluded | 156 |
| criterion 2: in stock | 46 |
| criterion 4: term not already held by an optimized page | 36 |
| criterion 3: selected for type spread | **10** |

**Only 29% of the band is in stock (46 of 156).** That is the sold-out pattern continuing well
below the giants, and it is why criterion 2 removes more pages than any other step.

Stock is from the storefront's own `products.json`, counted programmatically, cross-checked
against the 28 pages verified independently through Firecrawl. Term collisions are checked
against 429 primary, target and ceded terms drawn from `products-master.csv` and
`ceded-terms.csv`, using exact match plus two-token containment in both directions.

## The ten

| # | Handle | Type | Impr | Top query | Pos | Stock | Season | Price |
|---|---|---|---|---|---|---|---|---|
| 1 | `adidas-2026-colombia-mens-stadium-home-soccer-jersey` | National team | 22,329 | `colombia jersey 2026` | 9.14 | 4/6 | 2026 | $65.00 |
| 2 | `umbro-2025-2026-guatemala-mens-home-soccer-jersey` | National team | 26,482 | `guatemala soccer jersey` | 5.93 | 2/6 | 2025 | $62.00 |
| 3 | `puma-2026-paraguay-mens-authentic-home-soccer-jersey` | National team | 18,010 | `paraguay jersey` | 5.99 | 5/5 | 2026 | $98.00 |
| 4 | `adidas-2026-italy-mens-authentic-home-soccer-jersey` | National team | 11,312 | `italy world cup jersey` | 10.52 | 5/6 | 2026 | $98.00 |
| 5 | `adidas-2026-spain-mens-stadium-away-soccer-jersey` | National team | 23,122 | `spain jersey 2026` | 6.36 | 3/8 | 2026 | $99.99 |
| 6 | `nike-phantom-6-low-elite-firm-ground-soccer-cleats-erling-haaland-pack-fa25` | Footwear | 21,639 | `haaland cleats` | 6.10 | 2/15 | n/a | $162.00 |
| 7 | `adidas-2026-27-club-america-mens-authentic-home-soccer-jersey` | Club jersey | 10,657 | `america jersey 2026` | 5.48 | 6/6 | 2026 | $159.99 |
| 8 | `nike-2026-27-usmnt-mens-stadium-home-shorts` | National team, non-jersey | 10,589 | `usmnt shorts` | 12.28 | 4/4 | 2026 | $53.00 |
| 9 | `panini-2026-fifa-world-cup-stickers-box-50-packs-each` | Other | 29,765 | `panini sticker box` | 9.79 | 1/1 | 2026 | $129.99 |
| 10 | `nike-strike-sleeves-socks` | Other | 14,025 | `soccer sleeve socks` | 8.44 | 6/10 | n/a | $13.99 |

**Combined: 187,930 impressions.** Type spread: 5 national team jerseys, 1 footwear, 1 club jersey,
1 national-team non-jersey, 2 other.

## Why each was chosen

**1. `adidas-2026-colombia-mens-stadium-home-soccer-jersey`**  
Highest-impression in-stock national team page in the band with usable depth. Colombia 2026 is a live World Cup nation and the term is unclaimed.

**2. `umbro-2025-2026-guatemala-mens-home-soccer-jersey`**  
Guatemala is already flagged in B-COLL-05: the collection earns 48,496 impressions and 1,163 clicks at position 5.82, the strongest converting untracked collection we have. Optimizing the PDP under a collection that already performs is the cheapest test of whether PDP work compounds.

**3. `puma-2026-paraguay-mens-authentic-home-soccer-jersey`**  
Every size in stock, 5 of 5, at position 5.99 on the head term paraguay jersey. The cleanest case in the pool: full availability, strong position, nothing claimed.

**4. `adidas-2026-italy-mens-authentic-home-soccer-jersey`**  
Strong depth at 5 of 6 and the weakest position of the five jersey picks at 10.52, which makes it the clearest before-and-after read in the batch. Italy is also the one pick whose top query, italy world cup jersey, carries explicit tournament intent.

**5. `adidas-2026-spain-mens-stadium-away-soccer-jersey`**  
Second-highest in-stock impressions in the band. Spain has four sold-out siblings in the top 25, so this is the one Spain page that can actually take traffic.

**6. `nike-phantom-6-low-elite-firm-ground-soccer-cleats-erling-haaland-pack-fa25`**  
The ONLY in-stock unclaimed footwear page in the entire band. Footwear is 228 pages and 9.0% of the gap, so it earns a slot, and this is the only one available to fill it. Stock is thin at 2 of 15, flagged below.

**7. `adidas-2026-27-club-america-mens-authentic-home-soccer-jersey`**  
The only in-stock unclaimed club jersey in the band, and every size is available, 6 of 6, at position 5.48. Club America was examined in B-EQUITY-01 and found NOT stranded, so this is a clean club test with no equity complication.

**8. `nike-2026-27-usmnt-mens-stadium-home-shorts`**  
Deliberate probe of the merch finding. National-team non-jersey merch converts at 1.559%, three to seven times any jersey bucket, and it is the only bucket behaving like a healthy page. Full stock at 4 of 4. Weakest position in the set at 12.28, which is the point: if copy moves a healthy-CTR page from 12 to single digits, that is the strongest available evidence for the merch hypothesis.

**9. `panini-2026-fifa-world-cup-stickers-box-50-packs-each`**  
Highest-impression in-stock page in the whole band at 29,765. Collectibles are outside every silo the workforce has written for, so it tests whether the playbook generalizes past apparel and footwear.

**10. `nike-strike-sleeves-socks`**  
Equipment and accessories, 6 of 10 in stock, an evergreen product with no season. Gives the batch one page whose value does not decay with a tournament cycle.

## Flags Mike should see before approving

**Stock depth varies and thin stock is a real risk.** Three picks have most sizes gone: the
Haaland Phantom at 2 of 15, Guatemala at 2 of 6, and Spain at 3 of 8. Copy cannot sell a size
that is not there, and a page at 2 of 15 is closer to sold out than to in stock. They are in
because each is the best or only available page for its slot, not because the depth is good.
If you would rather hold the thin ones, the batch drops to seven and I would backfill from the
remaining 26 in the pool.

**Paraguay has three in-stock pages in the pool and only one was taken.** Authentic home,
stadium away and stadium home all qualify. Taking more than one would put three of our own
pages on adjacent Paraguay terms, which is the cannibalization the pre-dispatch check exists
to prevent. Flagged so the omission reads as deliberate.

**One page in the pool has a top query that does not match its product and it was excluded.**
`adidas-2026-south-africa-mens-stadium-away-soccer-jersey` earns 12,462 impressions with a top
query of `saudi arabia soccer jersey`. A South Africa page ranking on a Saudi Arabia term is
either a mismatch in the page or a gap where no Saudi page exists. Worth a look on its own,
not worth putting in a batch.

**A Germany page was dropped from this list at the last check, and what it turned up is bigger
than the pick.** The candidate was `adidas-2026-germany-mens-stadium-away-long-sleeve-soccer-
jersey-1`, 15,750 impressions at 6 of 7 stock. The trailing `-1` is Shopify's collision suffix,
so a base handle without it also exists and is live. They are DIFFERENT products: the base is
the **Stadium** long-sleeve, and the `-1` page, whose handle says `stadium`, is titled
**Authentic**. That is the live-title-governs rule firing exactly as written: the handle is not
a source of product attributes. Dropped and replaced with Italy rather than sending a brief
whose handle and tier disagree.

**The wider surface, logged as B-DUP-04: 439 live products carry a collision-suffix handle whose
base handle is ALSO live. 41 of those are in the detection gap, holding 135,255 impressions.**
Most look like true duplicates with identical titles on both pages (`nike-fa25-total-90-academy-
soccer-ball`, `nike-grip-strike-crew-socks`, `adidas-copa-mundial-firm-ground-soccer-cleats`).
At least one is worse than duplication: `adidas-2026-argentina-womens-originals-dress-1` is
titled **adidas 2026 Mexico Women's Originals Dress**. Not touched, not acted on, and no batch
selection should draw from a suffixed handle until it is understood.

**Criterion 4 is only as good as the registry.** It filters against terms the registry records.
The whole point of B-DETECT-01 is that the registry does not know about most ranking pages, so
this check cannot see a collision with an unoptimized page that already ranks. The
pre-dispatch cannibalization pass still has to run.
