# Runtime Store Specification

**Version:** v26 draft
**Status:** Draft
**Specification ID:** MAL-V06-DNA-SPEC-008

## Related Blueprint Documents
- MAL-V03-B03-06-003
- MAL-V03-B03-06-README
- MAL-V03-B03-06-001
- MAL-V03-B03-01-008
- MAL-V05-STD-011
- MAL-V05-STD-012

## Purpose
Define executable requirements for runtime storage for package metadata, active mounts, locks, snapshots, indexes, and audit records in the Mariam DNA Operating System.

## Scope
This specification covers functional behavior, non-functional expectations, inputs, outputs, interfaces, events, storage, security, observability, failure handling, recovery, tests, and implementation notes for runtime storage for package metadata, active mounts, locks, snapshots, indexes, and audit records.

## Responsibilities
- Convert the DNA Operating System blueprint into implementation-ready subsystem requirements.
- Define package lifecycle behavior without allowing unreviewed package mutation or unsafe runtime side effects.
- Preserve provenance, compatibility, governance, security classification, and release evidence for DNA packages.
- Integrate with Enterprise Core configuration, identity access, runtime, event bus, storage, security, and observability.

## Functional Requirements
- The subsystem MUST validate DNA package metadata, schema version, source provenance, trust level, and tenant scope before activation.
- The subsystem MUST reject packages or operations that violate policy, dependency, compatibility, version, or security requirements.
- The subsystem MUST emit canonical events for import, validation, mount, unmount, reload, export, rejection, failure, and recovery.
- The subsystem MUST maintain deterministic state transitions for draft, staged, validated, mounted, active, degraded, deprecated, archived, and rejected package states.
- The subsystem MUST support dry-run validation before package activation.
- The subsystem MUST preserve enough evidence to reproduce package acceptance decisions.

## Non-Functional Requirements
- Package operations SHOULD be idempotent where repeated commands may occur after retries.
- Derived indexes, graphs, and runtime views MUST be rebuildable from canonical package and audit records.
- Protected package operations MUST include authorization, tenant context, correlation ID, and audit trail.
- Runtime package operations SHOULD degrade safely instead of corrupting active package state.
- Package validation and graph operations SHOULD provide deterministic output for identical inputs.

## Inputs
- DNA package archive, MDP metadata, Git reference, ZIP archive, exported package, or extracted DNA candidate.
- Caller identity, tenant context, role, policy, trust level, and requested operation.
- Runtime compatibility matrix, dependency constraints, package graph state, and configuration.
- Source provenance, checksum, signature, version, and classification metadata.

## Outputs
- Validated or rejected package records.
- Mounted package runtime objects, dependency locks, graph edges, version records, and compatibility decisions.
- Events, metrics, logs, traces, and audit records.
- Exportable package artifact or evolved DNA package where applicable.

## Public Interfaces
- `POST /dna/packages/import`
- `POST /dna/packages/validate`
- `POST /dna/packages/mount`
- `POST /dna/packages/unmount`
- `POST /dna/packages/export`
- `GET /dna/packages/{package_id}`
- `GET /dna/graph`

## Internal Interfaces
- Enterprise Core identity access guard.
- Configuration provider and secret provider where applicable.
- Runtime manager for activation and reload operations.
- Event bus for DNA lifecycle events.
- Core storage for package records, graph records, locks, and audit history.
- Observability pipeline for metrics, logs, traces, and health signals.

## Events
- RuntimeStoreRequested
- RuntimeStoreValidated
- RuntimeStoreRejected
- RuntimeStoreMounted
- RuntimeStoreStateChanged
- RuntimeStoreFailed
- RuntimeStoreRecovered

## Storage Requirements
- Store canonical package metadata, checksums, source references, version, compatibility, and trust records.
- Store graph nodes, dependency edges, locks, mount records, validation reports, and export evidence.
- Store immutable audit references for protected operations.
- Store derived indexes separately from canonical package records so they can be rebuilt.

## Security Requirements
- Enforce least privilege for import, validation, mount, hot reload, federation, export, and deletion.
- Deny packages from untrusted or unknown sources unless a policy exception is approved.
- Redact secrets from packages, metadata, logs, diagnostics, exports, and validation reports.
- Validate package paths and archive contents to prevent traversal, overwrite, or unauthorized file access.
- Audit privileged operations, denied operations, policy exceptions, and federation imports.

## Observability Requirements
- Emit metrics for validation time, mount time, dependency resolution time, import failures, rejected packages, active package count, and rollback count.
- Emit structured logs with package ID, version, tenant, operation, result, and correlation ID.
- Emit traces around import, validation, dependency resolution, mount, export, and recovery paths.
- Provide health signals for package graph integrity, runtime store consistency, and mounted package readiness.

## Failure Modes
- Invalid package schema, missing metadata, checksum mismatch, incompatible version, or dependency conflict.
- Unauthorized caller, missing tenant context, denied source, or policy exception required.
- Archive extraction failure, Git reference failure, storage write failure, event publication failure, or runtime mount failure.
- Hot reload leaves dependent services stale or degraded.
- Federation import conflicts with local package authority.

## Recovery Rules
- Roll back partially mounted packages to the last accepted runtime state.
- Rebuild package graph and indexes from canonical records after storage or index failure.
- Quarantine failed imports until review or explicit deletion.
- Retry idempotent archive, graph, and storage operations with bounded attempts.
- Require operator review for repeated validation, mount, export, or federation failures.

## Test Requirements
- Unit tests for schema validation, compatibility decisions, dependency resolution, and state transitions.
- Integration tests across identity access, runtime manager, event bus, storage, configuration, and observability.
- Security tests for archive traversal, untrusted sources, tenant isolation, secret redaction, and denied operations.
- Recovery tests for partial mount, hot reload failure, graph rebuild, and import rollback.
- Acceptance tests proving required events, records, metrics, and audit evidence exist.

## Acceptance Criteria
- The specification is detailed enough to implement without relying on undocumented package behavior.
- Functional and non-functional requirements are measurable and testable.
- Security, observability, failure, and recovery behavior are explicit.
- DNA package authority, provenance, validation, compatibility, and lifecycle are traceable.

## Implementation Notes
- Begin with read-only import and validation before enabling mount, hot reload, federation, or export.
- Keep package parsing isolated from runtime activation.
- Use structured metadata and typed records instead of free-form package state.
- Treat every compatibility bypass as a governance exception with an expiry.

## Traceability
- MAL-V06-DNA-SPEC-008
- MAL-V03-B03-06-003
- MAL-V03-B03-06-README
- MAL-V05-STD-011
- MAL-V05-STD-012
- MAL-V05-STD-013
- MAL-V06-CORE-SPEC-003
- MAL-V06-CORE-SPEC-008

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v26 draft | 2026-06-29 | Draft | Initial DNA Operating System specification. |
