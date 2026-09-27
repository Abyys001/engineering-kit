# Currency Exchange sources

Sources cited in this domain's provenance fields.

| ID | Title | Type | License | Retrieved | Local path |
|---|---|---|---|---|---|
| `bdc-api` | [bdc-api (Bureau de Change API)](https://github.com/devmuhammad/bdc-api) | implementation | none found (no LICENSE file; all-rights-reserved by default) | 2026-09-27 | — |
| `chfx-odoo-modules` | [chfx-odoo-modules (Odoo currency-exchange counter modules)](https://github.com/amustafa995-tech/chfx-odoo-modules) | implementation | unknown (not stated in repository; verify before any reuse) | 2026-09-27 | — |
| `fatf-recommendations` | [FATF Recommendations](https://www.fatf-gafi.org/en/topics/fatf-recommendations.html) | authoritative | FATF public standard | 2026-09-27 | — |
| `iso4217` | [ISO 4217 — Currency codes](https://www.iso.org/iso-4217-currency-codes.html) | authoritative | ISO copyright; standard summary freely accessible | 2026-09-27 | — |
| `iso20022` | [ISO 20022 — Universal financial industry message scheme](https://www.iso20022.org/) | authoritative | ISO20022.org terms; message definitions freely published | 2026-09-27 | — |
| `eu-amld` | [EU Anti-Money Laundering Directive / Regulation package](https://eur-lex.europa.eu/eli/reg/2024/1624/oj) | authoritative | EU public law (EUR-Lex) | 2026-09-27 | — |

## Notes

- **`bdc-api`** (): Hobby-scale (1 star) TypeORM/Express API for a bureau de change: currency, daily_rate (buy/sell, official/market), purchase/purchasemain (buy transactions with cash-note serial ranges), selling (sell transactions with transaction_ref, buyingrate/soldrate, KYC fields mode_of_id/id_no/id_expirydate/bvn), users. Inspected via `gh api repos/.../contents` (not cloned; no license to extract under). Single implementation — evidence held at low/medium confidence per feature, never 'industry standard' on its own.
- **`chfx-odoo-modules`** (): Odoo addon modules (`exchange_counter`, `chfx_extension`) with real fields for exchange.branch, exchange.counter (till, linked to an accounting journal and per-currency cash accounts), exchange.session (cashier session on a counter), exchange.transaction (buy/sell with mid_rate vs used_rate vs manual_rate, margin_pct, commission, KYC required/confirmed flags, partner/client link, accounting move), exchange.rate, exchange.remittance. Inspected via `gh api repos/.../contents` (not cloned). Second independent implementation — corroborates branch/counter/session/rate/transaction/remittance as real, separately-modeled concepts.
- **`fatf-recommendations`** (): Recommendation 20 (suspicious transaction reporting) and the customer due diligence recommendations directly govern money-or-value-transfer services and currency exchange offices as 'obliged entities' / DNFBPs in most jurisdictions.
- **`iso4217`** (): Currency code terminology for buy/sell rate pairs and cash positions.
- **`iso20022`** (): Cross-border remittance/payment messaging terminology, used when an exchange house settles or receives via bank rails.
- **`eu-amld`** (Regulation (EU) 2024/1624 + Directive (EU) 2024/1640): Currency exchange offices are named obliged entities under EU AML law; cited generically — no jurisdiction-specific (e.g. Iranian) rule is asserted anywhere in this domain.
