# Shadcn Space

| Field | Value |
|---|---|
| Source URL | https://github.com/shadcnspace/shadcnspace |
| GitHub repository | `shadcnspace/shadcnspace` (owner shadcnspace, org) |
| Category | web |
| License | MIT — `LICENSE.txt` (root `LICENSE`); no other license files found in the checkout |
| Author / organization | Shadcn Space |
| Acquired | 2026-09-26 |
| Revision | `cf4c7dd8d5c832d72049256d5b4ccb3bc1aa0188` (main, committed 2026-09-24) |
| Attribution required | License notice only |
| Status | extraction-safe — plain MIT, no conditions beyond keeping the license text |

## Useful for
- Large marketing/SaaS block library (~90 `registry:block` items in `registry.json`): hero, feature, pricing, testimonial, team, CTA, services, FAQ, newsletter, blog, contact, navbar/topbar (6 variants), footer, sidebar, dashboard shell, statistics, chart blocks, bento grid, gallery, product listing/overview/category, checkout, empty-state, auth flows (login, register, forgot-password, verify-email, two-factor)
- Full re-implementation of core shadcn/ui primitives on **Base UI** (`components/shadcn-space/*`: dialog, drawer, select, combobox, command, sheet, popover, tooltip, dropdown-menu, context-menu, calendar, date-picker, carousel, resizable, input-otp, autocomplete, file-upload, rating, questionnaire, stepper, kbd, spinner, marquee, shine-border, apple-dock, animated-list/text, orbiting-circles, number-ticker)
- Admin/dashboard scaffolding: `sidebar-01`, `dashboard-shell-01`, `topbar-05` (sidebar-integrated), `widget-01/02`, `table-01` (project-management table), `chart-01..04` (Recharts)
- `custom-components/ss-sidebar`, `custom-components/code-dialog` — app-shell chrome pieces
- `blocks/code-viewer`, `blocks/file-tree-viewer` — dev-tool-style UI (code display, file tree) usable for docs/admin tooling

## Where things live
- `source/registry.json` — full manifest (name, title, description, dependencies, registryDependencies, file→target mapping) per block/component — read this first to resolve any item's exact file set
- `source/src/components/shadcn-space/blocks/<name>/` — one directory per marketing/app block (e.g. `hero-01/page.tsx`, `table-01/`, `dashboard-shell-01/`, `login-01/`)
- `source/src/components/shadcn-space/<primitive>/` — one directory per Base-UI-backed primitive (e.g. `dialog/`, `select/`, `command/`, `date-picker/`)
- `source/src/assets/` — block-scoped assets (e.g. `assets/logo/logo.tsx` used by `hero-01`) — check per-item in `registry.json` before assuming an asset is generic
- `source/src/components/home/`, `source/src/components/blocks/category|breadcrumb|master-category`, `source/src/components/templates/data` — this site's own marketing/catalog-browser UI, not registry items (reference only)
- `source/src/components/common/` — logo, copy button, generic data helpers used across the site (not registry items either)

## Known dependencies
- `package.json`: next 16.2.1, react 19.2.0, @base-ui/react ^1.0.0, radix-ui `latest` (present alongside Base UI — mixed), @dnd-kit/{core,sortable,utilities} ^6.3.1/^10.0.0 (used by `sortable`/apple-dock-style components), recharts 3.8.0, motion ^11.18.2, three ^0.167.1, embla-carousel-react ^8.5.2, react-hook-form ^7.53.1, zod ^3.24.1 (note: v3, not v4), react-day-picker ^10.0.1, canvas-confetti ^1.9.4, @iconify/react ^6.0.2, cmdk ^1.0.0, vaul ^1.1.2

## Do not copy
- `src/components/home/`, `src/components/blocks/category|breadcrumb|master-category|code-viewer` catalog UI, `src/components/templates/data` — this site's own catalog/browsing chrome, not intended as reusable product components
- Nothing pro/paid found — full registry appears open under the one root MIT license

## Notes
- No bundled fonts/images beyond standard Next.js app assets; no separately-licensed assets or Commons-Clause-style demands found anywhere in the checkout.
- `radix-ui: "latest"` alongside `@base-ui/react` is a live mixed-primitive dependency, not just our target-stack mismatch to fix on port — confirm per-component which primitive a given `shadcn-space/*` file actually imports before treating it as pure Base UI.
- `zod ^3.24.1` — one version behind our target's zod v4; check schema API compatibility (e.g. `z.infer`, error map shape) before wiring into forms that already use zod v4 elsewhere in the kit.
- `three ^0.167.1` is a dependency of the whole app but no component under `shadcn-space/` or `blocks/` obviously requires WebGL — likely used by a decorative home-page-only visual; verify before assuming any promoted block needs Three.js.
