# Book 03.01.05 - Runtime Registry

**Version:** v3 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-01-005

## Purpose
Define the Runtime Registry as the canonical inventory of runtimes available to the Enterprise Core.

## Scope
Covers runtime metadata, allowed states, versioning, capability declarations, ownership, and compatibility rules.

## Responsibilities
- Store approved runtime definitions.
- Expose runtime lookup and compatibility metadata.
- Track runtime lifecycle status.
- Prevent unregistered runtime execution.

## Inputs
- Runtime manifests.
- Provider metadata.
- Compatibility requirements.
- Security classifications.

## Outputs
- Runtime catalog entries.
- Compatibility decisions.
- Runtime availability state.
- Registry change events.

## Interfaces
- Runtime manager lookup API.
- Configuration interface.
- Security policy interface.
- Manifest validation interface.

## Events
- RuntimeRegistered
- RuntimeUpdated
- RuntimeDeprecated
- RuntimeRejected

## Storage
- Runtime manifest store.
- Registry version history.
- Compatibility metadata records.

## Security
- Registry writes require administrative authority.
- Runtime manifests must be validated.
- Deprecated runtimes must remain traceable.

## Metrics
- Registry lookup latency.
- Manifest validation failure count.
- Deprecated runtime usage.
- Runtime catalog coverage.

## Tests
- Manifest validation tests.
- Registry permission tests.
- Compatibility lookup tests.
- Deprecation tests.

## Acceptance Criteria
- Every runtime has owner, version, status, and security classification.
- Runtime manager cannot start unknown runtimes.
- Registry changes are auditable.

## Traceability
- MAL-V00-B009
- MAL-V02-B009
- MAL-V02-B010

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v3 draft | 2026-06-29 | Draft | Initial Enterprise Core blueprint content for Mariam Architecture Library v3. |
