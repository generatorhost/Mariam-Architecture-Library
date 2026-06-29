# Book 00-06 - AI Principles

**Version:** v1 draft
**Status:** Draft
**Document ID:** MAL-V00-B006


## Purpose
Define the constitutional rules for AI behavior inside Mariam.

## Scope
Covers agent boundaries, explainability, safety, human control, evaluation, and model independence.

## Principles
- AI must be assistive, inspectable, bounded, and accountable.
- Model providers are replaceable implementation details.
- High-impact AI actions require review, logging, and rollback paths.

## Operating Rules
- Do not let AI silently mutate authoritative records.
- Capture prompts, context, decisions, and outputs where governance requires it.
- Separate recommendation, decision, and execution states.

## Acceptance Criteria
- AI strategy in Volume 01 traces to this book.
- AI features define failure modes and review paths.
- Model changes can be evaluated without rewriting product identity.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v1 draft | 2026-06-29 | Draft | Initial canonical draft for the Mariam Architecture Library. |
