# engineering-kit

Local source library for code reused across `~/Projects`: starters, UI components, feature templates, backend modules, mobile core, AI building blocks, and architecture patterns.

- **Policies** (source of truth; they win over this summary): [`engineering-policy.md`](docs/conventions/engineering-policy.md) for stack and reuse, [`curation-and-builder-policy.md`](docs/conventions/curation-and-builder-policy.md) for sources, curation, and building whole products. [`ui-design-policy.md`](docs/conventions/ui-design-policy.md) for UI design: adapt sources, vary visuals per product, keep a `docs/design/DESIGN.md` per app.
- **What exists:** [`INDEX.md`](INDEX.md) to read, [`catalog.json`](catalog.json) to search. Promotion backlog: [`sources/CURATION.md`](sources/CURATION.md). Not-yet-downloaded candidates: [`sources/CANDIDATES.md`](sources/CANDIDATES.md).
- **Workflow:** classify → select stack → search project → search kit → reuse → adapt → implement → test.
- **Empty directories are intentional:** nothing has been promoted there yet. Don't fill them with placeholders.

## Layout

| Path | Contents |
|---|---|
| `starters/` | Project starters: `web-saas`, `backend-api`, `flutter-app`, `ai-service` |
| `components/` | UI components: `web` (React + Tailwind + shadcn/ui), `flutter` |
| `features/` | Complete feature templates (components, api, hooks, schemas, types, tests): `auth`, `users`, `dashboard`, `settings`, `billing`, `notifications`, `file-upload`, `search`, `filtering`, `pagination` |
| `backend/` | NestJS modules: `authentication`, `authorization`, `logging`, `audit-log`, `permissions`, `jobs`, `notifications`, `file-storage` |
| `mobile/` | Flutter core: `networking`, `storage`, `routing`, `theme`, `common` |
| `ai/` | Python AI building blocks: `providers`, `rag`, `agents`, `embeddings`, `evaluation` |
| `patterns/` | Reference patterns: `architecture`, `api`, `database`, `infrastructure` |
| `docs/` | `conventions/` (standards and policies), `decisions/` (architecture decision records) |
| `sources/` | Upstream repositories kept as reference material: `web`, `dashboards`, `ai`, `backend`, `mobile`, `registries`, `references`. Projects never use them directly |

## Local-first rule

For any common feature, component, pattern, or piece of infrastructure, search in this order and stop at the first good match:

1. Current project, including its installed dependencies
2. The kit: `INDEX.md` / `catalog.json`
3. Downloaded sources: `sources/CURATION.md`, then the source's `SOURCE.md`
4. Official documentation
5. Internet / external repositories
6. Implement from scratch

Don't go to the internet for something that may already exist locally, and don't regenerate code the kit already has.

## Reuse-first rule

**REUSE → ADAPT → EXTEND**, never REBUILD → DUPLICATE → DRIFT. Match by similarity, not exact name:

| Request | Look in |
|---|---|
| Admin sidebar | `components/web` — Sidebar, AppShell, Navigation |
| User management | `features/users`, `features/auth` |
| Logging | `backend/logging` |
| AI chat endpoint | `ai/`, `starters/ai-service` |

Copy the closest match into the project and change only what the project needs. Rebuilding something the kit already covers needs a stated reason.

## Token-efficiency rule

- Read `INDEX.md`, `SOURCE.md`, and READMEs before any implementation file.
- In a source repository, locate the relevant files first; never dump a source tree recursively.
- Reference kit files by path instead of pasting them into the conversation.
- Don't rediscover the same implementation twice, or rewrite working code just to get a fresh version.
- Keep every README short.

## Stack mapping (new projects)

| Project type | Stack |
|---|---|
| SaaS web app | Next.js, React, TypeScript, Tailwind, shadcn/ui, TanStack Query · NestJS · PostgreSQL + Drizzle · Redis + BullMQ |
| Admin dashboard | Next.js, React, TypeScript, Tailwind, shadcn/ui, TanStack Query · NestJS API |
| Mobile app | Flutter, Dart, go_router · repository-based architecture |
| AI service | Python, FastAPI, Pydantic · PostgreSQL · Redis · AI/ML libraries as needed |
| AI + web product | Next.js · NestJS · Python/FastAPI AI service · PostgreSQL · Redis + BullMQ |
| Background processing | NestJS or Python worker (by domain) · Redis + BullMQ |

- Add Redis/BullMQ only when the app needs caching, rate limiting, queues, pub/sub, or background work.
- Infrastructure: Docker, Docker Compose, GitHub Actions, Nginx or Caddy.
- Existing projects keep their stack; migrate only when explicitly asked.
- The stack is a default, not a law. To deviate, state the standard option, why it falls short, the alternative, and its trade-offs. The owner decides.
- Logging, error handling, validation, testing, infrastructure, and dependency standards: `engineering-policy.md` §25–§30.

## Using a template

1. Pick the closest starter, feature, or component and read its README.
2. Copy it into `~/Projects/<project>`. For a starter, remove demo code and any infrastructure the project doesn't need.
3. Adapt it inside the project.

**kit → copy → project → adapt.** Never edit a kit template to satisfy one project.

## Sources

Each upstream repository lives at `sources/<category>/<name>/`:

- `source/` — shallow clone at the revision recorded in `SOURCE.md`. Dependencies are never installed here.
- `SOURCE.md` — license, revision, attribution, status, where things live, what must not be copied.
- `LICENSE.txt` — the upstream license, verbatim.

Status values: **extraction-safe** (permissive license; copy and adapt, keeping the notice) · **reference-only** (learn the pattern, don't copy the code) · **REVIEW_REQUIRED** (licensing or attribution issue; don't extract until reviewed).

MIT, Apache-2.0, BSD, and ISC are fine for the production kit. Copyleft, non-commercial, unclear or mixed licensing, extra attribution demands, and separately licensed assets are `REVIEW_REQUIRED` — documented, never extracted silently.

To move a source to its latest upstream revision, run from the kit root, then update `Revision` in its `SOURCE.md`:

```bash
git -C sources/<category>/<name>/source fetch --depth 1 origin HEAD
git -C sources/<category>/<name>/source reset --hard FETCH_HEAD
```

Upstream clones are git-ignored (see `.gitignore`); only their metadata belongs in the kit's history.

Upstream agent config (`.claude/`, `CLAUDE.md`, `AGENTS.md` at any depth, `CLAUDE.local.md`, `.mcp.json`, `.agents/`, `.cursor/`, `.cursorrules`, `.windsurf*`, `.codex/`, `.gemini/`, Copilot instructions) is excluded from every clone with sparse-checkout, so third-party instructions, skills, and hooks never load into our sessions. Read an excluded file with `git -C <clone> show HEAD:CLAUDE.md`. Apply the same exclusion right after cloning any new source:

```bash
git -C sources/<category>/<name>/source sparse-checkout set --no-cone '/*' '!.claude/' '!CLAUDE.md' '!CLAUDE.local.md' '!.mcp.json' \
  '!AGENTS.md' '!**/AGENTS.md' '!**/CLAUDE.md' '!.agents/' '!.cursor/' '!.cursorrules' '!.windsurf/' '!.windsurfrules' \
  '!.github/copilot-instructions.md' '!.codex/' '!.gemini/'
```

## Promoting code into the kit

Sources never go straight into a project: **source → select → clean → normalize → our conventions → kit → project**.

Promote only when all of these hold:

- Reusable and isolated; no project-specific business logic.
- Matches our stack; every dependency is necessary; no half-a-repository imports.
- Understandable and typed, with clear props or interfaces; tested where useful.
- License and attribution recorded, with notices kept next to the code where the license requires it.
- Better than what the kit already has. If something similar exists, improve or generalize it, or document the difference — no near-duplicates.

Name by function, not by origin: `components/web/cards/animated-stat-card.tsx`, not `components/from-kokonut/<upstream-name>.tsx`. Keep alternatives only when they differ meaningfully in behavior or visual style.

Every template ships a short `README.md` covering:

- the problem it solves and when to use it
- important dependencies
- expected integration points
- assumptions
- how to adapt it

Every promotion updates `INDEX.md` and `catalog.json` in the same change.

## Maintaining the kit

- Improving a shared template is an explicit kit change, never a side effect of project work.
- Review external code before it enters the kit; never pull in random repositories or snippets blindly.
- Record significant decisions in `docs/decisions/`.
