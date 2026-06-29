# Volume 03 Index

**Version:** v3 draft
**Status:** Draft
**Document ID:** MAL-V03-INDEX

## Purpose
List the canonical blueprint books available in Volume 03.

## Scope
Covers current v3 content and establishes stable references for future blueprint books.

## Responsibilities
- Define blueprint authority for the Enterprise Core area.
- Maintain alignment with the Volume 02 Enterprise Core roadmap phase.
- Give later specifications enough structure to become implementation-ready.

## Inputs
- Volume 00 Enterprise Constitution principles.
- Volume 01 Master Vision strategy.
- Volume 02 Master Roadmap phase definitions.

## Outputs
- Canonical blueprint structure for Enterprise Core.
- Traceable subsystem boundaries.
- Acceptance expectations for later specifications and implementation.

## Interfaces
- Volume 03 Master Blueprint index.
- Book 03.01 Enterprise Core subsystem documents.
- Future Volume 06 subsystem specifications.

## Events
- BlueprintChanged
- SubsystemBoundaryDefined
- AcceptanceRuleUpdated

## Storage
- Markdown source files in the architecture library.
- Generated PDF release artifacts.
- Release manifest checksums.

## Security
- No secrets, credentials, private keys, or operational tokens are stored in blueprint files.
- Security-sensitive subsystem behavior is described as architecture, not executable configuration.
- Access-control decisions are deferred to approved specifications.

## Metrics
- Document completeness ratio.
- Traceability coverage across roadmap and constitution sources.
- Release artifact generation success.

## Tests
- Verify required sections exist in every file.
- Verify generated PDF is readable.
- Verify v3 ZIP contains Markdown, PDFs, manifest, and release notes.

## Acceptance Criteria
- The document contains all required v3 sections.
- The document can guide downstream specifications without code changes.
- The document is included in generated release artifacts.

## Traceability
- MAL-V00-B005
- MAL-V00-B011
- MAL-V02-B003

## Blueprint Books
- MAL-V03-B03-01-README - `book-03-01-enterprise-core/README.md`
- MAL-V03-B03-01-001 - `book-03-01-enterprise-core/book-03-01-01-enterprise-core-overview.md`
- MAL-V03-B03-01-002 - `book-03-01-enterprise-core/book-03-01-02-kernel.md`
- MAL-V03-B03-01-003 - `book-03-01-enterprise-core/book-03-01-03-lifecycle.md`
- MAL-V03-B03-01-004 - `book-03-01-enterprise-core/book-03-01-04-runtime-manager.md`
- MAL-V03-B03-01-005 - `book-03-01-enterprise-core/book-03-01-05-runtime-registry.md`
- MAL-V03-B03-01-006 - `book-03-01-enterprise-core/book-03-01-06-event-bus.md`
- MAL-V03-B03-01-007 - `book-03-01-enterprise-core/book-03-01-07-service-container.md`
- MAL-V03-B03-01-008 - `book-03-01-enterprise-core/book-03-01-08-configuration.md`
- MAL-V03-B03-01-009 - `book-03-01-enterprise-core/book-03-01-09-identity-access.md`
- MAL-V03-B03-01-010 - `book-03-01-enterprise-core/book-03-01-10-state-manager.md`
- MAL-V03-B03-01-011 - `book-03-01-enterprise-core/book-03-01-11-resource-manager.md`
- MAL-V03-B03-01-012 - `book-03-01-enterprise-core/book-03-01-12-object-manager.md`
- MAL-V03-B03-01-013 - `book-03-01-enterprise-core/book-03-01-13-health-manager.md`
- MAL-V03-B03-01-014 - `book-03-01-enterprise-core/book-03-01-14-core-events.md`
- MAL-V03-B03-01-015 - `book-03-01-enterprise-core/book-03-01-15-core-storage.md`
- MAL-V03-B03-01-016 - `book-03-01-enterprise-core/book-03-01-16-core-security.md`
- MAL-V03-B03-01-017 - `book-03-01-enterprise-core/book-03-01-17-core-observability.md`
- MAL-V03-B03-01-018 - `book-03-01-enterprise-core/book-03-01-18-core-testing.md`
- MAL-V03-B03-01-019 - `book-03-01-enterprise-core/book-03-01-19-core-acceptance.md`
- MAL-V03-B03-01-020 - `book-03-01-enterprise-core/book-03-01-20-core-roadmap.md`

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v3 draft | 2026-06-29 | Draft | Initial Enterprise Core blueprint content for Mariam Architecture Library v3. |
