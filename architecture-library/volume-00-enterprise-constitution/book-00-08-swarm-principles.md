# Book 00-08 - Swarm Principles

**Version:** v1 draft
**Status:** Draft
**Document ID:** MAL-V00-B008


## Purpose
Define how multiple agents, services, and contributors coordinate within Mariam.

## Scope
Covers agent collaboration, task decomposition, consensus, escalation, and conflict handling.

## Principles
- Swarm behavior must be orchestrated, not chaotic.
- Specialized agents require clear contracts.
- Conflicts should surface as reviewable events.

## Operating Rules
- Assign every agent a bounded role and output contract.
- Record handoffs between agents when work affects authoritative outputs.
- Escalate unresolved contradictions to human review.

## Acceptance Criteria
- Swarm workflows can be tested with deterministic scenarios.
- Agent outputs can be traced to source context.
- Coordination failures are observable.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v1 draft | 2026-06-29 | Draft | Initial canonical draft for the Mariam Architecture Library. |
