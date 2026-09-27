# engineering-kit index

What exists in the kit. Machine-readable twin: [`catalog.json`](catalog.json). Rules: [`README.md`](README.md).

Lookup: promoted items below → [`sources/CURATION.md`](sources/CURATION.md) (best upstream candidate per need) → that source's `SOURCE.md` → its code. Projects never use `sources/` code directly; promote it first.

## Promoted items

None yet. Record each item under an area heading (Web components, Features, Backend, Mobile, AI, Starters, Patterns) in this shape:

```markdown
### <Name>
- **Purpose:** … · **Platform:** web | mobile | backend | ai
- **Path:** `components/web/<group>/<name>` · **Source:** <source> (<license>)
- **Depends on:** … · **Related:** …
- **Use when:** … · **Avoid when:** …
```

## Sources

Status: **extraction-safe** — copy and adapt, keep the notice · **reference-only** — learn from it, don't copy · **REVIEW_REQUIRED** — licensing issue, don't extract. Details in each `SOURCE.md`.

The `source/` clones are git-ignored. On a fresh checkout, restore them from the pinned revisions in [`sources/MANIFEST.json`](sources/MANIFEST.json) with `tools/fetch-sources.sh`. Sources under `sources/domains/` back the per-industry knowledge in [`domains/INDEX.md`](domains/INDEX.md).

| Source | Path | License | Status | Best for |
|---|---|---|---|---|
| shadcn/ui | `sources/web/shadcn-ui` | MIT | extraction-safe | Canonical primitives and blocks (sidebar, dashboard, auth, data table) in Base UI, Radix, and React Aria flavors |
| Origin UI | `sources/web/originui` | MIT | extraction-safe | 599 app components beyond shadcn: date/time, event calendar, file upload, timeline, stepper, tree, navbar pieces (stale fork) |
| Cult UI | `sources/web/cult-ui` | MIT | extraction-safe | Distinctive cards, shader heroes, dock and dynamic-island controls |
| Kokonut UI | `sources/web/kokonutui` | MIT | extraction-safe | Polished SaaS cards, AI prompt input, navbar and toolbar, file upload |
| React Bits | `sources/web/reactbits` | MIT + Commons Clause | REVIEW_REQUIRED | Backgrounds, text and scroll animation — inspiration only; the clause forbids redistribution in a kit |
| Tremor | `sources/dashboards/tremor` | Apache-2.0 | extraction-safe | Charts and data viz (React 18 + Recharts 2 — port before use) |
| next-shadcn-dashboard | `sources/dashboards/next-shadcn-dashboard` | MIT + README footer-credit ask | REVIEW_REQUIRED | App shell, five table styles, auth screens — reference unless the credit is accepted |
| Kiranism dashboard starter | `sources/dashboards/kiranism-dashboard-starter` | MIT | extraction-safe | Web SaaS architecture: feature folders, URL-state tables, TanStack Form, kbar (Clerk-coupled auth) |
| shadcn chatbot template | `sources/ai/shadcn-chatbot-template` | MIT | extraction-safe | Chat UI: typed message parts, tool calls, citations, questionnaire |
| Vercel chatbot | `sources/ai/vercel-chatbot` | Apache-2.0 | extraction-safe | Drizzle schema and migrations, AI Elements, artifacts, Playwright e2e |
| NestJS starter | `sources/backend/nestjs-starter` | MIT | extraction-safe | NestJS plumbing: pino logging, error envelope, JWT + RBAC, BullMQ, health, Swagger (Prisma — don't copy) |
| FastAPI full-stack template | `sources/backend/fastapi-full-stack-template` | MIT | extraction-safe | FastAPI settings, JWT, DI, Alembic, Docker, CI (SQLModel — don't copy; Python 3.14) |
| flutter-structure | `sources/mobile/flutter-structure` | MIT | extraction-safe | Flutter starter: go_router shell, Riverpod MVVM + repository, Dio, secure storage, widget kit |
| shadcn registry template | `sources/registries/shadcn-registry-template` | none | REVIEW_REQUIRED | Layout reference for a future `@siavash/*` registry |
| Agent Elements | `sources/ai/agent-elements` | MIT | extraction-safe | Base UI agent UI: chat shell, tool-call cards (bash, edit + diff, plan, MCP), input bar, model picker |
| assistant-ui | `sources/ai/assistant-ui` | MIT | extraction-safe | Headless thread/composer primitives, runtime adapters, generative UI, approval flows (Radix — port) |
| OpenTerminal | `sources/dashboards/openterminal` | MIT | extraction-safe | Dense widget workspace (react-grid-layout), command palette, pro charting |
| NextCRM | `sources/dashboards/nextcrm` | MIT | extraction-safe | CRM domain model, audit timeline, activity feed, pipeline kanban (Prisma, Radix) |
| BoxyHQ SaaS Starter Kit | `sources/dashboards/boxyhq-saas-starter` | Apache-2.0 | extraction-safe | Team multi-tenancy, invites, RBAC, API keys, webhooks, Stripe, SSO/SCIM patterns |
| FastAPI Best Architecture | `sources/backend/fastapi-best-architecture` | MIT | extraction-safe | Layered FastAPI + async SQLAlchemy 2 + Alembic, RBAC admin |
| Flutter Riverpod Clean Architecture | `sources/mobile/flutter-riverpod-clean-architecture` | MIT | extraction-safe | Riverpod + go_router feature slices, Dio, storage, widget kit |
| Workflow Builder | `sources/web/workflowbuilder` | Apache-2.0 | extraction-safe | React Flow workflow editor on Base UI, execution engine, design tokens |
| Data Table Filters | `sources/web/data-table-filters` | MIT | extraction-safe | Table-agnostic filter DSL, filter command palette, row sheet, AI filters (Radix) |
| tablecn | `sources/web/tablecn` | MIT | extraction-safe | Base UI + TanStack Table v9 data table, Linear-style filters, action bar, data grid |
| Accessible dnd-kit Kanban | `sources/web/dnd-kanban` | MIT | extraction-safe | Keyboard-accessible kanban logic (stale versions — port logic) |
| Shadcn Space | `sources/web/shadcnspace` | MIT | extraction-safe | Base UI marketing and dashboard blocks |
| Magic UI | `sources/web/magicui` | MIT | extraction-safe | Functional micro-interactions: number ticker, animated list, reveals, progress |
| Schedule-X | `sources/web/schedule-x` | MIT (core; premium plugins absent) | extraction-safe | Calendar/scheduler core, recurrence, ICS, shadcn theme |
| Full-Stack AI Agent Template | `sources/ai/full-stack-ai-agent-template` | MIT | extraction-safe | PydanticAI agents + tools, RAG on pgvector, WebSocket streaming, observability (fills the Python AI gap) |
| Refine | `sources/dashboards/refine` | MIT | extraction-safe | Headless data, access-control, audit-log, and live provider contracts |
| Blnk | `sources/domains/blnk` | Apache-2.0 | reference-only | Double-entry ledger model: ledgers, balances with inflight/queued, accounts, transactions, reconciliation |
| Chatwoot | `sources/domains/chatwoot` | MIT (core); enterprise/ separately licensed | extraction-safe | Support domain model: conversations, inboxes/teams, 12 channels, knowledge base, macros, automation rules, CSAT |
| Fleetbase | `sources/domains/fleetbase` | AGPL-3.0 | reference-only | Fleet and dispatch schema via the repo's own generated ERD (orders, payloads, waypoints, proof of delivery) |
| Frappe Hospitality | `sources/domains/frappe-hospitality` | GPL-3.0 | reference-only | Restaurant and hotel entity models and reservation lifecycles (domain knowledge only — GPL-3.0) |
| InvenTree | `sources/domains/inventree` | MIT | reference-only | Parts, BOMs, stock with serial/batch, build orders, order status enums, quality inspection |
| Kanboard | `sources/domains/kanboard` | MIT | reference-only | Deliberately simple task/subtask model — the second independent project-management implementation |
| Karrio | `sources/domains/karrio` | LGPL-3.0 | reference-only | Multi-carrier shipment/rate/label/tracking model and status enums |
| Medplum | `sources/domains/medplum` | Apache-2.0 | extraction-safe | FHIR R4 definitions, healthcare React components, synthetic FHIR records, patient-portal reference apps |
| Odoo (mrp addon) | `sources/domains/odoo-mrp` | LGPL-3.0 | reference-only | Production orders with state machine, BOMs, routings and work centers (addons/mrp only) |
| Plane | `sources/domains/plane` | AGPL-3.0-only | reference-only | Project-management model: workspaces, grouped issue states, issues, cycles, modules |
