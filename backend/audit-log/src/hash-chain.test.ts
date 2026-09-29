import { test } from 'node:test';
import assert from 'node:assert/strict';
import { appendEvent, canonicalJson, verifyChain, type AuditEventInput, type AuditEventRecord } from './hash-chain.ts';

const ev = (n: number): AuditEventInput => ({
  id: `e${n}`, tenantId: 't1', contractId: 'c1', type: 'signed',
  actor: { kind: 'recipient', id: 'r1' }, occurredAt: new Date(2026, 0, n), metadata: { b: 1, a: 2 },
});
const chain = (n: number) => {
  const out: AuditEventRecord[] = [];
  for (let i = 1; i <= n; i++) out.push(appendEvent(out.at(-1) ?? null, ev(i)));
  return out;
};

test('canonical json is key-order independent', () => {
  assert.equal(canonicalJson({ a: 1, b: { d: 1, c: 2 } }), canonicalJson({ b: { c: 2, d: 1 }, a: 1 }));
});

test('valid chain verifies', () => assert.deepEqual(verifyChain(chain(5)), { ok: true }));

test('edited event, removed event, reordered events are detected', () => {
  const c = chain(5);
  assert.deepEqual(verifyChain(c.map((e, i) => (i === 2 ? { ...e, type: 'declined' } : e))), { ok: false, brokenAtSeq: 3, reason: 'hash_mismatch' });
  assert.equal(verifyChain([c[0]!, c[1]!, c[3]!, c[4]!]).ok, false);
  assert.equal(verifyChain([c[1]!, c[0]!, c[2]!]).ok, false);
});

test('truncating the tail is NOT detectable by the chain alone — anchor the head hash', () => {
  assert.deepEqual(verifyChain(chain(5).slice(0, 3)), { ok: true });
});
