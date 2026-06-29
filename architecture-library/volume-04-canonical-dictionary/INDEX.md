# Volume 04 Index

**Version:** v23 draft
**Status:** Draft
**Document ID:** MAL-V04-INDEX

## Purpose
List the canonical dictionary files and their document IDs.

## Scope
Volume 04 covers canonical terms used across Mariam AI Enterprise OS documentation, architecture, specifications, implementation planning, testing, operations, and release evidence.

## Responsibilities
- Maintain one official vocabulary for Mariam.
- Resolve naming conflicts before implementation.
- Keep dictionary entries traceable to constitutional, roadmap, and blueprint documents.

## Inputs
- Volume 00 Enterprise Constitution.
- Volume 01 Master Vision.
- Volume 02 Master Roadmap.
- Volume 03 Master Blueprint.

## Outputs
- Dictionary files grouped by domain.
- Standard terms for specifications, tests, dashboards, APIs, MCP tools, events, and storage schemas.
- Traceable vocabulary for future releases.

## Interfaces
- Architecture blueprints.
- Future specifications.
- Release notes and manifests.
- Engineering, operations, and testing guides.

## Events
- DictionaryTermAdded
- DictionaryTermUpdated
- DictionaryTermDeprecated
- DictionaryReleased

## Storage
- Markdown source files in Volume 04.
- Generated PDF release artifact.
- Manifest checksum records.

## Security
- Do not store secrets, credentials, or private operational data in dictionary entries.
- Classify security-sensitive terms clearly.
- Treat terminology changes as governance-relevant when they affect access, data, or authority.

## Metrics
- Dictionary coverage by domain.
- Duplicate or conflicting term count.
- Traceability coverage.
- Release artifact generation success.

## Testing
- Validate required dictionary files exist.
- Validate every term has the required fields.
- Validate PDF and ZIP generation.

## Acceptance Criteria
- Volume 04 contains administrative files and all 25 dictionary files.
- Each dictionary file contains a meaningful list of domain terms.
- Each term follows the required canonical structure.

## Traceability
- MAL-V00-B004
- MAL-V00-B009
- MAL-V02-B004
- MAL-V03-B03-20-020

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v23 draft | 2026-06-29 | Draft | Initial Volume 04 administrative document. |


## Dictionary Files
- MAL-V04-DICT-001 - `dictionary-04-01-enterprise-terms.md`
- MAL-V04-DICT-002 - `dictionary-04-02-organization-terms.md`
- MAL-V04-DICT-003 - `dictionary-04-03-ai-society-terms.md`
- MAL-V04-DICT-004 - `dictionary-04-04-agent-terms.md`
- MAL-V04-DICT-005 - `dictionary-04-05-swarm-terms.md`
- MAL-V04-DICT-006 - `dictionary-04-06-dna-terms.md`
- MAL-V04-DICT-007 - `dictionary-04-07-knowledge-terms.md`
- MAL-V04-DICT-008 - `dictionary-04-08-capability-terms.md`
- MAL-V04-DICT-009 - `dictionary-04-09-workflow-terms.md`
- MAL-V04-DICT-010 - `dictionary-04-10-runtime-terms.md`
- MAL-V04-DICT-011 - `dictionary-04-11-model-terms.md`
- MAL-V04-DICT-012 - `dictionary-04-12-provider-terms.md`
- MAL-V04-DICT-013 - `dictionary-04-13-plugin-terms.md`
- MAL-V04-DICT-014 - `dictionary-04-14-connector-terms.md`
- MAL-V04-DICT-015 - `dictionary-04-15-marketplace-terms.md`
- MAL-V04-DICT-016 - `dictionary-04-16-governance-terms.md`
- MAL-V04-DICT-017 - `dictionary-04-17-security-terms.md`
- MAL-V04-DICT-018 - `dictionary-04-18-infrastructure-terms.md`
- MAL-V04-DICT-019 - `dictionary-04-19-freelance-terms.md`
- MAL-V04-DICT-020 - `dictionary-04-20-remote-work-terms.md`
- MAL-V04-DICT-021 - `dictionary-04-21-evolution-terms.md`
- MAL-V04-DICT-022 - `dictionary-04-22-monitoring-terms.md`
- MAL-V04-DICT-023 - `dictionary-04-23-storage-terms.md`
- MAL-V04-DICT-024 - `dictionary-04-24-ui-dashboard-terms.md`
- MAL-V04-DICT-025 - `dictionary-04-25-integration-api-mcp-terms.md`
