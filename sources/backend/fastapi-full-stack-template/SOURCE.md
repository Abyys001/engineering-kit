# FastAPI Full Stack Template

| Field | Value |
|---|---|
| Source URL | https://github.com/fastapi/full-stack-fastapi-template |
| GitHub repository | `fastapi/full-stack-fastapi-template` (organization: fastapi) |
| Category | backend |
| License | MIT — `LICENSE.txt` (verbatim copy of root `LICENSE`; no license field in `backend/pyproject.toml` or `frontend/package.json`, no nested LICENSE/NOTICE files) |
| Author / organization | fastapi (originally Sebastián Ramírez — copyright holder named in LICENSE) |
| Acquired | 2026-09-26 |
| Revision | `cb740b656d7a0a6c5e12c7bf8e50343ec94ee9c7` (master, committed 2026-09-01) |
| Attribution required | License notice only |
| Status | extraction-safe — MIT, no extra conditions; but see Notes for a real bug that blocks copying one file as-is |

## Useful for
- FastAPI app layout that transfers to `starters/ai-service`: `backend/app/{core,api,models.py,crud.py,main.py}` split — `api/routes/*` per resource, `api/deps.py` for DI, `core/config.py` + `core/security.py` + `core/db.py` for cross-cutting concerns.
- `pydantic-settings` config pattern (`backend/app/core/config.py`): typed `BaseSettings`, `PostgresDsn`/`EmailStr`/`HttpUrl` fields, `field_validator`/`model_validator` (e.g. rejecting default `"changethis"` secrets outside dev) — directly reusable, SQLModel-free.
- Dependency injection pattern (`backend/app/api/deps.py`): `SessionDep`/`TokenDep`/`CurrentUser` as `Annotated[..., Depends(...)]` aliases, OAuth2 password-bearer JWT flow — structure transfers even though it imports `sqlmodel.Session` (swap for our DB layer's session type).
- JWT auth: `core/security.py` (`pwdlib` with Argon2+bcrypt fallback hashing, `create_access_token`) is dependency-layer-agnostic and directly portable.
- Error handling via `HTTPException` at the route/dependency boundary — simple, consistent pattern worth imitating.
- Alembic setup (`backend/app/alembic/env.py`, `versions/`) — migration workflow transfers even though model metadata comes from SQLModel; the alembic.ini + env.py wiring is the reusable part.
- Docker/Compose/Traefik: multi-stage `backend/Dockerfile` (uv-based, bytecode-compiled, cache-mounted), `compose.yml` with Traefik v3 labels for host-based routing + `db`/`adminer` healthchecks — good reference for our Docker-first default, Traefik labels are a bonus example beyond our current stack.
- CI: `.github/workflows/test-backend.yml` (docker compose up db+mailpit, run pytest via `uv run`, enforce `coverage report --fail-under=90`) and companion `test-docker-compose.yml`, `pre-commit.yml`, `zizmor.yml` (workflow security linting) — strong CI reference.
- Tests: `backend/tests/{api/routes,crud,utils}` — route-level tests hit a real `TestClient` against seeded fixtures (`conftest.py`), good shape for our `eng-testing`.
- Frontend (React + Vite + TanStack Query + shadcn/ui + Tailwind v4 + Radix, `frontend/`) is explicitly out of scope per our brief — note only as an integration reference for how the SPA consumes an auto-generated OpenAPI client (`openapi-ts.config.ts`, `scripts/generate-client.sh`).

## Where things live
- `source/backend/app/core/config.py`, `security.py`, `db.py` — settings, JWT/hashing, DB engine (entry points to open first).
- `source/backend/app/api/deps.py`, `api/main.py`, `api/routes/{login,users,items,utils,private}.py` — DI + route registration.
- `source/backend/app/models.py`, `crud.py` — SQLModel models + CRUD (do not copy as-is, see below).
- `source/backend/app/alembic/` — migration env + versions.
- `source/backend/tests/` — pytest suite; `source/backend/Dockerfile`, `source/compose.yml`, `source/compose.override.yml`, `source/compose.deploy.yml`, `source/deployment.md`, `source/deployment-docker-compose.md` — infra.
- `source/.github/workflows/` — 14 workflow files (test, deploy, release automation, dependency guard, Zizmor).
- `source/frontend/` — React/Vite app, out of scope except as reference.

## Known dependencies
- FastAPI, `pydantic` v2 + `pydantic-settings`, `SQLModel` (do not adopt — our standard is Drizzle/TypeScript on the Node side, and for `ai-service` we'd use SQLAlchemy or a plain query layer, not SQLModel), `psycopg` (v3, forced via a `field_validator` that rewrites `postgres://`/`postgresql://` to `postgresql+psycopg://`), `alembic`, `pwdlib` (Argon2+bcrypt), `PyJWT`, `uv` for dependency/venv management, Python 3.14 (`.python-version`), pytest.
- Frontend (out of scope): React, Vite, TypeScript, TanStack Query, shadcn/ui, Radix UI, Tailwind v4, Biome (lint/format), Playwright (e2e), `openapi-ts` codegen, Bun as package manager/runtime.

## Do not copy
- `source/backend/app/models.py`, `crud.py`, `core/db.py`, and every `sqlmodel.Session`/`SQLModel` usage in `api/deps.py` and `api/routes/*` — SQLModel-coupled; reimplement against our ORM-agnostic approach for `ai-service`.
- `source/backend/app/alembic/versions/*` — migration content is schema-specific to the demo `User`/`Item` models.
- `source/frontend/**` — React/Vite SPA, out of scope per brief (reference only for OpenAPI-client integration pattern).
- `source/img/*`, dashboard/login screenshots — demo branding, not licensed for reuse as our own assets even though MIT covers the code.
- `source/hooks/post_gen_project.py`, `.github/workflows/{add-to-project,bump-pre-commit-hooks,create-draft-release,detect-conflicts,guard-dependencies,issue-manager,prepare-release,smokeshow}.yml` — cookiecutter/repo-maintenance automation specific to the upstream project, not to a consumer of the template.

## Notes
- Python 3.14 is required (`requires-python >=3.14`, `FROM python:3.14`). `source/backend/app/api/deps.py:36` relies on it: `except InvalidTokenError, ValidationError:` is valid only on ≥ 3.14 (PEP 758) and a `SyntaxError` on 3.13 and earlier — parenthesize it if the AI-service starter targets an older Python.
- Root `pyproject.toml` is a `uv` workspace manifest (dev tooling only: `prek`, `typer`, `zizmor`, `smokeshow`); the real backend dependencies live in `backend/pyproject.toml`.
- Root-level `.env` file is present in the checkout — it is the project's own local-dev template (placeholder values like `changethis`), not a real secrets leak; `core/config.py` actively rejects `"changethis"` outside `FASTAPI_ENV=development`.
- Repo ships `.claude/skills/`, `.agents/skills/` (a "library-skills" AI-agent skill) and a `CONTRIBUTING.md` — not relevant to extraction.
- The reviewed core/API/test files are clean, typed, and idiomatic — consistent with a 45k-star, actively maintained template.
