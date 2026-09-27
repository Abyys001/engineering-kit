# NestJS Starter

| Field | Value |
|---|---|
| Source URL | https://github.com/hmake98/nestjs-starter |
| GitHub repository | `hmake98/nestjs-starter` (user account) |
| Category | backend |
| License | MIT — `LICENSE.txt` (verbatim copy of root `LICENSE`; no other license files present) |
| Author / organization | Harsh Makwana (`hmake98`) |
| Acquired | 2026-09-26 |
| Revision | `b5f05bd036260f6970b6f031e0c0fe0276b69a84` (master, committed 2026-05-14) |
| Attribution required | License notice only |
| Status | extraction-safe — MIT, `package.json` `license: "MIT"` matches root LICENSE, no nested LICENSE/NOTICE, no conditions beyond notice retention |

## Useful for
- Module layout: `common/` (cross-cutting) vs `modules/` (feature) vs `app/` (bootstrap) — clean, ORM-agnostic split we can mirror directly for `starters/backend-api`.
- Structured logging + request correlation IDs: `nestjs-pino` config with redaction list, correlation/trace-id propagation (`genReqId`, `customProps`) — fully ORM-agnostic, high value.
- Global exception filter + success/error envelope (interceptor + filter pair) — ORM-agnostic, matches our "Error Handling" priority need.
- JWT auth guards + RBAC: `JwtAccessGuard`/`JwtRefreshGuard` (public-route bypass via reflector) and `RolesGuard` (`@Roles`) — ORM-agnostic except the `UserRole` enum import from the Prisma-backed database layer (trivial to relocate).
- Swagger decorator kit (`ApiEndpoint` composing `DocResponse`/`DocPaginatedResponse`) — ORM-agnostic, reduces controller boilerplate.
- Redis cache service (typed wrapper over ioredis, JSON auto-(de)serialize) and BullMQ module wiring (shared Redis connection) — both ORM-agnostic; only one placeholder cron job exists (`midnight.scheduler.ts`), no real processor example.
- Rate limiting (`@nestjs/throttler` as a global guard), health checks (`@nestjs/terminus`), i18n (`nestjs-i18n`, JSON message catalogs under `languages/`) — all ORM-agnostic.
- Dockerfile (4-stage: dev/deps/build/prod, non-root user) and `docker-compose.yml` (Postgres + Redis + app, healthchecks) — solid reference for our Docker-first default.
- Test suite: one spec per guard/filter/interceptor/service under `test/`, `100%` coverage claimed in README — good shape to imitate for `eng-testing`.

## Where things live
- `source/src/common/` — cross-cutting concerns: `logger/`, `cache/`, `bullmq/`, `response/` (filters+interceptors+dtos), `request/` (guards+decorators), `doc/` (Swagger decorators), `config/`, `database/` (Prisma-coupled).
- `source/src/modules/auth/` and `source/src/modules/user/` — feature module reference (controller/service/dto split).
- `source/src/app/` — `app.module.ts` bootstrap, `health.controller.ts`, env enum.
- `source/src/languages/en/` — i18n message catalogs (`auth.json`, `user.json`, `http.json`).
- `source/src/workers/` — BullMQ/`@nestjs/schedule` wiring; `midnight.scheduler.ts` is a stub, not a real job.
- `source/Dockerfile`, `source/docker-compose.yml`, `source/.github/workflows/test.yml` — infra/CI entry points.
- `source/prisma/schema.prisma` — the Prisma schema to skip/replace (see Do not copy).

## Known dependencies
- NestJS 11, TypeScript 6.0.3, Node ≥20.
- Prisma 7 (`@prisma/client`, `@prisma/adapter-pg`) + `pg` — our standard is Drizzle, see Do not copy.
- `ioredis` (Redis), `bullmq` + `@nestjs/bullmq`, `nestjs-pino`/`pino`, `nestjs-i18n`, `@nestjs/swagger`, `@nestjs/terminus`, `@nestjs/throttler`, `passport`/`passport-jwt`, `argon2`, `class-validator`/`class-transformer`, `@sentry/node`, `helmet`, `compression`.
- Env config: `registerAs` factories read `process.env` with defaults and `configService.getOrThrow(...)` at use-site — there is **no** upfront Joi/zod schema validation on boot; a missing required var only fails the first time it's read, not at startup.

## Do not copy
- `source/prisma/**` (schema, migrations, `prisma.config.ts`) and `source/src/common/database/**` (`DatabaseService`, `UserRepository`, `user.interface.ts`) — all Prisma Client calls (`this.db.user.findUnique(...)`, etc.); reimplement against Drizzle.
- `source/src/scripts/seeds/user.seed.ts`, `source/src/cli.ts` (`nestjs-command`) — Prisma-backed seeding.
- Any `PrismaClient`/`@prisma/adapter-pg` references inside `common/config`, `common/cache/constants`, and module DTOs that type against Prisma-generated types.

## Notes
- Honest quality read: this is a genuinely well-built, idiomatic NestJS starter — small, single-responsibility files, consistent naming (`*.module.ts`/`*.service.ts`/`*.guard.ts`), JSDoc on non-obvious methods only, no dead code or TODOs seen in the files reviewed. 63 stars is low for the quality on display.
- The BullMQ/scheduler layer is thin: `BullMqModule` only registers the Redis connection, and the sole worker (`MidNightScheduleWorker`) is a placeholder cron logging a message — there is no real BullMQ processor/consumer example to extract, despite BullMQ being wired.
- Config validation is defaults-plus-`getOrThrow`, not schema-based — weaker than a Joi/zod approach; worth tightening when adapting.
- Repo ships `.claude/`, `.github/copilot-instructions.md`, `.github/instructions/`, `.github/prompts/` (AI-agent tooling files) — not relevant to extraction, ignore.
- Checkout is a shallow single-commit clone (`grafted`); size is small (no `node_modules`, no media).
