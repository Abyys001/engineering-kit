# Full-Stack AI Agent Template

| Field | Value |
|---|---|
| Source URL | https://github.com/vstorm-co/full-stack-ai-agent-template |
| GitHub repository | `vstorm-co/full-stack-ai-agent-template` (owner Vstorm — organization) |
| Category | ai |
| License | MIT — `LICENSE.txt` (root `LICENSE`); no other license files found in the checkout |
| Author / organization | Vstorm (hr@vstorm.co) |
| Acquired | 2026-09-26 |
| Revision | `3428d9a6214619d3514312886d59a36400747b7d` (main, fetched 2026-09-27) |
| Attribution required | License notice only |
| Status | extraction-safe — plain MIT, no conditions beyond keeping the license text |

## Useful for
- LLM provider abstraction across OpenAI/Anthropic/Google/OpenRouter via PydanticAI, with parallel LangChain and LangGraph agent variants for comparison
- RAG pipeline end to end: ingestion, chunking, embeddings, vector store, retrieval, reranking, image description — with pluggable backends (Milvus/Qdrant/pgvector) and source connectors (S3, Google Drive)
- Streaming chat: WebSocket-based agent route (`api/routes/v1/agent.py`) plus a dedicated `rag.py` route, paired with a full frontend chat UI (store, hooks, components)
- Tool calling: code execution, URL fetch, web search, chart generation, ask-user, and a RAG-retrieval tool under `agents/tools/`
- Observability/eval scaffolding: optional Logfire and Sentry integration wired through cookiecutter flags (`enable_logfire`, `enable_sentry`) — no separate eval harness found
- Auth (JWT/JWKS/OAuth), Celery workers, admin panel, rate limiting, billing, email/channels services as a broader FastAPI+Next.js reference

## Where things live
- `source/template/{{cookiecutter.project_slug}}/backend/app/agents/` — `assistant.py` (PydanticAI), `langchain_assistant.py`, `langgraph_assistant.py`, `deepagents_assistant.py`, `pydantic_deep_assistant.py`; `tools/` has the individual tool implementations
- `source/template/{{cookiecutter.project_slug}}/backend/app/services/rag/` — `ingestion.py`, `embeddings.py`, `vectorstore.py`, `retrieval.py`, `reranker.py`, `documents.py`, `image_describer.py`, `sources/` (s3.py, google_drive.py, base.py), `connectors/`
- `source/template/{{cookiecutter.project_slug}}/backend/app/api/routes/v1/agent.py` and `rag.py` — WebSocket streaming + RAG endpoints
- `source/template/{{cookiecutter.project_slug}}/frontend/src/components/chat/`, `src/hooks/use-chat.ts`, `src/stores/chat-store.ts` — chat UI consuming the streaming backend
- `source/fastapi_gen/` — the cookiecutter CLI generator itself (`cli.py`, `generator.py`, `config.py`, `prompts.py`); not part of the generated app
- `source/template/{{cookiecutter.project_slug}}/` — the actual generated project root: `backend/` (FastAPI), `frontend/` (Next.js), `docker-compose*.yml`, `kubernetes/`, `nginx/`, `docs/`

## Known dependencies
- Generator (`pyproject.toml`): Python `>=3.11`, `click`, `cookiecutter`, `pydantic>=2.13`, `ruff`
- Generated backend (`template/.../backend/pyproject.toml`, cookiecutter-conditional): `fastapi>=0.135.3,<0.137`, `sqlalchemy[asyncio]>=2.0.40` or `sqlmodel>=0.0.38`, `alembic>=1.18.0`, `asyncpg`, `pydantic-ai-slim[openai,anthropic,google,openrouter,...]>=1.80.0`, optional `langchain>=1.2.0` + `langgraph>=0.4.0` + provider packages, optional `pymilvus>=2.6.0` / `qdrant-client>=1.14.0` / pgvector via existing asyncpg, `logfire[...]>=4.30.0`, `sentry-sdk[fastapi]>=2.53.0` — most gated behind cookiecutter flags, not all-installed at once
- Generated frontend: Next.js (see `frontend/package.json`, not read in this pass — check before promoting frontend code)

## Do not copy
- `source/assets/` — README screenshots/GIFs (`app_start.gif`, `assets/new2/*.png`, `telegram.png`, `logfire.png`, etc.) — marketing/doc images, not app code
- `source/template/{{cookiecutter.project_slug}}/frontend/public/` — not audited in this pass; check for unlicensed images/fonts before reuse
- Cookiecutter-templated files (`.py.jinja`-style Jinja logic inside `.py`/`.toml` files, e.g. `{%- if cookiecutter.* %}` blocks) — copy only the rendered logic, strip Jinja conditionals and adapt to the target project's actual dependency set

## Notes
- This is a **tarball snapshot, not a git clone** — no `.git` directory, no history. Refresh by re-downloading `https://codeload.github.com/vstorm-co/full-stack-ai-agent-template/tar.gz/3428d9a6214619d3514312886d59a36400747b7d` (swap the SHA for the current `main` tip) and re-extracting over `source/`.
- Agent config files (e.g. `.claude/`, `.cursor/` or similar) were deleted from this checkout per the task setup — do not expect them.
- Repo is a cookiecutter *generator*: the CLI (`fastapi_gen/`) renders `template/{{cookiecutter.project_slug}}/` into a real project. Read `template/cookiecutter.json` for the full flag matrix before assuming any given dependency/file is present — most AI-provider and infra choices are conditional.
- Multiple parallel agent implementations exist for the same task (PydanticAI, LangChain, LangGraph, DeepAgents) — useful for comparing provider-abstraction patterns side by side, but only one is wired in per generated project depending on cookiecutter choices.
