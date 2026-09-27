# Kanboard

| Field | Value |
|---|---|
| Source URL | https://github.com/kanboard/kanboard |
| GitHub repository | `kanboard/kanboard` |
| Category | domains/project-management |
| License | MIT — `LICENSE.txt` (verbatim copy of root `LICENSE`) |
| Author / organization | Frédéric Guillot |
| Acquired | 2026-09-27 |
| Revision | `cf53b54597b67b60140586c09c2fe6132ead013c` (main) |
| Attribution required | MIT notice retention if code were reused |
| Status | permissive — the domain's genuinely-permissively-licensed source (kept reference-only in this pass anyway, since the task was domain-knowledge research, not kit implementation; see `sources.md`). |

## Useful for
- **TaskModel** (`app/Model/TaskModel.php`) — `STATUS_OPEN`/`STATUS_CLOSED` (a plain binary status, not a
  grouped multi-state model like Plane's), `is_active` flag. Grounds `pm.tasks_issues` (as a second,
  simpler independent implementation), and is the reason the `state` entity's grouped-state shape is
  scored `low` rather than `medium` confidence (only Plane models it that way).
- **SubtaskModel** / **SubtaskTimeTrackingModel** (`app/Model/`) — a lighter-weight, checklist-style
  subtask distinct from a full task, with a dedicated start/stop timer. Grounds `pm.subtasks` (as a
  differently-scoped second implementation) and `pm.time_tracking`.
- **ColumnModel** / **SwimlaneModel** / **BoardModel** / **ColumnRestrictionModel** /
  **ColumnMoveRestrictionModel** (`app/Model/`) — a dedicated, mature board/column/swimlane/WIP-limit
  model. Grounds `pm.boards_kanban`.
- **ProjectModel** / **ProjectRoleModel** / **ProjectGroupRoleModel** (`app/Model/`) — project and
  role-based access. Grounds `pm.projects`, and the `project_manager`/`contributor` roles.
- **TaskTagModel** — grounds `pm.labels` as a second independent source alongside Plane's Label.
- **TaskFileModel** — grounds `pm.attachments` as a second independent source.
- **TaskRecurrenceModel** / **RecurringTaskSubscriber** — grounds `pm.recurring_tasks`.
- **ProjectActivityModel** / **TaskEventBuilder** / **TaskEventJob** — grounds `pm.activity_feed` as a
  second independent source.

## Where things live
- `source/app/Model/` — all PHP models listed above (Task*, Subtask*, Column*, Swimlane*, Board*,
  Project*).
- `source/app/Controller/`, `Filter/`, `Formatter/`, `Action/`, `Export/` — extensive supporting surfaces
  (filters for every task field, automation "actions" engine, iCal/CSV export) present in the clone but
  not deeply inspected beyond confirming their existence for `pm.views_filters`/`pm.recurring_tasks`.
- `source/LICENSE` — MIT.

## Known dependencies
- PHP (no framework dependency beyond its own `app/Core/` — a from-scratch MVC structure), SQLite/MySQL/
  PostgreSQL support (`docker-compose.*.yml` for each).

## Do not copy
- No Kanboard code was copied into the kit in this pass (domain-knowledge research only). If a future
  pass promotes a kanban-board implementation, Kanboard's MIT license permits direct reuse with
  attribution.

## Notes
- Repository is 76 MB uncompressed source (well under the 200,000 KB threshold), so a full sparse-checkout
  (everything except agent-config directories) was used rather than narrowing further.
- Kanboard's status model is deliberately simple (open/closed via `is_active`) compared to Plane's
  grouped, per-project-configurable `State`/`StateGroup` — this asymmetry is called out explicitly in
  this domain's `entities.json`/`feature-map.json` provenance notes rather than glossed over.
