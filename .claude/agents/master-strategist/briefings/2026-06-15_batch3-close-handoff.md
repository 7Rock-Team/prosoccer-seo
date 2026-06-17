# Session-close handoff -- Batch 3 (2026-06-15)

Batch 3 (10 adidas Road to Glory PDP briefs, 5 F50 + 5 Predator) shipped and pushed to origin/main: commit `c1c5ca7` (briefs + audit trail + silo updates), commit `49e5959` (tier-appropriate word-count codification). Full per-SKU detail in `deliverables/page-optimizations/2026-06-15_session-01/_audit-trail.md`.

**Codification session 2026-06-17 closed (commit `e6bdec9`):** Updates 7 (Product Details H2 = "Product Details: [Short Name]"), 8 (internal-link placement varies by contextual fit, not fixed H2 position; pairwise flags identical positions), 9 (split H2 casing: editorial body H2s sentence case, structural H2s Title Case). Diagnostic confirmed no Update 10 gap (primary-keyword-in-Meta-Title/Description already codified). voice_check.py casing detection deliberately DEFERRED (false-positive risk on brand tokens); revisit only if casing violations recur as a Gate 15 issue across 3+ consecutive batches. All forward-only from Batch 4.

## Standing follow-ups for next session opening

### RESOLVED 2026-06-17 (MCP architecture + gating)
- **MCP sub-agent access -- FIXED + verified, all 5 agents.** Root cause was NOT OAuth propagation; it was the `tools:` allowlist. Commit `0c6dbb3` (2026-05-26) moved MCP tokens out of `tools:` into `mcpServers:` on a wrong premise, with a same-commit verification that covered the pre-refactor config (tested config != shipped config). Restored `mcp__<server>__*` wildcards to each agent's `tools:` (KIRA `be7ee36`; SCRIBE/VERITAS/RECON/ORIN `70adb8e`). Phase-C verified live: firecrawl / gsc / dfs / tavily all callable at sub-agent level. Architectural record corrected (`f7fe8bb`) and a verification-discipline convention added (verified claims need method + output excerpt + artifact).
- **SCRIBE self-gating -- FIXED (Fix 2, commit `7eddda1`).** Codified draft-write vs commit-stage gating across all 4 sub-agents: draft writes to `deliverables/` are auto-approved; self-gate only on commit-stage shared-state actions (silo / conventions / audit-trail / git). Eliminates the dispatch-prompt boilerplate.

### HIGH PRIORITY remaining
- **Fix 3: token-efficiency audit -- DEFERRED to post-Batch-4.** Baseline must come from sub-agents doing their own MCP work (now enabled), not the Batch 2-3 parent-level-workaround data. Run after Batch 4 dispatches under the corrected architecture.

### Batch 4 dispatch-pattern change (consequence of the MCP fix)
Sub-agents now call MCP directly, so ORIN no longer pre-runs Phase 0/1/4 at the parent level and injects data. KIRA runs its own GSC + DataForSEO Phase 1; SCRIBE runs its own Phase 0 Firecrawl scrape; VERITAS / RECON run their own scans. ORIN dispatches the task + lane spec, not pre-fetched MCP payloads. (Drive stays parent-read by design: ORIN reads the white-label sheet and injects rows; KIRA / SCRIBE do not need Drive.) Apply this shift when Batch 4 dispatches; it also reshapes what the Fix 3 audit will measure.

### OBSERVATIONS to watch in Batch 4
- **Fabrication mode.** Observed twice in Batch 3 (fabricated KD scores on HP9973; invented "Pasadena fitting room" retail detail on KK1307), both caught at the ORIN gate. If either recurs, codify the SCRIBE Phase 4 self-check: "No fabricated specifics: KD blank if not retrieved; no store / retail / policy details unless in source data."
- **Tier-appropriate writing under the new codification** (commit `49e5959`, active Batch 4 onward). Watch that lower-tier SKUs land in band (Elite 400-450 / Pro 340-390 / League-Club 280-340) rather than at the 465 ceiling.
- **H2 casing compliance under the split discipline** (commit `e6bdec9`, active Batch 4 onward). Watch that editorial body H2s come back in sentence case and structural H2s (FAQs about / Product Details: / Care and Maintenance) in Title Case. If casing violations recur as a Gate 15 issue across 3+ consecutive batches, revisit the deferred voice_check.py casing enhancement.

### CODIFICATIONS pending
- Jersey playbook (fit-tier / home-away / club-vs-national taxonomy)
- Mizuno silo
- Kelme FIFA research
- Reserved-opener blocklist
- Full-body word-count rule made explicit
- Worked-example refresh

### PRODUCTION
- Mike's 20-PDP Shopify implementation queue
- Batch 2 + Batch 3 keyword-sheet entries (white-label PDPs tab, manual entry by Mike; Batch 3 list in the Batch 3 `_audit-trail.md`)
