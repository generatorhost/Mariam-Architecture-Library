# Book 03.01.20 - Core Roadmap

**Version:** v3 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-01-020

## Purpose
Define the implementation-facing roadmap for moving Enterprise Core from blueprint to specification and code.

## Scope
Covers sequencing, specification priorities, implementation slices, dependencies, migration concerns, and future expansion.

## Responsibilities
- Translate blueprint into build-ready phases.
- Identify first specifications to write.
- Sequence implementation around kernel, identity, lifecycle, runtime, storage, security, and observability.
- Preserve alignment with Volume 02 roadmap.

## Inputs
- Enterprise Core blueprint documents.
- Master Roadmap phase 01.
- Engineering standards backlog.
- Testing and operations guide needs.

## Outputs
- Core specification backlog.
- Implementation sequence proposal.
- Dependency map.
- Risk and migration notes.

## Interfaces
- Volume 06 specification queue.
- Volume 05 engineering standards.
- Volume 09 testing guide.
- System repository implementation issues.

## Events
- CoreRoadmapUpdated
- CoreSpecificationQueued
- CoreImplementationGateOpened
- CoreImplementationGateBlocked

## Storage
- Roadmap decision records.
- Specification backlog.
- Implementation gate evidence.

## Security
- Implementation must not begin without security and identity specifications.
- Roadmap records must avoid secrets.
- Code repository references must remain traceable to document IDs.

## Metrics
- Specification readiness count.
- Blocked dependency count.
- Implementation gate completion.
- Roadmap change frequency.

## Tests
- Roadmap consistency tests.
- Dependency completeness review.
- Traceability review.
- Implementation readiness checklist.

## Acceptance Criteria
- The roadmap identifies specification order.
- The roadmap blocks premature autonomy or marketplace work before core foundations.
- Implementation gates are traceable to blueprint acceptance.

## Traceability
- MAL-V00-B014
- MAL-V02-B003
- MAL-V03-B03-01-019

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v3 draft | 2026-06-29 | Draft | Initial Enterprise Core blueprint content for Mariam Architecture Library v3. |
