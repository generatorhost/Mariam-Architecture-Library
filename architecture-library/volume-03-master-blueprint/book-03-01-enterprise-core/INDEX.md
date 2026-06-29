# Book 03.01 Index

**Version:** v3 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-01-INDEX

## Purpose
List the canonical Enterprise Core subsystem blueprint files.

## Scope
Covers Book 03.01 documents from overview through core roadmap.

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

## Book Files
1. `book-03-01-01-enterprise-core-overview.md`
2. `book-03-01-02-kernel.md`
3. `book-03-01-03-lifecycle.md`
4. `book-03-01-04-runtime-manager.md`
5. `book-03-01-05-runtime-registry.md`
6. `book-03-01-06-event-bus.md`
7. `book-03-01-07-service-container.md`
8. `book-03-01-08-configuration.md`
9. `book-03-01-09-identity-access.md`
10. `book-03-01-10-state-manager.md`
11. `book-03-01-11-resource-manager.md`
12. `book-03-01-12-object-manager.md`
13. `book-03-01-13-health-manager.md`
14. `book-03-01-14-core-events.md`
15. `book-03-01-15-core-storage.md`
16. `book-03-01-16-core-security.md`
17. `book-03-01-17-core-observability.md`
18. `book-03-01-18-core-testing.md`
19. `book-03-01-19-core-acceptance.md`
20. `book-03-01-20-core-roadmap.md`

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v3 draft | 2026-06-29 | Draft | Initial Enterprise Core blueprint content for Mariam Architecture Library v3. |
