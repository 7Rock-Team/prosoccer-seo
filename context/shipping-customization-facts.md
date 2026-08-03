# Shipping and Customization Facts

**Authoritative. Source: the ProSoccer shipping-delivery page.** Every agent (ORIN) and every on-page SCRIBE reads this on each run before writing or reviewing any brief. These are customer-facing facts: state them exactly, never round, never invent. Two of them have shipped wrong before (see the failure pattern in `SEO_BATCH_PROCESS.md` §7 and the gate check `check_customization_claims` in `scripts/batch_gate.py`).

## Processing tiers (business days: state these, never round to weeks, never invent)

- Standard orders: 1-2 business days
- Customized name/number: 2-3 business days
- Personalized jerseys: 5-10 business days
- Team/club orders: up to 4 weeks

## Copy rules

1. Name/number customization adds processing time in BUSINESS DAYS (2-3 total, about one extra day), NOT weeks. Never write that it adds "1-2 weeks" or "extra weeks."
2. Name/number customization is selected ON THE PRODUCT PAGE, NOT at checkout. Point the customer to the option on the product page.
3. Keep the tiers distinct: a name/number add is "Customized name/number" (2-3 business days); a fully personalized jersey is a separate, longer tier (5-10 business days). Do not conflate them.

CORRECT: "Add your name and number right on this page. Name and number orders ship in about 2 to 3 business days."

INCORRECT: "Customize at checkout. Personalized jerseys take an extra 1 to 2 weeks."

## Enforcement (defense-in-depth)

- SCRIBE writes from these facts at draft time; ORIN re-checks at the orchestrator layer.
- `scripts/batch_gate.py` `check_customization_claims` FAILS any brief whose body, short description, or FAQ (a) pairs customization language with "checkout", or (b) describes name/number customization in weeks rather than business days. The team/club "up to 4 weeks" tier is the only place "weeks" is correct, and it does not belong in a single-product PDP's customization copy.
