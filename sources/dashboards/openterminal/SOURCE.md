# OpenTerminal

| Field | Value |
|---|---|
| Source URL | https://github.com/ErTasselli/OpenTerminal |
| GitHub repository | `ErTasselli/OpenTerminal` (owner ErTasselli, User account) |
| Category | dashboards |
| License | MIT — `LICENSE.txt` (root `LICENSE`, copyright "OpenTerminal contributors"); no other license files found in the checkout |
| Author / organization | ErTasselli (OpenTerminal contributors) |
| Acquired | 2026-09-26 |
| Revision | `041822cfc2b54baf72001379618b1bc721567ab8` (committed 2026-09-21) |
| Attribution required | License notice only |
| Status | extraction-safe — plain MIT, no conditions beyond keeping the license text |

## Useful for
- Bloomberg-terminal-style financial dashboard: draggable/resizable widget grid, command palette, multi-panel workspace layout
- Widget patterns for market data: charts (`ChartWidget` via lightweight-charts), heatmaps, watchlists, screeners, options chains, crypto, macro/economic calendar, news, insider trades, portfolio, recap
- Backend provider-adapter pattern: `server/src/providers/` — one file per data source (Binance, Yahoo, Nasdaq, FRED, ECB, CoinGecko, SEC EDGAR, FINRA, TradingView, Stooq, econ calendar) behind a `registry.ts`, plus `cache.ts`/`rateLimit.ts`/`concurrency.ts` cross-cutting concerns — good reference architecture for a data-aggregation API even though our target backend is NestJS, not this Express-style server

## Where things live
- `source/web/components/Workspace.tsx`, `Sidebar.tsx`, `TopBar.tsx`, `CommandPalette.tsx`, `Terminal.tsx`, `Flash.tsx` — shell/layout components
- `source/web/components/widgets/` — 13 widget components, one file each
- `source/web/store/terminal.ts` — single Zustand store driving the whole layout/workspace state
- `source/server/src/routes/` — `market.ts`, `portfolio.ts`, `ai.ts` — API route handlers
- `source/server/src/providers/` — per-source data adapters + `registry.ts`
- `source/data/readme.md` — notes on the `data/` directory's role (seed/sample data, not code)
- `source/docker-compose.yml` — dev orchestration for web + server

## Known dependencies
- `web/package.json`: next ^15.5.25, react ^19.0.0, tailwindcss ^4.0.0, `@tanstack/react-query` ^5.64.1, zustand ^5.0.3, `react-grid-layout` ^1.5.0, `lightweight-charts` ^5.0.0, recharts ^2.15.0, d3 ^7.9.0, hls.js ^1.6.16 (video streaming, likely for a TV/news widget)
- `server/`: separate Node/TS package (Express-shaped, not inspected line-by-line) with its own `package.json`

## Do not copy
- Nothing found requiring exclusion — no separately-licensed fonts, images, videos, or 3D assets in this checkout (`web/public` and any asset dirs are empty/absent)
- `server/src/providers/*` make live calls to third-party financial APIs (Binance, Yahoo, FRED, etc.) with their own ToS — the adapter *code* is MIT and copyable, but reusing it means accepting each upstream API's own terms, separate from this repo's license

## Notes
- Small checkout (7.2 MB), no bundled binary assets to clear.
- Layout stack (`react-grid-layout` + Zustand) is a solid pattern-reference for any future draggable-widget dashboard in our kit, independent of the finance domain.
- Backend is a standalone Express-style Node server, not NestJS — treat `server/` as pattern-only (provider-adapter + registry idea), not a drop-in module.
