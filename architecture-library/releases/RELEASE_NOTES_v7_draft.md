# Release Notes - Mariam Architecture Library v7 draft

**Version:** v7 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V7-DRAFT

## What Was Added In v7
- Added Book 03.05 - Capability System under Volume 03 Master Blueprint.
- Added Capability System README and INDEX.
- Added 20 subsystem blueprint files covering capability graph, registry, discovery, matching, ranking, requirements, dependencies, lifecycle, DNA, benchmarks, quality, governance, security, events, storage, metrics, testing, acceptance, and roadmap.
- Updated Volume 03 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE to include Book 03.05.
- Added PDF build target for `Volume_03_Book_03_05_Capability_System_v7_draft.pdf`.
- Added v7 ZIP package generation.

## Artifact Counts
- Markdown files: 181
- PDF files: 8
- ZIP package: `Mariam_Architecture_Library_v7_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v7 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Book 03.05 Markdown exists and is included in the ZIP.
- Book 03.05 PDF exists and is readable.
- `MANIFEST.json` reports v7 draft artifacts.
- The v7 ZIP contains the Book 03.05 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v7 draft | 2026-06-29 | Draft | Added the Capability System blueprint package. |
