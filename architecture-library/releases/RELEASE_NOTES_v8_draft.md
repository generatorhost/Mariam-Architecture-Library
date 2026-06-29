# Release Notes - Mariam Architecture Library v8 draft

**Version:** v8 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V8-DRAFT

## What Was Added In v8
- Added Book 03.06 - DNA Operating System under Volume 03 Master Blueprint.
- Added DNA Operating System README and INDEX.
- Added 20 subsystem blueprint files covering the major architecture boundaries for DNA Operating System.
- Updated Volume 03 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE to include Book 03.06 .
- Added PDF build target for `Volume_03_Book_03_06_DNA_Operating_System_v8_draft.pdf`.
- Added v8 ZIP package generation.

## Artifact Counts
- Markdown files: 204
- PDF files: 9
- ZIP package: `Mariam_Architecture_Library_v8_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v8 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Book 03.06 Markdown exists and is included in the ZIP.
- Book 03.06 PDF exists and is readable.
- `MANIFEST.json` reports v8 draft artifacts.
- The v8 ZIP contains the Book 03.06 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v8 draft | 2026-06-29 | Draft | Added the DNA Operating System blueprint package. |
