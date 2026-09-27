# Project management

Workspaces and projects for planning and tracking work: tasks/issues with configurable statuses and
typed dependencies, kanban boards, sprints/cycles, epics/modules, milestones, time tracking, threaded
comments, and reporting. NACE Rev. 2.1: J62.01 (computer programming), M70.22 (business/management
consultancy) — illustrative; this domain applies far beyond software teams.

## Product types

- Modern issue trackers (Linear/Jira-like): typed statuses, cycles, modules, rich dependencies.
- Focused kanban boards (Trello-like): columns, swimlanes, WIP limits, simple task cards.
- Full PM suites combining both plus Gantt/timeline and portfolio reporting.

## Users

Workspace admin, project/team lead, contributor, guest/client, and an automated system actor (recurring
tasks, activity logging, reports). See `roles.json`.

## Core workflows

1. **Task lifecycle** — triage → backlog → unstarted → started → completed/cancelled.
2. **Subtask completion rollup**, **task dependency management** (typed, bidirectional relations).
3. **Commenting and mentions**, **cycle (sprint) planning**, **time tracking**.

See `workflows.json` for full steps and state machines. The task lifecycle's state names are verbatim
from one real implementation's grouped-status model (Plane's `StateGroup`); the other cloned source
(Kanboard) uses a much simpler open/closed status, so this domain is explicit in provenance notes about
which shape is corroborated by two sources vs. one.

## Capabilities by classification

- **Core**: workspaces, projects, tasks/issues, subtasks, statuses & workflows, kanban boards, task
  dependencies, comments & mentions.
- **Common**: cycles/sprints, milestones, labels, attachments, custom fields, saved views/filters, time
  tracking.
- **Recommended**: Gantt/timeline, modules/epics, estimates/story points, guest/client access, activity
  feed, recurring tasks.
- **Optional**: workload/capacity view, burndown/velocity reports, view sharing, intake/triage,
  favorites/pinning, private projects.

Full list with descriptions: `FEATURES.md` / `feature-map.json`.

## Compliance-sensitive areas

Data residency / export controls become relevant once guest/client access or file attachments cross a
jurisdiction boundary; this is customer- and contract-specific, not a fixed regulation, and is
`requires_human_review: true`. See `compliance.json`. This domain has comparatively little
jurisdiction-specific compliance compared to logistics or manufacturing — that is recorded honestly
rather than padded out.

## Integrations

Git provider issue linking (commits/PRs, auto-transition on merge), chat notifications (posting
task/comment activity into a team channel). See `integrations.json`.

## Entities

workspace, project, task, state, swimlane, task_relation, comment, cycle, module, milestone, label,
attachment, custom_field, view, time_entry, estimate, guest_member. See `entities.json`.

## UI patterns

Kanban board (columns × swimlanes, drag-and-drop cards), list/table view with saved filters, Gantt/
timeline with dependency lines, cycle/sprint burndown chart, task detail panel (description, comments,
activity, attachments, sub-tasks side by side), command palette for quick task creation/navigation.

## Mobile

Task list, board, and task detail are used on mobile for on-the-go status updates and comments; full
Gantt/timeline and cycle-planning views are typically web-only.

## AI opportunities

Priority/label suggestion, thread summarization, estimate suggestion from historical velocity,
overload-risk prediction, auto-triage/dedup of incoming intake requests.

## Standards

No domain-specific open standard was identified as genuinely load-bearing here (unlike GS1 for logistics
or ISA-95 for manufacturing) — project/task management is largely a product-convention space, not a
regulated or standards-body-defined one. `std:nace-rev2.1` is used only for the domain's `nace` codes.

## Terminology

- **Cycle** (Plane) = **sprint** (Scrum) — a fixed-duration iteration.
- **Module** (Plane) ≈ **epic** — a cross-cycle grouping of related tasks.
- **State group** — the small set of lifecycle buckets (backlog/unstarted/started/completed/cancelled/
  triage) that individual, project-configurable states are grouped into.
- **Swimlane** — a horizontal board grouping (e.g. by priority) distinct from the vertical columns
  (states).
