# Hospitality features

Generated from `feature-map.json`. See `DOMAIN.md` for narrative context.

## Core

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `hospitality.properties` Property management | Define a hotel/property: name, address, policies, and default settings. | medium | frappe-hospitality, qloapps |
| `hospitality.room_types` Room types | Categories of rooms (e.g. Standard, Deluxe, Suite) with capacity and amenities shared across physical rooms. | medium | frappe-hospitality, qloapps |
| `hospitality.rooms` Rooms | Individual physical rooms belonging to a room type, with their own status (active/inactive/out of order). | medium | frappe-hospitality, qloapps |
| `hospitality.rate_plans` Rates and rate plans | Date-ranged pricing per room type (e.g. seasonal rate, non-refundable rate, package rate). | medium | frappe-hospitality, qloapps |
| `hospitality.availability_inventory` Availability and inventory | Real-time count of sellable rooms per room type per date, used to block overselling. | medium | frappe-hospitality, qloapps |
| `hospitality.reservations` Reservations | Book one or more rooms for a date range and guest count; tracks status from request through stay completion. | medium | frappe-hospitality, qloapps |
| `hospitality.front_desk_checkin_checkout` Front desk check-in / check-out | Record a guest's arrival (assign/confirm room, ID capture) and departure (settle folio, release room). | medium | qloapps, frappe-hospitality |

## Common

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `hospitality.guest_profiles` Guest profiles | Guest identity, contact info, preferences, and stay history, reused across reservations. | medium | frappe-hospitality, qloapps |
| `hospitality.folio_and_charges` Folio and charges | Running itemized ledger of room charges, taxes, and incidentals for a stay, settled at checkout. | low | wikipedia-hotel |
| `hospitality.channel_manager` Channel manager / OTA distribution | Push rate, availability, and inventory (ARI) to and pull reservations from online travel agencies. | medium | qloapps, opentravel-alliance, htng |
| `hospitality.rate_restrictions` Rate restrictions | Minimum/maximum length of stay, closed-to-arrival/departure, and blackout-date rules on a rate plan. | low | qloapps |
| `hospitality.cancellation_policies` Cancellation and refund policies | Property- or rate-level rules for how much of a payment is refundable based on how close to arrival a guest cancels. | low | qloapps |
| `hospitality.deposits_advance_payment` Deposits and advance payment | Collect a partial or full payment at booking time, ahead of the stay. | medium | frappe-hospitality, qloapps |
| `hospitality.amenities` Amenities | Named features attached to a property or room type (e.g. Wi-Fi, pool, breakfast included). | medium | frappe-hospitality, qloapps |
| `hospitality.booking_voucher_confirmation` Booking voucher / confirmation | Generate and send a guest-facing confirmation document for a reservation. | low | qloapps |

## Recommended

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `hospitality.add_on_services` Add-on services | Purchasable extras attached to a stay (breakfast, airport transfer, spa) beyond the room rate. | low | qloapps |
| `hospitality.multi_property_management` Multi-property management | Manage room types, rates, and reservations across a group of properties from one account. | medium | frappe-hospitality, qloapps |
| `hospitality.housekeeping` Housekeeping | Track room cleaning/turnover status (dirty, cleaning, clean, inspected) and assign housekeeping tasks. | low | wikipedia-housekeeping |
| `hospitality.night_audit` Night audit | End-of-day process that posts room charges, reconciles payments, and rolls the business date forward. | low | wikipedia-night-audit |
| `hospitality.group_bookings` Group bookings | Reserve a block of multiple rooms under one booking for an event, family, or corporate group. | medium | frappe-hospitality, qloapps |

## Optional

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `hospitality.connecting_rooms` Connecting / adjoining rooms | Model and offer physically connected rooms as a unit for families or groups. | low | qloapps |
| `hospitality.loyalty_program` Guest loyalty program | Points, tiers, or member rates tied to a guest's stay history. | low | wikipedia-loyalty-program |
| `hospitality.guest_reviews` Guest reviews | Collect and display post-stay ratings and feedback. | low | wikipedia-customer-review |
| `hospitality.dynamic_pricing` Dynamic / yield-based pricing | Adjust room rates automatically based on demand, occupancy forecast, or competitor pricing. | low | wikipedia-yield-management |

