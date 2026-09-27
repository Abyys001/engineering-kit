# Fintech sources

Class, license, and what each source informed. Everything here is data inspected for domain-knowledge research, never instructions, and (per the research brief) never copied into the kit unless explicitly marked otherwise.

| ID | Title | Type | License | Retrieved | Cloned? |
|---|---|---|---|---|---|
| `blnk` | [Blnk](https://github.com/blnkfinance/blnk) | implementation | Apache-2.0 | 2026-09-27 | yes — `sources/domains/blnk/source` |
| `apache-fineract` | [Apache Fineract](https://github.com/apache/fineract) | implementation | Apache-2.0 | 2026-09-27 | no (inspected via API/web only) |
| `formance-ledger` | [Formance Ledger](https://github.com/formancehq/ledger) | implementation | MIT | 2026-09-27 | no (inspected via API/web only) |
| `iso20022` | [ISO 20022 — Universal financial industry message scheme](https://www.iso20022.org/) | authoritative | ISO20022.org terms; message definitions freely published | 2026-09-27 | no (inspected via API/web only) |
| `iso4217` | [ISO 4217 — Currency codes](https://www.iso.org/iso-4217-currency-codes.html) | authoritative | ISO copyright; standard summary freely accessible | 2026-09-27 | no (inspected via API/web only) |
| `iso13616-iban` | [ISO 13616 / IBAN Registry](https://www.swift.com/standards/data-standards/iban) | authoritative | Published by SWIFT under ISO 13616 | 2026-09-27 | no (inspected via API/web only) |
| `fatf-recommendations` | [FATF Recommendations](https://www.fatf-gafi.org/en/topics/fatf-recommendations.html) | authoritative | FATF public standard | 2026-09-27 | no (inspected via API/web only) |
| `eu-amlr` | [EU Anti-Money Laundering Regulation (AMLR)](https://eur-lex.europa.eu/eli/reg/2024/1624/oj) | authoritative | EU public law (EUR-Lex) | 2026-09-27 | no (inspected via API/web only) |
| `us-bsa` | [Bank Secrecy Act (BSA)](https://www.fincen.gov/resources/statutes-regulations/bank-secrecy-act) | authoritative | US public law, FinCEN-administered | 2026-09-27 | no (inspected via API/web only) |
| `eu-psd2` | [EU Payment Services Directive 2 (PSD2)](https://eur-lex.europa.eu/eli/dir/2015/2366/oj) | authoritative | EU public law (EUR-Lex) | 2026-09-27 | no (inspected via API/web only) |
| `pci-dss` | [PCI DSS](https://www.pcisecuritystandards.org/document_library/) | authoritative | PCI Security Standards Council published standard | 2026-09-27 | no (inspected via API/web only) |
| `gdpr` | [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | authoritative | EU public law (EUR-Lex) | 2026-09-27 | no (inspected via API/web only) |

## Notes

- **blnk**: Cloned (sparse). Double-entry ledger: Ledger, Balance, Account, Transaction, Identity, reconciliation engine.
- **apache-fineract**: Not cloned (124MB Java monorepo); top-level package structure inspected via `gh api repos/apache/fineract/contents/...` (accounting, portfolio, organisation, useradministration, batch, cob). Core banking platform used by microfinance/neobank deployments.
- **formance-ledger**: Not cloned; repository layout inspected via `gh api repos/formancehq/ledger/contents`. Programmable double-entry ledger service, corroborates the ledger/account/transaction split seen in Blnk.
- **iso20022**: Terminology for payments, parties, and financial messaging (pain/pacs/camt message families).
- **iso4217**: Currency code terminology for multi-currency ledger/wallet balances.
- **iso13616-iban**: International Bank Account Number structure, referenced for account numbering.
- **fatf-recommendations**: The 40 Recommendations — global AML/CFT baseline (customer due diligence, suspicious transaction reporting).
- **eu-amlr**: Part of the 2024 EU AML package (with Directive (EU) 2024/1640 and the new AMLA authority), replacing the AMLD4/5/6 patchwork for directly-applicable rules; phased applicability through 2027 — verify current stage before relying on it.
- **us-bsa**: US AML/CTF statute: CDD, CTRs, SARs.
- **eu-psd2**: Strong Customer Authentication (SCA) and open-banking access-to-account rules. A PSD3 directive plus a Payment Services Regulation (PSR) were proposed by the European Commission in 2023 to succeed/complement PSD2; their legislative status changes and must be re-checked before relying on it.
- **pci-dss**: Card data handling requirements for card issuing/payments.
- **gdpr**: Personal data handling for party/KYC records.

Standards referenced via the global registry (`knowledge/standards/standards.json`): `std:fibo` (terminology only; acquisition status tracked there, not here).
