# Book 02-06 - Phase 04 Knowledge System

**Version:** v2 draft
**Status:** Draft
**Document ID:** MAL-V02-B006


## Purpose
Define the knowledge layer that captures, validates, retrieves, and evolves enterprise memory.

## Scope
Covers knowledge objects, provenance, approval states, freshness, retrieval, and correction.

## Strategic Objective
Make work output reusable and trustworthy across users, teams, agents, and workflows.

## Systems Included
- Knowledge object model
- Source and provenance tracking
- Approval and freshness states
- Search and retrieval strategy
- Correction and supersession workflows

## Main Deliverables
- Knowledge schema specification
- Knowledge lifecycle policy
- Retrieval acceptance tests
- Provenance metadata rules
- Knowledge governance workflows

## Dependencies
- Organization model and core audit events.
- AI society context needs.
- Knowledge strategy and quality principles.

## Risks
- Generated text may be mistaken for approved knowledge.
- Poor metadata can reduce trust in retrieval.
- Knowledge decay can mislead agents and users.

## Acceptance Criteria
- Knowledge objects include source, owner, state, and freshness metadata.
- Approved knowledge is distinguishable from drafts and generated suggestions.
- Users can correct or supersede knowledge.

## Implementation Notes
- Design knowledge as a system of records and references, not a pile of documents.
- Use explicit lifecycle states for critical knowledge.
- Make retrieval explainable enough for review.

## Traceability
- MAL-V00-B007
- MAL-V00-B010
- MAL-V01-B008

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v2 draft | 2026-06-29 | Draft | Initial roadmap phase definition for Mariam Architecture Library v2. |
