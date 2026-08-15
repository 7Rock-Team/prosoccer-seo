#!/usr/bin/env python3
"""Tests for the editorial body H2 casing check in voice_check.py.

Editorial body H2s (the H2 sections between the "### Description" marker and the
"## Product Details" marker) must use sentence case: the first word is
capitalized, with "adidas" the sole lowercase-start exception. The check is
scope-limited -- it flags only lowercase-initial body H2s and does NOT attempt
reverse Title-Case-drift detection (that stays at SCRIBE Phase 4 + ORIN Gate 15).

Covers the four cases from the 2026-06-29 spec:
  1. all-uppercase first words on body H2s        -> PASS
  2. a lowercase first word on a body H2          -> FAIL, with the line number
  3. "adidas" as the first word in a body H2      -> PASS (exception)
  4. mixed casing across H2s                       -> FAIL, only the violators
"""

import os
import sys
import unittest
from pathlib import Path

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

import voice_check as vc  # noqa: E402


def make_brief(body_h2s):
    """Build a minimal brief whose editorial body region carries the given H2s.

    A lowercase FAQ H3 is included AFTER the "## Product Details" marker to prove
    the check is scoped to the editorial body region and does not reach into the
    FAQ (FAQ H3 casing stays with SCRIBE Phase 4 + ORIN Gate 15, not this script).
    Returns (text, {h2: line_number}) so tests can assert exact line numbers.
    """
    lines = [
        "# adidas Example PDP",                                          # 1
        "",                                                             # 2
        "### Description (body_html, accordion below product images)",  # 3
        "",                                                             # 4
    ]
    h2_lines = {}
    for h2 in body_h2s:
        lines.append(f"## {h2}")
        h2_lines[h2] = len(lines)  # 1-based line number of the H2 just appended
        lines.append("Body prose paragraph that says something real.")
        lines.append("")
    lines.append("## Product Details: Example")
    lines.append("- one technical attribute per bullet")
    lines.append("## FAQs about the Example")
    lines.append("### what does this lowercase FAQ question prove?")
    lines.append("It proves the check stops at the Product Details marker.")
    return "\n".join(lines), h2_lines


class TestLowercaseBodyH2s(unittest.TestCase):
    def test_1_all_uppercase_first_words_pass(self):
        text, _ = make_brief([
            "Some players chase the game, you set it",
            "The Predator control lineage, in the Elite tier",
            "Who the Predator Elite FG is for",
        ])
        hits = vc.find_lowercase_body_h2s(text.splitlines())
        self.assertEqual(hits, [], f"clean brief should produce no hits, got {hits}")
        self.assertEqual(vc.check(text), 0, "clean brief should PASS (exit 0)")

    def test_2_lowercase_first_word_fails_with_line_number(self):
        text, h2_lines = make_brief([
            "The clean overview",
            "what your kid actually gets on the turf",
            "Who it is for",
        ])
        hits = vc.find_lowercase_body_h2s(text.splitlines())
        self.assertEqual(len(hits), 1, f"expected exactly one violation, got {hits}")
        line_no, line_text = hits[0]
        self.assertEqual(line_no, h2_lines["what your kid actually gets on the turf"])
        self.assertTrue(line_text.startswith("## what your kid"), line_text)
        self.assertEqual(vc.check(text), 1, "brief with a lowercase body H2 should FAIL (exit 1)")

    def test_3_adidas_first_word_passes(self):
        text, _ = make_brief([
            "adidas took the laces out on purpose",
            "The step-up build, made for turf",
            "Who these turf shoes are for",
        ])
        hits = vc.find_lowercase_body_h2s(text.splitlines())
        self.assertEqual(hits, [], f"'adidas' opener is the exception; got {hits}")
        self.assertEqual(vc.check(text), 0, "adidas-opener brief should PASS (exit 0)")

    def test_4_mixed_casing_flags_only_violators(self):
        text, h2_lines = make_brief([
            "the everyday turf shoe that keeps up with a busy kid",
            "What your kid actually gets on the turf",
            "who the Junior Predator League turf is for",
        ])
        hits = vc.find_lowercase_body_h2s(text.splitlines())
        flagged_lines = sorted(ln for ln, _ in hits)
        expected = sorted([
            h2_lines["the everyday turf shoe that keeps up with a busy kid"],
            h2_lines["who the Junior Predator League turf is for"],
        ])
        self.assertEqual(flagged_lines, expected, f"should flag only the 2 lowercase H2s, got {hits}")
        clean_line = h2_lines["What your kid actually gets on the turf"]
        self.assertNotIn(clean_line, flagged_lines, "the correctly-cased H2 must not be flagged")
        self.assertEqual(vc.check(text), 1)

    def test_faq_h3_lowercase_is_not_flagged(self):
        # Defensive: the lowercase FAQ H3 lives after the Product Details marker,
        # outside the editorial body region, so the scoped check must ignore it.
        text, _ = make_brief(["A clean overview", "The build", "Who it is for"])
        hits = vc.find_lowercase_body_h2s(text.splitlines())
        self.assertEqual(hits, [], "FAQ H3 is out of scope for this check")

    def test_5_ki0586_h4_level_headers_regression(self):
        # Regression for the 2026-06-30 KI0586 gap: the Copa Pure IV Elite exemplar
        # used #### body-section headers (one heading level too deep) with lowercase
        # first words ("the first touch...", "built for..."). The original ##-only
        # check missed them and voice_check PASSED a real sentence-case violation.
        # Built from KI0586's exact original headers. This MUST fail on the pre-patch
        # ##-only implementation (that failure is the evidence the gap existed) and
        # pass after the heading-level-agnostic patch. It stays in the suite forever
        # to prevent re-regression.
        text = "\n".join([
            "# adidas Copa Pure IV Elite (Road to Glory Pack)",
            "",
            "### Description (body_html, accordion below product images)",
            "",
            "#### the first touch that buys you a half-second",   # lowercase -> violation
            "Some players win games with pace.",
            "",
            "#### adidas went back to the classic look",          # adidas opener -> excepted
            "The fourth-generation Copa Pure drops the knit collar.",
            "",
            "#### built for the player who runs the tempo",       # lowercase -> violation
            "This is a number 8 or a number 10's cleat.",
            "",
            "#### Product Details: Copa Pure IV Elite",
            "- Fusionskin upper",
        ])
        hits = vc.find_lowercase_body_h2s(text.splitlines())
        self.assertEqual(len(hits), 2, f"both lowercase #### headers must be detected, got {hits}")
        self.assertTrue(any(t.startswith("#### the first touch") for _, t in hits))
        self.assertTrue(any(t.startswith("#### built for the player") for _, t in hits))
        self.assertFalse(any("adidas" in t for _, t in hits), "the adidas opener is excepted")
        self.assertEqual(vc.check(text), 1, "an H4-level lowercase body header must FAIL the check")

    def test_6_h3_level_body_header_detected(self):
        # A ### body header (between ### Description and ### Product Details) with a
        # lowercase first word must also be caught.
        text = "\n".join([
            "# Title",
            "### Description (body_html, accordion below product images)",
            "### lowercase three-hash body header",
            "prose",
            "### Product Details: Example",
            "- bullet",
        ])
        hits = vc.find_lowercase_body_h2s(text.splitlines())
        self.assertEqual(len(hits), 1, f"a ### body header must be detected, got {hits}")
        self.assertEqual(vc.check(text), 1)

    def test_no_region_no_match(self):
        # A non-brief file (no Description -> Product Details region) never matches,
        # even if it contains a lowercase "## " heading somewhere.
        text = "# Some doc\n\n## a lowercase heading in a non-brief file\n\nprose\n"
        hits = vc.find_lowercase_body_h2s(text.splitlines())
        self.assertEqual(hits, [], "files without the region markers must not match")


class QuotedProscriptionExemptionTests(unittest.TestCase):
    """The quoted-proscription exemption for the UK 'boots' check (added 2026-08-13).

    A rule cannot state itself without naming the term it forbids. The exemption is
    narrow on purpose: it fires only when the term is QUOTED and the line NEGATES
    it. Regression fixture is the real line from SEO_BATCH_PROCESS.md section 3,
    which made that canonical file permanently fail its own voice check.
    """

    def test_real_canonical_line_is_exempt(self):
        text = '# Copy rules\n\n- "cleats" or "shoes", never "boots"\n'
        self.assertEqual(
            vc.check(text), 0,
            "the standing copy rule must not flag itself; it has to name the term",
        )

    def test_unquoted_boots_after_negation_still_fails(self):
        # Negation alone must NOT exempt: this is real prose using the UK term.
        text = "# Brief\n\nNever wear boots on turf, they wreck the surface.\n"
        self.assertEqual(
            vc.check(text), 1,
            "an unquoted UK 'boots' must still fail even after a negation word",
        )

    def test_quoted_boots_without_negation_still_fails(self):
        # Quoting alone must NOT exempt: no rule is being stated here.
        text = '# Brief\n\nHe called them "boots" and laced up.\n'
        self.assertEqual(
            vc.check(text), 1,
            "a quoted UK 'boots' with no negation must still fail",
        )

    def test_exemption_does_not_leak_to_other_terms_on_the_line(self):
        # Blanking the quoted term must not blank a genuine violation beside it.
        text = '# Copy rules\n\n- never say "boots"; these boots are for grass\n'
        self.assertEqual(
            vc.check(text), 1,
            "a real violation on the same line must survive the exemption",
        )

    def test_curly_quotes_are_covered(self):
        text = "# Copy rules\n\n- “cleats” not “boots”\n"
        self.assertEqual(
            vc.check(text), 0,
            "curly quotes must be treated the same as straight quotes",
        )


class FencedBlocksInCanonicalFilesTests(unittest.TestCase):
    """Fenced worked examples in instruction files must be CHECKED, not skipped.

    Origin (2026-08-14): `strip_backticks` blanked fenced blocks before every
    check, so worked examples, the most-copied text in the repo, were invisible.
    That is the mechanism behind all four exemplar-class failures: the 20 Meta
    Title brand-suffix violations, the capitalized `Adidas` spread, the UK `boot`
    in the silo files, and a meta description exemplar that was pre-workforce copy
    carrying a wrong shipping fact. `work-log/follow-ups.md` 2026-07-31 item.

    The split: fenced content is scanned in canonical INSTRUCTION files, still
    stripped everywhere else, and inline backticks stay stripped in both so a rule
    can still name the thing it forbids.
    """

    FENCED_VIOLATION = (
        "# Playbook section\n"
        "\n"
        "## Worked example\n"
        "\n"
        "```\n"
        "Meta Title\n"
        "Adidas Tiro 23 Training Pants\n"
        "```\n"
    )

    def test_fenced_violation_is_caught_in_context_playbook(self):
        v = vc.collect_violations(
            self.FENCED_VIOLATION,
            Path("context/page-type-playbooks/product-page-playbook.md"),
        )
        self.assertTrue(
            any("Adidas" in line for line in v),
            "capitalized Adidas inside a fenced worked example must FAIL in a playbook",
        )

    def test_fenced_violation_is_caught_in_agent_definition(self):
        v = vc.collect_violations(
            self.FENCED_VIOLATION, Path(".claude/agents/on-page-seo/agent.md")
        )
        self.assertTrue(any("Adidas" in line for line in v))

    def test_fenced_violation_is_caught_in_root_process_doc(self):
        v = vc.collect_violations(self.FENCED_VIOLATION, Path("SEO_BATCH_PROCESS.md"))
        self.assertTrue(any("Adidas" in line for line in v))

    def test_fenced_violation_still_skipped_in_ordinary_deliverable(self):
        v = vc.collect_violations(
            self.FENCED_VIOLATION,
            Path("deliverables/page-optimizations/2026-08-14_x/SKU_brief.md"),
        )
        self.assertEqual(
            v, [], "a fenced block in a deliverable is code or a quotation, not an exemplar"
        )

    def test_fenced_violation_still_skipped_in_agent_briefings(self):
        v = vc.collect_violations(
            self.FENCED_VIOLATION,
            Path(".claude/agents/on-page-seo/briefings/2026-05-29_adidas-soccer-cleats.md"),
        )
        self.assertEqual(
            v, [], "briefings are workforce-internal audit trail, not instruction"
        )

    def test_fenced_violation_skipped_when_no_path_given(self):
        self.assertEqual(vc.collect_violations(self.FENCED_VIOLATION), [])

    def test_inline_backticks_still_stripped_in_canonical_files(self):
        """A rule must be able to name what it forbids."""
        text = (
            "Never end a Meta Title with a manufacturer brand such as `| adidas`.\n"
            "Taxonomy compounds like `non-Adidas` stay as written.\n"
            'The footwear term rule reads: `- "cleats" or "shoes", never "boots"`.\n'
        )
        self.assertEqual(
            vc.collect_violations(text, Path("context/workforce-conventions.md")),
            [],
            "inline citations must stay exempt or the rules cannot be stated",
        )

    def test_em_dash_inside_fenced_example_is_caught(self):
        text = "## Worked example\n\n```\nShort Description\nThe cleat \u2014 built for speed.\n```\n"
        v = vc.collect_violations(text, Path("context/page-type-playbooks/collection-page-playbook.md"))
        self.assertTrue(any("EM-DASH" in line for line in v))

    def test_uk_boot_inside_fenced_example_is_caught(self):
        text = "## Worked example\n\n```\nDescription\nThe fastest boot Nike has ever built.\n```\n"
        v = vc.collect_violations(text, Path("context/silo-positioning/furon.md"))
        self.assertTrue(any("boot" in line.lower() for line in v))

    def test_clean_fenced_example_still_passes(self):
        text = (
            "## Worked example\n\n```\nMeta Title\nadidas Copa Pure IV Elite FG Soccer Cleats\n"
            "\nMeta Description\nThe adidas Copa Pure IV Elite turns a clean first touch into your edge.\n```\n"
        )
        self.assertEqual(
            vc.collect_violations(text, Path("context/page-type-playbooks/product-page-playbook.md")),
            [],
        )

    def test_pedagogical_marker_still_exempts_inside_a_fence(self):
        text = "## Worked example\n\n```\nINCORRECT: Adidas Tiro 23 Training Pants\n```\n"
        self.assertEqual(
            vc.collect_violations(text, Path("context/page-type-playbooks/product-page-playbook.md")),
            [],
            "anti-pattern demonstrations must stay exempt inside fences too",
        )

    def test_fence_delimiters_do_not_shift_line_numbers(self):
        text = "line one\n\n```\nAdidas here on line four\n```\n"
        v = vc.collect_violations(text, Path("context/x.md"))
        self.assertTrue(any("line 4:" in line for line in v), v)


class CanonicalInstructionClassificationTests(unittest.TestCase):
    def test_in_scope_paths(self):
        for p in (
            "context/03-brand-voice.md",
            "context/page-type-playbooks/homepage-playbook.md",
            "templates/per-sku-input-template.md",
            ".claude/agents/master-strategist/agent.md",
            "SEO_BATCH_PROCESS.md",
            "STEP_2_BRIEFING.md",
            "CLAUDE.md",
            r"C:\Dev-Projects\marketing\prosoccer-seo\context\workforce-conventions.md",
        ):
            self.assertTrue(vc.is_canonical_instruction(Path(p)), p)

    def test_out_of_scope_paths(self):
        for p in (
            "deliverables/page-optimizations/2026-08-14_x/SKU_brief.md",
            "deliverables/tracking/sitemap-state.md",
            ".claude/agents/on-page-seo/briefings/2026-05-29_adidas-soccer-cleats.md",
            "work-log/follow-ups.md",
            "strategy/sprint-backlog.md",
            "README.md",
        ):
            self.assertFalse(vc.is_canonical_instruction(Path(p)), p)

    def test_none_path_is_out_of_scope(self):
        self.assertFalse(vc.is_canonical_instruction(None))


if __name__ == "__main__":
    unittest.main()
