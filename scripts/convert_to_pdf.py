"""Convert docx to pdf using Microsoft Word COM with explicit dialog suppression."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pythoncom
import win32com.client as win32

REPO = Path(__file__).resolve().parent.parent
DOCX = (REPO / "deliverables" / "strategy-presentations"
        / "2026-04_seo-goals-presentation-for-tony.docx").resolve()
PDF = (REPO / "deliverables" / "strategy-presentations"
       / "2026-04_seo-goals-presentation-for-tony.pdf").resolve()

# Word constants
wdFormatPDF = 17
wdDoNotSaveChanges = 0
wdExportFormatPDF = 17
wdAlertsNone = 0


def main() -> int:
    if not DOCX.exists():
        print(f"DOCX not found: {DOCX}")
        return 1
    # Remove any prior output to avoid "already exists" dialogs
    if PDF.exists():
        PDF.unlink()

    pythoncom.CoInitialize()
    word = win32.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = wdAlertsNone
    doc = None
    try:
        doc = word.Documents.Open(
            str(DOCX),
            ReadOnly=True,
            AddToRecentFiles=False,
            ConfirmConversions=False,
            Visible=False,
        )
        doc.ExportAsFixedFormat(
            OutputFileName=str(PDF),
            ExportFormat=wdExportFormatPDF,
            OpenAfterExport=False,
            OptimizeFor=0,  # wdExportOptimizeForPrint
            BitmapMissingFonts=True,
            UseISO19005_1=False,
        )
        print(f"PDF saved: {PDF}")
        # Also report page count while Word has the doc open
        try:
            pages = doc.ComputeStatistics(2)  # wdStatisticPages
            print(f"PAGE_COUNT={pages}")
        except Exception as e:
            print(f"Could not read page count: {e}")
        return 0
    finally:
        if doc is not None:
            doc.Close(SaveChanges=wdDoNotSaveChanges)
        word.Quit(SaveChanges=wdDoNotSaveChanges)
        pythoncom.CoUninitialize()


if __name__ == "__main__":
    sys.exit(main())
