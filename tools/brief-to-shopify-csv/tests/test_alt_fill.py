#!/usr/bin/env python3
"""
Synthetic tests for the CONDITIONAL Image Alt Text rule and the parent-row-only
update logic (spec section 6).

The live fixtures (HQ2254, JP6271) already have alt text on every positioned
row, so the alt-FILL branch is never exercised by them. This module builds a
small synthetic export in memory to exercise exactly that untested branch:

  - empty alt cell + Image Position present  -> WRITE the brief alt
  - non-empty alt cell + Image Position      -> PRESERVE verbatim
  - empty alt cell + NO Image Position        -> leave untouched (not an image row)
  - Image Position beyond the brief's alt count -> leave empty (fewer alts)

It also asserts product-level target fields are written ONLY on the parent row,
and that non-target columns never change.
"""

import os
import sys
import unittest

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_TOOL_DIR = os.path.dirname(_THIS_DIR)
if _TOOL_DIR not in sys.path:
    sys.path.insert(0, _TOOL_DIR)

import brief_to_shopify_csv as mod  # noqa: E402


def make_header():
    # Minimal header containing every column resolve_columns() requires, plus a
    # couple of non-target columns to prove pass-through.
    return [
        mod.COL_HANDLE,            # 0
        mod.COL_TITLE,             # 1  (non-target, must never change)
        mod.COL_BODY,              # 2  target
        mod.COL_TAGS,              # 3  (non-target, must never change)
        mod.COL_SEO_TITLE,         # 4  target
        mod.COL_SEO_DESC,          # 5  target
        mod.COL_SHORT_DESC,        # 6  target
        mod.COL_VARIANT_SKU,       # 7
        mod.COL_IMAGE_POSITION,    # 8
        mod.COL_IMAGE_ALT,         # 9  target (conditional)
        "Variant Price",           # 10 (non-target, must never change)
    ]


def make_fields():
    return {
        "body_html": "<h2>New body</h2>",
        "seo_title": "New SEO Title",
        "seo_description": "New SEO Description",
        "short_description_html": "<p>New short.</p>",
        "image_alts": ["ALT ONE", "ALT TWO", "ALT THREE"],  # 3 alts only
    }


class AltFillTest(unittest.TestCase):
    def setUp(self):
        self.header = make_header()
        self.idx = mod.resolve_columns(self.header)
        # Rows (Handle "p"):
        # row 0 PARENT: pos 1, EMPTY alt  -> should WRITE "ALT ONE"
        # row 1 image : pos 2, EXISTING alt -> PRESERVE
        # row 2 image : pos 3, EMPTY alt  -> WRITE "ALT THREE"
        # row 3 image : pos 4, EMPTY alt  -> brief has no alt #4 -> leave EMPTY
        # row 4 variant: NO pos, EMPTY alt -> not an image row, leave EMPTY
        self.data = [
            ["p", "Keep Title", "old body", "keep,tags", "", "", "old short",
             "SKU1-A", "1", "", "9.99"],
            ["p", "", "", "", "", "", "", "SKU1-B", "2", "EXISTING ALT", "9.99"],
            ["p", "", "", "", "", "", "", "SKU1-C", "3", "", "9.99"],
            ["p", "", "", "", "", "", "", "SKU1-D", "4", "", "9.99"],
            ["p", "", "", "", "", "", "", "SKU1-E", "", "", "9.99"],
        ]
        self.applied = [{
            "sku": "SKU1", "handle": "p", "parent_idx": 0,
            "row_indices": [0, 1, 2, 3, 4], "fields": make_fields(), "brief": "SKU1_x_brief.md",
        }]
        self.out, self.log = mod.build_output(self.data, self.idx, self.applied)

    def test_empty_alt_with_position_is_written(self):
        self.assertEqual(self.out[0][self.idx[mod.COL_IMAGE_ALT]], "ALT ONE")
        self.assertEqual(self.out[2][self.idx[mod.COL_IMAGE_ALT]], "ALT THREE")

    def test_existing_alt_is_preserved(self):
        self.assertEqual(self.out[1][self.idx[mod.COL_IMAGE_ALT]], "EXISTING ALT")

    def test_position_beyond_brief_alts_left_empty(self):
        # pos 4 exists but brief only has 3 alts -> cell stays empty
        self.assertEqual(self.out[3][self.idx[mod.COL_IMAGE_ALT]], "")

    def test_no_position_row_untouched(self):
        # No Image Position -> not a gallery row -> never written even though empty
        self.assertEqual(self.out[4][self.idx[mod.COL_IMAGE_ALT]], "")

    def test_product_fields_only_on_parent_row(self):
        self.assertEqual(self.out[0][self.idx[mod.COL_BODY]], "<h2>New body</h2>")
        self.assertEqual(self.out[0][self.idx[mod.COL_SEO_TITLE]], "New SEO Title")
        self.assertEqual(self.out[0][self.idx[mod.COL_SEO_DESC]], "New SEO Description")
        self.assertEqual(self.out[0][self.idx[mod.COL_SHORT_DESC]], "<p>New short.</p>")
        # Variant/image rows must NOT receive product-level fields.
        for r in (1, 2, 3, 4):
            self.assertEqual(self.out[r][self.idx[mod.COL_BODY]], "")
            self.assertEqual(self.out[r][self.idx[mod.COL_SEO_TITLE]], "")
            self.assertEqual(self.out[r][self.idx[mod.COL_SHORT_DESC]], "")

    def test_hard_constraints_title_tags_price_unchanged(self):
        ti, tg, vp = (self.idx[mod.COL_TITLE], self.idx[mod.COL_TAGS],
                      self.header.index("Variant Price"))
        for r in range(len(self.data)):
            self.assertEqual(self.out[r][ti], self.data[r][ti], "Title changed on row %d" % r)
            self.assertEqual(self.out[r][tg], self.data[r][tg], "Tags changed on row %d" % r)
            self.assertEqual(self.out[r][vp], self.data[r][vp], "Variant Price changed on row %d" % r)

    def test_validation_passes(self):
        checks = mod.validate_output(self.header, self.header, self.data, self.out, self.idx)
        for name, passed, detail in checks:
            self.assertTrue(passed, "%s failed: %s" % (name, detail))


if __name__ == "__main__":
    unittest.main(verbosity=2)
