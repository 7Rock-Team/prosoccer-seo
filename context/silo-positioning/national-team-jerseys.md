# Silo Positioning: National Team Jerseys

Per-SKU prose patterns claimed in shipped briefs for national-team jersey PDPs. Unlike the cleat silos (named by base model line), this silo is keyed by **product class**, not brand: jerseys collide on the shared fan / matchday / national-pride / tournament-cycle prose lane regardless of kit supplier, and each nation is single-brand per cycle (Croatia = Nike, Mexico = adidas, and so on), so a brand-keyed file would scatter unrelated nations. Product-class taxonomy is also durable against kit-supplier changes between cycles. Taxonomy confirmed by Mike 2026-06-10. Format and append protocol: see `README.md`. ORIN reads this file during the pre-dispatch differentiation pass and appends after each batch commits.

Note: club-team jerseys (Real Madrid, Barcelona, etc.) sit in a distinct prose lane (club identity vs national pride) and will get their own silo file (`club-team-jerseys.md`) when that work first batches.

## Claimed patterns log

### SKU J000693-CRFT (Nike Croatia Men's Stadium Away 2026)
- Brief: `deliverables/page-optimizations/2026-06-10_session-01/nike-2026-croatia-mens-stadium-away-soccer-jersey_brief.md` (Batch 2, first jersey under the new architecture)
- Date: 2026-06-10
- Opening hook approach: the fan / matchday identity moment, pulling on the deep blue away shirt and being "Croatian for the summer"
- Primary metaphor: belonging / national identity (the anthem-moment supporter feeling); deliberately NO athletic-performance metaphor
- Use case scenario: the Croatia supporter buying the replica away shirt to wear through the summer tournament cycle (watch party, bar, stadium, casual)
- Angle of emphasis: national pride plus the Stadium (replica) tier and the distinct away colorway
- Heritage angle: Croatia's red-and-white checkerboard (sahovnica) rendered in deep royal blue; Nike as Croatia's 2026 (and final) kit supplier before adidas takes over
