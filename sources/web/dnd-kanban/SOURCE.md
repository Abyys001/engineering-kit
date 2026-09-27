# React DnD Kit Tailwind shadcn/ui Kanban

| Field | Value |
|---|---|
| Source URL | https://github.com/Georgegriff/react-dnd-kit-tailwind-shadcn-ui |
| GitHub repository | `Georgegriff/react-dnd-kit-tailwind-shadcn-ui` (owner Georgegriff, User account) |
| Category | web |
| License | MIT — `LICENSE.txt` (root `LICENSE`); no other license files found in the checkout |
| Author / organization | George Griffiths |
| Acquired | 2026-09-26 |
| Revision | `3e1dbb0b872125191d5f9c3686060f64d304b99e` (main, committed 2024-05-18) |
| Attribution required | License notice only |
| Status | extraction-safe — plain MIT, no conditions beyond keeping the license text; but see version staleness in Notes |

## Useful for
- Minimal, readable multi-column Kanban board built directly on `@dnd-kit` (core/sortable/modifiers/utilities): column + card drag-and-drop, keyboard-accessible sorting preset
- Reference implementation of `dnd-kit`'s `multipleContainers` pattern adapted to a kanban board shape, including a documented custom keyboard coordinate-getter (`multipleContainersKeyboardPreset.ts`)
- Small shadcn/ui component set (card, badge, dropdown-menu, scroll-area, button) as a bare-minimum baseline to diff against our current versions

## Where things live
- `source/src/components/KanbanBoard.tsx` — top-level DndContext, column/card state, drag handlers — the core extraction target
- `source/src/components/BoardColumn.tsx`, `source/src/components/TaskCard.tsx` — sortable column and card components
- `source/src/components/multipleContainersKeyboardPreset.ts` — custom keyboard sensor/coordinate-getter for cross-column keyboard drag
- `source/src/components/ui/` — `card.tsx`, `badge.tsx`, `dropdown-menu.tsx`, `scroll-area.tsx`, `button.tsx` (shadcn/ui, Radix-backed)
- `source/src/components/theme-provider.tsx`, `source/src/components/ThemeToggle.tsx` — dark-mode toggle, generic reference only
- `source/developer.md` — author's own notes on the dnd-kit patterns used (read for rationale, not for reuse)

## Known dependencies
- `package.json`: react ^18.2.0, react-dom ^18.2.0, @dnd-kit/core ^6.0.8, @dnd-kit/sortable ^7.0.2, @dnd-kit/modifiers ^6.0.1, @dnd-kit/utilities ^3.2.1, @radix-ui/react-{dropdown-menu,scroll-area,slot}, class-variance-authority ^0.7.0, tailwindcss-animate ^1.0.6
- devDependencies: vite ^4.4.5, tailwindcss ^3.3.3, typescript ^5.0.2 — Vite SPA, not Next.js

## Do not copy
- `src/assets/react.svg`, `App.css`, `index.html` — Vite scaffold boilerplate, not part of the kanban feature
- `public/` favicon assets — generic Vite defaults, no license concern but nothing to reuse

## Notes
- Last pushed 2024-05-18 — React 18 (target stack is React 19) and dnd-kit v6/v7 (tablecn/shadcnspace are on dnd-kit v6.3–10 with React 19 already, and shadcnspace/data-table-filters show working newer-dnd-kit + React 19 combinations) — port the drag logic, don't copy dependency versions.
- Tailwind v3 config (`tailwind.config.js`, `tailwindcss-animate`) — needs updating to Tailwind v4 conventions for our stack.
- Radix-based `ui/` primitives — same Base UI porting need as the other Radix-based repos here; this repo's `ui/` set is small enough it's easier to just use our own existing kit primitives and only lift `KanbanBoard`/`BoardColumn`/`TaskCard`/keyboard-preset logic.
- No bundled fonts, no pro/paid directories, no separately-licensed assets found.
