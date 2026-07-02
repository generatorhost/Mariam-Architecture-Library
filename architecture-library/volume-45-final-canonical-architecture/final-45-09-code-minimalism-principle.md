# Code Minimalism Principle

Version: draft
Status: Active
Document ID: architecture-library/volume-45-final-canonical-architecture/final-45-09-code-minimalism-principle.md

## Purpose
Make code minimalism a constitutional rule for Mariam implementation.

## Principle
The shortest clear implementation that is correct, testable, replaceable, and maintainable is preferred.

## Rules
- No large files without justification.
- No large functions without justification.
- No duplicate logic.
- No unnecessary abstractions.
- No complexity used to look sophisticated.
- Prefer 25 clear lines over 250 noisy lines when behavior and reliability are equal or better.

## Review Criteria
Every PR must justify complexity. Any module that grows too large must be split into focused files.

## Acceptance
Code is readable, testable, replaceable, composable, and documented only where documentation adds value.

## Acceptance Criteria
- The document contains actionable architecture rules.
- The document stays focused and does not become monolithic.
- The document can guide implementation without extra interpretation.

## Version History
- draft: enriched architecture content.
