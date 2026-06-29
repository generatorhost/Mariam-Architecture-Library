# Book 03.01.03 - Lifecycle

**Version:** v3 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-01-003

## Purpose
Define lifecycle states and transitions for Enterprise Core startup, operation, degradation, maintenance, and shutdown.

## Scope
Covers lifecycle state machines for the core platform and subsystem readiness.

## Responsibilities
- Define canonical lifecycle states.
- Coordinate subsystem startup and shutdown.
- Expose degradation and maintenance modes.
- Prevent invalid state transitions.

## Inputs
- Kernel state.
- Subsystem readiness reports.
- Runtime manager commands.
- Health manager signals.

## Outputs
- Lifecycle transition records.
- Readiness decisions.
- Maintenance mode state.
- Shutdown completion signals.

## Interfaces
- Kernel lifecycle hooks.
- Runtime manager lifecycle API.
- Event bus lifecycle topics.
- Health manager readiness API.

## Events
- LifecycleTransitionRequested
- LifecycleTransitionAccepted
- LifecycleTransitionRejected
- LifecycleStateChanged

## Storage
- Lifecycle transition journal.
- Readiness snapshots.
- Maintenance window records.

## Security
- Lifecycle transitions require authorized caller context.
- Rejected transitions must be auditable.
- Maintenance mode must preserve access-control boundaries.

## Metrics
- Transition success rate.
- Average startup time.
- Shutdown completion time.
- Invalid transition attempts.

## Tests
- State machine transition tests.
- Unauthorized transition tests.
- Degraded mode tests.
- Recovery transition tests.

## Acceptance Criteria
- All lifecycle states are defined.
- Invalid transitions are rejected and logged.
- Subsystem readiness gates core availability.

## Traceability
- MAL-V00-B010
- MAL-V00-B014
- MAL-V02-B009

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v3 draft | 2026-06-29 | Draft | Initial Enterprise Core blueprint content for Mariam Architecture Library v3. |
