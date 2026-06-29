# Book 03.01.14 - Core Events

**Version:** v3 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-01-014

## Purpose
Define the canonical event taxonomy for Enterprise Core.

## Scope
Covers event naming, envelopes, categories, severity, correlation, causation, and retention expectations.

## Responsibilities
- Standardize core event names.
- Define required event envelope fields.
- Classify event severity and category.
- Support traceability across subsystem boundaries.

## Inputs
- Subsystem event proposals.
- Event bus envelope requirements.
- Audit and observability needs.
- Security classification rules.

## Outputs
- Core event catalog.
- Event envelope standard.
- Retention guidance.
- Correlation and causation rules.

## Interfaces
- Event bus publisher interface.
- Audit log interface.
- Observability trace interface.
- Storage retention interface.

## Events
- CoreEventDefined
- CoreEventDeprecated
- CoreEventEmitted
- CoreEventRejected

## Storage
- Event catalog.
- Event schema history.
- Event retention metadata.

## Security
- Event payloads must be classified.
- Protected event streams require authorization.
- Event retention must respect data policy.

## Metrics
- Event schema coverage.
- Malformed event count.
- Correlation coverage.
- Protected stream access denial count.

## Tests
- Event schema validation tests.
- Correlation propagation tests.
- Protected event access tests.
- Deprecated event tests.

## Acceptance Criteria
- Core events follow naming and envelope rules.
- Events can be correlated across subsystems.
- Sensitive events are protected.

## Traceability
- MAL-V00-B009
- MAL-V00-B011
- MAL-V02-B011

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v3 draft | 2026-06-29 | Draft | Initial Enterprise Core blueprint content for Mariam Architecture Library v3. |
