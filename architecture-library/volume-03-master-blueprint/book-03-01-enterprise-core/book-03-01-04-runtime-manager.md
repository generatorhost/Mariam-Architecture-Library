# Book 03.01.04 - Runtime Manager

**Version:** v3 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-01-004

## Purpose
Define the Runtime Manager that supervises executable runtimes inside the Enterprise Core.

## Scope
Covers runtime creation, supervision, registration, isolation expectations, restart policy, and lifecycle integration.

## Responsibilities
- Start and stop approved runtimes.
- Coordinate runtime lifecycle with kernel state.
- Enforce runtime registration rules.
- Surface runtime health and failure events.

## Inputs
- Runtime definitions.
- Kernel lifecycle state.
- Configuration values.
- Runtime registry entries.

## Outputs
- Runtime instances.
- Runtime status records.
- Runtime failure events.
- Restart decisions.

## Interfaces
- Runtime registry API.
- Lifecycle manager API.
- Health manager API.
- Event bus topics.

## Events
- RuntimeStartRequested
- RuntimeStarted
- RuntimeFailed
- RuntimeRestarted
- RuntimeStopped

## Storage
- Runtime instance records.
- Runtime status journal.
- Restart history.

## Security
- Runtime actions require explicit permission.
- Runtime isolation boundaries must be documented.
- Runtime errors must not leak sensitive payloads.

## Metrics
- Runtime uptime.
- Restart count.
- Runtime startup latency.
- Failure recovery time.

## Tests
- Runtime startup tests.
- Restart policy tests.
- Unauthorized runtime action tests.
- Failure event tests.

## Acceptance Criteria
- Runtime manager supervises approved runtimes only.
- Runtime failures are observable.
- Restart policy is bounded and documented.

## Traceability
- MAL-V00-B012
- MAL-V02-B009
- MAL-V02-B010

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v3 draft | 2026-06-29 | Draft | Initial Enterprise Core blueprint content for Mariam Architecture Library v3. |
