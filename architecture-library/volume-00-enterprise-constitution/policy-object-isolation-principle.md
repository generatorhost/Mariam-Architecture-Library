# Policy Object Isolation Principle

Version: draft
Status: Active
Document ID: architecture-library/volume-00-enterprise-constitution/policy-object-isolation-principle.md

## Purpose
Security, API, compliance, and patching logic must live in isolated Policy Objects and registries, not inside monolithic runtime code.

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
