# FastAPI Best Architecture

| Field | Value |
|---|---|
| Source URL | https://github.com/fastapi-practices/fastapi-best-architecture |
| GitHub repository | `fastapi-practices/fastapi-best-architecture` (owner fastapi-practices, Organization repo) |
| Category | backend |
| License | MIT — `LICENSE.txt` (root `LICENSE`); no other license files found in the checkout |
| Author / organization | Wu Clan (xiaowu) |
| Acquired | 2026-09-26 |
| Revision | `123a44aed02daf5ea60d2a7469625c933d3bb759` (main, committed 2026-09-20) |
| Attribution required | License notice only |
| Status | extraction-safe — plain MIT, no conditions beyond keeping the license text |

## Useful for
- FastAPI + SQLAlchemy 2 (async) + Alembic layered architecture reference: api → service → crud → model → schema, per app — `backend/app/admin/`, `backend/app/task/`
- RBAC/menu/data-scope admin system: users, roles, menus, depts, data rules — `backend/app/admin/api/v1/sys/`, `backend/app/admin/model/`
- Auth + captcha + login/opera audit logging — `backend/app/admin/api/v1/auth/`, `backend/app/admin/api/v1/log/`
- Celery task app wired alongside FastAPI (async task submission/monitoring) — `backend/app/task/`
- Plugin system for extending the app without touching core — `backend/plugin/`
- Cross-cutting core setup: settings, path config, app registrar (lifespan/middleware wiring) — `backend/core/registrar.py`, `backend/core/conf.py`

## Where things live
- `source/backend/app/admin/{api,crud,model,schema,service,utils}/` — admin domain (users/roles/menus/depts/logs/monitor), full CRUD stack per entity
- `source/backend/app/task/{api,crud,model,schema,service,tasks}/` — Celery-backed task domain, parallel structure to `admin`
- `source/backend/core/` — `conf.py` (Pydantic Settings), `path_conf.py`, `registrar.py` (FastAPI app factory/lifespan)
- `source/backend/common/` — shared response/exception/pagination helpers (not deep-dived; grep before reuse)
- `source/backend/middleware/`, `source/backend/database/` — HTTP middleware and async SQLAlchemy session/engine setup
- `source/backend/plugin/` — plugin loader, code generator, OAuth2, dict/notice/email/SQL sub-plugins
- `source/backend/alembic/`, `source/backend/alembic.ini` — Alembic migration setup (directly relevant, target stack also uses Alembic)
- `source/deploy/`, `source/docker-compose.yml`, `source/Dockerfile` — deployment reference (Granian/Gunicorn, Docker)

## Known dependencies
- `pyproject.toml`: requires-python >=3.10; fastapi[standard-no-fastapi-cloud-cli]>=0.141.1, sqlalchemy[asyncio]>=2.0.52, alembic>=1.19.1, pydantic>=2.13.4, pydantic-settings>=2.15.0, celery>=5.6.3 + celery-aio-pool, redis[hiredis]>=8.1.0, sqlalchemy-crud-plus>=1.13.3, fastapi-pagination[sqlalchemy]>=0.15.16, psycopg[binary]==3.2.10 / asyncpg / asyncmy (Postgres + MySQL both supported), full OpenTelemetry instrumentation set, loguru, python-jose, pwdlib
- Matches our target backend stack closely: FastAPI + SQLAlchemy 2 (async) + Alembic + PostgreSQL

## Do not copy
- MySQL-specific driver code/config (asyncmy, pymysql) if we standardize on PostgreSQL only — keep the Postgres path (asyncpg/psycopg)
- Celery task queue wiring wholesale if the target project uses BullMQ on the Node side — the RBAC/admin/CRUD architecture is the reusable part, not the task queue choice
- `backend/static/`, `backend/sql/` — check contents before reuse (seed SQL / generated static assets, project-specific)

## Notes
- Very close pattern-match to our target FastAPI + SQLAlchemy 2 + Alembic stack — highest promote value of the four repos reviewed in this batch.
- Bilingual project (README + README.zh-CN.md); some in-code docstrings/comments are Chinese — expect to translate when extracting.
- No "ee"/enterprise split, no bundled fonts/images/3D assets — pure backend codebase.
