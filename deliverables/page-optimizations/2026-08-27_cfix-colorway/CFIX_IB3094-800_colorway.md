# C-FIX: IB3094-800 colorway correction (single row)

**Date:** 2026-08-27
**Scope:** ONE product. `nike-phantom-6-low-pro-firm-ground-soccer-cleats-erling-haaland-pack-fa25`
**SKU:** IB3094-800. Shipped in **B15**, `implementation_date` 2026-08-19, `status` shipped.
**Ships as:** a single-row Matrixify MERGE, the same shape as the IQ2388 fix.

---

## 1. What is wrong

The live copy describes the cleat as running **"red and yellow"**. The authoritative colorway, read from the Shopify `Color` product option, is:

> **Laser Orange / Blue Void / Lemon Venom**

There is no red in it. A buyer reading the description gets a shoe that does not match it. That is the whole reason this is a fix-forward and not a backlog note.

## 2. Nobody guessed, and that is the point

**This was not a fabrication and no one working on it made an error against the rules that existed at the time.**

- The phrase "red and yellow" is **Nike's own marketing prose on the live PDP**.
- The Phase 0 input file for IB3094-800 quoted that prose verbatim and, at line 69, explicitly authorised it: *"The colourway story IS on the live page and is sourceable: blue in the heel and core for calm, transitioning to red and yellow. You may use it."*
- SCRIBE followed an explicit authorization against a real, on-page, sourceable claim. Scrape-wins was satisfied.

**The contradiction is Nike's, between its own marketing copy and its own colorway name.** Nike's prose calls Laser Orange "red". Both strings are on the same page.

At the time the brief was written there was no rule saying which on-page source wins for colorway, so the page shipped with the prose. **The colorway exception now resolves it** (`context/workforce-conventions.md`, "The live title governs" -> THE COLORWAY EXCEPTION): the `Color` option is authoritative for colorway, and marketing prose is not.

**Record this as the reason the rule exists, not as a defect anyone caused.** It resolved the case one week after the page shipped, which is exactly the cost of codifying at discovery rather than in advance. It is the same shape as the Nanostrike tier exception: the live page asserts something that contradicts the authoritative source, and until the rule named the authority, the page was the only thing to go on.

## 3. Where the claim lives: BODY, not meta

Checked field by field. **This is a body edit, not a meta-only edit.**

| Field | Shipped by import? | Carries the wrong colour? |
|---|---|---|
| Meta Title | yes | **No.** `Nike Phantom 6 Low Pro FG Haaland Pack` is clean |
| Meta Description | yes | **No.** Names the pack, no colour word |
| **Short Description** | **yes** | **YES, 1 instance** |
| **Body HTML** | **yes** | **YES, 3 instances** |
| Image Alt Text | **no** | YES, 1 instance. See section 6 |

## 4. Exact replacements for Step 2

**Apply these as literal find-and-replace against the Body HTML and short description in the Matrixify EXPORT. Do NOT regenerate the body from the brief.** The rendered HTML that shipped is not on disk here, and regenerating it would replace a whole field to correct four strings, which risks changing markup nobody asked to change.

**Short description (1 replacement):**

| | |
|---|---|
| FIND | `Blue in the heel, red and yellow up front.` |
| REPLACE | `Blue in the heel, Laser Orange and Lemon Venom up front.` |

**Body HTML (3 replacements):**

| | |
|---|---|
| FIND | `From there it runs forward into red and yellow, brightest where most goals get scored.` |
| REPLACE | `From there it runs forward into Laser Orange and Lemon Venom, brightest where most goals get scored.` |

| | |
|---|---|
| FIND | `Colorway: Erling Haaland Pack (FA25), blue heel into red and yellow` |
| REPLACE | `Colorway: Laser Orange / Blue Void / Lemon Venom (Erling Haaland Pack, FA25)` |

| | |
|---|---|
| FIND | `running into red and yellow at the cleat's brightest point.` |
| REPLACE | `running into Laser Orange and Lemon Venom at the cleat's brightest point.` |

Watch the apostrophe in the last one: the live HTML may carry a curly `’` rather than `'`. Match whichever the export contains.

**A second defect fixed in passing.** The Product Details bullet read `Colorway: Erling Haaland Pack (FA25)`, which names the **pack** as the colorway. A pack is not a colorway, and pack names routinely contain colour words. The replacement names the real colorway and demotes the pack to a parenthetical.

## 5. Import file

```
Handle,Command,Body HTML,new_short_description
nike-phantom-6-low-pro-firm-ground-soccer-cleats-erling-haaland-pack-fa25,MERGE,<corrected body>,<corrected short description>
```

`Command` = MERGE. No Title column. Expected job summary: **Updated 1 / Created 0**. A nonzero Created is a stop condition.

## 6. What this import does NOT fix

**Image alt text.** The brief's alt text carried `showing the blue heel and red forefoot`, corrected in the brief to `showing the Blue Void heel and Laser Orange forefoot`. **Alt text is not one of the four fields this import ships** (Body HTML, meta title, meta description, short description), so the live alt attribute keeps the wrong colour until someone does an alt-text pass. Flagged rather than silently left.

## 7. Verification

- Brief corrected in place: `deliverables/page-optimizations/2026-08-18_session-01/IB3094-800_nike-phantom-6-low-pro-fg-haaland.md`
- Body word count **386 -> 390**. Band for this SKU is **[340, 390]**, so it lands exactly on the ceiling and draws none of the 15-word tolerance.
- `scripts/batch_gate.py` re-run over the whole 2026-08-18 session after the edit: **PASS, exit 0**, 10 briefs, 0 findings.
- Zero `red` or `yellow` tokens remain anywhere in the file, asserted programmatically rather than by eye.
