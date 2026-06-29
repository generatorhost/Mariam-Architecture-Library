# Book 02-10 - Phase 08 Model Ecosystem

**Version:** v2 draft
**Status:** Draft
**Document ID:** MAL-V02-B010


## Purpose
Define how Mariam manages model providers, model selection, evaluation, and fallback.

## Scope
Covers provider abstraction, model registry, routing, evaluation, cost controls, safety, and portability.

## Strategic Objective
Keep AI capabilities model-independent while preserving quality and accountability.

## Systems Included
- Model registry
- Provider adapter rules
- Routing policy
- Evaluation benchmark sets
- Cost and safety controls

## Main Deliverables
- Model ecosystem specification
- Provider abstraction contract
- Evaluation scorecard
- Fallback policy
- Model change review process

## Dependencies
- AI society contracts.
- Runtime execution model.
- AI principles and security principles.

## Risks
- Provider-specific behavior may leak into product contracts.
- Cost optimization may weaken quality.
- Model updates can silently change outputs.

## Acceptance Criteria
- Model changes are reviewable and testable.
- AI capabilities can declare model requirements without hardcoding providers.
- Fallback behavior is documented.

## Implementation Notes
- Keep model identity separate from agent identity.
- Track evaluation evidence for important model decisions.
- Design for multiple providers from the start.

## Traceability
- MAL-V00-B006
- MAL-V00-B011
- MAL-V01-B003

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v2 draft | 2026-06-29 | Draft | Initial roadmap phase definition for Mariam Architecture Library v2. |
