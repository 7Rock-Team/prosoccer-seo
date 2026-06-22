#!/usr/bin/env python3
"""
Golden-file tests for the markdown -> HTML converter (spec section 5).

Each pair in tests/golden/ is:
    input_<name>.md        markdown input
    expected_<name>.html   expected HTML output (NO trailing newline)

The test runs markdown_to_html() on the input and asserts a BYTE-FOR-BYTE match
against the expected file. If the converter's behavior ever changes (intentional
or accidental), these tests fail. This is the safety rail that makes the
"no dependencies" decision honest.

Run:
    python -m unittest discover -s tests        (from the tool folder)
    python tests/test_converter.py              (direct)
"""

import os
import sys
import unittest

# Make the tool folder importable regardless of where the test is launched from.
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_TOOL_DIR = os.path.dirname(_THIS_DIR)
if _TOOL_DIR not in sys.path:
    sys.path.insert(0, _TOOL_DIR)

from brief_to_shopify_csv import markdown_to_html  # noqa: E402

GOLDEN_DIR = os.path.join(_THIS_DIR, "golden")


def _read(path):
    with open(path, "r", encoding="utf-8", newline="") as f:
        return f.read()


def _golden_cases():
    cases = []
    for name in sorted(os.listdir(GOLDEN_DIR)):
        if name.startswith("input_") and name.endswith(".md"):
            stem = name[len("input_") : -len(".md")]
            expected = os.path.join(GOLDEN_DIR, "expected_%s.html" % stem)
            cases.append((stem, os.path.join(GOLDEN_DIR, name), expected))
    return cases


class GoldenConverterTest(unittest.TestCase):
    pass


def _make_test(stem, input_path, expected_path):
    def test(self):
        self.assertTrue(
            os.path.exists(expected_path),
            "missing expected file for %s" % stem,
        )
        md = _read(input_path)
        expected = _read(expected_path)
        actual = markdown_to_html(md)
        # Byte-for-byte comparison; show a readable diff on failure.
        self.assertEqual(
            actual,
            expected,
            "\n--- EXPECTED (%d chars) ---\n%r\n--- ACTUAL (%d chars) ---\n%r"
            % (len(expected), expected, len(actual), actual),
        )

    test.__name__ = "test_golden_%s" % stem
    return test


_cases = _golden_cases()
for _stem, _inp, _exp in _cases:
    setattr(GoldenConverterTest, "test_golden_%s" % _stem, _make_test(_stem, _inp, _exp))

# Guard: if nobody authored golden files, fail loudly rather than passing vacuously.
class GoldenPresenceTest(unittest.TestCase):
    def test_golden_files_exist(self):
        self.assertGreaterEqual(
            len(_cases), 7, "expected at least 7 golden cases, found %d" % len(_cases)
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
