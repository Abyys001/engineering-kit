# Ecommerce

Storefront and merchant-admin platform for selling physical or digital products online: catalog, cart, checkout, orders, payments, shipping, and returns. NACE: G47.91 (retail sale via mail order houses or via internet).

## Product types
Direct-to-consumer webshop · headless commerce (storefront decoupled from admin) · multi-vendor marketplace · B2B ordering portal.

## Users
Customer/Shopper · Merchant Admin · Fulfillment Staff · Support Agent.

## Core workflows
1. **Checkout** — enter address → select shipping → enter payment → review → place order (cart converts to order).
2. **Order lifecycle** — capture payment → allocate inventory → pick/pack → ship → deliver → complete (or cancel).
3. **Return/refund** — customer requests return → merchant approves/rejects → item received → refund issued, stock restocked.

## Capabilities
- **Core:** catalog/product management, categories, inventory, cart, checkout, orders & order state machine, payments, shipping/fulfilment, customer accounts, tax calculation, merchant admin dashboard.
- **Common:** returns/refunds, promotions/discounts, guest checkout, reviews & ratings, storefront search.
- **Recommended:** multi-currency.
- **Optional:** gift cards, wishlist, abandoned-cart recovery, product recommendations, promotion stacking rules, RMA tracking.
- **Premium:** B2B/tiered pricing, multi-vendor marketplace.

## Compliance-sensitive areas
EU Consumer Rights Directive (distance selling: pre-contract info, 14-day withdrawal, refund timelines) on checkout/orders/returns; PCI DSS on checkout/payments (typically satisfied by delegating card capture to a PCI-compliant gateway); GDPR on customer accounts and reviews; VAT/sales tax — rates and thresholds vary by jurisdiction and are **not** asserted for any specific country here. All marked `requires_human_review: true`.

## Integrations
Payment gateway · shipping carrier/fulfillment provider · tax calculation engine · search/indexing engine.

## Entities
product, product_variant, category, inventory_item, cart, cart_line_item, order, order_line_item, payment, shipment, return_request, promotion, customer_account, review, gift_card — see `entities.json`.

## UI patterns
Customer: product listing/detail, faceted search, cart drawer, multi-step checkout, order history/tracking, return request form. Merchant admin: product/variant editor, order queue with status filters, return/refund workspace, promotion builder, sales dashboard.

## Mobile
Storefront (browse/cart/checkout/order tracking) is mobile-first; merchant admin is typically web/tablet, not phone-first.

## AI
Product recommendations and storefront search ranking (`ai_relevance: high`/`medium`) are the most common AI surface; review moderation and catalog attribute extraction are secondary, lower-confidence opportunities.

## Standards & terminology
schema.org `Product`/`Offer`/`Order` vocabulary (authoritative for structured data), GS1 GTIN (product identifiers — distinct from GS1 EPCIS, which is for supply-chain *events* and isn't used here), FIBO (`std:fibo`) not typically relevant to this domain.

## Sources
Medusa (MIT core, Enterprise Edition carved out separately), Saleor (BSD-3-Clause), and Vendure (GPL-3.0 Community Edition — reference-only, never copied) — all inspected via GitHub API (module/entity directory listings), not cloned. See `sources.md`.
