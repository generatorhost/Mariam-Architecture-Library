# Release Notes - Mariam Architecture Library v22 draft

**Version:** v22 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V22-DRAFT

## What Was Added In v22
- Added Book 03.20 - Autonomous Enterprise under Volume 03 Master Blueprint.
- Added Autonomous Enterprise README and INDEX.
- Added 20 subsystem blueprint files covering the major architecture boundaries for Autonomous Enterprise.
- Updated Volume 03 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE to include Book 03.20 .
- Added PDF build target for `Volume_03_Book_03_20_Autonomous_Enterprise_v22_draft.pdf`.
- Added v22 ZIP package generation.

## Artifact Counts
- Markdown files: 526
- PDF files: 23
- ZIP package: `Mariam_Architecture_Library_v22_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v22 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Book 03.20 Markdown exists and is included in the ZIP.
- Book 03.20 PDF exists and is readable.
- `MANIFEST.json` reports v22 draft artifacts.
- The v22 ZIP contains the Book 03.20 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v22 draft | 2026-06-29 | Draft | Added the Autonomous Enterprise blueprint package. |
