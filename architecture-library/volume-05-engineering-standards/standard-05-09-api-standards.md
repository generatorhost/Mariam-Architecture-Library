# API Standards

**Version:** v24 draft
**Status:** Draft
**Document ID:** MAL-V05-STD-009

## Purpose
Define mandatory engineering expectations for API contracts, schemas, errors, pagination, authentication, idempotency, and compatibility in Mariam AI Enterprise OS.

## Scope
This standard applies to documentation, specifications, implementation plans, code reviews, generated artifacts, tests, operations, and release evidence whenever work touches API contracts, schemas, errors, pagination, authentication, idempotency, and compatibility.

## Mandatory Rules
- Every change must trace to an approved document ID, roadmap phase, blueprint, specification, issue, or release note.
- Interfaces, events, storage records, and security controls must be documented before implementation.
- Generated artifacts must be reproducible from repository content and listed in `MANIFEST.json`.
- Security-sensitive behavior must include least-privilege controls, audit evidence, and failure behavior.
- Acceptance criteria must be written before a change is declared complete.
- Breaking changes must include migration, compatibility, and deprecation notes.
- Reviews must verify naming, versioning, tests, observability, and governance impact.

## Recommended Practices
- Prefer small, reversible changes with clear ownership and limited blast radius.
- Use canonical dictionary terms from Volume 04 in names, comments, APIs, events, and dashboards.
- Keep examples close to real operating workflows instead of abstract placeholders.
- Add concise diagrams or tables when they reduce ambiguity.
- Automate validation for repeated checks such as required sections, PDF generation, ZIP contents, and manifest checksums.
- Record tradeoffs when a standard is intentionally relaxed.

## Prohibited Practices
- Do not introduce code, configuration, event names, APIs, or storage schemas that conflict with the architecture library.
- Do not store secrets, credentials, private keys, tokens, or sensitive operational data in documentation or release artifacts.
- Do not ship generated artifacts without verifying readability and ZIP inclusion.
- Do not use undocumented autonomous behavior for AI, agents, workflows, providers, plugins, or connectors.
- Do not silently change document IDs, artifact names, or public contracts.
- Do not merge changes that lack tests or explicit risk acceptance.

## Required Evidence
- Relevant source document IDs and traceability references.
- Updated Markdown source files when behavior, terminology, or architecture changes.
- Passing build output for PDFs, ZIP package, and `MANIFEST.json`.
- Test results appropriate to risk: unit, integration, security, acceptance, performance, or release packaging.
- Review notes for exceptions, unresolved risks, and compatibility decisions.
- Artifact names, checksums, and release notes for versioned releases.

## Acceptance Criteria
- The standard can be applied by an engineer without additional verbal instruction.
- Mandatory rules, prohibited practices, and required evidence are specific enough for review.
- The standard aligns with Volumes 00 through 04 and does not contradict the Source of Truth model.
- Release artifacts include this standard in Markdown, PDF, ZIP, and manifest outputs.

## Traceability
- MAL-V00-B010
- MAL-V00-B011
- MAL-V00-B012
- MAL-V00-B014
- MAL-V04-README
- MAL-V05-STD-009

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v24 draft | 2026-06-29 | Draft | Initial engineering standard for API Standards. |
