# Zero Core Modification Principle

Version: draft
Status: Active
Document ID: architecture-library/volume-45-final-canonical-architecture/final-45-10-zero-core-modification.md

## Purpose
Protect Mariam core from uncontrolled growth.

## Principle
Everything extends Mariam; nothing modifies Mariam core directly.

## Allowed Extension Paths
Plugins, providers, connectors, MCP servers, studios, registries, manifests, contracts, events, and DNA packages.

## Forbidden Pattern
No hardcoded feature logic in core such as if plugin equals YouTube or switch platform.

## Core Role
The core provides identity, registry, event bus, lifecycle, permissions, dependency graph, configuration, and runtime activation.

## Acceptance
A new business feature must be added as an extension unless it is necessary for all system components.

## Acceptance Criteria
- The document contains actionable architecture rules.
- The document stays focused and does not become monolithic.
- The document can guide implementation without extra interpretation.

## Version History
- draft: enriched architecture content.
