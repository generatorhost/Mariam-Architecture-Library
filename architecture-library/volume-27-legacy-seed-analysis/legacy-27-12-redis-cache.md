# Redis Cache

**Title:** Redis Cache
**Version:** v128 draft
**Status:** Draft
**Document ID:** MAL-V27-LEGACY-12

## Purpose
Document the safe legacy seed extracted from ai-business-os for the cache and ephemeral coordination pattern for sessions, queues, locks, rate limits, and live dashboard state. This document preserves historical product and infrastructure intent while preventing unsafe migration of code, secrets, runtime data, or implementation-specific coupling.

## Scope
- Captures the reusable pattern, user-facing role, integration boundary, storage implications, security constraints, and acceptance criteria.
- Applies to documentation-driven rebuild decisions in Mariam AI Enterprise OS.
- Excludes direct source code transfer, credentials, passwords, SSH material, raw runtime data, customer data, and environment files.

## Legacy Evidence Summary
- Legacy seed identified Redis Cache as a practical infrastructure or integration capability.
- Mariam should keep the architectural role, adapter boundary, health state, and governance requirements.
- No credentials, connection strings, local volumes, or runtime data are copied.

## Extracted Pattern
- Treat `Redis Cache` as a canonical capability candidate, not as copied implementation.
- Preserve the operating model: visible state, clear ownership, traceable events, auditable decisions, and dashboard-ready telemetry.
- Convert legacy naming into Mariam terminology through Canonical Dictionary alignment.
- Route all implementation through Blueprint, Specifications, Engineering Standards, and Experience Interface Design before code is written.

## Mariam Integration Target
- Register the capability as a governed RuntimeObject family or interface workspace where applicable.
- Connect state changes to Event Bus, Monitoring Center, Governance & Approvals, and relevant storage systems.
- Expose status, ownership, lifecycle phase, evidence, errors, and next actions in the Command Center.
- Use adapters for external services rather than embedding vendor-specific behavior in the core.

## Interfaces
- Runtime Ecosystem
- Connector Runtime
- Provider Runtime
- Infrastructure
- Operations Guide
- MANIFEST and release notes for documentation traceability.
- Security and governance review before implementation begins.

## Data Model Guidance
- Define canonical IDs, owner, tenant, lifecycle state, status, timestamps, provenance, trace ID, and policy version.
- Separate durable business records from ephemeral cache or live metric state.
- Store audit evidence for decisions, approvals, failures, retries, and manual interventions.
- Use schema versioning for legacy-derived patterns so future implementation can evolve safely.

## Events
- `legacy.seed.identified`
- `legacy.seed.reviewed`
- `legacy.seed.accepted`
- `legacy.seed.rejected`
- `legacy.seed.security_blocked`
- `legacy.seed.mapped_to_mariam`

## Security Controls
- Do not import secrets, passwords, SSH keys, tokens, database URLs, raw environment files, or runtime data.
- Redact any copied examples until only structural placeholders remain.
- Require security review before turning this seed into implementation tasks.
- Treat legacy service names as references only; current Mariam configuration must be generated fresh.

## What Was Explicitly Not Migrated
- passwords
- secrets
- API keys
- SSH private keys
- database connection strings
- runtime data dumps
- session tokens
- raw .env files
- MinIO access keys
- Postgres credentials
- Redis credentials
- n8n encryption keys
- Ollama local model paths containing user-private filesystem details
- Raw routes, raw schemas, raw Docker volumes, runtime database rows, and private local filesystem paths.

## Acceptance Criteria
- The document describes a reusable system pattern from ai-business-os without transferring unsafe implementation details.
- The integration target maps cleanly to existing Mariam volumes.
- Security exclusions are explicit and testable.
- Future code work can be planned from this document only after corresponding Specifications and implementation tickets are created.

## Traceability
| Source | Relationship |
| --- | --- |
| ai-business-os historical attachment | Legacy seed source; read-only and sanitized. |
| MAL-V27-LEGACY-12 | Safe v128 analysis of Redis Cache. |
| Volume 26 Experience & Interface Design | UI and dashboard integration reference. |
| Volume 06 Specifications | Implementation boundary reference. |
| Volume 21 Infrastructure | Runtime stack and operations reference where applicable. |

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v128 draft | 2026-06-30 | Draft | Added safe legacy seed analysis for Redis Cache. |
