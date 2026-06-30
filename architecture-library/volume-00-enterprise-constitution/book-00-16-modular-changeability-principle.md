# Modular Changeability Principle

**Title:** Modular Changeability Principle  
**Version:** v130 draft  
**Status:** Draft  
**Document ID:** MAL-V00-B16

## Purpose
Define the constitutional rule that every governed object in Mariam is modular, lifecycle-managed, and changeable through approved operations. No capability, model, provider, workflow, agent, dashboard, connector, policy, or runtime object is treated as permanently fixed.

## Scope
- Applies to all Mariam Living Enterprise OS Core objects, including runtime objects, DNA packages, models, providers, workflows, agents, services, storage adapters, dashboards, reports, policies, and integrations.
- Defines mandatory lifecycle operations and governance controls.
- Excludes unsafe direct mutation, hidden bypasses, unapproved destructive operations, and changes that skip audit or compatibility checks.

## Principle
Every object in Mariam can be changed through a governed lifecycle. The system must support:
- Add
- Edit
- Delete
- Disable
- Enable
- Upgrade
- Replace
- Fork
- Rollback
- Export as DNA
- Import from DNA

## Operating Rules
- Add creates a new governed object with owner, version, permissions, dependencies, and acceptance criteria.
- Edit changes an object through versioned revisions, not silent mutation.
- Delete prefers soft delete first; hard delete requires explicit policy, retention, dependency, and audit checks.
- Disable removes an object from active execution while preserving state and evidence.
- Enable reactivates a valid object after compatibility and permission checks.
- Upgrade moves an object to a newer version with migration and rollback planning.
- Replace swaps an implementation or provider behind a stable contract after impact analysis.
- Fork creates a derived object with separate ownership, version lineage, and compatibility metadata.
- Rollback restores a previous approved version or state without erasing audit history.
- Export as DNA packages the object, metadata, dependencies, compatibility rules, and governance evidence.
- Import from DNA validates a package before registration, activation, or execution.

## Governance Requirements
- Governance: changes must follow approval policy according to risk, scope, and authority.
- Permission: only authorized roles may perform lifecycle operations.
- Versioning: every meaningful change must produce a traceable version or revision.
- Audit: every lifecycle transition must record actor, time, reason, input, output, decision, and evidence.
- Compatibility: dependency and interface compatibility must be checked before activation.
- Testing: changes require tests appropriate to the object type and risk level.
- Rollback: activation must define rollback or safe-disable behavior before production use.

## Acceptance Criteria
- New designs assume objects are changeable unless policy explicitly restricts the operation.
- Documentation and implementation tickets include lifecycle operations for add, edit, delete, disable, enable, upgrade, replace, fork, rollback, export, and import.
- No object can bypass governance, permissions, versioning, audit, compatibility, testing, or rollback.
- DNA export/import is treated as a first-class lifecycle operation.

## Traceability
| Source | Relationship |
| --- | --- |
| MAL-V00-B16 | Constitutional principle for modular changeability. |
| Volume 14 DNA Operating System | DNA managed runtime object model. |
| Volume 15 Runtime Ecosystem | Runtime/provider lifecycle reference. |
| Volume 21 Infrastructure | Runtime object governance reference. |

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v130 draft | 2026-06-30 | Draft | Added modular changeability principle. |
