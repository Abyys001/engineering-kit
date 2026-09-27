# React Email

| Field | Value |
|---|---|
| Source URL | https://react.email |
| GitHub repository | `resend/react-email` (owner resend, org — not a fork) |
| Category | web |
| License | MIT — root `LICENSE.md` (copyright 2024 Plus Five Five, Inc; standard MIT body, no "MIT License" title line). Per-package `license.md` files at `packages/create-email`, `packages/editor`, `packages/react-email`, `packages/render`, `packages/ui`, and app-level `apps/demo`, `apps/docs`, `apps/web` are the same MIT text under the same copyright holder (2024–2026); no conflicting terms |
| Author / organization | Plus Five Five, Inc (Resend) |
| Acquired | not acquired — license and revision verified over the GitHub API on 2026-09-27; no checkout exists |
| Revision | `15419ff1f4cd0e32ed2c15a4a9182cc47a200a60` (committed 2026-09-23) |
| Attribution required | License notice only |
| Status | license-cleared, not acquired — plain MIT throughout, including every per-package file. Not cloned: disk budget, and only `packages/ui` + `packages/render` are actually wanted |

## Useful for
- Transactional email templating: React components that render to table-based HTML with inlined CSS, plus a render pipeline usable from a Node worker
- Fills a real kit gap — nothing in `sources/` covers email rendering, and every product with notifications needs it (see the P1 gap list in `sources/CANDIDATES.md`)

## Where things live
Verified from the pinned revision's git tree (paths only):
- `packages/ui/` — the email primitives (`Html`, `Head`, `Body`, `Container`, `Section`, `Row`, `Column`, `Button`, `Link`, `Text`, `Heading`, `Img`, `Hr`, `Preview`, `Tailwind`, …). **The extraction target.**
- `packages/render/` — `render()` / `renderAsync()`, the HTML + plain-text output pipeline. Second extraction target.
- `packages/editor/`, `packages/create-email/`, `packages/react-email` (the CLI/preview server) — tooling, not product code
- `examples/` — 16 one-file provider integrations (`resend`, `aws-ses`, `nodemailer`, `postmark`, `sendgrid`, `mailgun`, `brevo`, `mailersend`, `mailtrap`, `plunk`, `scaleway`, `zeptomail`, `azure-communication-email`, `eusend`, `lettermint`, `mailchimp-transactional`) — the cheapest reference for wiring a sender
- `apps/demo`, `apps/docs`, `apps/web`, `playground/emails`, `benchmarks/` — site and harness; reference only

## Known dependencies
Not inspected — no checkout. `packages/ui` has an optional Tailwind component implying a Tailwind-to-inline-CSS step; confirm the Tailwind major matches the kit's v4 target before promoting.

## Do not copy
- `skills/react-email/` — upstream agent config; never installed or trusted (untrusted-source rule)
- `apps/web/`, `apps/docs/` — marketing/docs site, including its assets

## Notes
- Correct acquisition shape is a sparse checkout of `packages/ui`, `packages/render`, and `examples/resend` — a few hundred KB, not the monorepo.
- `fetch: false` in `sources/MANIFEST.json`; flip it with a `sparse` list when the first product needs outbound email.
