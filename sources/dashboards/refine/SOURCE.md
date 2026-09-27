# Refine

| Field | Value |
|---|---|
| Source URL | https://github.com/refinedev/refine |
| GitHub repository | `refinedev/refine` (owner Refine Development Inc. — organization) |
| Category | dashboards |
| License | MIT — `LICENSE.txt` (root `LICENSE`); every package under `packages/*` also declares `"license": "MIT"` in its own `package.json`, and packages with their own `LICENSE` file carry identical MIT text |
| Author / organization | Refine Development Inc. |
| Acquired | 2026-09-26 |
| Revision | `2352eb5b6539e2f39ad9aef652279ad1dcf2c467` (committed 2026-09-10T15:56:33+03:00) |
| Attribution required | License notice only |
| Status | extraction-safe — plain MIT throughout; no enterprise/"ee" directories, no Commons Clause, no separately-licensed assets found |

## Useful for
- Headless data-provider contract: request/response shape (`getList`, `getOne`, `create`, `update`, `deleteOne`, custom) decoupled from any UI framework or backend — the pattern to copy for a FastAPI-backed data layer
- Access-control provider: `can({ resource, action, params })` pattern for centralizing authorization checks outside route handlers
- Audit-log provider: hooks for logging create/update/delete events against a resource, independent of persistence choice
- Live provider: subscribe/publish contract for real-time updates (WebSocket-agnostic interface), useful as a shape reference even without adopting Refine itself
- `packages/react-hook-form`, `packages/react-table` — thin adapter patterns showing how Refine decouples core hooks from specific form/table libraries (relevant since the kit's stack uses TanStack Table v9, not Refine's UI packages)

## Where things live
- `source/packages/core/src/contexts/data/` (`index.tsx`, `types.ts`) — `IDataContext` / data-provider contract
- `source/packages/core/src/hooks/data/useDataProvider.tsx` — data-provider resolution hook; `src/definitions/helpers/pickDataProvider/` — multi-provider selection logic
- `source/packages/core/src/contexts/accessControl/` and `src/hooks/accessControl/` — access-control provider contract and hook
- `source/packages/core/src/contexts/auditLog/` and `src/hooks/auditLog/` — audit-log provider contract and hook
- `source/packages/core/src/contexts/live/` and `src/hooks/live/` (incl. `useLiveMode/`) — live/real-time provider contract
- `source/packages/simple-rest/`, `source/packages/rest/`, `source/packages/graphql/` — reference data-provider implementations against concrete backends (simple-rest is the clearest one to read against a FastAPI backend)
- UI-framework integrations (`packages/antd`, `packages/mui`, `packages/mantine`, `packages/chakra-ui`, `packages/refine-ui`) — explicitly out of scope per task framing; not surveyed in depth

## Known dependencies
- `packages/core/package.json`: `"version": "5.2.0"`, peer deps `react: "^18.0.0 || ^19.0.0"`, `react-dom` same range — compatible with the kit's React 19 target
- Workspace uses pnpm (`pnpm-workspace.yaml`, `pnpm-lock.yaml`), Nx (`nx.json`) and Lerna (`lerna.json`) for monorepo builds — not needed if only copying `packages/core` source
- `documentation/` and image files were excluded from this checkout via sparse-checkout — do not expect docs site content

## Do not copy
- `packages/*` UI-framework integration packages (`antd`, `mui`, `mantine`, `chakra-ui`, `refine-ui`) — out of scope for this kit's headless-pattern focus; would also pull in UI libraries the kit doesn't use
- `packages/devtools*`, `packages/live-previews` — Refine's own tooling/devtools product, not reusable app patterns
- `examples/`, `templates/`, `hackathon/` — demo/sample apps, not source patterns to extract directly
- Backend-specific provider packages (`hasura`, `strapi`, `strapi-v4`, `medusa`, `supabase`, `appwrite`, `airtable`, `nestjsx-crud`, `nestjs-query`) — tied to specific third-party backends, not the kit's FastAPI target; read only as shape reference if needed, don't vendor

## Notes
- Shallow git clone, not a tarball: refresh with `git -C source fetch --depth 1 origin main && git -C source reset --hard origin/main` (respecting the existing sparse-checkout excluding `documentation/` and images). Current revision `2352eb5b6539e2f39ad9aef652279ad1dcf2c467`, committed 2026-09-10T15:56:33+03:00.
- `packages/core/src` has no `LICENSE` file of its own (unlike many other packages, e.g. `devtools`, `kbar`, `react-hook-form`) — it relies on the root `LICENSE`; both are identical MIT text where checked.
- No Commons Clause, no `ee`/`enterprise` directories found anywhere in the checkout (`find . -iname "*ee*" -o -iname "*enterprise*"` returns only unrelated path matches like `examples/refine-week-invoice-generator`).
- Focus for this kit is the headless provider contracts in `packages/core`, not the 20+ UI-framework/backend integration packages that make up most of the monorepo.
