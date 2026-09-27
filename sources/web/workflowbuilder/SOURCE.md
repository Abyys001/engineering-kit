# Workflow Builder

| Field | Value |
|---|---|
| Source URL | https://github.com/synergycodes/workflowbuilder |
| GitHub repository | `synergycodes/workflowbuilder` (owner Synergy Codes, Organization repo) |
| Category | web |
| License | Apache License 2.0 — `LICENSE.txt` (root `LICENSE`); identical Apache 2.0 text also present at `packages/temporal/LICENSE`, `packages/ui/LICENSE`, `packages/sdk/LICENSE` (byte-identical to root, verified with `diff`) |
| Author / organization | Synergy Codes |
| Acquired | 2026-09-26 |
| Revision | `052c396cc90aeebe5b8a1055b7625ec43a88a38e` (main, committed 2026-09-24) |
| Attribution required | License notice only |
| Status | extraction-safe — Apache-2.0 throughout (root + `packages/{temporal,ui,sdk}/LICENSE`, byte-identical). The README advertises a separately sold Enterprise Edition, but no EE code, feature gates, or license-key checks exist in this checkout (checked 2026-09-27) |

## Useful for
- React Flow–based visual workflow/node editor UI (canvas, nodes, panels, tokens) built on **Base UI** primitives — matches our target UI stack directly — `packages/ui/src/`
- Workflow execution engine abstracted from any specific runtime — `packages/execution-core/src/`
- Temporal.io integration patterns (worker, client, connection) — `apps/execution-worker/`, `packages/temporal/`, `packages/temporal-connection/` — pattern-only per our stack (Temporal is pattern-only, BullMQ is our target)
- Node-based editor app (`ai-studio`) using `@xyflow/react` + zustand — `apps/ai-studio/`
- Design tokens shared across apps — `packages/tokens/`
- Monorepo tooling reference: pnpm workspaces + catalogs, Turborepo-style structure, Changesets (`RELEASE.md`), Knip, commitlint — root configs

## Where things live
- `source/packages/ui/src/{components,shared,styles}/` — UI component library on `@base-ui/react` (not Radix/shadcn directly, but Base UI is our exact target primitive)
- `source/packages/execution-core/src/` — runtime-agnostic workflow execution logic; several `*.decision-log.md` files alongside explain design decisions (e.g. `topological-scheduling.decision-log.md`, `terminal-states.decision-log.md`)
- `source/packages/sdk/`, `source/packages/types/` — public SDK surface and shared TS types
- `source/apps/ai-studio/` — the visual editor app (`@xyflow/react`, zustand); has its own `ai-studio-extraction.decision-log.md` explaining how it was split out
- `source/apps/backend/` — Temporal client/connection wiring (`@temporalio/client`, workspace packages) — Node backend, not NestUJS/Drizzle; pattern-only
- `source/apps/execution-worker/` — Temporal worker process
- `source/apps/docs/` — Astro docs site; `apps/docs/src/components/enterprise-note.astro` is the only EE-specific artifact found, purely a doc callout, no gated code

## Known dependencies
- Root `package.json`: `workflow-builder` v2.0.0, pnpm workspaces with catalogs (pinned shared versions of `react`, `@base-ui/react`, `@temporalio/client`, `@xyflow/react`)
- `packages/ui`: `@base-ui/react` (catalog-pinned), react ^18||^19 peer range
- `apps/ai-studio`: `@xyflow/react` (catalog), react (catalog), zustand ^5.0.1
- `apps/backend` / `apps/execution-worker`: `@temporalio/client`, internal workspace packages (`@workflow-builder/temporal-connection`, `@workflowbuilder/temporal`)

## Do not copy
- `apps/backend/` Temporal-specific orchestration wholesale — target job stack is BullMQ; extract UI/execution-core logic, not the Temporal plumbing
- Anything under `apps/docs/` enterprise-note component or copy referencing paid tiers — doc-only but keep it out of any promoted docs content
- Don't bulk-copy whole `apps/`/`packages/` directories without checking for CE/EE feature gates at the file level first (see Status above) — cherry-pick specific files instead

## Notes
- `packages/ui` running on `@base-ui/react` is the strongest match to our target stack (Next.js + shadcn/ui on Base UI) among all four repos in this batch — highest promote value for actual component code.
- Multiple `*.decision-log.md` files (in `packages/execution-core/`, `apps/ai-studio/`) are unusually good "why" documentation — worth reading before adapting the adjacent code, not for copying verbatim.
- Root `LICENSE` and the three package-level `LICENSE` files are byte-identical Apache 2.0 — no divergent per-package terms.
