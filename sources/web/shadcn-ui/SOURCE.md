# shadcn/ui

| Field | Value |
|---|---|
| Source URL | https://github.com/shadcn-ui/ui |
| GitHub repository | `shadcn-ui/ui` (canonical — not a fork) |
| Category | web |
| License | MIT — `LICENSE.txt`. One nested license also exists: `source/packages/shadcn/test/fixtures/frameworks/remix-indie-stack/LICENSE.md` (MIT, Copyright Remix Software Inc. 2021 / Shopify Inc. 2022-2023) — covers a bundled third-party Remix "indie-stack" test fixture used by the `shadcn` CLI's framework-detection tests, not part of any extractable registry code. |
| Author / organization | shadcn-ui (org); root `package.json` author is "shadcn" |
| Acquired | 2026-09-26 |
| Revision | `98a1fe67b439324ddc857f47fbdce056600a4329` (main, committed 2026-09-21) |
| Attribution required | License notice only |
| Status | extraction-safe — plain MIT, no extra conditions |

## Useful for
- Sidebar/App Shell (16 sidebar variants), Dashboard, Login/Auth, Signup, Data Table, Forms, Calendar/Date
  Picker, Command Menu, Drawer/Sheet, Empty State, Charts — all present as registry blocks/primitives and
  directly matching our priority list.

## Where things live
- `source/apps/v4/registry/bases/base/ui/*.tsx` — Base UI–backed primitives (63 files); current authored
  primitive layer.
- `source/apps/v4/registry/bases/radix/ui/*.tsx` — Radix-backed parallel primitives (62 files), kept in
  sync with `base/` per `bases/README.md`.
- `source/apps/v4/registry/bases/aria/ui/*.tsx` — React Aria–backed primitives (60 files); present in the
  same tree shape but *not* mentioned in `bases/README.md`'s "two authored base registries" — looks newer/
  less stabilized than base and radix.
- `source/apps/v4/registry/bases/base/blocks/{sidebar-01..16,dashboard-01,login-01..05,signup-01..05}` —
  blocks; `dashboard-01/components/data-table.tsx` is the data-table block.
- `source/apps/v4/registry/new-york-v4/` — legacy registry, directly authored/committed (not generated),
  same block set, kept for back-compat; the docs site itself (`apps/v4/components.json`) still points here.
- `source/apps/v4/registry/styles.tsx` — current style-token catalog: vega, nova, maia, lyra, mira, luma,
  sera, rhea (replaces the old "new-york"/"default" style pair).
- `source/apps/v4/registry/README.md`, `source/apps/v4/registry/bases.ts` — explain the base×style
  generation pipeline in full.
- `source/skills/migrate-radix-to-base/` — shadcn's own Claude Code skill mapping Radix primitives to Base
  UI equivalents (menus, form-controls, overlays, disclosure, class-mapping, etc.) — useful reference when
  adapting a component between primitive layers.
- `source/packages/shadcn/src` — the `shadcn` CLI source (registry build/install tooling; reference only).

## Known dependencies
- `apps/v4`: Next.js 16.3.3, React 19.2, Tailwind v4 (`@tailwindcss/postcss` ^4.3.0), `@base-ui/react`
  1.6.0, `radix-ui` (umbrella package, for `bases/radix`), `react-aria-components` (for `bases/aria`),
  `@tanstack/react-table` ^9, `@tanstack/react-form` ^1.20, `cmdk`, `embla-carousel-react`, `lucide-react`,
  `motion` (Framer Motion successor), `zod`, `react-hook-form` + `@hookform/resolvers`.
- Root monorepo `devDependencies` pin `tailwindcss` ^3.4.18 for shared lint/build tooling only — that is
  not the registry's Tailwind version; the shipped registry (`apps/v4`) is Tailwind v4.
- pnpm workspaces (`pnpm@10.33.4`), ESM (`"type": "module"`), Turborepo.

## Do not copy
- `source/packages/shadcn/test/fixtures/**` — third-party fixtures under separate licenses/authors.
- Docs-site plumbing: `apps/v4/content` (fumadocs MDX), registry-health/Vercel Blob monitoring
  (`scripts/monitor-registries.mts`) — infra specific to ui.shadcn.com, not portable.
- `packages/shadcn` CLI internals / `scripts/build-registry.mts` — registry compiler, not app code.
- `new-york-v4` is fine to copy but is the legacy look; prefer `bases/base` or `bases/radix` for new work.

## Notes
- Major architectural shift versus the shadcn/ui most devs know: the registry is now generated as
  (primitive base) × (style token) rather than the old single "style" concept (new-york/default). Three
  primitive bases exist — Base UI, Radix UI, React Aria — with Base UI and Radix documented as the two
  kept-in-parity authored registries; React Aria exists alongside them but isn't called out the same way.
  8 named style tokens (vega, nova, maia, lyra, mira, luma, sera, rhea) replace new-york/default.
  `new-york-v4` remains as a directly-authored legacy registry for back-compat.
- Repo ships its own Claude Code skills at root (`skills/shadcn`, `skills/migrate-radix-to-base`),
  evidence of an active upstream Radix → Base UI migration.
- 62 MB monorepo; `templates/*` (next-app, astro-app, vite-app, react-router-app, start-app + monorepo
  variants) are bare `shadcn init` scaffolds (blank page + Tailwind v4), not full SaaS starters — weak
  candidates for our `web-saas` starter slot.
