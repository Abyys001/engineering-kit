# signing

- `signature-capture.tsx` — draw (`signature_pad`, MIT) or type. Emits a PNG data URL + typed text. Deps: `signature_pad`.
- `field-overlay.tsx` — percent-positioned field layer over a rendered PDF page; `nextRequiredField()` for the "Next" button. Uses the same relative rect as `backend/pdf`. No dependencies.

Not included (compose from the kit's existing sources): OTP input → shadcn `input-otp` (MIT); PDF page rendering → `react-pdf`; drag-and-drop palette → `dnd-kit`; resizable panels → shadcn `Resizable`. Mobile: reuse the same components in a sticky-bottom-action layout; see `docs/research/contract-platform/ux-patterns.md`.
Origin: original; typechecked strict against React 19 types. Adapt: labels come from your i18n layer; swap the plain elements for shadcn primitives.
