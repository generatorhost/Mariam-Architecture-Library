# Release Notes - Mariam Architecture Library v23 draft

**Version:** v23 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V23-DRAFT

## What Was Added In v23
- Added Volume 04 - Canonical Dictionary.
- Added administrative files: README, INDEX, CHANGELOG, TRACEABILITY, and ACCEPTANCE.
- Added 25 dictionary files covering enterprise, organization, AI society, agents, swarms, DNA, knowledge, capabilities, workflows, runtime, models, providers, plugins, connectors, marketplace, governance, security, infrastructure, freelance, remote work, evolution, monitoring, storage, UI dashboards, and integration/API/MCP terminology.
- Added PDF build target for `Volume_04_Canonical_Dictionary_v23_draft.pdf`.
- Added v23 ZIP package generation.

## Artifact Counts
- Markdown files: 557
- PDF files: 24
- ZIP package: `Mariam_Architecture_Library_v23_draft.zip`

## Build Notes
- The build uses the bundled Codex Python runtime with `reportlab`.
- PDF validation uses `pypdf` to confirm readability and page count.
- v23 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Volume 04 Markdown exists and is included in the ZIP.
- Volume 04 PDF exists and is readable.
- `MANIFEST.json` reports v23 draft artifacts.
- The v23 ZIP contains Volume 04 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v23 draft | 2026-06-29 | Draft | Added the canonical dictionary baseline. |
