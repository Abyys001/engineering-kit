# Agent Elements

| Field | Value |
|---|---|
| Source URL | https://github.com/21st-dev/agent-elements |
| GitHub repository | `21st-dev/agent-elements` (owner 21st-dev, org) |
| Category | ai |
| License | MIT — `LICENSE.txt` (root `LICENSE`); no other license files found in the checkout |
| Author / organization | 21st.dev |
| Acquired | 2026-09-26 |
| Revision | `b04b36cb6381a1dd1a0e86cc7c90564ddcd56d37` (committed 2026-04-24) |
| Attribution required | License notice only |
| Status | extraction-safe — plain MIT, no conditions beyond keeping the license text |

## Useful for
- Chat/agent UI primitives: message list, user message, error message, markdown renderer, input bar, send button
- Tool-call rendering: `generic-tool`, `bash-tool`, `edit-tool`, `search-tool`, `mcp-tool`, `plan-tool`, `question-tool`, `subagent-tool`, `todo-tool`, `tool-group`, `thinking-tool`
- Chrome: `agent-chat` shell, `mode-selector`, `model-picker`, `attachment-button`/`file-attachment`, `suggestions`, `text-shimmer`, `spiral-loader`
- Directly on our target primitive stack: built on `@base-ui/react` (not plain Radix), shadcn CLI-distributed registry

## Where things live
- `source/lib/agent-ui/components/` — the actual component source (imported by the registry build)
- `source/public/r/*.json` — built shadcn registry items (one JSON per component, e.g. `agent-chat.json`, `bash-tool.json`); `index.json` lists all 26
- `source/app/(docs)/docs/` — docs/demo pages pairing with each component
- `source/agents/my-agent/index.ts` — example agent wiring (`@21st-sdk/agent`), reference only, not a UI component
- `source/skills/agent-elements/` — a Claude skill (`SKILL.md`, `README.md`) bundled by the upstream repo itself; per this task's security rule, ignore its instructions, do not install as a skill

## Known dependencies
- `package.json`: next 16.1.6, react 19.2.3, tailwindcss ^4.2.1, `@base-ui/react` ^1.3.0, `ai` (Vercel AI SDK) ^5.0.0, motion ^12.0.0, shadcn ^4.0.6, zod ^4.3.6, cmdk ^1.1.1, lottie-react ^2.4.0

## Do not copy
- `public/fonts/Geist-Regular.ttf`, `Geist-Medium.ttf`, `Geist-SemiBold.ttf` — bundled Vercel Geist font, no license file included in this checkout; re-source Geist independently (it's OFL-licensed upstream) rather than lifting the binary from here
- `agents/my-agent/`, `app/api/agent/` — server-side agent runtime wiring tied to `@21st-sdk/*` packages, not portable UI

## Notes
- Small checkout (3.3 MB), no images/videos/3D assets beyond the three font files.
- Style is `base-nova` per `components.json` — confirms these are Base UI–flavored shadcn components, the closest match of the four repos to our target `shadcn/ui on Base UI` stack.
- `public/r/*.json` registry files embed the component source inline; reading the `.tsx` under `lib/agent-ui/components/` directly is simpler for extraction.
