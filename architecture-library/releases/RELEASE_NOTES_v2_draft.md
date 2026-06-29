# Release Notes - Mariam Architecture Library v2 draft

**Version:** v2 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V2-DRAFT

## Purpose
Document the second draft release of the Mariam Architecture Library.

## Scope
This release expands the documentation library with the complete Volume 02 Master Roadmap and generated v2 release artifacts. It does not modify the Mariam system code repository.

## What Was Added In v2
- Complete `architecture-library/volume-02-master-roadmap/` volume.
- Roadmap README, index, changelog, traceability, and acceptance documents.
- Roadmap overview book.
- Phase books 00 through 20 covering foundation, enterprise core, organization, AI society, knowledge, capabilities, DNA, runtime, models, workflows, swarm intelligence, opportunity intelligence, freelance automation, remote work automation, governance, services, infrastructure, experience, marketplace, evolution, and autonomous enterprise.
- Build support for `Volume_02_Master_Roadmap_v2_draft.pdf`.
- New v2 ZIP package and manifest metadata.

## Artifact Counts
- Markdown files: 61
- PDF files: 3
- ZIP package: `Mariam_Architecture_Library_v2_draft.zip`

## Build Notes
- The build reads Markdown from the architecture library and release notes.
- PDF generation uses the bundled Codex Python runtime with `reportlab`.
- v2 packaging includes all Markdown files, all PDFs, `MANIFEST.json`, and release notes.

## Acceptance Criteria
- Volume 02 Markdown exists and is included in the ZIP.
- Volume 02 PDF exists and is readable.
- `MANIFEST.json` reports v2 draft artifacts.
- The v2 ZIP contains the Volume 02 Markdown and PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v2 draft | 2026-06-29 | Draft | Added complete Volume 02 Master Roadmap and v2 release artifacts. |
