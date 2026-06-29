# Book 03.01.09 - Identity Access

**Version:** v3 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-01-009

## Purpose
Define identity and access primitives required by the Enterprise Core.

## Scope
Covers users, service identities, tenant context, roles, permissions, authorization checks, and audit decisions.

## Responsibilities
- Represent human and service identities.
- Resolve tenant and organization context.
- Authorize protected core actions.
- Emit audit evidence for access decisions.

## Inputs
- Authentication assertions.
- Tenant context.
- Role assignments.
- Permission policies.
- Service identity manifests.

## Outputs
- Authorization decisions.
- Identity context objects.
- Access audit events.
- Denied action records.

## Interfaces
- Kernel authorization guard.
- Service container privileged resolution.
- Event bus topic authorization.
- Audit event interface.

## Events
- IdentityContextResolved
- AuthorizationGranted
- AuthorizationDenied
- RoleBindingChanged

## Storage
- Identity records references.
- Role binding records.
- Permission policy versions.
- Access audit log.

## Security
- Use least privilege for humans and services.
- Deny by default for protected actions.
- Audit denied and privileged actions.

## Metrics
- Authorization latency.
- Denied action count.
- Privileged action count.
- Role binding change rate.

## Tests
- Permission matrix tests.
- Tenant isolation tests.
- Service identity tests.
- Denied action audit tests.

## Acceptance Criteria
- Protected core actions require authorization.
- Tenant context is explicit.
- Access decisions are auditable.

## Traceability
- MAL-V00-B005
- MAL-V00-B011
- MAL-V02-B003

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v3 draft | 2026-06-29 | Draft | Initial Enterprise Core blueprint content for Mariam Architecture Library v3. |
