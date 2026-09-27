# Shadcn Dashboard (next-shadcn-dashboard)

| Field | Value |
|---|---|
| Source URL | https://github.com/shadcndashboard/next-shadcn-dashboard |
| GitHub repository | `shadcndashboard/next-shadcn-dashboard` (organization; canonical) |
| Category | dashboards |
| License | MIT — `LICENSE.txt` (root, copyright shadcndashboard) — see Attribution below: README imposes a
  condition not present in `LICENSE.txt` itself |
| Author / organization | shadcndashboard.dev, "backed by WrapPixel" (commercial admin-template vendor) |
| Acquired | 2026-09-26 |
| Revision | `91deb10215bc6b567d881c608a9ad794e894994f` (main, committed 2026-08-26) |
| Attribution required | Yes — README.md "License" section: *"All our free items are Open Source and licensed under MIT. You can use our free items for personal as well as commercial purposes. We just need attribution from your end. Copy the link below and paste it in the footer of your web application or project."* followed by `<a href="https://shadcndashboard.dev/">Shadcn Dashboard</a>`. |
| Status | REVIEW_REQUIRED — `LICENSE.txt` is plain MIT, but the README demands a visible footer credit link in any deployed app, which is beyond MIT's source-notice-retention condition. Also: 43 MB of the 45 MB checkout is bundled `public/images/` marketing/demo art with no license of its own. |

## Useful for
- App shell / sidebar reference: `app/(dashboard-layout)/layout/vertical/sidebar/` is a full working
  vertical sidebar (collapsible groups, nav-items, nav-user, nav-secondary) plus header, breadcrumb,
  search, notifications dropdown, theme toggle — the most complete app-shell wiring of the three repos.
- 5 distinct table visual variants: `app/components/tables/{hover-table,striped-row-table,checkbox-table,data-table,basic-table}` — genuine visual variety, not shadcn defaults restyled once.
- `components/ui/` (50 files) includes newer shadcn primitives beyond the classic set: `sidebar.tsx`,
  `combobox.tsx`, `empty.tsx`, `item.tsx`, `kbd.tsx`, `chart.tsx`, `native-select.tsx`, `menubar.tsx`.
- Auth screens: `app/auth/auth2/{login,register,forgot-password,two-steps}`.

## Where things live
- `source/app/(dashboard-layout)/layout/` — shell/sidebar/header/breadcrumb (see above).
- `source/components/ui/` — shadcn-style primitives.
- `source/app/components/tables/` and `.../dashboards/modern` — table and dashboard block variants.
- `source/CHANGELOG.md` — tracks bleeding-edge Next.js 16.3 features (Cache Components, React
  Compiler) actively, good currency signal despite the licensing flag.

## Known dependencies
- Next.js `16.3.0`, React `19.2.5`, TypeScript `^7.0.2` (experimental major, `pnpm lint` noted broken
  under it in CHANGELOG.md), Tailwind v4, `@base-ui/react` (not Radix), `shadcn` CLI package.
- `recharts ^3.8.0`, `framer-motion`/`motion ^12`, `@tanstack/react-table` (but `swr` for data fetching,
  not TanStack Query — different from our stack), `@tiptap/*` (rich text), `lucide-react ^1.8.0`.

## Do not copy
- `source/public/images/**` (43 MB) — product screenshots, stock-looking backgrounds/avatars, pricing
  medal art (gold/silver/bronze) — unclear separate licensing, do not extract with the code.
- `app/components/apps/{blog,notes,tickets}` and `app/api/**` — demo CMS apps with fake data, project-
  specific.
- `layout/vertical/sidebar/buy-now/` — upsell CTA pointing at the paid WrapPixel product line.
- `AGENTS.md`, `CLAUDE.md`, `.claude/`, `.agents/`, `skills-lock.json` — the repo's own AI-tooling
  config, not app code.

## Notes
- Checkout is 45 MB (83 MB incl. `.git`); 43 MB is `public/images` alone — verify before vendoring
  anything wholesale.
- Attribution conflict must be resolved by a human before extracting: either add the footer link when
  shipping derived work, or get explicit confirmation the README ask is non-binding since `LICENSE.txt`
  doesn't carry it.
