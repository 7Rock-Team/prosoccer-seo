# Batch 9 — RESUME (session handoff 2026-07-22)

## ⏸ PAUSED Wed 2026-07-22 — resume Monday. All 10 SCRIBE background agents STOPPED.

### Rebuild stop-state (verify each Monday with `grep -L "Product Details" <session>/*.md`)
- **Rebuilt to full template (present, but some killed mid-trim so may be OVER word-band — re-gate):** KC4794, KA6868, KC4803, KC4786, UT1FL4GK, UT3FL7NF.
- **NOT rebuilt (still the truncated 7-field version — must re-dispatch SCRIBE):** JZ7206, UF1F7R4, UF3F51W, YF3F3V9.

### ⚠️ ROOT WORD-BAND ISSUE to fix FIRST on Monday
The gate counts the FULL `## Description` body (BODY_START `## Description` → BODY_END `## Meta Title`), i.e. all prose H2s + Product Details + Fit Notes + Care + FAQ. The `word_band` I put in each input's gate-meta ([280-340]/[340-390]/[400-450]) was calibrated to the OLD prose-only briefs and is WRONG for the full template — the Batch 8 exemplar KA6871 full body is ~528 words and passed. **Every SCRIBE hit this: they kept trimming real sections to fit a band that's too low.** Fix: read `deliverables/page-optimizations/2026-07-13_session-01/inputs/KA6871_input.md` for the correct full-template band, then recalibrate `word_band` in all 10 Batch-9 input files BEFORE re-running SCRIBE/gate. Do NOT let SCRIBE trim mandatory sections to hit a stale band.

---


## Where things stand
Batch 9 = 10 PDP briefs. Session dir: `deliverables/page-optimizations/2026-07-21_session-01/`.
The briefs were being REBUILT to the full PDP template after a structural miss.

### Root cause (fixed, do not repeat)
ORIN authored the 10 briefs directly, bypassing SCRIBE, so the `product-page-playbook.md` brief-structure spec was never applied. Briefs shipped a truncated 7-field shape (Title/Short/Description/Meta Title/Meta Desc/URL/Links) — MISSING Product Details, Fit Notes, Care & Maintenance, FAQs, Image Alt Text, Taxonomy, Quick Reference, Keywords table. Word-band failed by construction; the expansion padded prose and produced 11 claim-risky sentences (all fixed pre-rebuild). **Hard rule now: ORIN orchestrates, SCRIBE authors — never author briefs directly.**

### Setup complete
- `inputs/_brief-template.md` = mandatory PDP section list + all voice/claims/gate rules.
- All 10 `inputs/<SKU>_input.md` carry: Phase-0 scrape data, primary/supporting keyword (with volumes), avatar, forbidden phrasings, gate-meta (word band/brand/tier), AND a prepended MANDATORY STRUCTURE block.
- 5 codification candidates logged in `work-log/follow-ups.md` (false-green; input-sequencing; post-Layer-3 claim-risk; gate field-presence; ORIN-no-direct-author).

### Rebuild status
10 SCRIBE subagents were dispatched (background) to rebuild each brief to the full template. Background agents DO NOT survive into a new session.
- **KC4794 = CONFIRMED rebuilt** (full template, verified good).
- **Other 9 = status unknown in a fresh session** — must be checked.

## NEXT SESSION — do this
1. For each of the 10 brief files, check whether it has the FULL template (has `## Product Details`, `## Fit Notes`, `## Care and Maintenance`, `## FAQs`, `### Image Alt Text`, `### Taxonomy Category`, `## Quick Reference`, Keywords table). Quick check: `grep -L "Product Details" deliverables/page-optimizations/2026-07-21_session-01/*.md` lists any still-truncated briefs.
2. Re-dispatch SCRIBE (subagent_type on-page-seo) for any NOT rebuilt, using the same prompt pattern: read `inputs/<SKU>_input.md` + `inputs/_brief-template.md` + `context/page-type-playbooks/product-page-playbook.md` + current draft; overwrite with full template; specs from scrape only; no invented performance/durability/comparative claims; qualitative heritage; cleat not boot; NB non-FIFA; no em-dash; no price in body.
3. Run `python scripts/batch_gate.py deliverables/page-optimizations/2026-07-21_session-01` — fix any FAIL (word-band should now pass via real sections, not padding).
4. Run Layer 3 over the rebuilt briefs, focus on the NET-NEW sections (Product Details / Fit Notes / Care / FAQs) — disposition every claim PASS-WITH-SOURCE (scrape field) / PASS (qualitative) / FIX. Watch performance/safety/durability/comparative claims (the class the gate can't see). Note: Furon Team (UF3F51W) + Jr Furon (YF3F3V9) scrapes have NO durability spec; Tekela Team (UT3FL7NF) scrape DOES ("durable material construction").
5. Report to Mike when gate-green AND Layer-3-clean. NOTHING PUSHES until Mike clears.

## Commit sequence (Mike runs it — dontAsk blocks ORIN git mutations)
```
git add deliverables/page-optimizations/2026-07-21_session-01 \
        context/silo-positioning/furon.md context/silo-positioning/tekela.md \
        context/silo-positioning/club-team-jerseys.md work-log/follow-ups.md
git commit -m "Batch 9: 10 gate-green PDP briefs (full template) + NB/Real Madrid silo firsts

..." (see prior end-of-batch report for full message)
git push origin main && git rev-parse --short HEAD
```

## Reference: the 10 SKUs (SKU / brief file / primary kw / tier band / near-sold-out)
- JZ7206 real-madrid-mens-stadium-home / `real madrid jersey` 60,500 / stadium 280-340
- KA6868 man-united-mens-authentic-home / `manchester united jersey` 22,200 / authentic 340-390 (in stock 4)
- KC4803 man-united-mens-authentic-home-ls / `manchester united long sleeve jersey` 880 / authentic 340-390 (2 left)
- KC4786 man-united-youth-stadium-home-ls / `manchester united youth jersey` 210 / stadium 280-340 (1 left)
- KC4794 man-united-womens-stadium-home / `manchester united womens jersey` 210 / stadium 280-340 (1 left) [REBUILT]
- UT1FL4GK nb-tekela-elite-low-wide / `new balance tekela` 1,300 / elite 400-450 (1 left) — 209.1 g, control lane
- UF1F7R4 nb-furon-elite-wide / `new balance furon` 1,300 / elite 400-450 (1 left) — 176 g, speed lane
- UT3FL7NF nb-tekela-team-low-wide / `wide soccer cleats` 2,900 / team 280-340 (1 left) — 243.2 g, Mom avatar
- UF3F51W nb-furon-team-wide / `new balance soccer cleats` 8,100 / team 280-340 (1 left) — 223 g, Mom avatar
- YF3F3V9 nb-jr-furon-team-wide / `youth soccer cleats wide` 1,300 / stadium band 280-340 (2 left) — 134 g, Mom buyer!=wearer
