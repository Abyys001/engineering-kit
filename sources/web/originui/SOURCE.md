# Origin UI

| Field | Value |
|---|---|
| Source URL | https://github.com/shadcn/originui |
| GitHub repository | `shadcn/originui` — GitHub lists this as a **fork of `cosscom/coss`**, last pushed 2025-08-07, 14 stars: a stale snapshot on a personal account, not the active project. The repo's own README licenses section links to `https://github.com/origin-space/originui` as the canonical location, and the live demo is https://originui.com — `origin-space/originui` is where this project actually lives now. |
| Category | web |
| License | MIT — `LICENSE.txt`. No nested license files found (`find . -iname "LICENSE*"` under `source/` returns only the root file); `package.json` has no `license` field. |
| Author / organization | Origin UI (copyright holder per `LICENSE.md`); site credits @pacovitiello and @DavidePacilio (X/Twitter, per README) |
| Acquired | 2026-09-26 |
| Revision | `f4f366ae39759248d46b1252c52fbdc0bc01c285` (main, committed 2025-07-25) |
| Attribution required | License notice only |
| Status | extraction-safe — plain MIT, no extra conditions. (Caveat: this checkout is ~2 months stale relative to the fork's own last push, and further behind `origin-space/originui` upstream — re-verify against the live repo before large extraction pushes.) |

## Useful for
- The exact "beyond shadcn" application layer our priority list wants: advanced inputs (OTP, tags,
  currency, phone, password-strength), date/time pickers, an event calendar, file upload, data tables,
  filters, timeline, notifications, navbar pieces (team switcher, user menu, notification menu), steppers,
  tree views. Registers as a shadcn-compatible registry, so components can be pulled with the `shadcn` CLI.

## Where things live
- `source/config/components.ts` — **the index to open first.** Maps every category (slug + display name)
  to its list of `comp-XXX` names, e.g. `file-upload`, `calendar-date-picker`, `event-calendar`,
  `notification`, `navbar`, `stepper`, `table`, `timeline`, `tree`, `dropdown`, `pagination` (31 categories
  total). This is how a future session finds a component without opening 599 files.
- `source/registry/default/components/comp-01.tsx` … `comp-599.tsx` (599 files, contiguous) — flat,
  numbered, one component (with its own demo) per file; no descriptive names. Cross-reference with
  `config/components.ts` (category) or
  `registry.json` (per-item `meta.tags`, e.g. `["input", "label", "search"]`) to know what a given
  `comp-XXX` is.
- `source/registry/default/components/event-calendar/` — multi-file full calendar app (month/week/day/
  agenda views, drag-and-drop via `@dnd-kit`, event dialog) — not a single-file `comp-XXX`.
- `source/registry/default/components/navbar-components/` — reusable topbar pieces: `team-switcher.tsx`,
  `user-menu.tsx`, `notification-menu.tsx`, `filters.tsx`, `date-picker.tsx`, `settings-menu.tsx`,
  `theme-toggle.tsx`, `app-toggle.tsx`, `info-menu.tsx`, `logo.tsx`.
- `source/registry/default/ui/*.tsx` (43 files) — shadcn-equivalent primitives (accordion, dialog, select,
  stepper, timeline, multiselect, checkbox-tree, calendar/calendar-rac/datefield-rac, cropper, …) —
  Origin UI's own build of the base layer; README explicitly recommends using these over shadcn's for
  "a consistent styling experience."
- `source/registry.json` (10,989 lines) — full shadcn-schema registry index: per-item `dependencies`,
  `registryDependencies` (cross-component links as `https://originui.com/r/<name>.json`), and `meta.tags`.

## Known dependencies
- Next.js ^15.3.4, React ^19.1.0, Tailwind CSS v4 (`tailwindcss` ^4.1.10, `@tailwindcss/postcss`), the
  `radix-ui` umbrella package (`"latest"`) rather than per-primitive `@radix-ui/react-*` packages.
- `react-day-picker` ^9.7.0 (calendar/date picker), `@tanstack/react-table` ^8.21.3 (tables — one major
  behind shadcn-ui's v9), `@dnd-kit/*` (event calendar drag-and-drop), `cmdk` 1.1.1 (command menu),
  `sonner` ^2.0.5 (notifications/toasts), `zod` ^3.25.67.
- Tailwind v4 migration happened 2025-02-25 (per README); pre-migration v3 components are still served at
  `/legacy/comp-XX.json` via the CLI but are **not** present as separate files in this checkout — only the
  current v4 versions are in `registry/default/`. New components are v4-only going forward.

## Do not copy
- Nothing license-restricted found. Skip `app/` (the marketing/demo Next.js site itself, category routing,
  analytics) and `docs/` — that's the originui.com site, not extractable components, per the brief's
  "beyond docs-site plumbing" guidance.
- Treat this checkout as a snapshot: it trails both the fork's own later pushes (last push 2025-08-07,
  this revision is from 2025-07-25) and whatever `origin-space/originui` has shipped since — diff against
  upstream before assuming a category is complete or a component is current.

## Notes
- Organization = flat numbered files (`comp-01.tsx` … `comp-601`) + a hand-maintained category index
  (`config/components.ts`) + a registry index with tags (`registry.json`). There is no descriptive-name
  convention at the file level — always resolve through one of those two index files first.
- Two components ship as multi-file subdirectories instead of a single numbered file: `event-calendar/`
  and `navbar-components/`.
- Fork/provenance is exactly as the brief flagged: GitHub's fork parent (`cosscom/coss`) is unrelated
  noise (likely an old scaffold in the account's fork ancestry); the README's own license link and demo
  URL both point to `origin-space/originui` / originui.com as the real project home. Treat `shadcn/
  originui` as a read-only mirror for this curation, not a place to file issues or expect updates.
