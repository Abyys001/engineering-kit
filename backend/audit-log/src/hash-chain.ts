import { createHash } from 'node:crypto';

/**
 * Per-envelope hash chain. Tamper *evidence*, not prevention: prevention is REVOKE UPDATE/DELETE
 * plus a BEFORE UPDATE OR DELETE trigger (see README.md). A global chain would serialize every
 * write in the system, so chains are scoped to one contract.
 */
export interface AuditEventInput {
  id: string;
  tenantId: string;
  contractId: string;
  type: string;
  actor: { kind: 'user' | 'recipient' | 'system' | 'api_key'; id: string | null };
  occurredAt: Date;
  ip?: string | null;
  userAgent?: string | null;
  documentHash?: string | null;
  metadata?: Record<string, unknown>;
}

export interface AuditEventRecord extends AuditEventInput {
  seq: number;
  prevHash: string | null;
  hash: string;
}

export const GENESIS = null;

/** Deterministic JSON: sorted keys, so the same event always hashes the same. */
export function canonicalJson(value: unknown): string {
  if (value === null || typeof value !== 'object') return JSON.stringify(value);
  if (value instanceof Date) return JSON.stringify(value.toISOString());
  if (Array.isArray(value)) return `[${value.map(canonicalJson).join(',')}]`;
  const entries = Object.entries(value as Record<string, unknown>)
    .filter(([, v]) => v !== undefined)
    .sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0));
  return `{${entries.map(([k, v]) => `${JSON.stringify(k)}:${canonicalJson(v)}`).join(',')}}`;
}

export function computeEventHash(prevHash: string | null, seq: number, event: AuditEventInput): string {
  return createHash('sha256').update(`${prevHash ?? ''}|${seq}|${canonicalJson(event)}`).digest('hex');
}

/** Call inside the transaction that holds `SELECT ... FOR UPDATE` on the contract row, so seq/prevHash cannot fork. */
export function appendEvent(last: AuditEventRecord | null, event: AuditEventInput): AuditEventRecord {
  const seq = (last?.seq ?? 0) + 1;
  const prevHash = last?.hash ?? GENESIS;
  return { ...event, seq, prevHash, hash: computeEventHash(prevHash, seq, event) };
}

export type ChainVerdict = { ok: true } | { ok: false; brokenAtSeq: number; reason: 'seq_gap' | 'prev_mismatch' | 'hash_mismatch' };

export function verifyChain(events: AuditEventRecord[]): ChainVerdict {
  let prev: AuditEventRecord | null = null;
  for (const e of events) {
    const { seq, prevHash, hash, ...input } = e;
    if (seq !== (prev?.seq ?? 0) + 1) return { ok: false, brokenAtSeq: seq, reason: 'seq_gap' };
    if (prevHash !== (prev?.hash ?? GENESIS)) return { ok: false, brokenAtSeq: seq, reason: 'prev_mismatch' };
    if (computeEventHash(prevHash, seq, input) !== hash) return { ok: false, brokenAtSeq: seq, reason: 'hash_mismatch' };
    prev = e;
  }
  return { ok: true };
}
