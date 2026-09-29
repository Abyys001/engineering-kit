import { test } from 'node:test';
import assert from 'node:assert/strict';
import { checkSigningToken, hashToken, issueSigningToken, rotateSigningToken } from './signing-token.ts';

test('issued token validates and stores only a hash', () => {
  const { token, record } = issueSigningToken(60_000);
  assert.equal(token.length, 43);
  assert.notEqual(record.tokenHash, token);
  assert.equal(record.tokenHash, hashToken(token));
  assert.deepEqual(checkSigningToken(token, record), { ok: true });
});

test('rejects malformed, unknown, expired, revoked, used', () => {
  const now = new Date('2026-01-01T00:00:00Z');
  const { token, record } = issueSigningToken(1_000, now);
  const later = new Date(now.getTime() + 2_000);
  assert.deepEqual(checkSigningToken('short', record, now), { ok: false, reason: 'malformed' });
  assert.deepEqual(checkSigningToken(token, null, now), { ok: false, reason: 'not_found' });
  const other = issueSigningToken(1_000, now).token;
  assert.deepEqual(checkSigningToken(other, record, now), { ok: false, reason: 'not_found' });
  assert.deepEqual(checkSigningToken(token, record, later), { ok: false, reason: 'expired' });
  assert.deepEqual(checkSigningToken(token, { ...record, revokedAt: now }, now), { ok: false, reason: 'revoked' });
  assert.deepEqual(checkSigningToken(token, { ...record, usedAt: now }, now), { ok: false, reason: 'used' });
});

test('rotation revokes the old token', () => {
  const { token, record } = issueSigningToken(60_000);
  const rotated = rotateSigningToken(record, 60_000);
  assert.deepEqual(checkSigningToken(token, rotated.revoked), { ok: false, reason: 'revoked' });
  assert.deepEqual(checkSigningToken(rotated.token, rotated.record), { ok: true });
});
