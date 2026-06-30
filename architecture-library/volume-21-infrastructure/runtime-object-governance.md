# Runtime Object Governance

**Title:** Runtime Object Governance  
**Version:** v130 draft  
**Status:** Draft  
**Document ID:** MAL-V21-RUNTIME-GOVERNANCE-001

## Purpose
Define infrastructure governance for runtime object lifecycle operations in Mariam.

## Scope
- Covers runtime object lifecycle, add/edit/delete lifecycle, soft delete, hard delete, disable/enable, dependency checks, impact analysis, approval workflow, rollback, and audit logs.
- Applies to runtime objects, DNA managed objects, providers, models, workflows, services, dashboards, scrapers, APIs, MCP servers, policies, and storage adapters.

## Runtime Object Lifecycle
- Draft: object exists as proposed configuration or imported DNA.
- Registered: object has identity, owner, version, permissions, and metadata.
- Validated: object passes schema, compatibility, dependency, and security checks.
- Approved: governance permits activation or operational use.
- Enabled: object is active and routable.
- Disabled: object is retained but not routable.
- Deprecated: object is allowed only for migration or historical use.
- Deleted: object is removed according to soft or hard delete rules.
- Rolled Back: object returns to a previous approved state.

## Add/Edit/Delete Lifecycle
- Add requires registration, owner, version, permissions, tests, and activation approval.
- Edit requires revision history, compatibility check, impact analysis, and audit evidence.
- Delete requires dependency analysis, retention policy, approval, and recovery plan.

## Soft Delete
Soft delete hides or deactivates an object while preserving records, dependencies, audit history, and rollback evidence. It is the default deletion mode for operational objects.

## Hard Delete
Hard delete permanently removes eligible records only after retention, legal, security, governance, dependency, backup, and audit requirements are satisfied.

## Disable and Enable
- Disable stops routing and execution without destroying identity or history.
- Enable requires compatibility checks, health checks, policy checks, and activation audit.

## Dependency Checks
Before delete, disable, replace, upgrade, fork, rollback, or import, the system must inspect dependent missions, workflows, agents, providers, dashboards, reports, policies, storage adapters, APIs, MCP servers, and DNA packages.

## Impact Analysis
Impact analysis must estimate affected users, missions, workflows, data stores, providers, costs, permissions, integrations, dashboards, reports, and rollback paths.

## Approval Workflow
Approval requirements depend on risk, privilege, external effects, customer impact, data sensitivity, runtime criticality, and governance policy.

## Rollback
Rollback restores a previous approved version or state while preserving audit history. Rollback must be tested or have a documented safe-disable alternative.

## Audit Logs
Audit logs must record object ID, operation, actor, permission, timestamp, reason, previous version, new version, dependency result, approval result, and rollback target.

## Acceptance Criteria
- Runtime objects have a documented lifecycle.
- Add, edit, delete, soft delete, hard delete, disable, enable, dependency checks, impact analysis, approvals, rollback, and audit logs are required.
- Governance supports modular changeability without unsafe hidden mutation.

## Traceability
| Source | Relationship |
| --- | --- |
| MAL-V21-RUNTIME-GOVERNANCE-001 | Runtime object governance definition. |
| MAL-V00-B16 | Constitutional modular changeability principle. |
| MAL-V14-DNA-RUNTIME-OBJECTS-001 | DNA managed object reference. |

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v130 draft | 2026-06-30 | Draft | Added runtime object governance. |
