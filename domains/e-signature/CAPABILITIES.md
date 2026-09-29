# E-signature capability catalog

Hand-written companion to `feature-map.json` (the machine-readable source; ids are `e-signature.<name>`). Tiers: **CORE** = product not usable without it · **IMPORTANT** = expected by most buyers · **OPTIONAL** = per-product · **FUTURE** = interface now, build later. Complexity: S/M/L/XL. "Kit code" lists paths that exist today; everything else is `missing`. Legal notes are technical considerations, not legal advice; nothing here claims compliance.

Reference implementations are AGPL/proprietary and **read-only references** (not cloned): Documenso (DCM), DocuSeal (DSL), OpenSign (OSG), LibreSign (LBS). Standards: Standard Webhooks (SW), OWASP (OW).

## CORE

| Capability | Problem | Backend | Frontend / mobile | Data | Security | Deps | APIs · jobs · events | Kit code · refs | Cx | Future |
|---|---|---|---|---|---|---|---|---|---|---|
| Contract management | Group documents, recipients, fields | Aggregate, numbering, ownership, duplication, archive, lock, optimistic version for drafts | List/detail, status, owner filter | contract, contract_version | Object-level authz, tenant scope | multi_tenancy, state machine | `POST/GET /contracts` · none · `contract.created` | `components/web/contract` · DCM DSL OSG | L | CLM metadata, renewals |
| Contract state machine | Prevent illegal transitions | Transition table + compare-and-set update, event per transition | Status badge, timeline | contract.status | Only server transitions | audit_trail | `POST /contracts/:id/{send,void}` · expire job · `contract.*` | `backend/contracts` · DCM | M | Custom states per tenant |
| Document management | Store and version PDFs | StorageObject + DocumentFile, hash, metadata | Upload with progress | document, document_file | Type/size caps, tenant prefix | storage_abstraction | `POST /documents` · processing · `document.uploaded` | — · DCM DSL | M | Page-level ops |
| Upload security | Block malicious files | Magic bytes, size/pages caps, ClamAV, PDF preflight, quarantine | Clear error states | quarantine flag | No JS/OpenAction/Launch/EmbeddedFiles; sandboxed worker | processing pipeline | — · scan job · `document.rejected` | — · OW | M | Content disarm |
| Processing pipeline | Heavy work off request path | BullMQ stages, idempotent, DB is truth | Progress state | job state on document_file | Worker limits (time/mem) | shared.jobs | — · preflight, thumbnails, seal · `document.ready` | — · nestjs-starter (BullMQ) | L | Autoscaling workers |
| PDF viewer | Read and place on pages | Serve pages/thumbnails | pdfjs-dist + react-pdf, zoom, rotate, thumbnails; mobile pdfrx | — | pdfjs `isEvalSupported:false` | document_management | — | — · pdfjs, react-pdf | M | Annotation layer (EmbedPDF ref) |
| Document preparation | Sender sets up the signing | Autosave draft | Thumbnail rail, palette, properties panel, preview as recipient | field, recipient | Version check on save | pdf_viewer, field_placement | `PUT /contracts/:id/fields` | — · DCM DSL | L | Multi-doc contracts |
| Field placement | Position fields robustly | Relative→PDF point conversion | dnd-kit palette drop, pointer move/resize, snap, duplicate | field x,y,w,h ∈ [0,1] | Server validates bounds | field_types | — | `backend/pdf`, `components/web/signing` · pdfme | L | Rotated pages edge cases |
| Field types | Typed inputs | Zod schema per type, validation rules | 16 renderers | field.type, config JSON | Server-side validation only trusted | — | — | `backend/pdf` (geometry only) · DCM DSL DocuSign SDK | M | Conditional/calculated |
| Recipient management | Who acts and how | Roles, routing, status from events | Recipient cards, colour code, resend | recipient | Unique (contract, email) | contracts | `POST /contracts/:id/recipients` · reminders · `recipient.*` | — · DCM DSL OSG | M | Groups |
| Signing order | Sequential/parallel routing | Routing groups; advance in signing tx | Order editor | recipient.routing_order | Only current group can sign | recipient_management | — · notify next · `recipient.turn` | — · DCM OSG | M | Conditional routing |
| Signature capture | Adopt a signature | Store image + method | signature_pad draw, type, upload; touch-optimised | signature | Size/type check on upload | signing_session | `POST /sessions/:id/signatures` | `components/web/signing` · signature_pad | M | Saved signatures for users |
| Consent | Record willingness to sign electronically | Versioned text, record IP/UA/time | Consent step before fields | consent | Immutable | signing_session | `POST /sessions/:id/consent` · · `consent.accepted` | — · ESIGN/eIDAS (unfetched) | S | Per-jurisdiction texts |
| Signing session | Bind a signer to a version | Session after token exchange + verification; next-field | Progress, next required, finish | signing_session | Single active; device signals | secure_tokens | `POST /sign/exchange` · expiry · `session.*` | — · DCM DSL | M | Resume across devices |
| Secure tokens | Safe links | 32-byte CSPRNG, SHA-256 stored, expiry, revoke, rotate | — | token_hash on recipient | Constant-time compare, single purpose | — | — · · `token.revoked` | `backend/signing-tokens` · OW | S | Signed JWT alternative rejected |
| Email delivery | Reliable provider-neutral sending | EmailProvider interface, idempotency, retries, event normalisation | Delivery timeline | email_message, email_event | Verify provider webhook signatures | shared.jobs | `POST /provider-events/email` · send/retry · `email.*` | — · nestjs-starter | L | Provider fail-over |
| Email notifications | Tell people what to do | Template render, variables, branding | Preview, template editor | email_message | Escape variables, no tokens in logs | email_delivery | — · send · `email.sent` | — · DCM DSL | M | react-email templates |
| Document hashing | Detect tampering | SHA-256 streamed on upload/send/seal; verify on download | Show hash on certificate | document_file.sha256 | Hash pinned in audit | — | — | — · | S | Merkle anchoring not needed |
| Final PDF generation | Produce signed artifact | Flatten, stamp, merge certificate (`@cantoo/pdf-lib`), single-flight | Preview | document_file(kind=sealed) | One job per contract | concurrency, hashing | — · seal · `contract.completed` | `backend/pdf` (coords) · pdf-lib fork | L | PDF/A via sidecar |
| Immutable signed documents | Evidence must not change | Write-once storage, no overwrite | — | retain_until | Object lock / no delete role | storage_abstraction | — | — · | M | Legal hold |
| Completion certificate | Evidence report | pdfkit layout: signers, auth level, IP, UA, times, events, hashes | Download, view | completion_certificate | Generated server-side from audit data only | audit_trail | — · seal · | — · pdfkit | M | Localised certificate |
| Audit trail | Who did what, when | Append-only, REVOKE + trigger, per-contract hash chain | Timeline, export | audit_event | Serialise appends per contract | multi_tenancy | `GET /contracts/:id/events` | `backend/audit-log` · DCM DSL OSG LBS | M | External anchoring |
| Download security | Only the right person gets files | Pre-signed URL / proxy after authz, audit | Download panel | download | nosniff, attachment, short TTL | storage | `GET /files/:id/download` | — · OW | S | Watermarking |
| Storage abstraction (S3) | Provider independence | StorageProvider over S3/R2/MinIO, tenant keys, SSE | — | storage_object | Encryption, no public buckets | — | — | — · shared.file_storage | M | Multi-region |
| Multi-tenancy | No cross-tenant leakage | ALS context, tx wrapper with `set_config`, RLS, tenant in jobs/cache/storage | Org switcher | organisation_id everywhere | Non-owner DB role | shared.organizations | — | `backend/tenancy` · Drizzle RLS docs, boxyhq | L | Per-tenant DB |
| Concurrency and idempotency | Races at last signer | `FOR UPDATE`, unique signature, idempotency table | — | idempotency_key | DB is truth | multi_tenancy | `Idempotency-Key` header | — · | M | Saga for external calls |
| Rate limiting and anti-abuse | Stop enumeration/abuse | Redis windows per IP/token/tenant | Friendly errors | — | OTP and public endpoints | — | 429 + Retry-After | — · chatwoot | M | Bot scoring |

## IMPORTANT

| Capability | Problem | Notes (backend · frontend · data · security · deps) | APIs · jobs · events | Kit code · refs | Cx | Future |
|---|---|---|---|---|---|---|
| Initials | Per-page initials | Reuse signature capture; per-page fields | as signature | — · DCM | S | — |
| OTP | Verify recipient | randomInt + HMAC, TTL 10m, 5 attempts, cooldown, per-IP/link limits; input-otp UI; otp_challenge; lock challenge not account | `POST /sign/otp/{issue,verify}` · · `otp.*` | `backend/otp` · OW | M | WebAuthn |
| Identity verification levels | Assurance ladder | Level on recipient, recorded in evidence; ties to shared.identity_verification | | — · | M | KYC |
| SMS notifications | Text OTP/invites | SmsProvider (Twilio, Vonage, MessageBird, SNS); receipts normalised; country controls | `POST /provider-events/sms` | — · | M | RCS/WhatsApp |
| Notification centre | Sender inbox | shared.notifications + read state | | — | S | Push |
| Reminders and expiry | Nudge, expire | Scheduler with unique slot keys; stop on complete | reminder job | — | M | Smart cadence |
| Versioning | Immutable history | ContractVersion + DocumentFile; corrected copy | | — | M | Diff view |
| Public verification | Check authenticity | Hash lookup, QR, no enumeration | `POST /verify` | — · LBS | M | Signature validation of PAdES |
| Webhooks | Integrate | Standard Webhooks signing, dual secrets, SSRF guard | `/webhook-endpoints` | `backend/webhooks` · SW | M | Event replay UI |
| Webhook retry | Reliable delivery | BullMQ backoff+jitter, failed=DLQ, redrive, 5-min tolerance | | `backend/webhooks` | M | Per-endpoint circuit breaker |
| Search and filtering | Find contracts | tsvector+GIN, pg_trgm, tenant scoped | `GET /contracts?q=` | — · kiranism (tables) | M | External engine if measured |
| Exports | Reporting | Async CSV/PDF export | export job | — | S | Scheduled reports |
| Templates | Reuse | Roles, fields, variables, versions, publish/archive | `/templates` | — · DCM DSL OSG | L | Marketplace |
| Organisation branding | White label | Logo, colours, sender | | — | S | Custom domains |
| RBAC and overrides | Least privilege | Roles + object overrides | | — · boxyhq refine | M | ABAC |
| Security events | Detect abuse | Dedicated stream, alerts | | — | S | SIEM export |
| Admin security | Org policy | Verification level policy, IP allow-list, session lifetime | | — | M | SCIM |
| Observability | Operate it | Structured logs, OTel, queue metrics | | — · nestjs-starter | M | SLOs |
| i18n and RTL | English + Persian | next-intl, logical CSS, Vazirmatn, Intl calendars | | `components/web/typography` (fonts) | M | More locales |
| GDPR retention | Retain/erase | Policy, scheduled deletion, export | retention job | — | L | Automated DSAR |
| Billing readiness | Meter usage | Usage events, entitlements | | — | M | Stripe |
| Decline/void/correct | Terminal paths | Reason, revoke tokens, notify | `POST /contracts/:id/void` | `backend/contracts` (transitions) · DCM OSG | M | — |
| Mobile signing | Sign on phone | Responsive web + Flutter | | — | L | Offline-safe drafts |
| API documentation | Integrate | OpenAPI, scoped keys, idempotency, sandbox | | — · nestjs-starter | M | SDKs |
| Testing strategy | Trust it | Race/tenant/replay/PDF fixtures | | — | M | Load tests |
| Backup and recovery | Survive loss | PITR + object versioning + hash re-verify | | — | M | Cross-region |

## OPTIONAL

| Capability | Notes | Cx |
|---|---|---|
| Delegation and reassign | Revoke old token, verify new identity, custody record | M |
| Witness and in-person signing | Witness role; host-authenticated device hand-over | M |
| Bulk send | CSV → template → throttled queue → report | M |
| Public signing links | Bot protection, quotas, QR | M |
| Conditional and calculated fields | Safe expression evaluator, never `eval` | L |
| Attachment requests | Signer uploads with same upload security | S |
| Embedded signing | Session URL, postMessage, CSP frame-ancestors | M |
| SSO and SCIM | SAML/OIDC + SCIM via existing shared.auth | L |
| Approval workflow | Internal approver as routing step | M |
| Comments | Internal-only threads | M |
| Contract repository and renewals | Metadata, renewal reminders, folders | M |
| Legal hold | Freeze retention | S |

## FUTURE

| Capability | Notes | Cx |
|---|---|---|
| Advanced and qualified signatures | `SignatureProvider` interface, KMS/HSM, TSP, PAdES-B-B (signpdf), timestamps (pkijs); B-LT/LTA custom; legal level decided with counsel | XL |
| KYC document verification | Provider adapter; store evidence reference only | L |
| AI contract intelligence | Summaries, clauses, risk, OCR, comparison, anomaly, via `ai/` | XL |
| Data residency | Region per tenant across DB, storage, jobs | XL |

## Missing capabilities found by comparing with real platforms

Added beyond the requested inventory: decline/void/correct, delegation and reassign, witness and in-person signing, bulk send, public signing links, conditional/calculated fields, attachment requests, embedded signing, SSO/SCIM, approval workflow, comments, contract repository/renewals, legal hold, data residency, KYC, upload security, processing pipeline, API keys and sandbox, email delivery abstraction. Still not covered: payment collection in documents, notarisation/remote online notarisation, accessibility conformance of signed PDFs (tagged PDF), document translation, CRM/cloud-drive connectors, mobile push, DocuSign/Adobe import tooling. Vendor feature comparison was recalled, not fetched.
