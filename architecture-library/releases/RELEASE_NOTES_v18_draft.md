# Release Notes - Mariam Architecture Library v18 draft

**Version:** v18 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V18-DRAFT

## What Was Added In v18
- Added Book 03.16 - Freelance Automation under Volume 03 Master Blueprint.
- Added Freelance Automation README and INDEX.
- Added 20 subsystem blueprint files covering the major architecture boundaries for Freelance Automation.
- Updated Volume 03 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE to include Book 03.16 .
- Added PDF build target for `Volume_03_Book_03_16_Freelance_Automation_v18_draft.pdf`.
- Added v18 ZIP package generation.

## Artifact Counts
- Markdown files: 434
- PDF files: 19
- ZIP package: `Mariam_Architecture_Library_v18_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v18 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Book 03.16 Markdown exists and is included in the ZIP.
- Book 03.16 PDF exists and is readable.
- `MANIFEST.json` reports v18 draft artifacts.
- The v18 ZIP contains the Book 03.16 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v18 draft | 2026-06-29 | Draft | Added the Freelance Automation blueprint package. |
