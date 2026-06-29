# Book 03.02.12 - Enterprise KPIs

**Version:** v4 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-02-012

## Purpose
Define enterprise KPI architecture across boards, chief office, departments, missions, and operating reviews.

## Scope
Covers KPI definitions, ownership, targets, measurement sources, review cadence, and interpretation.

## Responsibilities
- Maintain KPI catalog.
- Attach KPIs to owners and missions.
- Define measurement source and cadence.
- Support executive and department review.

## Inputs
- KPI definition.
- Measurement source.
- Target value.
- Owner role.
- Mission or objective link.

## Outputs
- KPI catalog records.
- KPI measurement snapshots.
- Target status.
- Review actions.

## Interfaces
- Chief office.
- Department missions.
- Operating rhythm.
- Observability metrics.

## Events
- KpiDefined
- KpiMeasured
- KpiTargetChanged
- KpiReviewActionCreated

## Storage
- KPI catalog store.
- Measurement history.
- Target revision history.

## Security
- KPI visibility follows business sensitivity.
- Measurement sources require provenance.
- Manipulated or disputed metrics are flagged.

## Metrics
- KPI coverage.
- Measurement freshness.
- Target miss rate.
- Disputed KPI count.

## Tests
- KPI definition tests.
- Measurement freshness tests.
- Ownership tests.
- Access control tests.

## Acceptance Criteria
- KPIs have owners, sources, cadence, and targets.
- KPI status can drive operating reviews.
- KPI changes are traceable.

## Traceability
- MAL-V01-B002
- MAL-V02-B004
- MAL-V03-B03-01-017

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v4 draft | 2026-06-29 | Draft | Initial Enterprise Organization blueprint content for Mariam Architecture Library v4. |
