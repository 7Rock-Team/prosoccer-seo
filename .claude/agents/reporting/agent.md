# Reporting Agent

**Purpose (one line):** Assemble the monthly client report from GA4, GSC, and internal deliverables, with no vanity metrics.

**Status:** Not yet built. Scheduled for **Phase 1.6** of the rollout. See `CLAUDE.md`.

## Planned Responsibilities

- Pull monthly metrics from `data/ga4-exports/` and `data/gsc-exports/`.
- Populate `reports/templates/monthly-report-template.md` into `reports/monthly/YYYY-MM.md`.
- Tie every metric to a goal in `context/06-business-goals.md`.
- Draft the executive summary for Mike to review and edit.
- Flag risks and blockers.

## Planned Tools

- Memory MCP (namespace: reporting)
- Google Drive MCP (deliver PDF export to client folder)
- File system

## Known Dependencies Before Build

- `context/06-business-goals.md` populated with agreed KPIs
- At least one month of GA4 and GSC exports available
- Report template finalized
