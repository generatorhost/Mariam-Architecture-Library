# Book 03.02.06 - Department Missions

**Version:** v4 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-02-006

## Purpose
Define how missions are assigned, tracked, reviewed, and evolved for departments.

## Scope
Covers mission statements, strategic outcomes, operating commitments, dependencies, and review cadence.

## Responsibilities
- Attach missions to departments.
- Translate enterprise objectives into department commitments.
- Track mission dependencies and progress.
- Support mission review and revision.

## Inputs
- Enterprise objectives.
- Chief office mandates.
- Department scope.
- KPI targets.
- Dependency inputs.

## Outputs
- Department mission records.
- Mission dependency map.
- Mission review outcomes.
- Mission change events.

## Interfaces
- Chief office.
- Enterprise KPIs.
- Operating rhythm.
- Workflow system.

## Events
- DepartmentMissionAssigned
- MissionProgressReported
- MissionRevised
- MissionRetired

## Storage
- Mission store.
- Mission review history.
- Mission dependency records.

## Security
- Mission edits require owner or delegated authority.
- Sensitive mission data is classified.
- Mission retirement preserves history.

## Metrics
- Mission coverage by department.
- Mission progress reporting rate.
- Mission revision frequency.

## Tests
- Mission assignment tests.
- Authority tests.
- Dependency consistency tests.
- Mission review tests.

## Acceptance Criteria
- Every department can declare one or more missions.
- Missions trace to objectives or executive mandates.
- Mission changes are reviewable.

## Traceability
- MAL-V01-B002
- MAL-V02-B004
- MAL-V03-B03-02-04

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v4 draft | 2026-06-29 | Draft | Initial Enterprise Organization blueprint content for Mariam Architecture Library v4. |
