# Release Notes - Mariam Architecture Library v27 draft

**Version:** v27 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V27-DRAFT

## What Was Added In v27
- Added `architecture-library/volume-06-specifications/runtime-ecosystem/`.
- Added 15 executable Runtime Ecosystem specifications covering runtime ecosystem, model runtime, tool runtime, plugin runtime, connector runtime, provider runtime, service runtime, workflow runtime, memory runtime, mission runtime, runtime lifecycle, permissions, observability, failure recovery, and testing.
- Updated Volume 06 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE.
- Added PDF build target for `Volume_06_Runtime_Ecosystem_Specifications_v27_draft.pdf`.
- Added v27 ZIP package generation.

## Artifact Counts
- Markdown files: 630
- PDF files: 28
- ZIP package: `Mariam_Architecture_Library_v27_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v27 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Runtime Specifications Markdown exists and is included in the ZIP.
- Runtime Specifications PDF exists and is readable.
- `MANIFEST.json` reports v27 draft artifacts.
- The v27 ZIP contains Runtime Specifications Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v27 draft | 2026-06-29 | Draft | Added Runtime Ecosystem specifications. |
