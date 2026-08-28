# Batch 17 dispatch handoff

**Written:** 2026-08-28 | **Author:** ORIN | **For:** a fresh session that starts authoring immediately

**Nothing has been authored. There is no Batch 17 session folder.** Planning is complete and
locked; pre-dispatch has not started. Start at step 1 below.

---

## 1. Repo state

- **HEAD: `25ee84a`**, equal to `origin/main`. Nothing unpushed.
- Working tree clean apart from four pre-existing untracked items that are NOT yours to touch:
  `deliverables/client-presentations/`, `docs/workforce-v2-refactor-promt.md`,
  `scripts/_wordcount_probe.py`, `scripts/test-firecrawl.ps1`.
- **`deliverables/tracking/products-master.csv`: 178 data rows** (173 `shipped`, 4 `pending`,
  1 `intentionally-unoptimized`). Batch 17 will append 9 rows at step 14, not now.
- Most recent completed session folder: `deliverables/page-optimizations/2026-08-26_session-02`
  (Batch 16). Copy its shape.

## 2. The two authoritative documents

Read both before anything else. **They are the authority on which nine SKUs, what primary each
takes, and what the batch is measuring. Do not re-derive any of it.**

- `deliverables/page-optimizations/2026-08-27_batch-17-candidates.md`
  The nine, how the pool was cut, per-page selection rationale, and the flags Mike accepted
  (thin stock on three, the deliberate single-Paraguay choice, why Colombia was pulled).
- `deliverables/page-optimizations/2026-08-27_batch-17-readouts.md`
  **Locked read-outs**, frozen baselines, the control design, and the canonical-versus-variant
  split.

**The read-outs are LOCKED. They were written before authoring precisely so results cannot be
rationalised afterwards. Do not adjust them to fit the copy that gets written.** If authoring
turns up something that appears to invalidate a read-out, surface it to Mike; do not edit it.

## 3. The nine, with the primary decision already made

| # | Handle | Earned term | Term pos | Band | Stock |
|---|---|---|---|---|---|
| 1 | `umbro-2025-2026-guatemala-mens-home-soccer-jersey` | `guatemala soccer jersey` **CEDED** | 4.88 | under 5, protected | 2/6 |
| 2 | `adidas-2026-spain-mens-stadium-away-soccer-jersey` | `spain jersey 2026` | 5.50 | 5 to 10 | 3/8 |
| 3 | `puma-2026-paraguay-mens-authentic-home-soccer-jersey` | `paraguay jersey` | 4.89 | under 5, protected | 5/5 |
| 4 | `adidas-2026-italy-mens-authentic-home-soccer-jersey` | none | n/a | n/a | 5/6 |
| 5 | `nike-phantom-6-low-elite-firm-ground-soccer-cleats-erling-haaland-pack-fa25` | `haaland cleats` | 6.08 | 5 to 10 | 2/15 |
| 6 | `adidas-2026-27-club-america-mens-authentic-home-soccer-jersey` | `america jersey 2026` | 3.50 | under 5, protected | 6/6 |
| 7 | `nike-2026-27-usmnt-mens-stadium-home-shorts` | `usmnt shorts` | 10.57 | 10 to 20, standard | 4/4 |
| 8 | `panini-2026-fifa-world-cup-stickers-box-50-packs-each` | none | n/a | n/a | 1/1 |
| 9 | `nike-strike-sleeves-socks` | none | n/a | n/a | 6/10 |

### Six earned-term pages take the term they already earn

Rows 1, 2, 3, 5, 6, 7. **The primary is the term the page already earns. Copy supports that term;
it does not redirect the page.** Canonical rule: `context/workforce-conventions.md` 'Ranking-aware
posture (v2)'.

**One exception, row 1. Guatemala CEDES `guatemala soccer jersey` to `/collections/guatemala`**,
which takes 8,131 impressions and all 180 clicks on the term against the PDP's 6,450 and zero.
The PDP takes a **qualified primary** you assign. It still records `earned_term` and
`earned_term_position` as measured, because the band protects the title and H1 from disturbing an
existing position regardless of which primary the page targets.

### Three failed the concentration threshold

Rows 4, 8, 9 (Italy, Panini, socks). A term qualifies as earned only at **>=15% of the page's
impressions AND >=1,000 term impressions** over 90 days. These sit at 4.5%, 1.1% and 6.1%.

**They take conventional KIRA primaries, derived normally, not lifted from a top query.** Their
`earned_term_position` goes in as the string `"not-ranking"`, which is an **explicit declaration
the gate accepts**, never an omission. Set `earned_term` to `""`.

### Correction to the band count

Mike's instruction said three pages sit under position 10. **Five do**: Guatemala 4.88, Club
America 3.50, Paraguay 4.89, Spain 5.50, Haaland 6.08. The split is:

- **Three under 5 (rows 1, 3, 6): PROTECTED.** The brief MUST carry the WARNING line, and Title
  and H1 changes need Mike per page. The gate fails the batch if the WARNING line is absent.
- **Two at 5 to 10 (rows 2, 5): exact-match retention.** Title and H1 may be improved but MUST
  retain the earned term verbatim. No Mike gate. State the earned term and its position in the
  brief so the constraint is auditable.

Either way the exact-match constraint applies to all five and must be stated in each brief.

## 4. New mandatory gate-meta fields

**`earned_term` and `earned_term_position` are REQUIRED in every per-SKU `gate-meta` block.**
`scripts/batch_gate.py check_ranking_input` FAILS the batch when the position is absent or
malformed, when a page under 5 carries no WARNING line, and when a 5-to-10 page drops the earned
term from its Title. Eight regression tests; the suite is green at 66 tests.

The values are in the table above. Positions are **earned-term positions**, not page averages, and
the distinction is load-bearing: Club America is 5.48 page-average against 3.50 on its term.

**A known gap, not triggered by this batch.** For a page that CEDES its earned term while sitting
in the 5-to-10 band, the gate would demand the ceded term appear in the Title, contradicting the
cede. Guatemala is the only ceding page here and it is under 5, so it takes the WARNING branch and
no conflict arises. **Flag it if a future batch produces a ceding page at 5 to 10.**

## 5. The seven-step pre-dispatch sequence. None of it has run

1. **Create `deliverables/page-optimizations/2026-08-28_session-01/`** with an `inputs/`
   subfolder.
2. **Write `inputs/_registry1_primaries.txt`**, one claimed primary per line from
   `products-master.csv`, with any pending retargets applied. **The gate hard-fails without it**
   (`registry1-missing` is a batch-level FAIL). This is not optional and its absence is not a skip.
3. **Pre-dispatch cannibalization check** against the registry before any primary is finalised.
   Criterion 4 of the selection already filtered all nine against 429 registry and ceded terms,
   but that check only knows terms the registry records, which is the whole point of B-DETECT-01.
   Run the manual pass.
4. **Phase 0 scrape** of all nine live PDPs via `mcp__firecrawl-mcp__firecrawl_scrape`, one pass
   for the batch. Scrape-wins discipline: a value the scrape did not supply is marked
   "not in scrape", never invented.
5. **Write nine `inputs/<SKU>_input.md` files** to `templates/per-sku-input-template.md`: Phase 0
   scrape data, KIRA keyword table, validated internal links (200 plus H1 and product-count
   content signals), differentiation lane, structure skeleton, three-tier forbidden phrasings, and
   the `gate-meta` JSON block including the two new fields.
6. **Dispatch SCRIBE, one agent per SKU**, nine parallel, each pointed at its input file. Free-form
   markdown return; ORIN verifies from the written files, not from the agent's report.
7. **Run `python scripts/batch_gate.py <session>` to exit 0**, then write `_STEP2-HANDOFF.md`.

Naming convention for briefs, from Batch 16: `<SKU>_<handle>.md`.

## 6. What from this session's diagnostics authoring actually depends on

**Only these three. Everything else is closed and logged.**

1. **The copy on these pages is genuinely broken and fixing it is worth doing on its own terms.**
   Every PDP title is the raw product name plus the theme suffix. Metas are either the product
   name repeated at 54 characters or an unedited body-copy dump at 324 to 327 characters, one
   opening with an escaped HTML entity. This is what a person sees when the page IS served as an
   organic result.

2. **Batch 17 is a test, not an optimization batch.** The hypothesis, stated in the read-outs:
   does copy move a page whose impressions come substantially from non-snippet surfaces? Expected
   answer, no or barely. **This does not change how the briefs are written.** It changes how the
   result is read, and the read-outs already encode that. Write the best briefs you can.

3. **Row 2, Spain, must state its sibling split explicitly in the brief.** Four of our own pages
   split 85% of a 22,455-impression term and collect about nine clicks between them, and the
   selected page is not the best-positioned of the four. The author must not write as though the
   page were alone on the term. Filed as B-CANNIB-02.

**Deliberately excluded: the entire B-TECH-03 investigation** (merchant listings, feed status,
review coverage, rich-result variance). It is closed, logged in `strategy/sprint-backlog.md`, and
**it is not needed to write nine briefs.** Do not read it in.

## 7. Standing rules that bite on this batch specifically

- **The live title governs; the handle is never a source of product attributes.** Read tier, cut,
  surface, age band and closure from a fresh fetch of the live title.
- **No batch selection from a `-N` suffixed handle** until B-DUP-04 is classified. None of the
  nine carries one; do not introduce one if a SKU gets swapped.
- **Thin stock on three** (Haaland 2/15, Guatemala 2/6, Spain 3/8). Mike accepted these knowingly.
  Do not silently drop them, and do not write copy that implies broad availability.
- Meta Title max 48 characters for the written part, never ending with a manufacturer brand as a
  pipe suffix. Meta Description 120 to 160, full sentences, no colon opener.
- `### URL Handle` must restate the handle verbatim before any no-change rationale.
- Push is instruction-gated. Commit at batch close autonomously; **do not push without Mike saying
  so.**

## 8. First action for the next session

Read the two documents in section 2, then execute step 1 and step 2 of section 5. Do not
re-litigate the nine, the primaries, or the read-outs.
