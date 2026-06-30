# Security Exclusions

**Title:** Security Exclusions
**Version:** v128 draft
**Status:** Draft
**Document ID:** MAL-V27-SECURITY-001

## Purpose
Define what was intentionally blocked while extracting legacy seed patterns from ai-business-os.

## Scope
This document applies to all Volume 27 legacy seed analysis and any future implementation work derived from it.

## Blocked Materials
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
- Raw source code copied directly from old systems.
- Raw routes, schemas, runtime tables, Docker volumes, logs, object storage contents, and customer records.
- Any value that could grant access to a system, account, database, object store, cache, local model directory, workflow automation instance, or private repository.

## Allowed Materials
- System names.
- Architectural roles.
- UI and workflow patterns.
- Adapter boundaries.
- Storage responsibilities.
- Event and metric categories.
- Governance and acceptance requirements.

## Acceptance Criteria
- No blocked material appears in Volume 27.
- All legacy-derived systems are described as patterns and integration targets, not direct migrations.
- Any future implementation must create fresh configuration and secrets through approved secure channels.

## Traceability
| Source | Relationship |
| --- | --- |
| ai-business-os historical material | Read-only legacy source. |
| Volume 27 | Sanitized architecture seed analysis. |

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v128 draft | 2026-06-30 | Draft | Added security exclusions for legacy seed integration. |
