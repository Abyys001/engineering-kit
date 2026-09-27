# Candidate sources — not yet downloaded

2026-09-26 · from the user's external research report. **Nothing here is cloned yet, and the report's stars, dates, and licenses are unverified** — before downloading one, confirm its `LICENSE` file and last commit, then add it under the right `sources/<category>/` with a `SOURCE.md` and move its entry into [`CURATION.md`](CURATION.md). Adapt, never clone (see [`ui-design-policy.md`](../docs/conventions/ui-design-policy.md) §2, §19–20).

Stack notes: Prisma, Express, SQLite, Casbin, and Temporal sources are pattern references — the data/infra layer gets rewritten to Drizzle/NestJS/PostgreSQL/BullMQ.

## Must research

| # | Repository | Category | License (claimed) | Take | Watch |
|---|---|---|---|---|---|
| 1 | vstorm-co/full-stack-ai-agent-template | AI full stack | MIT | LLM provider layer, RAG (chunk/embed/retrieve/rerank), WebSocket streaming, tool calling, Stripe metering, Celery/ARQ jobs | Large; prune hard. Fills the kit's Python AI gap |
| 2 | pdovhomilja/nextcrm-app | CRM | MIT | AuditTimeline/AuditEntry, `diffObjects`, cursor-paginated activity feed, inline sheet forms, soft delete + restore, pgvector search | Prisma → Drizzle |
| 3 | openstatusHQ/data-table-filters | Data table | MIT | `createTableSchema` + `col.*`, faceted filters, filter command palette, row sheet, nuqs/zustand/memory adapters, Drizzle server helpers | Few contributors |
| 4 | sadmann7/tablecn | Data table | MIT | Server-side table, data grid, Notion/Linear filters, selection action bar, virtualized infinite scroll | TanStack DB beta; skip PartyKit |
| 5 | refinedev/refine | Internal tools | MIT | Headless CRUD, access-control + audit-log providers, live hooks | Framework — reference patterns only |
| 6 | assistant-ui/assistant-ui | AI chat UI | MIT | Thread/Message/Composer primitives, tool-call rendering, generative UI, approval flows | Paid cloud optional |
| 7 | 21st-dev/agent-elements | Agent UI | MIT | Tool cards (Bash/Edit/Search/Todo/Plan), streaming markdown, input bar, model picker | Small community |
| 8 | ErTasselli/OpenTerminal | Dense workspace | MIT | react-grid-layout widget workspace, command palette, lightweight-charts, heatmap, persisted layout store | 23 commits; frontend patterns only |
| 9 | udecode/plate | Rich text | MIT (Pro paid) | Notion-like editor, plugin architecture, AI integration | Avoid Pro components |
| 10 | comet-ml/opik | AI observability | Apache-2.0 | Tracing, LLM-as-judge metrics, prompt management, CI eval | Platform — run as service or extract patterns |
| 11 | magicuidesign/magicui | Animation | MIT | Curated micro-interactions only (policy §7) | Many gimmicks |
| 12 | shadcnspace/shadcnspace | Base UI components | MIT (verify) | Base UI variants, CVA patterns, dashboard blocks | Matches CURATION decision 1 (Base UI) |
| 13 | schedule-x/schedule-x | Calendar | MIT (premium paid) | Scheduler, recurrence, list/agenda views | Free core only |
| 14 | resend/react-email | Email | MIT | Email primitives, templates, render pipeline | — |
| 15 | Georgegriff/react-dnd-kit-tailwind-shadcn-ui | Kanban | MIT (verify) | Accessible dnd-kit board | No persistence; compare with Kiranism kanban already local |
| 16 | fastapi-practices/fastapi-best-architecture | FastAPI | MIT | Layered api/schema/service/crud/model structure, Celery | Casbin dep; last release 2025 |
| 17 | boxyhq/saas-starter-kit | Enterprise SaaS | Apache-2.0 | SSO/SAML, SCIM, audit log | Prisma |
| 18 | novuhq/novu | Notifications | MIT core (verify EE dirs) | Inbox UI, multi-channel delivery model | Enterprise dirs differ in license |
| 19 | synergycodes/workflowbuilder | Workflow editor | Apache-2.0 | React Flow editor SDK | Temporal-coupled |
| 20 | ssoad/flutter_riverpod_clean_architecture | Flutter | MIT (assumed — verify) | Feature-first 4-layer structure | Riverpod 2 → 3 |

## License-cleared, deliberately not on disk

Four candidates were cloned once and discarded. As of 2026-09-27 each has a `SOURCE.md`, a
`LICENSE.txt` captured at its pinned revision, and a `MANIFEST.json` entry carrying
`"acquired": false, "fetch": false` — license review is **done**, acquisition is not. Licenses and
commit dates were confirmed over the GitHub API at the pinned SHA; no repository was cloned.
`tools/fetch-sources.sh` skips `fetch: false` entries on a bare or category-wide run, so nothing
here lands on disk by accident. To adopt one, read its `SOURCE.md` **Notes** first — three of the
four want a sparse checkout, and novu's `enterprise/` tree is proprietary and must be excluded.

| # | Repository | Path | Pinned revision | License (verified) | Acquisition shape |
|---|---|---|---|---|---|
| 9 | udecode/plate | `sources/web/plate` | `babb3c2a733f821a33569d288e45da3f54eaf643` | MIT (root + 8 per-package); `packages/diff` dual MIT + Apache-2.0 | Sparse: only the `packages/<name>` a feature needs |
| 10 | comet-ml/opik | `sources/ai/opik` | `f898372e12782ca6df80aea00acf04b466b45f52` | Apache-2.0 (root + all `sdks/*`); attribution required | Run or read, do not extract; sparse `sdks/python` at most |
| 14 | resend/react-email | `sources/web/react-email` | `15419ff1f4cd0e32ed2c15a4a9182cc47a200a60` | MIT (root + every per-package `license.md`) | Sparse: `packages/ui`, `packages/render`, `examples/resend` |
| 18 | novuhq/novu | `sources/backend/novu` | `320a0ce360cdd3c1b8deeedc545b324fe2a6a3ca` | MIT outside `enterprise/`; `enterprise/packages/**` is Novu Proprietary | Sparse, **excluding `enterprise/`**: `packages/providers`, `packages/framework`, `packages/react`, `libs/dal` |

## Optional

TailAdmin/free-nextjs-admin-dashboard (non-shadcn visual style) · kcsujeet/ilamy-calendar (shadcn calendar) · keenthemes/reui (free tier) · shadcnblocks free blocks · uixmat/onborda (product tour) · kenanyusuf/react-resplit (split panes) · timc1/kbar (already inside Kiranism) · retracedhq/retraced (audit log service + viewer) · mburaksayici/RAG-Boilerplate (hybrid search, rerank, eval) · OwaliShawon/Multi-Tenant-SaaS-Starter-NestJS (tenant isolation) · aljalo/responsive_dashboard · SimpleBoilerplates/Flutter (Riverpod + Dio + go_router) · Untitled UI React (React Aria, Apache-2.0) · HeroUI v3 (React Aria + Tailwind v4) · imgeaslikok/deterministic-job-pipeline (transactional outbox) · Knaadh/nestjs-drizzle · React Flow · Tiptap · Lexical.

## Skip

Cal.com (AGPL) · SigNoz (license NOASSERTION) · Aceternity UI (custom license) · MediaCMS (AGPL, Django) · shadcnblocks Pro, ReUI Pro, Plate Pro, Schedule-X Premium (commercial) · OpenAlgo (trading-specific, not FastAPI).

## Gaps the research found no good source for

Build in-kit when a product first needs them (policy §18):

1. **P1:** org/team management UI (switcher, invites, roles) · RBAC permission editor · notification center (read/unread/archive/preferences) · workflow builder on BullMQ · settings system (profile, org, billing, notifications, integrations, API keys, team)
2. **P2:** file manager (progress, previews, versioning) · billing UI (invoices, plans, payment methods, usage meters) · document + AI analysis view · Flutter admin UI · view-agnostic filter builder
3. **P3:** onboarding checklist · standalone audit-log viewer · master/detail layout on shadcn · empty/loading/error state set · Linear/Raycast-style command palette
