# Plane

| Field | Value |
|---|---|
| Source URL | https://github.com/makeplane/plane |
| GitHub repository | `makeplane/plane`, branch `preview` |
| Category | domains/project-management |
| License | AGPL-3.0-only — `LICENSE.txt` (verbatim copy of root `LICENSE.txt`); `COPYRIGHT.txt` confirms `SPDX-License-Identifier: AGPL-3.0-only` |
| Author / organization | Plane Software, Inc. |
| Acquired | 2026-09-27 |
| Revision | `888b0869dc6a3cc993e6f2f289ee81b191139e1f` (branch `preview`) |
| Attribution required | AGPL notice retention if code were reused (it is not — reference-only) |
| Status | reference-only — AGPL-3.0 is on the research brief's copyleft list; learn from it, never copy code into the kit. |

## Useful for
- **Workspace / Project** (`db/models/workspace.py`, `db/models/project.py`) — Workspace, WorkspaceMember,
  Team, WorkspaceTheme; Project (`ProjectNetwork` enum: private/public), ProjectMember (`ROLE` enum),
  ProjectIdentifier, ProjectDeployBoard, ProjectPublicMember. Grounds `pm.workspaces`, `pm.projects`,
  `pm.private_projects`, `pm.guest_client_access`.
- **State / StateGroup** (`db/models/state.py`) — `StateGroup` TextChoices (backlog, unstarted, started,
  completed, cancelled, triage) plus `DEFAULT_STATES` seed data. Used verbatim as the task-lifecycle state
  vocabulary in `workflows.json`. Grounds `pm.statuses_workflows`.
- **Issue** (`db/models/issue.py`) — the largest file: `Issue` (parent self-FK, state FK, `point`/
  `estimate_point`, priority, start_date/target_date, assignees, sequence_id, sort_order, is_draft),
  `IssueRelation` + `IssueRelationChoices` (duplicate, relates_to, blocked_by, start_before,
  finish_before, implemented_by — with an explicit `_RELATION_PAIRS`/`_REVERSE_MAPPING` for bidirectional
  derivation), `IssueComment`/`IssueMention`/`IssueReaction`/`CommentReaction`, `IssueAttachment`,
  `IssueLabel`, `IssueActivity`, `IssueSubscriber`, `IssueVote`, `IssueVersion`. Grounds
  `pm.tasks_issues`, `pm.subtasks`, `pm.task_dependencies`, `pm.comments_mentions`, `pm.attachments`,
  `pm.labels`, `pm.activity_feed`, `pm.favorites` (via `favorite.py`).
- **Cycle** (`db/models/cycle.py`) — `Cycle` (start_date/end_date, owned_by), `CycleIssue`,
  `CycleUserProperties`. Grounds `pm.cycles_sprints`, `pm.burndown_velocity_reports`,
  `pm.workload_capacity` (reasoned).
- **Module** (`db/models/module.py`) — `Module` + `ModuleStatus` TextChoices (backlog, planned,
  in-progress, paused, completed, cancelled), `ModuleMember`, `ModuleIssue`, `ModuleUserProperties`.
  Grounds `pm.modules_epics`.
- **Estimate** (`db/models/estimate.py`), **View** (`db/models/view.py`), **Intake** (`db/models/intake.py`)
  — grounds `pm.estimates_story_points`, `pm.views_filters`/`pm.saved_views_sharing`, `pm.intake_triage`.
- **integration/github.py**, **integration/slack.py** — grounds `git_provider` and `chat_notifications`
  integrations.

## Where things live
- `source/apps/api/plane/db/models/` — every Django model listed above, one file per concern.
- `source/apps/api/plane/db/models/integration/` — GitHub/Slack integration models.
- `source/apps/api/plane/app/`, `space/`, `api/` — DRF views/serializers/urls per surface (admin app,
  public space, external API) — not deeply inspected in this pass.
- `source/LICENSE.txt`, `source/COPYRIGHT.txt` — AGPL-3.0-only.

## Known dependencies
- Django + DRF backend (`apps/api`). A separate `apps/web`/`apps/admin`/`apps/space` frontend and other
  apps (`live`, `proxy`) exist in the monorepo but were **not** cloned (sparse-checkout limited to
  `apps/api`, `LICENSE.txt`, `COPYRIGHT.txt`).

## Do not copy
- Any code from `apps/api` — AGPL-3.0. Reference-only per the research brief's license policy.

## Notes
- The repository's default branch is `preview` (not `main`/`master`); this was used as-is since it is the
  branch GitHub reports as default and it contains the full `apps/api` tree needed.
- Repo ships `.claude/`, `AGENTS.md`, `COPYRIGHT_CHECK.md` at root (AI-agent tooling / license-check
  files) — excluded by the sparse-checkout pattern.
- Total repo size (216,920 KB) is just over the 200,000 KB direct-clone threshold in the research brief,
  so a narrow sparse-checkout (`apps/api` + license files only, ~8.4 MB) was used instead of a full clone.
