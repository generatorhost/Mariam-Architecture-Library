# Book 02-04 - Phase 02 Enterprise Organization

**Version:** v2 draft
**Status:** Draft
**Document ID:** MAL-V02-B004


## Purpose
Model how organizations structure teams, units, responsibilities, and operating rhythms inside Mariam.

## Scope
Covers teams, departments, reporting context, ownership, handoffs, operating cadences, and organization memory.

## Strategic Objective
Turn enterprise structure into a usable system layer for accountability and coordination.

## Systems Included
- Organization graph
- Team and department registry
- Ownership model
- Handoff rules
- Operating cadence templates

## Main Deliverables
- Organization model specification
- Team setup workflows
- Ownership assignment rules
- Handoff record format
- Operating rhythm templates

## Dependencies
- Enterprise core identity, role, and tenant primitives.
- Remote work strategy and governance principles.
- Canonical definitions for team, unit, owner, and accountable party.

## Risks
- Organization models can become too rigid for real companies.
- Handoffs can create bureaucratic overhead if not ergonomic.
- Ownership data may become stale without maintenance flows.

## Acceptance Criteria
- Teams and owners can be represented without custom code per organization.
- Handoffs preserve accountability and context.
- Organization updates are auditable.

## Implementation Notes
- Support lightweight setup before complex hierarchy.
- Allow matrix and project-based structures.
- Design organization data to improve workflow routing.

## Traceability
- MAL-V00-B005
- MAL-V00-B009
- MAL-V01-B006

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v2 draft | 2026-06-29 | Draft | Initial roadmap phase definition for Mariam Architecture Library v2. |
