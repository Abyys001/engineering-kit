# signing-tokens

Single-use, expiring, revocable signing-link tokens. **Origin:** original, written for the kit from OWASP token guidance (see `docs/research/contract-platform/security.md`). No dependencies (`node:crypto`).

- 32 random bytes, base64url (43 chars). Only the SHA-256 hash is stored.
- `checkSigningToken` is a pure validity check; consumption must be a conditional `UPDATE … WHERE used_at IS NULL` (a check-then-write is a race).
- Rotation = new token + revoke old, one transaction.
- **Adapt:** persist `SigningTokenRecord` as a Drizzle table with a unique index on `token_hash`, scoped by tenant and recipient. Add IP/device signals in the signing-session layer, not here.
- Run tests: `node --test backend/signing-tokens/src/*.test.ts` (Node ≥ 22.18; type stripping, no build step).
