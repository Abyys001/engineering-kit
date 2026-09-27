# Support

Customer support / helpdesk: tickets/cases, SLAs, queues, assignment, multichannel communication
(email, chat, voice), a knowledge base, macros/canned responses, CSAT, escalation, and a customer
self-service portal. Depends on `shared.*` for auth, permissions, notifications, search, realtime,
and reporting rather than redefining them; tenancy and billing come from `general-saas` when this
product is sold as a SaaS.

NACE: this is a horizontal software category, not one customer industry. J62.01 (Computer
programming activities) fits the *vendor's* own activity; N82.20 (Activities of call centres)
fits a customer whose business specifically *is* running a call center/support desk. Both are
listed; neither is authoritative for "support software" as a category.

## Product types

- Standalone helpdesk/ticketing product.
- Embedded support module inside a larger vertical product.

## Users

`agent` (staff) · `team_lead` (management) · `administrator` (administration) ·
`customer` (customer, self-service portal) · `system` (SLA timers, automation rules, CSAT dispatch).

## Workflows

Ticket lifecycle (new → open → pending → resolved → closed, reopenable from either terminal
state), SLA escalation (timer → warning → breach → escalation rule fires), CSAT survey
(resolved → survey sent → rating recorded). See `workflows.json` for full steps and state machines.

## Core capabilities

Ticket management, queues/inboxes, SLA management, email channel, internal notes.

## Common capabilities

Assignment, escalation, live chat channel, knowledge base, macros/canned responses, customer
self-service portal, tagging/categorization, reporting and analytics.

## Recommended / optional

Business hours calendars, automation rules, unified multichannel inbox (recommended); voice/phone
channel, CSAT surveys (optional/recommended — see `FEATURES.md` for exact classification and why
CSAT is capped at low confidence in this pass: it was confirmed in only one of four sources
inspected).

## Compliance-sensitive areas

GDPR — support tickets are a common channel through which EU/EEA individuals exercise data
subject access/erasure requests, regardless of whether the product was built with that in mind.
The Telemarketing Sales Rule (US) is relevant if the voice channel is used for outbound calls.
Neither is satisfied merely by building a feature — see `compliance.json`'s disclaimer.

## Integrations

Email gateway (IMAP/SMTP or a transactional email provider), a website chat widget, a voice/
telephony provider for the phone channel.

## Entities

`ticket`, `queue`, `sla_policy`, `escalation_rule`, `macro`, `kb_article`, `csat_response`,
`customer`, `tag`, `business_hours_calendar`, `automation_rule`, `channel`.

## UI patterns

A ticket list/queue view with filters and bulk actions; a ticket detail page with a threaded
conversation, an internal-notes tab clearly visually separated from customer-visible replies, and
a sidebar for tags/SLA countdown/customer info; a separate, differently-branded customer portal;
an agent "collision" indicator when more than one agent opens the same ticket is common in
real-time-capable products but was not independently confirmed in this research pass.

## Mobile

An agent mobile app is common for on-call/urgent-response coverage; full queue management and
reporting are typically desktop-first. The customer portal is usually responsive web rather than
a dedicated app.

## AI

Medium opportunity surface: suggested replies drafted from the knowledge base, auto-tagging/
auto-routing of incoming tickets, and summarizing a long thread for a newly assigned agent.
Optional by default per the product builder's AI policy.

## Standards referenced

No support-ticketing-specific data standard was identified (unlike e.g. FHIR for healthcare).
Terminology and the ticket state machine are cross-referenced from four independent open-source
helpdesk data models instead (see `sources.md`). GDPR and the FTC Telemarketing Sales Rule are
cited for the compliance-sensitive channels.

## Terminology

**Ticket** and **conversation** are used interchangeably (chatwoot calls it a conversation; the
others call it a ticket — this domain uses "ticket"). **Resolved** vs. **closed** is a real,
useful distinction kept by two of the four sources inspected (chatwoot, osTicket): resolved means
the issue is fixed but the ticket stays open for a grace/reopen window, closed is final until
explicitly reopened.
