# webhooks

Outbound webhook signing/verification per [Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks) (Apache-2.0 spec; this implementation is original) + SSRF guard + retry backoff.

- `signWebhook(secrets[], id, payload)` → 3 headers; two secrets = rotation (dual signature). `verifyWebhook` checks tolerance (default 5 min, spec sets none) and compares constant-time. Verify against the **raw body**.
- Replay: the signature does not stop replays inside the tolerance window; consumers dedupe on `webhook-id`.
- `assertPublicHttpsUrl` resolves DNS, rejects private/link-local/loopback, returns the address to pin. Connect to that IP and disable redirects, otherwise DNS rebinding bypasses it. Run at registration **and** at delivery.
- `backoffWithJitter` for BullMQ custom backoff; after the last attempt mark the delivery `failed` (that row is your dead-letter queue).
- Not included: ed25519 (`whsk_`), the delivery table, the BullMQ processor. Svix (MIT) is reference for a hosted alternative.
