# Release Notes - Mariam Architecture Library v3 draft

**Version:** v3 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V3-DRAFT

## What Was Added In v3
- Started Volume 03 - Master Blueprint.
- Added Volume 03 administrative documents: README, index, changelog, traceability, and acceptance.
- Added Book 03.01 - Enterprise Core as the first detailed blueprint package.
- Added Enterprise Core subsystem documents for kernel, lifecycle, runtime manager, runtime registry, event bus, service container, configuration, identity access, state manager, resource manager, object manager, health manager, core events, core storage, core security, core observability, core testing, core acceptance, and core roadmap.
- Added PDF build target for `Volume_03_Book_03_01_Enterprise_Core_v3_draft.pdf`.
- Added v3 ZIP package generation.

## Artifact Counts
- Markdown files: 89
- PDF files: 4
- ZIP package: `Mariam_Architecture_Library_v3_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v3 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Book 03.01 Markdown exists and is included in the ZIP.
- Book 03.01 PDF exists and is readable.
- `MANIFEST.json` reports v3 draft artifacts.
- The v3 ZIP contains the Book 03.01 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v3 draft | 2026-06-29 | Draft | Added the initial Enterprise Core blueprint package. |
