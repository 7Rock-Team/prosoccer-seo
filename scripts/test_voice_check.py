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

    def test_no_region_no_match(self):
        # A non-brief file (no Description -> Product Details region) never matches,
        # even if it contains a lowercase "## " heading somewhere.
        text = "# Some doc\n\n## a lowercase heading in a non-brief file\n\nprose\n"
        hits = vc.find_lowercase_body_h2s(text.splitlines())
        self.assertEqual(hits, [], "files without the region markers must not match")


if __name__ == "__main__":
    unittest.main()
