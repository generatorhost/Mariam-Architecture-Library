# Installer Overview

Version: draft
Status: Active
Document ID: architecture-library/volume-42-bootstrap-installer-platform/installer-42-01-overview.md

## Purpose
Define the self-contained installation experience for Mariam.

## User Goal
The user downloads one package, runs it, chooses Desktop/VPS/Server mode, and opens Mariam without manual PowerShell or Docker commands.

## Included Services
Docker stack, PostgreSQL, Redis, MinIO, Ollama, API server, workers, dashboard UI, AI Resource Manager, security, monitoring, backup, and update manager.

## First Run
Detect environment -> verify prerequisites -> install services -> generate secrets -> run migrations -> register local AI resources -> create admin account -> open dashboard.

## Failure Handling
Installer must provide readable errors, rollback, retry, logs, and recovery steps without requiring the user to debug commands.

## Acceptance Criteria
- The document contains actionable architecture rules.
- The document stays focused and does not become monolithic.
- The document can guide implementation without extra interpretation.

## Version History
- draft: enriched architecture content.
