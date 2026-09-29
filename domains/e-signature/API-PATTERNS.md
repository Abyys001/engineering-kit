# REST API patterns

Conventions for a NestJS API over the model in `DATA-MODEL.md`. Follow the kit's existing envelope/error conventions from `sources/backend/nestjs-starter` when promoting. Not an implemented API.

- **Base:** `/v1`, JSON, `application/json`. Version in the path; additive changes only inside a version; deprecations announced via `Deprecation`/`Sunset` headers.
- **Auth:** internal users use httpOnly-cookie sessions with CSRF protection; API integrators use `Authorization: Bearer <api key>` with scopes; **signers never use either**: they exchange a single-purpose token at `POST /v1/sign/exchange` for a short-lived session cookie/bearer bound to one recipient and one contract version.
- **Authorisation:** tenant context first, then object-level check on every read and mutation (`contract.organisation_id`, role, override). Return 404 (not 403) for cross-tenant ids. Recipient endpoints check `session.recipient_id`.
- **Idempotency:** `Idempotency-Key` required on `POST` that send, void, remind, create. Same key + same body returns the stored response; same key + different body returns 422; stored per tenant for 24–48h.
- **Pagination:** cursor (`?limit=50&cursor=…`), stable sort `(created_at desc, id desc)`; response `{data, next_cursor}`. No offset on large tables.
- **Filtering / sorting:** `?status=sent,in_progress&owner=me&created_from=…&q=…&sort=-created_at`; whitelisted columns only; search uses tsvector/trigram behind `q`.
- **Errors:** `{ "error": { "code": "contract_not_editable", "message": "…", "details": [], "request_id": "…" } }`; 400 validation, 401, 403, 404, 409 state conflict, 422 semantic, 429 with `Retry-After`. Zod validation at the boundary; never echo tokens.
- **Concurrency:** state-changing routes return 409 with the current state when a transition is illegal; drafts use `If-Match: <version>` (optimistic).
- **Long work:** return 202 with a `Location` of a job/status resource for exports and bulk send.

| Resource | Endpoints |
|---|---|
| Contracts | `POST /contracts`, `GET /contracts`, `GET /contracts/:id`, `PATCH /contracts/:id` (draft), `POST /contracts/:id/send`, `/void`, `/duplicate`, `/archive`, `/remind` |
| Documents | `POST /contracts/:id/documents` (multipart or pre-signed upload), `GET …/documents/:docId/pages/:n` |
| Recipients | `POST/PATCH/DELETE /contracts/:id/recipients[/:rid]`, `POST …/:rid/resend` |
| Fields | `PUT /contracts/:id/fields` (replace set, versioned) |
| Templates | `GET/POST /templates`, `POST /templates/:id/publish`, `/archive`, `POST /contracts/from-template/:id` |
| Signing (signer) | `POST /sign/exchange`, `POST /sign/otp/issue`, `/verify`, `POST /sessions/:id/consent`, `GET /sessions/:id/document`, `POST /sessions/:id/fields/:fid`, `POST /sessions/:id/finish`, `POST /sessions/:id/decline` |
| Audit | `GET /contracts/:id/events` (cursor), `GET /audit-events?…&format=csv` (async export) |
| Downloads | `GET /contracts/:id/files/:kind` → 302 to short-lived signed URL or streamed body; every call writes a `download` row |
| Verification | `POST /verify` (hash) and `GET /verify/:publicId`, rate-limited, no enumeration, no content returned |
| Webhooks | `GET/POST/PATCH/DELETE /webhook-endpoints`, `POST …/:id/rotate-secret`, `GET …/:id/deliveries`, `POST …/deliveries/:did/redrive` |
| Provider events | `POST /provider-events/{email,sms}`: signature-verified, idempotent on provider event id |

## Webhook events

`contract.created|sent|completed|declined|voided|expired`, `recipient.sent|opened|signed|declined|bounced`, `document.ready|rejected`, `otp.locked`, `webhook.test`. Payload `{id, type, created_at, data}`; headers `webhook-id`, `webhook-timestamp`, `webhook-signature` (Standard Webhooks). Receivers must dedupe on `webhook-id` and reject timestamps older than ~5 minutes (the spec sets no tolerance; this is our choice).
