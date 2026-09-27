# Vercel Chatbot

| Field | Value |
|---|---|
| Source URL | https://github.com/vercel/chatbot |
| GitHub repository | `vercel/chatbot` (canonical; renamed from "ai-chatbot" per README) |
| Category | ai |
| License | Apache-2.0, granted by the license's standard short notice (full text by reference) — `LICENSE.txt` |
| Author / organization | Vercel, Inc. |
| Acquired | 2026-09-26 |
| Revision | `c2f8235e1f3ea903ad8b7f61447c4f74164b5c58` (main, committed 2026-07-08) |
| Attribution required | License notice only — keep "Copyright 2024 Vercel, Inc." and ship the full Apache-2.0 text with extracted code |
| Status | extraction-safe — Apache-2.0 via its official boilerplate notice; GitHub's NOASSERTION only reflects the missing full text (see Notes) |

## Useful for
- Artifacts feature: structured AI-output documents (code/text/sheet/image) with client+server
  handlers — pattern for AI-generated-document / advanced "File Management" features.
- `components/ai-elements/` — small, Radix-based chat/tool-call UI kit (conversation, message,
  prompt-input, reasoning, tool, code-block) — fits our stack directly.
- Drizzle schema + migrations (`lib/db/schema.ts`, 8 Postgres tables, `drizzle-kit` scripts) —
  directly portable to our NestJS + Drizzle + Postgres backend.
- `lib/errors.ts` — typed `` `${ErrorType}:${Surface}` `` error-code + per-surface visibility map —
  reusable, framework-agnostic error-handling idea.
- `lib/ratelimit.ts` — plain `redis` client limiter (not Vercel KV) — portable as-is.
- Playwright e2e suite (`tests/e2e/*`, page objects in `tests/pages/`) — reference for our setup.
- NextAuth v5 Credentials + guest-user upgrade path — RBAC/session-shape reference, not
  code-portable to NestJS.

## Where things live
- `source/app/(chat)/api/chat/route.ts` — main chat endpoint; read first.
- `source/lib/ai/providers.ts` — `gateway.languageModel(modelId)`, see "Do not copy".
- `source/lib/ai/tools/` — tool defs (create/edit-document, get-weather, request-suggestions).
- `source/artifacts/{code,text,sheet,image}/{client.tsx,server.ts}` — artifact kind handlers.
- `source/components/ai-elements/`, `source/components/chat/` — UI kit + full chat app shell.
- `source/lib/db/schema.ts`, `queries.ts`, `migrations/` — Drizzle schema and migrations.
- `source/app/(auth)/auth.ts` — NextAuth setup.
- `source/tests/e2e/`, `source/playwright.config.ts` — Playwright suite.

## Known dependencies
- next 16.2.10, react 19.2.7, tailwindcss ^4.3.2, `radix-ui` ^1.6.1 (Radix-based, matches our stack).
- `ai` 7.0.15 + `@ai-sdk/react` 4.0.16 — Gateway-only, no direct Anthropic/OpenAI SDK deps.
- `drizzle-orm` ^0.45.2 + `postgres` ^3.4.9, `drizzle-kit` ^0.31.10; `next-auth` 5.0.0-beta.25.
- `redis` ^6.1.0, `resumable-stream` ^2.2.12 (Redis-backed, portable).
- `prosemirror-*`, `react-data-grid`, `codemirror`, `katex`, `streamdown` — artifact editors.
- `@playwright/test` ^1.61.1; Biome + `ultracite` for lint (not our ESLint/Prettier).

## Do not copy
- `lib/ai/providers.ts` — production path is 100% AI Gateway (`gateway.languageModel`), no
  non-Gateway fallback outside tests; pointing this at our FastAPI service means writing a new
  provider module, not adapting this one.
- `@vercel/blob` uploads, `@vercel/functions` (`geolocation`/`ipAddress`), `@vercel/analytics`,
  `@vercel/otel`, `botid` (Vercel Bot ID) — Vercel-platform services, no drop-in equivalent.
- `vercel.json`, `vercel-template.json` — deploy config. Branding: "Chatbot" name, OG images.

## Notes
- **License**: root `LICENSE` (12 lines / 82 words) is only the short Apache-2.0 attribution
  *notice* — "Copyright 2024 Vercel, Inc. / Licensed under the Apache License, Version 2.0 ... /
  See the License for the specific language governing permissions and limitations under the
  License." — not the full ~200-line Apache-2.0 legal text (no Definitions, Grant of Patent
  License, Redistribution §4, Trademark, Disclaimer sections). No `NOTICE` file, no SPDX headers
  in source, no `license` field in `package.json`, no README license section. That's why GitHub's
  detector can't match it and reports NOASSERTION: intent is clearly Apache-2.0, but the operative
  terms aren't reproduced in-repo. That notice is the Apache
  License's own "how to apply" boilerplate, so the grant is unambiguous — reclassified from
  REVIEW_REQUIRED to extraction-safe on 2026-09-26. Extracted code must carry the full text
  (https://www.apache.org/licenses/LICENSE-2.0.txt) plus the copyright line, and modified files
  must state that they were changed (Apache-2.0 §4b).
- Large, production-shaped app (auth + db + artifacts + tests) — budget more time to isolate one
  feature than for shadcn-chatbot-template.
- `POSTGRES_URL`/`REDIS_URL` are generic; only `AI_GATEWAY_API_KEY`/`BLOB_READ_WRITE_TOKEN` are
  Vercel-specific per `.env.example`.
