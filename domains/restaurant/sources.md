# Restaurant sources

Class, license, and what each source informed. Full records: `feature-map.json` → `sources`.

| ID | Title | Type | License | Local clone | Informed |
|---|---|---|---|---|---|
| `frappe-hospitality` | [Frappe Hospitality](https://github.com/frappe/hospitality) | implementation | GPL-3.0 | sources/domains/frappe-hospitality/source | `dine_in_orders`, `menu`, `multi_location_management`, `payments`, `pos_integration`, `reservations`, `tables`, `tips`, `waitlist` |
| `odoo-pos-restaurant` | [Odoo Point of Sale + Restaurant addons (Community, addons/point_of_sale, addons/pos_restaurant)](https://github.com/odoo/odoo/tree/18.0/addons/pos_restaurant) | implementation | LGPL-3.0 | — | `dine_in_orders`, `kitchen_display`, `menu`, `menu_modifiers`, `payments`, `pos_integration`, `split_bills`, `tables` |
| `ury` | [URY (ERPNext-based restaurant POS + Mosaic KDS)](https://github.com/ury-erp/ury) | implementation | AGPL-3.0 | — | `dine_in_orders`, `kitchen_display`, `loyalty`, `menu`, `menu_modifiers`, `payments`, `pos_integration`, `split_bills`, `tables`, `takeout_orders` |
| `pci-dss` | [PCI Data Security Standard v4.0.1](https://www.pcisecuritystandards.org/document_library/) | authoritative | PCI SSC copyright; free to read/download with registration | — | (compliance/entities/roles/workflows only) |
| `eu-1169-2011` | [EU Regulation No 1169/2011 on food information to consumers (allergen labelling)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32011R1169) | authoritative | EU public document, free reuse per Commission Decision 2011/833/EU | — | `menu_allergen_labeling` |
| `us-fda-menu-labeling` | [US FDA Menu Labeling Requirements (21 CFR 101.11)](https://www.fda.gov/food/food-labeling-nutrition/menu-labeling-requirements) | authoritative | US government work, public domain | — | `menu_allergen_labeling` |
| `us-dol-flsa-tips` | [US DOL Fair Labor Standards Act — tipped employees / tip credit rules](https://www.dol.gov/agencies/whd/flsa) | authoritative | US government work, public domain | — | (compliance/entities/roles/workflows only) |
| `wikipedia-point-of-sale` | [Wikipedia: Point of sale](https://en.wikipedia.org/wiki/Point_of_sale) | secondary | CC BY-SA 4.0 | — | `inventory`, `recipes`, `staff_shifts` |
| `wikipedia-online-food-ordering` | [Wikipedia: Online food ordering](https://en.wikipedia.org/wiki/Online_food_ordering) | secondary | CC BY-SA 4.0 | — | `delivery_orders`, `online_ordering`, `qr_code_table_ordering`, `third_party_delivery_integration` |
| `wikipedia-loyalty-program` | [Wikipedia: Loyalty program](https://en.wikipedia.org/wiki/Loyalty_program) | secondary | CC BY-SA 4.0 | — | `loyalty` |
| `wikipedia-gift-card` | [Wikipedia: Gift card](https://en.wikipedia.org/wiki/Gift_card) | secondary | CC BY-SA 4.0 | — | `gift_cards` |
| `wikipedia-customer-review` | [Wikipedia: Customer review](https://en.wikipedia.org/wiki/Customer_review) | secondary | CC BY-SA 4.0 | — | `reviews` |
| `wikipedia-interactive-kiosk` | [Wikipedia: Interactive kiosk](https://en.wikipedia.org/wiki/Interactive_kiosk) | secondary | CC BY-SA 4.0 | — | `self_service_kiosk` |
| `wikipedia-opentable` | [Wikipedia: OpenTable](https://en.wikipedia.org/wiki/OpenTable) | secondary | CC BY-SA 4.0 | — | (compliance/entities/roles/workflows only) |

## Notes per source

### frappe-hospitality
- Retrieved: 2026-09-26; version: 2003ff8db7d7fbc453a9d14da0f971b9186a0b4b
- Reference-only (GPL-3.0). ERPNext restaurant module: Restaurant, Restaurant Table, Restaurant Menu/Menu Item, Restaurant Reservation, Restaurant Order Entry doctypes. Shared with domains/hospitality.

### odoo-pos-restaurant
- Retrieved: 2026-09-26; version: 18.0 branch
- Not cloned (monorepo, 17GB+, exceeds clone size cap; inspected via raw.githubusercontent.com). addons/ tree is Odoo Community, LGPL-3.0 per root LICENSE; pos_restaurant manifest confirms bill printing, bill splitting, kitchen order printing. Reference-only, no code copied.

### ury
- Retrieved: 2026-09-26; version: main branch, 2026-09-26 snapshot
- Not cloned (inspected via GitHub API + raw FEATURES.md). Confirms visual table layout with drag-drop, table/captain transfer, bill splitting by item or custom split, takeaway order flow, KOT (kitchen order ticket) reprint. Reference-only, no code copied.

### pci-dss
- Retrieved: 2026-09-26; version: 4.0.1
- Card payment security standard; applies to any restaurant accepting card payments.

### eu-1169-2011
- Retrieved: 2026-09-26; version: consolidated text
- EU-jurisdiction allergen/menu information disclosure requirement.

### us-fda-menu-labeling
- Retrieved: 2026-09-26; version: 21 CFR 101.11
- US chain-restaurant calorie/nutrition menu disclosure requirement.

### us-dol-flsa-tips
- Retrieved: 2026-09-26; version: current
- One jurisdiction's example of tip/labor rules; cited as illustrative, not exhaustive — labour law varies sharply by country/state.

### wikipedia-point-of-sale
- Retrieved: 2026-09-26; version: 2026-09-26 snapshot
- General background for POS-adjacent capabilities (inventory, staff, recipes) not found in the three inspected code implementations; not an independent implementation, does not raise confidence above low on its own.

### wikipedia-online-food-ordering
- Retrieved: 2026-09-26; version: 2026-09-26 snapshot
- General background for online ordering, delivery, and QR-code ordering; not an independent implementation.

### wikipedia-loyalty-program
- Retrieved: 2026-09-26; version: 2026-09-26 snapshot
- General background for loyalty/rewards; not an independent implementation.

### wikipedia-gift-card
- Retrieved: 2026-09-26; version: 2026-09-26 snapshot
- General background for stored-value gift cards; not an independent implementation.

### wikipedia-customer-review
- Retrieved: 2026-09-26; version: 2026-09-26 snapshot
- General background for customer review collection; not an independent implementation.

### wikipedia-interactive-kiosk
- Retrieved: 2026-09-26; version: 2026-09-26 snapshot
- General background for self-service kiosk ordering; not an independent implementation.

### wikipedia-opentable
- Retrieved: 2026-09-26; version: 2026-09-26 snapshot
- General background for third-party online reservation platforms; not an independent implementation.
