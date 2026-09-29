import { test } from 'node:test';
import assert from 'node:assert/strict';
import { currentTenant, inTenantTransaction, runWithTenant, withTenantJob, type TenantTx } from './tenant-context.ts';

test('throws outside a tenant scope', () => assert.throws(() => currentTenant(), /no tenant context/));

test('context is isolated across concurrent async work', async () => {
  const read = async (id: string) => runWithTenant({ tenantId: id }, async () => {
    await new Promise((r) => setTimeout(r, Math.random() * 10));
    return currentTenant().tenantId;
  });
  const results = await Promise.all(Array.from({ length: 50 }, (_, i) => read(`t${i}`)));
  results.forEach((r, i) => assert.equal(r, `t${i}`));
});

test('job re-establishes tenant from payload', () => {
  const id = withTenantJob({ tenantId: 'tenant-9', data: 1 }, () => currentTenant().tenantId);
  assert.equal(id, 'tenant-9');
});

test('transaction sets tenant before any work', async () => {
  const calls: string[] = [];
  const tx: TenantTx = { setTenant: async (t) => { calls.push(`set:${t}`); } };
  await runWithTenant({ tenantId: 'a' }, () =>
    inTenantTransaction(async (fn) => fn(tx), async () => { calls.push('work'); }));
  assert.deepEqual(calls, ['set:a', 'work']);
});
