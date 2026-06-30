# Release Notes - Mariam Architecture Library v128 draft

**Version:** v128 draft
**Status:** Draft
**Document ID:** MAL-RELNOTES-V128-DRAFT

## What Was Added In v128
- Added Volume 27 - Legacy Seed Analysis.
- Added safe Legacy Seed Integration documents for CRM Workspace, Sales Pipeline, AI Agent Chat, Memory JSON Pattern, WebSocket Live Metrics, Service Status Panel, Mindmap / Service Graph, Docker Runtime Stack, n8n Integration Layer, Ollama Local Provider, MinIO Storage, Redis Cache, and Postgres Business DB.
- Added dedicated Security Exclusions documentation to prevent secrets, passwords, SSH keys, API keys, runtime data, raw .env files, database URLs, and customer records from entering the Architecture Library.
- Added PDF build target `Volume_27_Legacy_Seed_Analysis_v128_draft.pdf`.
- Added ZIP package `Mariam_Architecture_Library_v128_draft.zip`.

## Artifact Counts
- Markdown files: 1329
- PDF files: 129
- ZIP package: `Mariam_Architecture_Library_v128_draft.zip`

## Build Notes
- Built with `tools/build_docs.py`.
- PDF readability is verified with `pypdf`.
- ZIP membership is verified for Volume 27 Markdown, PDF, MANIFEST, and release notes.
- Historical material was treated as read-only legacy seed input and sanitized before documentation.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v128 draft | 2026-06-30 | Draft | Added Legacy Seed Analysis volume. |
