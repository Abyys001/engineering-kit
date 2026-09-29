import { test } from 'node:test';
import assert from 'node:assert/strict';
import { backoffWithJitter, signWebhook, verifyWebhook, WebhookVerificationError } from './standard-webhooks.ts';
import { assertPublicHttpsUrl, isBlockedAddress } from './ssrf-guard.ts';

const S1 = 'whsec_' + Buffer.from('secret-one-secret-one-secret-one!').toString('base64');
const S2 = 'whsec_' + Buffer.from('secret-two-secret-two-secret-two!').toString('base64');
const body = JSON.stringify({ type: 'contract.completed', id: 'evt_1' });

test('sign/verify round trip', () => {
  const now = new Date();
  const h = signWebhook([S1], 'msg_1', body, now);
  verifyWebhook([S1], h, body, now);
});

test('tampered body, wrong secret, stale timestamp all fail', () => {
  const now = new Date();
  const h = signWebhook([S1], 'msg_1', body, now);
  assert.throws(() => verifyWebhook([S1], h, body + ' ', now), WebhookVerificationError);
  assert.throws(() => verifyWebhook([S2], h, body, now), WebhookVerificationError);
  assert.throws(() => verifyWebhook([S1], h, body, new Date(now.getTime() + 10 * 60_000)), /tolerance/);
});

test('secret rotation: dual-signed header verifies with either secret', () => {
  const now = new Date();
  const h = signWebhook([S1, S2], 'msg_2', body, now);
  verifyWebhook([S1], h, body, now);
  verifyWebhook([S2], h, body, now);
});

test('replay of a valid message is the consumer job: same id is detectable', () => {
  const h = signWebhook([S1], 'msg_3', body);
  const seen = new Set<string>();
  const accept = () => { verifyWebhook([S1], h, body); if (seen.has(h['webhook-id'])) return false; seen.add(h['webhook-id']); return true; };
  assert.equal(accept(), true);
  assert.equal(accept(), false);
});

test('backoff grows and is capped', () => {
  const max = (a: number) => backoffWithJitter(a, 1000, 60_000, () => 0.999999);
  assert.ok(max(2) > max(1));
  assert.ok(max(30) <= 60_000);
  assert.equal(backoffWithJitter(3, 1000, 60_000, () => 0), 0);
});

test('ssrf: private ranges blocked, public allowed', async () => {
  for (const ip of ['127.0.0.1', '10.1.2.3', '192.168.0.1', '172.16.5.5', '169.254.169.254', '::1', 'fd00::1', '::ffff:10.0.0.1', '0.0.0.0']) {
    assert.equal(isBlockedAddress(ip), true, ip);
  }
  for (const ip of ['8.8.8.8', '1.1.1.1', '172.32.0.1']) assert.equal(isBlockedAddress(ip), false, ip);
  await assert.rejects(assertPublicHttpsUrl('http://example.com/hook'), /https/);
  await assert.rejects(assertPublicHttpsUrl('https://user:pw@example.com/'), /credentials/);
  await assert.rejects(assertPublicHttpsUrl('https://localhost/hook'), /non-public/);
});
