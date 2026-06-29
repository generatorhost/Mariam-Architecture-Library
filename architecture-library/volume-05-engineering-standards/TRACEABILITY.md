# Volume 05 Traceability

**Version:** v24 draft
**Status:** Draft
**Document ID:** MAL-V05-TRACEABILITY

## Purpose
Map engineering standards to constitutional, dictionary, roadmap, and blueprint authority.

## Scope
Volume 05 defines engineering standards for architecture, documentation, naming, versioning, repositories, code, Python, runtime, APIs, events, storage, security, testing, quality, observability, PDF builds, releases, Git, CI/CD, and governance.

## Mandatory Rules
- Engineering work must follow the Source of Truth hierarchy in this repository.
- Standards apply to documentation and future implementation work.
- Exceptions must be explicit, temporary, owned, and traceable.

## Recommended Practices
- Apply standards during design, not only during final review.
- Keep evidence lightweight but complete.
- Use the canonical dictionary when choosing names.

## Prohibited Practices
- Do not implement against undocumented assumptions.
- Do not bypass security, testing, or release evidence because a change appears small.
- Do not treat generated artifacts as authoritative when Markdown sources disagree.

## Required Evidence
- Updated standards files.
- Generated PDF, ZIP, manifest, and release notes.
- Verification that every standard contains mandatory sections.

## Acceptance Criteria
- Administrative files and all 20 standards exist.
- Each standard contains practical mandatory rules, recommended practices, prohibited practices, required evidence, acceptance criteria, traceability, and version history.
- v24 release artifacts are generated and verified.

## Traceability
- MAL-V00-B012
- MAL-V00-B014
- MAL-V04-README

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v24 draft | 2026-06-29 | Draft | Initial Volume 05 administrative document. |
