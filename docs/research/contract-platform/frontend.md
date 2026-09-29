# Frontend findings

Baseline: Next.js, React, TypeScript, Tailwind, shadcn/ui (Base UI flavour per `sources/CURATION.md`), TanStack Query/Table/Form, zod. Nothing here replaces that.

## PDF viewer

| Choice | Detail |
|---|---|
| Renderer | `pdfjs-dist` 6.x (Apache-2.0, ships types, needs a worker) through `react-pdf` 11 (MIT) |
| Thumbnails | Low-scale pdfjs canvas per page; render lazily (IntersectionObserver) |
| Hardening | `isEvalSupported:false`; never run PDF JS/XFA; host the worker yourself |
| Rejected | react-pdf-viewer (archived, custom licence); EmbedPDF (REFERENCE — heavier PDFium/WASM) |
| Browser-only | pdfjs render, canvas thumbnails, signature capture. Server stamping is a separate pipeline (see backend.md) |

## Field editor architecture

- **Storage:** `{page, x, y, w, h}` as 0–1 fractions of the page's visible box (CropBox), unrotated orientation, origin top-left. Never CSS pixels, never PDF points. The server converts using CropBox + `/Rotate` and flips y. Helper: `components/web/signing` (coordinate utilities).
- **Layers:** `<Page>` canvas → absolutely positioned overlay sized to the rendered viewport → one `FieldOverlay` per field. Overlay coordinates = fraction × rendered size, so zoom needs no data change.
- **Interaction:** dnd-kit for palette → page drop (ADAPT); plain pointer events for move/resize/snap on the page (react-rnd rejected). Keyboard move/resize is required for accessibility.
- **Model:** field = type, recipientId, required, validation, page-relative box. Recipient colour coding, properties panel, duplicate, multi-page copy.
- **Panels:** `react-resizable-panels` (shadcn `Resizable`) for palette | canvas | properties.
- **RTL:** stored coordinates are direction-independent; only UI chrome flips.

## Signing UX (concepts; vendor detail unverified)

Consent first → Start jumps to next required field → adopt/draw/type/upload signature once, reuse for initials → Finish disabled until required fields done → completion screen with download. See [ux-patterns.md](ux-patterns.md).

| Piece | Choice |
|---|---|
| Signature capture | `signature_pad` directly (IMPLEMENT); react-signature-canvas rejected as a thin wrapper |
| OTP input | `input-otp` (shadcn OTP) |
| Email templates | `react-email` (one tool; maizzle rejected) |
| Rich text | tiptap only if templates need it (REFERENCE) |
| Forms | TanStack Form + zod, shared with NestJS DTOs |

## i18n / RTL / typography

| Item | Decision |
|---|---|
| Latin UI font | **Google Sans Flex** — OFL-1.1, one variable TTF, axes wght 1–1000, wdth 25–151, slnt −10–0, opsz 6–144, GRAD, ROND; italic via `slnt` (no italic file) |
| Alternative | **Google Sans** — OFL-1.1, variable `GoogleSans[GRAD,opsz,wght]` + real italic file |
| Persian/Arabic | Flex has **no Arabic/Persian** subsets → **Vazirmatn** (OFL, variable wght). Google Sans Arabic coverage not checked; assume none |
| Licence caveat | OFL covers the files; "Google", "Google Sans", "Google Sans Flex" are trademarks (`TRADEMARKS.md`) — no product/company naming or implied affiliation |
| Location | `components/web/typography/fonts/{google-sans-flex,google-sans,vazirmatn}/` with each `OFL.txt` (verified against the google/fonts listing, 2026-09-29) |
| Loading | self-host with `next/font/local`; stack: Flex → Vazirmatn → system |
| Layout | Tailwind logical utilities (`ms-`, `ps-`, `text-start`, `rtl:`); `next-intl` |
| Dates/numbers | `Intl.DateTimeFormat('fa-IR-u-ca-persian')`, `Intl.NumberFormat`; store UTC/ISO, format at the edge |
| Validation messages | zod error map per locale |

## Mobile (Flutter) — packages unverified, confirm on pub.dev before adopting

| Need | Candidate | Note |
|---|---|---|
| PDF view | `pdfrx` (PDFium) | `pdfx` rejected (maintenance unclear); avoid Syncfusion (commercial) |
| Signature | `signature` | drawing canvas → PNG |
| Biometrics | `local_auth` | gate re-open of signing session, not the signature itself |
| Secure storage | `flutter_secure_storage` | existing `mobile/storage` first |
| Networking/routing | existing `mobile/networking`, `mobile/routing` | reuse, don't add |

Field coordinates are the same 0–1 model; mobile renders the identical overlay. Sticky bottom action bar, one field at a time, offline-safe draft state (never queue a final signature offline).
