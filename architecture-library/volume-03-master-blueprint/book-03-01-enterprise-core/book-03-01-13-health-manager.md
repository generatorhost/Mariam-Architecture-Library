# Book 03.01.13 - Health Manager

**Version:** v3 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-01-013

## Purpose
Define health management for Enterprise Core subsystems, services, and runtimes.

## Scope
Covers readiness, liveness, degradation, dependency checks, incident signals, and health reporting.

## Responsibilities
- Collect health checks from core subsystems.
- Determine readiness and liveness state.
- Surface degradation and incidents.
- Feed lifecycle decisions.

## Inputs
- Subsystem health reports.
- Runtime status.
- Dependency check results.
- Configuration thresholds.

## Outputs
- Health status records.
- Readiness decisions.
- Incident signals.
- Health dashboards data.

## Interfaces
- Kernel readiness API.
- Runtime manager health API.
- Observability metrics interface.
- Event bus health topics.

## Events
- HealthCheckReported
- CoreReady
- CoreDegraded
- CoreUnhealthy
- IncidentSignalRaised

## Storage
- Health snapshots.
- Dependency check history.
- Incident signal records.

## Security
- Health checks must not expose secrets.
- Administrative health detail requires authorization.
- Incident signals must preserve tenant boundaries.

## Metrics
- Readiness pass rate.
- Health check latency.
- Degradation duration.
- Incident signal count.

## Tests
- Readiness tests.
- Dependency failure tests.
- Health authorization tests.
- Degradation event tests.

## Acceptance Criteria
- Core readiness reflects subsystem health.
- Degradation is observable.
- Health data is safe to expose at each authorization level.

## Traceability
- MAL-V00-B010
- MAL-V02-B018
- MAL-V03-B03-01-003

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v3 draft | 2026-06-29 | Draft | Initial Enterprise Core blueprint content for Mariam Architecture Library v3. |
