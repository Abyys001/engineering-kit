# Schedule-X

| Field | Value |
|---|---|
| Source URL | https://schedule-x.dev |
| GitHub repository | `schedule-x/schedule-x` (owner schedule-x, org — not a fork) |
| Category | web |
| License | MIT for everything in this checkout (`LICENSE.txt`, root `LICENSE`) — every package under `packages/*` declares `"license": "MIT"` in its own `package.json`. Premium features (`@sx-premium/*`) are closed-source and **not present** in this checkout at all — see "Premium vs MIT" below |
| Author / organization | Tom Österlund (schedule-x) |
| Acquired | 2026-09-26 |
| Revision | `0c197b798e97fbadcf8a13166999fca875835db6` (main, committed 2026-09-26) |
| Attribution required | License notice only (for the MIT-licensed `packages/*` code actually in this checkout) |
| Status | extraction-safe for `packages/*` (MIT) — REVIEW_REQUIRED if a task wants premium behavior, since that code is not open source and is not here to inspect |

## Premium vs MIT (verified)
- **MIT, in this checkout**: everything under `packages/*` (`calendar`, `calendar-controls`, `current-time`, `date-picker`, `event-modal`, `event-recurrence`, `events-service`, `ical`, `mcp-server`, `recurrence`, `scroll-controller`, `shared`, `theme-default`, `theme-shadcn`, `time-picker`, `timezone-select`, `translations`), published as `@schedule-x/*`. Each has its own MIT `package.json` license field, root `LICENSE` is MIT.
- **Premium, closed-source, NOT in this checkout**: `@sx-premium/*` packages (`drag-and-drop`, `resize`, `drag-to-create`, `draw`, `gantt-chart`, `interactive-event-modal`, `resource-scheduler`, `time-grid-resource-view`, `scheduling-assistant`, `sidebar`). These are fetched at build time from a private, auth-gated npm registry (`website/.npmrc`: `@sx-premium:registry=https://gitlab.schedule-x.com/api/v4/packages/npm/`, requires `NPM_TOKEN`). Only *consumer* code that imports these packages exists here — `website/components/partials/premium-calendar/*.tsx` and `website/components/pages/demo-*.tsx` — the premium plugin source itself is not in the repo, is paid (see `website/components/partials/pricing-card/`), and must not be extracted, reverse-engineered from the demo imports, or treated as MIT.
- `website/` (the marketing/docs Next.js app) declares its own `"license": "ISC"` in `website/package.json` — irrelevant to component extraction, it's just the site's own metadata.

## Useful for
- Calendar core: `@schedule-x/calendar` — month/week/day/agenda views, plugin architecture
- Recurrence: `@schedule-x/recurrence`, `@schedule-x/event-recurrence` — RRULE-based recurring events (free tier; the *interactive* recurrence UI is the paid `interactive-event-modal`)
- Supporting widgets: `@schedule-x/date-picker`, `@schedule-x/time-picker`, `@schedule-x/timezone-select`, `@schedule-x/current-time`, `@schedule-x/scroll-controller`
- Data/service layer: `@schedule-x/events-service`, `@schedule-x/ical` (ICS import/export)
- Theming: `@schedule-x/theme-default`, `@schedule-x/theme-shadcn` — the shadcn theme is the direct fit for our stack
- MCP integration reference: `@schedule-x/mcp` (`packages/mcp-server`)

## Where things live
- `source/packages/calendar/` — core calendar engine (MIT)
- `source/packages/theme-shadcn/` — shadcn-flavored theme package, best starting point for style integration
- `source/packages/date-picker/`, `source/packages/time-picker/`, `source/packages/timezone-select/` — standalone pickers, each independently publishable
- `source/packages/events-service/`, `source/packages/ical/`, `source/packages/recurrence/`, `source/packages/event-recurrence/` — non-UI logic packages
- `source/website/components/partials/premium-calendar/` — demo-only wiring against `@sx-premium/*`; shows the API shape of premium plugins but contains none of their implementation — reference only, do not extract as if it were the plugin
- `source/website/components/partials/pricing-card/` — the paid-plan pricing UI, confirms premium is a commercial add-on, not a licensing style to copy
- `source/documentation/adr/` — architecture decision records (e.g. `003_temporal_api.md`), useful background reading
- `source/libs/` — internal dev tooling (`assertions`, `e2e-testing`, `prettier-config`, `vitest-config`), not product code

## Known dependencies
- Root `package.json`: private monorepo managed with `nx` + `lerna`, TypeScript, Vite, Cypress for e2e
- `packages/calendar`, other core packages: no framework lock-in — framework wrappers (React/Vue/Angular adapters) live in separate repos, not in this checkout
- `website/package.json`: next-based marketing/docs site pulling both `@schedule-x/*` (^4.x) and `@sx-premium/*` (^15.7.2, private registry) — version numbers there do not reflect this monorepo's own package versions

## Do not copy
- Any file under `website/components/partials/premium-calendar/` or `website/components/pages/demo-*.tsx` that imports `@sx-premium/*` — these only demonstrate a paid API, the implementation is not present and not MIT
- `website/` in general — it's the commercial marketing/pricing site (ISC-licensed site code, ties into checkout/licensing flows), not a component source
- `documentation/development/001_issues.md` explicitly states premium plugin code is closed-source even though issues can be filed against it — treat that as confirmation, not an invitation to look for the source elsewhere in this checkout

## Notes
- This is an Nx/Lerna monorepo (`nx.json`, `lerna.json`); package boundaries are enforced by nx project config, not just directory convention.
- No bundled fonts/images requiring separate clearance were found in `packages/*`; unrelated marketing assets live under `website/public/`.
- `packages/mcp-server` (`@schedule-x/mcp`) is namespaced as MCP tooling for schedule-x, not related to Anthropic's Model Context Protocol tooling in our own stack beyond sharing the acronym — read its own README before assuming compatibility.
