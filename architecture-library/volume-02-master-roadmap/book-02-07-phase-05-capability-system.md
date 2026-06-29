# Book 02-07 - Phase 05 Capability System

**Version:** v2 draft
**Status:** Draft
**Document ID:** MAL-V02-B007


## Purpose
Define reusable capabilities as governed units of work that users, teams, and agents can invoke.

## Scope
Covers capability registry, inputs, outputs, permissions, evaluation, and lifecycle.

## Strategic Objective
Turn repeated work patterns into controlled platform capabilities rather than one-off automations.

## Systems Included
- Capability registry
- Capability contracts
- Input and output schemas
- Permission gates
- Capability evaluation

## Main Deliverables
- Capability model specification
- Reusable capability templates
- Lifecycle states
- Capability test checklist
- Dependency map

## Dependencies
- Enterprise core permissions.
- Knowledge system schemas.
- Engineering and quality principles.

## Risks
- Capabilities may overlap and create confusion.
- Weak contracts can make automation unsafe.
- Capability reuse may hide domain-specific requirements.

## Acceptance Criteria
- Each capability has a clear owner, contract, and allowed users.
- Capability outputs are testable.
- Capabilities can be deprecated or versioned.

## Implementation Notes
- Start with human-in-the-loop capabilities.
- Use capability contracts to keep agents and workflows aligned.
- Avoid making capabilities depend on hidden context.

## Traceability
- MAL-V00-B010
- MAL-V00-B012
- MAL-V01-B004

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v2 draft | 2026-06-29 | Draft | Initial roadmap phase definition for Mariam Architecture Library v2. |
