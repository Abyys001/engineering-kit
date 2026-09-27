# Tremor Raw

| Field | Value |
|---|---|
| Source URL | https://github.com/tremorlabs/tremor |
| GitHub repository | `tremorlabs/tremor` (organization; canonical) |
| Category | dashboards |
| License | Apache-2.0 — `LICENSE.txt` (root Apache 2.0 full text; no NOTICE file anywhere in the checkout) |
| Author / organization | Tremor Labs (tremorlabs) |
| Acquired | 2026-09-26 |
| Revision | `ca4d588f47820ff3d514d37fa4ee08a4222dec11` (main, committed 2025-10-10) |
| Attribution required | License notice only |
| Status | extraction-safe — permissive Apache-2.0, no NOTICE, no attribution ask beyond keeping license text |

## Useful for
- Charts: BarChart, AreaChart, LineChart, ComboChart, DonutChart, SparkChart, CategoryBar, BarList,
  Tracker — the deepest chart coverage of the three repos, all on Recharts.
- KPI/metric building blocks: Card, BarList, ProgressCircle, ProgressBar (compose into KPI cards; no
  pre-assembled "KPI Card" component, but the primitives are here).
- Table, DatePicker/Calendar, Combobox-adjacent Select/SelectNative, Dialog/Drawer/Popover/Toast,
  form inputs (Input, Checkbox, RadioGroup, RadioCardGroup, Slider, Switch, Textarea).
- Not a source for App Shell / Sidebar / Nav — this is a pure component library (like shadcn/ui's
  model: copy-paste, `private: true`, no npm publish), not a dashboard app.

## Where things live
- `source/src/components/<Name>/<Name>.tsx` — 39 component folders, one per component; each also has
  `*.stories.tsx`, `*.spec.ts`, and a per-component `changelog.md`. Header comment e.g.
  `// Tremor Button [v1.0.0]` gives per-file versioning.
- `source/src/utils/` — shared helpers (`cx`, `focusRing`) every component imports.
- `source/scripts/component-folder.js` — Tremor's own import-consolidation tool; not needed by us.

## Known dependencies
- react/react-dom `^18.3.1` (not 19), recharts `^2.15.2`, tailwindcss `^4.1.3`, tailwind-variants
  `^1.0.0`, tailwind-merge `^3.2.0`.
- Radix UI primitives per-component (`@radix-ui/react-*`, mixed `1.x`/`2.x`), `@remixicon/react`
  (icons), `date-fns ^3.6.0`, `react-day-picker ^8.10.1`, `@react-aria/datepicker` +
  `@internationalized/date` for Calendar/DatePicker.

## Do not copy
- `source/public/images/tremor-logo-*.svg`, `github-banner.png` — Tremor's own branding/trademark.
- Storybook config (`.storybook/`) and Playwright setup are project scaffolding, not shell code.

## Notes
- Shallow clone (depth 1, no tags) so full history isn't visible, but the signal that matters: last
  commit 2025-10-10, ~11.5 months with nothing pushed as of today (2026-09-26). `.github/workflows/`
  has only a Playwright CI job; no recent releases/tags found. Treat as stable-but-quiet, not abandoned
  — API surface is small and finished-feeling, not obviously bit-rotting.
- React 18 (not 19) and Recharts v2 (not v3, unlike the other two dashboard repos) — check compatibility
  before mixing Tremor charts into a React 19 / Recharts v3 app shell from another source.
