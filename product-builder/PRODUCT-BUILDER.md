# Product builder

How a "build me X" request becomes a scoped, dependency-ordered plan. This file is the process; the data comes from `domains/` (what should exist), the kit (how to build it), and the project's own request (what was asked for).

```text
WHAT SHOULD EXIST?          → domains/        (domain intelligence)
HOW SHOULD IT BE BUILT?     → kit             (features/, backend/, components/, starters/, patterns/, sources/)
HOW IS IT COMPOSED HERE?    → product-builder (this file + schemas/)
```

Never confuse these three. A feature in a domain catalog is **knowledge, not scope**.

Governing policies still apply and win on conflict: stack and reuse (`docs/conventions/engineering-policy.md`), autonomy, blueprint, and when to ask (`curation-and-builder-policy.md` §27–32, §42), and visual design (`ui-design-policy.md`).

## 1. Process

| # | Step | Reads | Produces (`schemas/`) |
|---|---|---|---|
| 1 | **Understand the request.** Quote what was literally asked for; note the product type, audience, public vs internal, prototype vs production. | request | `project.json` → `request`, `classification` |
| 2 | **Classify the domain.** Match against `domains/catalog.json` names and aliases. Multi-domain products are normal (clinic = healthcare + booking + general-saas). | `domains/catalog.json` | `project.json` → `domains` |
| 3 | **Roles and experiences.** From each domain's `roles.json`, pick the roles present in this product and group them into experiences (§4). | `roles.json` | `project.json` → `roles`, `experiences` |
| 4 | **Feature discovery.** Read `DOMAIN.md` → `FEATURES.md` → `feature-map.json`. Map every explicit ask to a feature id; unmatched asks become `custom.*` features. | domain files | `feature-selection.json` |
| 5 | **Scope levels** (§2) for every candidate feature. | same | `feature-selection.json` → `scope` |
| 6 | **Dependencies.** `python3 tools/kb.py order <in-scope ids> --with-enhances` gives the closure; `requires` targets become `DEPENDENCY`, `enhances` targets are proposed at most. | `dependencies.json` | `feature-selection.json` |
| 7 | **Platforms, real-time, AI** (§4–§6), per experience, not per product. | feature `platforms`, relevance fields | `architecture.json` |
| 8 | **Compliance and integrations.** List affected items with jurisdiction; mark those needing a human decision. | `compliance.json`, `integrations.json` | `project.json` → `compliance`, `integrations` |
| 9 | **Kit search.** For each in-scope feature: `implementation-map.json` → `domains/features.json` (shared status) → `INDEX.md`/`catalog.json` → `sources/CURATION.md`. Record reuse / adapt / build. | kit indexes | `feature-selection.json` → `implementation` |
| 10 | **Architecture.** Map features to frontend apps, API modules, DB, workers, storage, notifications, real-time, AI, integrations, deployment, testing. | engineering policy | `architecture.json` |
| 11 | **Design direction.** Domain UI patterns from `DOMAIN.md` feed `docs/design/DESIGN.md` per the UI policy. Architecture consistency never forces visual repetition. | `ui-design-policy.md` | project `docs/design/DESIGN.md` |
| 12 | **Build plan.** Dependency-ordered phases (§7) with acceptance checks. | all of the above | `build-plan.json` |
| 13 | **Present the blueprint once** (template: `templates/blueprint.md`): matrix, assumptions, open decisions. After approval, build without micro-questions. | — | — |

`python3 tools/kb.py matrix <domain> --requested id,id,…` prints the starting feature matrix for steps 4–9.

## 2. Scope levels

| Level | Meaning | Built without asking? |
|---|---|---|
| `IN_SCOPE` | Explicitly requested (classification in the project becomes `requested`) | yes |
| `DEPENDENCY` | Required (`requires` edge) by something in scope, or clearly necessary supporting infrastructure (auth, permissions, the entities a workflow touches) | yes — list it in the blueprint |
| `PROPOSED` | Not requested, but `core`/`common` for the domain, or an `enhances` target of high value | no — propose; build only once accepted |
| `OPTIONAL` | `recommended`/`optional`/`premium` features worth mentioning | no — mention briefly, don't build |
| `OUT_OF_SCOPE` | Considered and excluded (say why in one line) | no |
| `BLOCKED` | Wanted but blocked on a human decision, credentials, a contract, or compliance review | no — list the blocker |

**Never auto-invent client scope.** The catalog's `core` label means "products of this type usually have it", not "the client asked for it". Obvious supporting infrastructure is `DEPENDENCY`; loyalty programs, delivery, AI receptionists, and the like are `PROPOSED` or `OPTIONAL`.

When the request is vague ("a restaurant SaaS"), the product's defining capabilities — the domain's `core` features — are the reasonable reading of the request: mark them `IN_SCOPE` with an assumption line in the blueprint, and keep `common` and below as `PROPOSED`/`OPTIONAL`.

## 3. Feature matrix

Every blueprint contains it. Columns:

```text
Feature | Scope | Domain class | Requested | Existing impl | Platforms | Real-time | AI | Compliance
```

`Existing impl` is the `implementation-map.json` status (`unknown`/`reference`/`partial`/…); never upgrade it from memory.

## 4. Experiences, apps, and mobile

Model the product as up to four **experiences**: Customer, Staff, Management, System administration (plus Partner when relevant). Each maps to a surface: routes in one app, a role-specific workspace, a separate web app, or a mobile app. Choose per requirements; one unified Next.js app with role workspaces is the default until a reason to split appears (different audience or domain, public SEO surface, very different density, separate release cadence).

Consider a **mobile** app per experience, not per product, when users are on the move or away from a desk, when usage is frequent and short, when push notifications matter, or when they need the camera, barcode scanning, location, offline use, or signatures. Otherwise responsive web is enough.

| Signal | Leans |
|---|---|
| Field/on-the-go staff (drivers, technicians, waiters, housekeeping) | Staff mobile is likely core |
| Consumers returning frequently, push-driven | Customer mobile is likely valuable (or a PWA first) |
| Desk-bound analysis/administration | Responsive web |

Ask only when the mobile decision changes architecture or cost materially (policy §29).

## 5. Real-time

Pick transport from the highest `real_time_relevance` among in-scope features: `none`/`low` → request/response plus TanStack Query refetch; `medium` → polling or SSE; `high`/`core` → WebSocket gateway (NestJS) with Redis pub/sub once there is more than one API instance. Kitchen displays, live tracking, trading rates, and chat are typical `high`/`core` cases.

## 6. AI

AI opportunities in the catalog are optional by default. AI becomes in-scope only when requested, or when the product is AI-first. Then use `starters/ai-service` + `ai/` modules behind the NestJS API. Record opportunities as `OPTIONAL` with a one-line value statement.

## 7. Build order

Build dependencies before dependents. Default phases, reordered by `kb.py order` output:

1. Foundation — starter, repo, Docker, env, CI skeleton
2. Database — schema for core entities (conceptual model from `entities.json`; lifecycles from `workflows.json` state machines)
3. Authentication → 4. Authorization (tenancy, roles from the chosen experiences)
5. Core domain entities and API — in `kb.py order` sequence
6. Shared UI and app shell (design direction first)
7. Core workflows end to end (state machines enforced server-side)
8. Notifications and jobs
9. Real-time channels
10. Mobile apps
11. AI service
12. External integrations (behind adapters; sandbox first)
13. Tests (unit + integration per module, e2e per core workflow)
14. Deployment and documentation

## 8. Human decision points

Ask when a decision is expensive to reverse or changes cost/scope: major scope expansion, a new platform (mobile app, second web app), meaningful compliance scope (health data, payments card data, KYC/AML, children's data), paid third-party integrations, tenancy model, ambiguous business rules (pricing, refunds, cancellation penalties). Don't ask about obvious implementation details.

## 9. Language and certainty

Say "X is a common capability in this type of product", never "this industry always needs X". Referencing a standard (FHIR, PCI DSS, EPCIS) never makes a product compliant; compliance items stay flagged for human review with their jurisdiction.

## 10. Files

| Path | Purpose |
|---|---|
| `schemas/project.json` | Product understanding: request, domains, roles, experiences, platforms, compliance, integrations, assumptions, decisions |
| `schemas/feature-selection.json` | Per-feature scope, reason, dependency origin, implementation reuse plan |
| `schemas/architecture.json` | Surfaces, services, data, infra mapped to features |
| `schemas/build-plan.json` | Ordered phases, tasks, acceptance checks |
| `templates/blueprint.md` | The one-page blueprint shown to the user |
| `examples/` | Worked examples generated from real domain data |

A project stores its filled files in `~/Projects/<name>/docs/product/` (not in the kit).
