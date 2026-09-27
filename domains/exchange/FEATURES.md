# Currency Exchange features

Generated from `feature-map.json`. See `DOMAIN.md` for narrative context.

## Core

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `exchange.customer_management` Customer / Party Management | Maintain walk-in and repeat customer records for an exchange business, including individuals and corporate clients. | medium | chfx-odoo-modules, bdc-api |
| `exchange.currency_master` Currency Master Data | The list of currencies an exchange business trades, with display codes and precision. | high | bdc-api, chfx-odoo-modules, iso4217 |
| `exchange.rate_management` Buy/Sell Rate & Spread Management | Set and update buy and sell rates per currency pair, including the spread margin, either manually or from a rate source. | high | bdc-api, chfx-odoo-modules |
| `exchange.exchange_requests` Exchange Requests / Quotes | A customer or teller requests a quote to buy or sell a currency before committing to the transaction. | medium | bdc-api, chfx-odoo-modules |
| `exchange.buy_sell_transactions` Buy/Sell Transactions | Execute a currency purchase from, or sale to, a customer at a locked-in rate, updating cash positions and the ledger. | high | bdc-api, chfx-odoo-modules |
| `exchange.till_cash_management` Tills / Cash Drawers & Cash Positions | Track each teller's till (cash drawer) balance per currency, opened and closed once per cashier session. | medium | chfx-odoo-modules |
| `exchange.branch_management` Branch Management | Manage physical branch/counter locations a multi-site exchange business operates from. | medium | chfx-odoo-modules |
| `exchange.audit_log` Transaction Audit Log | Immutable, time-stamped record of every rate change, transaction, and cash-session action for later audit. | medium | chfx-odoo-modules |

## Common

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `exchange.rate_feed_ingestion` Rate Source Feed Ingestion | Pull reference/mid-market rates from an external market-data source to seed or sanity-check manual rates. | medium | chfx-odoo-modules |
| `exchange.remittance` Remittance / Money Transfer | Send or receive a cross-border money transfer on behalf of a customer, typically via a remittance network partner. | medium | chfx-odoo-modules |
| `exchange.staff_management` Staff / Teller Management | Manage teller and manager accounts, their assigned branch/till, and shift scheduling. | medium | bdc-api, chfx-odoo-modules |
| `exchange.receipts_payments` Receipts & Payment Vouchers | Print or email a receipt/voucher for a completed exchange or remittance transaction. | low | bdc-api |
| `exchange.reports_analytics` Reports & Analytics | Daily/periodic reports on volume, profit/margin, cash positions, and branch performance. | medium | chfx-odoo-modules |
| `exchange.commission_management` Commission & Fee Management | Configure a commission or flat fee on top of the exchanged amount, per currency, branch, or channel. | medium | chfx-odoo-modules |

## Optional

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `exchange.notifications` Customer Notifications | Notify a customer by SMS/email when a remittance is ready for pickup or a rate alert threshold is hit. | low | chfx-odoo-modules |
| `exchange.online_ordering` Online Rate Lookup / Order-Ahead | Let a customer look up current rates and reserve/order a currency amount online for branch pickup. | low | bdc-api |

## Compliance

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `exchange.kyc_thresholds` KYC with Transaction Thresholds | Require identity capture above a configured transaction-amount threshold, and stronger due diligence above a second, higher threshold. | medium | bdc-api, fatf-recommendations |
| `exchange.aml_reporting` AML Reporting (Suspicious / Large Transaction Reports) | Flag and file suspicious-transaction or large-cash-transaction reports with the relevant authority. | high | fatf-recommendations |

