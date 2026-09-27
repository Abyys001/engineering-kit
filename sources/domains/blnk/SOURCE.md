# Blnk

| Field | Value |
|---|---|
| Source URL | https://github.com/blnkfinance/blnk |
| GitHub repository | `blnkfinance/blnk` |
| Category | domains/fintech |
| License | Apache-2.0 — `LICENSE.txt` (verbatim copy of root `LICENSE.md`) |
| Author / organization | Blnk Finance |
| Acquired | 2026-09-27 |
| Revision | `36ecff3ec7f480c38689ad4e6fedc4b9f172a6ff` (main) |
| Attribution required | License notice only |
| Status | reference — Apache-2.0, learn from model/domain shape only, not copied into the kit |

## Useful for
- Real double-entry ledger data model: `Ledger` (grouping), `Balance` (per-currency balance with separate `Balance`/`InflightBalance`/`CreditBalance`/`DebitBalance`/`QueuedDebitBalance`/`QueuedCreditBalance` and an optimistic-lock `Version`), `Account` (external-facing account linking a `Balance` to an `Identity`), `Transaction` (posting, supports multi-way `Distribution` splits), `Identity` (KYC party: individual or organization fields), and a standalone `reconciliation.go` engine.
- Confirms the domain split used in `domains/fintech`: party/identity, ledger account, wallet-like balance, payment/transaction, reconciliation are separate concerns in a real production ledger, not one flat "transactions" table.

## Where things live
- `source/model/` — `ledger.go`, `balance.go`, `transaction.go`, `identity.go`, `accouunt.go` (sic) — the core domain types.
- `source/reconciliation.go`, `source/reconciliation_matching_test.go`, `source/reconciliation_rules_test.go` — matching/reconciliation logic.
- `source/lineage*.go` — fund-lineage / allocation tracking on top of balances.
- `source/api/model/` — API-facing request/response shapes.

## Known dependencies
- Go 1.25, PostgreSQL (`database/`), Redis (`internal/redis-db`), background queue workers (`queue*.go`).

## Do not copy
- No code is copied into the kit; this clone is for domain-model research only (`domains/fintech` entities/features), per the research brief.

## Notes
- `Balance.Balance`/`InflightBalance`/etc. are `*big.Int` in minor units — a real, working answer to "how do you represent money safely," worth remembering even though the kit doesn't copy code.
- Shallow single-commit checkout, sparse (excludes `.claude/`, `AGENTS.md`, etc. per brief); no `node_modules`/vendor present.
