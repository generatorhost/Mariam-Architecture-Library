# Book 03.02.17 - Organization Security

**Version:** v4 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-02-017

## Purpose
Define security controls for organization data, roles, approvals, decisions, KPIs, and governance records.

## Scope
Covers least privilege, tenant isolation, role visibility, audit, sensitive records, and administrative authority.

## Responsibilities
- Enforce least privilege across organization subsystems.
- Classify sensitive organization records.
- Audit protected organization changes.
- Prevent unauthorized approval or role escalation.

## Inputs
- Identity context.
- Role binding.
- Record classification.
- Approval authority.
- Governance policy.

## Outputs
- Security control baseline.
- Protected action catalog.
- Audit requirements.
- Access denial events.

## Interfaces
- Identity access.
- Core security.
- Approval lines.
- Organization storage.

## Events
- OrganizationProtectedActionRequested
- OrganizationAccessDenied
- RoleEscalationBlocked
- OrganizationPolicyChanged

## Storage
- Protected action catalog.
- Organization access audit log.
- Policy version records.

## Security
- Deny by default for protected organization actions.
- Privileged role changes require audit.
- Sensitive organization records are classified.

## Metrics
- Access denial count.
- Privileged change count.
- Policy change count.
- Security test pass rate.

## Tests
- Least privilege tests.
- Role escalation tests.
- Protected action tests.
- Sensitive record access tests.

## Acceptance Criteria
- Protected organization actions require authorization.
- Role escalation is controlled.
- Sensitive records remain tenant-scoped and auditable.

## Traceability
- MAL-V00-B011
- MAL-V03-B03-01-016
- MAL-V03-B03-02-07

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v4 draft | 2026-06-29 | Draft | Initial Enterprise Organization blueprint content for Mariam Architecture Library v4. |
