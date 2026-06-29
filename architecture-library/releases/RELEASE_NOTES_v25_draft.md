# Release Notes - Mariam Architecture Library v25 draft

**Version:** v25 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V25-DRAFT

## What Was Added In v25
- Added Volume 06 - Specifications foundation.
- Added administrative files: README, INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE.
- Added `core/` specification group.
- Added the first 10 executable Enterprise Core specifications: kernel, lifecycle, runtime manager, runtime registry, event bus, service container, configuration, identity access, state manager, and health manager.
- Added PDF build target for `Volume_06_Core_Specifications_v25_draft.pdf`.
- Added v25 ZIP package generation.

## Artifact Counts
- Markdown files: 599
- PDF files: 26
- ZIP package: `Mariam_Architecture_Library_v25_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v25 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Volume 06 Markdown exists and is included in the ZIP.
- Volume 06 Core Specifications PDF exists and is readable.
- `MANIFEST.json` reports v25 draft artifacts.
- The v25 ZIP contains Volume 06 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v25 draft | 2026-06-29 | Draft | Added specifications foundation and first 10 core specifications. |
