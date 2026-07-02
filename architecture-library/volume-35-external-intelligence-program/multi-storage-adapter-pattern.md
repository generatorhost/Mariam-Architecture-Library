# Multi Storage Adapter Pattern

Version: draft
Status: Active
Document ID: architecture-library/volume-35-external-intelligence-program/multi-storage-adapter-pattern.md

## Purpose
Artifacts use storage adapters so Mariam can move between local, cloud, object storage, and future storage systems.

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
