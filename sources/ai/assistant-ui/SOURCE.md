# assistant-ui

| Field | Value |
|---|---|
| Source URL | https://github.com/assistant-ui/assistant-ui |
| GitHub repository | `assistant-ui/assistant-ui` (owner assistant-ui, org) |
| Category | ai |
| License | MIT — `LICENSE.txt` (root `LICENSE`, copyright AgentbaseAI Inc.); per-package MIT licenses found in `python/assistant-stream/LICENSE` (Simon Farshid) and `python/assistant-ui-sync-server-api/LICENSE` (AgentbaseAI Inc.) — no conflicting terms |
| Author / organization | AgentbaseAI Inc. |
| Acquired | 2026-09-26 |
| Revision | `2980cafdf4f894995daa77c34f3db09e74205ff7` (committed 2026-09-26) |
| Attribution required | License notice only |
| Status | extraction-safe — plain MIT throughout; no Commons Clause / enterprise carve-outs found |

## Useful for
- Headless chat primitives (Radix-style compound components) for message threads, composer, attachments, branch picking, chain-of-thought, reasoning display, suggestions, action bars
- Pre-styled `packages/ui` components layered on the primitives — closest thing here to a shadcn-registry for chat UI
- Runtime adapters: AI SDK, LangGraph, LangChain, Google ADK, MCP, generative UI — reference for wiring patterns even where we won't take the code (React-only for our stack; `react-native`, `vue`, `svelte` packages are out of scope)

## Where things live
- `source/packages/react/src/primitives/` — headless primitives (`thread`, `composer`, `message`, `messagePart`, `attachment`, `branchPicker`, `chainOfThought`, `reasoning`, `suggestion`, `actionBar`, `selectionToolbar`, etc.), each a `<Name>.<Part>` compound export
- `source/packages/ui/src/components/` — styled components built on the primitives, paired `globals.css`
- `source/packages/react-hook-form/`, `source/packages/react-markdown/`, `source/packages/react-syntax-highlighter/` — small focused integration packages
- `source/apps/docs/` — Next.js docs/demo site; `apps/docs/components/pages/shop/` is an unrelated internal demo flow (fake e-commerce wizard), not upstream licensing — ignore
- `source/templates/` — starter templates (check before use; not inspected in depth here)

## Known dependencies
- Monorepo is pnpm + turbo; `packages/react` and `packages/ui` target React 19-era peer ranges; `packages/ai-sdk` pairs with Vercel `ai` SDK; `packages/cloud` is a hosted-service client SDK (network calls to assistant-ui's own cloud, not a UI component — treat as reference only)
- Radix UI–based primitives (not Base UI) — adapting to our Base UI target stack needs a substitution pass, not a drop-in copy

## Do not copy
- `packages/cloud/` — client for AgentbaseAI's hosted service; pulling it in means depending on their backend
- `apps/docs/components/pages/shop/` — internal demo/marketing flow unrelated to the library surface
- `packages/react-native/`, `packages/vue/`, `packages/svelte/` — off-stack framework targets

## Notes
- Largest of the four checkouts (132 MB) — mostly the monorepo's many packages/examples/evals, not binary assets; no fonts, images, or 3D models found requiring separate clearance.
- Primitives are Radix-pattern (compound-component, unstyled) — good reference for the *shape* of our own Base UI chat primitives even though the underlying primitive library differs.
