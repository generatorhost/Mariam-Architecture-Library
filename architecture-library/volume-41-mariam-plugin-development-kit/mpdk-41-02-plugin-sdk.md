# Plugin SDK

Version: draft
Status: Active
Document ID: architecture-library/volume-41-mariam-plugin-development-kit/mpdk-41-02-plugin-sdk.md

## Purpose
Define how third parties and internal studios build installable Mariam plugins.

## Plugin Shape
Each plugin has manifest, contract, dashboard, settings, chat, chief agent, swarm, events, permissions, data ownership, reports, tests, and marketplace metadata.

## Manifest Requirements
plugin_id, name, version, owner, capabilities, dependencies, permissions, APIs, events, storage, UI entrypoints, and compatibility range.

## Contract Requirements
Inputs, outputs, events, permissions, dependencies, error modes, approval gates, rollback rules, and test obligations.

## Lifecycle
Draft -> Validate -> Security Review -> Install -> Configure -> Enable -> Run -> Update -> Disable -> Uninstall -> Archive.

## Zero Core Modification
Plugins must extend Mariam through registries and contracts. They must not require direct core changes.

## Acceptance Criteria
- The document contains actionable architecture rules.
- The document stays focused and does not become monolithic.
- The document can guide implementation without extra interpretation.

## Version History
- draft: enriched architecture content.
