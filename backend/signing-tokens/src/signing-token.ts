import { createHash, randomBytes, timingSafeEqual } from 'node:crypto';

export interface SigningTokenRecord {
  tokenHash: string;
  expiresAt: Date;
  revokedAt: Date | null;
  usedAt: Date | null;
}

export type TokenCheck =
  | { ok: true }
  | { ok: false; reason: 'malformed' | 'not_found' | 'expired' | 'revoked' | 'used' };

const TOKEN_BYTES = 32;

/** Only the hash is persisted; the raw token exists in the emailed link and nowhere else. */
export function hashToken(token: string): string {
  return createHash('sha256').update(token, 'utf8').digest('hex');
}

export function issueSigningToken(ttlMs: number, now = new Date()) {
  const token = randomBytes(TOKEN_BYTES).toString('base64url');
  const record: SigningTokenRecord = {
    tokenHash: hashToken(token),
    expiresAt: new Date(now.getTime() + ttlMs),
    revokedAt: null,
    usedAt: null,
  };
  return { token, record };
}

/**
 * Pure validity check. Lookup the record by `hashToken(token)` (indexed unique column),
 * then call this. Single-use enforcement must still be a conditional UPDATE
 * (`... WHERE used_at IS NULL`) — this function cannot make consumption atomic.
 */
export function checkSigningToken(
  presented: string,
  record: SigningTokenRecord | null,
  now = new Date(),
): TokenCheck {
  if (!/^[A-Za-z0-9_-]{43}$/.test(presented)) return { ok: false, reason: 'malformed' };
  if (!record) return { ok: false, reason: 'not_found' };
  const a = Buffer.from(hashToken(presented), 'hex');
  const b = Buffer.from(record.tokenHash, 'hex');
  if (a.length !== b.length || !timingSafeEqual(a, b)) return { ok: false, reason: 'not_found' };
  if (record.revokedAt) return { ok: false, reason: 'revoked' };
  if (record.usedAt) return { ok: false, reason: 'used' };
  if (record.expiresAt <= now) return { ok: false, reason: 'expired' };
  return { ok: true };
}

/** Rotation = issue a new token and revoke the old record in the same transaction. */
export function rotateSigningToken(old: SigningTokenRecord, ttlMs: number, now = new Date()) {
  return {
    revoked: { ...old, revokedAt: now },
    ...issueSigningToken(ttlMs, now),
  };
}
