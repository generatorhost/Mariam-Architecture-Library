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

## Book 03.02 Enterprise Organization
- MAL-V03-B03-02-README - `book-03-02-enterprise-organization/README.md`
- MAL-V03-B03-02-001 - `book-03-02-enterprise-organization/book-03-02-01-enterprise-organization-overview.md`
- MAL-V03-B03-02-002 - `book-03-02-enterprise-organization/book-03-02-02-enterprise-structure.md`
- MAL-V03-B03-02-003 - `book-03-02-enterprise-organization/book-03-02-03-board-governance.md`
- MAL-V03-B03-02-004 - `book-03-02-enterprise-organization/book-03-02-04-chief-office.md`
- MAL-V03-B03-02-005 - `book-03-02-enterprise-organization/book-03-02-05-departments.md`
- MAL-V03-B03-02-006 - `book-03-02-enterprise-organization/book-03-02-06-department-missions.md`
- MAL-V03-B03-02-007 - `book-03-02-enterprise-organization/book-03-02-07-roles-responsibilities.md`
- MAL-V03-B03-02-008 - `book-03-02-enterprise-organization/book-03-02-08-decision-flow.md`
- MAL-V03-B03-02-009 - `book-03-02-enterprise-organization/book-03-02-09-escalation-model.md`
- MAL-V03-B03-02-010 - `book-03-02-enterprise-organization/book-03-02-10-approval-lines.md`
- MAL-V03-B03-02-011 - `book-03-02-enterprise-organization/book-03-02-11-cross-department-coordination.md`
- MAL-V03-B03-02-012 - `book-03-02-enterprise-organization/book-03-02-12-enterprise-kpis.md`
- MAL-V03-B03-02-013 - `book-03-02-enterprise-organization/book-03-02-13-operating-rhythm.md`
- MAL-V03-B03-02-014 - `book-03-02-enterprise-organization/book-03-02-14-governance-checkpoints.md`
- MAL-V03-B03-02-015 - `book-03-02-enterprise-organization/book-03-02-15-organization-events.md`
- MAL-V03-B03-02-016 - `book-03-02-enterprise-organization/book-03-02-16-organization-storage.md`
- MAL-V03-B03-02-017 - `book-03-02-enterprise-organization/book-03-02-17-organization-security.md`
- MAL-V03-B03-02-018 - `book-03-02-enterprise-organization/book-03-02-18-organization-testing.md`
- MAL-V03-B03-02-019 - `book-03-02-enterprise-organization/book-03-02-19-organization-acceptance.md`
- MAL-V03-B03-02-020 - `book-03-02-enterprise-organization/book-03-02-20-organization-roadmap.md`

## Book 03.03 AI Society
- MAL-V03-B03-03-README - `book-03-03-ai-society/README.md`
- MAL-V03-B03-03-001 - `book-03-03-ai-society/book-03-03-01-ai-society-overview.md`
- MAL-V03-B03-03-002 - `book-03-03-ai-society/book-03-03-02-chief.md`
- MAL-V03-B03-03-003 - `book-03-03-ai-society/book-03-03-03-mission-manager.md`
- MAL-V03-B03-03-004 - `book-03-03-ai-society/book-03-03-04-department-managers.md`
- MAL-V03-B03-03-005 - `book-03-03-ai-society/book-03-03-05-team-leaders.md`
- MAL-V03-B03-03-006 - `book-03-03-ai-society/book-03-03-06-swarms.md`
- MAL-V03-B03-03-007 - `book-03-03-ai-society/book-03-03-07-agents.md`
- MAL-V03-B03-03-008 - `book-03-03-ai-society/book-03-03-08-skills.md`
- MAL-V03-B03-03-009 - `book-03-03-ai-society/book-03-03-09-capabilities.md`
- MAL-V03-B03-03-010 - `book-03-03-ai-society/book-03-03-10-agent-memory.md`
- MAL-V03-B03-03-011 - `book-03-03-ai-society/book-03-03-11-agent-communication.md`
- MAL-V03-B03-03-012 - `book-03-03-ai-society/book-03-03-12-agent-planning.md`
- MAL-V03-B03-03-013 - `book-03-03-ai-society/book-03-03-13-agent-execution.md`
- MAL-V03-B03-03-014 - `book-03-03-ai-society/book-03-03-14-agent-review.md`
- MAL-V03-B03-03-015 - `book-03-03-ai-society/book-03-03-15-agent-validation.md`
- MAL-V03-B03-03-016 - `book-03-03-ai-society/book-03-03-16-agent-optimization.md`
- MAL-V03-B03-03-017 - `book-03-03-ai-society/book-03-03-17-agent-dna.md`
- MAL-V03-B03-03-018 - `book-03-03-ai-society/book-03-03-18-agent-governance.md`
- MAL-V03-B03-03-019 - `book-03-03-ai-society/book-03-03-19-ai-society-testing.md`
- MAL-V03-B03-03-020 - `book-03-03-ai-society/book-03-03-20-ai-society-roadmap.md`

## Book 03.04 Knowledge System
- MAL-V03-B03-04-README - `book-03-04-knowledge-system/README.md`
- MAL-V03-B03-04-001 - `book-03-04-knowledge-system/book-03-04-01-knowledge-system-overview.md`
- MAL-V03-B03-04-002 - `book-03-04-knowledge-system/book-03-04-02-knowledge-graph.md`
- MAL-V03-B03-04-003 - `book-03-04-knowledge-system/book-03-04-03-knowledge-store.md`
- MAL-V03-B03-04-004 - `book-03-04-knowledge-system/book-03-04-04-document-intelligence.md`
- MAL-V03-B03-04-005 - `book-03-04-knowledge-system/book-03-04-05-memory-system.md`
- MAL-V03-B03-04-006 - `book-03-04-knowledge-system/book-03-04-06-vector-store.md`
- MAL-V03-B03-04-007 - `book-03-04-knowledge-system/book-03-04-07-embedding-system.md`
- MAL-V03-B03-04-008 - `book-03-04-knowledge-system/book-03-04-08-semantic-search.md`
- MAL-V03-B03-04-009 - `book-03-04-knowledge-system/book-03-04-09-knowledge-indexing.md`
- MAL-V03-B03-04-010 - `book-03-04-knowledge-system/book-03-04-10-knowledge-versioning.md`
- MAL-V03-B03-04-011 - `book-03-04-knowledge-system/book-03-04-11-knowledge-ingestion.md`
- MAL-V03-B03-04-012 - `book-03-04-knowledge-system/book-03-04-12-knowledge-extraction.md`
- MAL-V03-B03-04-013 - `book-03-04-knowledge-system/book-03-04-13-knowledge-normalization.md`
- MAL-V03-B03-04-014 - `book-03-04-knowledge-system/book-03-04-14-knowledge-linking.md`
- MAL-V03-B03-04-015 - `book-03-04-knowledge-system/book-03-04-15-knowledge-quality.md`
- MAL-V03-B03-04-016 - `book-03-04-knowledge-system/book-03-04-16-knowledge-security.md`
- MAL-V03-B03-04-017 - `book-03-04-knowledge-system/book-03-04-17-knowledge-events.md`
- MAL-V03-B03-04-018 - `book-03-04-knowledge-system/book-03-04-18-knowledge-testing.md`
- MAL-V03-B03-04-019 - `book-03-04-knowledge-system/book-03-04-19-knowledge-acceptance.md`
- MAL-V03-B03-04-020 - `book-03-04-knowledge-system/book-03-04-20-knowledge-roadmap.md`

## Book 03.05 Capability System
- MAL-V03-B03-05-README - `book-03-05-capability-system/README.md`
- MAL-V03-B03-05-001 - `book-03-05-capability-system/book-03-05-01-capability-system-overview.md`
- MAL-V03-B03-05-002 - `book-03-05-capability-system/book-03-05-02-capability-graph.md`
- MAL-V03-B03-05-003 - `book-03-05-capability-system/book-03-05-03-capability-registry.md`
- MAL-V03-B03-05-004 - `book-03-05-capability-system/book-03-05-04-capability-discovery.md`
- MAL-V03-B03-05-005 - `book-03-05-capability-system/book-03-05-05-capability-matching.md`
- MAL-V03-B03-05-006 - `book-03-05-capability-system/book-03-05-06-capability-ranking.md`
- MAL-V03-B03-05-007 - `book-03-05-capability-system/book-03-05-07-capability-requirements.md`
- MAL-V03-B03-05-008 - `book-03-05-capability-system/book-03-05-08-capability-dependencies.md`
- MAL-V03-B03-05-009 - `book-03-05-capability-system/book-03-05-09-capability-lifecycle.md`
- MAL-V03-B03-05-010 - `book-03-05-capability-system/book-03-05-10-capability-dna.md`
- MAL-V03-B03-05-011 - `book-03-05-capability-system/book-03-05-11-capability-benchmarks.md`
- MAL-V03-B03-05-012 - `book-03-05-capability-system/book-03-05-12-capability-quality.md`
- MAL-V03-B03-05-013 - `book-03-05-capability-system/book-03-05-13-capability-governance.md`
- MAL-V03-B03-05-014 - `book-03-05-capability-system/book-03-05-14-capability-security.md`
- MAL-V03-B03-05-015 - `book-03-05-capability-system/book-03-05-15-capability-events.md`
- MAL-V03-B03-05-016 - `book-03-05-capability-system/book-03-05-16-capability-storage.md`
- MAL-V03-B03-05-017 - `book-03-05-capability-system/book-03-05-17-capability-metrics.md`
- MAL-V03-B03-05-018 - `book-03-05-capability-system/book-03-05-18-capability-testing.md`
- MAL-V03-B03-05-019 - `book-03-05-capability-system/book-03-05-19-capability-acceptance.md`
- MAL-V03-B03-05-020 - `book-03-05-capability-system/book-03-05-20-capability-roadmap.md`

## Book 03.06 DNA Operating System
- MAL-V03-B03-06-README - `book-03-06-dna-operating-system/README.md`
- MAL-V03-B03-06-001 - `book-03-06-dna-operating-system/book-03-06-01-dna-operating-system-overview.md`
- MAL-V03-B03-06-002 - `book-03-06-dna-operating-system/book-03-06-02-dna-package-engine.md`
- MAL-V03-B03-06-003 - `book-03-06-dna-operating-system/book-03-06-03-runtime-store.md`
- MAL-V03-B03-06-004 - `book-03-06-dna-operating-system/book-03-06-04-package-graph.md`
- MAL-V03-B03-06-005 - `book-03-06-dna-operating-system/book-03-06-05-dependency-resolver.md`
- MAL-V03-B03-06-006 - `book-03-06-dna-operating-system/book-03-06-06-mount-manager.md`
- MAL-V03-B03-06-007 - `book-03-06-dna-operating-system/book-03-06-07-hot-reload.md`
- MAL-V03-B03-06-008 - `book-03-06-dna-operating-system/book-03-06-08-universal-dna-extractor.md`
- MAL-V03-B03-06-009 - `book-03-06-dna-operating-system/book-03-06-09-dna-federation.md`
- MAL-V03-B03-06-010 - `book-03-06-dna-operating-system/book-03-06-10-dna-export.md`
- MAL-V03-B03-06-011 - `book-03-06-dna-operating-system/book-03-06-11-dna-import.md`
- MAL-V03-B03-06-012 - `book-03-06-dna-operating-system/book-03-06-12-dna-versioning.md`
- MAL-V03-B03-06-013 - `book-03-06-dna-operating-system/book-03-06-13-dna-validation.md`
- MAL-V03-B03-06-014 - `book-03-06-dna-operating-system/book-03-06-14-dna-governance.md`
- MAL-V03-B03-06-015 - `book-03-06-dna-operating-system/book-03-06-15-dna-security.md`
- MAL-V03-B03-06-016 - `book-03-06-dna-operating-system/book-03-06-16-dna-events.md`
- MAL-V03-B03-06-017 - `book-03-06-dna-operating-system/book-03-06-17-dna-storage.md`
- MAL-V03-B03-06-018 - `book-03-06-dna-operating-system/book-03-06-18-dna-testing.md`
- MAL-V03-B03-06-019 - `book-03-06-dna-operating-system/book-03-06-19-dna-acceptance.md`
- MAL-V03-B03-06-020 - `book-03-06-dna-operating-system/book-03-06-20-dna-roadmap.md`
