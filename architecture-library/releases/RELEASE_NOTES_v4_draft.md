# Release Notes - Mariam Architecture Library v4 draft

**Version:** v4 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V4-DRAFT

## What Was Added In v4
- Added Book 03.02 - Enterprise Organization under Volume 03 Master Blueprint.
- Added Enterprise Organization README and INDEX.
- Added 20 subsystem blueprint files covering enterprise structure, board governance, chief office, departments, missions, roles, decision flow, escalation, approval lines, cross-department coordination, KPIs, operating rhythm, governance checkpoints, organization events, organization storage, organization security, organization testing, organization acceptance, and organization roadmap.
- Updated Volume 03 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE to include Book 03.02.
- Added PDF build target for `Volume_03_Book_03_02_Enterprise_Organization_v4_draft.pdf`.
- Added v4 ZIP package generation.

## Artifact Counts
- Markdown files: 112
- PDF files: 5
- ZIP package: `Mariam_Architecture_Library_v4_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v4 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Book 03.02 Markdown exists and is included in the ZIP.
- Book 03.02 PDF exists and is readable.
- `MANIFEST.json` reports v4 draft artifacts.
- The v4 ZIP contains the Book 03.02 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v4 draft | 2026-06-29 | Draft | Added the Enterprise Organization blueprint package. |
