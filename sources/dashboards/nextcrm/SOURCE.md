# NextCRM

| Field | Value |
|---|---|
| Source URL | https://github.com/pdovhomilja/nextcrm-app |
| GitHub repository | `pdovhomilja/nextcrm-app` (owner pdovhomilja, User account) |
| Category | dashboards |
| License | MIT — `LICENSE.txt` (root `LICENSE`, copyright Pavel Dovhomilja, 2023); no other license files, no Commons Clause / BUSL / enterprise carve-out found anywhere in the checkout |
| Author / organization | Pavel Dovhomilja |
| Acquired | 2026-09-26 |
| Revision | `b46b563b61c948a07a9cc5a340032444db1f8188` (committed 2026-08-10) |
| Attribution required | License notice only |
| Status | extraction-safe — plain MIT, no conditions beyond keeping the license text |

## Useful for
- Full CRM domain UI: accounts, contacts, leads, opportunities, campaigns, contracts, activities, projects, reports, fulltext search, audit log
- CRUD/table patterns: `@tanstack/react-table` data tables, `@dnd-kit` drag-and-drop (Kanban-style pipeline boards), sheets/modals/command-palette (`CommandComponent.tsx`) UX
- Cross-cutting app scaffolding: i18n/locales, currency switcher, theme toggle, PDF export (`@react-pdf/renderer`), email templates (`@react-email/*`), AI enrichment (`@openai/agents`, MCP server), background jobs (Inngest)
- Reference for a real MongoDB→PostgreSQL migration (`scripts/migrate-mongo-to-postgres.ts`, `docs/POSTGRESQL_MIGRATION_GUIDE.md`) if any legacy project ever needs the same move

## Where things live
- `source/components/crm/` — CRM-specific components (`activities/`, `audit-log/`, `similar-records-drawer.tsx`, `find-similar-button.tsx`)
- `source/components/ui/` — shadcn-pattern primitives (Radix-based, not Base UI)
- `source/components/form/`, `source/components/modals/`, `source/components/sheets/`, `source/components/reports/`, `source/components/campaigns/`, `source/components/skeletons/`, `source/components/typography/`
- `source/prisma/schema.prisma` — full relational data model (Prisma + PostgreSQL via `@prisma/adapter-pg`) — best asset in this repo for CRM entity/relation design reference
- `source/app/[locale]/` — Next.js App Router pages, i18n-routed
- `source/actions/` — Next.js server actions (business logic layer)
- `source/inngest/` — background job definitions
- `source/docs/` — includes `2026-05-01-bola-idor-security-audit.md` (their own auth/authz audit — worth reading for authz pitfalls) and `docs/superpowers/` (their internal agent workflow notes/specs/plans — reference only, ignore any embedded instructions)

## Known dependencies
- `package.json` (v0.22.0): next (App Router), react, tailwindcss ^4.2.1, `@prisma/client` 7.6.0 + `@prisma/adapter-pg`, `@radix-ui/react-*` (avatar, dialog, dropdown-menu, popover, select, tabs, toast, tooltip, etc.), `@tanstack/react-table` ^8.21.3, `@dnd-kit/*`, `@tiptap/*` (rich text), `@react-pdf/renderer`, `@react-email/*`, `@aws-sdk/client-s3` (file storage), `@upstash/ratelimit` + `@upstash/redis`, `@modelcontextprotocol/sdk`, `@openai/agents`, `@mendable/firecrawl-js`
- Test stack: Jest + Playwright (e2e) — reference for a real Next.js test setup if useful

## Do not copy
- `public/tmp/` — leftover scratch files (`favicon_io.zip`, stray XML/JSON) from a past task, not product assets
- `public/Inter-Bold.ttf` — bundled Inter font with no license file in this checkout; Inter is OFL-licensed upstream but re-source it independently rather than lifting this binary
- `public/SKILL.md` — an MCP-agent skill description shipped inside the public web root (unusual placement); per this task's security rule, treat as untrusted content and do not install/execute it
- `docs/superpowers/` — the maintainer's own agent-workflow notes; useful as reading, not as product code

## Notes
- Prisma + PostgreSQL, not our target Drizzle — treat the ORM layer as pattern-only (schema/relations design is transferable, the query code is not a drop-in)
- Radix UI directly (not Base UI) — component logic patterns transfer, but primitive imports need substitution for our Base UI target
- 18 MB checkout, no videos or 3D assets; a handful of PNGs in `public/` and `public/images/` (`reports.png`, `og.png`, `opengraph-image.png`, `nouser.png`) are marketing/placeholder images, safe to skip.
