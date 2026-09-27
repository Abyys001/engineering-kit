# shadcn chatbot-template

| Field | Value |
|---|---|
| Source URL | https://github.com/shadcn-ui/chatbot-template |
| GitHub repository | `shadcn-ui/chatbot-template` (canonical) |
| Category | ai |
| License | MIT — `LICENSE.txt` |
| Author / organization | shadcn-ui |
| Acquired | 2026-09-26 |
| Revision | `f79416827acd90244683903a34343f58193432ac` (main, committed 2026-08-31) |
| Attribution required | License notice only |
| Status | extraction-safe — MIT, no conditions beyond keeping the license text |

## Useful for
- Streaming chat UI (Chat, App Shell): message list + composer on shadcn/react `message-scroller`
  and shadcn/typeset markdown rendering.
- Tool-call UI parts pattern: typed `part.type` switch dispatching to per-tool components, driven
  by `input-streaming` → `input-available` → `output-available`/`output-error` states.
- Citations: `sources-part.tsx` dedupes `source-url` parts into a "Searched N websites" drawer.
- Human-in-the-loop questionnaire UI: `question-card.tsx` + `components/ui/questionnaire.tsx` — a
  multi-step form the model triggers mid-conversation; a genuinely different component, not in
  default shadcn/ui.
- AI Chat feature: minimal end-to-end Next.js chat route + typed tool registry (`InferUITools`).

## Where things live
- `source/app/api/chat/route.ts` — the whole server: model allowlist, `validateUIMessages`,
  `streamText`, `toUIMessageStream`. Read this first.
- `source/lib/models.ts` — model id list, passed as bare strings resolved via the AI Gateway.
- `source/tools/` — one file per tool (`ask_user.ts`, `github_repo.ts`, `web_search.ts`) +
  `index.ts` composing them and exporting the `ChatUIMessage` type.
- `source/components/chat-message.tsx` + `source/components/parts/*` — part-type dispatch and
  per-part renderers (`text`, `sources`, `ask-user`, `github-repo`, `web-search`).
- `source/components/question-card.tsx`, `source/components/ui/questionnaire.tsx` — questionnaire UI.
- `source/components/ui/` — primitives (`message.tsx`, `message-scroller.tsx`, `bubble.tsx`,
  `item.tsx`, `empty.tsx`) — newer shadcn packages, not the classic block set.

## Known dependencies
- next 16.2.6, react 19.2.4, tailwindcss ^4, typescript ^5.
- UI primitives are **Base UI**, not Radix: `@base-ui/react` ^1.7.0 + `@shadcn/react` ^0.3.0 +
  `shadcn/typeset` (via `shadcn` CLI ^4.16.2) — drop-in with shadcn's Base UI flavor; with the
  Radix flavor, `Drawer`/`Select` must be re-derived (see `sources/CURATION.md`, decision 1).
- `ai` ^7.0.58, `@ai-sdk/react` ^4.0.61, `@ai-sdk/gateway` ^4.0.46, `@ai-sdk/anthropic` ^4.0.36,
  `@ai-sdk/openai` ^4.0.36, zod ^4.4.3, react-markdown ^10.1.0, react-shiki ^0.11.0.

## Do not copy
- Vercel AI Gateway coupling: `streamText({ model: modelId })` passes a bare string id, resolved
  by AI SDK v7 through the Gateway (`@ai-sdk/gateway`) via `AI_GATEWAY_API_KEY`/Vercel OIDC — there
  is no explicit provider client to swap. Pointing this at our FastAPI AI service means replacing
  the call with an explicit provider (custom `LanguageModelV2`, or an OpenAI-compatible client
  against FastAPI) and dropping `@ai-sdk/gateway` and the gateway-style ids in `lib/models.ts`.
- `tools/web_search.ts` calls each provider's *built-in* server-side search tool
  (`openai.tools.webSearch()`, `anthropic.tools.webSearch_20260209()`) — FastAPI-backed models
  won't have this; would need a custom search tool (pattern: `tools/github_repo.ts`).
- Deploy-with-Vercel button, `.env.example` gateway var, README's Vercel-specific security notes.

## Notes
- Small, single Next.js app, no monorepo. `AGENTS.md` is a generic "this Next.js version has
  breaking changes" note, not project-specific — skip it.
- `/api/chat` is intentionally public/unauthenticated in the template; add auth before reuse.
- Message part types are inferred end-to-end from tool definitions (`InferUITools`) — adding a
  tool is a typed, compiler-checked change, worth keeping even after the Gateway call is replaced.
