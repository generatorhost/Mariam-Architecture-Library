# Book 00-11 - Security Principles

**Version:** v1 draft
**Status:** Draft
**Document ID:** MAL-V00-B011


## Purpose
Define the security posture required for Mariam AI Enterprise OS.

## Scope
Covers identity, access, data protection, secrets, audit, AI safety, and supply chain awareness.

## Principles
- Security is a design constraint, not a final review step.
- Least privilege applies to humans, agents, services, and integrations.
- Sensitive data must have purpose, boundary, and lifecycle.

## Operating Rules
- Require explicit permission models for protected actions.
- Never store secrets in documentation, code, prompts, or release artifacts.
- Log security-relevant actions without exposing sensitive content.

## Acceptance Criteria
- Future specifications include security considerations.
- Release artifacts contain no secrets.
- AI workflows respect data classification boundaries.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v1 draft | 2026-06-29 | Draft | Initial canonical draft for the Mariam Architecture Library. |
