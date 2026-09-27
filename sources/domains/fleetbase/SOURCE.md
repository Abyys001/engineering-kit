# Fleetbase

| Field | Value |
|---|---|
| Source URL | https://github.com/fleetbase/fleetbase |
| GitHub repository | `fleetbase/fleetbase` |
| Category | domains/logistics |
| License | AGPL-3.0 — `LICENSE.txt` (verbatim copy of root `LICENSE.md`) |
| Author / organization | Fleetbase |
| Acquired | 2026-09-27 |
| Revision | `4ff6980c6db6f3e8103b3ec425a089aa6d251af4` (main) |
| Attribution required | AGPL notice retention if code were reused (it is not — reference-only) |
| Status | reference-only — AGPL-3.0 is on the research brief's copyleft list; learn from it, never copy code into the kit. |

## Useful for
- **`database.mmd`** — the repository ships its own generated Mermaid ERD of the entire schema (4,007
  lines). This was the primary research artifact: it gave real column names/types for every table without
  needing to read Laravel migration files one by one. Grounds almost every fleet/dispatch entity and
  feature in this domain: `fleetbase_orders` (dispatch/route/status columns), `fleetbase_payloads`
  (pickup/dropoff/return/cod columns), `fleetbase_waypoints` (time windows, service_time, pod columns),
  `fleetbase_routes`, `fleetbase_drivers`, `fleetbase_vehicles`, `fleetbase_fleets`,
  `fleetbase_manifests`, `fleetbase_tracking_statuses`, `fleetbase_issues`, `fleetbase_zones` /
  `fleetbase_service_areas`, `fleetbase_maintenance_schedules` / `fleetbase_maintenances`,
  `fleetbase_service_rates` / `fleetbase_purchase_rates`, `fleetbase_fuel_provider_*` /
  `fleetbase_fuel_reports`, `fleetbase_places`, `fleetbase_telematics`.
- Confirms Fleetbase is a monorepo of Ember/Laravel packages under `packages/` (`fleetops` = core
  logistics domain, `fleetops-data`, `core-api`, `ledger`, `storefront`, `ai`, etc.) — only the root-level
  generated ERD and license/docs were cloned, not the package source itself, per the sparse-checkout
  pattern used (full `/*` minus agent-config directories, since the repo is only 21 MB).

## Where things live
- `source/database.mmd` — full ERD (Mermaid `erDiagram` syntax), table-by-table with columns, types, and
  FK relationships. `source/erd.svg` / `erd-dark.svg` are rendered versions.
- `source/packages/fleetops/`, `source/packages/fleetops-data/` — the core logistics/fleet Ember
  engine and its data layer (not deeply inspected beyond the ERD in this pass).
- `source/api/` — Laravel API application (migrations live under nested package `database/migrations/`
  directories, not individually inspected — the ERD was used instead as the faster, equally authoritative
  source for schema shape).
- `source/LICENSE.md` — AGPL-3.0.

## Known dependencies
- Laravel (PHP) API + Ember.js frontend/console, per `composer.json`/`package.json` (not inspected in
  depth).

## Do not copy
- Any code from `packages/`, `api/`, or elsewhere — AGPL-3.0. Reference-only per the research brief's
  license policy. The schema/column names recorded in this domain's JSON are facts about a public
  database design, not copied source code.

## Notes
- Exact string values for several `VARCHAR status` columns (e.g. `fleetbase_orders.status`,
  `fleetbase_drivers.status`/`current_status`) are **not** enumerated in the ERD — only the column exists,
  not a checked enum. Where this domain's `workflows.json`/`entities.json` proposes specific state names
  for those columns, it is explicitly marked as reasoned/inferred, not verbatim.
- The full clone was small enough (21 MB) that no narrowing sparse-checkout was needed.
