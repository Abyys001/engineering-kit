# tenancy

Tenant context via `AsyncLocalStorage` (Node built-in; `nestjs-cls` wraps the same primitive if you want NestJS integration), fail-loud `currentTenant()`, job payload contract, and a transaction wrapper that sets the tenant transaction-locally.

Defense in depth, all three layers: (1) every repository takes tenant from `currentTenant()`, never from a parameter; (2) Postgres RLS with `USING (tenant_id = current_setting('app.tenant_id')::uuid)` (Drizzle: `pgPolicy`, `.withRLS()`; no policy = deny) on a **non-owner, non-BYPASSRLS** role; (3) tenant in cache keys, object-storage prefixes, search filters, webhook endpoints. `set_config(..., true)` must be transaction-local or pooled connections leak the tenant. Verify with a two-tenant test on every table.
