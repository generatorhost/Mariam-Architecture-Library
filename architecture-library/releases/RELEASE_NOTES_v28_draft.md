# Release Notes - Mariam Architecture Library v28 draft

**Version:** v28 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V28-DRAFT

## What Was Added In v28
- Added `architecture-library/volume-06-specifications/execution-os/`.
- Added 15 executable Execution OS specifications covering mission orchestration, mission manager, swarm engine, team coordination, agent routing, task graph, mission graph, distributed scheduler, parallel executor, long-running missions, stall detection, recovery engine, self-healing, and execution testing.
- Updated Volume 06 INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE.
- Added PDF build target for `Volume_06_Execution_OS_Specifications_v28_draft.pdf`.
- Added v28 ZIP package generation.

## Artifact Counts
- Markdown files: 646
- PDF files: 29
- ZIP package: `Mariam_Architecture_Library_v28_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v28 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Execution OS Specifications Markdown exists and is included in the ZIP.
- Execution OS Specifications PDF exists and is readable.
- `MANIFEST.json` reports v28 draft artifacts.
- The v28 ZIP contains Execution OS Specifications Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v28 draft | 2026-06-29 | Draft | Added Execution OS specifications. |
