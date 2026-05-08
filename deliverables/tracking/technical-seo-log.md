# Technical SEO Log

_Maintained by ORIN. Timestamped Markdown entries for technical SEO work that doesn't fit a per-URL grid in `collections-master.csv` or `products-master.csv`. URL consolidations, redirect maps, schema rollouts at template level, sitemap submissions, robots.txt edits, Core Web Vitals fixes, hreflang setup, disavow file submissions, theme template changes, and app conflict resolutions all land here._

## Why this file exists

Per-URL technical work (a single page's schema injection, a single page's title-rendering fix) belongs in a consolidated brief and tracks via the master CSVs. Site-wide or template-level technical work doesn't fit that grid. Disavow submissions, sitemap rollouts, theme template changes, and URL consolidation maps all touch many URLs at once. This log captures that work in a chronological, readable format that ORIN can summarize for METRIK (when built) and Mike can reference during weekly reviews.

## Format

Every entry uses this template:

```
### YYYY-MM-DD HH:MM - <Headline> (Severity: Critical / High / Medium / Low)

**Work type:** [URL consolidation / redirect map / schema rollout / sitemap change / robots.txt edit / Core Web Vitals fix / hreflang setup / disavow file / theme template change / app conflict resolution]

**Affected surfaces:** [URLs, templates, files; comma-separated or bulleted if many]

**Implementer:** [Misal / Misha / Jorge / Mike]

**Brief reference:** [path to VERITAS brief if standalone, OR consolidated brief path if part of per-page work]

**Validation status:** [Draft / Shipped pending validation / Validated YYYY-MM-DD]

**Outcome:** [One paragraph. Anchored to data citations. What changed, why, current state. Plain-language for Mike's read; technical detail in the brief reference.]

**Open follow-ups:** [items that need ongoing monitoring or future revisit; cross-reference work-log/follow-ups.md when applicable]
```

## Format rules

- **Newest entries at the top** of the Entries section below. Reverse-chronological reads better than chronological for "what's recent."
- **Severity matches VERITAS Section 4 labels.** Critical means revenue-blocking, equity-eroding, or actively losing rankings. High means material lift opportunity inside the current sprint. Medium means routine technical hygiene. Low means nice-to-have.
- **Voice check passes** on every entry before commit. Run `scripts/voice_check.py deliverables/tracking/technical-seo-log.md` after appending.
- **Brief reference is mandatory.** Every entry points to the VERITAS standalone brief or the consolidated brief that authorized the work. Entries without a brief reference are protocol violations; either the work shouldn't have shipped, or a brief is missing and needs to be backfilled.
- **Validation status updates in place.** When work moves from "Shipped pending validation" to "Validated YYYY-MM-DD," edit the entry rather than appending a new one. Validation date and method belong inline in the original entry.
- **Outcome is plain-language for Mike.** Technical detail belongs in the brief reference. Mike reads the log entry to understand what happened; he reads the brief when he wants the implementation specifics.

## Entries

_No entries yet. ORIN appends the first entry when the first technical fix ships._
