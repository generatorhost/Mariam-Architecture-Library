# Release Notes - Mariam Architecture Library v6 draft

**Version:** v6 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V6-DRAFT

## What Was Added In v6
- Added Book 03.04 - Knowledge System under Volume 03 Master Blueprint.
- Added Knowledge System README and INDEX.
- Added 20 subsystem blueprint files covering knowledge graph, knowledge store, document intelligence, memory system, vector store, embedding system, semantic search, knowledge indexing, knowledge versioning, knowledge ingestion, knowledge extraction, knowledge normalization, knowledge linking, knowledge quality, knowledge security, knowledge events, knowledge testing, knowledge acceptance, and knowledge roadmap.
- Updated Volume 03 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE to include Book 03.04.
- Added PDF build target for `Volume_03_Book_03_04_Knowledge_System_v6_draft.pdf`.
- Added v6 ZIP package generation.

## Artifact Counts
- Markdown files: 158
- PDF files: 7
- ZIP package: `Mariam_Architecture_Library_v6_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v6 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Book 03.04 Markdown exists and is included in the ZIP.
- Book 03.04 PDF exists and is readable.
- `MANIFEST.json` reports v6 draft artifacts.
- The v6 ZIP contains the Book 03.04 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v6 draft | 2026-06-29 | Draft | Added the Knowledge System blueprint package. |
