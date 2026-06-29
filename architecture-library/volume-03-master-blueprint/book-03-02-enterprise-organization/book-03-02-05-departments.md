# Book 03.02.05 - Departments

**Version:** v4 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-02-005

## Purpose
Define department architecture for stable enterprise functions and accountable operating units.

## Scope
Covers department identity, lifecycle, ownership, operating scope, staffing, and cross-department relationships.

## Responsibilities
- Create canonical department records.
- Assign department owners and operating scope.
- Track department lifecycle.
- Represent dependencies between departments.

## Inputs
- Department creation request.
- Department owner assignment.
- Operating scope definition.
- Staffing and role inputs.

## Outputs
- Department catalog.
- Department ownership records.
- Department lifecycle events.
- Dependency map.

## Interfaces
- Enterprise structure.
- Department missions.
- Roles responsibilities.
- Organization storage.

## Events
- DepartmentCreated
- DepartmentOwnerAssigned
- DepartmentScopeChanged
- DepartmentArchived

## Storage
- Department catalog store.
- Department dependency index.
- Ownership history.

## Security
- Department changes require organization authority.
- Department visibility respects tenant policies.
- Archived departments remain available for audit.

## Metrics
- Department count.
- Unowned department count.
- Scope change frequency.
- Dependency density.

## Tests
- Department lifecycle tests.
- Owner authorization tests.
- Dependency mapping tests.

## Acceptance Criteria
- Every active department has an owner and scope.
- Department relationships are visible.
- Department lifecycle changes are auditable.

## Traceability
- MAL-V00-B005
- MAL-V02-B004
- MAL-V03-B03-02-02

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v4 draft | 2026-06-29 | Draft | Initial Enterprise Organization blueprint content for Mariam Architecture Library v4. |
