# WhatsApp Business Unit

Version: draft
Status: Active
Document ID: architecture-library/volume-40-universal-digital-platform-intelligence/udpi-40-05-whatsapp-business-unit.md

## Purpose
Define WhatsApp as a policy-aware communication business unit.

## Scope
Covers official WhatsApp Business API usage, templates, consent, approved messaging, support flows, rate limits, customer records, and audit.

## Chief Agent
WhatsApp Chief Agent manages safe messaging workflows, approved templates, customer context, escalation, and compliance.

## Swarm Roles
- Template Agent
- Consent Agent
- Conversation Agent
- Support Agent
- Escalation Agent
- Compliance Agent

## Policy Rules
The system must avoid spam behavior, unauthorized bulk messaging, scraping contacts, or bypassing official controls.

## Execution Flow
Customer event -> permission check -> template selection -> message draft -> approval if needed -> delivery -> audit -> follow-up.

## Acceptance Criteria
- The document contains actionable architecture rules.
- The document stays focused and does not become monolithic.
- The document can guide implementation without extra interpretation.

## Version History
- draft: enriched architecture content.
