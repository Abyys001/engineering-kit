# Curation report — initial pass

2026-09-26 · nothing promoted yet · paths are relative to `sources/`; each source's license, revision, and layout are in its `SOURCE.md`.

Further repos from external research (not downloaded) are in [`CANDIDATES.md`](CANDIDATES.md). Every promotion follows [`ui-design-policy.md`](../docs/conventions/ui-design-policy.md).

This is the promotion backlog: for each priority need, the implementation to curate from (**take**), alternatives worth keeping for visual or behavioral variety (**alt**), and what adapting it involves. Work through *Promotion order*; every promotion updates this file, `INDEX.md`, and `catalog.json`.

## Decisions to confirm first

These shape how every promotion is adapted. Recommendation in bold.

1. **Primitive layer: Base UI.** shadcn's v4 registry ships every primitive and block in Base UI, Radix, and React Aria flavors (`web/shadcn-ui/source/apps/v4/registry/bases/`). Kiranism, the official shadcn chatbot template, and next-shadcn-dashboard are already on Base UI, and shadcn ships a Radix→Base UI migration map (`web/shadcn-ui/source/skills/migrate-radix-to-base/`). Origin UI, Tremor, Kokonut, Cult, and Vercel's AI Elements are Radix and get ported when promoted. Choosing Radix is equally supported by shadcn; it just flips which sources need porting.
2. **Forms: TanStack Form + zod 4.** shadcn's `field.tsx` supports it (and react-hook-form); Kiranism uses it, and it sits with our TanStack Query/Table defaults.
3. **Validation: zod end to end** — web forms, NestJS DTOs (instead of class-validator), and env config — so web and API can share schemas.
4. **Web auth: NestJS-issued sessions** (JWT access + refresh tokens in httpOnly cookies, RBAC enforced by the API). Kiranism's Clerk integration is replaced, not ported.
5. **Tables: TanStack Table v9**, matching shadcn (`^9.0.0`); Kiranism, Origin, and Cult are still on v8.
6. **ai-service data layer: SQLAlchemy 2 + Alembic**; the FastAPI template's SQLModel is out. Target Python 3.14 like the template (the local interpreter is 3.13; Docker uses `python:3.14`).
7. **Flutter ViewModels: Riverpod**, as flutter-structure uses; our policy fixes the layering, not the state library.

## License blockers

| Source | Issue | Recommendation |
|---|---|---|
| React Bits | MIT **+ Commons Clause**: "You may not sell, sublicense, or otherwise redistribute the components of this library as part of a component library, template, UI kit, or other packaged product." Use inside commercial apps is allowed. Also bundles `.glb` models and the OFL-licensed Figtree font. Stale fork of `DavidHDev/react-bits`. | Keep it out of the kit and any `@siavash/*` registry. Use an effect directly in a single app if needed, or re-implement it. |
| next-shadcn-dashboard | MIT license file, but the README asks for a footer credit link to shadcndashboard.dev; 43 MB of marketing images with no stated license. | Reference only unless you accept the footer credit; never copy the images. Kiranism + shadcn blocks cover the same needs cleanly. |
| shadcn registry-template | No license at all. | Don't copy its files. Build the registry on shadcn's MIT schemas (`web/shadcn-ui/source/apps/v4/public/schema/registry.json`, `registry-item.json`), using the template only as a layout reference. |

The Vercel chatbot was flagged during inspection but is clear: its `LICENSE` is Apache-2.0's own short "how to apply" notice. Extracted code must ship the full Apache-2.0 text and keep the copyright line.

## Promotion order

Foundations first (builder policy §30):

1. **Web base** → `components/web/`: shadcn primitives in the chosen flavor — button, input, field, select, combobox, dialog, alert-dialog, drawer, sheet, dropdown, tooltip, tabs, command, calendar, skeleton, spinner, empty, alert, sonner, pagination, chart, sidebar.
2. **`starters/web-saas`**: Kiranism's architecture (feature folders, URL-state tables, forms, command menu) on the web base, with Clerk swapped for NestJS auth and the shell built from shadcn's sidebar/dashboard blocks.
3. **`starters/backend-api`**: nestjs-starter's plumbing (logger + correlation IDs, response envelope, JWT + roles guards, health, Swagger, BullMQ, Docker) with Prisma replaced by Drizzle, following the Vercel chatbot's `lib/db/`, plus zod env validation.
4. **`features/auth` + `features/users`**: shadcn login/signup blocks + NestJS auth/user modules + Kiranism's users feature.
5. **`starters/flutter-app`**: flutter-structure minus its counter demo.
6. **`starters/ai-service`**: the FastAPI template's backend minus SQLModel, the items demo, and the React frontend.
7. **`features/ai-chat`**: chat UI from the shadcn chatbot template + Vercel AI Elements; server side through our FastAPI service.
8. **Visual alternatives** from Cult, Kokonut, Origin, and Tremor — promoted when a product needs them, not up front.

## Web components

- **Sidebar** — take `web/shadcn-ui/source/apps/v4/registry/bases/base/blocks/sidebar-01` through `sidebar-16` (16 layouts). Alt: `dashboards/kiranism-dashboard-starter/source/src/components/layout/app-sidebar.tsx` (RBAC-filtered nav, Clerk-coupled).
- **App Shell** — take `web/shadcn-ui/source/apps/v4/registry/bases/base/blocks/dashboard-01` (sidebar + site header + content). Alt: `dashboards/kiranism-dashboard-starter/source/src/app/dashboard/layout.tsx`.
- **Topbar** — take `web/shadcn-ui/source/apps/v4/registry/bases/base/blocks/dashboard-01/components/site-header.tsx` plus the pieces in `web/originui/source/registry/default/components/navbar-components/` (team-switcher, user-menu, notification-menu, settings-menu, theme-toggle). Alt: `web/kokonutui/source/components/kokonutui/morphic-navbar.tsx`, `toolbar.tsx`, `profile-dropdown.tsx`; `dashboards/kiranism-dashboard-starter/source/src/components/layout/header.tsx`.
- **Data Table** — take `dashboards/kiranism-dashboard-starter/source/src/features/products/components/product-tables` (nuqs URL state for filters, sort, and pagination; columns / options / cell-action split), ported to TanStack Table v9. Alt: `web/shadcn-ui/source/apps/v4/registry/bases/base/blocks/dashboard-01/components/data-table.tsx`; Origin's `table` category.
- **Advanced Form** — take `web/shadcn-ui/source/apps/v4/registry/bases/base/ui/field.tsx` + `dashboards/kiranism-dashboard-starter/source/src/app/dashboard/forms` (basic, advanced, multi-step, sheet form on TanStack Form). Alt: Origin's `input`, `select`, `slider`, and `stepper` categories.
- **Search** — take `web/shadcn-ui/source/apps/v4/registry/bases/base/ui/command.tsx` + `input-group.tsx`. Alt: `web/kokonutui/source/components/kokonutui/action-search-bar.tsx`.
- **Filters** — take the nuqs filters inside Kiranism's `product-tables`. Alt: `web/originui/source/registry/default/components/navbar-components/filters.tsx`.
- **Date Picker** — take `web/shadcn-ui/source/apps/v4/registry/bases/base/ui/calendar.tsx` (date-fns). Alt: Origin's `calendar-date-picker` category and `navbar-components/date-picker.tsx`; Tremor's `DatePicker` (older react-day-picker v8).
- **Combobox** — take `web/shadcn-ui/source/apps/v4/registry/bases/base/ui/combobox.tsx`. Alt: Origin's `select` category (searchable and multi-select variants).
- **Modal** — take `web/shadcn-ui/source/apps/v4/registry/bases/base/ui/dialog.tsx` and `alert-dialog.tsx` (confirmation dialog).
- **Drawer** — take `web/shadcn-ui/source/apps/v4/registry/bases/base/ui/drawer.tsx` and `sheet.tsx`. Alt: `web/kokonutui/source/components/kokonutui/smooth-drawer.tsx`.
- **Command Menu** — take `web/shadcn-ui/source/apps/v4/registry/bases/base/ui/command.tsx` (cmdk). Alt: `dashboards/kiranism-dashboard-starter/source/src/components/kbar` (kbar, wired to the nav).
- **Notifications** — take `web/shadcn-ui/source/apps/v4/registry/bases/base/ui/sonner.tsx` (toasts) + `web/originui/source/registry/default/components/navbar-components/notification-menu.tsx`. Alt: Origin's `notification` category; `dashboards/kiranism-dashboard-starter/source/src/features/notifications`.
- **Empty State** — take `web/shadcn-ui/source/apps/v4/registry/bases/base/ui/empty.tsx`.
- **Error State** — no dedicated component in any source; compose `empty.tsx` + `alert.tsx` with a retry action.
- **Loading State** — take `web/shadcn-ui/source/apps/v4/registry/bases/base/ui/skeleton.tsx` and `spinner.tsx`. Alt: `web/cult-ui/source/apps/www/registry/default/ui/loading-carousel.tsx`.
- **File Upload** — take `web/kokonutui/source/components/kokonutui/file-upload.tsx`. Alt: Origin's `file-upload` and `image-cropper` categories (the upload library varies per component — check each).
- **Charts** — take `web/shadcn-ui/source/apps/v4/registry/bases/base/ui/chart.tsx` + `web/shadcn-ui/source/apps/v4/registry/bases/base/blocks/dashboard-01/components/chart-area-interactive.tsx` (Recharts 3). Alt for analytics depth: `dashboards/tremor/source/src/components/` — BarChart, AreaChart, LineChart, ComboChart, DonutChart, SparkChart, CategoryBar, BarList, Tracker (React 18 + Recharts 2 — port before use).
- **KPI Cards** — take `web/shadcn-ui/source/apps/v4/registry/bases/base/blocks/dashboard-01/components/section-cards.tsx`. Alt: `web/kokonutui/source/components/kokonutui/apple-activity-card.tsx`, `card-stack.tsx`; Tremor's Card + ProgressCircle + BarList; `web/cult-ui/source/apps/www/registry/default/ui/minimal-card.tsx`, `texture-card.tsx`, `cutout-card.tsx`, `shift-card.tsx`.
- **Activity Timeline** — take `web/originui/source/registry/default/ui/timeline.tsx` and Origin's `timeline` category.

Worth promoting beyond the list: Origin's event calendar (`web/originui/source/registry/default/components/event-calendar`), `stepper.tsx`, and `checkbox-tree.tsx` in `web/originui/source/registry/default/ui/`; Kiranism's kanban (`dashboards/kiranism-dashboard-starter/source/src/features/kanban`); Cult's `dock.tsx`, `dynamic-island.tsx`, `floating-panel.tsx`, and shader heroes (`hero-liquid-metal.tsx`, `hero-dithering.tsx`, `hero-heatmap.tsx`) in `web/cult-ui/source/apps/www/registry/default/ui/`; Kokonut's `smooth-tab.tsx` and hooks (`web/kokonutui/source/hooks/use-debounce.ts` and siblings).

Origin UI numbers its components (`comp-XXX`): find one through the categories in `web/originui/source/config/components.ts` or the tags in `web/originui/source/registry.json`.

## Features

- **Authentication** — UI: `web/shadcn-ui/source/apps/v4/registry/bases/base/blocks/login-01` … `login-05` and `signup-01` … `signup-05`; alt `web/cult-ui/source/apps/www/registry/default/block/authentication-01.tsx`. API: `backend/nestjs-starter/source/src/modules/auth` + `backend/nestjs-starter/source/src/common/request/guards/jwt-access.guard.ts` and `roles.guard.ts`. Don't port Kiranism's Clerk flow.
- **User Management** — UI: `dashboards/kiranism-dashboard-starter/source/src/features/users` (on the product-tables pattern). API: `backend/nestjs-starter/source/src/modules/user` (Prisma → Drizzle).
- **Settings** — no clean source; Kiranism's `src/features/profile` delegates to Clerk. Compose from shadcn `tabs.tsx` + `field.tsx`, with Origin's `navbar-components/settings-menu.tsx` as the entry point.
- **Dashboard** — `web/shadcn-ui/source/apps/v4/registry/bases/base/blocks/dashboard-01` + `dashboards/kiranism-dashboard-starter/source/src/features/overview`, charts as above. Vary the composition per product (builder policy §25–26).
- **Notifications** — UI as in Web components; delivery (email/push via BullMQ) is a gap.
- **File Management** — UI from Kokonut's `file-upload.tsx`; storage is a gap (the Vercel chatbot uses `@vercel/blob` — don't copy).
- **Search** — UI from shadcn `command.tsx` / `input-group.tsx`; the search backend (PostgreSQL full-text) is a gap.
- **Filtering + Pagination** — Kiranism's nuqs URL-state pattern in `product-tables` + `web/shadcn-ui/source/apps/v4/registry/bases/base/ui/pagination.tsx`; Origin's `pagination` category for variants.
- **AI Chat** — UI: `ai/shadcn-chatbot-template/source/components/chat-message.tsx` + `ai/shadcn-chatbot-template/source/components/parts` (typed part dispatch with streaming states), `ai/shadcn-chatbot-template/source/components/ui/questionnaire.tsx`, `ai/shadcn-chatbot-template/source/components/parts/sources-part.tsx` (citations); `ai/vercel-chatbot/source/components/ai-elements` (Radix); `web/kokonutui/source/components/kokonutui/ai-prompt.tsx` (composer). Server pattern: `ai/shadcn-chatbot-template/source/app/api/chat/route.ts` (AI SDK `streamText`, `validateUIMessages`), but production requests go to our FastAPI service, not the Vercel AI Gateway. `dashboards/kiranism-dashboard-starter/source/src/features/ai-chat` shows the client hooks.

## Backend (NestJS)

- **Auth + RBAC** — `backend/nestjs-starter/source/src/common/request/guards/jwt-access.guard.ts`, `roles.guard.ts`, and `backend/nestjs-starter/source/src/modules/auth` (reflector-based public routes).
- **Logging** — `backend/nestjs-starter/source/src/common/logger/services/logger.service.ts` (nestjs-pino, redaction, correlation IDs).
- **Error Handling** — `backend/nestjs-starter/source/src/common/response/filters/response.exception.filter.ts` + `backend/nestjs-starter/source/src/common/response/interceptors/response.interceptor.ts` (success/error envelope). Pattern for typed error codes: `ai/vercel-chatbot/source/lib/errors.ts`.
- **Validation** — nestjs-starter's global ValidationPipe; redo with zod per decision 3. Its env config has no schema — add one.
- **Audit Log** — gap: no source has one. Build a Drizzle table + an interceptor on mutations.
- **Jobs / BullMQ / Redis** — `backend/nestjs-starter/source/src/common/bullmq/bullmq.module.ts` (connection only, no real processor), `backend/nestjs-starter/source/src/common/cache/services/cache.service.ts`; Redis rate limiting in `ai/vercel-chatbot/source/lib/ratelimit.ts`.
- **File Storage** — gap: build an S3-compatible module (MinIO locally).
- **Health Checks** — `backend/nestjs-starter/source/src/app/controllers/health.controller.ts` (Terminus).
- **API Documentation** — `backend/nestjs-starter/source/src/common/doc/decorators/doc.api-endpoint.decorator.ts` (composable Swagger decorator).
- **Database** — `ai/vercel-chatbot/source/lib/db/schema.ts`, `queries.ts`, and `migrations/` (Drizzle + PostgreSQL with drizzle-kit).
- **Docker** — `backend/nestjs-starter/source/Dockerfile` (multi-stage, non-root) and `docker-compose.yml` (PostgreSQL + Redis with healthchecks).

## Mobile (Flutter)

All from `mobile/flutter-structure/source/lib/`:

- **App Shell / Navigation** — `app/router/app_router.dart` (go_router StatefulShellRoute tabs + auth redirect).
- **Auth** — `features/auth/presentation/login_page.dart`, `auth_controller.dart`.
- **Networking** — `core/network/dio_client.dart`, `logging_interceptor.dart`.
- **Storage** — `core/storage/secure_store.dart`, `key_value_store.dart`.
- **Theme** — `core/theme/app_theme.dart` (Material 3 light/dark from one seed color).
- **Error Handling** — `core/error/failure.dart`, `exceptions.dart`, and `core/utils/result.dart` (sealed Failure + Result).
- **Common Widgets** — `core/widgets/` (barrel `widgets.dart`), live gallery in `features/showcase/`.
- **Forms** — only a text-field widget in `core/widgets/`; a form layer is a gap.
- **Reference pipeline** — `features/posts/` (domain / data / presentation), i18n in `l10n/`, flavors in `core/config/app_config.dart`.

## AI

- **ai-service starter** — from `backend/fastapi-full-stack-template/source/backend/app/`: `core/config.py` (pydantic-settings; rejects default secrets outside dev), `core/security.py` (Argon2/bcrypt + JWT), `api/deps.py` (Annotated dependency injection), `main.py` + `api/main.py` (router composition), `alembic/env.py`. Plus `backend/fastapi-full-stack-template/source/backend/Dockerfile`, `compose.yml`, and `.github/workflows/test-backend.yml` (coverage-gated CI).
- **Chat, streaming, tool-calling UI** — see AI Chat under Features.
- **Provider abstraction, structured output, embeddings, RAG, evaluation, AI workers** — gap: no source covers the Python side. Build from the official SDK docs behind an `LLMProvider` interface.

## Starters

| Starter | Base | Must change |
|---|---|---|
| `web-saas` | Kiranism dashboard starter | Clerk → NestJS auth; TanStack Table v8 → v9; drop demo features |
| `backend-api` | nestjs-starter | Prisma → Drizzle; zod for env and DTOs; a real BullMQ processor |
| `flutter-app` | flutter-structure | Drop `features/counter`; keep `features/posts` as the pattern example |
| `ai-service` | FastAPI template `backend/` | SQLModel → SQLAlchemy 2; drop the items demo and React frontend; add the provider abstraction |

## Registry (later)

Build `@siavash/*` once roughly 20 items are promoted. Format: shadcn's MIT schemas at `web/shadcn-ui/source/apps/v4/public/schema/registry.json` and `registry-item.json`. Layout reference only (no license): `registries/shadcn-registry-template/source/registry.json`, built with `shadcn build` into static `public/r/*.json`. Private-registry auth isn't covered by any source — a gap.

## Gaps — no local source; build from official docs

- AI (Python): LLM provider abstraction, structured output, embeddings, RAG, evaluation, AI workers.
- Backend: audit log, file storage (S3-compatible), notification delivery, search backend.
- Web: error-state component, settings feature. Mobile: forms layer. Registry: private access.

## Contract / e-signature (2026-09-29)

No new upstream source was cloned for this pass (the useful projects are AGPL or unverified — see [`CANDIDATES.md`](CANDIDATES.md)). Promoted from original code instead: `backend/{signing-tokens,otp,webhooks,audit-log,contracts,tenancy,pdf}`, `components/web/{signing,contract,typography}`. Library picks: `pdfjs-dist` + `react-pdf` (browser), `@cantoo/pdf-lib` + `pdfkit` + `@signpdf/signpdf` + `pkijs` (server), `signature_pad`, `input-otp`, `dnd-kit`. Domain: [`domains/e-signature/`](../domains/e-signature/DOMAIN.md).
