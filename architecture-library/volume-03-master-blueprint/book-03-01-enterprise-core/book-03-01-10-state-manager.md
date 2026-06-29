# Book 03.01.10 - State Manager

**Version:** v3 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-01-010

## Purpose
Define the State Manager responsible for controlled state transitions inside the Enterprise Core.

## Scope
Covers state ownership, transition validation, persistence expectations, consistency, and recovery.

## Responsibilities
- Own canonical core state transitions.
- Validate state changes against lifecycle rules.
- Expose state snapshots to authorized services.
- Support recovery after failure.

## Inputs
- State transition commands.
- Current state snapshots.
- Lifecycle constraints.
- Caller context.

## Outputs
- Accepted state changes.
- Rejected transition records.
- State snapshots.
- Recovery checkpoints.

## Interfaces
- Lifecycle manager interface.
- Storage interface.
- Event bus state events.
- Health manager state checks.

## Events
- StateChangeRequested
- StateChanged
- StateChangeRejected
- StateRecovered

## Storage
- State snapshot store.
- Transition journal.
- Recovery checkpoints.

## Security
- State mutations require authorized callers.
- Sensitive state values must be classified.
- Recovery data must preserve tenant boundaries.

## Metrics
- Transition success rate.
- Rejected transition count.
- State recovery time.
- Snapshot write latency.

## Tests
- State transition tests.
- Invalid mutation tests.
- Recovery tests.
- Concurrent state update tests.

## Acceptance Criteria
- State transitions are validated and observable.
- Invalid mutations are rejected.
- Recovery restores a consistent state.

## Traceability
- MAL-V00-B010
- MAL-V02-B009
- MAL-V02-B011

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v3 draft | 2026-06-29 | Draft | Initial Enterprise Core blueprint content for Mariam Architecture Library v3. |
