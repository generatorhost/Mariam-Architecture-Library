# Release Notes - Mariam Architecture Library v16 draft

**Version:** v16 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V16-DRAFT

## What Was Added In v16
- Added Book 03.14 - Marketplace under Volume 03 Master Blueprint.
- Added Marketplace README and INDEX.
- Added 20 subsystem blueprint files covering the major architecture boundaries for Marketplace.
- Updated Volume 03 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE to include Book 03.14 .
- Added PDF build target for `Volume_03_Book_03_14_Marketplace_v16_draft.pdf`.
- Added v16 ZIP package generation.

## Artifact Counts
- Markdown files: 388
- PDF files: 17
- ZIP package: `Mariam_Architecture_Library_v16_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v16 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Book 03.14 Markdown exists and is included in the ZIP.
- Book 03.14 PDF exists and is readable.
- `MANIFEST.json` reports v16 draft artifacts.
- The v16 ZIP contains the Book 03.14 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v16 draft | 2026-06-29 | Draft | Added the Marketplace blueprint package. |
