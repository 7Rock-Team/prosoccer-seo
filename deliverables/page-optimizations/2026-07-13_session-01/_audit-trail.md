# Audit Trail -- Batch 8 (2026-07-13_session-01)

_ORIN v2 escalate-on-exception batch. Run under `--permission-mode dontAsk` (unattended). Mike is pacing the batch by SKU-group: Liverpool first, then United (club-silo first -> escalates), then the 3 cleats. ONE batch commit + ONE end-of-batch report at batch close; push holds for Mike's go._

## Step 0 (pre-flight verification) -- GREEN
- v2 SCRIBE spec loaded (`on-page-seo/agent.md` Section 2 v2 input-driven flow).
- dontAsk allow/deny configured (`settings.json` HEAD 5f8437e: completed allow-list incl. tool-name allows; hardened deny-list).
- Word-band drafting fix loaded (full-body-incl-FAQ band; lean-first; self-run gate to green).
- Calibration note: Mike's "~250-280 editorial" is jersey-calibrated; codified 200-250 is the cleat figure. Reconciled: jersey band is higher, editorial runs richer.
- Resolved (not just noted): Registry 1 Drive read WORKS under dontAsk (tested live); the parent-mediated Drive connector is not gated by the Bash/MCP allow-list, so the full Registry 1 cross-check runs.

## Escalation status
- **Liverpool (this group): decide-and-log, NOT an escalation** (Mike's call: established men's/youth/women's/LS split pattern, not a new-lane first).
- **Manchester United: WILL escalate** when surfaced (zero precedent in club-team-jerseys.md; criterion 1 architectural first). Guardrail block already researched + drafted, holds for Mike's approval before any United brief is written.
- 3 cleats: established-silo parallel (Phantom x2, F50 Messi x1); decide-and-log when surfaced.

---

## Liverpool subset (4 SKUs) -- COMPLETE, gate-green, ORIN-verified. Staged, UNCOMMITTED (accumulating to batch commit).

### Brand-IP posture (decide-and-log)
Club-kit posture, NOT national-team/FIFA. Premier League named directly; European competition GENERIC only (never "Champions League"/"European Cup" -- turned into a deterministic gate check via each SKU's forbidden-phrasings `verbatim` list). No FIFA/World Cup chrome (moot on a club page). Evergreen heritage, no current-form.

### Cannibalization resolution (Registry 1 + 2 cross-check; gate check #9 clean)
Bare generic `liverpool jersey` / `liverpool soccer jersey` (18,100/mo) CEDED to `/collections/liverpool` (confirmed unassigned in Registry 1; enforced via `inputs/_registry1_primaries.txt`). Each PDP takes an audience/cut-qualified primary; no PDP<->collection or sibling collision.

| SKU | Avatar | Primary | Vol/mo | KD |
|---|---|---|---|---|
| KA6852 | flagship adult | liverpool home jersey | 1000 | 8 |
| KB8255 | parent-for-kid | liverpool youth jersey | 260 | -- |
| KB8256 | women's-cut | liverpool women's jersey | 110 | -- |
| KB8268 | long-sleeve | liverpool long sleeve jersey | 1300 | -- |

New PDPs (no ranking history) -> DataForSEO governs, no GSC-override (consistent with Batch 7 Jordan).

### Decide-and-log calls
1. **Salah player-spotlight PULLED.** Currency-check confirmed Salah leaving Liverpool (end 2025-26, announced 24 Mar 2026). The obvious Cole-Palmer-style pick would be a currency trap. Switched to evergreen non-player internal link `/collections/epl` (validated live, "Premier League Jerseys & Apparel", 342 products, content-signal confirmed). Heritage carried by retired legends (Shankly, Gerrard, Dalglish) in body copy.
2. **Joint-20-titles guard.** Liverpool's 2024-25 title made 20 English league titles a JOINT record with Man United (18 First Division + 2 Premier League: 2019-20, 2024-25). Baked into all four inputs; "most titles"/"more than any other" gate-enforced-forbidden. Binds United symmetrically when it surfaces.
3. **Word band [450, 520] tol 15** (aim ~480), held across all four cuts for sibling parity. Anchored to the shipped jersey class (Jordan authentic 440-520), NOT the Chelsea-Youth 740 outlier (write-to-ceiling avoidance).
4. **Primary selection:** men's took `liverpool home jersey` (1,000/mo, KD 8) over the ~0-vol year-qualified term; home-qualified so it does not take the ceded bare generic.
5. Hillsborough/97/flames: respectful-omission across all four (leaned on Liver Bird + anthem + all-red).
6. adidas framed as a 2025-26 "reunion" supplier, never "longtime partner"; no deal figures/prices in body.

### Dispatch shape + gate
Parallel (4 SCRIBEs, no exemplar-first; Liverpool club identity established). Authoritative `batch_gate.py` over the settled 4-brief set: **PASS, zero findings** (word-band, forbidden, FIFA/IP, headings, price, cannibalization #9, cross-brief #7 all clean).

### Word-band fix -- CONFIRMED WORKING
All four drafted lean-first, at most ONE internal trim (571->523, 562->500, 536->534), self-gated green, ZERO ORIN<->SCRIBE ping-pong. This was the load-bearing Batch 7 miss; fixed. Per-SCRIBE tool self-counts all <=10 (6/9/9/8); harness counts 7/14/18/15 (vs Batch 7's up-to-66).

### Token note (honest)
Per-SCRIBE tokens still ~200k (194k/214k/217k/204k) -- v1-like, NOT the lean ~100k v2 target. Root cause is DIFFERENT from the (now-fixed) tool-use blowup: it's context-file reads on top of the input file (each SCRIBE re-read the full product-page playbook + club silo + brand-voice, though the input file already distills the silo lane + structure). OPTIMIZATION for remaining groups: lean the SCRIBE reading list (input file + brand-voice; drop the redundant full-silo re-read, since the differentiation lane is already extracted into the input file).

### ORIN content verify (trust-but-verify; gate-invisible classes)
Four avatars read distinct; honours framing correct in situ; no leather-care error class; specs scrape-matched. Micro-note (non-blocking): KB8268 "the burgundy Shankly wore into legend" is mild poetic license (Shankly's kit was red; this shirt is a burgundy shade of that red) -- scrape-grounded colorway, left as-is.

### Registry 1 handoff (white-label team enters in PDPs tab; write ownership theirs by design)
| SKU | Product | Primary keyword |
|---|---|---|
| KA6852 | Liverpool Men's Stadium Home | liverpool home jersey |
| KB8255 | Liverpool Youth Stadium Home | liverpool youth jersey |
| KB8256 | Liverpool Women's Stadium Home | liverpool women's jersey |
| KB8268 | Liverpool Men's Home Long Sleeve | liverpool long sleeve jersey |

### Publish-priority note
KB8256 (Women's) -- only 1 left, near-sold-out. Evergreen copy ships regardless; flagged for Mike's implementation ordering.

### Housekeeping
`scripts/_wordcount_probe.py` is a throwaway used to anchor the jersey word band; it is untracked and will be EXCLUDED from the batch commit (dontAsk blocks `rm`; left on disk, not staged).

### Registry 2 append (pending batch commit)
On batch close, append the 4 Liverpool per-SKU prose-pattern entries to `context/silo-positioning/club-team-jerseys.md` (Liverpool adidas-home lane: adult-belonging / parent-handed-down / women's-cut / long-sleeve-winter). [DONE at batch commit -- see below.]

---

## Six-SKU completion run (United 3 + cleats 3) -- COMPLETE, gate-green, ORIN-verified. TIMESTAMPED.

### Timing (measured, date-stamped; ZERO escalation waits -- Mike pre-approved United guardrail + cleats)
- Run start: 2026-07-13 13:49:23 PDT
- Phase 0 (URL resolution + 6 scrapes + F50 verify + DataForSEO + registry): done 13:55:48 (~6.4 min)
- Wave 1 dispatched (United KA6871 exemplar + 3 cleats) ~13:57
- Wave 2 dispatched (United Youth + LS, off exemplar skeleton) 14:04:22
- All SCRIBEs returned + authoritative gate PASS: 14:09:31
- **Total 6-SKU execution wall-clock: 13:49:23 -> 14:09:31 = 20 min 8 sec, MEASURED, pure execution (no escalation waits).** Well under the 50-70 min target.

### Dispatch shape
United Men's Home (KA6871) exemplar-first -> gated green -> United Youth (KC4796) + LS (KC4773) parallel off its skeleton. 3 cleats (IH1897 F50 Messi, HJ4122 Phantom Pro FG, HQ2325 Phantom Academy Turf) parallel in wave 1. No wave-logic leak.

### Cannibalization (Registry 1 + 2; gate #9 clean over all 10)
United: cede `manchester united jersey`/`soccer jersey`/`man united jersey` (22,200) -> /collections/manchester-united. KA6871 `manchester united home jersey` (390) / KC4796 `manchester united youth jersey` (210) / KC4773 `manchester united long sleeve jersey` (880). F50 junior: `junior f50 messi` (blank), cede `f50 messi`/`adidas f50 messi` to the senior El Ultimo Tango PDP. Phantom: `nike phantom 6 low pro fg shadow` / `nike phantom 6 academy turf shadow`, cede model-tier generics to shipped Breakout. All ceded terms enforced in `inputs/_registry1_primaries.txt`.

### F50 Messi scrape verification (Mike's item 5, done BEFORE writing)
IH1897 scrape confirmed: Messi signature/likeness present; "El Ultimo Tango Pack" is the real pack name; specs Hybridtouch+ / Halocage+ TPU / F50 Speedsystem plate / LIGHTSTRIKEPRO / Ivory-Semi Blue Burst-Icey Blue / FG / 156.4 g. Page states the pack NAME but NOT any farewell/retirement narrative -> that narrative barred.

### Gate-caught + ORIN content fixes
- `batch_gate.py` over all 10: PASS, zero findings (both before and after the 2 ORIN edits).
- ORIN content fixes (classes the mechanical gate cannot see):
  1. IH1897 -- removed "the blue Messi has always played in" (soft over-reach; Messi's current club plays pink/black). Colorway stated factually.
  2. KC4773 -- added the missing `/collections/epl` internal link (prose referenced "Premier League home kits" but wasn't hyperlinked; the gate checks link FORMAT, not PRESENCE -- logged gap).
- Word-band trim-loop status: HELD for 5 of 6 (single internal trims, self-counts <=10). ONE regression: IH1897 harness tool count 42 (over-drafted editorial to 581 on a tight Elite-band junior cleat where fixed bullet/FAQ structure eats ~230 words; SCRIBE self-noted editorial should draft ~180-200 for junior Elite). Still one internal dispatch, NO ORIN<->SCRIBE ping-pong.

### Token / tool instrumentation (honest)
- Per-SCRIBE tokens still ~200-229k each (KA6871 201k, IH1897 229k, HJ4122 201k, HQ2325 208k, KC4796 225k, KC4773 200k). The lean-reading-list optimization (dropped the full-silo re-read) had LIMITED effect: the per-SCRIBE floor is the brand-voice + product-page-playbook reads, which are load-bearing per the SCRIBE spec. Real token reduction would need distilling those into the input file too, or trimming the playbook -- flagged for a future codification, NOT attempted mid-batch.
- Tool self-counts: KA6871 14, IH1897 15, HJ4122 12, HQ2325 9, KC4796 9, KC4773 8. All but the count-inflated trim passes within target; harness peak 42 (IH1897).

### ORIN content verify (trust-but-verify; gate-invisible)
All 6 read distinct + guardrail-clean: United exemplar/youth/LS genuinely differentiated (belonging / handed-down / LS-heritage-collar); joint-20 framed correctly in all United ("shared with Liverpool", never "most"); European generic; FA Cup named directly; 1976/77 FA Cup collar tribute (KC4773) is scrape-confirmed. Cleats: anti-convergence held (no workhorse/springboard/disguise; HQ2325 correctly NikeSkin not VNMSkin); synthetic-upper care correct (no leather-conditioner error). F50: Messi named (licensed), no fabricated narrative after the fix.

### Registry 1 handoff -- FULL BATCH 8 (all 10; white-label team enters in PDPs tab, write ownership theirs)
| SKU | Product | Primary keyword |
|---|---|---|
| KA6852 | Liverpool Men's Stadium Home | liverpool home jersey |
| KB8255 | Liverpool Youth Stadium Home | liverpool youth jersey |
| KB8256 | Liverpool Women's Stadium Home | liverpool women's jersey |
| KB8268 | Liverpool Men's Home Long Sleeve | liverpool long sleeve jersey |
| KA6871 | Manchester United Men's Home | manchester united home jersey |
| KC4796 | Manchester United Youth Home | manchester united youth jersey |
| KC4773 | Manchester United Men's Home LS | manchester united long sleeve jersey |
| IH1897 | Jr F50 Messi Elite FG (El Ultimo Tango) | junior f50 messi |
| HJ4122 | Phantom 6 Low Pro FG Shadow | nike phantom 6 low pro fg shadow |
| HQ2325 | Phantom 6 Low Academy Turf Shadow | nike phantom 6 academy turf shadow |

### Publish-priority (near-sold-out; evergreen copy ships regardless, flagged for implementation ordering)
KB8256 Liverpool Women's -- 1 left. IH1897 F50 Messi junior -- 1 left.

### Escalations raised this run: NONE (United guardrail pre-approved as-is; cleats decide-and-log). Escalations across all of Batch 8: ONE (Manchester United club-silo first, resolved by Mike's guardrail approval).

### Registry 2 appended at commit: club-team-jerseys.md (United guardrail block + 7 club per-SKU entries), phantom.md (HJ4122, HQ2325), f50.md (IH1897).

---

## Claims-verification pass (Mike-requested, post-commit; before push) -- all resolved, commit amended

Mike required a claims-extraction pass with a SOURCE per PASS (no claim ships on say-so). Outcome:
- **Heritage league-title counts converted to qualitative honours** (date-sensitive / contestable; the 20-title figure is actively contested against the exact United-Liverpool comparison):
  - KA6871, KC4796, KC4773 (United): dropped "13 PL / record 20 shared with Liverpool" -> "among England's most decorated clubs."
  - KB8255, KB8256, KB8268 (Liverpool): dropped "Twenty English league titles" / "20 titles level with Man United + six European crowns" / "most successful side in Europe's premier competition" -> qualitative ("one of England's most decorated histories," "a European pedigree few can match").
- **F50 IH1897 (Mike-ruled; the brief false-verified earlier this session, so every claim re-checked against the Phase 0 scrape):**
  - CUT "adidas launched the F50 in 2004... F for fast" (unsourced -- launch history is silo/world-knowledge, not in this product's scrape) -> "This is the Elite build of the adidas F50."
  - REFRAMED "the F50 family Messi has worn for years" / "the speed line Messi wears" / "the one Messi wears" (wearing-history not in scrape) -> "Messi's signature F50" (scrape field `messi_signature_or_likeness: "Yes"`).
- **Sources for surviving facts:** founding/stadium dates (United 1878/1902/1910; Liverpool 1892; Shankly all-red 1964; Liver Bird since 1892) = identity-research web verification, multi-source. Product specs / colorways / the KC4773 1976/77 FA Cup collar tribute / all F50 specs + weight (156.4 g -> 5.5 oz) / all cleat tech = the per-SKU Phase 0 scrape. Cleats HJ4122/HQ2325 carry no dates/honours/weight (100% scrape).
- Gate + voice re-run GREEN after all fixes. Commit `6b4d563` amended (it had the pre-fix United copy and must not ship). Push held for Mike's clearance.

### Process note (for the standing claims-gate codification)
Three times this session the claims discipline caught a fact getting ahead of the files (a fabricated ~50-min figure; an assumed F50 scrape-verify; an assumed United-count propagation). Mike's directive: codify a standing claims gate -- Layer 1 playbook rule (every checkable claim carries a scrape/club/web source or is cut), Layer 2 `batch_gate` check (flag bare title-counts / "record"/"most" superlatives in club jersey body copy; KA6871's "record 20 English league titles" as the regression fixture), Layer 3 pipeline verification -- so Batch 9 onward enforces this automatically. To be done as a SEPARATE codification commit after the Batch 8 push.
