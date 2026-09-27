# KokonutUI

| Field | Value |
|---|---|
| Source URL | https://github.com/kokonut-labs/kokonutui |
| GitHub repository | `kokonut-labs/kokonutui` (organization, canonical location) |
| Category | web |
| License | MIT — `LICENSE.txt` (root `LICENSE`) + one nested Apache-2.0 file that covers an unrelated bundled tool (see Notes) |
| Author / organization | kokonutUI (kokonut-labs) |
| Acquired | 2026-09-26 |
| Revision | `83eec6d982d400a18438001a8efdbac1f159dd43` (main, committed 2026-08-20) |
| Attribution required | License notice only |
| Status | extraction-safe — plain MIT for all component code |

## Useful for
- KPI/stat & activity pieces: `apple-activity-card`, `bento-grid`, `currency-transfer`, `tweet-card`
- Dashboard-adjacent cards: `card-flip`, `card-stack`, `spotlight-cards`, `carousel-cards`, `liquid-glass-card`, `mouse-effect-card`
- Navigation/chrome: `morphic-navbar`, `toolbar`, `profile-dropdown`, `team-selector`, `smooth-tab`, `smooth-drawer`
- AI Chat need: `ai-prompt`, `ai-input-search`, `ai-voice`, `ai-loading`, `ai-text-loading`
- File Management / Search needs: `file-upload`, `avatar-picker`, `action-search-bar`
- Motion accents for visual variety: `gradient-button`, `particle-button`, `attract-button`, `hold-button`, `glitch-text`/`shimmer-text`/`matrix-text` family

## Where things live
- `source/components/kokonutui/` — all 44 shipped components, flat directory, one `.tsx` file each — the extraction target
- `source/registry/registry-components.ts` — maps each component to its deps/files; cross-check before copying to catch hidden sub-deps
- `source/content/docs/` — MDX docs per component (usage examples, prop notes)
- `source/hooks/` — 8 small reusable hooks (debounce, click-outside, file-input, etc.), usable standalone

## Known dependencies
- `package.json`: next ^16.2.10, react ^19.2.7, tailwindcss v4 (`@tailwindcss/postcss` ^4.3.0), motion (Framer Motion) ^12.23.25
- Radix UI (dropdown-menu, slot, tooltip), class-variance-authority, embla-carousel — all Next/React-native, no stack mismatch

## Do not copy
- `source/.agents/skills/frontend-design/` — a bundled Claude Code agent skill under Apache-2.0, unrelated to the UI kit; don't attribute it as kokonutUI's license
- `source/app/`, `source/content/` docs-site scaffolding — this site's own Fumadocs setup, not components
- `source/registry.json`, `source/public/r/*.json` — generated registry artifacts; regenerate from source rather than copying

## Notes
- Nested license: `source/.agents/skills/frontend-design/LICENSE.txt` is the standard **Apache License 2.0** (full text, no modifications). It covers only that one bundled agent-skill directory (a dev-tooling skill for contributors), not any kokonutUI component or the site itself. No NOTICE file accompanies it.
- Small, clean checkout: 7.1 MB. No videos, fonts, or 3D models found; largest `public/` asset is `public/pro.png` at 640 KB.
- Root `package.json` has no top-level `"license"` field (`"private": true`); the root `LICENSE` file is the authority and is plain MIT.
