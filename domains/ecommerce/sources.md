# Ecommerce sources

Sources cited in this domain's provenance fields.

| ID | Title | Type | License | Retrieved | Local path |
|---|---|---|---|---|---|
| `medusa` | [Medusa](https://github.com/medusajs/medusa) | implementation | MIT (core); Enterprise Edition materials under a separate license per ENTERPRISE-LICENSE.md — not used here | 2026-09-27 | — |
| `saleor` | [Saleor](https://github.com/saleor/saleor) | implementation | BSD-3-Clause | 2026-09-27 | — |
| `vendure` | [Vendure](https://github.com/vendure-ecommerce/vendure) | implementation | GPL-3.0 (Vendure Community Edition) — verified from repository LICENSE.md; a paid Vendure Commercial License is the alternative. Reference-only: GPL code is never copied into the kit. | 2026-09-27 | — |
| `schema-org` | [schema.org — Product, Offer, Order](https://schema.org/Product) | authoritative | CC BY-SA 3.0 (schema.org vocabulary) | 2026-09-27 | — |
| `gs1-gtin` | [GS1 GTIN (Global Trade Item Number)](https://www.gs1.org/standards/id-keys/gtin) | authoritative | GS1 published standard | 2026-09-27 | — |
| `eu-crd` | [EU Consumer Rights Directive (CRD)](https://eur-lex.europa.eu/eli/dir/2011/83/oj) | authoritative | EU public law (EUR-Lex) | 2026-09-27 | — |
| `pci-dss` | [PCI DSS](https://www.pcisecuritystandards.org/document_library/) | authoritative | PCI Security Standards Council published standard | 2026-09-27 | — |
| `gdpr` | [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | authoritative | EU public law (EUR-Lex) | 2026-09-27 | — |

## Notes

- **`medusa`** (): Not cloned (893MB monorepo); module list inspected via `gh api repos/medusajs/medusa/contents/packages/modules` (cart, checkout via order, order, payment, product, promotion, pricing, customer, fulfillment, inventory, tax, region, sales-channel, store).
- **`saleor`** (): Not cloned (247MB Django monorepo); top-level app list inspected via `gh api repos/saleor/saleor/contents/saleor` (account, attribute, channel, checkout, discount, giftcard, invoice, order, payment, product, shipping, tax, warehouse, webhook).
- **`vendure`** (): Not cloned (164MB monorepo); core entity list inspected via `gh api repos/vendure-ecommerce/vendure/contents/packages/core/src/entity` (order, order-line, payment, product, product-variant, promotion, shipping-method, stock-level, stock-location, customer, customer-group, channel, zone, tax-rate, fulfillment, refund, surcharge).
- **`schema-org`** (): Authoritative vocabulary for product, offer, and order structured data (also schema.org/Offer, schema.org/Order).
- **`gs1-gtin`** (): Product identifier standard (barcodes/GTIN-13 etc.) for catalog items; distinct from GS1 EPCIS (`std:gs1-epcis`), which is for supply-chain *events* and is not used for plain product identification here.
- **`eu-crd`** (Directive 2011/83/EU): Distance-selling consumer rights: pre-contract information, 14-day withdrawal/return right, refund timelines.
- **`pci-dss`** (4.0.1): Card data handling for checkout/payment capture.
- **`gdpr`** (Regulation (EU) 2016/679): Personal data handling for customer accounts, order history, and marketing consent.
