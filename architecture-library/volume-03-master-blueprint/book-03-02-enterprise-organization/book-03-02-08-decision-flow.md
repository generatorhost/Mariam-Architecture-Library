# Book 03.02.08 - Decision Flow

**Version:** v4 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-02-008

## Purpose
Define how decisions move through enterprise roles, departments, chief office, and board governance.

## Scope
Covers decision proposals, routing, review, authority checks, outcomes, and decision records.

## Responsibilities
- Represent decision requests.
- Route decisions to accountable authorities.
- Record decision rationale and outcomes.
- Connect decisions to approvals and escalations.

## Inputs
- Decision proposal.
- Decision context.
- Authority matrix.
- Impact and risk classification.
- Supporting evidence.

## Outputs
- Decision route.
- Decision record.
- Decision outcome event.
- Follow-up actions.

## Interfaces
- Approval lines.
- Escalation model.
- Board governance.
- Event bus.

## Events
- DecisionProposed
- DecisionRouted
- DecisionApproved
- DecisionRejected
- DecisionDeferred

## Storage
- Decision record store.
- Rationale archive.
- Decision route history.

## Security
- Decision visibility follows classification.
- Decision authority is checked before approval.
- High-impact decisions require audit.

## Metrics
- Decision cycle time.
- Deferred decision count.
- Authority mismatch count.
- Decision trace completeness.

## Tests
- Decision routing tests.
- Authority validation tests.
- Decision record immutability tests.

## Acceptance Criteria
- Decisions have owners, routes, rationale, and outcomes.
- Authority mismatches are rejected or escalated.
- Decision records are traceable.

## Traceability
- MAL-V00-B009
- MAL-V02-B004
- MAL-V03-B03-02-10

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v4 draft | 2026-06-29 | Draft | Initial Enterprise Organization blueprint content for Mariam Architecture Library v4. |
