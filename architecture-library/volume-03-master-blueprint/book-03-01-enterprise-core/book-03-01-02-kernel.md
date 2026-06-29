# Book 03.01.02 - Kernel

**Version:** v3 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-01-002

## Purpose
Define the Mariam Kernel as the minimal trusted coordinator for core boot, service access, and platform invariants.

## Scope
Covers kernel responsibilities, allowed dependencies, startup responsibilities, core service exposure, and failure boundaries.

## Responsibilities
- Own the platform boot sequence.
- Expose stable access to core services.
- Enforce core invariants before subsystem startup.
- Prevent domain modules from coupling directly to infrastructure details.

## Inputs
- Boot configuration.
- Runtime registry definitions.
- Service container bindings.
- Identity and security policy handles.

## Outputs
- Kernel readiness state.
- Core service handles.
- Kernel lifecycle events.
- Boot diagnostics.

## Interfaces
- Kernel boot API.
- Service container interface.
- Runtime manager interface.
- Health manager interface.

## Events
- KernelBootRequested
- KernelBooted
- KernelInvariantFailed
- KernelShutdownRequested

## Storage
- Kernel boot log.
- Core invariant registry.
- Kernel state snapshot.

## Security
- Only trusted boot code can mutate kernel state.
- Kernel APIs must validate caller context.
- Boot diagnostics must not expose secrets.

## Metrics
- Boot duration.
- Invariant failure count.
- Kernel panic count.
- Service resolution latency.

## Tests
- Kernel boot unit tests.
- Invariant failure tests.
- Unauthorized service access tests.
- Shutdown sequence tests.

## Acceptance Criteria
- Kernel boots with required services available.
- Kernel refuses unsafe startup state.
- Kernel shutdown is orderly and observable.

## Traceability
- MAL-V00-B011
- MAL-V00-B012
- MAL-V02-B003

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v3 draft | 2026-06-29 | Draft | Initial Enterprise Core blueprint content for Mariam Architecture Library v3. |
