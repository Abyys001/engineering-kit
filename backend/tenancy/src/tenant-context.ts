import { AsyncLocalStorage } from 'node:async_hooks';

export interface TenantContext {
  tenantId: string;
  actorId?: string;
}

const storage = new AsyncLocalStorage<TenantContext>();

export const runWithTenant = <T>(ctx: TenantContext, fn: () => T): T => storage.run(ctx, fn);

/** Throws instead of returning undefined: code that forgot to establish a tenant must fail loudly, not query unscoped. */
export function currentTenant(): TenantContext {
  const ctx = storage.getStore();
  if (!ctx) throw new Error('no tenant context: wrap the request/job in runWithTenant()');
  return ctx;
}

/** Job payloads carry tenantId explicitly; the worker re-establishes context from it, never from ambient state. */
export interface TenantJob<T> {
  tenantId: string;
  actorId?: string;
  data: T;
}

export const withTenantJob = <T, R>(job: TenantJob<T>, fn: (data: T) => R): R =>
  runWithTenant({ tenantId: job.tenantId, actorId: job.actorId }, () => fn(job.data));

/**
 * Minimal structural type so this file has no ORM dependency. Drizzle's transaction object satisfies it via
 * `tx.execute(sql\`select set_config('app.tenant_id', ${id}, true)\`)`.
 * `true` = transaction-local, so a pooled connection never leaks the tenant into the next request.
 */
export interface TenantTx {
  setTenant(tenantId: string): Promise<void>;
}

export async function inTenantTransaction<Tx extends TenantTx, R>(
  begin: <T>(fn: (tx: Tx) => Promise<T>) => Promise<T>,
  fn: (tx: Tx) => Promise<R>,
): Promise<R> {
  const { tenantId } = currentTenant();
  return begin(async (tx) => {
    await tx.setTenant(tenantId);
    return fn(tx);
  });
}
