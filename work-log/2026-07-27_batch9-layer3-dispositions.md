# Batch 9 — Layer 3 dispositions on post-read and pre-commit edits (2026-07-27)

Records the independent Layer 3 claim disposition for every string authored or edited AFTER the initial Layer 3 read pass, so nothing ships without a recorded disposition. Prompted by Mike's pre-commit verification (Item 4). Session dir: `deliverables/page-optimizations/2026-07-21_session-01/`.

Disposition key: **PASS** (qualitative or self-evidently non-claim) / **PASS-WITH-SOURCE** (tied to the SKU's Phase-0 scrape or a cited live-PDP scrape) / **FIX** (cut or rewritten).

## 1. Strings authored during the first Layer 3 pass (previously un-re-audited)

- **KA6868** — "United sit among England's most decorated clubs, with a long Premier League history and European nights the city still remembers."
  - "among England's most decorated clubs": **PASS** (approved qualitative heritage; no title/trophy count, no "most successful/record" superlative; gate `check_heritage_*` clean).
  - "a long Premier League history": **PASS** (qualitative; Premier League is nameable directly on club-jersey PDPs per `context/silo-positioning/club-team-jerseys.md`).
  - "European nights the city still remembers": **PASS** (generic European reference, heritage tense; no competition named, no count, no present-tense current-form claim). Replaced the earlier "near the top of the Premier League" current-form line.

- **UF3F51W** — "They carry a genuine 2E wide fit, so wide feet get real room at their normal size; narrow feet may prefer a standard width."
  - "genuine 2E wide fit": **PASS-WITH-SOURCE** (2E Wide is in the Phase-0 scrape and the live PDP title/spec).
  - "wide feet get real room": **PASS** (qualitative consequence of the 2E last).
  - "narrow feet may prefer a standard width": **PASS** (hedged fit guidance, "may prefer"; no true-to-size assertion). Replaced the earlier unsourced "They fit true for most players" true-to-size claim.

## 2. Edits made this pass (Items 1 and 2)

- **KA6868 meta description** (Item 1, trimmed to 160 chars): "The player-grade Manchester United jersey for 2026-27: the Authentic cut in Red Devils red, with the flat-knit striped collar that nods to United's 1970s teams." — **PASS-WITH-SOURCE** (Authentic player-grade cut, Red Devils red, flat-knit striped collar, 1970s tribute all in the Phase-0 scrape). Cut trailing "Official and licensed." (a claim removed, not added).

- **UT1FL4GK meta description** (Item 1, rewritten to 147 chars): "The New Balance Tekela Elite: control in a true 2E wide fit. Microfiber upper, firm-ground plate, 7.4 oz. For the playmaker tired of narrow cleats." — **PASS-WITH-SOURCE** ("control" = live PDP "Crafted for Control"; 2E wide, microfiber PU upper, FG plate, and 209.1 g = 7.4 oz all in the Phase-0 scrape and the 2026-07-27 live scrape). "playmaker tired of narrow cleats": PASS (qualitative).

- **Title / Quick Reference / doc-H1 corrections on the 5 New Balance cleats** (Item 2 — UT1FL4GK, UF1F7R4, UT3FL7NF, UF3F51W, YF3F3V9): each set to the exact live product title. **PASS-WITH-SOURCE** — cited to a fresh live-PDP H1 scrape on 2026-07-27 (the store product titles, which are never changed). These are factual product-name corrections, not marketing claims. In-prose short references ("the Tekela Elite", "the Furon Team", "the Jr Furon") were retained as valid shorthand; none assert a wrong generation or tier.

## Result
Gate re-run after all edits: PASS, EXIT 0 (no findings). All 10 meta descriptions <= 160 chars. All 10 brief Titles and Quick References match the live product title verbatim.
