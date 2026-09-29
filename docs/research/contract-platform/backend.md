# Backend findings

Stack: NestJS · Drizzle · PostgreSQL · Redis/BullMQ (existing `backend/jobs`, `backend/audit-log`, `backend/file-storage`, `backend/notifications` — reuse before adding). Sources marked [V] were verified this session; the rest is prior knowledge.

## Modules and patterns

| Concern | Pattern | Kit path |
|---|---|---|
| Contract lifecycle | Explicit state machine (draft → sent → in_progress → completed / declined / voided / expired), transitions validated in one place, terminal states immutable | `backend/contracts` |
| Documents & versions | Immutable versions; sealed version never mutated; SHA-256 stored per file; storage keys tenant-prefixed | `backend/file-storage` + `backend/pdf` |
| Signing links | 32 random bytes, base64url; store SHA-256 only; per-recipient `expires_at`, `revoked_at`, `used_at`; rotate = issue new + revoke old | `backend/signing-tokens` |
| OTP | `randomInt` 6 digits; store HMAC-SHA256(secret, challengeId‖code); `timingSafeEqual`; 5 attempts, 10 min TTL, resend cooldown; Redis rate limit per IP + per link | `backend/otp` |
| Audit trail | Append-only; `REVOKE UPDATE, DELETE, TRUNCATE` from app role + BEFORE UPDATE/DELETE trigger; hash chain **per envelope** (`prev_hash`, `hash` over canonical JSON); serialise appends with `FOR UPDATE` on the envelope row; no global chain (write hotspot) | `backend/audit-log` |
| Webhooks | Standard Webhooks [V]: `webhook-id`, `webhook-timestamp`, `webhook-signature` over `id.timestamp.payload`, HMAC-SHA256, `whsec_` secrets, dual-sign during rotation, ~5 min tolerance (spec sets none), BullMQ exponential backoff + jitter, failed state in `webhook_deliveries` = DLQ | `backend/webhooks` |
| Email/SMS | Small `EmailProvider` / `SmsProvider` interfaces; adapters (SMTP, SES, Postmark, Resend, SendGrid / Twilio, Vonage, SNS); normalise provider events into one table; verify each provider's webhook signature; never mark "delivered" without a provider delivery event | `backend/notifications` (extend) |
| Tenancy | `nestjs-cls` holds tenant; one Drizzle transaction wrapper runs `set_config('app.tenant_id', $1, true)`; RLS policies [V: `pgPolicy`, `.withRLS()`, deny by default]; non-owner, non-BYPASSRLS app role; `tenantId` in every job payload, context rebuilt in worker | `backend/tenancy` |
| Search | `tsvector` + GIN for text, `pg_trgm` GIN for fuzzy name/email/number; external engine only when measured slow | `features/search` |

## Concurrency

| Race | Guard |
|---|---|
| Last signer completes twice | Tx: `SELECT … FOR UPDATE` on envelope → count remaining → complete; exactly one tx sees "last" |
| Duplicate signature | unique `(recipient_id, field_id)` on signature row |
| Duplicate sends/reminders | `Idempotency-Key` table, unique `(tenant_id, key)`; reminder unique `(recipient_id, kind, window)` |
| Final PDF generated twice | Job `jobId = complete:<envelopeId>` (dedupe only); DB state `sealing → sealed` transition is the real guard |
| Draft edits | optimistic `version` column, drafts only |
| Webhook retries | consumer dedupes on `webhook-id`; sender delivery row unique per `(endpoint, event)` |

## PDF server pipeline (server-only; browser libs stay in the browser)

upload → magic-byte sniff (`file-type`) → size/page caps → `qpdf --check` preflight → ClamAV (clamd) job, quarantined until clean → store immutable original + hash → field stamp/flatten (`@cantoo/pdf-lib`) → append certificate PDF (`pdfkit`) → PAdES-B-B seal (`@signpdf/signpdf` + `pkijs`), keys in KMS/HSM → optional RFC 3161 timestamp → hash + store sealed version. Changes after signing must be incremental updates. PDF/A and PAdES-LT/LTA are not covered by any maintained pure-Node tool (Ghostscript is AGPL; veraPDF validates only) — confirm the requirement before committing.

## Performance and operations

- Stream downloads from object storage via short-lived presigned URLs; never buffer whole PDFs in the API process; pdf-lib loads whole files in memory, so cap size and run in a worker.
- Keyset pagination for contracts/audit; partial indexes on `(tenant_id, status)`; partition audit by time only when measured.
- Separate BullMQ queues: `email`, `sms`, `pdf`, `webhook`, `cleanup`; concurrency per queue; retention/reminder jobs are cron-triggered and idempotent.
- S3/R2/MinIO with lifecycle rules; structured logs with correlation IDs (existing `backend/logging`); secrets from a manager, never env files in images; TLS + security headers at the proxy; backups with tested restore for Postgres and object store.
- Job failures: exponential backoff, capped attempts, failed jobs surfaced (not silently dropped).

## Data model sketch

Organisation, User, Role, Permission → Contract (tenant-owned) → ContractVersion (immutable when sealed) → DocumentFile/StorageObject; Recipient → RecipientField; SigningToken, OtpChallenge, Consent, Signature (immutable), AuditEvent (immutable, chained), EmailMessage/EmailEvent, SmsMessage, Reminder, Notification, WebhookEndpoint/WebhookDelivery, IdempotencyKey, Download, CompletionCertificate, VerificationRecord. Every table carries `tenant_id`; soft-delete on drafts/templates only, never on audit, signatures or sealed versions. Details: `domains/e-signature/entities.json`.
