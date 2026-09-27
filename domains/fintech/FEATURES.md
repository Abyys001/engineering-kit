# Fintech features

Generated from `feature-map.json` (29 features). Classification is judgement, not a scope list — see `../_schema/RESEARCH-BRIEF.md`.

## Core

| Feature | Description | AI | Real-time | Confidence |
|---|---|---|---|---|
| `fintech.fraud_monitoring` Fraud / Risk Monitoring | Score transactions in real time against fraud rules/models and flag or block suspicious activity. | high | core | low |
| `fintech.kyc_onboarding` KYC / Onboarding | Capture identity documents, run identity verification, and produce a risk rating before a party can transact. | high | low | high |
| `fintech.ledger_accounts` Ledger Accounts (Double-Entry) | Post every balance movement as a balanced double-entry to an immutable ledger; accounts are a view over ledger entries. | none | medium | high |
| `fintech.limits_management` Limits Management | Enforce per-transaction, daily, and velocity limits on payments, transfers, and card spend. | low | high | medium |
| `fintech.party_management` Party / Customer Management | Maintain customer and counterparty profiles (individuals and organizations) as the root record every account, wallet, and payment attaches to. | low | none | high |
| `fintech.payments` Payments | Move money into or out of the platform over a payment rail (card, ACH, SEPA, wire) with a lifecycle from initiation to settlement. | low | high | high |
| `fintech.reconciliation` Reconciliation | Match internal ledger entries against external settlement/processor/bank statements and surface discrepancies. | low | none | medium |
| `fintech.wallets` Wallets | Stored-value balances a party can hold, fund, and spend from, backed by ledger accounts. | none | high | high |

## Common

| Feature | Description | AI | Real-time | Confidence |
|---|---|---|---|---|
| `fintech.card_controls` Card Controls | Freeze/unfreeze a card and set per-card spend limits or merchant-category restrictions. | none | medium | low |
| `fintech.card_issuing` Card Issuing | Issue virtual or physical debit/prepaid cards linked to a wallet or account. | none | medium | low |
| `fintech.dispute_management` Dispute / Chargeback Management | Let a customer dispute a transaction and route it through investigation to resolution, including card-network chargebacks. | low | none | low |
| `fintech.fee_management` Fee Management | Define fee schedules (flat, percentage, tiered) and assess them against payments, cards, or accounts. | none | none | medium |
| `fintech.internal_transfers` Internal Transfers | Move money between two wallets or accounts on the same platform without leaving the ledger. | none | high | medium |
| `fintech.lending_origination` Lending Origination | Take a loan application, underwrite it against credit/risk data, and approve or reject. | high | low | medium |
| `fintech.loan_servicing` Loan Servicing | Disburse approved loans, generate repayment schedules, apply payments, and track arrears. | low | none | medium |
| `fintech.p2p_transfers` Peer-to-Peer Transfers | Send money to another party by handle, phone number, or account identifier, typically instant. | none | high | medium |
| `fintech.statements` Statements | Generate periodic (monthly) account or card statements summarizing balances and transactions. | none | none | medium |

## Recommended

| Feature | Description | AI | Real-time | Confidence |
|---|---|---|---|---|
| `fintech.credit_scoring` Credit Scoring | Compute or fetch a creditworthiness score to support lending decisions and limit setting. | high | low | low |
| `fintech.interest_accrual` Interest Accrual | Accrue and post interest on interest-bearing balances (savings) or outstanding loan principal on a schedule. | none | none | medium |
| `fintech.multi_currency_ledger` Multi-Currency Ledger | Hold and post balances in more than one currency per party, with FX conversion at transaction time. | none | medium | medium |
| `fintech.virtual_accounts` Virtual Account Numbers | Issue a dedicated account number per customer or purpose that routes incoming funds into the right ledger account automatically. | none | low | medium |

## Optional

| Feature | Description | AI | Real-time | Confidence |
|---|---|---|---|---|
| `fintech.bill_pay` Bill Pay | Pay a registered biller (utility, telecom, government) from a wallet or account. | none | low | low |
| `fintech.recurring_payments` Recurring Payments | Schedule standing orders or subscription-style payments that execute automatically on a recurrence rule. | none | low | low |
| `fintech.savings_goals` Savings Goals | Let a customer set aside money in a labeled sub-balance ('pot') toward a target amount. | low | none | low |
| `fintech.spend_analytics` Spend Analytics | Categorize a customer's transactions and surface spending insights and trends. | high | none | low |

## Compliance

| Feature | Description | AI | Real-time | Confidence |
|---|---|---|---|---|
| `fintech.aml_transaction_monitoring` AML Transaction Monitoring | Continuously screen posted transactions for structuring, unusual patterns, and thresholds requiring a suspicious activity report. | high | medium | high |
| `fintech.sanctions_screening` Sanctions / PEP Screening | Screen parties against sanctions and politically-exposed-person lists at onboarding and periodically thereafter. | medium | low | high |

## Integration

| Feature | Description | AI | Real-time | Confidence |
|---|---|---|---|---|
| `fintech.open_banking_connectivity` Open Banking Connectivity | Expose PSD2-style account information and payment initiation APIs to authorized third-party providers. | none | medium | high |
| `fintech.webhooks_events` Webhooks / Event Notifications | Deliver signed webhook events for account, payment, and card lifecycle changes to integrating partners. | none | high | medium |

