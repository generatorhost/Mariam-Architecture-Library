# Release Notes - Mariam Architecture Library v24 draft

**Version:** v24 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V24-DRAFT

## What Was Added In v24
- Added Volume 05 - Engineering Standards.
- Added administrative files: README, INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE.
- Added 20 practical engineering standards covering architecture, documentation, naming, versioning, repositories, code, Python, runtime, APIs, events, storage, security, testing, quality, observability, PDF builds, releases, Git, CI/CD, and governance.
- Added PDF build target for `Volume_05_Engineering_Standards_v24_draft.pdf`.
- Added v24 ZIP package generation.

## Artifact Counts
- Markdown files: 583
- PDF files: 25
- ZIP package: `Mariam_Architecture_Library_v24_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v24 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Volume 05 Markdown exists and is included in the ZIP.
- Volume 05 PDF exists and is readable.
- `MANIFEST.json` reports v24 draft artifacts.
- The v24 ZIP contains Volume 05 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v24 draft | 2026-06-29 | Draft | Added the engineering standards baseline. |
