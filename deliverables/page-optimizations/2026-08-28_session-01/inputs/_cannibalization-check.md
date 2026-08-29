# Batch 17 pre-dispatch cannibalization check

**Run 2026-08-28, before any primary was finalised.** Registry 1 is
`inputs/_registry1_primaries.txt`: **177 claimed primaries**, every non-blank
`normalized_primary` in `deliverables/tracking/products-master.csv` (178 data rows; the one blank
is the `intentionally-unoptimized` New Balance Furon colorway pair, which claims nothing).
`deliverables/tracking/ceded-terms.csv` is header-only, so there is nothing to check against there.

Criterion 4 of the selection already filtered all nine against 429 registry and ceded terms. That
pass only knows terms the registry records, which is the whole point of B-DETECT-01, so this is the
manual pass over the terms actually being assigned.

## Method

Exact match plus two-token containment in both directions against all 177, plus a hierarchy read
against `collections-master.csv` and the live collection pages, plus a live check of the sibling
PDPs in each lane.

## Result: no blocking collision. Two findings worth recording.

| # | SKU | Primary assigned | Exact hit | 2-token containment | Verdict |
|---|---|---|---|---|---|
| 1 | Guatemala | `guatemala home jersey` | none | see finding A | CLEAR |
| 2 | Spain | `spain jersey 2026` | none | none | CLEAR |
| 3 | Paraguay | `paraguay jersey` | none | none | CLEAR |
| 4 | Italy | `italy authentic jersey` | none | none | CLEAR |
| 5 | Haaland | `haaland cleats` | none | see finding B | CLEAR |
| 6 | Club America | `america jersey 2026` | none | none | CLEAR |
| 7 | USMNT shorts | `usmnt shorts` | none | none | CLEAR |
| 8 | Panini | `panini sticker box` | none | none | CLEAR |
| 9 | Socks | `nike strike sleeves` | none | none | CLEAR |

No token containing `guatemala`, `spain`, `paraguay`, `italy`, `america`, `usmnt`, `panini`,
`sticker` or `sock` appears anywhere in Registry 1. The Guatemala, Spain, Italy, Club America,
USMNT, Panini and socks lanes are entirely unclaimed.

---

### Finding A. Guatemala's assigned primary shares two tokens with the term it is CEDING

`guatemala home jersey` and the ceded `guatemala soccer jersey` share {guatemala, jersey}. Under a
mechanical two-token rule that reads as a collision. It is not one, and the distinction matters:

`guatemala soccer jersey` is being ceded **to `/collections/guatemala`**, which earns 8,131
impressions and all 180 clicks on it against the PDP's 6,450 and zero. A ceded term has an owner
and the PDP is not it. Taking a cut-qualified sub-floor primary beside it is exactly the outcome
the cede rule prescribes (`workforce-conventions.md`, 'When the earned term is hierarchy-invalid'),
not an accident to be flagged. Recorded so the overlap reads as deliberate.

The shape follows the established national-team PDP precedent in the registry:
`mexico 2026 home jersey`, `croatia jersey 2026`, `croatia youth away jersey 2026`,
`bosnia jersey 2026`. Nation plus cut is PDP territory; the bare nation head term is the
collection's.

**Volume: 50/mo (Google Ads and DFS Labs agree). Sub-floor and flagged as such.** The higher-volume
alternative `umbro guatemala jersey` at 880/mo was rejected on hierarchy: brand plus nation is a
term a searcher would satisfy with several products, so it belongs to `/collections/guatemala`,
which is live and already the strongest performer in the lane. Volume never overrides hierarchy.

### Finding B. The Haaland lane already holds two registry primaries, and neither is the one assigned

| Registry primary | Page | Batch |
|---|---|---|
| `nike phantom 6 low elite fg` | `...-cleats-shadow-fa26` (the **Shadow** pack, Elite Low FG) | B6 |
| `nike phantom 6 low pro fg erling haaland` | `...-cleats-erling-haaland-pack-fa25` (the **Pro** Haaland) | B15 |

So the unqualified Elite Low FG configuration term is held by the Shadow incumbent, and the Pro
tier of this very pack is separately claimed. Under pack succession alone this page would take
`nike phantom 6 low elite fg erling haaland`, a pack-qualified sub-floor primary.

**It does not, and the reason is that the ranking-aware posture (v2, approved 2026-08-27)
supersedes conventional assignment for a page that already earns a term.** This page earns
`haaland cleats` at 54.6% share and term position 6.08. The posture is explicit: the primary is the
term the page already earns, and copy supports that term rather than redirecting the page. The
read-outs lock it.

The hierarchy amendment test was run on the contested term and it comes out for the PDP:
`/collections/nike-haaland-pe-pack` takes 37.0% of `haaland cleats` at position 10.73 against the
PDP's 54.6% at 6.08. The PDP earns more and sits materially better, so under step 3 of the
amendment the PDP holds the term.

`haaland cleats` shares no two-token overlap with either registry entry, so nothing collides. The
pack-qualified configuration term is carried as a **secondary** so the Shadow incumbent's
unqualified term is not disturbed and the configuration is still covered.

---

## Intra-batch

Nine distinct primaries, no duplicates. The five jerseys sit on five different nations or clubs.
The two national-team pages that could have collided were pre-empted at selection: Colombia was
pulled (the earning page is the sold-out Authentic Away, not the pick), and only one of the three
qualifying in-stock Paraguay pages was taken.

## Sibling exposure that is NOT cannibalization but must be stated in the briefs

Two pages sit on terms where we own untouched pages that outperform or crowd them. Neither is a
collision to resolve; both are facts the author must not write around.

- **Spain (B-CANNIB-02).** Four of our own pages split 85% of the 22,455-impression
  `spain jersey 2026` and collect about nine clicks between them. The selected page is **not** the
  best-positioned of the four. The brief must not read as though the page is alone on the term.
- **USMNT shorts.** The sibling `usmnt-mens-stadium-away-shorts` holds 36.3% of `usmnt shorts` at
  position **7.28, better than our 10.57**. Same discipline.

Both are carried into the per-SKU input files as explicit constraints.
