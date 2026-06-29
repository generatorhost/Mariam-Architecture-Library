# Release Notes - Mariam Architecture Library v14 draft

**Version:** v14 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V14-DRAFT

## What Was Added In v14
- Added Book 03.12 - Plugin Runtime under Volume 03 Master Blueprint.
- Added Plugin Runtime README and INDEX.
- Added 20 subsystem blueprint files covering the major architecture boundaries for Plugin Runtime.
- Updated Volume 03 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE to include Book 03.12 .
- Added PDF build target for `Volume_03_Book_03_12_Plugin_Runtime_v14_draft.pdf`.
- Added v14 ZIP package generation.

## Artifact Counts
- Markdown files: 342
- PDF files: 15
- ZIP package: `Mariam_Architecture_Library_v14_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v14 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Book 03.12 Markdown exists and is included in the ZIP.
- Book 03.12 PDF exists and is readable.
- `MANIFEST.json` reports v14 draft artifacts.
- The v14 ZIP contains the Book 03.12 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v14 draft | 2026-06-29 | Draft | Added the Plugin Runtime blueprint package. |
