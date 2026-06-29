# Mariam Architecture Library

**Version:** v1 draft
**Status:** Draft
**Document ID:** MAL-ROOT-README

This repository is the official Source of Truth for Mariam AI Enterprise OS. It defines the enterprise constitution, product vision, engineering doctrine, operating model, specifications, testing rules, release artifacts, and traceability framework that govern all implementation work in the Mariam system repository.

No system code is authored here. This repository exists to make decisions explicit before code is written, to preserve architectural continuity across releases, and to give every contributor one canonical place to verify what Mariam is, how it evolves, and what standards must be satisfied.

## Purpose
Define the canonical documentation authority for Mariam AI Enterprise OS.

## Scope
This README covers repository purpose, library structure, and governance relationship to implementation work.

## Principles
- Documentation governs implementation.
- Architectural decisions must be durable, traceable, and versioned.
- The system repository must not become the first place where enterprise architecture is invented.

## Operating Rules
- Use this repository for architecture, strategy, standards, specifications, guides, releases, and traceability.
- Do not place product runtime code in this repository.
- Treat generated releases as documentation artifacts, not application builds.

## Library Structure
- `architecture-library/volume-00-enterprise-constitution/` defines identity, mission, principles, governance, quality, security, engineering, lifecycle, and long-term strategy.
- `architecture-library/volume-01-master-vision/` defines executive vision, objectives, domain strategy, ecosystem strategy, knowledge strategy, DNA strategy, and expansion direction.
- `architecture-library/volume-02-master-roadmap/` is reserved for staged delivery planning.
- `architecture-library/volume-03-master-blueprint/` is reserved for canonical architecture blueprints.
- `architecture-library/volume-04-canonical-dictionary/` is reserved for controlled terminology.
- `architecture-library/volume-05-engineering-standards/` is reserved for engineering rules.
- `architecture-library/volume-06-specifications/` is reserved for product and technical specifications.
- `architecture-library/volume-07-development-guide/` is reserved for contributor workflows.
- `architecture-library/volume-08-operations-guide/` is reserved for deployment, support, and operating procedures.
- `architecture-library/volume-09-testing-guide/` is reserved for verification and release testing.
- `architecture-library/releases/` contains generated release artifacts and notes.

## Governance
The documentation library controls implementation authority. Code changes in `generatorhost/Mariam` should trace to approved documents in this repository. When a code decision conflicts with this library, the library wins until a documented amendment is accepted.

## Acceptance Criteria
- The README identifies this repository as the Source of Truth.
- The README lists the canonical volume structure.
- The README states that no system code belongs in this repository.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v1 draft | 2026-06-29 | Draft | Initial repository README. |
