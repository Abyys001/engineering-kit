# Restaurant

Dine-in, takeout, and delivery food-service operations for a single restaurant or a small chain: floor plan and
reservations, menu and kitchen order flow, point-of-sale payment, and the staff/inventory operations behind them.
NACE Rev. 2.1: I56.10 (restaurants and mobile food service activities).

Domain knowledge is a reasoning aid, not a scope list — see `product-builder/PRODUCT-BUILDER.md`.

## Product types
Full-service (sit-down) restaurants, quick-service/counter restaurants, cafés, food trucks, and ghost/delivery-only
kitchens. The same core model (menu → order → kitchen ticket → bill) covers all four; dine-in-specific pieces
(tables, reservations, waitlist) drop out for counter/delivery-only operations.

## Users
Customer/guest, host, server, kitchen staff, cashier, delivery driver, manager (see `roles.json`).

## Core workflows
Reservation lifecycle, walk-in waitlist, order fulfillment (dine-in/takeout/delivery), kitchen ticket routing,
billing and payment (including split bills), delivery dispatch. See `workflows.json` for state machines.

## Capabilities
- **Core**: tables and floor plan, menu management, table reservations, dine-in order taking, kitchen display
  system (KDS), in-restaurant payment capture.
- **Common**: menu modifiers/variants, walk-in waitlist, POS integration, split bills, tips, takeout orders,
  delivery orders, ingredient inventory, recipes, staff shift scheduling, online ordering, allergen/nutrition
  labelling.
- **Recommended**: loyalty/rewards, customer reviews, QR code table ordering, third-party delivery marketplace
  integration.
- **Optional**: gift cards, self-service kiosk ordering, multi-location management.

Full list with classification and sourcing: `FEATURES.md` / `feature-map.json`.

## Compliance-sensitive areas
PCI DSS (any card payment path), EU Regulation 1169/2011 and US FDA menu labeling (21 CFR 101.11) for allergen/
nutrition disclosure, and tip/labour rules (illustrated with US FLSA, varies sharply by jurisdiction). See
`compliance.json` — domain knowledge, not legal advice; every item requires human review per deployment.

## Integrations
POS terminals, payment gateways, SMS gateways (reservation/waitlist notifications), delivery marketplaces,
accounting software, online reservation platforms, kitchen printer/KDS hardware. See `integrations.json`.

## Entities
restaurant_location, table, guest, reservation, waitlist_entry, menu, menu_item, modifier_group, modifier, order,
order_item, kitchen_ticket, bill, payment, inventory_item, recipe, shift, loyalty_account, review, delivery.
See `entities.json`.

## UI patterns
Visual floor-plan/table-status board (real-time), kitchen display grid by station, POS-style order entry with
modifier drill-down, bill-splitting UI (by item/seat/even share), reservation calendar/timeline.

## Mobile
Server-facing order-taking and table management (tablet/handheld), customer-facing reservation/waitlist status and
online ordering (phone), delivery driver app (phone).

## AI opportunities
No-show prediction (reservations), smart table assignment, prep-time prediction and auto-routing by kitchen
station load, demand forecasting for inventory, menu description generation, review sentiment/summarization.
None are implemented in the kit; see `ai_opportunities` per feature.

## Standards referenced
NACE Rev. 2.1 (industry classification, not acquired locally — `knowledge/standards/standards.json`), PCI DSS,
EU 1169/2011, US 21 CFR 101.11. No restaurant-specific data-interchange standard (equivalent to OTA/HTNG for
hospitality) was identified in this research pass.

## Terminology
KDS = kitchen display system; KOT = kitchen order ticket (printed equivalent of a KDS ticket); "86" = mark an item
unavailable; cover = one seated guest; check/bill = the payable total for a table.

## Maturity: curated
25 features, 3 independent open-source implementations cross-referenced (Frappe Hospitality, Odoo
point_of_sale/pos_restaurant, URY), plus 4 authoritative compliance/standards sources — clears the tool's
`curated` bar (≥10 features, ≥3 sources). Not `reviewed`: single research pass, no second-reviewer pass, and
several features (reservations, waitlist, inventory, recipes, staff shifts, loyalty, reviews, delivery) rest on
one or zero corroborating implementations and are marked `low` confidence accordingly — see `sources.md`.

## Relationship to `booking`
Restaurant reservations are time-boxed, capacity-bound bookings — conceptually the same shape as the generic
`booking.*` primitives (availability, slots, cancellation policy). `dependencies.json` records
`restaurant.reservations enhances booking.availability`: a restaurant can implement date/party-size logic
standalone (as Frappe Hospitality does), but can reuse a generic availability engine instead of duplicating it.
Not modeled as `requires`, because table-capacity/combination logic is domain-specific enough that a restaurant
product is still coherent without the generic engine.
