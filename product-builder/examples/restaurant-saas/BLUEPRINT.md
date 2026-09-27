# Restaurant SaaS — worked example blueprint

> Illustrative. It shows how `PRODUCT-BUILDER.md` turns a request into scope. Generated from real domain data on 2026-09-27: `feature-selection.json` is the unedited output of `kb.py matrix restaurant --requested restaurant.reservations,restaurant.dine_in_orders,restaurant.kitchen_display --json`. A real project would copy this into `~/Projects/<name>/docs/product/` and edit the reasons.

**Request (verbatim):** "Build a restaurant SaaS with table reservations, waiter ordering, and a kitchen screen."
**Reading:** restaurant operations SaaS · b2b · mvp · tenancy: multi (assumed — decision 1)
**Domains:** restaurant (primary), general-saas (tenancy/onboarding), booking (proposed: reuse its slot engine)

## Experiences

| Experience | Roles | Surface | Mobile |
|---|---|---|---|
| Customer | customer | Public reservation page (web routes) | not needed for MVP; PWA later |
| Staff | host, server, kitchen_staff | Web workspace: floor plan, order pad, KDS board | **valuable** for servers (tablet/phone order pad), so start with responsive/PWA (decision 2) |
| Management | manager (+ owner: general-saas tenant owner) | Web workspace: menu, tables, reports | not needed |
| Administration | platform operator (general-saas) | Admin routes | not needed |

## Feature matrix (abridged — full list in `feature-selection.json`)

| Feature | Scope | Domain class | Existing impl |
|---|---|---|---|
| Reservations | IN_SCOPE | core | reference (Frappe Hospitality, GPL — learn only) |
| Dine-in orders | IN_SCOPE | core | reference |
| Kitchen display | IN_SCOPE | core | unknown |
| Tables and floor plan · Menu | DEPENDENCY | core | reference |
| Auth · Users · Permissions · Real-time | DEPENDENCY | platform/infra | unknown (kit folders still empty) |
| Payments · Waitlist · Modifiers · Split bills · Tips · Takeout · Allergen labelling | PROPOSED | core/common | unknown |
| Loyalty · Reviews · QR table ordering · Gift cards · Kiosk | OPTIONAL | recommended/optional | unknown |

Payments is `core` for the domain but wasn't asked for, so it's proposed, not built. Tips and allergen labelling carry compliance items (`labor_tip_regulations`, EU 1169/2011, US FDA), each flagged for human review.

## Architecture

Next.js web app with role workspaces · NestJS modules (tables, menu, reservations, orders, kitchen) · PostgreSQL + Drizzle · WebSocket gateway for KDS/order status (`real_time_relevance: core`) · Redis only once more than one API instance runs · BullMQ for reservation reminders if notifications are accepted · Docker Compose + GitHub Actions.

## Build order (`kb.py order`)

Foundation → auth/users/permissions → realtime gateway → tables → reservations → menu → dine-in orders → kitchen display → tests (e2e: reserve → seat → order → fire → bump) → deploy.

## Decisions for you

1. Multi-tenant SaaS (recommended) or a single restaurant?
2. Server order pad: responsive PWA first (recommended), or a Flutter staff app now?
3. Accept any PROPOSED features? Payments is the most consequential (PCI DSS scope; use a hosted provider to minimise it).
