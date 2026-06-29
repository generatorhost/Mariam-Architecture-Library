# Release Notes - Mariam Architecture Library v1 draft

**Version:** v1 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V1-DRAFT

## Purpose
This release initializes the Mariam Architecture Library as the official Source of Truth for Mariam AI Enterprise OS.

## Scope
The release covers the initial documentation library baseline, generated PDFs, release ZIP, and manifest. It does not include implementation code for the Mariam system repository.

## Principles
- Release notes must make included documentation explicit.
- Generated artifacts must be reproducible from repository content.
- Reserved future volumes should be visible without pretending they are complete.

## Operating Rules
- Update release notes before producing a new release ZIP.
- Keep generated artifact names stable for the release version.
- Record known omissions and reserved areas honestly.

## Included Content
- Root repository README defining documentation authority and governance role.
- Full architecture-library directory structure for Volumes 00 through 09.
- Complete Volume 00 Enterprise Constitution with README, index, changelog, traceability, acceptance rules, and 15 constitutional books.
- Initial Volume 01 Master Vision with README and 10 strategic books.
- Build script at `tools/build_docs.py` for Markdown-to-PDF, ZIP packaging, and manifest generation.

## Generated Artifacts
- `architecture-library/releases/pdf/Volume_00_Enterprise_Constitution_v1_draft.pdf`
- `architecture-library/releases/pdf/Volume_01_Master_Vision_v1_draft.pdf`
- `architecture-library/releases/Mariam_Architecture_Library_v1_draft.zip`
- `architecture-library/releases/MANIFEST.json`

## Notes
Volumes 02 through 09 are intentionally reserved in this release. They exist as tracked library locations so later roadmap, blueprint, dictionary, standards, specifications, development, operations, and testing documents have stable canonical paths.

## Acceptance Criteria
- The release includes Volume 00 and Volume 01 Markdown content.
- The release includes PDFs for Volume 00 and Volume 01.
- The release includes a ZIP package and `MANIFEST.json`.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v1 draft | 2026-06-29 | Draft | Initial release package for the documentation library. |
