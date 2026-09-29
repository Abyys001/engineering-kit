# Digital contracts and e-signature

Preparing documents, routing them to signers, capturing signatures with evidence, sealing the final PDF, and keeping a verifiable audit trail, plus a light contract-lifecycle layer around it (templates, reminders, expiry, repository, renewals). NACE Rev. 2.1: J62.10 (computer programming) and M69.10 (legal activities) are the nearest codes; there is no e-signature-specific code.

## Maturity: partial

Legal and compliance content here is **technical considerations, not legal advice**. No statute or standard was fetched this session; every legal item is `low` confidence and `requires_human_review`. Vendor certificate layouts and email/SMS provider event schemas were not verified. Extends `shared.e_signature` and `shared.identity_verification`, which have no implementation to start from.

## Product types

- Sender-driven e-signature (DocuSign, Dropbox Sign, Documenso-style): upload, place fields, route to recipients, seal.
- Template and forms signing (DocuSeal-style): public links, waivers, bulk send from CSV.
- Contract lifecycle management (CLM-lite): repository, metadata, renewals, approvals, search.
- Embedded signing inside another product via API, webhooks and an embed URL.

## Users

Sender, signer, CC recipient, witness, approver, organisation administrator, template manager, compliance officer, public verifier, API integrator, and the system (workers). See `roles.json`.

## Core workflows

1. **Contract lifecycle** — draft → sent → in_progress → completed | declined | voided | expired → archived.
2. **Document preparation** — upload, preflight, render, place fields, bind recipients, preview, send.
3. **Signing flow** — token exchange, verification, consent, adopt signature, next-required-field, finish.
4. **Completion and sealing** — claim under row lock, flatten and stamp, certificate, hash, store write-once, notify, webhook.
5. **OTP, token and webhook lifecycles**, **reminders and expiry**, **decline/void/reassign**, **template publishing**, **bulk send**, **public verification**, **retention and deletion**.

## Capabilities by classification

- **Core (27)**: contracts, state machine, document management, upload security, processing pipeline, PDF viewer, preparation, field placement and types, recipients, signing order, signature capture, consent, signing session, secure tokens, email delivery and notifications, hashing, final PDF, immutable documents, completion certificate, audit trail, download security, storage abstraction, multi-tenancy, concurrency/idempotency, rate limiting.
- **Common (IMPORTANT)**: OTP, identity levels, SMS, notification centre, reminders and expiry, versioning, public verification, webhooks and retry, search, exports, templates, branding, RBAC overrides, security events, admin security, observability, i18n/RTL, billing readiness, decline/void, mobile signing, GDPR retention.
- **Optional**: delegation, witness/in-person, bulk send, public links, conditional/calculated fields, attachment requests, embedded signing, SSO/SCIM, approvals, comments, repository and renewals, legal hold.
- **Future (premium)**: advanced/qualified signatures, KYC document verification, AI contract intelligence, data residency.

Per-capability detail is in [`CAPABILITIES.md`](CAPABILITIES.md). Proposed data model: [`DATA-MODEL.md`](DATA-MODEL.md). REST patterns: [`API-PATTERNS.md`](API-PATTERNS.md).

## Design decisions recorded from research

- **Coordinates:** store `{page, x, y, w, h}` as 0–1 fractions of the CropBox in the unrotated orientation, origin top-left; convert to PDF points on the server (bottom-left origin, /Rotate, CropBox offset). Never store CSS pixels; never flip for RTL.
- **PDF libraries:** browser rendering with pdfjs-dist through react-pdf; server stamping with the maintained `@cantoo/pdf-lib` fork; certificate with pdfkit; PAdES-B-B with `@signpdf/signpdf` and `pkijs` for timestamps when needed. mupdf (AGPL) and node-forge (GPL dual, CVEs) are rejected. Keep browser-only and server-only code separate.
- **Tokens and OTP:** 32-byte CSPRNG tokens, store SHA-256 only. OTP via `crypto.randomInt` plus HMAC with a server secret; lock the challenge, never the account. `otplib` is for TOTP and is not needed.
- **Audit trail:** append-only table, hash chain per contract only (a global chain is a write hotspot), verified by recomputation.
- **Webhooks:** implement the Standard Webhooks format directly with `node:crypto`; self-hosting Svix is rejected as an extra service.
- **Concurrency:** the database is the arbiter: `SELECT … FOR UPDATE` on the contract, unique(recipient_id) on signature, unique(tenant, idempotency key). Queue `jobId` is a hint only.
- **Tenancy:** transaction-local `set_config('app.tenant_id')` under a non-owner role with Postgres RLS as defence in depth, plus tenant id in every job, key and cache prefix.
- **Search:** Postgres tsvector + GIN and pg_trgm first; an external engine only after measurement.
- **Legal level:** the platform records evidence for simple signatures. AdES/QES need a trust service provider and are interface-only until decided with counsel.

## Compliance-sensitive areas

eIDAS levels, ESIGN/UETA consent and record retention, UK and UAE electronic-signature law, GDPR retention/erasure/residency, PAdES and timestamping, PDF/A archival (not decided). All flagged in `compliance.json` for human review. Nothing here claims a product is compliant.

## Integrations

Transactional email and SMS providers, S3-compatible storage, ClamAV, TSA, KMS/HSM, qualified trust service providers, identity verification vendors, enterprise SSO, customer webhook consumers, OpenTelemetry, OCR/LLM. See `integrations.json`; vendors are examples only.

## Entities

Organisation, user, role/permission, contract, contract version, document, document file, storage object, template and version, recipient, signature request, field, signature, signing session, OTP challenge, consent, audit event, email/SMS message, email event, reminder, notification, webhook endpoint and delivery, download, completion certificate, verification record, API key, idempotency key.

## UI patterns

Preparation workspace (thumbnail rail, page canvas, field palette, recipient colour coding, properties panel), signing flow (start, next required field, sticky finish), contract list with URL-state filters, audit timeline, template browser, settings by section. Patterns are drawn from open-source editors; proprietary vendor designs are not copied.

## Mobile

Responsive web signing first; Flutter for touch signature, PDF view (PDFium-based `pdfrx` candidate, maintenance unverified), OTP entry, secure token storage and biometric unlock (`local_auth`, `flutter_secure_storage`).

## AI

Optional, tenant opt-in, off by default: summarisation, clause extraction, risk flags, metadata/variable extraction, OCR, classification, semantic search, comparison, missing-signature and anomaly detection. Uses the kit's `ai/` layer.

## Sources and licensing

Open-source e-signature products (Documenso, DocuSeal, OpenSign, LibreSign, Papermark) are AGPL-3.0, several with proprietary `ee/` parts or attribution terms: **reference only, not cloned, never copied**. Permissive libraries (pdfjs, react-pdf, pdf-lib fork, signpdf, pkijs, pdfkit, signature_pad) are candidates to use as dependencies. See `sources.md`.

## Terminology

Envelope = contract. Recipient roles: signer, approver, CC, witness. AdES/QES = advanced/qualified electronic signature. PAdES = PDF Advanced Electronic Signatures. TSA = timestamp authority. Sealing = producing the final immutable PDF.
