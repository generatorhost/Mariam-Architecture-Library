# Release Notes - Mariam Architecture Library v21 draft

**Version:** v21 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V21-DRAFT

## What Was Added In v21
- Added Book 03.19 - Infrastructure under Volume 03 Master Blueprint.
- Added Infrastructure README and INDEX.
- Added 20 subsystem blueprint files covering the major architecture boundaries for Infrastructure.
- Updated Volume 03 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE to include Book 03.19 .
- Added PDF build target for `Volume_03_Book_03_19_Infrastructure_v21_draft.pdf`.
- Added v21 ZIP package generation.

## Artifact Counts
- Markdown files: 503
- PDF files: 22
- ZIP package: `Mariam_Architecture_Library_v21_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v21 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Book 03.19 Markdown exists and is included in the ZIP.
- Book 03.19 PDF exists and is readable.
- `MANIFEST.json` reports v21 draft artifacts.
- The v21 ZIP contains the Book 03.19 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v21 draft | 2026-06-29 | Draft | Added the Infrastructure blueprint package. |
