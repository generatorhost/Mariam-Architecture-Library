# Volume 26 - Experience & Interface Design

**Title:** Volume 26 - Experience & Interface Design
**Version:** v127 draft
**Status:** Draft
**Document ID:** MAL-V26-README

## Purpose
Volume 26 defines the real product interface for Mariam AI Enterprise OS Dashboard / Command Center. It is a UI and experience design volume, not an architecture diagram volume.

## Scope
- Command Center dashboard.
- Chief and swarm chat panels.
- Mission, task, jobs, reports, communications, integrations, marketplace, knowledge, DNA, monitoring, governance, settings, and responsive behavior.
- Independent scraping and crawling interface with source management, five crawl levels, queues, crawl jobs, extraction, deduplication, ranking, scoring, alerts, failed crawl handling, manual review, and approval before proposal generation.

## Official Design Tokens
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

## Operating Rule
All future interface implementation must follow this volume and must preserve the token values adopted from index(2).html.
