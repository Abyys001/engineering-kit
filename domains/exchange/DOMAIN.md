# Currency Exchange

Business management for a currency-exchange / money-exchange operation — bureau de change counters and remittance desks — not a crypto trading engine. NACE: K64.99 (other financial service activities n.e.c.; covers currency exchange on own account).

**Maturity note:** genuine open-source coverage of this vertical is thin. A GitHub search for bureau-de-change / money-changer / forex-bureau software found no maintained, well-starred project; the two implementation sources used here (`bdc-api`, `chfx-odoo-modules`) are hobby-scale/addon-scale but give real, concrete data models. Maturity is recorded as `partial`, honestly, rather than `curated`.

## Related but distinct product type
**Crypto exchange** (order books, matching engines, custody, trading pairs — e.g. Bisq, an AGPL-3.0 P2P crypto exchange) is a related but different product: it trades continuously at market-discovered prices with no physical cash, versus a bureau de change's counter-quoted buy/sell rates on physical or bank-transferred cash. Not modeled in this domain; flag explicitly if a request turns out to be a crypto exchange instead.

## Product types
Single-branch or multi-branch bureau de change · remittance/money-transfer counter · exchange desk embedded in a travel/hospitality business.

## Users
Customer · Teller/Cashier · Branch Manager · Compliance Officer · Administrator · System (rate feeds, threshold flags).

## Core workflows
1. **Exchange transaction** — quote a rate → customer accepts → capture ID if above threshold → lock rate, record transaction → update till position → receipt.
2. **Rate update** — pull/enter a rate → apply spread policy → publish to branches.
3. **Cash session** — open till with a float → transact through the shift → count and reconcile at close.
4. **AML report** — auto-flag a transaction crossing a threshold → compliance review → file or dismiss.

## Capabilities
- **Core:** customer management, currency master data, buy/sell rate & spread management, exchange requests/quotes, buy/sell transactions, tills/cash positions, branch management, audit log.
- **Common:** rate-feed ingestion, remittance, staff management, receipts, reports & analytics, commission management.
- **Compliance:** KYC transaction thresholds, AML suspicious/large-transaction reporting.
- **Optional:** customer notifications, online rate lookup/order-ahead.

## Compliance-sensitive areas
KYC due-diligence thresholds and AML suspicious/large-transaction reporting trace to FATF Recommendation 20 and the customer-due-diligence recommendations, which most jurisdictions implement by naming currency exchange offices as obliged entities (see EU AMLR/AMLD for one concrete example). **No jurisdiction-specific rule — including any Iranian regulation — is asserted anywhere in this domain**; every compliance item is global/EU-sourced, marked `requires_human_review: true`, and a real deployment must have its own jurisdiction's regulator confirm exact thresholds and filing rules.

## Integrations
Market rate source (e.g. ECB reference-rate feeds) · remittance network partner (e.g. Western Union-style networks).

## Entities
customer, currency, exchange_rate, exchange_request, exchange_transaction, remittance, till, cash_session, branch, staff, aml_report — see `entities.json`.

## UI patterns
Customer: rate board, quote request, transaction receipt. Teller: quick buy/sell ticket, till open/close, ID capture at threshold. Manager/Compliance: rate override, cash-session reconciliation, AML flag queue, branch reports.

## Mobile
Primarily a counter/back-office (web/admin) product; customer-facing mobile is optional (rate lookup, order-ahead) rather than core.

## AI
Limited: AML pattern detection on transaction volume/velocity is the only feature marked `ai_relevance: medium`; most of the domain is rules- and threshold-driven, not model-driven.

## Standards & terminology
ISO 4217 (currency codes), ISO 20022 (settlement/remittance messaging where bank rails are used), FIBO (`std:fibo`, party/transaction terminology).

## Sources
`bdc-api` and `chfx-odoo-modules` (both inspected via GitHub API, not cloned — see licensing notes in `sources.md`) plus FATF Recommendations and the EU AML package for compliance grounding.
