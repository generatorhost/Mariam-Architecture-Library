# Book 03.01.15 - Core Storage

**Version:** v3 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-01-015

## Purpose
Define core storage responsibilities for Enterprise Core records and operational metadata.

## Scope
Covers logical stores, record ownership, retention, backup expectations, migration posture, and consistency.

## Responsibilities
- Define logical stores for core records.
- Support persistence for state, registry, audit, health, and configuration metadata.
- Declare retention and backup expectations.
- Avoid binding blueprint to one database product.

## Inputs
- Core record schemas.
- Retention policy inputs.
- Backup requirements.
- Storage classification.

## Outputs
- Logical storage map.
- Persistence requirements.
- Retention rules.
- Migration guidance.

## Interfaces
- State manager storage API.
- Object manager storage API.
- Audit store interface.
- Backup and recovery interface.

## Events
- StorageWriteRequested
- StorageWriteCommitted
- StorageReadDenied
- StorageRecoveryStarted

## Storage
- State snapshots.
- Runtime registry records.
- Object records.
- Audit references.
- Health snapshots.

## Security
- Encrypt sensitive storage where required.
- Authorize protected reads and writes.
- Keep tenant data isolated.

## Metrics
- Storage write latency.
- Read denial count.
- Backup success rate.
- Migration failure count.

## Tests
- Persistence tests.
- Tenant isolation storage tests.
- Backup restore tests.
- Migration compatibility tests.

## Acceptance Criteria
- Core storage map is documented.
- Protected records enforce access rules.
- Recovery expectations are explicit.

## Traceability
- MAL-V00-B011
- MAL-V02-B018
- MAL-V03-B03-01-010

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v3 draft | 2026-06-29 | Draft | Initial Enterprise Core blueprint content for Mariam Architecture Library v3. |
