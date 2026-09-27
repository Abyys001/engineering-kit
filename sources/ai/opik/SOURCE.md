# Opik

| Field | Value |
|---|---|
| Source URL | https://www.comet.com/docs/opik/ |
| GitHub repository | `comet-ml/opik` (owner comet-ml, org — not a fork) |
| Category | ai |
| License | Apache-2.0 — root `LICENSE` (copyright Comet ML, Inc; full Apache-2.0 text). Identical Apache-2.0 files at `sdks/python/LICENSE`, `sdks/typescript/LICENSE`, `sdks/opik_optimizer/LICENSE`, `extensions/cursor/LICENSE`. No additional-restriction clause: the only "except as"/"notwithstanding" hits are Apache-2.0's own §3 and §6 boilerplate |
| Author / organization | Comet ML, Inc |
| Acquired | not acquired — license and revision verified over the GitHub API on 2026-09-27; no checkout exists |
| Revision | `f898372e12782ca6df80aea00acf04b466b45f52` (committed 2026-09-27) |
| Attribution required | **Yes** — Apache-2.0 §4: keep the license, the copyright notice, and any `NOTICE` file contents on redistribution |
| Status | license-cleared, not acquired — plain Apache-2.0 throughout. Not cloned: it is a full platform (Java backend + React frontend + Helm charts + load/e2e suites), and what we want from it is a design reference, not code |

## Useful for
- LLM observability as a **pattern reference**: trace/span data model, LLM-as-judge evaluation metrics, prompt versioning, CI evaluation gates
- Relevant to every domain's AI features (`ai_relevance: high`/`core`) once the kit gets an AI layer; also the natural comparison point for whatever tracing the `ai-service` starter ends up with

## Where things live
Verified from the pinned revision's git tree (paths only):
- `sdks/python/`, `sdks/typescript/` — client SDKs; the tracing/decorator API and the metric definitions are the part worth reading
- `sdks/opik_optimizer/` — prompt-optimization package
- `apps/opik-backend/` (Java), `apps/opik-frontend/` (React), `apps/opik-python-backend/`, `apps/opik-guardrails-backend/`, `apps/opik-sandbox-executor-python/` — the platform services
- `deployment/docker-compose/`, `deployment/helm_chart/` — self-host manifests, if it is ever run as a service instead of read
- `apps/opik-documentation/` — docs, including the metric definitions in prose
- `tests_end_to_end/`, `tests_load/` — QA harnesses; not product code

## Known dependencies
Not inspected — no checkout. The backend is Java/Maven with its own datastore stack; the Python SDK is the only piece that would sit inside our FastAPI `ai-service`.

## Do not copy
- `extensions/cursor/` and any bundled agent/skill config — upstream agent instructions, never trusted (untrusted-source rule)
- `apps/opik-backend/` — a Java service; off-stack for this kit (NestJS/FastAPI), reference only
- Anything without carrying the Apache-2.0 `NOTICE`/copyright forward

## Notes
- Decision: **run or read, do not extract.** If observability is needed, self-host from `deployment/` or use the hosted service; only the SDK-level tracing patterns are candidates for adaptation.
- `fetch: false` in `sources/MANIFEST.json`. If a checkout becomes necessary, sparse-checkout `sdks/python` only.
