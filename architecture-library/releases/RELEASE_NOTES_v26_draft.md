# Release Notes - Mariam Architecture Library v26 draft

**Version:** v26 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V26-DRAFT

## What Was Added In v26
- Added `architecture-library/volume-06-specifications/dna-operating-system/`.
- Added 15 executable DNA Operating System specifications covering DNA kernel, package engine, MDP import/export, ZIP/Git/archive adapters, package runtime object, package graph, dependency resolver, runtime store, mount/unmount/hot reload, universal DNA extractor, validation, versioning, compatibility, federation, and evolved DNA export.
- Updated Volume 06 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE.
- Added PDF build target for `Volume_06_DNA_Operating_System_Specifications_v26_draft.pdf`.
- Added v26 ZIP package generation.

## Artifact Counts
- Markdown files: 615
- PDF files: 27
- ZIP package: `Mariam_Architecture_Library_v26_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v26 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- DNA Specifications Markdown exists and is included in the ZIP.
- DNA Specifications PDF exists and is readable.
- `MANIFEST.json` reports v26 draft artifacts.
- The v26 ZIP contains DNA Specifications Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v26 draft | 2026-06-29 | Draft | Added DNA Operating System specifications. |
