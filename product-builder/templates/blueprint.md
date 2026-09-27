# <Product> — blueprint

> Filled per project into `~/Project/<name>/docs/product/BLUEPRINT.md`. One page. Shown once for approval; then build.

**Request (verbatim):** "<…>"
**Reading:** <product type> · <audience> · <stage> · tenancy: <single|multi>
**Domains:** <primary> (+ <secondary> …) — from `domains/catalog.json`

## Experiences

| Experience | Roles | Surface | Mobile |
|---|---|---|---|
| Customer | … | … | core / valuable / optional / not needed — why |
| Staff | … | … | … |
| Management | … | … | … |
| Administration | … | … | … |

## Feature matrix

Start from `python3 tools/kb.py matrix <domain> --requested <ids>`; edit scope with reasons.

| Feature | Scope | Domain class | Requested | Existing impl | Platforms | RT | AI | Compliance |
|---|---|---|---|---|---|---|---|---|

Scope: IN_SCOPE (asked) · DEPENDENCY (required by in-scope) · PROPOSED (needs your yes) · OPTIONAL · OUT_OF_SCOPE · BLOCKED.

## Architecture

Frontend · Backend modules · Database · Workers · Storage · Notifications · Real-time · AI · Integrations · Deployment · Testing — one line each, standard stack unless a deviation is listed with trade-offs.

## Build order

1. … (from `kb.py order`)

## Assumptions

- …

## Decisions for you

Only items that change scope, cost, platforms, compliance, or tenancy. Each with a recommendation.

1. …
