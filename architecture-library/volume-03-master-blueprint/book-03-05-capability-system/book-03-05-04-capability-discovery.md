# Book 03.05.04 - Capability Discovery

**Version:** v7 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-05-004

## Purpose
Define discovery of available capabilities by domain, task, role, agent, workflow, quality bar, and permission context as part of the Mariam Capability System blueprint.

## Scope
This document covers architecture-level responsibilities, contracts, data, events, controls, metrics, tests, and acceptance rules for discovery of available capabilities by domain, task, role, agent, workflow, quality bar, and permission context. It does not implement system code or approve unreviewed automation.

## Responsibilities
- Establish the canonical boundary for discovery of available capabilities by domain, task, role, agent, workflow, quality bar, and permission context.
- Convert repeatable work patterns into governed, reusable capability contracts.
- Coordinate with Enterprise Core, AI Society, Knowledge System, and future Workflow System interfaces.
- Provide implementation-ready constraints for future capability specifications and runtime execution.

## Inputs
- Enterprise Constitution enterprise, AI, quality, security, governance, and engineering principles.
- Master Roadmap Phase 05 Capability System requirements.
- Enterprise Core identity, runtime, event, storage, security, and observability contracts.
- AI Society skills, agents, planning, validation, and governance needs.
- Knowledge System retrieval, provenance, and quality signals.

## Outputs
- Blueprint contract for discovery of available capabilities by domain, task, role, agent, workflow, quality bar, and permission context.
- Capability records, dependency links, requirements, benchmarks, lifecycle states, and governance evidence.
- Traceable inputs for Volume 06 specifications and Volume 13 Capability System expansion.
- Acceptance evidence for matching, ranking, invocation, quality, security, and lifecycle gates.

## Interfaces
- Enterprise Core object manager, runtime manager, event bus, storage, security, and observability interfaces.
- AI Society agent, skill, capability, execution, validation, and governance interfaces.
- Knowledge System search, graph, metadata, quality, and provenance interfaces.
- Future DNA Operating System, Workflow System, Marketplace, and Evolution System interfaces.

## Events
- CapabilityDiscoveryDefined
- CapabilityDiscoveryRegistered
- CapabilityDiscoveryMatched
- CapabilityDiscoveryInvoked
- CapabilityDiscoveryRetired

## Storage
- Capability definitions with owner, version, state, input contract, output contract, constraints, and permission metadata.
- Capability graph records for prerequisites, dependencies, alternatives, compositions, and domain fit.
- Invocation, benchmark, review, exception, and acceptance evidence.
- Audit metadata linking capability use to user intent, agent role, workflow context, model choice, and policy status.

## Security
- Apply least privilege to capability invocation, tool access, model use, knowledge retrieval, and protected actions.
- Deny capability execution when required policies, permissions, data classifications, or review gates are missing.
- Classify capability inputs, outputs, logs, benchmarks, and evidence before storage or sharing.
- Audit privileged capability registration, invocation, exception, deprecation, and replacement decisions.

## Metrics
- Capability discovery rate, match precision, ranking quality, invocation success, and fallback rate.
- Quality score, benchmark pass rate, review rejection rate, defect rate, and rework count.
- Cost, latency, throughput, usage by domain, adoption by role, and business outcome contribution.
- Security denial count, governance exception count, stale capability count, and deprecation completion rate.

## Tests
- Contract tests for capability definitions, requirements, dependencies, and event envelopes.
- Matching and ranking evaluation tests with known work-intent scenarios.
- Security tests for protected actions, tenant isolation, tool permissions, and data classification.
- Lifecycle tests for proposal, approval, active use, deprecation, retirement, and replacement.

## Acceptance Criteria
- Capability Discovery has explicit contracts, ownership, lifecycle, security, metrics, and governance controls.
- Events, storage records, metrics, and tests are defined well enough for downstream specifications.
- Capability use remains traceable to approved requirements, policies, evidence, and runtime context.
- Traceability links this blueprint to Volume 00, Volume 02, Book 03.01, Book 03.03, and Book 03.04.

## Traceability
- MAL-V00-B010
- MAL-V00-B011
- MAL-V00-B012
- MAL-V02-B007
- MAL-V03-B03-01-004
- MAL-V03-B03-03-008
- MAL-V03-B03-04-015

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v7 draft | 2026-06-29 | Draft | Initial Capability System blueprint content for Mariam Architecture Library v7. |
