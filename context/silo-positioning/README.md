# Silo-Positioning Registry

This directory is **Registry 2** of the workforce's dual-registry architecture for cross-batch coordination. It is the internal, version-controlled, workforce-owned half. Registry 1 is the external white-label keyword sheet (Google Sheets, source of truth for keyword status); see `context/workforce-conventions.md` 'Dual Registry Architecture for Cross-Batch Coordination' for the full picture.

## Purpose

A SCRIBE instance drafting a brief is unaware of sibling dispatches in its own batch (ORIN handles intra-batch differentiation via the pre-dispatch lane spec). It is also unaware of every brief shipped in **prior** batches for the same product silo. Without a persistent record, SCRIBE can reuse an opening hook, a primary metaphor, or a use-case scenario that already shipped weeks ago in the same silo. These files are that persistent record: per-silo memory of the prose patterns already claimed, so each new batch differentiates against past work, not just against its current-batch siblings.

ORIN reads the relevant silo file during the pre-dispatch differentiation pass (Step 2 of the six-step protocol) and appends new entries after a batch commits (Step 6).

## Structure

One file per product silo, named by the silo's base model line:

- `phantom.md`: Nike Phantom
- `mercurial.md`: Nike Mercurial (Superfly and Vapor share the Mercurial speed silo)
- `tiempo.md`: Nike Tiempo
- `copa.md`: adidas Copa
- `predator.md`: adidas Predator
- `f50.md`: adidas F50

Add a new silo file as that silo first sees batch work (for example `puma-future.md`, `puma-king`, `nike-premier.md`, `new-balance-tekela.md`). Keep the filename to the base model line, lowercase, kebab-case.

## Per-SKU entry format

Keep entries terse and machine-readable. One entry per shipped SKU, appended under the silo file's log:

```
### SKU [code]
- Brief: [filename or commit hash]
- Date: [YYYY-MM-DD]
- Opening hook approach: [one line]
- Primary metaphor: [one line]
- Use case scenario: [one line]
- Angle of emphasis: [one line]
- Heritage angle: [one line]
```

## Append protocol (who writes, when)

- **Owner:** ORIN (the Master Strategist orchestrator). SCRIBE does not read or write these files directly; the silo registry is an orchestrator-level concern, and SCRIBE works only from the differentiation lane spec ORIN hands it at dispatch.
- **When:** ORIN appends entries **after** Mike approves a batch and it commits, never before. Proposed patterns can change at gate review, so the registry records only shipped, validated prose patterns.
- **What:** one entry per SKU in the committed batch, summarizing the five prose-pattern dimensions that SKU claimed (opening hook, primary metaphor, use-case scenario, angle of emphasis, heritage angle).
- **Append-only:** entries are not edited or deleted once written. A shipped pattern is a historical fact; if a brief is later re-run, the re-run adds a new entry (it does not overwrite the old one), and the entry's Brief field (filename or commit hash) disambiguates.

## Relationship to the other registry

Registry 1 (white-label keyword sheet) tracks **keyword** status and assignments and is the external source of truth maintained by Mike's white-label team. Registry 2 (these files) tracks **prose patterns** and is workforce-internal. Both feed ORIN's pre-dispatch differentiation pass; neither replaces the other. Keyword cannibalization is checked against Registry 1; prose-pattern collision is checked against Registry 2.
