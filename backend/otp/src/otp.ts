import { createHmac, randomInt, randomUUID, timingSafeEqual } from 'node:crypto';

export interface OtpChallenge {
  id: string;
  codeHmac: string;
  expiresAt: Date;
  attempts: number;
  maxAttempts: number;
  consumedAt: Date | null;
  lockedAt: Date | null;
}

export type OtpVerdict =
  | { ok: true }
  | { ok: false; reason: 'expired' | 'consumed' | 'locked' | 'mismatch' };

export interface OtpOptions {
  digits?: number;
  ttlMs?: number;
  maxAttempts?: number;
}

/** HMAC keyed with a server secret and bound to the challenge id: a leaked table cannot be brute-forced offline without the key. */
export function hmacCode(secret: string, challengeId: string, code: string): string {
  return createHmac('sha256', secret).update(`${challengeId}:${code}`).digest('hex');
}

export function createOtpChallenge(secret: string, opts: OtpOptions = {}, now = new Date()) {
  const digits = opts.digits ?? 6;
  const id = randomUUID();
  const code = randomInt(0, 10 ** digits).toString().padStart(digits, '0');
  const challenge: OtpChallenge = {
    id,
    codeHmac: hmacCode(secret, id, code),
    expiresAt: new Date(now.getTime() + (opts.ttlMs ?? 10 * 60_000)),
    attempts: 0,
    maxAttempts: opts.maxAttempts ?? 5,
    consumedAt: null,
    lockedAt: null,
  };
  return { code, challenge };
}

/**
 * Returns the verdict and the challenge state to persist. Persist it with
 * a row lock (SELECT ... FOR UPDATE) so parallel guesses cannot exceed maxAttempts.
 * The lock is on the challenge, never on the account (OWASP: account lockout is a DoS vector).
 */
export function verifyOtp(
  secret: string,
  challenge: OtpChallenge,
  submitted: string,
  now = new Date(),
): { verdict: OtpVerdict; next: OtpChallenge } {
  if (challenge.consumedAt) return { verdict: { ok: false, reason: 'consumed' }, next: challenge };
  if (challenge.lockedAt || challenge.attempts >= challenge.maxAttempts) {
    return { verdict: { ok: false, reason: 'locked' }, next: { ...challenge, lockedAt: challenge.lockedAt ?? now } };
  }
  if (challenge.expiresAt <= now) return { verdict: { ok: false, reason: 'expired' }, next: challenge };

  const expected = Buffer.from(challenge.codeHmac, 'hex');
  const actual = Buffer.from(hmacCode(secret, challenge.id, submitted), 'hex');
  if (expected.length === actual.length && timingSafeEqual(expected, actual)) {
    return { verdict: { ok: true }, next: { ...challenge, consumedAt: now } };
  }
  const attempts = challenge.attempts + 1;
  return {
    verdict: { ok: false, reason: 'mismatch' },
    next: { ...challenge, attempts, lockedAt: attempts >= challenge.maxAttempts ? now : null },
  };
}
