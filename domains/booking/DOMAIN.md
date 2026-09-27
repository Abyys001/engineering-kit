# Booking

Generic appointment and resource scheduling: services, providers/staff or resources, availability rules and
exceptions, time-slot booking with buffers and capacity, recurrence, reminders, cancellation policy, and calendar
sync. NACE Rev. 2.1: N82.99 (other business support service activities, the closest fit for a generic scheduling
capability — this domain is horizontal, not tied to one industry).

Domain knowledge is a reasoning aid, not a scope list — see `product-builder/PRODUCT-BUILDER.md`.

## Product types
Standalone appointment schedulers (consultants, clinics, salons, tutoring), resource-booking systems (meeting
rooms, equipment, vehicles), and the shared scheduling primitive other domains can build on instead of
reimplementing slot/availability logic (see `restaurant.reservations`, `hospitality.reservations`).

## Users
Customer/bookee, provider/staff member, scheduling assistant (secretary), scheduling manager/admin (see
`roles.json`).

## Core workflows
Booking lifecycle (slot selection → confirm/approve → reminder → complete/no-show/cancel), reminder workflow.
See `workflows.json` for state machines.

## Capabilities
- **Core**: services, providers/staff, availability rules (working hours), time-slot computation, bookings.
- **Common**: availability exceptions, buffers, recurring bookings, reminders, cancellation/no-show policies,
  minimum booking notice, calendar sync, out-of-office/blocked time, timezone-aware scheduling.
- **Recommended**: bookable resources (non-human), group bookings/shared capacity, deposits and paid bookings,
  embeddable booking widget/public link, webhooks.
- **Optional**: multi-provider teams/round-robin assignment, manual booking approval, waitlist.

Full list with classification and sourcing: `FEATURES.md` / `feature-map.json`.

## Compliance-sensitive areas
PCI DSS where a deposit/payment is collected at booking time. See `compliance.json` — domain knowledge, not legal
advice; requires human review per deployment. No booking-specific regulation (comparable to food-safety or
lodging-tax rules in the other two domains) was identified; this is a generic capability, not a regulated
industry.

## Integrations
Calendar providers (Google Calendar, Outlook, CalDAV), payment gateways, SMS/email providers, outbound webhooks.
See `integrations.json`.

## Entities
service, provider, resource, schedule, availability_rule, availability_exception, time_slot, booking, attendee,
payment, external_calendar_link, out_of_office_entry, webhook_subscription. See `entities.json`.

## UI patterns
Public booking page (service → provider → date/time picker, timezone-aware), provider availability/working-hours
editor, calendar/agenda view of bookings, booking approval queue.

## Mobile
Provider schedule and booking-approval app (phone), customer-facing booking and reminder view (phone).

## AI opportunities
No-show prediction, smart rescheduling suggestions, load-balanced provider assignment, optimal reminder timing,
waitlist reallocation prediction. None are implemented in the kit; see `ai_opportunities` per feature.

## Standards referenced
RFC 5545 (iCalendar) is the authoritative model for calendar events and recurrence rules (RRULE); cited directly
wherever recurrence or calendar sync is involved. NACE Rev. 2.1 for industry classification, though this domain is
horizontal rather than industry-specific.

## Terminology
Slot = a computed bookable start/end time; buffer = padding time immediately before/after a booking; ARI-style
availability concept here is per-provider/resource rather than per-room-type as in hospitality; no-show = a
confirmed booking where the customer did not attend.

## Maturity: curated
22 features, 2 independent open-source implementations cross-referenced (Cal.diy, Easy!Appointments) plus RFC
5545 and PCI DSS — clears the tool's `curated` bar (≥10 features, ≥3 sources). Not `reviewed`: single research
pass; `resources` (non-human bookable units) and `waitlist` rest on zero corroborating implementations (both
inspected systems are provider/host-centric) and are marked `low` confidence — a genuine gap, not an oversight,
noted in the final report.

## Correction on file: Cal.com license
The task brief's working assumption was `calcom/cal.com` = AGPL, reference-only. Verified from the actual root
`LICENSE` file (2026-09-26): it is **MIT**. The repository's own README identifies it as **Cal.diy**, an
open-source fork of Cal.com with all enterprise/commercial code removed ("100% MIT-licensed... no Open Core
split") — a real, recent restructuring, not a misread. AGPL historically described Cal.com's paid/Enterprise
core, which this repository does not contain. See `sources.md` → `caldiy` for the full note.

## Relationship to `restaurant` and `hospitality`
Both domains model their reservations as capacity-bound, date/time-boxed bookings — the same shape as this
domain's generic scheduling primitives (`booking.availability` + `booking.time_slots`).
`restaurant.reservations` and `hospitality.reservations` each record a `dependencies.json` edge
`enhances booking.availability`: reservations in both domains can and do work standalone (as Frappe Hospitality,
Odoo, URY, and QloApps all demonstrate), but a product could instead build them on top of this domain's generic
slot engine rather than duplicating date/time-window conflict logic. Kept as `enhances`, not `requires`, because
table capacity/combination rules and hotel rate-plan restrictions are domain-specific enough that neither product
is incomplete without the generic engine.
