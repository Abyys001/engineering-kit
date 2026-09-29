# Engineering Kit Upgrade — Contract Platform

2026-09-29. Companion docs: [README](README.md) · [frontend](frontend.md) · [backend](backend.md) · [security](security.md) · [ux-patterns](ux-patterns.md). Legal/compliance content is technical consideration only, not legal advice, and needs human review.

## Existing Architecture
Inspected: README, INDEX, catalog.json, sources/CURATION.md + CANDIDATES.md, 44 pinned upstream sources, 15 domains under `domains/`, policies in `docs/conventions/`. **Nothing was promoted** into `components/ features/ backend/ mobile/ ai/ patterns/ starters/` (all `.gitkeep`). So "reuse" of kit code was not possible; only policy (stack: Next/React/Tailwind/shadcn/TanStack; NestJS/Drizzle/Postgres/Redis+BullMQ; Flutter; zod everywhere) and source pointers existed. No kit equivalent of PDF, signing, email/SMS providers, webhooks, or storage existed; the existing `refine` (audit-log provider contract), `boxyhq-saas-starter` (webhooks, multi-tenancy patterns) and `nestjs-starter` (BullMQ, RBAC) sources are useful references but were not deeply re-reviewed in this pass.

## Research Summary
Four parallel research tracks (OSS repos, PDF stack, backend/security, frontend/fonts) merged into decisions. **Evidence quality is uneven** — see README "Evidence quality". Verified this session: npm versions/licenses, GitHub API license + last-push, google/fonts file listing and OFL text (I re-checked these directly), Standard Webhooks spec, OWASP forgot-password sheet, Drizzle RLS docs. **Not verified**: vendor UX details and certificate layouts, email/SMS provider event schemas, Flutter package status (pdfrx, signature, local_auth), react-email/input-otp maintenance, every legal text. Also not done: I did not read the source of any AGPL project, and the per-product study of DocuSign/Dropbox Sign/etc. is from prior knowledge, not fresh fetches.

## Frontend Findings
Browser PDF: `pdfjs-dist` 6.3 (Apache-2.0) + `react-pdf` 11 (MIT). Field geometry stored as page-relative fractions. Signature capture: `signature_pad` 5.1.4 (MIT). OTP input: shadcn `input-otp` 1.5 (MIT, verified). Drag/drop: `dnd-kit`; panels: shadcn Resizable. Added: `signature-capture`, `field-overlay` (+`nextRequiredField`), `contract-status-badge`. **Not added**: prepare-document editor, PDF viewer wrapper, recipient cards, audit timeline, template UI, settings layouts, notification centre, OtpInput, CompletionScreen — the domain doc describes them; none built.

## Backend Findings
Added (original, strict-typed, 30 passing `node --test` tests): signing tokens, OTP challenges, Standard-Webhooks signing + SSRF guard + backoff, per-contract audit hash chain (+ Postgres immutability SQL in README), contract state machine, tenant context/job payload/tx wrapper, PDF field-coordinate conversion. Concurrency, RLS and idempotency are documented patterns (README/backend.md), not tested DB code — no database was run.

## PDF / Document Findings
Server: `@cantoo/pdf-lib` (pdf-lib unmaintained since 2022), `pdfkit` for certificate, `@signpdf/signpdf` + `pkijs` for PAdES/RFC 3161. Rejected: `mupdf` (AGPL), `node-forge`, Syncfusion, Chromium certificates. Gaps: PAdES-B-LT/LTA needs custom DSS/VRI work; PDF/A has no maintained Node generator. **No stamping, sealing, or certificate code was added** and none of the listed server libraries was executed here.

## Security Findings
Hashed single-use tokens; challenge-level (not account) OTP lockout per OWASP; tamper-*evident* chain with documented limits (tail truncation invisible unless head hash anchored); SSRF resolve-then-pin; RLS on non-BYPASSRLS role with transaction-local `set_config`; upload preflight; webhook replay = consumer dedupe on `webhook-id`. Test coverage exists for tokens, OTP, webhooks/SSRF, chain, state machine, tenancy context, coordinates. Not tested: RLS against a real Postgres, upload attacks, concurrent signing.

## Email Findings
Provider-independent `MessageProvider` interface + normalized bounce/complaint/delivery event table recommended (SES/Postmark/Resend/SendGrid/Mailgun). **Not implemented**; provider webhook schemas unverified. Delivery status must come from provider events only.

## SMS Findings
Same abstraction (Twilio primary; Vonage/MessageBird/SNS as adapters). Not implemented; unverified.

## Mobile Findings
Flutter: `pdfrx`, `signature`, `local_auth`, `flutter_secure_storage` proposed — **none verified this session and nothing added**. Mobile signing UX documented in ux-patterns.md.

## Infrastructure Findings
S3-compatible storage with presigned URLs, BullMQ workers per queue (email, sms, pdf, webhooks, retention), ClamAV quarantine, structured logging, backups. Documented in backend.md; no infra code added.

## Domain Capability Matrix
Source: `domains/e-signature/` (69 features; validates with 0 errors; maturity `partial`, quality gate **not met**: ~51% of features are low-confidence against a 30% limit). "Reused" is "no" throughout because the kit had no promoted code. "Exists": partial = some kit code now exists, reference = only a source/pattern.

| Capability | Exists | Reused | Added | Kit path | Priority (classification) | Notes |
|---|---|---|---|---|---|---|
| Contract (envelope) management | partial | no | yes | `components/web/contract`, `backend/contracts` | core | State machine and status badge only; aggregate and UI not built. |
| Contract state machine | partial | no | yes | `backend/contracts` | core | Partial reusable module; see path README. |
| Document management | no | no | no | — | core | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Upload validation and malware scanning | no | no | no | — | core | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Document processing pipeline | reference | no | no | — | core | Local source informs the pattern only; the e-signature specifics are not covered. |
| PDF viewer | no | no | no | — | core | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Document preparation | no | no | no | — | core | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Field placement | partial | no | yes | `components/web/signing`, `backend/pdf` | core | Coordinate conversion and overlay component only; editor not built. |
| Field types and validation | partial | no | yes | `backend/pdf` | core | Coordinate helpers only; field schema not built. |
| Recipient management | no | no | no | — | core | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Signing order and routing | no | no | no | — | core | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Signature capture | partial | no | yes | `components/web/signing` | core | Signature capture component only. |
| Initials capture | no | no | no | — | common | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Electronic signing consent | no | no | no | — | core | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Signing session | no | no | no | — | core | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Secure signing tokens | partial | no | yes | `backend/signing-tokens` | core | Real module; see backend/signing-tokens/README.md. Tests exist, not production-hardened. |
| One-time-code verification | partial | no | yes | `backend/otp` | common | Partial reusable module; see path README. |
| Signer identity verification levels | no | no | no | — | common | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Email delivery abstraction | reference | no | no | — | core | Local source informs the pattern only; the e-signature specifics are not covered. |
| Signing email notifications | no | no | no | — | core | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| SMS notifications and OTP delivery | no | no | no | — | common | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| In-app notification centre | reference | no | no | — | common | Local source informs the pattern only; the e-signature specifics are not covered. |
| Reminders and expiry | reference | no | no | — | common | Local source informs the pattern only; the e-signature specifics are not covered. |
| Document and contract versioning | no | no | no | — | common | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Document hashing and integrity | no | no | no | — | core | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Final PDF generation | partial | no | yes | `backend/pdf` | core | Coordinate helpers only; stamping/flatten/seal not built. |
| Immutable signed documents | no | no | no | — | core | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Completion certificate | no | no | no | — | core | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Immutable audit trail | partial | no | yes | `backend/audit-log` | core | Partial reusable module; see path README. |
| Public verification page | no | no | no | — | common | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Secure downloads | no | no | no | — | core | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Storage abstraction (S3-compatible) | no | no | no | — | core | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Webhooks | partial | no | yes | `backend/webhooks` | common | Partial reusable module; see path README. |
| Webhook retry and dead-letter | partial | no | yes | `backend/webhooks` | common | Partial reusable module; see path README. |
| Search and filtering | reference | no | no | — | common | Local source informs the pattern only; the e-signature specifics are not covered. |
| Exports and reports | no | no | no | — | common | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Templates | no | no | no | — | common | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Organisation branding | no | no | no | — | common | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| RBAC and permission overrides | reference | no | no | — | common | Local source informs the pattern only; the e-signature specifics are not covered. |
| Multi-tenancy and isolation | partial | no | yes | `backend/tenancy` | core | Partial reusable module; see path README. |
| Concurrency control and idempotency | no | no | no | — | core | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Rate limiting and anti-abuse | reference | no | no | — | core | Local source informs the pattern only; the e-signature specifics are not covered. |
| Security events | no | no | no | — | common | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Admin security settings | reference | no | no | — | common | Local source informs the pattern only; the e-signature specifics are not covered. |
| Observability | reference | no | no | — | common | Local source informs the pattern only; the e-signature specifics are not covered. |
| Internationalisation and RTL | partial | no | yes | `components/web/typography` | common | Fonts and typography docs only; no i18n framework wiring. |
| GDPR and retention | no | no | no | — | compliance | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Legal hold | no | no | no | — | compliance | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Data residency | no | no | no | — | premium | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Billing readiness | no | no | no | — | common | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Public API, API keys and sandbox | reference | no | no | — | platform | Local source informs the pattern only; the e-signature specifics are not covered. |
| Domain testing strategy | no | no | no | — | infrastructure | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Backup and disaster recovery | no | no | no | — | infrastructure | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Mobile signing | reference | no | no | — | common | Local source informs the pattern only; the e-signature specifics are not covered. |
| Decline, void and correct | no | no | no | — | common | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Delegation and reassign | no | no | no | — | optional | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Witness and in-person signing | no | no | no | — | optional | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Bulk send | no | no | no | — | optional | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Public signing links | no | no | no | — | optional | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Conditional and calculated fields | no | no | no | — | optional | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Attachment requests | no | no | no | — | optional | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Embedded signing | no | no | no | — | optional | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| SSO and SCIM provisioning | reference | no | no | — | optional | Local source informs the pattern only; the e-signature specifics are not covered. |
| Approval workflow | no | no | no | — | optional | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Comments and collaboration | no | no | no | — | optional | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Contract repository and renewals | no | no | no | — | optional | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Advanced and qualified signatures | no | no | no | — | premium | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| Document and KYC verification | no | no | no | — | premium | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |
| AI contract intelligence | no | no | no | — | premium | Assessed: no kit code or on-disk source covers it. Open-source e-signature repositories are reference-only (AG |

Full per-capability requirements (backend/frontend/mobile/data/security/jobs/events/tiers): [`domains/e-signature/CAPABILITIES.md`](../../../domains/e-signature/CAPABILITIES.md). Data model: [DATA-MODEL.md](../../../domains/e-signature/DATA-MODEL.md). API: [API-PATTERNS.md](../../../domains/e-signature/API-PATTERNS.md).

## Imported / Adapted Sources
None imported. No upstream code was copied. Fonts (OFL-1.1) copied unmodified from `google/fonts`: Google Sans Flex, Google Sans (+Italic), Vazirmatn → `components/web/typography/fonts/` with OFL.txt (+TRADEMARKS.md). Fonts are TTF; **WOFF2 subsetting is not done** (README says do it before shipping). Google Sans Flex has no Arabic/Persian; Google Sans Arabic coverage unverified.

## References Only
Documenso (AGPL + proprietary ee), DocuSeal (AGPL + attribution terms), OpenSign (AGPL), LibreSign (AGPL), Papermark (AGPL + ee), Svix, Standard Webhooks (spec implemented from scratch), `docusign-esign` SDK (MIT, only if integrating), `pdfme` and `embedpdf` (candidates pending embed/license check). See `sources/CANDIDATES.md`. None cloned.

## Rejected Sources
`mupdf` (AGPL), `pdf-lib` 1.17 (stale), `node-forge` (GPL option, CVEs), `react-pdf-viewer` (archived, custom license), Syncfusion, `otplib` for SMS/email OTP, `react-signature-canvas`, `react-rnd`, `pdfx`, Chromium/Playwright certificates, self-hosted Svix, global audit hash chain.

## New Engineering-Kit Structure
```
backend/{signing-tokens,otp,webhooks,audit-log,contracts,tenancy,pdf}/  (src, tests, README, tsconfig)
backend/tsconfig.base.json
components/web/{signing,contract,typography}/
domains/e-signature/  (DOMAIN, CAPABILITIES, DATA-MODEL, API-PATTERNS + 9 JSON maps)
docs/research/contract-platform/
```
Run tests: `node --test backend/*/src/*.test.ts` (Node ≥ 22.18).

## Recommended Future Contract Platform Architecture
NestJS modular monolith; Postgres with RLS + tenant context; BullMQ workers (pdf, email, sms, webhooks, reminders, retention); S3-compatible storage with immutable versioned objects and SHA-256 hashes; contract state machine with CAS + row-lock completion; per-contract audit chain anchored in the completion certificate; provider-adapter interfaces for email/SMS/KYC/trust services; Next.js signing app on relative-coordinate fields; Flutter reuses the same API and signing-session tokens. AdES/QES only via a qualified trust-service adapter, later.

## Known Gaps
Not built: prepare-document editor, PDF viewer component, recipient/audit/template/settings/notification UI, email/SMS/storage/document/retention/search modules, stamping/sealing/certificate generation, i18n scaffolding, Flutter modules, AI capabilities, test fixtures for DB/concurrency. The 69-feature domain has 44 `missing` implementations. Kit-wide: `kb.py validate` still emits 35 pre-existing warnings in other domains.

## Risks
1. Vendor/provider/legal claims marked low confidence are unverified. 2. Timestamp tolerance, OTP limits and state list are defaults, not product decisions. 3. Font files unsubsetted (15 MB). 4. pdfme/EmbedPDF embed and per-package licensing unchecked. 5. Code is strict-typechecked and unit-tested but never run against Postgres/Redis/S3.

## Next Steps
1. Build the Drizzle schema from DATA-MODEL.md + RLS migration with a two-tenant test. 2. Spike: upload → preflight → react-pdf → relative field placement → `@cantoo/pdf-lib` stamp → pdfkit certificate → signpdf B-B, on rotated/CropBox-offset PDFs. 3. Email/SMS provider interfaces + event normalization. 4. Promote a prepare-document editor and viewer. 5. WOFF2 subsetting. 6. Human legal review of compliance.json before any compliance claim.
