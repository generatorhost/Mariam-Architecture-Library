# Release Notes - Mariam Architecture Library v13 draft

**Version:** v13 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V13-DRAFT

## What Was Added In v13
- Added Book 03.11 - Provider Ecosystem under Volume 03 Master Blueprint.
- Added Provider Ecosystem README and INDEX.
- Added 20 subsystem blueprint files covering the major architecture boundaries for Provider Ecosystem.
- Updated Volume 03 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE to include Book 03.11 .
- Added PDF build target for `Volume_03_Book_03_11_Provider_Ecosystem_v13_draft.pdf`.
- Added v13 ZIP package generation.

## Artifact Counts
- Markdown files: 319
- PDF files: 14
- ZIP package: `Mariam_Architecture_Library_v13_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v13 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Book 03.11 Markdown exists and is included in the ZIP.
- Book 03.11 PDF exists and is readable.
- `MANIFEST.json` reports v13 draft artifacts.
- The v13 ZIP contains the Book 03.11 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v13 draft | 2026-06-29 | Draft | Added the Provider Ecosystem blueprint package. |
