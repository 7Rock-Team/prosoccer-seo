# DataFeedWatch: a ten-minute check

**Date:** 2026-08-28 | **For:** Mike | **Item:** B-TECH-03 | **Author:** ORIN

7 Rock manages the DataFeedWatch account, so this is not blocked on access. Work top to bottom
and stop at the first thing that looks wrong; each step is written so a problem is recognisable
without knowing the tool.

**SUPERSEDED 2026-08-28. Mike ran this and the feed is healthy: 44.4K approved, 15 limited, 4 not
approved, Top Quality Store, all channels OK. There is no eligibility problem, so steps 1 to 3
below are answered. The follow-on analysis is at `2026-08-28_merchant-listings-diagnostic.md`.**

**One correction to the table below: the percentages were computed against 8.25M, which is the sum
of search-appearance rows, not the site total. The true site total is 19,842,113, so merchant
listings are 3.4% of impressions rather than 8.2%. The CTR and position figures are unaffected.**

**Why this is worth ten minutes, in one number.** Across the whole property over 90 days:

| Search surface | Impressions | Clicks | CTR | Avg position |
|---|---|---|---|---|
| Product snippets (ordinary organic) | 7,556,381 | 65,596 | 0.868% | 12.07 |
| **Merchant listings (free product listings)** | **678,578** | **23,947** | **3.529%** | **3.49** |
| Review snippet | 2,181 | 28 | 1.284% | 21.43 |
| Translated result | 10,729 | 15 | 0.140% | 9.93 |

**Merchant listings convert at four times ordinary organic and rank nine positions higher, and
they carry only 8.2% of our impressions.** That surface is working when we are in it. The
question this check answers is whether we are in it for as much of the catalogue as we should be.

---

## 1. Is the feed delivering at all (2 minutes)

Open DataFeedWatch and look at the **shop dashboard** for prosoccer.com, then the channel entry
for **Google Shopping**.

Read three things:

- **Last update / last fetch timestamp.** Should be within the last 24 hours. Anything older than
  a few days means the feed has stopped refreshing and the catalogue Google sees is stale.
- **Feed status.** Should read as active or enabled. A paused or errored channel is the single
  fastest explanation for missing coverage.
- **Product count in the output feed.** Compare it to **16,322**, the number of published products
  on the storefront today. This is the most informative number on the page.

**What a problem looks like:** an output count far below 16,322. A gap of a few hundred is normal
(out-of-stock exclusions, deliberate filters). A gap of thousands means rules are excluding
products, and those products cannot appear in merchant listings no matter what we write on them.

## 2. Errors and warnings in the feed itself (3 minutes)

Still in DataFeedWatch, open the channel's **review / errors** view before going to Google. DFW
validates against Google's spec and flags problems before they are ever submitted.

Look for counts against these fields specifically, because they are the ones that gate eligibility
rather than merely warn:

- `id`, `title`, `link`, `image_link`, `price`, `availability` (missing any of these excludes an item)
- `brand`, `gtin`, `mpn` (missing identifiers commonly downgrade an item to limited visibility
  rather than excluding it, which is exactly the silent failure this item is chasing)
- `google_product_category` and `product_type`

**What a problem looks like:** a nonzero error count on any of the first group, or a large warning
count on identifiers. Note the numbers; they are the input to the next step.

## 3. Approved versus disapproved on the Google side (4 minutes)

DataFeedWatch surfaces Google's response, so start there rather than logging into Merchant Center.
Look for the channel's **Google Merchant Center status** or **results** panel.

Read, in this order:

- **Approved / active item count.** Compare to both 16,322 and to the output count from step 1.
  Three numbers that should be close: products on the site, products sent, products approved. Any
  large step down between them localises the problem to a specific stage.
- **Disapproved count and the top disapproval reasons.** Common ones worth recognising: image
  issues, price or availability mismatch between feed and landing page, missing identifiers,
  policy violations.
- **Pending / under review count.** A large pending number is normal right after a big feed change
  and abnormal otherwise.

**What a problem looks like:** approved materially below sent. If sent is 16,000 and approved is
9,000, roughly 7,000 products are ineligible for the surface that converts at 3.529%, and that is
almost certainly worth more than any copy work queued behind it.

**Price and availability mismatch is the one to look for hardest**, because two thirds of the
catalogue is currently out of stock and a feed that lags inventory produces exactly this
disapproval at scale.

## 4. Are free listings actually switched on (1 minute)

This is a separate opt-in from paid Shopping ads and a store can run one without the other. It
lives in Merchant Center rather than DataFeedWatch, under the programme or growth settings, as
**free listings** (sometimes shown as free product listings or surfaces across Google).

Confirm it is **enabled** for the United States.

**What a problem looks like:** free listings off, or enabled but with its own separate disapproval
count distinct from the Shopping ads one. The two programmes report eligibility separately, and a
product can be fine for ads and excluded from free listings.

---

## What to report back

Five numbers is enough, and they do not need interpreting:

1. Products in the output feed (versus 16,322 on the site)
2. Feed errors, and against which fields
3. Approved / disapproved / pending on the Google side
4. Top two disapproval reasons
5. Free listings enabled, yes or no

That is enough to say whether the merchant-listing gap is a feed problem, an approval problem, or
neither, and it decides whether B-TECH-03 goes to VERITAS or stops here.

**Nothing here blocks Batch 17.**
