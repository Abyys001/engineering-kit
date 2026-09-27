# CRM features

Generated from `feature-map.json`. See `DOMAIN.md` for narrative context.

## Core

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `crm.contacts` Contacts | Individual people records with contact details, linked to companies, deals, and activities. | high | nextcrm, espocrm, odoo-crm |
| `crm.companies_accounts` Companies / accounts | Organization records that group contacts and deals, with optional parent/subsidiary hierarchy. | high | nextcrm, espocrm, odoo-crm |
| `crm.leads` Leads | Unqualified prospects captured before they become a contact/account and a deal. | high | nextcrm, espocrm, odoo-crm |
| `crm.deals_pipelines` Deals / opportunities and pipelines | Sales opportunities moving through one or more configurable pipelines and stages, with value and close date. | high | nextcrm, espocrm, odoo-crm |
| `crm.activities_tasks` Activities and tasks | Calls, meetings, notes, and follow-up tasks logged against a contact, company, lead, or deal. | high | nextcrm, espocrm, odoo-crm |

## Common

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `crm.lead_conversion` Lead conversion | Convert a qualified lead into a contact, account, and an opportunity, preserving lineage back to the original lead. | low | espocrm |
| `crm.contact_timeline` Unified contact timeline | A single chronological view of every activity, email, and document tied to a contact, company, or deal. | medium | nextcrm, espocrm |
| `crm.record_assignment` Record assignment | Assign a lead, deal, or account to a specific sales rep. | low | nextcrm |
| `crm.email_sync` Email sync | Two-way email sync (IMAP/SMTP or provider OAuth) that logs sent/received email against the matching contact or deal. | medium | nextcrm, espocrm |
| `crm.campaign_management` Campaign management | Group leads and deals under a marketing campaign to track source and attribution. | medium | nextcrm, espocrm |
| `crm.segmentation` Segmentation | Dynamic lists of contacts/leads built from filter criteria, used for targeted outreach. | medium | nextcrm, espocrm |
| `crm.deal_products` Deal line items / product catalog | A product/price catalog that can be attached as line items to a deal or quote. | low | nextcrm |
| `crm.reports_dashboards` Sales reports and dashboards | Pipeline, activity, and win/loss reporting dashboards for sales management. | low | nextcrm |
| `crm.data_import` Bulk data import | CSV import of segments/target lists and products, with a review step before committing records. | low | nextcrm |

## Recommended

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `crm.calendar_sync` Calendar sync | Sync meetings scheduled in the CRM with an external calendar (Google/Outlook) and vice versa. | low | nextcrm |
| `crm.quotes` Quotes | A priced proposal generated from a deal's line items, routed for internal approval before it is sent to the customer. | low | nextcrm |
| `crm.pipeline_automation` Pipeline automation | Rule-based automation on deal/lead lifecycle events: stage-change timers, kill/recycle rules, scheduled follow-up cadences. | low | nextcrm |
| `crm.forecasting` Sales forecasting | Pipeline-based revenue forecast, weighted by stage probability, often with recurring-revenue (MRR) tracking. | medium | odoo-crm, nextcrm |

## Optional

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `crm.account_hierarchy` Account hierarchy | Parent/subsidiary relationships between company accounts, with rollup reporting. | low | nextcrm |

