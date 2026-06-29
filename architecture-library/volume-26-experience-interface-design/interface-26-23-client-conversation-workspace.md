# Client Conversation Workspace

**Title:** Client Conversation Workspace
**Version:** v127 draft
**Status:** Draft
**Document ID:** MAL-V26-EXP-23

## Purpose
Defines client context, conversation history, proposal readiness, attachments, approval, and follow-up UI. The screen must support repeated enterprise work, dense scanning, fast decisions, and clear state transitions.

## Scope
- Defines real product interface behavior for Dashboard / Command Center workflows, not an architecture diagram.
- Applies to web dashboard screens, operator workspaces, approval surfaces, communication panels, scraping operations, marketplace UI, monitoring, and settings.
- Uses the official index(2).html token set as the required visual foundation for v127 interface design.
- Excludes implementation code, vendor-specific SDK decisions, and decorative marketing pages.

## Design Tokens Used
| Token | Value | Usage |
| --- | --- | --- |
| `--bg` | `#0a0b12` | Primary application background for the command center shell. |
| `--card` | `#11131f` | Primary panel and dashboard card surface. |
| `--card2` | `#151829` | Secondary nested panel, list row, tab, and inspector surface. |
| `--border` | `#1a1d2e` | Panel borders, dividers, grid rules, and inactive control outlines. |
| `--text` | `#c8c8d8` | Primary readable text on dark surfaces. |
| `--green` | `#00e676` | Healthy, accepted, online, completed, and safe-to-proceed indicators. |
| `--yellow` | `#ffab00` | Waiting, review-needed, medium-risk, warning, and scheduled states. |
| `--red` | `#ff3d3d` | Failed, blocked, rejected, destructive, critical alert, and denied states. |
| `--blue` | `#448aff` | Primary action, selected navigation, active job, link, and focused control states. |
| `--purple` | `#b388ff` | AI, chief, swarm, DNA, intelligence, and premium capability accents. |

## Primary Users
- Enterprise Chief and executive operators who issue missions, approve work, and inspect outcomes.
- Department managers, reviewers, validators, and support operators who manage queues and evidence.
- AI agents and swarms represented through visible state, messages, progress, and decisions.
- Growth, freelance, remote work, and marketplace teams discovering opportunities and managing client workflows.

## Screen Structure
- Global shell uses `--bg` for the application background with high-density panels using `--card` and `--card2`.
- Navigation must remain persistent on desktop and collapse to an icon or drawer pattern on tablet and mobile.
- Main workspace must support split panes for command context, operational tables, detail inspectors, and chat panels.
- Status areas must be visible without relying on hover-only interactions.
- Critical workflows must keep the next required action visible above the fold whenever possible.

## Core Components
- Header with current object, status, owner, and primary actions.
- Filterable table or board view with saved views and state chips.
- Detail inspector for selected item, history, evidence, risks, and next actions.
- Empty, loading, error, blocked, review, approved, and completed states.
- Tokenized buttons, tabs, badges, cards, tables, timeline entries, modals, drawers, toasts, and command inputs.
- Evidence chips for mission, task, report, crawl, proposal, client, approval, source, and artifact references.

## States
- Default state: readable dense enterprise view using `--text`, `--card`, and `--border`.
- Active/selected state: `--blue` for focused navigation, selected row, primary command, or current job.
- AI/intelligence state: `--purple` for Chief, swarm, DNA, ranking, scoring, or model-assisted decisions.
- Success state: `--green` for completed, accepted, online, validated, and safe-to-proceed states.
- Warning state: `--yellow` for pending review, medium risk, scheduled, waiting, or needs-attention states.
- Failure state: `--red` for failed, blocked, rejected, unauthorized, destructive, or critical alert states.

## Interactions
- Users can filter, sort, inspect, approve, reject, retry, pause, resume, escalate, assign, comment, export, and open linked evidence.
- All destructive or externally visible actions require confirmation and must show impact before execution.
- Chat commands must be linkable to missions, tasks, crawls, proposals, documents, and approvals.
- Tables must support keyboard navigation, row selection, bulk actions, and saved filters for repeated operations.
- Notifications must deep-link to the relevant mission, job, crawl, approval, communication, or report.

## Data Requirements
- Screen objects require stable IDs, status, owner, timestamps, source, priority, risk, confidence, trace ID, and linked evidence.
- List views require pagination or virtualization for high-volume tasks, crawls, messages, jobs, and opportunities.
- Detail panels require audit history, current state, permissions, dependencies, metrics, and next actions.
- Scraping and opportunity screens require source, crawl level, extracted entity, duplicate group, score, rank, alert, failed crawl reason, and review decision.

## Security and Governance
- Role-based access must control every command, approval, export, integration, and client-facing action.
- Sensitive data must be masked by default in screenshots, previews, logs, notifications, and shared review links.
- Proposal generation, outbound communication, marketplace publishing, and destructive automation require explicit approval where risk policy demands it.
- All approvals must record reviewer, role, timestamp, decision, evidence, policy version, and artifact version.

## Accessibility
- Text and controls must maintain readable contrast against `--bg`, `--card`, and `--card2`.
- State must not rely on color alone; badges must include labels and icons where appropriate.
- Keyboard focus must be visible using `--blue` and must not shift layout.
- Tables, modals, drawers, chat timelines, and queues must have screen-reader-friendly labels and ordering.
- Motion should be limited to operational feedback and must not hide critical state changes.

## Responsive Behavior
- Desktop: persistent navigation, multi-pane command workspace, dense tables, visible chat/inspector combinations.
- Tablet: collapsible navigation, two-pane workspaces, sticky action bars, and simplified tables.
- Mobile: single-column task-focused flows, searchable navigation, bottom action bars, and progressive disclosure for inspectors.
- Responsive rules must preserve command authority, approval visibility, and scraping job state rather than hiding them behind decoration.


## Acceptance Criteria
- The screen is documented as a real interface with components, states, interactions, data, security, accessibility, and responsive behavior.
- The official index(2).html colors are used exactly as Design Tokens.
- Dashboard / Command Center workflows are represented as product UI, not architecture diagrams.
- Scraping appears as an independent visible workspace wherever relevant, with source manager, levels 1-5, queue, jobs, extracted opportunities, deduplication, ranking, scoring, alerts, failed crawls, manual review, and approval before proposal generation.
- The document can be used by UI designers and frontend engineers to implement the v127 interface direction without undocumented assumptions.

## Traceability
| Source | Relationship |
| --- | --- |
| MAL-V26-EXP-23 | Defines v127 Experience & Interface Design for Client Conversation Workspace. |
| Volume 22 Experience Layer | Higher-level experience architecture reference. |
| Volume 19 Opportunity Intelligence | Opportunity and scraping intelligence reference. |
| Volume 06 Specifications | Runtime, execution, integration, automation, and analytics specification reference. |
| index(2).html token set | Official color token source for this volume. |

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v127 draft | 2026-06-30 | Draft | Added Client Conversation Workspace interface design documentation. |
