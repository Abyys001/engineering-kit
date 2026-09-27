# Ecommerce features

Generated from `feature-map.json`. See `DOMAIN.md` for narrative context.

## Core

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `ecommerce.catalog_management` Catalog / Product Management | Create and maintain products with variants, options, media, and attributes. | high | medusa, saleor, vendure, schema-org |
| `ecommerce.category_navigation` Categories / Collections | Organize products into browsable categories or curated collections. | high | medusa, saleor, vendure |
| `ecommerce.inventory_management` Inventory Management | Track stock levels per variant and location, reserve stock on order, and release it on cancellation. | high | medusa, saleor, vendure |
| `ecommerce.cart` Shopping Cart | Let a shopper accumulate items, adjust quantities, and apply a promotion code before checking out. | high | medusa, saleor, vendure |
| `ecommerce.checkout` Checkout | Collect shipping/billing details, shipping method, and payment, then convert a cart into an order. | high | medusa, saleor, vendure |
| `ecommerce.order_management` Orders & Order State Machine | Track an order through payment, fulfillment, and completion, or cancellation/return, as the single source of truth for what was sold. | high | medusa, saleor, vendure, schema-org |
| `ecommerce.payments` Payments | Authorize, capture, and refund payment for an order through one or more payment providers. | high | medusa, saleor, vendure |
| `ecommerce.shipping_fulfillment` Shipping & Fulfilment | Choose a shipping method/rate at checkout, then pack and ship the order via a fulfillment provider or in-house. | high | medusa, saleor, vendure |
| `ecommerce.customer_accounts` Customer Accounts | Let a shopper register, sign in, and view their order history, addresses, and saved payment methods. | high | medusa, saleor, vendure |
| `ecommerce.tax_calculation` Tax Calculation | Compute VAT/sales tax per line item based on customer location, product tax class, and jurisdiction rules. | high | medusa, saleor, vendure |
| `ecommerce.merchant_admin` Merchant Admin Dashboard | Back-office console for managing catalog, orders, customers, and store settings. | high | medusa, saleor, vendure |

## Common

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `ecommerce.returns_refunds` Returns & Refunds | Let a customer request a return or exchange for a delivered order, and process the refund once received. | high | medusa, saleor, vendure |
| `ecommerce.promotions_discounts` Promotions & Discounts | Configure percentage/fixed discounts, coupon codes, and automatic promotions with eligibility rules. | high | medusa, saleor, vendure |
| `ecommerce.guest_checkout` Guest Checkout | Let a shopper complete an order without creating an account. | medium | medusa, saleor |
| `ecommerce.reviews_ratings` Reviews & Ratings | Let a verified purchaser leave a rating and written review on a product. | low | saleor |
| `ecommerce.storefront_search` Storefront Search | Let a shopper search and filter the catalog by keyword, category, price, and attribute facets. | medium | medusa, saleor |

## Recommended

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `ecommerce.multi_currency` Multi-Currency | Display prices and accept payment in more than one currency, with per-currency price lists or live FX conversion. | medium | medusa, vendure |

## Optional

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `ecommerce.gift_cards` Gift Cards | Sell a stored-value gift card that a recipient can redeem toward a future order. | medium | saleor, medusa |
| `ecommerce.wishlist` Wishlist / Saved Items | Let a shopper save products to a list to revisit or share later. | low | saleor |
| `ecommerce.abandoned_cart_recovery` Abandoned Cart Recovery | Detect a cart left inactive and prompt the shopper by email/notification to complete checkout. | low | medusa |
| `ecommerce.product_recommendations` Product Recommendations | Surface related, similar, or personalized product recommendations on product and cart pages. | low | medusa |
| `ecommerce.discount_stacking_rules` Promotion Eligibility & Stacking Rules | Define whether multiple promotions can combine on one order and in what priority. | medium | vendure |
| `ecommerce.order_returns_rma_tracking` RMA Tracking | Track a return-merchandise-authorization shipment back to the warehouse with a carrier tracking number. | low | saleor |

## Premium

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `ecommerce.b2b_pricing` B2B / Tiered Pricing | Offer customer-group- or quantity-based price lists distinct from public retail pricing. | medium | vendure |
| `ecommerce.marketplace_multi_vendor` Multi-Vendor Marketplace | Let multiple independent sellers list products on one storefront, with per-vendor order splitting and payout. | low | medusa |

