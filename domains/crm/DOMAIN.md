# CRM

Customer relationship management for a B2B sales team: contacts, companies/accounts, leads,
deals/opportunities and pipelines, activities/tasks, email/calendar sync, quotes, segmentation,
and forecasting. Depends on `shared.*` for auth, users, organizations, permissions, notifications,
search, and reporting rather than redefining them; tenancy and billing come from the `general-saas`
domain when this product is sold as a SaaS.

NACE: J62.01 (Computer programming activities) — approximate; CRM is a horizontal software
category, not a customer industry vertical.

## Product types

- Standalone sales CRM (the product itself).
- CRM as a module inside a larger vertical product (e.g. a services business's own client-management layer).

## Users

`sales_rep` (staff) · `sales_manager` (management) · `marketing_user` (staff) ·
`sales_ops_admin` (administration) · `system` (automation: sync workers, pipeline timers, reports).

## Workflows

Lead lifecycle (new → contacted → qualified → converted/disqualified), deal lifecycle
(open → won/lost), quote approval and send (draft → pending_approval → approved → sent →
accepted/rejected/expired). See `workflows.json` for full steps and state machines.

## Core capabilities

Contacts, companies/accounts, leads, deals/opportunities and pipelines, activities/tasks.

## Common capabilities

Lead conversion, unified contact timeline, record assignment, email sync, campaign management,
segmentation, deal line items/product catalog, sales reports and dashboards, bulk data import.

## Recommended / optional

Calendar sync, quotes, pipeline automation, sales forecasting (recommended); account hierarchy
(optional). Quotes and forecasting were the weakest-evidenced areas in this research pass — see
`FEATURES.md` confidence column before treating either as a settled industry standard.

## Compliance-sensitive areas

GDPR for EU/EEA contact and lead data (lawful basis, retention, subject rights); CAN-SPAM for
commercial email sent to US recipients via campaigns/segmentation. See `compliance.json`'s
disclaimer — neither is satisfied merely by building a feature.

## Integrations

Email providers (Gmail/Google Workspace, Microsoft 365/Outlook, generic IMAP/SMTP) for two-way
email sync; calendar providers (Google Calendar, Outlook Calendar) for meeting sync.

## Entities

`contact`, `company`, `lead`, `deal`, `pipeline_stage`, `activity`, `task`, `quote`, `product`,
`segment`, `campaign`, `email_message`, `calendar_event`.

## UI patterns

Kanban-style pipeline board for deals (drag between stages); a record detail page per
contact/company/deal with a unified activity timeline; list views with saved filters for
segments; a quote builder with a line-item table and an approval banner.

## Mobile

A lightweight mobile app for field/on-the-go reps (contact lookup, call logging, quick notes) is
common; full pipeline management and reporting are typically desktop-first.

## AI

Medium opportunity surface: lead scoring, next-best-action suggestions, deal-risk flags, and
drafting follow-up emails from the activity timeline. Optional by default per the product
builder's AI policy.

## Standards referenced

GDPR (Regulation (EU) 2016/679), CAN-SPAM Act. No CRM-specific data standard was identified or
cited (unlike e.g. FHIR for healthcare); terminology here is cross-referenced from three
independent open-source CRM data models instead (see `sources.md`).

## Terminology

**Lead** = an unqualified prospect, before conversion. **Deal** and **opportunity** are used
interchangeably (this domain uses "deal"). **Account** and **company** are used interchangeably
(this domain uses "company" for the entity id, "account" in role/permission names, matching how
the inspected products name it). A **quote** here is a conceptual entity: none of the three
implementations inspected has a single dedicated Quote object — it is assembled from a deal's
line items plus an approval step.
