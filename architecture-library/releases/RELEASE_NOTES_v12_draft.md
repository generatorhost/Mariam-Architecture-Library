# Release Notes - Mariam Architecture Library v12 draft

**Version:** v12 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V12-DRAFT

## What Was Added In v12
- Added Book 03.10 - Model Ecosystem under Volume 03 Master Blueprint.
- Added Model Ecosystem README and INDEX.
- Added 20 subsystem blueprint files covering the major architecture boundaries for Model Ecosystem.
- Updated Volume 03 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE to include Book 03.10 .
- Added PDF build target for `Volume_03_Book_03_10_Model_Ecosystem_v12_draft.pdf`.
- Added v12 ZIP package generation.

## Artifact Counts
- Markdown files: 296
- PDF files: 13
- ZIP package: `Mariam_Architecture_Library_v12_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v12 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Book 03.10 Markdown exists and is included in the ZIP.
- Book 03.10 PDF exists and is readable.
- `MANIFEST.json` reports v12 draft artifacts.
- The v12 ZIP contains the Book 03.10 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v12 draft | 2026-06-29 | Draft | Added the Model Ecosystem blueprint package. |
