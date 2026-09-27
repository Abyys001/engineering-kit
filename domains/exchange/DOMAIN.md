# Currency Exchange

Business management for a currency-exchange / money-exchange operation — bureau de change counters and remittance desks — not a crypto trading engine. NACE: K64.99 (other financial service activities n.e.c.; covers currency exchange on own account).

## Maturity: curated

Vertical-specific open-source coverage is thin: a search for bureau-de-change / money-changer / forex-bureau software found no maintained, well-starred project, so the two vertical implementation sources (`bdc-api`, `chfx-odoo-modules`) are hobby- and addon-scale. What carries this domain instead is **authoritative grounding** — FATF, ISO 4217, ISO 20022, the EU AML Regulation and Transfer of Funds Regulation, FinCEN, HMRC, Wolfsberg — plus Apache-2.0 building-block implementations for the parts a bureau shares with payments infrastructure (`blnk` for the ledger, `moov-io/watchman` for screening, `moov-io/ach` and `moov-io/iso20022` for rails). 16 sources, 6 of them authoritative. Four features stay `low` confidence and say so.

## Related but distinct product type
**Crypto exchange** (order books, matching engines, custody, trading pairs — e.g. Bisq, an AGPL-3.0 P2P crypto exchange) is a related but different product: it trades continuously at market-discovered prices with no physical cash, versus a bureau de change's counter-quoted buy/sell rates on physical or bank-transferred cash. Not modeled in this domain; flag explicitly if a request turns out to be a crypto exchange instead.

## Product types
Single-branch or multi-branch bureau de change · remittance/money-transfer counter · exchange desk embedded in a travel/hospitality business.

## Users
Customer · Teller/Cashier · Branch Manager · Compliance Officer · Administrator · System (rate feeds, threshold flags).

## Core workflows
Ten workflows in `workflows.json`, nine with a state machine.
1. **Exchange transaction** — quote a rate → customer accepts → capture ID if above threshold → lock rate, record transaction → update till position → receipt.
2. **Rate quote and expiry** — read rate → apply margin and commission → present an all-in amount with an explicit validity window → accept (convert) or expire. A stale quote is re-quoted, never silently re-priced.
3. **Rate update** — pull/enter a rate → apply spread policy → publish to branches.
4. **Cash session** — open till with a float → transact through the shift → count and reconcile at close.
5. **Customer onboarding and due diligence** — identify → verify document → screen → record purpose and risk rating → activate or hold (FATF R.10; R.6/R.7 for screening).
6. **Screening match review and escalation** — compare against the list entry → disposition false-positive or true match → freeze and stop the pending transaction → escalate, and consider a report.
7. **Outbound remittance** — beneficiary and payout method → screen and attach originator/payee data → quote → collect → transmit → track to payout, or return and refund.
8. **Settlement and reconciliation** — batch per currency → expected position from the ledger → settle over the rail → match the statement → dispute the variance → post to the GL.
9. **Refund and cancellation** — authorise, then post a compensating reversal rather than editing the original; adjust till and commission; both entries stay in the audit trail.
10. **AML report** — auto-flag a transaction crossing a threshold → compliance review → file or dismiss.

## Capabilities
23 features — the authoritative grouping is the generated [`FEATURES.md`](FEATURES.md).
- **Core:** customer management, currency master data, buy/sell rate & spread management, exchange requests/quotes, buy/sell transactions, tills/cash positions, branch management, audit log.
- **Common:** rate-feed ingestion, remittance, beneficiary management, staff management, receipts, settlement & reconciliation, refunds & cancellations, reports & analytics, commission management.
- **Compliance:** KYC transaction thresholds, sanctions/PEP screening, transaction limits, AML suspicious/large-transaction reporting.
- **Optional:** customer notifications, online rate lookup/order-ahead.

Classification is domain knowledge, never scope: a single-branch cash-only bureau needs neither remittance nor settlement batches.

## Compliance-sensitive areas
KYC due-diligence thresholds and AML suspicious/large-transaction reporting trace to FATF Recommendation 20 and the customer-due-diligence recommendations, which most jurisdictions implement by naming currency exchange offices as obliged entities (see EU AMLR/AMLD for one concrete example). **No jurisdiction-specific rule — including any Iranian regulation — is asserted anywhere in this domain**; every compliance item is global/EU-sourced, marked `requires_human_review: true`, and a real deployment must have its own jurisdiction's regulator confirm exact thresholds and filing rules.

## Integrations
Market rate source (e.g. ECB reference rates) · remittance network partner · identity-verification provider (document/liveness checks for CDD) · sanctions/PEP watchlist screening (OFAC SDN and consolidated lists, EU and UN consolidated lists) · bank transfer rail (SEPA, ACH/NACHA, wire/RTGS, ISO 20022 pacs.008 out and camt.053 back) · accounting/general ledger. Vendors are named as examples only, and only screening is classified `compliance`; the rest are `common` and a cash-only counter may use none of them.

## Entities
customer, currency, exchange_rate, exchange_request, exchange_transaction, remittance, beneficiary, screening_match, settlement_batch, till, cash_session, branch, staff, aml_report — see `entities.json`. `beneficiary` is a first-class record rather than fields on a remittance because EU Regulation 2023/1113 requires payee name and account identifier to travel with the transfer.

## UI patterns
Customer: rate board, quote request, transaction receipt. Teller: quick buy/sell ticket, till open/close, ID capture at threshold. Manager/Compliance: rate override, cash-session reconciliation, AML flag queue, branch reports.

## Mobile
Primarily a counter/back-office (web/admin) product; customer-facing mobile is optional (rate lookup, order-ahead) rather than core.

## AI
Limited and assistive only; the domain is rules- and threshold-driven. Realistic opportunities, none of them a requirement and none of them autonomous: AML pattern detection on transaction volume/velocity · screening-match triage to rank likely false positives for a human to disposition · identity-document extraction at onboarding · reconciliation-variance explanation · customer-facing rate/fee explanation. Every compliance decision stays with the compliance officer.

## Standards & terminology
ISO 4217 (currency codes) · ISO 20022 (pacs.008 credit transfer, camt.053 statement) · NACHA ACH file format · FATF Recommendations (R.10 CDD, R.6/R.7 targeted financial sanctions, R.16 wire transfers, R.20 suspicious reporting) · EU Regulation 2024/1624 (AMLR) and 2023/1113 (Transfer of Funds) · FinCEN MSB rules · HMRC MSB guidance · Wolfsberg correspondent-banking guidance · PCI DSS 4.0.1 where cards are taken · FIBO (`std:fibo`, party/transaction terminology).

Terminology: *bureau de change* (counter exchanging physical currency) · *spread* (gap between buy and sell rate) · *margin* (markup over the mid-market rate) · *till/float* (a teller's opening cash per currency) · *CDD/EDD* (customer / enhanced due diligence) · *PEP* (politically exposed person) · *SDN* (OFAC Specially Designated Nationals list) · *travel rule* (originator and payee data accompanying a transfer) · *nostro position* (the firm's balance held at a correspondent bank).

## Sources
16, listed in `feature-map.json` and annotated in `sources.md`. Vertical implementations `bdc-api` (no LICENSE file — pattern reference only, never code) and `chfx-odoo-modules` (license not stated) were inspected over the GitHub API, not cloned. Building-block implementations: `blnk` (Apache-2.0, on disk) for the double-entry ledger and reconciliation, `moov-io/watchman`, `moov-io/ach`, `moov-io/iso20022`, `moov-io/customers` (all Apache-2.0, read over the API, not on disk). Authoritative: FATF, ISO 4217, ISO 20022, EU AMLR 2024/1624, EU TFR 2023/1113, FinCEN, HMRC, Wolfsberg, PCI DSS.
