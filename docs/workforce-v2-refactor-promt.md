WORKFORCE REFACTOR — SPEED + TOKEN OPTIMIZATION (v2 architecture)

GOAL: Cut a 10-PDP batch from 4-6 hours / 3-4M tokens down to under 
90 min wall-clock / ~1-1.5M tokens / 1-2 human stop-points — WITHOUT 
losing quality. Every defect class the current gates catch (casing, 
headings, FIFA-terms, fabrication, cannibalization, convergence) must 
still be caught, just moved from human-in-the-loop to deterministic 
script + exception-only escalation.

READ FIRST before changing anything:
- .claude/agents/ (ORIN, KIRA, SCRIBE agent specs)
- context/workforce-conventions.md
- context/silo-positioning/README.md and all silo files
- scripts/voice_check.py and scripts/test_voice_check.py
- scripts/test-firecrawl.ps1
- The most recent batch audit-trail and follow-ups.md
- Surface a written understanding of the current pipeline stages + 
  where the time/token costs concentrate BEFORE proposing the refactor 
  implementation. Hold for my confirmation that your understanding is 
  correct, THEN build.

=== CHANGE 1: ESCALATE-ON-EXCEPTION (replace APPROVE-EVERY-ACTION) ===

Current: ORIN holds for Mike approval at Checkpoint 1 (keywords), 
Checkpoint 2 (exemplar plan), Checkpoint 2b (exemplar review), 
Checkpoint 3 (final review), plus every "surface decision" hold.

New: ORIN runs the batch autonomously end-to-end. It STOPS for Mike 
ONLY on genuine exceptions it cannot resolve from codified rules:
- A true architectural first with NO silo precedent (new brand 
  licensing status, new product-class requiring a new silo, new 
  competition-IP question)
- A fabrication trap it cannot resolve from Phase 0 scrape (scrape 
  contradicts itself, or required spec is absent AND load-bearing)
- A cannibalization collision with no clean resolution under codified 
  discipline
- A cross-brief convergence the dedup script flags that ORIN cannot 
  auto-resolve

Everything else — keyword selection within codified floors + GSC 
override rules, exemplar selection, differentiation lanes, gate-caught 
MECHANICAL fixes (casing, headings, word-count, table dupes, motif 
re-voices) — ORIN DECIDES, APPLIES, and LOGS. Does not ask.

ORIN produces ONE end-of-batch report for Mike containing:
- All decisions it made autonomously (keyword table, exemplar choices, 
  differentiation lanes) with one-line rationale each
- All gate-caught defects it auto-fixed
- Any exceptions it escalated (should be rare)
- The Registry 1 handoff block (for Mike's manual sheet entry)
- Commit hashes
- Publish-priority notes (sold-out SKUs, etc.)

Mike reviews the ONE report, not every checkpoint. Codify the 
exception criteria explicitly in workforce-conventions.md so ORIN has 
a deterministic "is this an exception?" test.

=== CHANGE 2: COLLAPSE WAVES (parallel dispatch default) ===

Current: Wave 1 (exemplars) → ORIN gate → Wave 2 (siblings), 
sequential.

New: For any SKU whose silo already has established patterns, dispatch 
ALL SCRIBEs in parallel in a single wave. The pre-dispatch 
differentiation spec (which ORIN already writes) IS the skeleton — 
SCRIBEs pull their lane from the spec + their silo's existing patterns. 
No live exemplar extraction needed.

KEEP a small exemplar-first wave ONLY when a genuinely new lane exists 
with zero precedent (e.g., first-ever club team, first-ever brand with 
new licensing). In that case: 1 exemplar for the new lane runs first, 
gets gated, its skeleton feeds only the siblings in that same new lane. 
All OTHER SKUs (established silos) still parallelize immediately 
alongside it — they do not wait.

Decision logic ORIN uses: "Does this SKU's silo have >=1 shipped entry 
with an established lane? Yes -> parallel now. No -> exemplar-first for 
that lane only."

=== CHANGE 3: SCRIBE TOKEN DIET (pre-loaded inputs, tool cap) ===

Current: each SCRIBE independently scrapes its PDP, reads silos, looks 
up keywords, validates links — 40+ tool uses, ~270-300k tokens each.

New, three parts:

3a. BATCHED PRE-SCRAPE. Add an ORIN pre-dispatch step that Firecrawl-
scrapes ALL batch URLs once, writes each SKU's scrape data 
(specs, colorway, price, materials, existing copy) into a per-SKU 
input file at deliverables/<session>/inputs/<SKU>_input.md. SCRIBE 
READS this file instead of making live Firecrawl calls. One scrape 
per URL for the whole batch, not one scrape per SCRIBE.

3b. PRE-RESOLVED KEYWORDS + LINKS. KIRA's keyword table + ORIN's 
validated internal links get written into the same per-SKU input file. 
SCRIBE receives validated keywords and validated links as INPUTS. It 
does not re-derive or re-validate them.

3c. SCRIBE TOOL CAP. With inputs pre-loaded, SCRIBE's job is: read its 
input file, read its silo lane + differentiation spec, write the brief, 
run self-check, write the brief file. Target <=10 tool uses. Update the 
SCRIBE agent spec to reflect the leaner input-driven flow. Remove the 
instruction for SCRIBE to independently scrape / keyword-lookup / 
link-validate (ORIN now owns those upstream).

Per-SKU input file schema (ORIN writes, SCRIBE reads):
- SKU, URL, handle
- Phase 0 scrape data (specs, colorway, materials, price, existing 
  copy, sibling colorways)
- Primary keyword + secondaries + pack-secondary (from KIRA)
- Validated internal links (from ORIN link-check)
- Differentiation lane + facet (from ORIN diff spec)
- Forbidden-phrasings (verbatim + motifs + title-frames, from Change 5)
- Tier + word band (SKU-specific, NOT inherited from exemplar)
- Brand-IP posture (FIFA-permitted vs cycle-language-only)

=== CHANGE 4: DETERMINISTIC GATE SCRIPT (replace ORIN reasoning-gate) ===

Current: ORIN reads every brief and reasons about every compliance 
dimension.

New: Build scripts/batch_gate.py that runs ALL mechanical checks in one 
pass over a session's brief files and outputs a pass/fail report with 
specific line numbers for failures. ORIN reads only the FAILURES and 
reasons only about genuine judgment calls.

batch_gate.py checks (extend existing voice_check.py, don't duplicate):
1. Casing: body H2 first-word capitalization at any heading level 
   (existing voice_check logic, adidas excepted)
2. Heading levels: body H2 must be ##, FAQ must be ###, FLAG any 
   #### or ##### (the KI0586/IF8512 defect)
3. Em-dash: flag any — anywhere (existing)
4. adidas-caps, forbidden words (existing)
5. FIFA/WC term grep: on any non-adidas SKU (brand from input file), 
   flag "FIFA", "World Cup", "World Cup 2026" unless it's the codified 
   permitted historical anchor pattern. Allow adidas SKUs.
6. Forbidden-phrasing grep: verbatim strings + MOTIFS + TITLE-FRAMES 
   (per Change 5) from the SKU's forbidden list in its input file
7. Cross-brief pairwise similarity: within a batch, detect shared 
   motif words, shared H2 title frames, near-identical openings/
   closings across sibling briefs (the Shadow "gone" convergence 
   class). Output the overlapping SKU pairs + the shared element.
8. Word-count band: per SKU tier (from input file), flag over/under
9. Cannibalization: grep each brief's primary against Registry 1 
   existing primaries + intra-batch primaries, flag duplicates
10. Price-in-body: flag any $ or explicit price in body copy 
    (evergreen discipline)
11. Fabrication-hedge markers: flag "approximately", "around", "about" 
    near specs (weight/dimensions) as possible fabrication-hedges 
    to review against scrape

Output: a single report, PASS or a list of FAILURES with SKU + line + 
which check. ORIN acts on failures only. Add regression tests in 
scripts/test_batch_gate.py built from real past defects (KK3725 casing, 
KI0586 headings, DR Congo FIFA-in-body, Shadow "gone" motif, IF8512 
weight-hedge) so the script provably catches every historical defect 
class.

=== CHANGE 5: CODIFICATION FEED (forbidden-phrasings scope expansion) ===

Current: Mechanism B forbidden-phrasings carries verbatim H2 titles 
only. Motifs and title-frames re-emerge across independent SCRIBEs 
(the Shadow "gone" convergence).

New: Expand forbidden-phrasings extraction to three tiers, written into 
each sibling's input file and checked by batch_gate.py:
- Verbatim strings (existing): exact hooks, H2 titles, closing lines
- Motifs (new): recurring payoff/register words from the exemplar 
  (e.g., "gone", "invisible", "elusive") — siblings must not reuse
- Title-frames (new): the structural template of exemplar H2s 
  (e.g., "The [noun] [nobody] sees coming") — siblings must not 
  mirror the frame with swapped nouns

ORIN extracts all three tiers when building the differentiation spec. 
batch_gate.py check #6 + #7 enforce them. This stops the workforce 
re-litigating the same convergence class every batch.

Also codify: Mechanism A skeleton handoff must carry the SKU's OWN 
tier-band, never inherit the exemplar's (the IF8512 Elite-band-on-a-
Pro-SKU defect).

=== CHANGE 6: PERMISSION ALLOWLIST (kill the "yes, yes, yes") ===

Create/update .claude/settings.json with a permissions allowlist so 
routine commands auto-approve while genuinely dangerous ones still 
prompt:

{
  "permissions": {
    "allow": [
      "Bash(git add*)", "Bash(git commit*)", "Bash(git push*)",
      "Bash(git status*)", "Bash(git diff*)", "Bash(git log*)",
      "Bash(git show*)", "Bash(git stash*)",
      "Bash(node*)", "Bash(python*)", "Bash(python3*)",
      "Bash(npx*)", "Bash(npm run*)",
      "Bash(cat*)", "Bash(ls*)", "Bash(grep*)", "Bash(rg*)",
      "Bash(cd*)", "Bash(echo*)", "Bash(head*)", "Bash(tail*)",
      "Bash(wc*)", "Bash(find*)",
      "Read(*)", "Write(*)", "Edit(*)",
      "mcp__firecrawl*", "mcp__tavily*", "mcp__dfs*", "mcp__gsc*"
    ],
    "deny": [
      "Bash(rm -rf*)", "Bash(git reset --hard*)", 
      "Bash(git push --force*)", "Bash(curl*)", "Bash(wget*)"
    ]
  }
}

This auto-approves the workforce's routine operations (git, node, 
python, file ops, the 4 MCPs) while still prompting or blocking 
destructive commands. Adjust the deny list if any of those are 
actually needed, but keep force-push and rm-rf gated.

=== BUILD SEQUENCE ===

1. Read the current architecture (listed at top). Surface your 
   understanding + where time/tokens concentrate. HOLD for my 
   confirmation.
2. Build Change 6 first (permission allowlist) — smallest, immediate 
   quality-of-life win, test it works.
3. Build Change 4 (batch_gate.py + regression tests from historical 
   defects). Verify it catches every past defect class. This is the 
   safety net that makes cutting human gates safe — build and prove 
   it BEFORE cutting gates.
4. Build Change 3 (SCRIBE token diet: pre-scrape step, input-file 
   schema, SCRIBE spec update, tool cap).
5. Build Change 5 (forbidden-phrasings 3-tier expansion, tier-band 
   handoff fix).
6. Build Change 2 (collapse waves, parallel-default dispatch logic).
7. Build Change 1 (escalate-on-exception, end-of-batch report format, 
   exception criteria in workforce-conventions.md). Build this LAST 
   because it depends on the deterministic gate (Change 4) existing 
   to safely replace human gates.
8. Update workforce-conventions.md + all agent specs to reflect v2.
9. Commit each change as its own coherent commit; surface hashes.
10. Write a v2 pipeline doc: the new flow end-to-end, so I can see 
    what a batch looks like under v2.

QUALITY BAR (non-negotiable): every defect class caught by the current 
human gates must be caught by batch_gate.py or the escalation criteria. 
The regression tests in step 3 are the proof. If a historical defect 
class can't be caught deterministically, that specific class KEEPS a 
human touchpoint — don't silently drop it.

Do NOT run a live batch during the refactor. Build + test against 
existing shipped briefs as fixtures. First live v2 batch is Batch 7, 
after I review the v2 pipeline doc.

APPROVE-EVERY-ACTION is suspended FOR THIS REFACTOR BUILD ONLY (so you 
don't stop at every step) EXCEPT: hold at step 1 (understanding 
confirmation) and after step 10 (v2 pipeline doc review). Two 
stop-points for the whole build.