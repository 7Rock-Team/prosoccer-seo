#!/usr/bin/env python3
"""Regression tests for scripts/build_ceded_terms.py, built from REAL past defects.

Origin of this file (2026-08-26, Mike): `build_ceded_terms.py` was hardened on
2026-08-21 to REQUIRE `--date` rather than default it, because a defaulted date
silently rewrote the recording date of every derived row. That hardening is real and
test_requires_date below proves it works.

It is also insufficient, and Batch 15.1 proved that the hard way. Recording six new
Sparkfusion cedes on 2026-08-25 meant running with `--date 2026-08-25`, an honest and
current date. That run rewrote the recording date of all 24 PRE-EXISTING derived rows
from their real 2026-08-03. Byte-identical content, only the dates moved, so the diff
read as an ordinary update. It was caught only by diffing the regenerated file against
the committed one, which means the tool still depends on a human remembering to diff.

The lesson, codified as `context/workforce-conventions.md` codification checklist item
11: A GUARD THAT FORCES AN INPUT IS NOT A GUARD THAT VALIDATES IT. Requiring --date
converts a silent default into a visible argument; it does not make the argument
correct. Ask of every required-argument guard: what happens if the caller passes a
plausible but WRONG value? Here, the same silent corruption the guard was added to
prevent.

    QUARANTINED, NOT IGNORED (2026-08-26, Mike). The two tests naming the open defect
    are marked `@unittest.expectedFailure` and renamed to carry B-PROV-01 in the test
    NAME, so the suite runs GREEN and the pending work is visible in the run output
    rather than buried in this docstring:

        test_PENDING_B_PROV_01_idempotent_under_any_date
        test_PENDING_B_PROV_01_existing_row_dates_survive_a_later_run

    Why quarantine rather than leave them red: a red suite teaches everyone to ignore
    failures, which is the broken-window problem the codification checklist already
    warns about. An expected-failure is a claim with a deadline; a red suite is noise.
    If either test starts PASSING, unittest reports an UNEXPECTED SUCCESS and the run
    goes non-zero, which is the signal that the fix landed and the decorator and the
    PENDING prefix should both come off.

    Do not "fix" them by relaxing the assertion. They go green when per-row
    provenance lands: inline `term@YYYY-MM-DD` inside `ceded_from`, so the generator
    reads each term's own recorded date and `--date` applies ONLY to terms that
    carry none (the genuinely-new case, the one where a run-time date is correct).
    Tracked as sprint-backlog B-PROV-01. Approved shape: B (inline), because the
    parallel-column shape creates the very drift class it would be removed to fix.
"""
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_SCRIPT = _THIS_DIR / "build_ceded_terms.py"

COLL_REL = Path("deliverables/tracking/collections-master.csv")
CEDED_REL = Path("deliverables/tracking/ceded-terms.csv")

COLL_HEADER = "url,ceded_from,status\n"
COLL_ROWS = (
    "/collections/adidas-f50,adidas f50 sparkfusion; f50 sparkfusion,inherited\n"
    "/collections/arsenal,arsenal jersey; arsenal soccer jersey,optimized\n"
)

# A ceded-terms.csv as it would sit in git: derived rows carrying the date they were
# ACTUALLY recorded, plus one preserved non-collection cede the script must not touch.
CEDED_SEEDED = (
    "term,normalized_term,ceded_to_url,source_file,date\n"
    "f50 messi,f50 messi,the SENIOR F50 Messi PDP,some/session/file.txt,2026-07-13\n"
    "adidas f50 sparkfusion,adidas f50 sparkfusion,/collections/adidas-f50,"
    "collections-master.csv (derived),2026-08-03\n"
    "f50 sparkfusion,f50 sparkfusion,/collections/adidas-f50,"
    "collections-master.csv (derived),2026-08-03\n"
    "arsenal jersey,arsenal jersey,/collections/arsenal,"
    "collections-master.csv (derived),2026-08-03\n"
    "arsenal soccer jersey,arsenal soccer jersey,/collections/arsenal,"
    "collections-master.csv (derived),2026-08-03\n"
)


class CededTermsTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="ceded-test-")
        self.root = Path(self.tmp)
        (self.root / COLL_REL.parent).mkdir(parents=True, exist_ok=True)
        (self.root / COLL_REL).write_text(COLL_HEADER + COLL_ROWS, encoding="utf-8")
        (self.root / CEDED_REL).write_text(CEDED_SEEDED, encoding="utf-8")

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def run_script(self, *args):
        return subprocess.run(
            [sys.executable, str(_SCRIPT), *args],
            cwd=self.tmp, capture_output=True, text=True, encoding="utf-8",
        )

    def ceded_text(self):
        return (self.root / CEDED_REL).read_text(encoding="utf-8")

    # ---- the guard that DOES work -------------------------------------------------

    def test_requires_date(self):
        """A bare run must refuse rather than default. This is the 2026-08-21 hardening."""
        r = self.run_script()
        self.assertNotEqual(r.returncode, 0, "bare run should refuse, not proceed")
        self.assertIn("--date", (r.stdout + r.stderr))

    def test_rejects_malformed_date(self):
        r = self.run_script("--date", "08/26/2026")
        self.assertNotEqual(r.returncode, 0, "malformed date should refuse")

    def test_preserves_non_collection_cedes(self):
        """Cedes whose target is not a /collections/ URL have no collection home and
        must survive verbatim, including their own date."""
        r = self.run_script("--date", "2026-08-03")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        out = self.ceded_text()
        self.assertIn("f50 messi,f50 messi,the SENIOR F50 Messi PDP", out)
        self.assertIn("2026-07-13", out, "preserved row must keep its own recorded date")

    # ---- the guard that does NOT work: known-failing, and that is the point --------

    @unittest.expectedFailure  # B-PROV-01: goes green when inline term@date lands
    def test_PENDING_B_PROV_01_idempotent_under_any_date(self):
        """Regenerating with NO new cedes must produce a byte-identical file under ANY
        --date. Nothing about the underlying facts changed, so nothing in the output
        should change.

        FAILS TODAY: --date is applied to every derived row at regeneration time, so
        the recording dates of rows recorded weeks ago move to whatever date this run
        happens to pass. See the module docstring. B-PROV-01.
        """
        first = self.run_script("--date", "2026-08-03")
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        baseline = self.ceded_text()

        second = self.run_script("--date", "2026-09-15")
        self.assertEqual(second.returncode, 0, second.stdout + second.stderr)

        self.assertEqual(
            baseline, self.ceded_text(),
            "regenerating with no new cedes changed the file. A different --date "
            "rewrote the recording date of rows whose underlying cede did not change. "
            "Per-row provenance (inline term@YYYY-MM-DD) is the fix, not a stricter flag.",
        )

    @unittest.expectedFailure  # B-PROV-01: goes green when inline term@date lands
    def test_PENDING_B_PROV_01_existing_row_dates_survive_a_later_run(self):
        """The Batch 15.1 case exactly: a run passing an HONEST current date, made to
        record NEW cedes, must not rewrite the dates of the rows already recorded.

        FAILS TODAY. B-PROV-01.
        """
        # Author adds a sixth cede to the source of truth and regenerates "today".
        (self.root / COLL_REL).write_text(
            COLL_HEADER
            + "/collections/adidas-f50,adidas f50 sparkfusion; f50 sparkfusion; "
              "adidas womens f50 sparkfusion,inherited\n"
            + "/collections/arsenal,arsenal jersey; arsenal soccer jersey,optimized\n",
            encoding="utf-8",
        )
        r = self.run_script("--date", "2026-08-26")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        out = self.ceded_text()

        self.assertIn(
            "adidas womens f50 sparkfusion,adidas womens f50 sparkfusion,"
            "/collections/adidas-f50,collections-master.csv (derived),2026-08-26",
            out,
            "the genuinely NEW cede should carry the run date",
        )
        for old in ("arsenal jersey", "arsenal soccer jersey"):
            row = next(l for l in out.splitlines() if l.startswith(old + ","))
            self.assertTrue(
                row.endswith("2026-08-03"),
                f"pre-existing cede {old!r} had its recorded date rewritten to the run "
                f"date. Row: {row!r}",
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
