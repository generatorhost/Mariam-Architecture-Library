# Book 03.01.07 - Service Container

**Version:** v3 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-01-007

## Purpose
Define the Service Container that binds and resolves Enterprise Core services.

## Scope
Covers service registration, dependency resolution, scope, lifecycle hooks, and replacement rules.

## Responsibilities
- Register core services with explicit contracts.
- Resolve dependencies safely.
- Support service lifecycle hooks.
- Prevent circular or hidden dependencies.

## Inputs
- Service definitions.
- Dependency declarations.
- Kernel boot context.
- Configuration values.

## Outputs
- Service instances.
- Resolution diagnostics.
- Dependency graph.
- Service lifecycle events.

## Interfaces
- Kernel service lookup.
- Configuration provider.
- Lifecycle hooks.
- Health checks.

## Events
- ServiceRegistered
- ServiceResolved
- ServiceResolutionFailed
- ServiceDisposed

## Storage
- Service registry.
- Dependency graph snapshot.
- Resolution logs.

## Security
- Service resolution must respect caller authority where needed.
- Sensitive service configuration must not be logged.
- Privileged services must be explicitly marked.

## Metrics
- Resolution latency.
- Circular dependency count.
- Service startup failures.
- Privileged service access attempts.

## Tests
- Dependency graph tests.
- Circular dependency tests.
- Privileged resolution tests.
- Service disposal tests.

## Acceptance Criteria
- Core services have explicit interfaces.
- Invalid dependency graphs fail fast.
- Service lifecycle is observable.

## Traceability
- MAL-V00-B012
- MAL-V02-B003
- MAL-V02-B018

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v3 draft | 2026-06-29 | Draft | Initial Enterprise Core blueprint content for Mariam Architecture Library v3. |
