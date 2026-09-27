# next-shadcn-dashboard-starter (Kiranism)

| Field | Value |
|---|---|
| Source URL | https://github.com/Kiranism/next-shadcn-dashboard-starter |
| GitHub repository | `Kiranism/next-shadcn-dashboard-starter` (personal user account; canonical) |
| Category | dashboards |
| License | MIT — `LICENSE.txt` (root, copyright (c) 2023 Kiranism) |
| Author / organization | Kiranism (individual maintainer) |
| Acquired | 2026-09-26 |
| Revision | `7705dfc0d13889e45c26a55ad5908da6a7a9a605` (main, committed 2026-08-25) |
| Attribution required | License notice only — README FAQ states explicitly: "Yes. MIT-licensed and free for both personal and commercial projects: no paid tier, no license keys." No footer-credit or backlink ask found. |
| Status | extraction-safe — clean MIT, no extra conditions, no bundled third-party media of note (5.9 MB checkout). |

## Useful for
- Primary reference for **dashboard architecture / feature-folder layout**: `src/features/<name>/{components,schemas,constants,api}` (verified on `products`: `api/{queries,mutations,service,types}.ts`) — cleanest UI/data separation of the three repos.
- **Data table with URL-state filters/pagination**: `src/features/products/components/product-tables/`
  (`index.tsx` uses `nuqs` for URL state, plus `columns.tsx`, `options.tsx`, `cell-action.tsx`) — exact
  match for the priority need.
- **Forms**: `src/app/dashboard/forms/{basic,advanced,multi-step,sheet-form}` + `@tanstack/react-form`.
- **Command Menu**: `kbar` wired in `src/components/kbar`. **Kanban** (dnd-kit) in `src/features/kanban`.
- **AI Chat**: `ai` + `@ai-sdk/react` wired into `src/features/ai-chat` and `src/features/chat` (Vercel
  AI SDK usage pattern, front-end half only).
- **Billing**: `src/app/dashboard/billing/page.tsx`; no separate "settings" feature — Clerk's own
  `src/app/dashboard/profile/[[...profile]]` catch-all covers account management instead.
- `src/components/ui/` has 71 files — the largest shadcn-primitive set of the three, incl. `kanban.tsx`,
  `combobox.tsx`, `empty.tsx`, `item.tsx`, `kbd.tsx`, `attachment.tsx`, `bubble.tsx` (chat), `frame.tsx`.

## Where things live
- `source/src/app/dashboard/` — routed pages (overview w/ parallel routes `@bar_stats`/`@pie_stats`/
  `@sales`/`@area_stats`, forms, kanban, billing, users, product, profile, workspaces/team).
- `source/src/features/` — feature modules (see above).
- `source/src/components/layout/app-sidebar.tsx`, `header.tsx` — app shell.
- `source/docs/{clerk_setup,deployment,forms,nav-rbac,themes}.md` — real architecture docs, worth
  reading before extracting the RBAC/nav pattern.

## Known dependencies
- Next.js `16.2.12`, React `19.2.4`, TypeScript `5.7.2` (stable). Tailwind v4, `@base-ui/react`.
- Auth: `@clerk/nextjs ^7.8.1` — **hard vendor lock-in**. `docs/nav-rbac.md`'s client-side nav RBAC is
  built directly on Clerk's `useOrganization()`/`membership.permissions`/`membership.role` — swapping
  auth providers means rewriting that layer, not just the login screen.
- State/URL: `nuqs ^2.8.9` (URL state), `zustand ^5.0.12` (used only inside `kanban`/`notifications`/
  `chat` feature stores, not global app state), `@tanstack/react-query`, `@tanstack/react-table`,
  `@tanstack/react-form`, `zod ^4.3.6`. Also `@sentry/nextjs`, `recharts 3.8.0`.
- Tooling: bun (`bun.lock`, `bunfig.toml`), `oxlint`/`oxfmt` (Rust-based, not eslint/prettier) — cheap
  to swap for our own tooling if adopted wholesale.

## Do not copy
- Anything under Clerk-specific auth/RBAC without first deciding on our own auth abstraction — this is
  the one piece that doesn't fit our stack as-is (our stack has no mandated auth vendor).
- `AGENTS.md` (27 KB), `CLAUDE.md`, `.claude/`, `.agents/`, `skills-lock.json` — repo's own AI-tooling
  config, not app code (useful only as background reading on their conventions).

## Notes
- **Best of the three as a base for `starters/web-saas`**: feature-folder architecture, URL-state
  tables, RBAC-aware nav, command menu, AI chat, billing route, license-clean — but budget time to
  replace the Clerk coupling with our own auth abstraction before treating it as canonical.
- Next.js 16, actively maintained (commit the day before acquisition).
