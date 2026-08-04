# Silo Positioning: Mizuno Morelia

Per-SKU prose patterns for the Mizuno Morelia soccer cleat line. Created 2026-08-03 (Batch 12, FIRST Mizuno entry; brand-first, new brand lane). Keyed by boot MODEL like predator / copa / mercurial / tiempo / phantom / f50 / furon / tekela. Morelia = Mizuno's heritage kangaroo-leather touch boot: the craftsmanship / feel lane, distinct from the speed lanes (Mercurial / F50 / Furon) and the power lanes.

Format and append protocol: see `README.md`. ORIN reads this file during the pre-dispatch differentiation pass and appends per-SKU entries after the batch commits.

## Pre-dispatch reference / guardrails

### Brand and model head-term cede policy (added 2026-08-03, Batch 12)

Bare Mizuno brand and model head terms belong to their collection pages, not to any PDP. Recorded in `deliverables/tracking/ceded-terms.csv` and on each collection row's `ceded_from` in `deliverables/tracking/collections-master.csv`:

- `mizuno soccer cleats`, `mizuno cleats` to `/collections/mizuno-soccer-cleats` (live-verified 2026-08-03, H1 "Mizuno Soccer Cleats for Men, Women, & Youth", 9 products; the brand cleats collection).
- `mizuno morelia soccer cleats` (the model head term) is already the PRIMARY of `/collections/mizuno-morelia` (live), so no PDP takes it either. Treat it as collection-owned in the cannibalization check.
- `mizuno bright black soccer cleats` is the PRIMARY of the colorway collection `/collections/mizuno-bright-black-soccer-cleats` (registry row; confirm live before internal-linking, it postdates the 2026-05-08 sitemap snapshot).

PDPs take model + tier + surface + colorway qualified terms only (for example `mizuno morelia neo v beta elite fg`). Expect sub-floor.

### Brand-IP posture (Mizuno)

- Mizuno holds no FIFA license. FIFA / "World Cup" terminology is FORBIDDEN in every field, the same rule as Nike / New Balance / Kelme / Umbro (`context/brand-ip-constraints.md`). Moot on a boot page, but enforced; neutral cycle language only.
- Do NOT map Nike or adidas tier logic onto Mizuno. Verify the Morelia ladder from the live pages per SKU.

### Cross-lane motif scope (added 2026-08-04, Batch 12)

The Nike Shadow Pack barred-motif list (`gone`, `vanish`, `disappear`, `blackout`, `menace`, `shadowy`, `phantom of`, `illusion of`) is scoped to the **Nike Shadow cleat lane only, NOT global**. `blackout` appears in the 540394 Beta Elite body and is fine here: it is not on Mizuno's forbidden list, it is a different silo and a different colorway (Bright Black, not Shadow Pack), so there is no cross-lane convergence risk. Do not re-litigate a Mizuno motif against the Nike Shadow audits; each silo's barred list is its own.

### Tier ladder (VERIFIED live 2026-08-03, not assumed)

- `540394.9025` Morelia Neo V Beta ELITE FG: $219.99, the TOP tier of the pair. Mizuno Kangaroo Leather upper.
- `540396.9025` Morelia Neo V Beta PRO FG: $149.99, sits BELOW Elite. Mizuno Kangaroo Leather upper.
- Both: "Bright Black Pack (FA26)", internal color Black-Lava Orange, FG so the live title says "Cleats" (not "Shoes").
- The ladder direction (Elite above Pro) is confirmed by live price, not by porting Nike/adidas naming assumptions.
- **WATCH (colorway sibling, Batch 12 decision):** a **Morelia Neo V Beta Pro Prism White Pack (FA26)** is a live, separate product NOT optimized in Batch 12. 540396 (the Bright Black Pro) takes the bare tier term `mizuno morelia neo beta pro` (no colorway qualifier) per Mike's Batch 12 call, so the page is not left on a narrower term than it needs. When the Prism White Pro is optimized, both Pro colorways will contend for that bare tier term; colorway-qualify then, not now.

### Model positioning (PROPOSED, pending Mike approval at the Batch 12 gate)

- Morelia = HERITAGE TOUCH / CRAFTSMANSHIP. Frame on kangaroo-leather feel, barefoot touch, low-profile fit, comfort. Do NOT frame Morelia as a speed or power boot.
- Claims bar (PROPOSED): the K-leather touch signature is scrape-confirmed for both SKUs (Mizuno Kangaroo Leather upper) and may be stated. "Made in Japan" is a Mizuno flagship signature that does NOT automatically apply to the Beta tier: state it only if that specific SKU's Phase 0 scrape confirms it, otherwise cut it. No superlatives ("best leather boot," "finest touch in the game"). Comparisons to Mercurial / F50 only as market references, never as a superiority claim.

### Tier -> avatar (PROPOSED)

- Beta Elite ($219.99) -> Tyler / The Athlete primary (touch player, playmaker who buys on feel).
- Beta Pro ($149.99) -> Tyler / The Athlete, value entry into the K-leather feel; Jennifer / The Mom secondary (leather comfort for a growing player).

## Claimed patterns log

(Append one entry per SKU after the Batch 12 commit, per `README.md`. Empty until then.)
