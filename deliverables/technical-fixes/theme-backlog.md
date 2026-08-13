# Theme Backlog

_Theme-level items owned by Misha, surfaced by the SEO workforce. LOG ONLY. Nothing here is actioned, drafted, or proposed to Misha without Mike instructing it. This file is separate from `strategy/sprint-backlog.md` (SEO workstream tasks) and from `deliverables/tracking/technical-seo-log.md` (work that shipped, which requires a brief reference)._

Item IDs use the `T-THEME-NN` sequence.

## Open

### T-THEME-01: store suffix on PDP title tags consumes 12 characters

**Logged:** 2026-08-13, from the Batch 13 third correction pass (B-PACK-02 resolution).

**Owner:** Misha (theme repo `github.com/7Rock-Team/prosoccer`). Mike routes.

**Status:** LOGGED ONLY. Not actioned, not drafted, no change proposed.

**What.** The Hyper theme auto-appends the literal string `` ` – ProSoccer` `` (space, en-dash, space, store name; en-dash is U+2013, verified against the live rendered `<title>` 2026-07-31) to every title tag. That is 12 characters, which is why the written part of a PDP meta title is capped at 48 against Google's roughly 60-character truncation point. The suffix applies across roughly 15,000 PDPs.

**Why it is on the record.** That suffix is the direct cause of the B-PACK-02 conflict: at the fold-over tongue Predator Elite configs, no title could carry both the spelled-out configuration name and the pack qualifier under 48 characters, so the configuration had to abbreviate. Removing the suffix for product pages would return 12 characters on every PDP, which is the difference between `adidas Predator Elite FO FG Chaos vs Control` (44) and `adidas Predator Elite Fold-Over Tongue FG Chaos vs Control` (58, currently impossible).

**Why it is not a recommendation.** The suffix carries brand recognition in the SERP, and dropping it store-wide is a trade nobody has evaluated. It also touches every page type, not only PDPs. Any move here needs the brand-recognition tradeoff assessed first, and it is Misha's template to change, not the SEO workforce's.

**Related:** `strategy/sprint-backlog.md` B-PACK-02 (closed 2026-08-13); `context/page-type-playbooks/product-page-playbook.md` 'Meta Title and Meta Description compliance' (the 48-char rule) and 'Meta title precedence when the 48-character cap binds' (the rule the cap forced).
