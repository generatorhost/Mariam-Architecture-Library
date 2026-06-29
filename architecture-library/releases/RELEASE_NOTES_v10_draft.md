# Release Notes - Mariam Architecture Library v10 draft

**Version:** v10 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V10-DRAFT

## What Was Added In v10
- Added Book 03.08 - Workflow System under Volume 03 Master Blueprint.
- Added Workflow System README and INDEX.
- Added 20 subsystem blueprint files covering the major architecture boundaries for Workflow System.
- Updated Volume 03 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE to include Book 03.08 .
- Added PDF build target for `Volume_03_Book_03_08_Workflow_System_v10_draft.pdf`.
- Added v10 ZIP package generation.

## Artifact Counts
- Markdown files: 250
- PDF files: 11
- ZIP package: `Mariam_Architecture_Library_v10_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v10 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Book 03.08 Markdown exists and is included in the ZIP.
- Book 03.08 PDF exists and is readable.
- `MANIFEST.json` reports v10 draft artifacts.
- The v10 ZIP contains the Book 03.08 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v10 draft | 2026-06-29 | Draft | Added the Workflow System blueprint package. |
