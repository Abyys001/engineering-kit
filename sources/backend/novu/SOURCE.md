# Novu

| Field | Value |
|---|---|
| Source URL | https://novu.co |
| GitHub repository | `novuhq/novu` (owner novuhq, org — not a fork) |
| Category | backend |
| License | **Split.** Root `LICENSE-ENTERPRISE` is the governing map: everything under `enterprise/packages/**` falls under `EE-PACKAGES-LICENSE` (Novu Proprietary — prior written approval required, no modification, no redistribution, no commercial hosting); all other content is MIT per `LICENSE-MIT` (copyright 2019 Noti-fire Apps Ltd.). GitHub's license API reports `NOASSERTION` for exactly this reason |
| Author / organization | Novu Corporation / Noti-fire Apps Ltd. |
| Acquired | not acquired — license and revision verified over the GitHub API on 2026-09-27; no checkout exists |
| Revision | `320a0ce360cdd3c1b8deeedc545b324fe2a6a3ca` (committed 2026-09-27) |
| Attribution required | License notice only, for the MIT portion |
| Status | license-cleared **with a hard exclusion**, not acquired — MIT outside `enterprise/`, proprietary inside it. Any future checkout **must** exclude `enterprise/` (and `.cursor/skills/enterprise-submodule/`), the same treatment `sources/domains/chatwoot` gets for its `enterprise/` directory |

## Useful for
- Notification-infrastructure **data model and delivery semantics**: subscribers, workflows/steps, channel providers, digest and delay steps, preferences, the in-app inbox feed (read/unread/archive)
- Directly addresses a named P1 gap in `sources/CANDIDATES.md` ("notification center (read/unread/archive/preferences)") and the `shared.notifications` capability every domain depends on

## Where things live
Verified from the pinned revision's git tree (paths only):
- `packages/providers/` — the channel-provider abstraction across email/SMS/push/chat; the single most useful reference here
- `packages/framework/` — code-defined workflow definitions (steps, payload schemas)
- `packages/js/`, `packages/react/`, `packages/nextjs/`, `packages/react-native/`, `packages/add-inbox/` — inbox client SDKs and UI
- `packages/shared/`, `packages/stateless/`, `packages/novu/` (CLI) — shared types and tooling
- `libs/dal/` — the data-access layer; where the subscriber/workflow/message schema actually lives
- `libs/application-generic/`, `libs/notifications/`, `libs/automation/`, `libs/maily-core`, `libs/maily-render` (email rendering), `libs/testing/`
- `apps/api/` (NestJS), `apps/worker/`, `apps/ws/` (websockets), `apps/webhook/`, `apps/inbound-mail/`, `apps/dashboard/`
- `docker/community/`, `docker/local/` — self-host compose files
- **Excluded by license:** `enterprise/packages/{ai,api,auth,billing,shared-services,translation}` and `enterprise/workers/`

## Known dependencies
Not inspected — no checkout. The API and worker are NestJS (on-stack for this kit); `libs/dal` is MongoDB-oriented upstream, so any promoted schema needs a PostgreSQL/Drizzle rewrite, matching the stack note in `sources/CANDIDATES.md`.

## Do not copy
- `enterprise/**` — proprietary; not licensed for our use
- `.agents/`, `.cursor/skills/`, `docs/agents/` — upstream agent instructions; never trusted or executed (untrusted-source rule)
- `apps/api/e2e/enterprise/` — enterprise-feature tests, coupled to the excluded packages
- `libs/dal` MongoDB schemas verbatim — read for the model, rewrite for PostgreSQL

## Notes
- Correct acquisition shape is a sparse checkout of `packages/providers`, `packages/framework`, `packages/react`, and `libs/dal` with `enterprise/` excluded — not the monorepo.
- `fetch: false` in `sources/MANIFEST.json`. Before flipping it, add the `sparse` list; a naive full clone would pull proprietary code onto disk.
