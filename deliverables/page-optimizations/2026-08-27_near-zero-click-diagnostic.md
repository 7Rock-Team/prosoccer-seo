# Why these pages earn impressions and no clicks

**Date:** 2026-08-27 | **Author:** ORIN | **Status: DIAGNOSTIC. Requested before authoring Batch 17.**

Mike's question: if a page at position 4.88 earns zero clicks, copy is not the binding constraint,
and we should know what is before spending nine briefs on the assumption that it is.

**Short answer: copy is not the binding constraint, and for the worst cases we are not in the
organic result set at all. But copy is not irrelevant either, and the two facts need separating.**

Sources: live DataForSEO SERP scrapes (2026-08-27, desktop, United States), GSC search-appearance
and term-level data over 90 days to 2026-08-27, and direct fetches of our own rendered pages.

---

## 1. The single sharpest comparison available

`guatemala soccer jersey`, same query, same SERP, two of our own pages:

| Our page | Impressions | Clicks | CTR | In organic top 20? |
|---|---|---|---|---|
| `/collections/guatemala` | 8,131 | 180 | **2.21%** | **Yes, rank 3** |
| `/products/umbro-2025-2026-guatemala-mens-home` | 6,450 | **0** | 0% | **No. Absent.** |

The live SERP scrape returns **one** prosoccer.com organic result and it is the collection. The
PDP does not appear anywhere in the top 20 organic. GSC nevertheless reports 6,450 impressions at
average position 4.88 for that page on that term.

**Both facts are true, which means those impressions are not organic-listing impressions.** They
come from somewhere else on the page. The SERP shows what that somewhere is: three separate
`Popular products` carousels occupying rank slots 1, 10 and 11, carrying 30 shopping tiles, and
several of those tiles are ours, listed under the seller name "Pro Soccer."

**This is the mechanism.** A product tile inside a horizontally scrolling carousel is an
impression. Its reported position is the position of the module, not a rank a reader scans down
to. A page can therefore show "position 4.88" while never appearing as a blue link anyone reads.
No title tag and no meta description is being read in that surface, because neither is displayed.
The tile shows an image, a short product name, a price, a seller and sometimes a rating.

---

## 2. It generalises. Spain is worse

`spain jersey 2026`, live SERP, top 12:

**prosoccer.com does not appear at all.** Not in organic, not in the Popular products carousel.

Who does hold the organic results, with what:

| Rank | Domain | Rating shown | Price shown |
|---|---|---|---|
| 1 | adidas.com | **4.9 (243 votes)** | $150.00 |
| 2 | dickssportinggoods.com | **4.9 (570 votes)** | $100.00 |
| 4 | us.shop.realmadrid.com | none | $40 to $190 |
| 5 | soccer.com | none | $60 to $140 |
| 6 | fanatics.com | none | $70 to $185 |

**Every organic result above us carries a price rich result, and the top two carry star ratings.**
Our Spain Stadium Away is $99.99, which is not the problem: DICK'S sits at $100.00 with a 4.9 from
570 reviews and outranks the brand's own site's price point.

The Popular products carousel on that query is dominated by counterfeit-tier sellers at $15.99,
$16.43, $25.99, $29.99 and $30.73, alongside TUDN Fan Shop at $99.99 with 4.8 from 194 votes and
MyFitteds at $100.00 with 4.8 from **1,600** votes.

---

## 3. What we can attribute, and what we cannot

### Rich results: we are largely absent, and it correlates but does not explain everything

GSC search-appearance, share of each page's impressions carrying a recognised enhancement:

| Page | Enhanced share | CTR |
|---|---|---|
| `/collections/guatemala` | **91.66%** | **2.398%** |
| PDP usmnt shorts | 88.24% | 0.246% |
| PDP spain stadium away | 9.57% | 0.428% |
| PDP colombia authentic away | 7.47% | 0.091% |
| PDP club america authentic home | 2.00% | 0.019% |
| PDP guatemala home | 0.05% | 0.076% |
| PDP paraguay authentic home | **0.00%** | 0.205% |

The collection earns product snippets on 92% of its impressions and converts 10 to 100 times
better than any PDP here. **But USMNT shorts carries enhancements on 88% of impressions and still
converts at 0.246%, so rich results are not sufficient on their own.** Stating that plainly
because the tempting read of this table is a single-cause story, and the table does not support
one.

### Ratings: we have none, and our competitors do

Checked directly on all five pages fetched. Every one carries Product schema with availability
nodes, and **not one carries `aggregateRating`.** The organic winners on `spain jersey 2026` show
4.9 from 243 and 4.9 from 570. The strongest carousel tiles show 4.8 from 1,600.

This is a structural disadvantage no copy change can close. It is a VERITAS and merchandising
question, not a SCRIBE one.

### Titles and metas: genuinely unoptimized, and worth fixing regardless

Rendered, as Google receives them:

| Page | Title | Meta description |
|---|---|---|
| PDP guatemala | `Umbro 2025-2026 Guatemala Men's Home Soccer Jersey - ProSoccer` (72) | **54 chars, the product name repeated. Nothing else.** |
| PDP spain | `adidas 2026 Spain Men's Stadium Away Soccer Jersey - ProSoccer` (72) | **324 chars of raw body copy spilling in** |
| PDP paraguay | `Puma 2026 Paraguay Men's Authentic Home Soccer Jersey - ProSoccer` (75) | **327 chars, opens `FEATURES &amp; BENEFITS MOISTURE MANAGEMENT:`** |
| PDP club america | `adidas 2026-27 Club America Men's Authentic Home Soccer Jersey - ProSoccer` (84) | 324 chars of raw body copy |
| COLL guatemala | `Guatemala Soccer Jerseys and Fan Gear - ProSoccer` (55) | **155 chars, benefit plus shipping. Optimized.** |

Every PDP title is the raw product name plus the theme suffix. Every PDP meta is either the
product name repeated or an unedited dump of body copy running double the 160-character limit,
one of which leads with an escaped HTML entity. The collection, which is the page that converts,
is the only one written by a person.

**So there IS real copy work here.** What the evidence does not support is that copy is the
binding constraint on the zero-click cases, because on those queries the snippet is frequently
not the surface we appear in.

### What cannot be determined from available data, stated rather than guessed

1. **Which surface each individual impression came from.** GSC's `searchAppearance` dimension
   only reports impressions carrying a recognised enhancement. Guatemala PDP returns 14 such
   impressions against 26,482 total, so **over 99.9% of that page's impressions are not
   attributable to a named surface** from this data. The carousel explanation is strongly
   supported by the SERP scrape but is an inference, not a measurement.
2. **Whether reported position is an organic rank or a module position.** GSC does not expose
   this, and the two are not comparable. This matters for the safe band, since a band keyed on
   position is keyed on a number that means different things for different impressions.
3. **Whether we are in Google's Merchant Center free listings for these SKUs, and with what feed
   quality.** That is Mike's or Jorge's surface, not visible from here, and it is the most likely
   single explanation for why our tiles appear on some queries and not others.
4. **Competitor pricing at the SKU level over time.** One SERP snapshot is a point in time and
   these are promotional categories.

---

## 4. What this means for Batch 17

**It does not invalidate the batch, and it does change what the batch is for.**

Three of the nine sit in the near-zero-click population: Guatemala (0 clicks on 6,450 for its
term), Spain (99 clicks on 23,122 page-wide, absent from the SERP entirely), Club America (2
clicks on 10,657, 0.019%). Writing better copy for those pages is defensible on its own terms,
the metas are genuinely broken, but **it should not be sold as a traffic intervention**, because
the surface that produces most of their impressions does not display the copy.

Six of the nine are not in that population and the normal case for copy holds.

**The honest framing: Batch 17 becomes a test of whether copy alone moves a page whose impressions
come substantially from non-snippet surfaces.** That is worth knowing, and it is cheap to learn
now that the read-outs are written down. But if the answer is no, the lever is feed quality,
ratings and price, and those are not SCRIBE's to pull.

**Recommendation, for Mike's call:**

1. **Proceed with the six clean pages.** No change to the plan.
2. **For Guatemala, Spain and Club America, proceed but re-scope the expected read-out** so we are
   measuring "did fixing a broken meta move anything on a page we may not be organically visible
   for," not "did copy lift traffic."
3. **Open a separate item for the structural half:** aggregateRating absent site-wide, Merchant
   Center feed status unknown, and product-snippet coverage varying from 0% to 92% across pages
   with identical schema. That is the larger lever and it is not a copy project.

---

## 5. Revised read-out for the three probes, given this

The three probe read-outs written earlier stand, with one addition applied to all of them:
**before crediting or blaming copy, check the page's enhanced-impression share and whether it
appears in a live organic scrape for its earned term.** A page that was never organically visible
cannot have its snippet judged, and a movement in traffic on such a page is more likely a feed or
inventory event than a copy event.
