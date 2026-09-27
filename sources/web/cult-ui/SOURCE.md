# Cult UI

| Field | Value |
|---|---|
| Source URL | https://github.com/nolly-studio/cult-ui |
| GitHub repository | `nolly-studio/cult-ui` (owner nolly-studio, User account — not a fork) |
| Category | web |
| License | MIT — `LICENSE.txt` (root `LICENSE.md`); no other license files found in the checkout |
| Author / organization | Jordan Gilliam (nolly-studio) |
| Acquired | 2026-09-26 |
| Revision | `ee98a5dd2e319b63cc2e707dd968d6af04209b7e` (main, committed 2026-09-23) |
| Attribution required | License notice only |
| Status | extraction-safe — plain MIT, no conditions beyond keeping the license text |

## Useful for
- Distinctive cards: `minimal-card`, `texture-card`, `cutout-card`, `shift-card`, `expandable-card`
- Hero/landing sections: `hero-liquid-metal`, `hero-dithering`, `hero-heatmap`, `hero-color-panel`, `hero-static-radial-gradient`, `feature-carousel`, `logo-carousel`, `tweet-grid`
- Interactive controls: `dock`, `dynamic-island`, `floating-panel`, `side-panel`, `family-button`/`family-drawer`, `sortable-list`, `three-d-carousel`, `popover-form`, `color-picker`
- Auth starter block: `block/authentication-01.tsx` (web-saas starter — Authentication need)
- Checked for sidebar/topbar/menu components: none exist in this repo

## Where things live
- `source/apps/www/registry/default/ui/` — 82 standalone components, one `.tsx` file each; the real extraction target (shadcn-registry style)
- `source/apps/www/registry/default/block/authentication-01.tsx` — only block; auth page starter
- `source/apps/www/registry/default/example/` — 79 usage-demo files, pair with `ui/` files to see props in use
- `source/apps/www/components/landing/` — this site's own marketing sections (reference only, not reusable)
- Root `package.json` workspaces list `apps/*`, `packages/*`, `templates/*`, but only `apps/www` exists in this checkout — the `cult-ui` CLI package and starter templates are absent.

## Known dependencies
- `apps/www/package.json`: next 16.3.6, react 19.2.4, tailwindcss ^4.2.2, motion (Framer Motion) ^12.35.2
- Radix UI primitives + class-variance-authority pattern (shadcn-adjacent, not literal shadcn/ui files)

## Do not copy
- `apps/www/public/cult-pro-images/`, `apps/www/public/migrate/` — marketing/paid-product screenshots, not components
- `apps/www/components/landing/assets/` (cult-logo-gpt.png, rune-hero.png, etc.) — project-specific branding
- `apps/www/fonts/haskoy.ttf` and `apps/www/public/fonts/haskoy.ttf` — bundled font, currently commented out/unused in `lib/fonts.ts`, no license or credit found anywhere in the repo; don't reuse without independently clearing it

## Notes
- Checkout is 242 MB, almost entirely `apps/www/public/cult-pro-images/*.png` (~40 marketing screenshots, 1.5–4.2 MB each, for a paid "Cult Pro" upsell) — not code, safe to skip when promoting.
- No videos, 3D models, or icon-set assets found beyond the one unused TTF font.
- `ui/shader-shape-lens-blur copy.tsx` looks like a leftover dev duplicate (space + "copy" in filename) — diff against `shader-lens-blur.tsx` before extracting either.
