# Proposed data model (conceptual)

Not a migration. Postgres + Drizzle, every row carries `organisation_id` (tenant boundary) unless marked global. UUIDv7 primary keys, `created_at`, `updated_at`. Immutable = no UPDATE/DELETE grant. Soft-delete only where marked; evidence tables are never soft-deleted, only retention-deleted.

| Entity | Belongs to / has | Key columns | Indexes / uniqueness | Lifecycle | Immutable | Soft-delete |
|---|---|---|---|---|---|---|
| Organisation | has users, contracts, templates, endpoints | name, slug, region, retention_policy, branding | unique(slug) | active → suspended → deleted | no | yes |
| User | org; roles | email, name, locale | unique(org, email) | invited → active → disabled | no | yes |
| Role / Permission | org, user | role, resource_type, resource_id, permission | idx(user), unique(user, resource_type, resource_id, permission) | grant/revoke | no | no |
| Contract | org; versions, recipients, events | number, title, status, owner_id, version, expires_at, completed_at, metadata jsonb | unique(org, number); idx(org, status, created_at desc); GIN(metadata); trgm(title) | draft→sent→in_progress→completed/declined/voided/expired→archived | after `completed` | yes until sent; archive after |
| ContractVersion | contract; documents | sequence, content_hash | unique(contract, sequence) | created at send | yes | no |
| Document | version; files, fields | title, page_count, order | idx(version) | with version | after send | no |
| DocumentFile | document; storage_object | kind(original/prepared/sealed/certificate), sha256, size, mime | unique(document, kind, sha256) | uploaded→scanned→ready | yes | no |
| StorageObject | org | bucket, key, etag, encryption, retain_until | unique(bucket, key) | put once | yes | no (retention delete) |
| Template / TemplateVersion | org; fields | name, status; sequence, published_at | unique(org, name); unique(template, sequence) | draft→published→archived | version yes | template yes |
| Recipient | contract; fields, sessions | email, name, role, routing_order, auth_level, status, token_hash, token_expires_at, locale | unique(contract, email, role); unique(token_hash) | pending→sent→opened→signed/declined/bounced | after terminal | no |
| RecipientField (Field) | document, recipient | type, page, x,y,w,h ∈ [0,1], required, config jsonb, value | idx(document, page); idx(recipient) | draft→locked at send→filled | locked after send | no |
| SignatureRequest | recipient | expires_at, sent_at, completed_at | unique(recipient) | with recipient | no | no |
| Signature | recipient, field, session | method, image_ref, signed_at, ip, ua, doc_hash | **unique(field_id)** and unique(recipient, field) | written once | yes | no |
| SigningSession | recipient | assurance_level, started_at, expires_at, ip, ua | idx(recipient, expires_at) | created→verified→signing→finished/expired | ended rows | no |
| OTP (challenge) | recipient | channel, code_hmac, attempts, expires_at, consumed_at | idx(recipient, created_at desc) | issued→consumed/locked/expired | after end | purged after 30d |
| Consent | session | text_version, accepted_at, ip, ua | unique(session, text_version) | once | yes | no |
| AuditEvent | contract | type, actor, ip, ua, doc_hash, prev_hash, hash, correlation_id, occurred_at | idx(contract, seq); unique(contract, seq); idx(org, occurred_at); BRIN(occurred_at) | append only | **yes** | no |
| EmailMessage / EmailEvent | org; recipient | template, provider, provider_message_id, status, idempotency_key; type, provider_event_id | unique(org, idempotency_key); unique(provider, provider_event_id) | queued→sent→delivered/bounced/complained | events yes | no |
| SMSMessage | recipient | provider, status, segments, country | idx(recipient) | like email | events yes | no |
| Reminder | signature_request | slot_key, due_at, sent_at | **unique(signature_request, slot_key)** | scheduled→sent/cancelled | after sent | no |
| Notification | user | type, link, read_at | idx(user, read_at) | unread→read | no | purge |
| Webhook (endpoint) | org | url, events[], secret_current, secret_previous, enabled | idx(org) | active→disabled | no | yes |
| WebhookDelivery | endpoint | event_id, attempts, state, next_attempt_at, last_status | unique(endpoint, event_id); idx(state, next_attempt_at) | pending→retrying→delivered/failed | delivered/failed | purge after N days |
| Download | recipient/user, storage_object | actor, ip, expires_at | idx(storage_object) | logged | yes | no |
| CompletionCertificate | contract, document_file | sha256, layout_version | unique(contract) | generated once | yes | no |
| VerificationRecord | certificate | sha256, public_id | unique(sha256); unique(public_id) (random, non-sequential) | created at seal | yes | no |
| ApiKey | org | prefix, hash, scopes, last_used_at, revoked_at | unique(prefix); unique(hash) | active→revoked | no | no |
| IdempotencyKey | org | key, request_hash, response | unique(org, key) | expire after 24–48h | yes | purge |

## Rules

- **Tenant boundary:** `organisation_id` on every table; repositories accept a tenant-scoped transaction only. RLS policy `organisation_id = current_setting('app.tenant_id')::uuid`, app role is non-owner, no BYPASSRLS. Public token endpoints resolve the tenant from the hashed token, then set context.
- **Ownership:** a contract has one owner user and optional per-object permission overrides.
- **Immutability:** send freezes fields; sealed files, signatures, consents, audit events and certificates are write-once. Corrections create a new ContractVersion.
- **Chain:** `hash = SHA-256(canonical_json(event) || prev_hash)`, `seq` per contract, appended while holding `FOR UPDATE` on the contract row. Global chains are not used.
- **Retention:** deletion runs from policy, respects legal hold, records a deletion event outside the deleted contract's chain. Personal data erasure vs evidence retention needs legal review.
- **Soft delete:** only drafts, templates, users and orgs; never evidence.
