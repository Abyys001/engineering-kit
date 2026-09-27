# tablecn

| Field | Value |
|---|---|
| Source URL | https://github.com/sadmann7/tablecn |
| GitHub repository | `sadmann7/tablecn` (owner sadmann7, User account) |
| Category | web |
| License | MIT — `LICENSE.txt` (root `LICENSE.md`); no other license files found in the checkout |
| Author / organization | Sadman Sakib |
| Acquired | 2026-09-26 |
| Revision | `b6e365f303ed728357493bc97e0cb7292c4b4f71` (main, committed 2026-09-23) |
| Attribution required | License notice only |
| Status | extraction-safe — plain MIT, no conditions beyond keeping the license text |

## Useful for
- Full-featured TanStack Table v9 data-table stack shipped in **two parallel primitive variants** — `bases/base` (Base UI) and `bases/radix` (Radix) — same component API, direct drop-in match for our target stack's primitive choice
- Advanced filtering UI: faceted filter, slider filter, date/range filter, filter list + filter menu (combobox-driven filter builder), sort list, view options, advanced/toolbar variants
- A second, distinct "data grid" component family (`data-grid*`, spreadsheet-like: row-height menu, keyboard shortcuts, undo/redo hook, select column) — different UX pattern from the data-table, worth evaluating separately
- `use-data-table` hook centralizing table state (sorting/filtering/pagination) wiring, reusable independent of the specific UI
- Real Next.js app usage examples (`src/app/components/tasks-table*.tsx`) showing the registry components wired to a live table with toolbar actions and row action bar

## Where things live
- `source/src/registry/bases/base/` — Base UI variant: `components/data-table/*.tsx`, `ui/{table,sortable}.tsx`, `hooks/use-data-table.ts` — **this is the primary extraction target for our stack**
- `source/src/registry/bases/radix/` — identical component set built on Radix primitives; useful as a porting reference/diff against the `base` variant
- `source/registry.json` — registry manifest listing `data-table`, `data-table-sort-list`, `data-table-filter-list`, `data-table-filter-menu`, `data-grid*` items, `use-data-grid-undo-redo` hook
- `source/src/app/components/tasks-table*.tsx` — consumer-side usage example (columns, toolbar actions, action bar) for the `data-table` components
- `source/src/lib/{data-table-types,data-table-utils,table-features}.ts` — shared types/utils/custom TanStack Table feature extensions
- `source/drizzle/`, `source/drizzle.config.ts` — Drizzle + Postgres schema backing the demo app (matches our DB stack)
- `source/party/`, `source/partykit.json` — PartyKit realtime layer for the demo's live-collaboration features; not part of the table components themselves

## Known dependencies
- `package.json`: next ^16.3.5, react ^19.3.0, @tanstack/react-table ^9.2.4, @tanstack/react-query ^5.103.1, @tanstack/react-db ^0.4.1, @tanstack/react-virtual ^3.14.13, @base-ui/react ^1.8.0, @base-ui/utils ^0.4.0, radix-ui ^1.6.7 (radix variant only), @dnd-kit/* ^6-10, nuqs ^2.10.1, zod ^4.6.5, drizzle-orm ^0.45.2, react-hook-form ^7.88.0, cmdk ^1.1.1, vaul ^1.1.2
- Already on Base UI + TanStack Table v9 + nuqs + zod v4 + Drizzle/Postgres — the closest dependency match to our target stack of the four repos reviewed

## Do not copy
- `party/`, `partykit.json`, `docker-compose.yml` — demo-app realtime/infra glue, unrelated to the reusable table components
- `scripts/`, `tsconfig.scripts.json` — repo-internal registry-build tooling

## Notes
- No bundled fonts/images, no pro/paid directories, no separately-licensed assets found.
- The `base` vs `radix` split is the repo's own answer to a Radix→Base UI migration — read both before porting to confirm the `base` variant's Base UI API usage is current (Base UI is young and has moved fast).
- `data-grid` family is unrelated to `data-table` (different rendering model, no TanStack Table dependency visible in the file list) — evaluate as its own promote candidate, don't assume it shares code with `data-table`.
