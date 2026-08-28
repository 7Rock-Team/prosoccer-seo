# Primary selection for pages that already rank

**Date:** 2026-08-27 | **Author:** ORIN | **Status: PROPOSAL, HOLDING FOR MIKE. Nothing authored.**

Batch 17's ten are approved in principle. This settles how their primaries are chosen before
any brief is written.

---

## 1. The proposed rule, and the verdict

> For a page already earning impressions, the primary is the term it already earns. The copy
> supports that term rather than redirecting the page.

**Supported by the data, with one amendment and one correction to how it is measured.**

The evidence is strong. Measured at the level of the earned TERM rather than the page average,
these pages rank better than their page-average position suggests, and in most cases they are
the page our own store fields for that term:

| Page | Earned term | Term impr | Share of the term across all our pages | Term pos |
|---|---|---|---|---|
| club-america authentic home | `america jersey 2026` | 3,710 | **73.3%** | 3.50 |
| nike-strike-sleeves-socks | `soccer sleeve socks` | 854 | **87.7%** | 11.85 |
| panini stickers box | `panini sticker box` | 329 | **70.8%** | 10.74 |
| usmnt stadium home shorts | `usmnt shorts` | 1,700 | **63.3%** | 10.57 |
| phantom 6 low elite haaland | `haaland cleats` | 4,124 | **54.6%** | 6.08 |
| paraguay authentic home | `paraguay jersey` | 5,189 | **45.3%** | 4.89 |
| italy authentic home | `italy world cup jersey` | 512 | 50.1% | 10.95 |
| guatemala mens home | `guatemala soccer jersey` | 6,450 | 41.7% | 4.88 |
| spain stadium away | `spain jersey 2026` | 5,971 | 26.6% | 5.50 |
| colombia stadium home | `colombia jersey 2026` | 5,613 | 17.5% | 10.20 |

Google has already run the experiment we would otherwise be guessing at. Assigning a different
primary to a page at position 3.50 on a term it already fields 73% of is not optimization, it is
starting over on a page that has already arrived.

### The amendment: an earned term must be CONCENTRATED to be a primary

The rule as written assumes each page has a term it earns. For four of the ten, the top query is
a thin slice of a long tail rather than a target:

| Page | Top query share OF THAT PAGE's impressions | Term impr |
|---|---|---|
| panini stickers box | **1.1%** | 329 |
| italy authentic home | **4.5%** | 512 |
| nike-strike-sleeves-socks | **6.1%** | 854 |
| usmnt shorts | 16.1% | 1,700 |
| guatemala | 24.4% | 6,450 |
| colombia stadium home | 25.1% | 5,613 |
| spain stadium away | 25.8% | 5,971 |
| paraguay | 28.8% | 5,189 |
| haaland | 19.1% | 4,124 |
| club-america | 34.8% | 3,710 |

The Panini box earns 29,765 impressions and its single biggest query is 329 of them. There is no
earned term there; there is diffuse demand across hundreds of long-tail queries. Making
`panini sticker box` its primary would be picking a new destination in exactly the way the rule
is trying to avoid, while telling ourselves we were not.

**Proposed condition: the earned term becomes the primary when it holds at least 15% of the
page's impressions AND at least 1,000 term impressions in the trailing 90 days.** Below either
threshold the page has no earned term and falls back to conventional assignment.

Applying it: **seven of the ten qualify** (club-america 34.8%, paraguay 28.8%, spain 25.8%,
colombia 25.1%, guatemala 24.4%, haaland 19.1%, usmnt 16.1%). **Panini 1.1%, Italy 4.5% and the
socks 6.1% do not**, and revert to conventional keyword research.

The 1,000-impression floor is not new: it is the same meaningful-signal floor B-CEDE-01 and pack
succession v3 already use, on the same reasoning that a page at position 2 on one impression is
noise rather than evidence.

### The correction: measure the TERM, not the page

The positions in the Batch 17 proposal (5.48 to 12.28) are GSC 90-day **page averages across all
queries**. They are not the position for any specific term, and they are not what the rule
should key on. Term-level positions differ materially in both directions:

- club-america: page 5.48, **term 3.50**
- guatemala: page 5.93, **term 4.88**
- paraguay: page 5.99, **term 4.89**
- colombia: page 9.14, **term 10.20**
- socks: page 8.44, **term 11.85**

**This matters immediately for the top-5 posture.** On page average, two pages sit under 6. On
earned-term position, **three sit under 5** (club-america 3.50, guatemala 4.88, paraguay 4.89)
and Spain is at 5.50. The posture must key on the term, or it fires on the wrong pages.

---

## 2. Question 1: when the earned term is hierarchy-invalid

**The answer is not the one the framing expects, and Guatemala is the reason.**

Head to head on `guatemala soccer jersey`, across every page of ours that appears:

| Page | Impressions | Clicks | Position | Share |
|---|---|---|---|---|
| `/collections/guatemala` | 8,131 | **180** | 5.62 | **52.6%** |
| `/products/umbro-2025-2026-guatemala-mens-home` | 6,450 | **0** | 4.88 | 41.7% |
| four other Guatemala PDPs | 865 | 0 | 5.15 to 11.07 | 5.7% |

**The collection earns more impressions AND all 180 of the clicks. The PDP has a marginally
better average position and converts nothing.** That is the hierarchy being vindicated, not
contradicted: a searcher typing `guatemala soccer jersey` wants to see the range, and when both
pages are shown, the collection is the one they click.

Guatemala is therefore **not** a second Cruz Azul. B-CEDE-01 recorded n=1 and said explicitly not
to propose a fix on one instance. This measurement leaves it at n=1.

### Proposed condition

**The earned term overrides the hierarchy only when the hierarchy-preferred owner is
demonstrably worse at it, measured, not assumed.**

Test, run per contested term over a trailing 90 days with a 50-impression floor on both sides:

1. Pull term-level GSC for the exact term, dimension `page`, canonical rows only.
2. If a collection appears and earns **more impressions or more clicks** than the PDP, the
   collection keeps the term. The PDP takes a qualified sub-floor primary. This is Guatemala.
3. If the PDP earns more on both and the collection is materially worse in position, the PDP
   holds the term and it is recorded as PDP-held. This is Paraguay (PDP 45.3% at 4.89 versus
   collection 13.1% at 10.24) and Club America (73.3% at 3.50 versus 8.1% at 8.15).
4. If no collection appears at all above the floor, there is nothing to cede to and the PDP
   holds it. This is Spain: the `spain-jerseys` collection takes 1,521 impressions at 12.82 and
   does not appear on `spain jersey 2026` at all.

**Is this an amendment to the hierarchy rule, or an exception? It is an AMENDMENT, and it should
be written as one.**

The hierarchy's stated justification is intent: collections own terms "where a searcher would be
satisfied by multiple products." That is a **prediction about behaviour**. Clicks are the
measurement of that same prediction. Where the two agree, nothing changes. Where they disagree
on a specific term with real volume, the measurement is better evidence than the prediction,
because it is the same question answered by data instead of by judgment.

Calling it an exception would imply the rule is right and the case is odd. That is the weaker
reading, and it is the reading that lets a second and third instance accumulate without ever
revisiting the rule. The honest form is: **the hierarchy assigns by default and remains the
default; a measured, term-level head-to-head above the floor can override it in either
direction.** Note the direction that matters most here: applied to Guatemala it hands the term
TO the collection, which is the hierarchy's own answer. An amendment that mostly confirms the
rule is not a weakening of it.

**Cost of adopting it, stated plainly:** it adds one GSC call per contested term at pre-dispatch,
and it creates a class of terms whose ownership is evidence-based and therefore can change. That
needs the same churn guard pack succession already has, or pages will thrash.

---

## 3. Question 2: when the earned term is already assigned to a registry page

**For these ten, it does not arise, and that is a verified statement rather than an assumption.**
Criterion 4 of the Batch 17 cut removed every candidate whose top query collided with any of 429
primary, target and ceded terms in `products-master.csv` and `ceded-terms.csv`, by exact match
plus two-token containment in both directions. All ten survived that filter.

**The general rule, for when it does arise:**

**Demonstrated performance outranks assignment, but it does not silently reassign.** An assigned
term is a claim; an earned term is a result. When the two conflict, the earning page has evidence
and the assigned page has a decision. But a shipped page carrying a primary is not retargeted
without Mike's explicit per-page call. That is already the standing rule under pack succession
v3, and this proposal does not widen it.

Concretely: the earning page takes a **qualified** primary and the conflict is logged with both
pages' term-level numbers. If the assigned page earns nothing on its own claimed term over two
consecutive measurement periods while the unassigned page earns it, that is the trigger to bring
the reassignment to Mike. One period is not enough, for the same churn reason.

**The uncomfortable part, which should be said rather than buried:** the registry's assigned
primaries have never been validated against what the pages actually earn. `Current ranking` data
exists in 26 of 314 briefs and nearly every recorded value reads "not in top 100." So the
population of assigned-but-not-earned terms is probably large, and this rule will surface it. I
would not treat that as a defect to fix in Batch 17; it is a measurement to run separately.

---

## 4. Question 3: the ranking-aware posture, verbatim, and whether it is sufficient

Reproduced exactly from `context/workforce-conventions.md` 'Ranking-aware posture' (identical
text appears in `.claude/agents/on-page-seo/agent.md`):

> The Current ranking position governs how aggressively SCRIBE iterates on Title and H1 copy.
>
> - **Top 5:** WARNING required in the visible brief. The line reads: "Page currently ranks top 5. Title/H1 changes carry equity risk. Confirm with Mike before shipping changes to these fields." Recommendations preserve exact-match phrasing of the primary keyword in Title and H1; copy iteration leans toward Meta Description, Short Description, and Long Description where equity risk is lower.
> - **Top 6 to 20:** Standard recommendations. Current position noted for context. No warning line.
> - **Top 21 to 100:** Standard recommendations. Current position noted for context.
> - **Not ranking (not in top 100):** Standard recommendations. Treated as opportunity for a fresh ranking attempt.

### It is not sufficient. Four defects, in order of severity.

**1. The 6-to-20 band has no protection at all, and that is where this batch lives.** "Standard
recommendations" means full latitude on Title and H1. On earned-term position, six of the ten sit
in 6 to 20. These are pages ranking on page one for a term they already field the majority of,
and the posture currently authorises rewriting their title with no warning and no constraint.
**The cliff at 5 is arbitrary.** Nothing about position 5.9 versus 6.1 justifies the difference
between "equity risk, confirm with Mike" and "no note required."

**2. It keys off the position of the CHOSEN primary, which inverts the order this rule needs.**
The posture runs after a primary is picked: choose the term, look up the rank, apply the band.
Under the proposed rule the earned term IS the primary, so the ranking data is the input to
selection rather than a check on it. The sequence has to flip.

**3. It reads a different instrument than the one this proposal uses.** The posture specifies
`mcp__dfs-mcp__serp_organic_live_advanced`, a point-in-time SERP rank. Everything here is GSC
90-day average position. Those disagree routinely, and the posture does not say which governs.
Since GSC is the source of record for our own ranking context, and since a 90-day average is far
more stable than a single SERP snapshot, GSC should govern for this decision and the SERP call
should stay what it is good at, competitor context.

**4. Mike's premise is right but the reason is worse than "no page ranked that well."** Audited
across all 314 briefs on disk:

- Briefs containing the top-5 WARNING line: **0**.
- Briefs containing a `Current ranking:` line at all: **26 of 314, about 8%**.
- `baseline_position`, `day_30_position` and `day_60_position` in `products-master.csv`:
  populated on **0 of 178 rows**.

So the posture has never fired, but not because pages were measured and found lower. **The
mandatory input was never collected on 92% of briefs, and the registry has never stored a
position for any page.** The posture is not a safeguard that has been waiting; it is a safeguard
that has never been wired to anything. That belongs in the codification checklist as a check
that cannot fire, which is item 9's class.

---

## 5. The safe band

Mike's instinct: under 5 protect Title and H1 and change only description and body; above 20
there is nothing to protect. **The shape is right. Both lines want moving, and the data says
where.**

Position distribution across the 1,280 untracked products:

| Page-average position | Pages | Share | Impressions | CTR |
|---|---|---|---|---|
| under 5 | 57 | 4.5% | 360,451 | **0.607%** |
| 5 to 10 | 990 | **77.3%** | 7,688,241 | 0.530% |
| 10 to 20 | 215 | 16.8% | 871,785 | 0.382% |
| over 20 | 18 | 1.4% | 47,698 | 0.417% |

**77.3% of the population sits between 5 and 10.** A protection line drawn at 5 leaves the
overwhelming majority of these pages unprotected, and CTR only falls off meaningfully past 10,
not past 5. The 5-to-10 band converts at 0.530% against 0.607% above it, a real but modest gap;
the drop to 0.382% at 10 to 20 is the first genuine break in the curve.

**Proposed bands, keyed on EARNED-TERM position, not page average:**

| Earned-term position | Posture |
|---|---|
| **under 5** | Protect Title and H1 fully. Exact-match phrasing preserved. Changes to those two fields need Mike per page. Iterate on Meta Description, Short Description, Long Description. This is the current top-5 rule, unchanged. |
| **5 to 10** | **NEW BAND.** Title and H1 may be improved but must RETAIN the earned term in exact-match form. Everything else is open. No per-page Mike gate, but the brief states the earned term and its position so the constraint is visible and auditable. |
| **10 to 20** | Standard recommendations. Earned term should be carried into the Title where it fits naturally, but is not binding. |
| **over 20** | Standard recommendations. Nothing to protect; treat as a fresh attempt. |

The middle band is the substantive change and it is where nine of Batch 17's ten fall. It is
deliberately lighter than the under-5 rule: a constraint on wording rather than a gate on
shipping, because gating 77% of the population on Mike would make the batch model unworkable.

The line at 20 rather than 100 matches the data: only 1.4% of the population sits past 20, and
the posture's existing 21-to-100 and not-ranking bands can collapse into one.

---

## 6. Three findings that change the batch itself

Running the term-level pull surfaced three problems with the ten as proposed. **None is a reason
to stop; all three need a decision before authoring.**

**a. The Colombia pick is not the page that earns the term.** On `colombia jersey 2026`:

| Page | Impr | Pos | Share |
|---|---|---|---|
| `adidas-2026-colombia-mens-authentic-away` | **15,933** | 5.02 | **49.8%** |
| `adidas-2026-colombia-mens-stadium-home` (our pick) | 5,613 | 10.20 | 17.5% |

The page that earns the term is the Authentic Away, and it is **sold out**, which is why the
in-stock filter surfaced the Stadium Home instead. Under the proposed rule the Stadium Home does
not own `colombia jersey 2026`; it earns 17.5% of it while a sibling earns half. Options: give
the Stadium Home a genuinely distinct qualified primary, or swap the pick.

**b. The Spain pick is out-ranked by its own sibling.** On `spain jersey 2026`, our pick
(Stadium Away) takes 26.6% at position 5.50, while `adidas-2026-spain-mens-authentic-away` takes
24.2% at **4.65**. Four of our pages split 85% of a 22,455-impression term and collect about nine
clicks between them. This is severe self-competition and the batch would be adding copy to one
combatant without addressing it.

**c. Guatemala's term belongs to the collection**, per section 2. The PDP should take a qualified
primary, not `guatemala soccer jersey`. The probe rationale still holds and arguably improves:
it now tests whether a PDP can be optimized underneath a collection that owns the head term
without cannibalising it.

**A pattern worth naming across all three: near-zero clicks.** Guatemala PDP 0 clicks on 6,450
impressions. Colombia 7 clicks on 15,933. Spain about 9 clicks across 22,455. These pages appear
and are not clicked, which is the same signature as the sold-out giants and is not obviously a
copy problem. Worth holding in mind when the expected read-outs below are judged.

---

## 7. Expected read-outs for the three probes, recorded BEFORE authoring

Written now so no result can be rationalised afterwards. Measurement window: 30 and 60 days
post-import, GSC, canonical rows only, term-level where a term is named.

### Probe 1: Guatemala. Does PDP work compound under a performing collection?

- **Success:** PDP term impressions on its qualified primary rise, AND `/collections/guatemala`
  holds or grows its 8,131 impressions and 180 clicks on `guatemala soccer jersey`. Both rise.
- **Failure:** the collection's clicks fall while the PDP's rise. That is substitution, not
  compounding, and it would be evidence that PDP optimization under a strong collection
  cannibalises it.
- **Null:** PDP moves, collection unchanged, no measurable total gain. Reads as neutral.
- **Confound to declare now:** Guatemala's collection is already at 5.62 with healthy CTR. There
  may be little headroom, so a null here is weak evidence either way.

### Probe 2: USMNT shorts. Does the merch CTR advantage transfer, or is it structural?

- **Success:** position improves from 10.57 on `usmnt shorts` AND CTR holds at or above the merch
  bucket's 1.559%. That would say the advantage is a property of the query and survives our
  intervention, which makes the other 223 merch pages a real opportunity.
- **Failure, and the more interesting outcome:** position improves and CTR falls toward the
  jersey buckets' 0.2 to 0.5%. That would say the 1.559% was a property of ranking lower on
  narrower intent, and it evaporates on contact. That kills the merch thesis cheaply.
- **Null:** neither moves. Reads as no evidence, not as support.
- **Confound to declare now:** the sibling `usmnt-mens-stadium-away-shorts` sits at 7.28 on the
  same term with 36.3% share. Any gain must be checked against the sibling's numbers or we will
  read a transfer between our own pages as a win.

### Probe 3: Panini sticker box. Does the playbook generalise past apparel and footwear?

- **Success:** total page impressions rise from 29,765, and the rise is spread across the long
  tail rather than concentrated in one query. Since it fails the concentration test, the honest
  target is aggregate demand, not a single term.
- **Failure:** the brief cannot be written without inventing product attributes the scrape does
  not supply. Collectibles have no tier, cut, surface or age band, so the entire configuration
  tuple the PDP playbook is built on is absent. **If SCRIBE has to reach for fabricated specifics
  to fill the template, that is the result, and it is a useful one: the playbook does not
  generalise and collectibles need their own.**
- **Null:** brief writes cleanly, numbers do not move. Reads as inconclusive on the playbook
  question but establishes that the template is at least usable.
- **Confound to declare now:** this is a World Cup year and Panini demand is seasonal and rising
  independently of anything we do. A rise here is the LEAST attributable of the three probes, so
  the read-out leans on whether the brief could be written well, not on the traffic.

---

## 8. What is being asked

1. Accept, reject or amend the primary rule plus the 15% / 1,000-impression concentration
   condition.
2. Accept or reject the hierarchy amendment in section 2, including that it is an amendment
   rather than an exception.
3. Accept or reject the four-band posture in section 5, and confirm the shift from page-average
   to earned-term position.
4. Decide on Colombia and Spain in section 6, and confirm Guatemala takes a qualified primary.

Nothing is authored until these are settled.
