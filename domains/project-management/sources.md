# Project management sources

## Implementations cloned (`sources/domains/<name>/`)

| Source | License | Status | Informed |
|---|---|---|---|
| [Plane](https://github.com/makeplane/plane) (`sources/domains/plane`) | AGPL-3.0 | reference-only | Workspace, Project, Issue (+ Assignee/Label/Comment/Attachment/Relation/Mention/Reaction/Version), State/StateGroup, Cycle, Module, Estimate, View, Intake, integration/github.py + slack.py. Grounds the majority of this domain's core/recommended features and the task-lifecycle and dependency-relation state models. |
| [Kanboard](https://github.com/kanboard/kanboard) (`sources/domains/kanboard`) | MIT | permissive — the domain's "genuinely permissively licensed" source per the research brief | TaskModel/SubtaskModel/ColumnModel/SwimlaneModel/BoardModel/ProjectModel/ProjectRoleModel/TaskTagModel/TaskRecurrenceModel/SubtaskTimeTrackingModel. Grounds the kanban-board, time-tracking, and recurring-task features, and corroborates project/task/label/attachment/activity as a second independent source. |

Kanboard is MIT (permissive) and was kept **reference-only** in this pass for the same reason as
InvenTree in manufacturing: this task was scoped to domain-knowledge research, not kit implementation. A
future pass promoting a kanban board into `features/` could start from Kanboard's models directly, with
attribution, since the license permits it.

## Standards referenced

- `std:nace-rev2.1` — used only for the domain's `nace` classification codes, not as a feature source.
- No other registered standard (`knowledge/standards/standards.json`) was found to be genuinely relevant
  to project/task management; none is cited here, per the brief's instruction not to fabricate standards
  citations.

## Considered but not used

- **OpenProject** (GPL-3.0, ~2.98 GB) and **Taiga** (`taiga-back` MPL-2.0, `taiga-front` AGPL-3.0) — named
  in the research brief. Not cloned: Plane (AGPL, feature-rich, actively developed, well-structured
  Django models) and Kanboard (MIT, focused, mature, genuinely permissive) together cover the requested
  feature surface — boards, cycles/sprints, dependencies, custom workflows, time tracking, recurring
  tasks — more completely than adding a third/fourth source would have within the 2-clone budget.
- **Focalboard** (`mattermost/focalboard`) — its `LICENSE.txt` describes a dual scheme ("compiled
  versions... under an MIT license" vs. a separate source-license path), which is exactly the kind of
  unclear/non-standard licensing the research brief flags for `reference-only` treatment at best; given
  Kanboard already filled the "find a permissive one" requirement unambiguously, Focalboard was not
  pursued further.
- **Wekan** (`wekan/wekan`, confirmed MIT via the GitHub API, ~323 MB) — a plausible second permissive
  candidate (Trello-clone board model), not cloned because Kanboard already provides equivalent
  board/column/swimlane grounding within the 2-clone-per-domain limit.
