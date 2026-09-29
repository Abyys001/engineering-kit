import { test } from 'node:test';
import assert from 'node:assert/strict';
import { createOtpChallenge, verifyOtp } from './otp.ts';

const SECRET = 'test-secret';

test('correct code verifies once, then is consumed (replay)', () => {
  const { code, challenge } = createOtpChallenge(SECRET);
  const first = verifyOtp(SECRET, challenge, code);
  assert.deepEqual(first.verdict, { ok: true });
  const replay = verifyOtp(SECRET, first.next, code);
  assert.deepEqual(replay.verdict, { ok: false, reason: 'consumed' });
});

test('locks after maxAttempts, even for the right code', () => {
  const { code, challenge } = createOtpChallenge(SECRET, { maxAttempts: 3 });
  const wrong = code === '000000' ? '111111' : '000000';
  let c = challenge;
  for (let i = 0; i < 3; i++) c = verifyOtp(SECRET, c, wrong).next;
  assert.ok(c.lockedAt);
  assert.deepEqual(verifyOtp(SECRET, c, code).verdict, { ok: false, reason: 'locked' });
});

test('expired challenge rejects', () => {
  const now = new Date('2026-01-01T00:00:00Z');
  const { code, challenge } = createOtpChallenge(SECRET, { ttlMs: 1000 }, now);
  const v = verifyOtp(SECRET, challenge, code, new Date(now.getTime() + 2000));
  assert.deepEqual(v.verdict, { ok: false, reason: 'expired' });
});

test('code is bound to challenge id and secret', () => {
  const a = createOtpChallenge(SECRET);
  const b = createOtpChallenge(SECRET);
  assert.notEqual(a.challenge.codeHmac, b.challenge.codeHmac);
  assert.equal(verifyOtp('other-secret', a.challenge, a.code).verdict.ok, false);
});

test('codes are zero-padded to the configured length', () => {
  for (let i = 0; i < 50; i++) assert.match(createOtpChallenge(SECRET, { digits: 8 }).code, /^\d{8}$/);
});
