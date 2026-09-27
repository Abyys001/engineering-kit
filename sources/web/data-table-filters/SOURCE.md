# Data Table Filters

| Field | Value |
|---|---|
| Source URL | https://github.com/openstatusHQ/data-table-filters |
| GitHub repository | `openstatusHQ/data-table-filters` (owner openstatusHQ, org) |
| Category | web |
| License | MIT — `LICENSE.txt` (root `LICENSE`); no other license files found in the checkout |
| Author / organization | OpenStatus |
| Acquired | 2026-09-26 |
| Revision | `b3b085f34ac7f67dd3af73f40c0ea25a57290787` (main, committed 2026-09-20) |
| Attribution required | License notice only |
| Status | extraction-safe — plain MIT, no conditions beyond keeping the license text |

## Useful for
- Advanced TanStack Table v9 data tables: filter rail/controls, faceted filters, slider/timerange filters, saved-filter command palette (incl. an AI natural-language filter box), infinite-scroll and remote/server-driven table variants
- Rich cell renderers: badge, gauge, heatmap, bar, star rating, level-indicator, code, boolean, timestamp, status-code
- Row-detail sheet pattern (`data-table-sheet-*`), row-actions bar/column with confirm dialog, floating selection bar
- A reusable filter DSL (`lib/filters/{types,normalize,evaluate}.ts`) decoupled from the table for filtering data client- or server-side
- nuqs-backed filter/sort state sync (`data-table-store-sync.tsx`) and a Drizzle/Postgres query-builder pairing (`db/drizzle`, `lib/drizzle`)

## Where things live
- `source/packages/registry/src/components/data-table/` — the extraction target; one concern per file (see `data-table-filter-*.tsx`, `data-table-cell/*.tsx`, `data-table-actions/*.tsx`, `data-table-sheet/*.tsx`, `data-table-chart/*.tsx`, `data-table-remote/*.tsx`)
- `source/packages/registry/src/lib/filters/` — filter type/normalize/evaluate DSL, independent of TanStack Table
- `source/packages/registry/src/lib/table/` — custom TanStack Table features (`features.ts`) and filter functions (`filterfns.ts`)
- `source/packages/registry/src/lib/drizzle/`, `src/lib/mcp/`, `src/lib/ai/` — server-side query building, MCP tool wiring, and the AI filter-command backend
- `source/packages/registry/public/r/*.json` — shadcn-registry manifests, one per composable slice (`data-table.json`, `data-table-filter-command-ai.json`, `data-table-remote.json`, `data-table-nuqs.json`, `data-table-zustand.json`, `data-table-drizzle.json`, `data-table-mcp.json`, `data-table-schema.json`, etc.) — use these to see exact file/dependency groupings per feature
- `source/apps/web/src/` — the docs/demo Next.js app (same component tree duplicated under `components/data-table`); read-only reference for usage, not the canonical source
- `source/apps/web/src/content/docs/` — MDX docs explaining each filter/column pattern

## Known dependencies
- `apps/web/package.json`: next 16.2.12, react 19.2.3, @tanstack/react-table ^9.2.3, @tanstack/react-query ^5.101.4, @tanstack/react-virtual ^3.11.2, nuqs ^2.3.0, zod ^4.3.6, drizzle-orm ^0.45.2, zustand ^5.0.9, radix-ui ^1.4.3 + individual `@radix-ui/react-*` packages, @dnd-kit/* ^6-9, react-hook-form ^7.71.2, recharts ^3.8.0, @ai-sdk/anthropic + `ai` (AI filter box), @modelcontextprotocol/sdk ^1.30.0
- Uses `babel-plugin-react-compiler` (React 19 compiler) — confirm your Next config enables/tolerates this before copying components verbatim

## Do not copy
- `apps/web/src/app/api/`, `apps/web/src/app/api/mcp`, `apps/web/src/app/api/cron` — OpenStatus-specific backend routes (AI, MCP, cron), not generic table code
- `apps/web/src/db/mock` and `apps/web/src/db/drizzle/migrations` — project-specific seed/schema, reference only for shape
- `apps/web/src/content/`, `apps/web/src/posts/` — this site's own docs/blog content

## Notes
- No bundled fonts/images beyond standard Next.js app assets; no pro/paid directories found.
- Radix-based (`@radix-ui/react-*`, `radix-ui`), not Base UI — primitives (select, dialog, popover, tooltip, slider, tabs, dropdown-menu, hover-card, accordion, toggle) need porting to Base UI for our stack.
- TanStack Table v9 already matches target stack — no table-version migration needed, unlike most shadcn table templates still on v8.
- `packages/registry/e2e/fixtures/` contains three sample Next.js app skeletons (`next-src`, `next-src-base`, `next-no-src`) used only for the registry CLI's install-path e2e tests — not reusable UI.
