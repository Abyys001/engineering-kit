# FIBO summary

Financial Industry Business Ontology, EDM Council. Full spec: `SOURCE.md` (MIT, SHA `08322e9`, version 20260701). All classes below carry `hasMaturityLevel = Release` (not provisional) unless noted.

## Domain modules (one line each)

| Module | Purpose |
|---|---|
| **FND** (Foundations) | General-purpose concepts underpinning every other module: agreements, parties, accounting, currency/monetary amounts, dates, places, arrangements, organizations, products and services. |
| **BE** (Business Entities) | Legal-entity concepts for data governance and regulatory reporting: corporations, partnerships, sole proprietorships, trusts, government entities, ownership/control structures. |
| **FBC** (Financial Business and Commerce) | Business concepts shared across finance domains: financial products/services, client & account relationships, market/exchange infrastructure, financial instruments. |
| **SEC** (Securities) | Concepts common to securities generally plus equities and debt instruments; securities identification schemes. |
| **DER** (Derivatives) | Options, futures, forwards, swaps and other derivative instruments, including currency and commodity derivative contracts. |
| **IND** (Indices and Indicators) | Market indices, reference rates, economic indicators, **foreign exchange**, interest rates. |
| **LOAN** | Concepts common to loans (commercial, small-business, auto, education, mortgage), including card accounts. |
| **BP** (Business Process) | Financial process/workflow ontologies, e.g. securities issuance. |
| **CAE** (Corporate Actions and Events) | Events during a security's life: offerings, splits, dividends, etc. |
| **MD** (Market Data) | Temporally-variant data for instruments, loans, funds (i.e. market-data time series shape). |
| **ACTUS** | Algorithmic contract types (ACTUS taxonomy) mapped onto FIBO contract terms. |
| **EXMP** | Reference/example individuals (e.g. named financial institutions) used for testing, not part of the TBox. |

## Key classes for a fintech app / currency-exchange business

| Concept | Class / file |
|---|---|
| Currency | `FND/Accounting/CurrencyAmount.rdf` (Currency class + ISO 4217 compliance); individuals in `FND/Accounting/ISO4217-CurrencyCodes.rdf` |
| Monetary amount | `FND/Accounting/CurrencyAmount.rdf` - distinguishes concrete "money amount" from abstract "monetary amount" |
| Account | `FBC/ProductsAndServices/ClientsAndAccounts.rdf` (client/account relationship); `LOAN/LoansSpecific/CardAccounts.rdf` for card accounts; `FND/Accounting/AccountingEquity.rdf` for the accounting-equity side |
| Party / customer | `FND/Parties/Parties.rdf` (base Party concept); `FND/AgentsAndPeople/Agents.rdf` for agent/person roles; `BE/*` for the legal-entity form a corporate customer takes |
| Financial service provider | `EXMP/LegalEntities/FinancialInstitutionExamples.rdf` (worked examples); the general concept lives under `FBC/ProductsAndServices/` product/service classes |
| Payment | `FND/ProductsAndServices/PaymentsAndSchedules.rdf` |
| Exchange rate | `IND/ForeignExchange/ForeignExchange.rdf` - the FX/exchange-rate concepts live in the **Indices and Indicators** module, not FBC |
| Transaction / contract | `FND/Agreements/Contracts.rdf` (general contract); `ACTUS/ACTUSContractTerms.rdf` + `ACTUSContractTermMapping.rdf` for algorithmic contract-term detail; `DER/DerivativesContracts/CurrencyContracts.rdf` for FX derivative contracts specifically |
| KYC-related identifiers | `SEC/Securities/SecuritiesIdentification.rdf` and `SecuritiesIdentificationIndividuals.rdf` (identifier schemes); `FND/Arrangements/IdentifiersAndIndices.rdf` for general identifier/index patterns. FIBO has no single dedicated "KYC" module - identity/identifier concepts are distributed across `FND/Parties`, `FND/Arrangements`, and `SEC/Securities` identification files; assemble a KYC data model from these rather than expecting one canonical class. |

## Notes

- No provisional-maturity classes were found among the files checked above; all inspected `hasMaturityLevel` annotations resolved to `Release`. If pulling additional classes, check each file's `owl:Ontology` header for `fibo-fnd-utl-av:hasMaturityLevel` before treating it as stable.
- `etc/source/` (Cameo/Sparx binary model files, ~62 MB) was excluded from the local checkout - not needed for RDF consumption and violates the "no large bundles" acquisition rule.
