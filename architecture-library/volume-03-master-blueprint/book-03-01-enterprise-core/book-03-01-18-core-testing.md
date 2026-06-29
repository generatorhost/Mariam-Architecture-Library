# Book 03.01.18 - Core Testing

**Version:** v3 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-01-018

## Purpose
Define the testing blueprint for Enterprise Core subsystems.

## Scope
Covers unit, integration, system, security, performance, recovery, and acceptance testing for the core.

## Responsibilities
- Define test layers for core services.
- Map subsystem risks to test types.
- Establish release gating expectations.
- Prepare inputs for Volume 09 Testing Guide.

## Inputs
- Subsystem blueprints.
- Acceptance criteria.
- Security controls.
- Runtime and lifecycle states.

## Outputs
- Core test matrix.
- Acceptance test scenarios.
- Security test requirements.
- Performance and recovery test targets.

## Interfaces
- CI test runner interface.
- Runtime test harness.
- Security test hooks.
- Observability verification.

## Events
- TestPlanCreated
- CoreTestStarted
- CoreTestFailed
- CoreAcceptancePassed

## Storage
- Test result records.
- Coverage reports.
- Failure evidence.
- Acceptance signoff records.

## Security
- Security tests must avoid real secrets.
- Test fixtures must isolate tenant data.
- Privileged test paths must be explicit.

## Metrics
- Test pass rate.
- Coverage by subsystem.
- Flaky test rate.
- Mean time to diagnose failures.

## Tests
- Unit tests for service logic.
- Integration tests for subsystem contracts.
- Security tests for protected actions.
- Recovery tests for lifecycle and storage.

## Acceptance Criteria
- Every core subsystem has named test expectations.
- Acceptance tests map to blueprint criteria.
- Build verification includes PDF and ZIP checks.

## Traceability
- MAL-V00-B010
- MAL-V00-B012
- MAL-V02-B003

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v3 draft | 2026-06-29 | Draft | Initial Enterprise Core blueprint content for Mariam Architecture Library v3. |
