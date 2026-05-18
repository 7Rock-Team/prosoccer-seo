# Workforce Conventions

This file documents cross-agent operational conventions for the ProSoccer SEO workforce. Conventions here apply to all agents (ORIN, KIRA, VERITAS, SCRIBE, SAGE if built, RECON, METRIK) and are read at startup alongside `context/00-business-overview.md`, `context/03-brand-voice.md`, `context/04-customer-avatars.md`, and `context/brand-ip-constraints.md`.

When a convention in this file conflicts with an agent-specific rule in `.claude/agents/<agent-name>/agent.md`, the convention here is the default; the agent-specific rule overrides only when it is explicit about doing so.

## Page optimization deliverable folder structure

All page-optimization deliverables produced during a session (whitelabel audits, per-page briefs, regenerated briefs, comparison docs) land in a date-stamped session folder under `deliverables/page-optimizations/`. The structure is:

```
deliverables/page-optimizations/
  whitelabel-audit/
    YYYY-MM-DD_session-NN/
      <slug>_audit-and-regen.md
      <slug-2>_audit-and-regen.md
      ...
  YYYY-MM-DD_session-NN/
    <slug>_brief.md
    ...
```

### Naming convention

- **Folder name pattern:** `YYYY-MM-DD_session-NN/` where YYYY-MM-DD is the session start date and NN is a zero-padded two-digit session ordinal within the work-unit (e.g., `01`, `02`, `03`).
- **Work-unit boundary:** a "session" is a single ORIN-orchestrated work unit (Mike's prompt to the agent, the agent's execution, and the GATE review or completion). Multi-session work units (e.g., a 3-collection whitelabel audit pilot) get a session folder per session.
- **Examples:**
  - `deliverables/page-optimizations/whitelabel-audit/2026-05-16_session-01/` (whitelabel audit pilot, session 1)
  - `deliverables/page-optimizations/whitelabel-audit/2026-05-17_session-02/` (whitelabel audit pilot, session 2)
  - `deliverables/page-optimizations/2026-06-01_session-01/` (a non-whitelabel batch of per-page briefs)

### Session folder creation

The session folder is created at session start if it does not already exist. ORIN creates the folder via the orchestrator's first file write of the session. Specialist agents (SCRIBE, KIRA, etc.) write into the session folder ORIN has established.

### Workforce-internal briefings

Per-page workforce-internal briefings (SCRIBE classification reasoning, KIRA keyword research notes, etc.) continue to live in agent-specific briefings folders: `.claude/agents/<agent-name>/briefings/YYYY-MM-DD_<slug>.md`. These are agent-internal and not part of the page-optimization deliverable folder.

### Historical / pre-convention files

Existing flat-directory deliverables (e.g., `deliverables/page-optimizations/2026-05-08_mexico-v3.md`) stay where they are. Do NOT retroactively move historical files into session folders. The convention applies going forward; the audit trail of the convention transition is the git history.

## Cleanup and retention policy

Page-optimization deliverables are operational artifacts with a finite useful life. The audit trail of who-decided-what lives in commit messages and PR descriptions; the deliverable file itself becomes stale once the recommendation has been implemented and either succeeded or been superseded.

### Retention window

- **Active retention:** 6 to 12 months from session date. The exact window depends on the deliverable type (whitelabel audits clear faster than evergreen brief work) and is decided at quarterly cleanup time, not pre-fixed per file.
- **Long-tail exception:** any deliverable that remains the source-of-truth for a live page's copy stays in the repo indefinitely. The Mexico v3 brief, for example, governs the Mexico page's copy until a v4 supersedes it; v3 stays in the repo until v4 lands.

### Quarterly cleanup pass

Once per quarter, ORIN (or Mike directly) runs a cleanup pass:

1. Enumerate all session folders under `deliverables/page-optimizations/` and `deliverables/page-optimizations/whitelabel-audit/`.
2. For each folder older than 6 months from today: review the contents to confirm the deliverables have been implemented, superseded, or are no longer load-bearing.
3. Folders meeting the retention threshold and review criteria are removed in a dedicated cleanup commit.
4. The cleanup commit message lists every removed folder and the disposition (implemented / superseded / abandoned). This preserves the audit trail even after the file is gone.

### Cleanup commit structure

The cleanup commit is its own commit, not bundled with other work. Commit message format:

```
Quarterly cleanup YYYY-Q[N]: removed N page-optimization session folders past retention window

Folders removed (with disposition):
- deliverables/page-optimizations/YYYY-MM-DD_session-NN/ — implemented YYYY-MM-DD via Shopify admin
- deliverables/page-optimizations/whitelabel-audit/YYYY-MM-DD_session-NN/ — superseded by [reference]
- ...
```

The disposition note is the audit trail of why each folder was safely removable.

### Cleanup does NOT apply to

- Agent-specific briefings under `.claude/agents/<agent-name>/briefings/`. Those are agent-internal context that future sessions read; retention is per-agent and managed in the agent's own learnings.md compaction protocol.
- The `templates/` directory.
- Any deliverable file in `deliverables/technical-fixes/`, `deliverables/keyword-research/`, `deliverables/phase-2-discovery/`, or other non-page-optimization deliverable folders. Those have their own retention conventions to be documented separately as they emerge.

## Cross-references

- `context/brand-ip-constraints.md` documents the FIFA terminology constraint that applies to all page-optimization deliverables produced under this folder structure.
- `.claude/agents/on-page-seo/agent.md` Section 13 ("Output Templates") references this convention for per-page brief file placement.
- `templates/consolidated-page-brief-template.md` template-level file-path guidance may lag this convention until next template refresh; current canonical file-path convention is here.
