# Fintech

Digital financial products — customer wallets, accounts, payments, cards, and lending — built on a double-entry ledger with KYC/AML controls. Covers neobanks, embedded-finance/BaaS platforms, and standalone lending products. NACE: K64.19 (other monetary intermediation), K64.92 (other credit granting), K66.19 (activities auxiliary to financial services).

## Product types
Neobank / digital wallet app · embedded finance (banking-as-a-service for a non-bank product) · standalone lending platform · payment/remittance processor front-end.

## Users
Customer (party) · Compliance Officer · Risk/Fraud Analyst · Support Agent · Loan Officer · Finance Operations · Administrator · System (automation).

## Core workflows
1. **KYC onboarding** — submit documents → verify identity → screen sanctions/PEP → compliance review if flagged → approve/reject.
2. **Payment lifecycle** — initiate → authorize/fraud-screen → submit to rail → settle/fail → reverse if disputed.
3. **Loan lifecycle** — apply → underwrite → approve/reject → disburse → repay → close/default.
4. **Dispute lifecycle** — open → investigate → resolve (customer/merchant) → close.
5. **Reconciliation** — import external statement → auto-match ledger entries → flag discrepancies → resolve.

## Capabilities
- **Core:** party management, KYC/onboarding, double-entry ledger accounts, wallets, payments, limits management, fraud/risk monitoring, reconciliation.
- **Common:** internal/P2P transfers, card issuing & controls, lending origination & servicing, statements, fee management, dispute/chargeback management.
- **Recommended:** interest accrual, credit scoring, multi-currency ledger, virtual account numbers.
- **Optional:** recurring payments, bill pay, savings goals, spend analytics.
- **Compliance:** AML/CFT transaction monitoring, sanctions/PEP screening.
- **Integration:** open banking connectivity, webhooks/event notifications.

## Compliance-sensitive areas
AML/CFT (FATF Recommendations; EU AMLR/AMLD package; US BSA) on onboarding and transaction monitoring; PSD2 Strong Customer Authentication (with PSD3/PSR in EU legislative progress — verify current status) on payments and open banking; PCI DSS on card issuing and payments; GDPR on personal/KYC data. All require human/legal review — the catalog never claims a product "is compliant" (see `compliance.json`).

## Integrations
KYC/identity verification provider · payment rail/network (card networks, ACH, SEPA, SWIFT) · card issuing processor · credit bureau · fraud/risk scoring engine · webhook delivery.

## Entities
party, kyc_case, account, ledger_entry, wallet, payment, transfer, card, loan, loan_schedule, statement, fee, limit, fraud_alert, dispute, reconciliation_run — see `entities.json`.

## UI patterns
Customer: balance/wallet home, transaction list/detail, send/request money, card freeze toggle, statement download. Staff: KYC review queue, fraud alert queue, loan underwriting workspace, reconciliation discrepancy list.

## Mobile
Customer-facing wallet/payments/cards are mobile-first; staff review/underwriting tools are typically web/admin only.

## AI
Identity-document extraction and liveness scoring (KYC), transaction fraud scoring, credit scoring, spend categorization/insights — all `ai_relevance: high` on their respective features; used as decision support, not autonomous compliance decisions.

## Standards & terminology
ISO 20022 (payment messaging), ISO 4217 (currency codes), ISO 13616/IBAN (account numbering), FIBO (`std:fibo`, financial-entity/relationship terminology).

## Sources
Apache Fineract (Apache-2.0, inspected via API), Formance Ledger (MIT, inspected via API), Blnk (Apache-2.0, cloned — `sources/domains/blnk/`) for the double-entry ledger/account/transaction/identity model. See `sources.md` for the full registry and what each source did/didn't inform.
