# Support features

Generated from `feature-map.json`. See `DOMAIN.md` for narrative context.

## Core

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `support.ticket_management` Ticket management | Create, view, update, and track support tickets/conversations through a status lifecycle. | high | chatwoot, zammad, osticket, freescout |
| `support.ticket_queues` Queues / inboxes | Group tickets into queues, inboxes, or departments so teams see only the tickets relevant to them. | high | chatwoot, zammad, osticket, freescout |
| `support.sla_management` SLA management | Define first-response and resolution time targets per priority/queue and track tickets against them. | high | zammad, osticket, chatwoot |
| `support.email_channel` Email channel | Create and reply to tickets via email, with reply threading matched back to the original ticket. | high | chatwoot, zammad, osticket, freescout |
| `support.internal_notes` Internal notes | Private, agent-only notes on a ticket that the customer never sees, distinct from customer-visible replies. | medium | chatwoot, osticket |

## Common

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `support.assignment` Ticket assignment | Assign a ticket to a specific agent, and reassign it as needed. | high | chatwoot, zammad, osticket, freescout |
| `support.escalation` Escalation | Automatically escalate a ticket (reassign, notify a manager, raise priority) when it breaches its SLA. | high | zammad, osticket, chatwoot |
| `support.chat_channel` Live chat channel | A website chat widget that creates and updates tickets in real time. | high | chatwoot, freescout, zammad |
| `support.knowledge_base` Knowledge base | Public and/or internal help-center articles, organized into categories, with search. | high | chatwoot, zammad, osticket |
| `support.macros_canned_responses` Macros / canned responses | Saved reply templates and/or bulk multi-step actions an agent can apply to a ticket in one click. | medium | chatwoot, osticket |
| `support.customer_portal` Customer self-service portal | A logged-in area where a customer can view, create, and track their own tickets. | high | osticket, chatwoot, zammad |
| `support.tagging_categorization` Tags and categorization | Apply free-form tags or fixed categories to tickets for filtering and reporting. | medium | chatwoot, zammad |
| `support.reporting_analytics` Reporting and analytics | Dashboards on ticket volume, agent performance, and SLA compliance. | low | chatwoot |

## Recommended

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `support.csat_surveys` CSAT surveys | Send a post-resolution customer satisfaction survey and record the rating/feedback. | low | chatwoot |
| `support.business_hours` Business hours / holiday calendar | Define operating hours and holidays that SLA countdown timers pause outside of. | low | zammad |
| `support.ticket_automation_rules` Automation rules | Trigger-based automation on ticket events (time-based or field-change), e.g. auto-tag, auto-assign, or notify. | medium | zammad, chatwoot |
| `support.multichannel_unification` Unified multichannel inbox | Present tickets from every channel (email, chat, voice, social) in one inbox per customer, rather than siloed by channel. | medium | chatwoot, freescout |

## Optional

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `support.voice_channel` Voice / phone channel | Log a phone call as a ticket, optionally integrated with an IVR or call system. | medium | freescout, chatwoot |

