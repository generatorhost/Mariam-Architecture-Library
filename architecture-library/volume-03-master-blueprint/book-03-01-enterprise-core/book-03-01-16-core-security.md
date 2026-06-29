# Book 03.01.16 - Core Security

**Version:** v3 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-01-016

## Purpose
Define security controls that every Enterprise Core subsystem must respect.

## Scope
Covers least privilege, tenant isolation, secrets, audit, policy enforcement, secure defaults, and threat-aware design.

## Responsibilities
- Set mandatory core security controls.
- Define protected action handling.
- Separate secrets from configuration.
- Ensure auditability of privileged operations.

## Inputs
- Security principles.
- Identity and access decisions.
- Configuration and secret provider data.
- Threat and risk assumptions.

## Outputs
- Core security control baseline.
- Protected action catalog.
- Audit requirements.
- Security acceptance checklist.

## Interfaces
- Identity access interface.
- Configuration secret provider.
- Audit event bus topics.
- Storage security hooks.

## Events
- ProtectedActionRequested
- ProtectedActionDenied
- SecretAccessed
- SecurityPolicyChanged

## Storage
- Protected action records.
- Security policy versions.
- Audit event store.
- Secret access metadata.

## Security
- Deny by default.
- Never store secrets in release artifacts.
- Audit privileged and denied actions.
- Keep tenant isolation explicit.

## Metrics
- Denied protected action count.
- Secret access count.
- Policy change count.
- Security test pass rate.

## Tests
- Least privilege tests.
- Secret redaction tests.
- Tenant isolation tests.
- Protected action audit tests.

## Acceptance Criteria
- Every core subsystem states security behavior.
- Protected actions are known and auditable.
- Secrets are separated from ordinary configuration.

## Traceability
- MAL-V00-B011
- MAL-V02-B016
- MAL-V02-B018

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v3 draft | 2026-06-29 | Draft | Initial Enterprise Core blueprint content for Mariam Architecture Library v3. |
