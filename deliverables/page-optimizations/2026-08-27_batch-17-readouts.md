# Batch 17 expected read-outs, written BEFORE authoring

**Date:** 2026-08-27 | **Author:** ORIN | **Status: read-outs locked. Authoring begins after this.**

## What this batch is

**Batch 17 is a test, not an optimization batch (Mike, 2026-08-27).**

**Hypothesis: does copy move a page whose impressions come substantially from non-snippet**
**surfaces? Stated expectation: no, or barely.** The value of the batch is finding out cheaply
rather than assuming either way in either direction.

The diagnostic behind it: a page earning 6,450 impressions at position 4.88 while absent from
the live organic top 20 is not being served as an organic listing. Carousel tiles render an
image, a name, a price and a seller. **The two fields SCRIBE writes are not displayed there.**
That is not a copy quality problem and copy cannot fix it.

## Two things this batch preserves regardless of the ranking question

**1. The copy on these pages is genuinely broken and worth fixing on its own terms.** Raw
product-name titles, metas that are either the product name repeated at 54 characters or an
unedited body-copy dump at 324 to 327, one of which opens with an escaped HTML entity. That is
what a person sees when the page IS served as an organic result, which happens on some share of
impressions for every page here. Fixing it does not depend on the hypothesis resolving either way.

**2. The collection is the only page in this comparison written by a person, and it is the one**
**that converts.** `/collections/guatemala` carries an authored title and a 155-character meta
with a benefit and a shipping line, and takes 2.398% CTR. Every PDP beside it carries machine
output and takes 0.018% to 0.457%. **This is not proof.** The collection differs in page type,
rich-result coverage (91.66% against 0.1%) and intent match, any of which could carry the effect.
**It is the only clean contrast available and it is noted as such, not as evidence.**

## The control problem, and the control we do have

Mike named the confound: World Cup year, seasonal demand, no control. The first two are real and
unavoidable. **The third is partly solvable and the batch should exploit it.**

**Sibling control.** Five of the nine sit on terms where we own other pages that are NOT being
touched: Spain has three untouched siblings on `spain jersey 2026`, Paraguay two, USMNT one at a
better position than ours, Guatemala four, Club America five. **Those siblings experience the
same seasonal demand and the same SERP, and receive no copy change.** Any movement in an
optimized page must be netted against its untouched siblings on the same term before it counts.
That is not a randomised control, but it removes the tournament and the category from the
comparison, which is most of the confound.

**Evergreen control.** `nike-strike-sleeves-socks` has no season and no World Cup exposure. If
every tournament page moves and this one does not, the movement was the tournament.

**Measurement:** GSC, canonical rows only, 30 and 60 days post-import, term-level where a term
is named and page-level where none is. Compare SHARE of the term, not absolute impressions.

## Baseline, frozen today

| # | Page | Type | Earned term | Term pos | Page impr | CTR | Enhanced | Stock |
|---|---|---|---|---|---|---|---|---|
| 1 | `umbro-2025-2026-guatemala-mens-home-soccer-jer` | National team | `guatemala soccer jersey` | 4.88 | 26,493 | 0.075% | 0.1% | 2/6 |
| 2 | `adidas-2026-spain-mens-stadium-away-soccer-jer` | National team | `spain jersey 2026` | 5.50 | 23,146 | 0.428% | 9.6% | 3/8 |
| 3 | `puma-2026-paraguay-mens-authentic-home-soccer-` | National team | `paraguay jersey` | 4.89 | 18,018 | 0.205% | 13.8% | 5/5 |
| 4 | `adidas-2026-italy-mens-authentic-home-soccer-j` | National team | none | n/a | 11,336 | 0.088% | 72.9% | 5/6 |
| 5 | `nike-phantom-6-low-elite-firm-ground-soccer-cl` | Footwear | `haaland cleats` | 6.08 | 21,834 | 0.128% | 4.1% | 2/15 |
| 6 | `adidas-2026-27-club-america-mens-authentic-hom` | Club jersey | `america jersey 2026` | 3.50 | 10,926 | 0.018% | 1.9% | 6/6 |
| 7 | `nike-2026-27-usmnt-mens-stadium-home-shorts` | National team merch | `usmnt shorts` | 10.57 | 10,602 | 0.245% | 88.3% | 4/4 |
| 8 | `panini-2026-fifa-world-cup-stickers-box-50-pac` | Other | none | n/a | 29,773 | 0.309% | 36.0% | 1/1 |
| 9 | `nike-strike-sleeves-socks` | Other | none | n/a | 14,211 | 0.457% | 27.6% | 6/10 |

Three of the nine (Italy, Panini, socks) have NO earned term under the 15% / 1,000-impression
concentration condition and take conventional keyword assignment. Two (Paraguay 4.89, Club
America 3.50) sit in the protected band and carry the WARNING line, with Title and H1 changes
gated on Mike per page.

## Per-page read-outs

### 1. `umbro-2025-2026-guatemala-mens-home-soccer-jersey`

**Primary:** Ceding `guatemala soccer jersey` to the collection, which earns it. Takes a qualified primary.

**Why it is in the batch:** **The cleanest instance of the hypothesis in the batch.** 0.1% enhanced share, zero clicks on the term, absent from the live organic top 20. If copy moves anything here it moves it with almost no snippet surface to move it through.

- **Success:** page impressions or clicks rise while `/collections/guatemala` HOLDS its 8,131 impressions and 180 clicks. Both rise, or the PDP rises and the collection is unharmed.
- **Failure:** the collection's clicks fall as the PDP's rise. That is substitution under a strong collection, and it would be an argument against optimizing PDPs beneath collections that already own their head term.
- **Null (expected):** PDP unchanged, collection unchanged. Reads as support for the hypothesis that copy cannot reach a page served mainly outside organic snippets.
- **Confound:** Guatemala's collection is already at 5.62 with healthy CTR, so headroom is limited and a null is weak evidence in both directions.

### 2. `adidas-2026-spain-mens-stadium-away-soccer-jersey`

**Primary:** `spain jersey 2026`, held at 26.6% share and term position 5.50. The brief states the four-way sibling split explicitly.

**Why it is in the batch:** 9.6% enhanced share. Absent from the live organic top 12 entirely, where adidas.com and DICK'S hold the top two with star ratings.

- **Success:** this page's share of the 22,455-impression term rises AND the three siblings do not fall by the same amount. A rise matched by sibling losses is redistribution, not gain.
- **Failure:** this page rises and siblings fall in step, confirming we are moving traffic between our own pages rather than winning any.
- **Null (likely):** no movement against competitors who carry ratings we do not.
- **Confound:** the strongest in the batch. Spain is a World Cup finalist storyline in a World Cup year, so seasonal demand alone will move the raw numbers. Judge SHARE of the term, never absolute impressions.

### 3. `puma-2026-paraguay-mens-authentic-home-soccer-jersey`

**Primary:** `paraguay jersey`, held. Term position 4.89, so it sits in the PROTECTED band: Title and H1 need Mike per page and the brief carries the WARNING line.

**Why it is in the batch:** 13.8% enhanced share, full stock at 5 of 5, and the PDP genuinely owns the term at 45.3% against a collection at 13.1%.

- **Success:** CTR rises from 0.205% with term position holding at or better than 4.89. This is the page where a snippet rewrite has the best chance, because we hold the term and are not fighting a stronger collection.
- **Failure:** term position degrades after the Title or H1 change. That is the equity risk the protected band exists to prevent, and it would be the strongest argument for keeping the under-5 gate.
- **Null:** CTR flat. Given full stock and clear term ownership, a null here is the most damaging single result for the copy hypothesis, because this is the most favourable page in the batch.
- **Confound:** Paraguay qualified for the 2026 World Cup, so interest is rising independently. Use term share and position, not impressions.

### 4. `adidas-2026-italy-mens-authentic-home-soccer-jersey`

**Primary:** NO earned term. `italy world cup jersey` holds 4.5% of the page and 512 impressions, failing both concentration thresholds. Conventional keyword assignment applies.

**Why it is in the batch:** **72.9% enhanced share against 0.088% CTR**, which is the sharpest counter-example in the batch to a simple rich-results-explain-it story.

- **Success:** CTR rises materially from 0.088%. On a page that is already enhanced on three quarters of its impressions, that would isolate copy as the active ingredient better than any other page here.
- **Failure:** CTR falls or position degrades.
- **Null:** unchanged. Combined with the high enhanced share, a null says the deficit is neither snippet presence nor snippet wording, which points hard at price, ratings and feed.
- **Confound:** Italy famously failed to qualify for 2026, so demand may DECLINE over the window independently of anything we do. This is the one page where a decline is not evidence against us.

### 5. `nike-phantom-6-low-elite-firm-ground-soccer-cleats-erling-haaland-pack-fa25`

**Primary:** `haaland cleats`, held at 54.6% share, term position 6.08.

**Why it is in the batch:** 4.1% enhanced share. The only in-stock unclaimed footwear page in the band, and stock is thin at 2 of 15.

- **Success:** CTR rises from 0.128% and the `/collections/nike-haaland-pe-pack` collection, which takes 37.0% of the term at 10.73, does not lose clicks.
- **Failure:** no movement, or the collection loses ground.
- **Null:** expected. Thin stock means most size seekers bounce regardless of copy.
- **Confound:** **2 of 15 sizes is the dominant variable and it will probably swamp the copy signal.** This page is in the batch for type coverage, not because it is a clean test. Say so when the result comes in rather than reading a null as evidence about copy.

### 6. `adidas-2026-27-club-america-mens-authentic-home-soccer-jersey`

**Primary:** `america jersey 2026`, held at 73.3% share. Term position **3.50**, the PROTECTED band: WARNING line required, Title and H1 need Mike per page.

**Why it is in the batch:** **The worst CTR in the batch at 0.018%, on 10,926 impressions, with full stock at 6 of 6 and only 1.9% enhanced share.** The page dominates its term and converts almost nothing.

- **Success:** CTR rises from 0.018% with term position holding at or better than 3.50.
- **Failure:** term position degrades. At 3.50 this is the page with the most to lose, which is precisely why the protected band applies and why Title and H1 changes need your sign-off.
- **Null:** expected. Full stock, dominant term ownership, near-zero clicks and almost no rich-result coverage is the clearest single profile of a page whose problem is not its words.
- **Confound:** $159.99 is at the top of the range for a club jersey and no competitor price comparison was run for this term. Price may be the whole story here and the batch will not isolate it.

### 7. `nike-2026-27-usmnt-mens-stadium-home-shorts`

**Primary:** `usmnt shorts`, held at 63.3% share, term position 10.57. The merch probe.

**Why it is in the batch:** 88.3% enhanced share, full stock at 4 of 4, and the worst position in the batch, which is what makes it the best before-and-after read.

- **Success:** position improves from 10.57 AND CTR holds at or above the merch bucket's 1.559%. That says the merch advantage is a property of the query, survives intervention, and the other 223 merch pages are a real opportunity.
- **Failure (the more interesting outcome):** position improves and CTR falls toward the jersey buckets' 0.2 to 0.5%. That says the 1.559% was a property of ranking lower on narrower intent and evaporates on contact. It kills the merch thesis cheaply, which is worth more than confirming it.
- **Null:** neither moves. No evidence, not support.
- **Confound:** the sibling `usmnt-mens-stadium-away-shorts` holds 36.3% of the same term at position 7.28, BETTER than ours. Any gain must be netted against the sibling or we will read a transfer between our own pages as a win.

### 8. `panini-2026-fifa-world-cup-stickers-box-50-packs-each`

**Primary:** NO earned term. `panini sticker box` is 1.1% of the page and 329 impressions. This is the case that justified the concentration threshold.

**Why it is in the batch:** Highest page impressions in the batch at 29,773, 36.0% enhanced, single variant in stock.

- **Success:** total page impressions rise AND the rise is spread across the long tail rather than concentrated in one query. With no earned term, aggregate demand is the only honest target.
- **Failure:** the brief cannot be written without inventing product attributes the scrape does not supply. Collectibles have no tier, cut, surface or age band, so the entire configuration tuple the PDP playbook rests on is absent. **If SCRIBE reaches for fabricated specifics to fill the template, that IS the result**, and it says the playbook does not generalise and collectibles need their own.
- **Null:** brief writes cleanly, numbers flat. Inconclusive on traffic, but establishes the template is usable outside apparel and footwear.
- **Confound:** **the least attributable page in the batch.** Panini demand in a World Cup year rises on its own. The read-out leans on whether the brief could be written well, not on the traffic.

### 9. `nike-strike-sleeves-socks`

**Primary:** NO earned term. `soccer sleeve socks` is 6.1% of the page and 854 impressions. Conventional assignment.

**Why it is in the batch:** 27.6% enhanced, 6 of 10 in stock, and the only page in the batch with no season, so its value does not decay with the tournament cycle.

- **Success:** CTR rises from 0.457%, already the highest in the batch.
- **Failure:** CTR falls.
- **Null:** flat.
- **Confound:** **the cleanest page in the batch and the best control we have.** Evergreen equipment, no World Cup exposure, no seasonal story. If every World Cup page moves and this one does not, the movement was the tournament. If this one moves too, the copy did something.


## Does the merchant-listing surface change what this batch is testing?

**Asked by Mike 2026-08-28, after the variant finding. Answer: the impression baselines survive,
the CTR baselines do not, and one page needs its narrative corrected. The core test holds.**

These nine were selected from an organic-only list and the read-outs above were written against
canonical organic behaviour. Merchant-listing impressions are reported exclusively against
`?variant=` URLs, which the canonical-only ruling strips, so none of it was counted. Measured per
page over the same 90 days:

| Page | Canon impr | Canon clicks | Variant impr | Variant clicks | of which merch listing | Variant share of CLICKS |
|---|---|---|---|---|---|---|
| `umbro-2025-2026-guatemala-mens-home-soccer-j` | 26,492 | 21 | 89 | 35 | 65 | 62% |
| `adidas-2026-spain-mens-stadium-away-soccer-j` | 23,297 | 104 | 2,185 | 43 | 1,164 | 29% |
| `puma-2026-paraguay-mens-authentic-home-socce` | 19,068 | 51 | 490 | 6 | 29 | 11% |
| `adidas-2026-italy-mens-authentic-home-soccer` | 11,312 | 10 | 38 | 0 | 38 | 0% |
| `nike-phantom-6-low-elite-firm-ground-soccer-` | 21,658 | 27 | 584 | 15 | 23 | 36% |
| `adidas-2026-27-club-america-mens-authentic-h` | 10,688 | 2 | 6 | 0 | 8 | 0% |
| `nike-2026-27-usmnt-mens-stadium-home-shorts` | 10,913 | 29 | 0 | 0 | 0 | 0% |
| `panini-2026-fifa-world-cup-stickers-box-50-p` | 30,039 | 98 | 2,479 | 20 | 2,024 | 17% |
| `nike-strike-sleeves-socks` | 14,925 | 74 | 334 | 55 | 345 | 43% |

**Batch totals: variant URLs are 3.6% of impressions but 29.5% of CLICKS.**

| | Impressions | Clicks | CTR |
|---|---|---|---|
| Canonical, what the read-outs measure | 168,392 | 416 | **0.247%** |
| Variant URLs, never counted | 6,205 | 174 | **2.804%** |
| Combined, what the pages actually do | 174,597 | 590 | **0.338%** |

### What this changes

**1. Impression read-outs stand.** Variant URLs are 3.6% of impressions. Any read-out phrased as
"impressions rise" or "share of the term" is measuring 96.4% of the page and is not materially
affected.

**2. Every CTR figure in this document understates by about 1.37x and is hereby restated.** The
batch converts at **0.338%**, not the 0.247% the canonical-only view shows. Per-page CTR targets
in the read-outs above are canonical-only baselines: they remain valid as a like-for-like
before-and-after, but they are NOT the page's true CTR and must not be quoted as such.

**3. One page needs its narrative corrected, and it is Guatemala.** It was described in the
near-zero-click diagnostic as converting nothing. In canonical organic that is true: 21 clicks on
26,492 impressions. **But it takes 35 clicks off variant URLs, of which 26 come from merchant
listings on 65 impressions.** More of its clicks come from the surface we never counted than from
the one we did. It is the only page of the nine where that is so.

**The Guatemala picture is therefore the opposite of what was reported.** The page is not failing
to convert. It converts through free listings and not through organic, which is consistent with
the collection owning the organic term. That strengthens rather than weakens the decision to cede
`guatemala soccer jersey` to the collection and give the PDP a qualified primary.

**4. The decisive test survives intact, which is the important part.** The read-outs name Club
America and Paraguay as the two pages whose null results would settle the copy question. **Club
America has 6 variant impressions and 0 variant clicks; Paraguay has 490 and 6.** Neither has
meaningful hidden traffic, so both remain clean tests and the "one result that would change the
programme" section stands without amendment.

**5. USMNT shorts, the merch probe, has ZERO variant impressions.** The merch hypothesis is
unaffected.

### Measurement rule for the post-import read

**Report both surfaces, always, and never collapse them into one number.** At 30 and 60 days
pull canonical rows and query-string rows separately, and state impressions, clicks and CTR for
each. A page can improve in organic while losing in free listings, or the reverse, and a combined
figure hides both. Guatemala is the proof that the split can invert a conclusion.
## The one result that would change the programme

If Club America and Paraguay both come back null, the case is close to settled. They are the two
most favourable pages in the batch: full stock, dominant ownership of their terms, top-5 term
positions, and nothing competing internally. **If copy cannot move those two, it will not move
the other 1,271 untracked pages either, and the programme should redirect to B-TECH-03.**

If they move, the hypothesis is wrong in a useful way and the copy programme has a measured
mandate it has never had.
