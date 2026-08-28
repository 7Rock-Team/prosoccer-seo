# Merchant listings: why a healthy feed still surfaces little

**Date:** 2026-08-28 | **Item:** B-TECH-03 | **Author:** ORIN

Mike checked Merchant Center: **44.4K products, 44.4K approved, 15 limited, 4 not approved, 0
under review, US store quality Top Quality Store, feeds updated 7 hours ago, all channels OK.**

**My eligibility hypothesis is dead. Google accepts essentially the entire catalogue.** This
answers the reframed question against data rather than guesses, taking Mike's four candidates in
the order that turned out to matter.

---

## 1. GSC's merchant-listings figure does NOT count what we thought. Two separate errors, one mine

**a. My denominator was wrong, and the error is mine.** I reported merchant listings as "8.2% of
impressions". The true site total over the same window is **19,842,113 impressions**, not the
8,247,869 I used. That 8.2M was the SUM OF THE SEARCH-APPEARANCE ROWS, which I treated as if it
were the site total.

| | Impressions | Share of TRUE site total |
|---|---|---|
| **Site total, no dimensions** | **19,842,113** | 100% |
| Sum of all appearance types | 8,247,869 | 41.6% |
| Product snippets | 7,556,381 | 38.1% |
| **Merchant listings** | **678,578** | **3.4%** |
| Review snippet | 2,181 | 0.0% |

**58.4% of our impressions carry no recognised search appearance at all.** Merchant listings are
**3.4% of the real total, not 8.2%.** Every share I quoted from that 8.25M base was inflated by
roughly 2.4x, including in the DataFeedWatch brief. Corrected here and there.

**b. Merchant-listing impressions are reported against VARIANT URLs, exclusively.** Of 12,543
merchant-listing page rows, **12,543 carry `?variant=` and zero are canonical.** Examples:
`.../products/nike-2026-27-canada-mens-stadium-home-soccer-jersey?variant=48284342616319`.

**This matters well beyond this item. The standing canonical-only ruling excludes every URL with a
query string, so 100% of the merchant-listing surface was invisible to the B-DETECT-01 analysis.**
The 1,280 untracked products, the 8.97M impressions, the CTR figures and the near-zero-click
diagnostic are all organic and product-snippet only. They are not wrong, but their scope is
narrower than the framing implied, and nothing in the method said so.

**c. GSC does not agree with itself.** The aggregate `searchAppearance` row says **678,578**
merchant-listing impressions. Summing the same filter broken out by page gives **397,313**, a 41%
shortfall. Both come from the same API over the same window. Treat merchant-listing volumes as
directional, not exact.

## 2. Free listings ARE enabled. That candidate is closed

GSC's `MERCHANT_LISTINGS` appearance reports free product listings specifically. We have 678,578
of them. **A surface cannot report impressions if it is switched off**, so no Merchant Center
settings check is needed for this question.

## 3. Out-of-stock items are eligible but heavily under-represented, not suppressed

| | Share of merchant-listing pages | Catalogue baseline |
|---|---|---|
| In stock | **78.4%** (9,832 pages, 75.1% of impressions) | 33.7% |
| Sold out | 21.5% (2,701 pages, 24.8% of impressions) | 66.3% |

**In-stock products are over-represented by about 2.3x against their share of the catalogue.**
Availability clearly influences the surface. **But sold-out items are NOT excluded**: 2,701 of
them draw 98,426 impressions. So this is a ranking or selection weight, not an eligibility gate,
and it is consistent with the 44.4K approval figure.

## 4. It is competitive selection, not eligibility. This is the answer

**Only 3,292 of 16,322 products (20.2%) received a single merchant-listing impression in 90 days.
Restricting to the in-stock catalogue, which is where the surface concentrates, 2,493 of 5,504
(45.3%) ever appeared.**

With approval at essentially 100%, four in five products are eligible and never surface, and more
than half of in-stock products never surface. **Nothing is blocking them. They are losing.** Free
listings rank on relevance, price competitiveness, offer quality and seller signals, and on the
SERPs already examined our tiles sit alongside sellers at $15.99 to $30.73 against our $62 to
$159.99, and alongside competitors carrying 1,600-vote ratings against our ~1.7% review coverage.

**That is the reframe: the merchant-listing gap is a competitiveness problem on a surface we are
fully admitted to, not an admission problem.** It is also the surface that converts at 3.529% at
position 3.49, four times ordinary organic, so the upside is real even though the lever is harder
than a feed fix.

---

## The 44.4K number does not reconcile, and it is worth one question

| Count | Value |
|---|---|
| Published products on the storefront | 16,322 |
| **Merchant Center items** | **44,400** |
| Total variants across the catalogue | 87,891 |
| DataFeedWatch V2 feed | 14,903 |
| DataFeedWatch Test feed | 16,706 |
| V2 + Test | 31,609 |

**44.4K matches neither the product count nor the variant count.** If Merchant Center were
counting variants it would be near 87,891; if products, near 16,322. It sits between, and
V2 + Test + a Canada feed would plausibly reach it.

Two things in the DataFeedWatch numbers are worth noticing on their own:

- **The Test feed carries 16,706 items, which is 384 MORE than the store has published products.**
  A test feed containing more items than exist published is worth explaining.
- **V2 carries 14,903, which is 1,419 FEWER.** Something in V2's rules excludes roughly 1,419
  products, and since V2 looks like the production feed, those are products that cannot appear.

**The 1,803 gap between the two feeds is the concrete question: which rule differs.** Given
approval is ~100%, neither feed is being rejected, so this is not urgent, but a live Test feed
submitting alongside production would mean duplicate offers competing with each other, which is a
plausible contributor to a competitiveness problem.

---

## Not for ORIN to solve, logged from the same screen

- **Google Shopping clicks down 42.2% over 28 days.** Post-tournament seasonality is the obvious
  candidate and it is worth ruling IN rather than assuming. The cheap test: compare the same 28
  days against the equivalent window in the prior non-tournament year, and check whether organic
  impressions fell by a similar proportion. If organic held and Shopping fell, seasonality is not
  the whole story.
- **Canada store quality reads "Missing signals" while US reads Top Quality Store.** Noted, not
  investigated. Canada products appeared prominently in the merchant-listing sample, so the two
  may be related.

## What changes

Nothing blocks Batch 17. Inside B-TECH-03 the priority order is now:

1. **Competitiveness on a surface we are already admitted to**, since 45.3% coverage of in-stock
   products with 100% approval is the finding.
2. **The V2 versus Test feed gap**, because it is cheap to answer and a live test feed would
   matter.
3. **Reviews**, which remain a slow programme against a 0.026% surface.

And one correction that belongs to B-DETECT-01 rather than here: **the canonical-only ruling
silently excluded an entire search surface.** That should be recorded on the ruling itself.
