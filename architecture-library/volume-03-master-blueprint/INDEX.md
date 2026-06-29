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

## Book 03.07 Runtime Ecosystem
- MAL-V03-B03-07-README - `book-03-07-runtime-ecosystem/README.md`
- MAL-V03-B03-07-001 - `book-03-07-runtime-ecosystem/book-03-07-01-runtime-ecosystem-overview.md`
- MAL-V03-B03-07-002 - `book-03-07-runtime-ecosystem/book-03-07-02-runtime-kernel.md`
- MAL-V03-B03-07-003 - `book-03-07-runtime-ecosystem/book-03-07-03-model-runtime.md`
- MAL-V03-B03-07-004 - `book-03-07-runtime-ecosystem/book-03-07-04-plugin-runtime.md`
- MAL-V03-B03-07-005 - `book-03-07-runtime-ecosystem/book-03-07-05-connector-runtime.md`
- MAL-V03-B03-07-006 - `book-03-07-runtime-ecosystem/book-03-07-06-provider-runtime.md`
- MAL-V03-B03-07-007 - `book-03-07-runtime-ecosystem/book-03-07-07-workflow-runtime.md`
- MAL-V03-B03-07-008 - `book-03-07-runtime-ecosystem/book-03-07-08-mission-runtime.md`
- MAL-V03-B03-07-009 - `book-03-07-runtime-ecosystem/book-03-07-09-service-runtime.md`
- MAL-V03-B03-07-010 - `book-03-07-runtime-ecosystem/book-03-07-10-runtime-scheduler.md`
- MAL-V03-B03-07-011 - `book-03-07-runtime-ecosystem/book-03-07-11-runtime-isolation.md`
- MAL-V03-B03-07-012 - `book-03-07-runtime-ecosystem/book-03-07-12-runtime-policy.md`
- MAL-V03-B03-07-013 - `book-03-07-runtime-ecosystem/book-03-07-13-runtime-observability.md`
- MAL-V03-B03-07-014 - `book-03-07-runtime-ecosystem/book-03-07-14-runtime-recovery.md`
- MAL-V03-B03-07-015 - `book-03-07-runtime-ecosystem/book-03-07-15-runtime-scaling.md`
- MAL-V03-B03-07-016 - `book-03-07-runtime-ecosystem/book-03-07-16-runtime-events.md`
- MAL-V03-B03-07-017 - `book-03-07-runtime-ecosystem/book-03-07-17-runtime-storage.md`
- MAL-V03-B03-07-018 - `book-03-07-runtime-ecosystem/book-03-07-18-runtime-security.md`
- MAL-V03-B03-07-019 - `book-03-07-runtime-ecosystem/book-03-07-19-runtime-testing.md`
- MAL-V03-B03-07-020 - `book-03-07-runtime-ecosystem/book-03-07-20-runtime-roadmap.md`

## Book 03.08 Workflow System
- MAL-V03-B03-08-README - `book-03-08-workflow-system/README.md`
- MAL-V03-B03-08-001 - `book-03-08-workflow-system/book-03-08-01-workflow-system-overview.md`
- MAL-V03-B03-08-002 - `book-03-08-workflow-system/book-03-08-02-workflow-engine.md`
- MAL-V03-B03-08-003 - `book-03-08-workflow-system/book-03-08-03-mission-graph.md`
- MAL-V03-B03-08-004 - `book-03-08-workflow-system/book-03-08-04-task-graph.md`
- MAL-V03-B03-08-005 - `book-03-08-workflow-system/book-03-08-05-planner.md`
- MAL-V03-B03-08-006 - `book-03-08-workflow-system/book-03-08-06-scheduler.md`
- MAL-V03-B03-08-007 - `book-03-08-workflow-system/book-03-08-07-executor.md`
- MAL-V03-B03-08-008 - `book-03-08-workflow-system/book-03-08-08-recovery.md`
- MAL-V03-B03-08-009 - `book-03-08-workflow-system/book-03-08-09-self-healing.md`
- MAL-V03-B03-08-010 - `book-03-08-workflow-system/book-03-08-10-approval-gates.md`
- MAL-V03-B03-08-011 - `book-03-08-workflow-system/book-03-08-11-workflow-state.md`
- MAL-V03-B03-08-012 - `book-03-08-workflow-system/book-03-08-12-workflow-templates.md`
- MAL-V03-B03-08-013 - `book-03-08-workflow-system/book-03-08-13-workflow-routing.md`
- MAL-V03-B03-08-014 - `book-03-08-workflow-system/book-03-08-14-workflow-observability.md`
- MAL-V03-B03-08-015 - `book-03-08-workflow-system/book-03-08-15-workflow-governance.md`
- MAL-V03-B03-08-016 - `book-03-08-workflow-system/book-03-08-16-workflow-events.md`
- MAL-V03-B03-08-017 - `book-03-08-workflow-system/book-03-08-17-workflow-storage.md`
- MAL-V03-B03-08-018 - `book-03-08-workflow-system/book-03-08-18-workflow-security.md`
- MAL-V03-B03-08-019 - `book-03-08-workflow-system/book-03-08-19-workflow-testing.md`
- MAL-V03-B03-08-020 - `book-03-08-workflow-system/book-03-08-20-workflow-roadmap.md`

## Book 03.09 Swarm Intelligence
- MAL-V03-B03-09-README - `book-03-09-swarm-intelligence/README.md`
- MAL-V03-B03-09-001 - `book-03-09-swarm-intelligence/book-03-09-01-swarm-intelligence-overview.md`
- MAL-V03-B03-09-002 - `book-03-09-swarm-intelligence/book-03-09-02-swarm-chief.md`
- MAL-V03-B03-09-003 - `book-03-09-swarm-intelligence/book-03-09-03-coordinator.md`
- MAL-V03-B03-09-004 - `book-03-09-swarm-intelligence/book-03-09-04-teams.md`
- MAL-V03-B03-09-005 - `book-03-09-swarm-intelligence/book-03-09-05-dynamic-swarms.md`
- MAL-V03-B03-09-006 - `book-03-09-swarm-intelligence/book-03-09-06-parallel-execution.md`
- MAL-V03-B03-09-007 - `book-03-09-swarm-intelligence/book-03-09-07-recovery.md`
- MAL-V03-B03-09-008 - `book-03-09-swarm-intelligence/book-03-09-08-communication.md`
- MAL-V03-B03-09-009 - `book-03-09-swarm-intelligence/book-03-09-09-optimization.md`
- MAL-V03-B03-09-010 - `book-03-09-swarm-intelligence/book-03-09-10-consensus.md`
- MAL-V03-B03-09-011 - `book-03-09-swarm-intelligence/book-03-09-11-critique-loops.md`
- MAL-V03-B03-09-012 - `book-03-09-swarm-intelligence/book-03-09-12-conflict-resolution.md`
- MAL-V03-B03-09-013 - `book-03-09-swarm-intelligence/book-03-09-13-task-allocation.md`
- MAL-V03-B03-09-014 - `book-03-09-swarm-intelligence/book-03-09-14-swarm-memory.md`
- MAL-V03-B03-09-015 - `book-03-09-swarm-intelligence/book-03-09-15-swarm-governance.md`
- MAL-V03-B03-09-016 - `book-03-09-swarm-intelligence/book-03-09-16-swarm-events.md`
- MAL-V03-B03-09-017 - `book-03-09-swarm-intelligence/book-03-09-17-swarm-storage.md`
- MAL-V03-B03-09-018 - `book-03-09-swarm-intelligence/book-03-09-18-swarm-security.md`
- MAL-V03-B03-09-019 - `book-03-09-swarm-intelligence/book-03-09-19-swarm-testing.md`
- MAL-V03-B03-09-020 - `book-03-09-swarm-intelligence/book-03-09-20-swarm-roadmap.md`

## Book 03.10 Model Ecosystem
- MAL-V03-B03-10-README - `book-03-10-model-ecosystem/README.md`
- MAL-V03-B03-10-001 - `book-03-10-model-ecosystem/book-03-10-01-model-ecosystem-overview.md`
- MAL-V03-B03-10-002 - `book-03-10-model-ecosystem/book-03-10-02-model-registry.md`
- MAL-V03-B03-10-003 - `book-03-10-model-ecosystem/book-03-10-03-model-router.md`
- MAL-V03-B03-10-004 - `book-03-10-model-ecosystem/book-03-10-04-gguf-models.md`
- MAL-V03-B03-10-005 - `book-03-10-model-ecosystem/book-03-10-05-onnx-models.md`
- MAL-V03-B03-10-006 - `book-03-10-model-ecosystem/book-03-10-06-safetensors-models.md`
- MAL-V03-B03-10-007 - `book-03-10-model-ecosystem/book-03-10-07-transformers-models.md`
- MAL-V03-B03-10-008 - `book-03-10-model-ecosystem/book-03-10-08-pytorch-models.md`
- MAL-V03-B03-10-009 - `book-03-10-model-ecosystem/book-03-10-09-llama-cpp-runtime.md`
- MAL-V03-B03-10-010 - `book-03-10-model-ecosystem/book-03-10-10-vllm-runtime.md`
- MAL-V03-B03-10-011 - `book-03-10-model-ecosystem/book-03-10-11-ktransformers-runtime.md`
- MAL-V03-B03-10-012 - `book-03-10-model-ecosystem/book-03-10-12-provider-abstraction.md`
- MAL-V03-B03-10-013 - `book-03-10-model-ecosystem/book-03-10-13-model-evaluation.md`
- MAL-V03-B03-10-014 - `book-03-10-model-ecosystem/book-03-10-14-model-fallback.md`
- MAL-V03-B03-10-015 - `book-03-10-model-ecosystem/book-03-10-15-model-cost-control.md`
- MAL-V03-B03-10-016 - `book-03-10-model-ecosystem/book-03-10-16-model-events.md`
- MAL-V03-B03-10-017 - `book-03-10-model-ecosystem/book-03-10-17-model-storage.md`
- MAL-V03-B03-10-018 - `book-03-10-model-ecosystem/book-03-10-18-model-security.md`
- MAL-V03-B03-10-019 - `book-03-10-model-ecosystem/book-03-10-19-model-testing.md`
- MAL-V03-B03-10-020 - `book-03-10-model-ecosystem/book-03-10-20-model-roadmap.md`
