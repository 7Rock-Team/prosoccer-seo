# V2 versus Test feed: a ten-minute check

**Date:** 2026-08-28 | **For:** Mike | **Item:** B-TECH-03 | **Author:** ORIN

Two Google Shopping US feeds exist in DataFeedWatch. **V2 includes 14,903 products, Test includes
16,706, a 1,803 difference on the same channel type.** The store has 16,322 published products.

Neither is failing: approval is essentially 100%. This matters anyway, for two reasons.

- **V2 carries 1,419 FEWER items than the store has published products.** If V2 is production,
  roughly 1,419 products cannot appear in free listings at all, by a rule nobody has identified.
- **Test carries 384 MORE items than the store has published.** A test feed larger than the
  catalogue is worth explaining on its own.
- **If both submit to the same Merchant Center account, we are competing against ourselves.** In
  an item that is now about competitiveness rather than eligibility, duplicate offers for the same
  product are a direct contributor.

---

## 1. Are both feeds actually submitting (3 minutes)

In DataFeedWatch, open each of the two Google Shopping US channels in turn and look for the
**destination or connection** setting, not the product count.

For each feed, note:

- **Is it connected to a Merchant Center account, or is it download-only?** A feed can exist and
  generate output without ever being submitted. Download-only or FTP-only means it is inert and
  the question closes.
- **Which Merchant Center account ID is it connected to.** Write both down.
- **Is the channel status active or paused.**

**The answer you are looking for:** if both are connected and active against the **same** account
ID, they are both submitting and duplicate offers are real. If Test is paused, download-only, or
pointed at a different or sandbox account, it is harmless and only V2's 1,419-product gap matters.

## 2. What rule differs between them (4 minutes)

Open both channels' **filters or rules** view side by side. DataFeedWatch applies exclusions as
named rules, so the difference is usually visible in one screen.

Look for rules that exclude on:

- **availability or inventory** (for example, exclude when quantity equals 0). This is the most
  likely candidate given two thirds of the catalogue is out of stock, though note the gap is 1,419
  and out-of-stock is 10,818, so an availability rule alone does not explain it.
- **price** (exclude below or above a threshold)
- **product type, vendor or tag** (exclude a category, a brand, or a tag such as clearance or
  final-sale)
- **missing field** (exclude when an identifier or image is absent)

**Compare the rule LISTS, not the counts.** The useful output is the name of a rule present on one
feed and absent on the other.

## 3. Which is production (2 minutes)

Check each feed's **last download or fetch timestamp** and its update schedule. The production
feed is the one Google is actually pulling on a schedule. If **Test** turns out to be the one
updating on schedule while V2 is stale, that is the finding, and it inverts which gap matters.

## 4. The Master Field Issue warning (1 minute)

There is a shop-level **Master Field Issue** warning affecting all channels. Open it and read
which field it names. A master field is an input other rules depend on, so a broken one can
silently change what downstream feeds include, which would be a plausible source of a 1,803 gap.

---

## What to report back

1. Both feeds' Merchant Center account IDs, and whether each is connected and active
2. The name of any rule present on one feed and absent on the other
3. Which feed updated most recently
4. What field the Master Field Issue names

**If both feeds submit to the same account, that is the headline** and it goes straight into
B-TECH-03 as a competitiveness contributor. If not, the only live question is which V2 rule
excludes 1,419 products.

**Nothing here blocks Batch 17.**
