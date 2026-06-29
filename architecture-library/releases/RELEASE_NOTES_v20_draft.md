# Release Notes - Mariam Architecture Library v20 draft

**Version:** v20 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V20-DRAFT

## What Was Added In v20
- Added Book 03.18 - Enterprise Governance under Volume 03 Master Blueprint.
- Added Enterprise Governance README and INDEX.
- Added 20 subsystem blueprint files covering the major architecture boundaries for Enterprise Governance.
- Updated Volume 03 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE to include Book 03.18 .
- Added PDF build target for `Volume_03_Book_03_18_Enterprise_Governance_v20_draft.pdf`.
- Added v20 ZIP package generation.

## Artifact Counts
- Markdown files: 480
- PDF files: 21
- ZIP package: `Mariam_Architecture_Library_v20_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v20 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Book 03.18 Markdown exists and is included in the ZIP.
- Book 03.18 PDF exists and is readable.
- `MANIFEST.json` reports v20 draft artifacts.
- The v20 ZIP contains the Book 03.18 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v20 draft | 2026-06-29 | Draft | Added the Enterprise Governance blueprint package. |
