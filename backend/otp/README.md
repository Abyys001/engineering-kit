# otp

Email/SMS one-time codes as challenges. **Origin:** original; `node:crypto` only. `otplib` was rejected: it is for TOTP, not delivered codes.

- `randomInt` code; store `HMAC-SHA256(secret, challengeId:code)`, never the code; constant-time compare.
- Attempt cap + TTL + consumed flag (replay). Lock the **challenge**, not the account (OWASP: account lockout on recovery flows is a DoS vector).
- **You add:** row lock (`SELECT … FOR UPDATE`) around `verifyOtp` + persist `next`; resend cooldown and per-IP/per-link rate limits in Redis; audit events for issued/failed/locked/verified; delivery via the email/SMS provider interface.
- Secret comes from your secrets manager; rotate by keying challenges with a key id.
