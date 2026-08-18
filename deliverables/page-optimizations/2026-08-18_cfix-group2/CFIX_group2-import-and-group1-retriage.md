# C-FIX split: Group 2 import (3 rows) and Group 1 re-triage (9 rows)

**Built:** 2026-08-18 | **Authorized:** Mike, 2026-08-18 (split C-FIX; ship Group 2, re-triage Group 1)
**Status:** Group 2 import file BUILT and validated, not imported. Group 1 re-triage complete, 3 of 9 survive.

---

## 1. Group 2: the three rows that ship now

These unblock Batch 15 rows 2, 4 and 7 (final numbering, after the Tiempo Ligera reduction). Files in this folder:
`ProSoccer_SEO_CFIX_Group2_3_Products.xlsx` (primary) and `.csv` (fallback).

| C-FIX row | SKU | Handle | Term released | To Batch 15 row |
|---|---|---|---|---|
| 10 | IH1779-900 | `nike-phantom-6-high-elite-firm-soccer-cleats-breakout-pack-su26` | nike phantom 6 elite fg (cut-less) | **row 2** (HJ2147-003) takes `nike phantom 6 high elite fg` (210/mo) |
| 11 | IQ1886-900 | `nike-phantom-6-low-pro-firm-ground-soccer-cleats-breakout-pack-su26` | nike phantom 6 pro (880/mo, cut-less and surface-less) | **nobody takes it.** IQ1886-900 KEEPS `nike phantom 6 low pro fg` as the v3 incumbent; see 1a |
| 12 | HP9971 | `adidas-predator-elite-fold-over-tongue-artificial-grass-soccer-cleats-road-to-glory-pack-sp26` | adidas predator elite ag (590/mo) | **row 4** (JR5899) takes `adidas predator elite ag` (590/mo) |

**Strings are unchanged from the 2026-08-14 C-FIX build.** They were already Layer 3 claim-verified there; nothing was re-authored, so nothing needs re-verifying. Copied verbatim.

**Validation run before the file was written** (the script refuses to write on any failure):

| Check | Result |
|---|---|
| Meta title <= 48 chars | 37, 34, 41 |
| Meta description 120 to 160 | 144, 136, 148 |
| `Command` = MERGE on every row | pass |
| No em dash or en dash | pass |
| `adidas` lowercase at position 0 | pass |
| No manufacturer-brand pipe suffix | pass |
| No colon-fragment opener | pass |
| Sheet named exactly `Products` | pass |
| All three handles live in the sitemap | pass, checked against the 14,402-product fetch |

No Title column, no Body HTML, no short description. Only `title_tag` and `description_tag` ship, which is the preservation guarantee.

## 1a. Row 11's registry outcome, decided 2026-08-18

Mike's ruling: **v3 wins.** IQ1886-900 is the measured incumbent at Phantom 6 Low Pro FG (523 impressions) and **keeps the unqualified `nike phantom 6 low pro fg`** (70/mo). Batch 15 row 7 (IB3094-800, 363 impressions) takes the pack-qualified `nike phantom 6 low pro fg erling haaland` instead.

**The import file is unchanged and imports as built.** Row 11's shipped meta title, "Nike Phantom 6 Low Pro FG Breakout", names model, tier, cut, surface AND pack, so it reads correctly under either primary. Only the registry differs.

**Registry state to write at step 15, on confirmed import** (not before, per the step 15 rule):

| SKU | `primary_keyword` before | after | `primary_volume` |
|---|---|---|---|
| IQ1886-900 | nike phantom 6 pro | **nike phantom 6 low pro fg** | 70 |
| IH1779-900 | nike phantom 6 elite fg | nike phantom 6 high elite fg breakout | none |
| HP9971 | adidas predator elite ag | adidas predator elite fold over tongue ag road to glory | 10 |

Note that IQ1886-900's row differs from what the 2026-08-14 C-FIX document specified (`nike phantom 6 low pro fg breakout`). That document was written under the old incumbency rule. This supersedes it.

**Note on row 11.** It releases `nike phantom 6 pro` at 880/mo, and no Batch 15 row claims it. It is cut-less and surface-less, so it is not PDP-valid under the keyword hierarchy. It belongs to `/collections/nike-phantom`, which is live. Routed to the collection workstream, not silently dropped.

---

## 2. Group 1 re-triage: 3 of 9 survive

Bar set by Mike: **measurable earned impressions, or a customer-visible defect.**

The raw impression test alone passes almost everything (all nine pages earn something, none earn zero), so it is the wrong test on its own. The right question for a retarget is not "does this page earn," it is **"is the retarget still pointing the right way."** Under the v3 incumbent definition Mike ruled today, that question has a new answer for two rows.

### The nine, against page-level GSC (2026-07-17 to 2026-08-14)

| Row | SKU | Page impr | Config total | Rank in config | Top earner in config | Verdict |
|---|---|---|---|---|---|---|
| 1 | HQ2278-001 | 121 | 2,145 | 5 of 9 | High Academy FG/MG Breakout (1,247) | **DROP** |
| 2 | HQ2277-001 | 73 | 364 | 3 of 4 | High Academy Turf Attack SP26 (139) | **SURVIVES** |
| 3 | HJ4564-001 | 92 | 1,463 | 6 of 9 | Low Academy FG/MG (398) | **DROP** |
| 4 | IO1494-001 | 160 | 233 | **1 of 3** | itself | **DROP, retarget is backwards** |
| 5 | IM0358-001 | 482 | 1,103 | 2 of 5 | Club FG/MG Breakout (516) | **DROP, too close to call** |
| 6 | IB1600-001 | 91 | 517 | 3 of 5 | Maestro Academy FG/MG (241) | **DROP** |
| 7 | 540394.9025 | 124 | 4,234 | 2 of 3 | Beta Elite Prism White FA26 (4,110) | **SURVIVES** |
| 8 | 540396.9025 | **1,068** | 1,089 | **1 of 2** | itself (98% of config) | **DROP, retarget is backwards** |
| 9 | HQ2325 | 41 | 2,601 | 6 of 7 | Low Academy Turf Haaland (1,256) | **SURVIVES** |

### Rows 4 and 8: the retarget is backwards under the v3 rule

Both pages are the **top earner at their own configuration**, so under the incumbency definition Mike ruled today they ARE the incumbent and should KEEP the unqualified term. C-FIX would strip it from them.

Row 8 is the stark one: `mizuno-morelia-neo-v-beta-pro-fg-soccer-cleats-bright-black` earns **1,068 of the config's 1,089 impressions, 98% of it.** The C-FIX retarget would move `mizuno morelia neo beta pro` off that page and leave the term for a sibling earning 21. That is the exact inversion the Predator Elite AG case exposed, and it is inside C-FIX itself.

Row 4 is smaller but the same shape: 160 impressions, rank 1 of 3.

Both were correct under the old season-earliest rule and are wrong under the new one. This is the first live test of the v3 ruling and it changed two decisions.

### Row 5: dropped by the churn guard, not by the bar

482 against a config top of 516. That gap is well inside noise for a 29-day window, and the churn guard says incumbency does not move on a single period's near-tie. Re-measure at the next period rather than acting on a 34-impression difference.

### Rows 1, 3 and 6: the zero-to-zero cases Mike predicted

Each page is mid-pack in its config, and each releases a term with no measurable demand (`nike phantom 6 high academy fg mg` no volume, `nike phantom 6 low academy fg mg` 10/mo, `nike tiempo maestro academy fg mg` no volume). Correct in principle, worth nothing in practice. They fail both legs of the bar: the freed term has no measurable earnings and there is no customer-visible defect. Dropped.

### The three that survive

- **Row 2 (HQ2277-001).** Releases `nike phantom 6 high academy turf` at 70/mo, real measured demand, and the page ranks 3rd of 4 in its config so it is not the incumbent. **One correction: the C-FIX rationale names the wrong beneficiary.** It says the term "belongs to the Scary Good FA25 incumbent." Under v3 it belongs to Attack Pack SP26 (139 impressions); Scary Good FA25 earns 24. The retarget direction is right; the stated recipient must be fixed before this ships.
- **Row 7 (540394.9025).** 124 impressions against a sibling at 4,110. Clearly not the incumbent, and it releases a 30/mo term to a page that dominates the config.
- **Row 9 (HQ2325).** Survives on the defect leg, not the impressions leg. It holds `nike phantom 6 academy turf shadow`, which carries no cut token while both a High and a Low Academy Turf Shadow FA26 page are live. The term describes two products, so it cannot resolve to one. That is a genuine targeting defect (B-DUP-03) and it stands independent of what the page earns.

---

## 3. What this means for C-FIX

The original 12 becomes **3 shipping now (Group 2) plus 3 surviving from Group 1**, with 6 dropped. If Mike wants the survivors shipped, rows 2, 7 and 9 can be appended to this import or held for the next correction batch. Row 2's rationale needs the beneficiary corrected first.

Recommendation: ship Group 2 alone now, because it is what unblocks Batch 15 and it is already verified. Fold rows 2, 7 and 9 into the next correction batch (B-FIX-01) rather than widening this import.

---

## 4. Provenance

- Page-level GSC: `sc-domain:prosoccer.com`, dimension `page`, 2026-07-17 to 2026-08-14. Two pulls: the six Batch 15 model families (2,362 rows) and a second scoped to `superfly-11|morelia-neo` for the four Group 1 rows outside the first regex. Variant, locale and UTM URL forms folded into parent handles.
- Live sitemap: 14,402 products, fetched 2026-08-16.
- Scripts: `retriage.py`, `retriage2.py`, `build_g2.py` in the session scratchpad.

**Nothing imported. Nothing pushed.**
