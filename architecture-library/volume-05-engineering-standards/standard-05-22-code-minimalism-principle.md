# Standard 05.22 - Code Minimalism Principle

Version: draft
Status: Active
Document ID: architecture-library/volume-05-engineering-standards/standard-05-22-code-minimalism-principle.md

## Purpose
Mariam code must be small, clear, testable, replaceable, composable, and free from unnecessary abstractions.

## Scope
This document belongs to the final Mariam Architecture closure set.

## Core Rules
- Small files only.
- Registry-driven design.
- Everything is a managed runtime object.
- Everything extends Mariam; nothing modifies Mariam Core directly.
- Human approval is required for sensitive actions.

## Acceptance Criteria
- The concept is documented.
- The file is small and focused.
- The content is traceable to Mariam architecture.

## Version History
- draft: initial creation.
