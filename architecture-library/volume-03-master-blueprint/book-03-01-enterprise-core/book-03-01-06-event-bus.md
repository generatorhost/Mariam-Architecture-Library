# Book 03.01.06 - Event Bus

**Version:** v3 draft
**Status:** Draft
**Document ID:** MAL-V03-B03-01-006

## Purpose
Define the core Event Bus used by Enterprise Core subsystems to publish and consume governed events.

## Scope
Covers event topics, envelopes, delivery expectations, ordering assumptions, auditing, and failure handling.

## Responsibilities
- Provide core event transport semantics.
- Standardize event envelope metadata.
- Route subsystem events without hidden coupling.
- Support audit and observability requirements.

## Inputs
- Event envelopes.
- Publisher identity.
- Subscriber registrations.
- Delivery configuration.

## Outputs
- Delivered events.
- Dead-letter records.
- Event metrics.
- Audit references.

## Interfaces
- Publisher API.
- Subscriber API.
- Dead-letter interface.
- Observability interface.

## Events
- EventPublished
- EventDelivered
- EventDeliveryFailed
- EventDeadLettered

## Storage
- Event journal metadata.
- Dead-letter queue records.
- Subscriber registry.

## Security
- Events must include caller and tenant context when relevant.
- Sensitive payloads require classification.
- Subscribers must be authorized for protected topics.

## Metrics
- Event throughput.
- Delivery latency.
- Dead-letter count.
- Unauthorized subscription attempts.

## Tests
- Envelope validation tests.
- Subscription authorization tests.
- Delivery failure tests.
- Dead-letter handling tests.

## Acceptance Criteria
- Core events use a consistent envelope.
- Failed delivery is observable.
- Protected topics enforce authorization.

## Traceability
- MAL-V00-B010
- MAL-V00-B011
- MAL-V02-B011

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v3 draft | 2026-06-29 | Draft | Initial Enterprise Core blueprint content for Mariam Architecture Library v3. |
