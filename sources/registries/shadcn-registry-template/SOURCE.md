# shadcn Registry Template

| Field | Value |
|---|---|
| Source URL | https://github.com/shadcn-ui/registry-template |
| GitHub repository | `shadcn-ui/registry-template` (canonical) |
| Category | registries |
| License | None found — no `LICENSE.txt` (see Status) |
| Author / organization | shadcn-ui |
| Acquired | 2026-09-26 |
| Revision | `906f859db0125965cba71c51da1707c0a4c6d045` (main, committed 2025-12-12) |
| Attribution required | N/A — no license grant found, so no rights to attribute against |
| Status | REVIEW_REQUIRED — no root LICENSE, no `license` field in `package.json`, no README license section, no NOTICE; GitHub reports no license |

## Useful for
- The exact thing we need: running a private/personal component registry (e.g. `@siavash/*`) for
  our own Next.js/shadcn stack — distributing components, hooks, lib, and pages.
- `registry.json` as the reference format: item shape, `registryDependencies` vs `dependencies`,
  multi-file items with per-file `type`/`target`.
- `shadcn build` → static `public/r/*.json` as the whole "hosting" model: no server required, any
  static host works (Vercel, S3, Nginx).

## Where things live
- `source/registry.json` — the registry manifest; read first. Shows `registry:component`,
  `registry:page` (with a `target` path), `registry:lib`, `registry:hook` items in active use
  (this template does not exemplify `registry:file` or `registry:config` — the schema at
  `https://ui.shadcn.com/schema/registry.json` may document more types, unverified here).
- `source/registry/new-york/{blocks,ui}/` — the actual item source files `registry.json` points at.
- `source/public/r/*.json` — pre-built output of `pnpm registry:build` (`shadcn build`); this is
  what actually gets served. No dynamic route handler exists in this checkout, despite the README
  mentioning one — the static-file model is what's real here.
- `source/components/open-in-v0-button.tsx` — optional v0 deep link, not required for hosting.
- `source/app/page.tsx` — demo page previewing each item; replace entirely for a real site.
- `source/components.json` — registry-author-side shadcn config (`new-york`, `neutral`), separate
  from any *consumer* project's own `components.json`.

## Known dependencies
- next 15.5.9, react 19.1.0, tailwindcss ^4.1.11, `shadcn` CLI ^3.0.0, zod ^3.25.76 (v3, not v4).
- `@radix-ui/react-label`, `@radix-ui/react-slot` only — minimal, Radix-based.

## Do not copy
- Demo items (`hello-world`, `example-form`, `complex-component` Pokemon lookup,
  `example-with-css`) — placeholder content; keep only as a files/shape example.
- Nothing else is stack-mismatched — this is otherwise a thin, on-stack scaffold.

## Notes
- **No auth/gating for private registries is implemented or documented anywhere in this repo** —
  confirmed via repo-wide search: no `middleware.ts`, no token/auth code. It's a fully public,
  static-file registry. If `@siavash/*` needs to be private, that mechanism has to come from
  elsewhere (the shadcn CLI's own docs, or host-level auth in front of `public/r/`).
- README points to a Tailwind v3 sibling, `registry-template-v3`, if we ever need v3.
- The license gap is the single biggest issue with this repo — resolve before reusing any file
  verbatim; there is no `LICENSE.txt` in this kit entry because none exists upstream to copy.
