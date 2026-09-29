# UX patterns

Generalised from public product behaviour (DocuSign, Dropbox Sign, Adobe Acrobat Sign, PandaDoc, SignWell, Documenso, DocuSeal, BoldSign, Zoho Sign). Vendor specifics were **not verified this session**; no proprietary design or assets are copied (`ui-design-policy.md` §2).

| Area | Pattern | Component concept |
|---|---|---|
| Contract list | Dense table, status badge, next-action column, recipient progress, expiry indicator; URL-state filters + saved views; command-palette search | `ContractStatusBadge`, `SignerProgress`, tablecn / data-table-filters sources |
| Contract detail | Header (title, number, status, actions) · tabs: Document, Recipients, Activity, Versions, Downloads | `ContractHeader`, `VersionList`, `DownloadPanel` |
| Timeline / audit | Chronological events with actor, IP/device summary, expandable hash/metadata; export | `AuditTimeline` |
| Prepare document | Left: recipients + field palette; centre: pages with thumbnails rail; right: properties panel; recipient colour coding; snap/align, duplicate, multi-page copy; validate "every signer has a signature field" before send | `DocumentViewer`, `FieldOverlay`, `FieldPalette`, `FieldPropertiesPanel` |
| Recipients & routing | Ordered list with drag reorder; roles (signer, approver, CC, witness); sequential vs parallel; optional recipients; per-recipient status, resend, reminder | `RecipientList`, `SigningOrderEditor`, `ReminderDialog` |
| Signing | Consent → guided "next required field" → adopt signature once (draw/type/upload) → reuse for initials → Finish enabled at 100% → confirmation + download | `ConsentCheckbox`, `SigningProgress`, `SignatureCapture`, `CompletionScreen` |
| Verification | OTP screen with clear attempt/expiry feedback, banner when identity level applies | `OtpInput`, `VerificationBanner` |
| Templates | Browser with preview, variables (picker inserts placeholders), version + publish/archive states | `TemplateCard`, `TemplateVariablePicker` |
| Notifications / email | Inbox-style activity centre; email preview with variable substitution; delivery timeline showing only provider-confirmed states | `NotificationCentre` (reuse `features/notifications`) |
| Admin / settings | Left-nav settings sections: general, security, signing, authentication, email, SMS, branding, templates, storage, retention, audit, webhooks; one save model per section; danger zone separated; webhook secret shown once | shadcn settings blocks |
| Mobile signing | Single-column page, pinch zoom, one field at a time, sticky bottom "Next / Finish", progress count, large touch-signature canvas (landscape hint), no offline final signature | responsive overlay, Flutter parity |

## Design principles

Dense but readable enterprise UI; strong hierarchy; one type scale (Google Sans Flex, Vazirmatn for fa/ar); restrained colour (recipient colours are the only saturated palette); status via badge + text, never colour alone; visible focus and keyboard paths for field placement; skeleton/empty/error states; no glassmorphism, no gradient heroes, no card-in-card. Per-product visual variation follows `ui-design-policy.md` §3; write `docs/design/DESIGN.md` per app.
