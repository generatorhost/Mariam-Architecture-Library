# Release Notes - Mariam Architecture Library v17 draft

**Version:** v17 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V17-DRAFT

## What Was Added In v17
- Added Book 03.15 - Opportunity Intelligence under Volume 03 Master Blueprint.
- Added Opportunity Intelligence README and INDEX.
- Added 20 subsystem blueprint files covering the major architecture boundaries for Opportunity Intelligence.
- Updated Volume 03 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE to include Book 03.15 .
- Added PDF build target for `Volume_03_Book_03_15_Opportunity_Intelligence_v17_draft.pdf`.
- Added v17 ZIP package generation.

## Artifact Counts
- Markdown files: 411
- PDF files: 18
- ZIP package: `Mariam_Architecture_Library_v17_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v17 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Book 03.15 Markdown exists and is included in the ZIP.
- Book 03.15 PDF exists and is readable.
- `MANIFEST.json` reports v17 draft artifacts.
- The v17 ZIP contains the Book 03.15 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v17 draft | 2026-06-29 | Draft | Added the Opportunity Intelligence blueprint package. |
