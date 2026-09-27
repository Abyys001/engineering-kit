# Restaurant features

Generated from `feature-map.json` (schema: `domains/_schema/SCHEMA.md`). 25 features.

## Core

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `restaurant.tables` Tables and floor plan | Define dining areas, tables, and seating capacity; visual floor-plan layout with per-table status (available, occupied, reserved, cleaning). | high | medium | low |
| `restaurant.menu` Menu management | Categories, items, prices, and availability windows for a restaurant's sellable menu. | high | low | medium |
| `restaurant.reservations` Table reservations | Book a table for a date/time and party size; capacity and time-window conflict checking. | low | medium | medium |
| `restaurant.dine_in_orders` Dine-in order taking | Capture an order against a table/seat, send to kitchen, and track status through to billing. | high | high | low |
| `restaurant.kitchen_display` Kitchen display system (KDS) | Route order tickets to kitchen stations, track prep status, and flag delayed items in real time. | medium | core | medium |
| `restaurant.payments` In-restaurant payment capture | Charge a table's bill through a payment provider; supports pay-at-table and receipt printing. | high | medium | low |

## Common

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `restaurant.menu_modifiers` Menu modifiers and variants | Add-ons, size options, ingredient substitutions, and combo choices attached to a menu item. | medium | none | none |
| `restaurant.waitlist` Walk-in waitlist | Queue walk-in parties without a reservation; estimated wait time and notify-when-ready. | low | medium | low |
| `restaurant.pos_integration` POS integration | Connect to or embed a point-of-sale system for order capture and payment settlement. | low | medium | none |
| `restaurant.split_bills` Split bills | Divide a table's bill by item, by seat, or evenly across a party. | medium | low | none |
| `restaurant.tips` Tips and gratuity | Capture tip amount at payment and record it against the server/order for payout and reporting. | low | none | none |
| `restaurant.takeout_orders` Takeout / pickup orders | Orders placed for customer pickup rather than dine-in; no table assignment. | low | medium | none |
| `restaurant.delivery_orders` Delivery orders | Orders fulfilled by delivery to a customer address, with own or third-party couriers. | low | medium | low |
| `restaurant.inventory` Ingredient inventory | Track stock levels of ingredients and supplies used to prepare menu items. | low | low | medium |
| `restaurant.recipes` Recipes and yield | Bill-of-materials per menu item: ingredient quantities and yield, used to cost dishes and deplete stock. | low | none | low |
| `restaurant.staff_shifts` Staff shift scheduling | Plan and publish staff work shifts and track clock-in/clock-out. | low | none | low |
| `restaurant.online_ordering` Online ordering | Customer-facing web/app storefront for takeout and delivery ordering against the live menu. | low | low | none |
| `restaurant.menu_allergen_labeling` Allergen and nutrition labelling | Flag allergens and (where required) publish calorie/nutrition information per menu item. | high | none | none |

## Recommended

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `restaurant.third_party_delivery_integration` Third-party delivery marketplace integration | Publish menu and receive orders from delivery marketplaces (e.g. aggregator apps). | low | low | none |
| `restaurant.loyalty` Loyalty and rewards | Points, punch cards, or tiered rewards tied to a guest's order history. | low | none | medium |
| `restaurant.reviews` Customer reviews and ratings | Collect and display post-visit ratings/feedback tied to an order or visit. | low | none | medium |
| `restaurant.qr_code_table_ordering` QR code table ordering | Guests scan a table QR code to view the menu and order from their own device. | low | medium | none |

## Optional

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `restaurant.gift_cards` Gift cards | Sell and redeem stored-value gift cards. | low | none | none |
| `restaurant.self_service_kiosk` Self-service kiosk ordering | In-store kiosk for customers to browse the menu, order, and pay without staff assistance. | low | low | none |
| `restaurant.multi_location_management` Multi-location management | Manage menus, pricing, and reporting across a chain of restaurant locations from one account. | low | none | none |
