# Book 02-03 - Phase 01 Enterprise Core

**Version:** v2 draft
**Status:** Draft
**Document ID:** MAL-V02-B003


## Purpose
Define the first executable enterprise platform core for identity, tenancy, roles, and accountable records.

## Scope
Covers the minimum enterprise substrate required before advanced AI, marketplace, or automation modules.

## Strategic Objective
Create a stable core that can host governed workflows without relying on ad hoc permissions or records.

## Systems Included
- Identity and access core
- Tenant and organization model
- Role and permission model
- Audit event foundation
- Core entity registry

## Main Deliverables
- Enterprise core blueprint
- Core data model specification
- Permission matrix
- Audit event catalog
- Initial admin workflow specification

## Dependencies
- Foundation constitution and enterprise objectives.
- Canonical dictionary for core enterprise terms.
- Security principles for least privilege and auditability.

## Risks
- Overbuilding enterprise abstractions before workflows are validated.
- Under-scoping audit needs and forcing rewrites later.
- Confusing user identity with organization membership.

## Acceptance Criteria
- Core entities have owners and lifecycle states.
- Protected actions have role and audit rules.
- Future modules can reuse identity and tenant primitives.

## Implementation Notes
- Favor simple primitives that can support multiple domains.
- Keep access control explicit in specifications.
- Do not bind the core to a single deployment model yet.

## Traceability
- MAL-V00-B005
- MAL-V00-B011
- MAL-V01-B002

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v2 draft | 2026-06-29 | Draft | Initial roadmap phase definition for Mariam Architecture Library v2. |
