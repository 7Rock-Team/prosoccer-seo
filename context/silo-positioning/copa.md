# Silo Positioning: adidas Copa

Per-SKU prose patterns claimed in shipped briefs for the adidas Copa silo (the touch-and-comfort line). Format and append protocol: see `README.md` in this directory. ORIN reads this file during the pre-dispatch differentiation pass and appends after each batch commits.

## Pre-dispatch reference / guardrails

Reference notes ORIN reads at the pre-dispatch differentiation pass. This section is NOT the append-only per-SKU log below; it carries forward guardrails for the silo, not shipped-pattern records.

### Copa Pure IV tech-accuracy (added 2026-06-29, from ORIN research for Batch 5 senior Copa)
- **Upper material is tier AND surface variable (refined 2026-06-30 from Batch 5 Wave 2 scrape-wins; the 6/29 "Elite/Pro = Fusionskin" note oversimplified). Never "kangaroo" or "K-leather" anywhere.** Verified matrix: **FG Elite + FG Pro = Fusionskin** (calfskin-leather forefoot stitched to a synthetic mesh midfoot; "calfskin leather touch" accurate). **Pro TURF = Fusionfeel 2.0 (synthetic), NOT calfskin.** **League, both FG and Turf = Fusionfeel (synthetic): never call League "leather."** So calfskin/leather framing is FG-Elite/FG-Pro ONLY; every turf SKU and every League SKU is synthetic. Always verify the specific SKU's upper from its Phase 0 scrape (adidas marketing copy is internally inconsistent, e.g. a turf PDP labeled "Fusionfeel 2.0 leather upper" -- scrape-wins, treat as synthetic). The K-leather heritage belongs to Copa Mundial / Copa Gloro, NOT Copa Pure.
- **Plate / outsole is tier AND surface variable (refined 2026-06-30). "Sprintframe" is FORBIDDEN (never appears on Copa Pure).** Verified: **FG Elite = "Comfort Frame"; FG League = "Comfort Plate (TPU)"; Turf SKUs = rubber turf outsole (no frame/plate name, no stud count).** Confirm the exact plate name from each SKU's scrape; do not assume one name across the line.
- **Tongue is tier variable (refined 2026-06-30):** Elite = low floating tongue (the gen-IV U-throat return); Pro FG scrape showed a **Primeknit tongue**. Confirm per SKU; do not assume floating tongue across the line.
- Gen IV vs Pure III change: classic U-throat with a floating tongue (vs the Pure III Primeknit tongue); adiPure pinline (heel-to-toe) retained; Ortholite sockliner and soleplate carried over.
- Turf (TF) variants (Pro Turf, League Turf): rubber turf outsole for artificial turf; do not claim a specific stud count.
- **Positioning lane (already canonical in the log below):** Copa = TOUCH / clean first touch / comfort. Distinct from Predator (control/strike) and F50 (speed). Safe Copa framing: "touch / clean first touch / calfskin-soft feel (Elite/Pro only)."
- **Signature face: do NOT assert a current signature face.** Declan Rice is the current Copa face (TIME-SENSITIVE); prefer evergreen / no-face framing. NOTE: the KI0662 log entry below records "Bernardo Silva" as a historical Copa association at that brief's write time; that entry stays as historical record and is NOT a forward directive for this batch.
- Pack-secondary keyword "adidas copa pure road to glory" is JUSTIFIED: Copa Pure IV is confirmed in the adidas Road to Glory pack (Solar Turbo / Ivory / Core Black colorway; Phase 0 scrape-verified 2026-06-30 on KI0586, supersedes the earlier research "Solar Red" note).

## Claimed patterns log

### SKU KI0662
- Brief: `deliverables/page-optimizations/2026-06-03_session-01/adidas-junior-copa-pure-iv-league-fg-road-to-glory_brief.md` (commit 68664ca)
- Date: 2026-06-03
- Opening hook approach: parent-milestone emotion, the child's first real cleats framed as a reward to earn rather than a guess to gamble on
- Primary metaphor: adidas builds in three lanes (speed in the F50, control in the Predator, touch in the Copa); the Copa is the touch lane
- Use case scenario: a parent (the Jennifer avatar) buying for a developing or rec youth player on firm ground, Saturday league and school matches, growing feet
- Angle of emphasis: the League value tier as most of the pro Copa feel at a price that fits a still-growing foot, comfort and clean first touch over speed
- Heritage angle: the Copa Pure IV return to the classic look (low floating tongue plus the adiPure pinline heel to toe), the Copa touch worn across the line by players like Bernardo Silva and Sam Coffey, sized down for younger feet
