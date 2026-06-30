# Release Notes - Mariam Architecture Library v129 draft

**Version:** v129 draft  
**Status:** Draft  
**Document ID:** MAL-RELNOTES-V129-DRAFT

## What Was Corrected In v129
- Replaced unofficial data terminology such as `legacy single-database wording` and `legacy single-database wording` with `Mariam Data Platform`.
- Replaced language that could imply Mariam is merely an `legacy narrow-core wording` or `legacy narrow-core wording` with `Mariam Living Enterprise OS Core`.
- Added `architecture-library/volume-21-infrastructure/data-platform/mariam-data-platform.md`.
- Added `architecture-library/volume-14-dna-operating-system/living-enterprise-os-core.md`.
- Renamed the legacy seed document for the old Postgres-oriented pattern to `legacy-27-13-mariam-data-platform.md`.
- Added PDF build target `Volume_21_Mariam_Data_Platform_v129_draft.pdf`.
- Added ZIP package `Mariam_Architecture_Library_v129_draft.zip`.

## Mariam Data Platform Components
- Runtime DB
- Knowledge DB
- Audit DB
- Governance DB
- Mission DB
- CRM DB
- Scraping DB
- Opportunity DB
- Communication DB
- Document DB
- DNA Registry DB
- Capability Graph DB
- Workflow DB
- Vector Store
- Object Storage
- Cache
- Logs Store
- Metrics Store
- Artifact Store

## Mariam Living Enterprise OS Core
The official core term now emphasizes that Mariam is a living enterprise operating system able to learn, expand, develop, extract DNA, compose DNA, run DNA, evolve behavior, and export new DNA.

## Build Notes
- Built with `tools/build_docs.py`.
- PDF readability is verified with `pypdf`.
- ZIP membership is verified for v129 release notes, MANIFEST, and `Volume_21_Mariam_Data_Platform_v129_draft.pdf`.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v129 draft | 2026-06-30 | Draft | Corrected Mariam terminology and data platform architecture. |
