"""Regression tests for scripts/phase0_product_facts.py.

Fixtures are REAL payloads captured from live product JSON on 2026-08-27, not
invented shapes. Each one is the actual case that motivated a behaviour.
"""
import unittest

import phase0_product_facts as p0


def _variants(base, sizes):
    return [{"sku": "%s-%s" % (base, s), "option1": "C", "option2": s} for s in sizes]


# The Batch 16 pair. Byte-identical titles, different colorways. This is the case
# that cost a SKU when the comparison was title-only.
UF1F16X = {
    "handle": "new-balance-furon-elite-v9-2e-wide-fg-soccer-cleats-black-fa26",
    "options": [
        {"name": "Color", "values": ["Black with White"]},
        {"name": "Adult Shoe Size", "values": ["M 7 / W 8.5", "M 7.5 / W 9"]},
    ],
    "variants": _variants("UF1F16X", ["M 7 / W 8.5", "M 7.5 / W 9"]),
}
UF1F3ZB = {
    "handle": "new-balance-furon-elite-v9-2e-wide-fg-soccer-cleats-black",
    "options": [
        {"name": "Color", "values": ["Black"]},
        {"name": "Adult Shoe Size", "values": ["M 7 / W 8.5"]},
    ],
    "variants": _variants("UF1F3ZB", ["M 7 / W 8.5"]),
}

# Apparel: no Color option at all. Verified on the Arsenal stadium jersey.
ARSENAL_JERSEY = {
    "handle": "adidas-2026-27-arsenal-mens-stadium-home-soccer-jersey",
    "options": [{"name": "Men's Apparel Size", "values": ["S", "M", "L", "XL", "2XL", "3XL"]}],
    "variants": _variants("JZ3168", ["S", "M", "L"]),
}

# Multi-token manufacturer colorway, and a youth size ladder.
JR_TEKELA = {
    "handle": "new-balance-jr-tekela-team-low-v5-fg-soccer-cleats-neon-tide",
    "options": [
        {"name": "Color", "values": ["Metallic Blue with Alkaline Green"]},
        {"name": "Youth Shoe Size", "values": ["1", "1.5", "2"]},
    ],
    "variants": _variants("YT3FL1NM", ["1", "1.5", "2"]),
}

# The Haaland cleat: official colorway disagrees with Nike's own marketing prose,
# which calls Laser Orange "red". The Color option is what governs.
HAALAND = {
    "handle": "nike-phantom-6-low-pro-firm-ground-soccer-cleats-erling-haaland-pack-fa25",
    "options": [
        {"name": "Color", "values": ["Laser Orange/Blue Void/Lemon Venom"]},
        {"name": "Adult Shoe Size", "values": ["M 4 / W 5.5"]},
    ],
    "variants": _variants("IB3094-800", ["M 4 / W 5.5"]),
}


class ColorwayTests(unittest.TestCase):
    def test_footwear_colorway_is_read_from_the_color_option(self):
        self.assertEqual(p0.extract_colorway(UF1F16X), "Black with White")
        self.assertEqual(p0.extract_colorway(UF1F3ZB), "Black")

    def test_the_pair_that_reads_identical_on_title_is_separated_by_colorway(self):
        """The whole point. Same config, same pack, distinct colorways."""
        self.assertNotEqual(p0.extract_colorway(UF1F16X), p0.extract_colorway(UF1F3ZB))

    def test_apparel_has_no_color_option_and_that_is_by_design(self):
        facts = p0.extract(ARSENAL_JERSEY)
        self.assertIsNone(facts["colorway"])
        self.assertTrue(facts["is_apparel"])
        self.assertTrue(facts["colorway_absent_by_design"])

    def test_apparel_input_line_states_absence_rather_than_blank(self):
        line = p0.input_line(p0.extract(ARSENAL_JERSEY))
        self.assertIn("NOT APPLICABLE", line)
        self.assertIn("Absent by design", line)

    def test_footwear_without_a_color_option_escalates_rather_than_defaults(self):
        broken = {"handle": "x", "options": [{"name": "Adult Shoe Size", "values": ["M 9"]}],
                  "variants": []}
        facts = p0.extract(broken)
        self.assertIsNone(facts["colorway"])
        self.assertFalse(facts["colorway_absent_by_design"])
        self.assertIn("Escalate", p0.input_line(facts))

    def test_multi_token_manufacturer_colorway_survives_intact(self):
        self.assertEqual(p0.extract_colorway(HAALAND), "Laser Orange/Blue Void/Lemon Venom")

    def test_colorway_is_never_taken_from_handle_or_pack_name(self):
        """The handle says 'neon-tide' and 'black'; neither may leak into colorway."""
        self.assertEqual(p0.extract_colorway(JR_TEKELA), "Metallic Blue with Alkaline Green")
        self.assertNotIn("Neon", p0.extract_colorway(JR_TEKELA))
        self.assertEqual(p0.extract_colorway(UF1F3ZB), "Black")  # not "Black Pack"


class SkuVerificationTests(unittest.TestCase):
    def test_base_sku_is_recovered_from_variant_skus(self):
        self.assertEqual(p0.base_skus(UF1F16X), ["UF1F16X"])
        self.assertEqual(p0.base_skus(JR_TEKELA), ["YT3FL1NM"])

    def test_matching_sku_verifies(self):
        self.assertEqual(p0.verify_sku("UF1F16X", UF1F16X), "UF1F16X")

    def test_sku_verification_is_case_insensitive(self):
        self.assertEqual(p0.verify_sku("uf1f16x", UF1F16X), "UF1F16X")

    def test_wrong_sku_raises_rather_than_warning(self):
        """Handing UF1F16X's SKU to its colorway sibling must FAIL, not pass.
        This is the check that separates the pair by more than the title."""
        with self.assertRaises(p0.SkuMismatch):
            p0.verify_sku("UF1F16X", UF1F3ZB)

    def test_page_with_no_variant_skus_raises_rather_than_silently_passing(self):
        with self.assertRaises(p0.SkuMismatch):
            p0.verify_sku("ANY", {"handle": "h", "options": [], "variants": []})

    def test_extract_propagates_the_mismatch(self):
        with self.assertRaises(p0.SkuMismatch):
            p0.extract(UF1F3ZB, expected_sku="UF1F16X")

    def test_extract_records_the_verified_sku_on_success(self):
        self.assertEqual(p0.extract(UF1F3ZB, expected_sku="UF1F3ZB")["verified_sku"], "UF1F3ZB")


class SizeOptionTests(unittest.TestCase):
    def test_size_option_is_not_confused_with_color(self):
        self.assertEqual(p0.size_option(UF1F16X)[0], "Adult Shoe Size")
        self.assertEqual(p0.size_option(ARSENAL_JERSEY)[0], "Men's Apparel Size")

    def test_youth_ladder_is_footwear_not_apparel(self):
        self.assertFalse(p0.is_apparel(JR_TEKELA))


if __name__ == "__main__":
    unittest.main(verbosity=2)
