# Installer Overview

Version: draft
Status: Active
Document ID: architecture-library/volume-42-bootstrap-installer-platform/installer-42-01-overview.md

## Purpose
Mariam must install as a self-contained package without manual PowerShell usage by ordinary users.

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
