#!/usr/bin/env python3
"""Regression tests for scripts/batch_gate.py, built from REAL past defects.

Each historical defect class the human gate used to catch by hand gets a test that
proves batch_gate.py catches it deterministically. This is the proof the prompt
requires before any human gate is cut (Change 1): if a defect class here ever stops
being caught, this suite fails and the gate is not safe to rely on.

Defect classes covered (with their production origin):
  - KK3725  casing:    lowercase editorial body H2s (Batch 4)          -> voice reuse
  - KI0586  headings:  #### body-section headers, one level too deep (Batch 5)
  - DR Congo FIFA:     "FIFA World Cup 2026" in body on a non-adidas page (Batch 6)
  - Shadow  "gone":    barred motif token reused; "sees coming" title-frame (Batch 6)
  - IF8512  word-band: Pro-tier SKU carrying the exemplar's Elite word band (Batch 6)
  - IF8512  hedge:     hedge word next to a (fabricated) weight spec (Batch 6)
Plus: adidas FIFA-permitted negative, cross-brief convergence, cannibalization,
price-in-body, clean-brief PASS, and honest skip when an input file is absent.
"""
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

import batch_gate as bg  # noqa: E402


DEFAULT_META = {
    "sku": "SKU0",
    "brand": "nike",
    "brand_ip_posture": "cycle-language-only",
    "tier": "pro",
    "word_band": [340, 390],
    "word_band_tolerance": 15,
    "primary_keyword": "nike test cleat",
    "forbidden_phrasings": {"verbatim": [], "motifs": [], "title_frames": []},
}


def _para(nwords: int, word: str = "control") -> str:
    """A paragraph of exactly nwords plain word tokens (no forbidden content)."""
    return " ".join([word] * nwords) + "."


def make_brief(
    *,
    short_desc="The ball settles under your foot before the defender can set. That is what this cleat is for.",
    body_sections=None,
    meta_title="Nike Test Cleat FG Soccer Cleats",
    meta_desc="A clean first touch, a locked-in fit, firm-ground grip. Shop the pack.",
    complete=False,
):
    """Build a minimal but structurally real PDP brief. body_sections is a list of
    (h2_line, prose_line) tuples for the Description body; defaults to one clean
    sentence-case section.

    complete=False (default) keeps the historical minimal shape so the existing
    word-band / voice / claims fixtures are byte-for-byte unchanged. complete=True adds
    the full required PDP section set (Fit Notes, Care and Maintenance, a FAQ whose
    answer carries the required internal link, and an Image Alt Text field) so a brief
    can genuinely PASS check_section_presence. The link lives in the FAQ answer, after
    the editorial region, so it never becomes the cross-brief 'closing' line."""
    if body_sections is None:
        # Default body is realistically sized (~360 words) so a default brief is
        # genuinely in-band; explicit word-band tests override body_sections. The
        # padding word varies by caller so distinct briefs do not trip cross-brief
        # overlap in the fully-clean batch test.
        body_sections = [("## Built for the player who reads the game",
                          "This cleat is built for the player who wins the half-second "
                          "after the ball arrives. " + _para(320))]
    lines = [
        "# Nike Test Cleat -- PDP Optimization",
        "",
        "## Quick Reference",
        "- SKU: SKU0",
        "- Current live Title (for Shopify admin search): Nike Test Cleat FG",
        "- URL: https://www.prosoccer.com/products/nike-test-cleat-fg",
        "",
        "## SEO Details (copy-paste into Shopify)",
        "",
        "### Keywords",
        "",
        "| Type | Keyword | Volume | Difficulty |",
        "|---|---|---|---|",
        "| Primary | nike test cleat |  |  |",
        "",
        "### Title (Shopify \"Title\" field)",
        "Nike Test Cleat Firm Ground Soccer Cleats",
        "",
        "### Short Description (metafield, hero block above Add to Cart)",
        short_desc,
        "",
        "### Description (body_html, accordion below product images)",
        "",
    ]
    for h2, prose in body_sections:
        lines += [h2, "", prose, ""]
    lines += [
        "## Product Details: Test Cleat",
        "- Synthetic upper with a lightweight mesh midfoot",
        "- Firm-ground plate with conical studs",
        "",
    ]
    if complete:
        lines += [
            "## Fit Notes",
            "Runs true to size with a snug midfoot; size up for a wider foot.",
            "",
            "## Care and Maintenance",
            "- Wipe the upper with a damp cloth after play",
            "- Air-dry away from direct heat, never in the dryer",
            "",
            "## FAQs about Test Cleat",
            "### Do these run true to size?",
            "Yes, true to size for most players. Compare the "
            "[test collection](https://www.prosoccer.com/collections/test-collection) for other widths.",
            "",
        ]
    lines += [
        "### Meta Title (Search engine listing)",
        meta_title,
        "",
        "### Meta Description (Search engine listing)",
        meta_desc,
        "",
        "### URL Handle",
        "nike-test-cleat-fg-soccer-cleats",
        "",
    ]
    if complete:
        lines += [
            "### Image Alt Text",
            "- Nike Test Cleat firm ground soccer cleats front view",
            "- Nike Test Cleat side profile on grass",
            "",
        ]
    lines += [
        "### Taxonomy Category (Shopify admin)",
        "Apparel & Accessories > Shoes > Athletic Shoes > Soccer Cleats",
    ]
    return "\n".join(lines)


class GateTestBase(unittest.TestCase):
    def setUp(self):
        self.dir = Path(tempfile.mkdtemp(prefix="batch_gate_test_"))
        (self.dir / "inputs").mkdir()

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def write_brief(self, sku, text, slug="test"):
        (self.dir / f"{sku}_{slug}_brief.md").write_text(text, encoding="utf-8")

    def write_input(self, sku, meta):
        m = dict(DEFAULT_META)
        m.update(meta)
        m["sku"] = sku
        block = "```gate-meta\n" + json.dumps(m, indent=2) + "\n```\n"
        (self.dir / "inputs" / f"{sku}_input.md").write_text(
            f"# Input for {sku}\n\n{block}\nHuman-readable lane notes here.\n",
            encoding="utf-8",
        )

    def findings(self):
        """Run the full gate over the session and return the flat Finding list."""
        briefs = bg.discover_briefs(self.dir)
        registry1 = bg.load_registry1_primaries(self.dir)
        all_findings, briefs_meta, briefs_data = [], [], []
        for path in briefs:
            sku = bg.sku_from_brief(path)
            meta = bg.load_input_meta(self.dir, sku)
            briefs_meta.append((sku, meta))
            f, _ = bg.gate_brief(sku, path, meta)
            all_findings += f
            lines = path.read_text(encoding="utf-8").splitlines()
            briefs_data.append({"sku": sku, "lines": lines, "meta": meta,
                                "opening": bg.brief_opening(lines),
                                "closing": bg.brief_closing(lines)})
        all_findings += bg.check_cannibalization(briefs_meta, registry1)
        all_findings += bg.check_cross_brief(briefs_data)
        return all_findings

    def checks_present(self):
        return {f.check for f in self.findings()}

    def exit_code(self):
        return bg.run(self.dir)


class TestKK3725Casing(GateTestBase):
    """Batch 4: three lowercase editorial body H2s shipped past both human gates."""

    def test_lowercase_body_h2_flagged_via_voice_reuse(self):
        self.write_brief("KK3725", make_brief(body_sections=[
            ("## the everyday cleat that keeps up with a busy player",
             "It keeps up with the player who never stops moving."),
            ("## What the player actually gets on the pitch",
             "A locked-in fit and a clean strike surface."),
        ]))
        self.write_input("KK3725", {})
        checks = self.checks_present()
        self.assertIn("voice", checks, "lowercase body H2 must surface via voice reuse")
        self.assertEqual(self.exit_code(), 2, "hard defect -> exit 2")

    def test_clean_casing_passes(self):
        self.write_brief("KK3725", make_brief())
        self.write_input("KK3725", {})
        self.assertNotIn("voice", self.checks_present())


class TestKI0586Headings(GateTestBase):
    """Batch 5: #### body-section headers (one level too deep) slipped past the
    ##-only casing check. batch_gate flags heading depth directly."""

    def test_h4_body_headers_flagged(self):
        self.write_brief("KI0586", make_brief(body_sections=[
            ("#### The first touch that buys you a half-second",
             "Some players win games with pace."),
            ("#### Built for the player who runs the tempo",
             "This is a number 8's cleat."),
        ]))
        self.write_input("KI0586", {})
        fs = [f for f in self.findings() if f.check == "heading-level"]
        self.assertEqual(len(fs), 2, f"both #### body headers must be flagged, got {fs}")
        self.assertTrue(all(f.severity == bg.FAIL for f in fs))
        self.assertEqual(self.exit_code(), 2)

    def test_h5_body_header_flagged(self):
        self.write_brief("KI0586", make_brief(body_sections=[
            ("##### Way too deep a header", "Prose under a level-5 header."),
        ]))
        self.write_input("KI0586", {})
        self.assertIn("heading-level", self.checks_present())


class TestDRCongoFIFA(GateTestBase):
    """Batch 6: live DR Congo Umbro PDP body read 'worn at the FIFA World Cup 2026' --
    a FIFA-family term on a non-adidas page."""

    def test_fifa_in_body_on_non_adidas_flagged(self):
        self.write_brief("DRCHRM25", make_brief(body_sections=[
            ("## Les Leopards and the sky-blue identity",
             "This is the kit worn at the FIFA World Cup 2026 by the national side."),
        ]))
        self.write_input("DRCHRM25", {"brand": "umbro", "brand_ip_posture": "cycle-language-only"})
        fs = [f for f in self.findings() if f.check == "fifa-terms"]
        self.assertTrue(fs, "FIFA term on a non-adidas page must be flagged")
        self.assertTrue(all(f.severity == bg.FAIL for f in fs))

    def test_adidas_page_fifa_permitted(self):
        """Negative: the exact same body on an adidas 2026 World Cup page is allowed."""
        self.write_brief("KB7474", make_brief(body_sections=[
            ("## Reggae Boyz and the road to the tournament",
             "This is the kit worn at the FIFA World Cup 2026 by the national side."),
        ]))
        self.write_input("KB7474", {"brand": "adidas", "brand_ip_posture": "fifa-permitted"})
        fs = [f for f in self.findings() if f.check == "fifa-terms"]
        self.assertEqual(fs, [], "adidas holds the 2026 World Cup license; the family is permitted here")

    def test_fifa_runs_provisional_without_input(self):
        """A missing input file must NOT let a FIFA leak hide: FIFA still runs, flagged
        provisional (a non-adidas assumption is the safe default)."""
        self.write_brief("DRCARM25", make_brief(body_sections=[
            ("## Away-day roaming", "Worn at the World Cup 2026 on the road."),
        ]))
        # no input file written
        fs = [f for f in self.findings() if f.check == "fifa-terms"]
        self.assertTrue(fs, "FIFA must still be checked when the input file is absent")


class TestShadowConvergence(GateTestBase):
    """Batch 6: the four Shadow cleats converged on a 'gone' payoff word and the
    'The X sees coming' H2 title-frame. Mechanism B carried verbatim strings only;
    Change 5 adds motifs + title-frames, and batch_gate enforces them from the SAME
    per-SKU input-file lists."""

    def test_own_barred_motif_flagged(self):
        self.write_brief("HJ2146", make_brief(
            short_desc="You are already gone before the defender turns his head.",
        ))
        self.write_input("HJ2146", {"forbidden_phrasings": {
            "verbatim": [], "motifs": ["gone"], "title_frames": ["sees coming"]}})
        fs = [f for f in self.findings() if f.check == "forbidden-motif"]
        self.assertTrue(fs, "a brief reusing its own barred motif must be flagged")
        self.assertEqual(self.exit_code(), 2)

    def test_own_barred_title_frame_flagged(self):
        self.write_brief("HJ2146", make_brief(body_sections=[
            ("## The first step nobody sees coming",
             "The half-turn a set defender cannot read."),
        ]))
        self.write_input("HJ2146", {"forbidden_phrasings": {
            "verbatim": [], "motifs": ["gone"], "title_frames": ["sees coming"]}})
        self.assertIn("forbidden-title-frame", self.checks_present())

    def test_own_barred_verbatim_flagged(self):
        self.write_brief("HJ2146", make_brief(body_sections=[
            ("## The pass no one sees coming", "The disguise of the pass."),
        ]))
        self.write_input("HJ2146", {"forbidden_phrasings": {
            "verbatim": ["The pass no one sees coming"], "motifs": [], "title_frames": []}})
        self.assertIn("forbidden-verbatim", self.checks_present())

    def test_cross_brief_shared_motif_flagged(self):
        """Same barred motif recurring across two sibling briefs -> REVIEW convergence.
        The motif vocabulary is the union of the per-SKU input lists (one source of
        truth), not a hardcoded dictionary."""
        self.write_brief("HJ2147", make_brief(
            short_desc="He is already gone from the defender's picture."), slug="a")
        self.write_brief("HJ2146", make_brief(
            short_desc="You are gone before the turn."), slug="b")
        self.write_input("HJ2147", {"forbidden_phrasings": {
            "verbatim": [], "motifs": ["gone"], "title_frames": []}})
        self.write_input("HJ2146", {"forbidden_phrasings": {
            "verbatim": [], "motifs": ["gone"], "title_frames": []}})
        fs = [f for f in self.findings() if f.check == "cross-brief-motif"]
        self.assertTrue(fs, "shared motif across siblings must surface as REVIEW")
        self.assertTrue(all(f.severity == bg.REVIEW for f in fs))


class TestIF8512WordBandAndHedge(GateTestBase):
    """Batch 6: the Vapor 17 PRO Shadow inherited the exemplar's ELITE word band
    (~446 words vs the Pro band 340-390) and carried a fabricated '6.3 oz (180g)'
    weight."""

    def test_word_band_over_flagged(self):
        self.write_brief("IF8512", make_brief(body_sections=[
            ("## The ghosted run", _para(500)),
        ]))
        self.write_input("IF8512", {"tier": "pro", "word_band": [340, 390]})
        fs = [f for f in self.findings() if f.check == "word-band"]
        self.assertTrue(fs, "a Pro-band SKU at ~500 body words must be flagged over-band")
        self.assertEqual(self.exit_code(), 2)

    def test_word_band_within_passes(self):
        self.write_brief("IF8512", make_brief(body_sections=[
            ("## The ghosted run", _para(360)),
        ]))
        self.write_input("IF8512", {"tier": "pro", "word_band": [340, 390]})
        self.assertNotIn("word-band", self.checks_present())

    def test_elite_band_would_have_passed_same_body(self):
        """Proves the band is SKU-specific: the same ~446-word body passes on an Elite
        band but fails on the Pro band it was wrongly given."""
        body = [("## The ghosted run", _para(430))]
        self.write_brief("IF8512", make_brief(body_sections=body))
        self.write_input("IF8512", {"tier": "elite", "word_band": [400, 450]})
        self.assertNotIn("word-band", self.checks_present())

    def test_hedge_near_weight_flagged_review(self):
        self.write_brief("IF8512", make_brief(body_sections=[
            ("## The ghosted run", "The Flyknit build weighs approximately 6.3 oz for a low-cut."),
        ]))
        self.write_input("IF8512", {})
        fs = [f for f in self.findings() if f.check == "fabrication-hedge"]
        self.assertTrue(fs, "hedge word next to a weight spec must surface for review")
        self.assertTrue(all(f.severity == bg.REVIEW for f in fs))


class TestCannibalizationAndPrice(GateTestBase):
    def test_intra_batch_duplicate_primary_flagged(self):
        self.write_brief("HJ2146", make_brief(), slug="a")
        self.write_brief("HJ2147", make_brief(), slug="b")
        self.write_input("HJ2146", {"primary_keyword": "nike phantom 6 elite fg"})
        self.write_input("HJ2147", {"primary_keyword": "nike phantom 6 elite fg"})
        fs = [f for f in self.findings() if f.check == "cannibalization"]
        self.assertTrue(fs, "two SKUs sharing a primary keyword must be flagged")

    def test_registry1_collision_flagged(self):
        self.write_brief("HJ2146", make_brief())
        self.write_input("HJ2146", {"primary_keyword": "nike phantom 6 elite fg"})
        (self.dir / "inputs" / "_registry1_primaries.txt").write_text(
            "nike phantom 6 elite fg\n", encoding="utf-8")
        fs = [f for f in self.findings() if f.check == "cannibalization"]
        self.assertTrue(fs, "a primary already claimed in Registry 1 must be flagged")

    def test_price_in_body_flagged(self):
        self.write_brief("KB7474", make_brief(body_sections=[
            ("## The Authentic tier", "This match-spec kit runs $149.99 at retail."),
        ]))
        self.write_input("KB7474", {})
        self.assertIn("price-in-body", self.checks_present())


class TestCleanAndSkips(GateTestBase):
    def test_fully_clean_batch_passes(self):
        # Two distinct, in-band, defect-free, structurally COMPLETE briefs -> zero
        # findings, exit 0. complete=True so the section-presence check is satisfied
        # too; _para is retuned so the fuller body stays inside the default band.
        self.write_brief("HJ2146", make_brief(
            short_desc="The ball settles under your foot before the defender can set.",
            body_sections=[("## Built for the player who reads the game",
                            "This cleat rewards the player who reads the game a beat early. " + _para(250, "touch"))],
            complete=True,
        ), slug="a")
        self.write_brief("KB7474", make_brief(
            short_desc="The Reggae Boyz identity, in a match-spec away kit for the road.",
            body_sections=[("## Reggae Boyz on the road",
                            "The away kit carries the black-based identity onto foreign turf. " + _para(250, "speed"))],
            meta_title="Jamaica Authentic Away Jersey 2026",
            meta_desc="The Reggae Boyz away kit, match-spec and ready for the cycle.",
            complete=True), slug="b")
        self.write_input("HJ2146", {"primary_keyword": "nike phantom low elite fg"})
        self.write_input("KB7474", {"brand": "adidas", "brand_ip_posture": "fifa-permitted",
                                    "primary_keyword": "jamaica soccer jersey 2026"})
        self.assertEqual(self.exit_code(), 0,
                         f"clean batch must PASS; findings={[f.format() for f in self.findings()]}")

    def test_missing_input_reports_honest_skip(self):
        self.write_brief("HJ2146", make_brief())
        # no input file
        briefs = bg.discover_briefs(self.dir)
        sku = bg.sku_from_brief(briefs[0])
        meta = bg.load_input_meta(self.dir, sku)
        self.assertIsNone(meta)
        _, skipped = bg.gate_brief(sku, briefs[0], meta)
        self.assertTrue(any("no-input" in s for s in skipped),
                        "a missing input file must be reported as a skip, never silent")

    def test_malformed_gate_meta_flagged(self):
        self.write_brief("HJ2146", make_brief())
        (self.dir / "inputs" / "HJ2146_input.md").write_text(
            "# bad\n\n```gate-meta\n{not valid json,}\n```\n", encoding="utf-8")
        self.assertIn("input-file", self.checks_present())


class TestKA6871HeritageCounts(GateTestBase):
    """2026-07-13 claims gate: KA6871's first draft shipped 'among England's most
    successful clubs: 13 Premier League titles, a record 20 English league titles
    (shared with Liverpool)'. Liverpool drew level with Manchester United at 20 English
    league titles in 2024-25, breaking both the 'record 20' count and the 'most
    successful' superlative. The gate that this claim motivated MUST catch this claim."""

    _CLUB_META = {
        "brand": "adidas",
        "brand_ip_posture": "club-kit-premier-league-fa-cup-direct-european-generic",
        "tier": "Stadium", "word_band": [450, 520],
        "primary_keyword": "manchester united home jersey",
    }
    KA6871_CLAIM = ("United sit among England's most successful clubs: 13 Premier League "
                    "titles, a record 20 English league titles overall (shared with "
                    "Liverpool), and European nights the city remembers.")
    QUALITATIVE_FIX = ("United rank among England's most decorated clubs, with FA Cup "
                       "runs the fans still replay and European nights the city remembers.")

    def test_ka6871_original_claim_is_caught(self):
        self.write_brief("KA6871", make_brief(body_sections=[
            ("## Who it's for, and the history in the red",
             self.KA6871_CLAIM + " " + _para(430)),
        ]))
        self.write_input("KA6871", dict(self._CLUB_META))
        checks = self.checks_present()
        self.assertIn("heritage-count", checks,
                      "the '13 Premier League titles' / '20 English league titles' counts "
                      "must be caught -- a claims gate that misses the claim that "
                      "motivated it is not done")
        self.assertIn("heritage-superlative", checks,
                      "'most successful' + 'record 20' superlatives must be caught")
        self.assertEqual(self.exit_code(), 2, "unsourced heritage counts are a hard defect -> exit 2")

    def test_qualitative_fix_passes(self):
        self.write_brief("KA6871", make_brief(body_sections=[
            ("## Who it's for, and the history in the red",
             self.QUALITATIVE_FIX + " " + _para(430)),
        ]))
        self.write_input("KA6871", dict(self._CLUB_META))
        checks = self.checks_present()
        self.assertNotIn("heritage-count", checks,
                         "qualitative honours must not trip the count check")
        self.assertNotIn("heritage-superlative", checks,
                         "'most decorated' is the approved qualitative language and must pass")

    def test_liverpool_analog_counts_caught(self):
        """The identical class on the Liverpool side: '20 English league titles' and
        'six European crowns'."""
        self.write_brief("KB8268", make_brief(body_sections=[
            ("## For the supporter who follows through winter",
             "The Reds hold 20 English league titles, level with Manchester United, plus "
             "six European crowns won on the biggest nights. " + _para(420)),
        ]))
        self.write_input("KB8268", dict(self._CLUB_META,
                                        primary_keyword="liverpool long sleeve jersey"))
        self.assertIn("heritage-count", self.checks_present(),
                      "Liverpool '20 English league titles' + 'six European crowns' must be caught")


class TestSectionPresence(GateTestBase):
    """2026-08-01, codification candidate 4. Two production origins:
      - Batch 9 shipped briefs missing Product Details / Fit Notes / Care / FAQ, caught
        only by accident (the absent prose dragged the word count under band).
      - Batch 10 shipped KC3952 / KB8251 / YT3FL1NM with ZERO internal links; nothing in
        the pipeline checked section presence, so four green reports missed it.
    The gate must now look directly, unconditionally, and hard-fail."""

    _BODY = [("## Built for the player who reads the game",
              "This cleat rewards the player who reads the game a beat early. " + _para(250, "grip"))]

    def _complete(self, **kw):
        kw.setdefault("body_sections", list(self._BODY))
        return make_brief(complete=True, **kw)

    def _section_msgs(self):
        return [f.message for f in self.findings() if f.check == "section-presence"]

    def test_complete_brief_passes(self):
        self.write_brief("HJ2146", self._complete())
        self.write_input("HJ2146", {})
        self.assertEqual([], self._section_msgs(),
                         "a structurally complete PDP brief must raise no section finding")
        self.assertEqual(self.exit_code(), 0)

    def test_missing_internal_link_flagged(self):
        # The exact Batch 10 defect: every section present, zero internal links.
        brief = self._complete().replace(
            "[test collection](https://www.prosoccer.com/collections/test-collection)",
            "our other widths")
        self.write_brief("KC3952", brief)
        self.write_input("KC3952", {})
        msgs = self._section_msgs()
        self.assertTrue(any("internal link" in m for m in msgs),
                        f"a brief with no internal link must be flagged; got {msgs}")
        self.assertEqual(self.exit_code(), 2, "missing internal link is a hard defect -> exit 2")

    def test_missing_fit_notes_flagged(self):
        brief = self._complete().replace(
            "## Fit Notes\nRuns true to size with a snug midfoot; size up for a wider foot.\n\n", "")
        self.write_brief("HJ2146", brief)
        self.write_input("HJ2146", {})
        self.assertTrue(any("Fit Notes" in m for m in self._section_msgs()))
        self.assertEqual(self.exit_code(), 2)

    def test_missing_care_flagged(self):
        brief = self._complete().replace(
            "## Care and Maintenance\n- Wipe the upper with a damp cloth after play\n"
            "- Air-dry away from direct heat, never in the dryer\n\n", "")
        self.write_brief("HJ2146", brief)
        self.write_input("HJ2146", {})
        self.assertTrue(any("Care and Maintenance" in m for m in self._section_msgs()))

    def test_missing_faq_flagged(self):
        brief = self._complete().replace(
            "## FAQs about Test Cleat\n### Do these run true to size?\n"
            "Yes, true to size for most players. Compare the "
            "[test collection](https://www.prosoccer.com/collections/test-collection) for other widths.\n\n", "")
        self.write_brief("HJ2146", brief)
        self.write_input("HJ2146", {})
        msgs = self._section_msgs()
        # FAQ gone takes the only internal link with it: both must fire.
        self.assertTrue(any("FAQ" in m for m in msgs), f"missing FAQ must fire; got {msgs}")
        self.assertEqual(self.exit_code(), 2)

    def test_missing_image_alt_flagged(self):
        brief = self._complete().replace(
            "### Image Alt Text\n- Nike Test Cleat firm ground soccer cleats front view\n"
            "- Nike Test Cleat side profile on grass\n\n", "")
        self.write_brief("HJ2146", brief)
        self.write_input("HJ2146", {})
        self.assertTrue(any("Image Alt Text" in m for m in self._section_msgs()))

    def test_empty_heading_counts_as_missing(self):
        # Fit Notes heading present but no content beneath -> missing, not present.
        brief = self._complete().replace(
            "## Fit Notes\nRuns true to size with a snug midfoot; size up for a wider foot.\n",
            "## Fit Notes\n")
        self.write_brief("HJ2146", brief)
        self.write_input("HJ2146", {})
        msgs = self._section_msgs()
        self.assertTrue(any("Fit Notes" in m and "no content" in m for m in msgs),
                        f"an empty Fit Notes heading must count as missing; got {msgs}")

    def test_missing_editorial_region_flagged(self):
        # Body jumps straight from Description to Product Details: no lead copy.
        self.write_brief("HJ2146", self._complete(body_sections=[]))
        self.write_input("HJ2146", {})
        self.assertTrue(any("editorial" in m for m in self._section_msgs()))
        self.assertEqual(self.exit_code(), 2)

    def test_no_description_body_flagged(self):
        # A file with no '### Description' field at all is maximally broken.
        self.write_brief("HJ2146", "# Broken\n\n## Quick Reference\n- SKU: HJ2146\n")
        self.write_input("HJ2146", {})
        self.assertTrue(any("Description" in m for m in self._section_msgs()))

    def test_runs_without_input_file(self):
        # Unconditional: the check must fire even when the input file is absent (the
        # Batch 10 root cause was an unmet input contract that nothing verified).
        brief = self._complete().replace(
            "[test collection](https://www.prosoccer.com/collections/test-collection)",
            "our other widths")
        self.write_brief("KC3952", brief)  # no input file written
        self.assertTrue(any("internal link" in m for m in self._section_msgs()),
                        "section presence must not depend on the per-SKU input file")


class TestCustomizationClaims(GateTestBase):
    """2026-08-03, failure pattern 1 (SEO_BATCH_PROCESS.md §7). Two customer-facing facts
    shipped wrong across Batch 10 briefs: name/number customization is a PRODUCT-PAGE
    option (briefs said 'at checkout') and it adds BUSINESS DAYS (briefs said '1 to 2
    weeks'). Authoritative: context/shipping-customization-facts.md. Hard FAIL."""

    def _cust_msgs(self):
        return [f.message for f in self.findings() if f.check == "customization-claim"]

    def _brief(self, prose):
        return make_brief(body_sections=[("## Make it yours", prose)])

    def test_at_checkout_flagged(self):
        self.write_brief("KB8251", self._brief(
            "Add a name and number at checkout, such as Virgil 4 or Gakpo 18."))
        self.write_input("KB8251", {})
        msgs = self._cust_msgs()
        self.assertTrue(any("checkout" in m for m in msgs),
                        f"'name and number ... at checkout' must be flagged; got {msgs}")
        self.assertEqual(self.exit_code(), 2, "wrong customization location is a hard defect -> exit 2")

    def test_weeks_duration_flagged(self):
        self.write_brief("KC3947", self._brief(
            "The jersey is customizable with a name and number. Customized orders need an "
            "extra 1 to 2 weeks before they ship."))
        self.write_input("KC3947", {})
        msgs = self._cust_msgs()
        self.assertTrue(any("weeks" in m for m in msgs),
                        f"name/number customization timed in weeks must be flagged; got {msgs}")
        self.assertEqual(self.exit_code(), 2)

    def test_both_errors_in_one_answer_both_fire(self):
        # The exact KC3952 defect: location AND duration wrong in one FAQ answer.
        self.write_brief("KC3952", self._brief(
            "Name and number customization is available at checkout. Customized shirts "
            "need an extra one to two weeks before they ship."))
        self.write_input("KC3952", {})
        msgs = self._cust_msgs()
        self.assertTrue(any("checkout" in m for m in msgs), f"location error missing; {msgs}")
        self.assertTrue(any("weeks" in m for m in msgs), f"duration error missing; {msgs}")

    def test_correct_copy_passes(self):
        # The codified CORRECT line: product page + business days.
        self.write_brief("KC3952", self._brief(
            "Add your name and number right on this page. Name and number orders ship in "
            "about 2 to 3 business days."))
        self.write_input("KC3952", {})
        self.assertEqual([], self._cust_msgs(),
                         "product-page + business-days copy must not be flagged")

    def test_care_line_customized_no_false_positive(self):
        # 'customized name and number' in a care instruction, with no checkout/weeks, is clean.
        self.write_brief("KC3993", self._brief(
            "Wash a customized name and number inside-out and keep it away from direct heat "
            "to protect the print."))
        self.write_input("KC3993", {})
        self.assertEqual([], self._cust_msgs(),
                         "a care-instruction mention of 'customized' must not false-positive")

    def test_runs_without_input_file(self):
        # Unconditional: fires even when the per-SKU input file is absent.
        self.write_brief("KC3952", self._brief(
            "Name and number customization is available at checkout."))  # no input written
        self.assertTrue(any("checkout" in m for m in self._cust_msgs()),
                        "customization check must not depend on the per-SKU input file")


if __name__ == "__main__":
    unittest.main()
