# Security findings

Technical considerations, **not legal advice**. [V] = verified this session; otherwise prior knowledge — review before relying.

## Threat model

| Threat | Control |
|---|---|
| IDOR / BOLA | Authorise the object, not the route: every repository query takes tenant + actor; signing endpoints resolve the recipient from the token, never from a URL id |
| Tenant leakage | RLS deny-by-default [V], transaction-local `set_config`, non-BYPASSRLS role, tenant in job payloads, tenant-prefixed storage keys, cache keys, search filters, webhook endpoints |
| Privilege escalation | Permission checks on every mutation; role changes audited; overrides explicit and logged |
| Token theft/replay | CSPRNG 32 bytes [V: OWASP CSPRNG/single-use/expiry], hash-only storage, expiry, revoke, rotate, single purpose (view ≠ sign ≠ download); session bound to token + device/IP signals as risk input, not identity |
| OTP abuse | HMAC-stored code, 5 attempts/challenge, resend cooldown, Redis limits per IP + link. **Lock the challenge/link, not the account** — account lockout on reset-style flows enables DoS [V: OWASP] |
| Webhook replay | Signed `id.timestamp.payload` [V], reject stale timestamps (~5 min), dedupe by id, dual secrets on rotation |
| SSRF (webhook URLs, fetches) | Resolve DNS then block private/link-local/loopback/metadata IPs, disable redirects, allow https only, connect to the resolved IP |
| Upload attacks | Magic-byte sniff, allow-list (PDF + few images), size/page caps, ClamAV quarantine, presigned URLs with size limit + short expiry, never trust client MIME |
| PDF attack surface | Reject/strip `/JavaScript`, `/OpenAction`, `/Launch`, `/EmbeddedFiles`, XFA; parse in worker with timeout + memory limit; `qpdf --check` preflight; guard decompression bombs |
| XSS / CSRF / sessions | CSP, output encoding, httpOnly + SameSite cookies, CSRF tokens on cookie-auth mutations, no tokens in URLs logged (strip from referrer/logs) |
| Race conditions | See backend.md concurrency table |
| Secrets | Secret manager, rotation, never logged; signing keys in KMS/HSM |
| Secure download | Authz then short-lived presigned URL; audit every download; `Content-Disposition` + `nosniff` |

## Compliance engineering implications (technical considerations only)

| Regime | Engineering implication |
|---|---|
| eIDAS (EU) | Evidence-rich SES is engineerable; AES needs signer-linked keys/identity; QES needs a qualified trust service provider — integrate, don't fake |
| UK | Treated as evidence-based like eIDAS-UK; unverified — counsel |
| US ESIGN/UETA | Capture consent to transact electronically, intent to sign, record association, retain and give signer a copy |
| UAE (Decree-Law 46/2021) | Evidence-based regime assumed; unverified — counsel |
| GDPR | Lawful basis, per-tenant retention, export, erasure vs audit-retention reconciliation (pseudonymise, don't delete evidence) |

Cross-cutting: trusted server time, UTC storage, optional RFC 3161 timestamp, consent record, audit export, integrity hash of the sealed PDF, retention policy per tenant. None of this makes a product compliant.

## Future interfaces (interfaces only, no fake crypto)

`IdentityVerifier` (email/SMS/passcode → KYC/IdP), `SigningCertificateProvider` (tenant/CSC/QTSP, KMS/HSM-backed), `TimestampAuthority` (RFC 3161), `VerificationService` (public hash/QR lookup returning integrity + metadata only, no document content). Each ships as an interface with a "not implemented" adapter until a real provider is chosen.
