# Hospitality

Hotel and short-stay lodging operations: property/room/rate setup, availability and reservations, front-desk
check-in/out and folio, and distribution to online travel agencies via a channel manager.
NACE Rev. 2.1: I55.10 (hotels and similar accommodation).

Domain knowledge is a reasoning aid, not a scope list — see `product-builder/PRODUCT-BUILDER.md`.

## Product types
Independent hotels, small hotel groups/chains, B&Bs, and short-stay apartments. The core model (property → room
type → room, rate plan → availability → reservation → folio) applies to all; channel-manager distribution and
multi-property management matter most for chains and OTA-listed independents.

## Users
Guest, front desk agent, housekeeper, revenue manager, property manager (see `roles.json`).

## Core workflows
Reservation lifecycle (request → confirm → check-in → check-out), housekeeping task lifecycle, night audit,
channel ARI (availability/rate/inventory) sync, folio and billing. See `workflows.json` for state machines.

## Capabilities
- **Core**: property management, room types, rooms, rate plans, availability/inventory, reservations, front-desk
  check-in/out.
- **Common**: guest profiles, folio and charges, channel manager/OTA distribution, rate restrictions,
  cancellation/refund policies, deposits and advance payment, amenities, booking voucher/confirmation.
- **Recommended**: add-on services, multi-property management, housekeeping, night audit, group bookings.
- **Optional**: connecting/adjoining rooms, guest loyalty program, guest reviews, dynamic/yield-based pricing.

Full list with classification and sourcing: `FEATURES.md` / `feature-map.json`.

## Compliance-sensitive areas
PCI DSS (card deposits/folio settlement), GDPR (guest identity/contact/stay data, EU-resident guests regardless of
property location), and guest ID/passport registration requirements (illustrative only — varies sharply by
country). See `compliance.json` — domain knowledge, not legal advice; every item requires human review per
deployment.

## Integrations
Channel manager/OTA distribution, payment gateways, guest messaging (email/SMS), ID/passport verification,
accounting software, revenue management systems (RMS). See `integrations.json`.

## Entities
property, room_type, room, rate_plan, rate_restriction, reservation, reservation_room_stay, guest_profile, folio,
payment, deposit, cancellation_policy, channel, amenity, add_on_service, booking_voucher, housekeeping_task,
night_audit_run. See `entities.json`.

## UI patterns
Availability calendar/grid (room type × date), rate-plan/restriction editor, reservation timeline, front-desk
check-in/out board, folio ledger view, housekeeping room-status board, channel connection dashboard.

## Mobile
Front desk / housekeeping tablet apps (room status, task assignment), guest-facing booking and digital
check-in/folio view (phone).

## AI opportunities
No-show prediction, overbooking risk scoring, demand-based dynamic pricing, cleaning-time prediction,
personalized upsell (add-ons, loyalty offers), review sentiment analysis, night-audit reconciliation anomaly
detection. None are implemented in the kit; see `ai_opportunities` per feature.

## Standards referenced
NACE Rev. 2.1 (industry classification). OpenTravel Alliance (OTA) and HTNG define hotel-industry message
specifications for availability/rate/inventory and reservations — **their current specification text is
member/registration-gated** (OTA's public mirror stops at release 2017B; HTNG specs are member/vendor-distributed).
This research verified their organizational status and terminology only, not full message schemas; see
`sources.md` for exactly what was and wasn't verified. Treat any future OTA/HTNG-conformance claim as unverified
until the actual spec text is obtained and read.

## Terminology
PMS = property management system; ARI = availability, rate, inventory (the data pushed to a channel manager);
OTA = online travel agency; folio = a guest's itemized in-stay charge ledger; night audit = the end-of-day
close/reconciliation/date-rollover process; RMS = revenue management system.

## Maturity: partial
24 features, 2 independent open-source implementations cross-referenced (Frappe Hospitality, QloApps) plus 4
authoritative/standards-adjacent sources (PCI DSS, GDPR, OTA, HTNG) and 6 secondary sources. Not `curated`: only
two implementations were available (restaurant research had three), so 11 of 24 features (46%) carry `low`
confidence — folio as a distinct ledger, housekeeping, night audit, add-on services, cancellation rules, channel
manager, connecting rooms, loyalty, reviews, dynamic pricing among them — which fails the `curated` bar's ≤30%
low-confidence ceiling (`tools/kb.py validate`). A third independent property-management implementation is the
missing input. See `sources.md`.

## Relationship to `booking`
Hotel reservations are date-range, capacity-bound bookings — the same shape as `booking.*`'s generic slot/
availability primitives, just with nights instead of time slots. `dependencies.json` records
`hospitality.reservations enhances booking.availability`: a property can implement room-inventory availability
standalone (as both Frappe Hospitality and QloApps do), but could reuse a generic availability engine instead of
duplicating date-range/capacity logic. Not modeled as `requires`, because room-type capacity, rate-plan
restrictions (min-stay, closed-to-arrival), and channel-manager inventory sync are domain-specific enough that a
hospitality product is coherent without the generic engine — mirroring the same judgement made for
`restaurant.reservations`.
