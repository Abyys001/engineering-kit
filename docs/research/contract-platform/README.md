# Contract + e-signature platform — research

Date: 2026-09-29 · Scope: reusable foundation for a DocuSign / Dropbox Sign-style product on the kit stack (Next.js/React/TS/Tailwind/shadcn/TanStack Query · NestJS/Drizzle/Postgres/Redis+BullMQ · Flutter). No product is built here.

Companion docs: [frontend](frontend.md) · [backend](backend.md) · [security](security.md) · [ux-patterns](ux-patterns.md). Kit paths: `backend/{signing-tokens,otp,webhooks,audit-log,contracts,tenancy,pdf}`, `components/web/{signing,typography}`, `domains/e-signature`.

## Evidence quality (read first)

| Verified this session | Not verified (prior knowledge — confirm before relying) |
|---|---|
| npm registry versions + licenses (pdfjs-dist, react-pdf, @cantoo/pdf-lib, pdf-lib, mupdf, pdfkit, pdfmake, @react-pdf/renderer, @signpdf/signpdf, pkijs, node-forge, @hyzyla/pdfium, @embedpdf/core) | Vendor UX details (DocuSign, Dropbox Sign, Adobe Sign, PandaDoc, SignWell, BoldSign, Zoho Sign…) |
| GitHub API license + last-push + stars for the OSS repos below | Vendor completion-certificate layouts |
| google/fonts file listing + OFL/TRADEMARKS text (Google Sans, Google Sans Flex, Vazirmatn) | Provider bounce/complaint event schemas (SES, Postmark, Resend, SendGrid, Twilio, Vonage) |
| Standard Webhooks spec; OWASP forgot-password cheat sheet; Drizzle RLS docs | Flutter packages: pdfrx, signature, local_auth, flutter_secure_storage, pdfx |
| | react-email, input-otp, signature_pad licence (believed MIT), dnd-kit |
| | All legal texts (eIDAS, ESIGN/UETA, UK, UAE 46/2021, GDPR) — none fetched |
| | PAdES-LT/LTA tooling gaps, PDF attack-surface list, pdfme/EmbedPDF per-package licences |

Legal/compliance material anywhere in this folder is a **technical consideration, not legal advice**.

## Repositories reviewed (license verified via GitHub API)

| Repo | License | Last push | Verdict |
|---|---|---|---|
| documenso/documenso | AGPL-3.0; `packages/ee` proprietary | 2026-09-29 | REFERENCE — best field/recipient/audit model |
| docusealco/docuseal | AGPL-3.0 + attribution terms | 2026-09-28 | REFERENCE — form builder, field schema |
| OpenSignLabs/OpenSign | AGPL-3.0 (carve-out dir) | 2026-08-21 | REFERENCE — Parse/Mongo is a poor fit |
| LibreSign/libresign | AGPL-3.0 | 2026-09-29 | REFERENCE — PKCS#12/PAdES concepts |
| papermark/papermark | AGPL-3.0; `ee/` commercial | 2026-08-28 | REFERENCE — data-room/analytics only |
| pdfme/pdfme | MIT | 2026-09-29 | REFERENCE/ADAPT — designer; embed in Next.js unchecked |
| standard-webhooks/standard-webhooks | Apache-2.0 | 2026-09-24 | IMPLEMENT (spec, own ~50 lines) |
| svix/svix-webhooks | MIT | 2026-09-29 | REFERENCE — design only; self-hosting is an extra service |
| szimek/signature_pad | MIT (believed) | 2026-09-29 | IMPLEMENT |
| embedpdf/embed-pdf-viewer | Apache-2.0 mostly; `cloudpdf/server` FCL | 2026-09-29 | REFERENCE — duplicates react-pdf |
| docusign-esign-node-client | MIT | 2026-07-16 | REFERENCE — envelope/recipient/tab vocabulary |
| react-pdf-viewer | custom, archived | 2024-08-19 | REJECT |

## Library selections

| Need | Selected | Rejected (reason) |
|---|---|---|
| Browser PDF render | pdfjs-dist 6.x (Apache-2.0) via react-pdf 11 (MIT) | EmbedPDF (heavier, duplicate), react-pdf-viewer (archived) |
| Server stamp/merge/flatten | @cantoo/pdf-lib (MIT, active fork) | pdf-lib 1.17.1 (unmaintained since 2022), mupdf (AGPL) |
| PAdES + RFC 3161 | @signpdf/signpdf + pkijs (BSD-3) | node-forge (GPL dual, ASN.1 CVEs) |
| Certificate PDF | pdfkit (MIT) | Chromium/Playwright (heavy, sandbox surface), pdfmake / @react-pdf/renderer (overlap), Syncfusion (commercial) |
| Thumbnails/text (server, optional) | @hyzyla/pdfium (MIT) | — |
| Webhook signing | Standard Webhooks via `node:crypto` | self-hosted Svix |
| OTP | `node:crypto` randomInt + HMAC | otplib (TOTP-oriented; unnecessary for SMS/email OTP) |
| Fonts | Google Sans Flex (OFL) + Vazirmatn (OFL) | — |

## Conflict resolutions

- **otplib:** OSS track said IMPLEMENT, backend track REJECT → REJECT for SMS/email OTP; revisit only for authenticator-app TOTP.
- **pdf-lib:** pdfme's fork vs `@cantoo/pdf-lib` → `@cantoo/pdf-lib` (verified active, drop-in).
- **pdfme:** kept REFERENCE/ADAPT until embeddability, React 19/Next compatibility and UI-package licence are checked.

## Conclusions

- **Architecture:** own the workflow (envelope, recipients, fields, audit, sealing) in NestJS/Drizzle/BullMQ; every AGPL e-sign project is reference-only.
- **Frontend:** pdfjs/react-pdf + page-relative 0–1 field coordinates + pointer-event field editor; dnd-kit only for palette drops.
- **Backend:** Postgres is the source of truth for every race; queue dedupe is an optimisation, never correctness.
- **Security:** hashed single-purpose tokens, per-link (not per-account) lockout, per-envelope hash chain, RLS as defence in depth.
- **Mobile:** Flutter signing is web-view-free where possible; packages unverified — justify each on adoption.

## Future opportunities

AES/QES via trust-service-provider adapter · RFC 3161 timestamping · PAdES-LT/LTA (custom DSS/VRI work) · PDF/A sidecar · KYC/IdP adapters · public QR verification · AI (clause extraction, summarisation, semantic search) on the existing `ai/` architecture · Postgres → external search only if measured slow.
