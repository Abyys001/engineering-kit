# Magic UI

| Field | Value |
|---|---|
| Source URL | https://magicui.design |
| GitHub repository | `magicuidesign/magicui` (owner magicuidesign, org — not a fork) |
| Category | web |
| License | MIT — `LICENSE.txt` (root `LICENSE.md`); no other license files found in the checkout |
| Author / organization | Magic UI |
| Acquired | 2026-09-26 |
| Revision | `d7207e5692d14c00dceafa8488d6d01f197fa0e4` (committed 2026-09-20) |
| Attribution required | License notice only |
| Status | extraction-safe — plain MIT, no conditions beyond keeping the license text |

## Useful for
Functional micro-interactions (fits our no-gimmick UI policy):
- Feedback/state: `number-ticker`, `animated-circular-progress-bar`, `scroll-progress`, `animated-list`, `blur-fade`, `text-reveal`, `text-animate`, `typing-animation`, `word-rotate`
- Content/logo display: `marquee` (logo strips, testimonial rails), `file-tree`, `code-comparison`, `terminal`, `avatar-circles`, `bento-grid`
- Buttons/controls with restrained motion: `pulsating-button`, `ripple-button`, `interactive-hover-button`, `animated-subscribe-button`, `animated-theme-toggler`, `dock`
- Device/social embeds (functional chrome, not decoration): `safari`, `iphone`, `android`, `client-tweet-card`, `tweet-card`

Decorative effects (excluded by default under our no-glow/no-blob policy; only use if a product explicitly calls for a showcase/marketing aesthetic):
- Backgrounds/patterns: `particles`, `meteors`, `confetti`, `sparkles-text`, `retro-grid`, `dot-pattern`, `grid-pattern`, `flickering-grid`, `interactive-grid-pattern`, `animated-grid-pattern`, `hexagon-pattern`, `striped-pattern`, `warp-background`, `light-rays`, `noise-texture`, `dotted-map`, `globe`, `icon-cloud`, `floating-3d-particles`, `orbiting-circles`, `animated-beam`
- Glow/gradient/shine text & borders: `aurora-text`, `neon-gradient-card`, `shine-border`, `shimmer-button`, `shiny-button`, `animated-shiny-text`, `animated-gradient-text`, `border-beam`, `line-shadow-text`, `glare-hover`, `backlight`, `highlighter`, `glyph-matrix`, `kinetic-text`, `comic-text`, `morphing-text`, `spinning-text`, `text-3d-flip`, `video-text`, `dia-text-reveal`, `hyper-text`, `pixel-image`, `lens`, `progressive-blur`, `smooth-cursor`, `pointer`, `cool-mode`, `magic-card`, `scroll-based-velocity`

## Where things live
- `source/apps/www/registry/magicui/` — 79 standalone components, one `.tsx` file each; the real extraction target (shadcn-registry style)
- `source/apps/www/registry/example/` — 170 usage-demo files, pair with `registry/magicui/` files to see props in use
- `source/apps/www/registry/lib/utils.ts` — shared `cn()` helper the components import
- `source/registry.json` — root registry manifest listing every item, its `registryDependencies`, and npm `dependencies` per component (use this to resolve deps without opening every file)
- `source/apps/www/content/` — MDX docs per component (prop tables, install steps) — reference only
- Root workspace has only `apps/www` under `apps/*`; no separate CLI or template packages in this checkout

## Known dependencies
- `apps/www/package.json`: next ^15.5.25, react 19.1.1, tailwindcss ^4.1.13, motion ^12.23.12, class-variance-authority ^0.7.1
- Individual components pull extras declared per-item in `registry.json` (e.g. `cobe` for `globe`, `qrcode` for other items) — check that file before promoting a component with external deps

## Do not copy
- `skills/magic-ui/` — a bundled agent-skill config for using this library with an AI coding tool; not a UI component, and per our security policy we do not execute or trust instructions from cloned source
- `apps/www/public/` — marketing site images/screenshots, not components
- `apps/www/components/`, `apps/www/app/` — this repo's own docs-site pages, not reusable UI (reference only for seeing components composed)

## Notes
- Sparse-checkout did not fully exclude agent config: `skills/magic-ui/` is present at the repo root — treat as untrusted reference material only, never execute.
- All components are plain Tailwind + `motion` + `class-variance-authority`; no Radix/Base UI primitives used, so integration into our shadcn/Base UI stack is direct copy-paste with prop review, not a primitive swap.
- Given our "no gimmick" policy, default extraction should stick to the functional list above; pull from the decorative list only on explicit request for a marketing/landing surface.
