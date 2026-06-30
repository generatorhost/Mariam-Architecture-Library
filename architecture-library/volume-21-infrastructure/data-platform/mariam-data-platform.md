# Mariam Data Platform

**Title:** Mariam Data Platform  
**Version:** v129 draft  
**Status:** Draft  
**Document ID:** MAL-V21-DATA-PLATFORM-001

## Purpose
Define the official data architecture term for Mariam AI Enterprise OS. `Mariam Data Platform` replaces informal phrases such as `legacy single-database wording` or `legacy single-database wording` and describes the complete data substrate required by Mariam Living Enterprise OS Core.

## Scope
- Covers operational databases, knowledge stores, audit records, governance data, mission records, CRM data, scraping data, opportunities, communication records, documents, DNA registries, capability graphs, workflow state, vector search, object storage, cache, logs, metrics, and artifacts.
- Defines platform responsibilities and boundaries, not vendor-specific credentials or runtime deployment secrets.
- Applies to architecture, implementation specifications, operations, testing, governance, and future code rebuild work.

## Official Components
- Runtime DB: stores runtime object state, lifecycle state, registrations, service metadata, and execution-safe runtime records.
- Knowledge DB: stores curated knowledge records, document metadata, memory references, citations, and knowledge lifecycle state.
- Audit DB: stores immutable audit evidence, decisions, approvals, rejections, policy versions, and trace records.
- Governance DB: stores policies, controls, risk decisions, authority mappings, compliance evidence, and governance workflows.
- Mission DB: stores missions, task graphs, mission graphs, schedules, dependencies, execution attempts, and acceptance evidence.
- CRM DB: stores accounts, contacts, client profiles, conversation summaries, relationship state, and follow-up obligations.
- Scraping DB: stores crawl sources, crawl jobs, queue state, extracted entities, failed crawls, deduplication groups, and review state.
- Opportunity DB: stores opportunities, scores, ranks, fit analysis, proposal readiness, status, source lineage, and approval state.
- Communication DB: stores message metadata, threads, channel references, outbound approval records, and consent state.
- Document DB: stores document metadata, generated report state, review status, version references, and approval evidence.
- DNA Registry DB: stores DNA packages, package versions, manifests, compatibility metadata, mount state, and export records.
- Capability Graph DB: stores capabilities, dependencies, skill relationships, benchmark links, ranking signals, and graph edges.
- Workflow DB: stores workflow definitions, runs, triggers, actions, approvals, retries, and automation evidence.
- Vector Store: stores embeddings, semantic indexes, similarity references, retrieval metadata, and vector provenance.
- Object Storage: stores binary artifacts, reports, generated files, uploads, package assets, exports, and long-lived evidence files.
- Cache: stores ephemeral state, sessions, locks, queue hints, dashboard snapshots, rate limits, and short-lived coordination records.
- Logs Store: stores structured logs, correlation IDs, service logs, runtime logs, security logs, and operational records.
- Metrics Store: stores time-series metrics, service health, latency, throughput, queue depth, crawl metrics, and dashboard measurements.
- Artifact Store: stores generated outputs, proposal drafts, PDFs, Word files, PowerPoint files, exports, validation bundles, and delivery packages.

## Platform Rules
- No component may be treated as the single `legacy single-database wording`; Mariam is a living enterprise platform with multiple governed data stores.
- Durable business records, ephemeral cache, vector indexes, object artifacts, logs, and metrics must remain conceptually separate even if a deployment combines physical infrastructure.
- Every data component must define ownership, retention, access control, backup, restore, observability, and audit behavior.
- Data movement between components must preserve trace IDs, provenance, schema version, policy version, and security scope.

## Mariam Living Enterprise OS Core Relationship
Mariam Data Platform serves Mariam Living Enterprise OS Core, which is not a narrow legacy narrow-core wording. The core is a living enterprise operating system able to learn, expand, evolve, extract DNA, compose DNA, run DNA, improve behavior, and export new DNA under governance.

## Security
- Credentials, database URLs, tokens, access keys, private paths, and runtime dumps are never part of this architecture document.
- Data access must follow tenant, role, mission, department, project, and policy constraints.
- Sensitive records must support redaction, encryption, retention rules, and audit trails.
- Cross-store joins must happen through governed services or approved analytics views, not ad hoc credential sharing.

## Acceptance Criteria
- Official documentation uses `Mariam Data Platform`, not `legacy single-database wording` or `legacy single-database wording`.
- All listed components are represented as platform responsibilities.
- The document makes clear that Mariam is a living enterprise operating system, not merely an legacy narrow-core wording.
- Future implementation can derive storage tickets without inventing terminology.

## Traceability
| Source | Relationship |
| --- | --- |
| MAL-V21-DATA-PLATFORM-001 | Official data platform terminology and architecture. |
| Volume 21 Infrastructure | Infrastructure and operations reference. |
| Volume 27 Legacy Seed Analysis | Corrects legacy database terminology. |
| Volume 14 DNA Operating System | DNA extraction, composition, runtime, evolution, and export reference. |

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v129 draft | 2026-06-30 | Draft | Added official Mariam Data Platform terminology. |
