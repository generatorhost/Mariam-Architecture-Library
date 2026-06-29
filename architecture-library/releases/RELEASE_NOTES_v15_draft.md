# Release Notes - Mariam Architecture Library v15 draft

**Version:** v15 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V15-DRAFT

## What Was Added In v15
- Added Book 03.13 - Connector Runtime under Volume 03 Master Blueprint.
- Added Connector Runtime README and INDEX.
- Added 20 subsystem blueprint files covering the major architecture boundaries for Connector Runtime.
- Updated Volume 03 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE to include Book 03.13 .
- Added PDF build target for `Volume_03_Book_03_13_Connector_Runtime_v15_draft.pdf`.
- Added v15 ZIP package generation.

## Artifact Counts
- Markdown files: 365
- PDF files: 16
- ZIP package: `Mariam_Architecture_Library_v15_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v15 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Book 03.13 Markdown exists and is included in the ZIP.
- Book 03.13 PDF exists and is readable.
- `MANIFEST.json` reports v15 draft artifacts.
- The v15 ZIP contains the Book 03.13 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v15 draft | 2026-06-29 | Draft | Added the Connector Runtime blueprint package. |
