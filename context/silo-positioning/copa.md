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

### SKU KI0586 (Copa Pure IV Elite FG, senior exemplar)
- Brief: `deliverables/page-optimizations/2026-06-30_session-01/KI0586_..._brief.md` (commit 812b613, Batch 5 Wave 1 exemplar)
- Date: 2026-06-30
- Opening hook approach: the half-second after the ball arrives, the first touch that buys you time before the defender reads the move
- Primary metaphor: the tempo-running playmaker who reads the game a beat early (No.8 / No.10), touch over pace
- Use case scenario: senior playmaker dictating tempo on firm natural grass and well-kept pitches
- Angle of emphasis: premium Elite calfskin touch that makes your best touch repeatable; flagship tier
- Heritage angle: gen-IV return to the classic look (floating tongue + adiPure pinline), Fusionskin calfskin forefoot, Comfort Frame; evergreen, no current face

### SKU KI0625 (Copa Pure IV Pro FG)
- Brief: `deliverables/page-optimizations/2026-06-30_session-01/KI0625_..._brief.md` (commit a34c7d6)
- Date: 2026-06-30
- Opening hook approach: take the ball on the half-turn and it stops right where you wanted, the first touch that decides whether the move lives
- Primary metaphor: the decisive first-touch in tight space, close-quarters control
- Use case scenario: serious player on firm natural grass at Pro-tier value
- Angle of emphasis: most of the Elite's touch without flagship money; Fusionskin calfskin + Primeknit tongue (scrape override vs floating)
- Heritage angle: Copa touch lineage, adiPure pinline, gen-IV classic look

### SKU KI0630 (Copa Pure IV Pro Turf)
- Brief: `deliverables/page-optimizations/2026-06-30_session-01/KI0630_..._brief.md` (commit a34c7d6)
- Date: 2026-06-30
- Opening hook approach: weeknight five-a-side, tight pocket, a defender on your shoulder before the ball lands
- Primary metaphor: the small-sided game decided in tight turf spaces
- Use case scenario: Pro-tier turf and small-sided regular on artificial turf
- Angle of emphasis: Copa touch rebuilt for turf; Fusionfeel 2.0 synthetic + Touchprint grip + rubber turf outsole (NOT calfskin)
- Heritage angle: Copa heritage carried onto turf

### SKU KI0645 (Copa Pure IV League Turf)
- Brief: `deliverables/page-optimizations/2026-06-30_session-01/KI0645_..._brief.md` (commit a34c7d6)
- Date: 2026-06-30
- Opening hook approach: most of a young player's soccer happens on turf, and the ball has to behave
- Primary metaphor: entry-tier Copa feel made for the turf player
- Use case scenario: value / youth / rec player on artificial turf (Jennifer + Mike the Coach)
- Angle of emphasis: most of the Copa feel for less; synthetic Fusionfeel soft touch; rubber turf outsole; entry tier
- Heritage angle: Copa touch at the entry tier

### SKU KI0653 (Copa Pure IV League FG)
- Brief: `deliverables/page-optimizations/2026-06-30_session-01/KI0653_..._brief.md` (commit a34c7d6)
- Date: 2026-06-30
- Opening hook approach: most cleats make you earn the comfort with blisters first, this one plays soft from the box
- Primary metaphor: comfort-from-day-one, no break-in (gear a developing player forgets they are wearing)
- Use case scenario: developing / rec value player on firm natural grass (Jennifer)
- Angle of emphasis: most of the Copa feel and comfort at a friendlier price; synthetic Fusionfeel (NOT leather, explicit FAQ); Comfort Plate TPU; senior clean term vs junior KI0662
- Heritage angle: Copa touch lineage, the accessible League build
