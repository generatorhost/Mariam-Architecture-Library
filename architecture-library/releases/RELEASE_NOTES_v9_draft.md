# Release Notes - Mariam Architecture Library v9 draft

**Version:** v9 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V9-DRAFT

## What Was Added In v9
- Added Book 03.07 - Runtime Ecosystem under Volume 03 Master Blueprint.
- Added Runtime Ecosystem README and INDEX.
- Added 20 subsystem blueprint files covering the major architecture boundaries for Runtime Ecosystem.
- Updated Volume 03 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE to include Book 03.07 .
- Added PDF build target for `Volume_03_Book_03_07_Runtime_Ecosystem_v9_draft.pdf`.
- Added v9 ZIP package generation.

## Artifact Counts
- Markdown files: 227
- PDF files: 10
- ZIP package: `Mariam_Architecture_Library_v9_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v9 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Book 03.07 Markdown exists and is included in the ZIP.
- Book 03.07 PDF exists and is readable.
- `MANIFEST.json` reports v9 draft artifacts.
- The v9 ZIP contains the Book 03.07 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v9 draft | 2026-06-29 | Draft | Added the Runtime Ecosystem blueprint package. |
