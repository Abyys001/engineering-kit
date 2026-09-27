# Booking features

Generated from `feature-map.json`. See `DOMAIN.md` for narrative context.

## Core

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `booking.services` Services | A bookable offering with a name, duration, and price (e.g. '30-minute consultation'). | high | caldiy, easyappointments |
| `booking.providers` Providers / staff | The person (or team member) who performs a service and owns a schedule. | high | caldiy, easyappointments |
| `booking.availability` Availability rules / working hours | A provider's (or resource's) recurring weekly working hours, from which bookable time slots are derived. | high | caldiy, easyappointments |
| `booking.time_slots` Time slot computation | Derive bookable start times from availability rules, existing bookings, buffers, and slot interval. | high | caldiy, easyappointments |
| `booking.bookings` Bookings / appointments | A confirmed reservation of a service with a provider (and/or resource) for a specific time slot. | high | caldiy, easyappointments |

## Common

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `booking.availability_exceptions` Availability exceptions | One-off overrides to the normal schedule for a specific date: holidays, custom hours, or extra availability. | high | caldiy, easyappointments |
| `booking.buffers` Buffers | Padding time before and/or after a booking during which the provider/resource is not bookable. | medium | caldiy |
| `booking.recurring_bookings` Recurring bookings | Book the same service/slot on a repeating schedule (weekly, monthly) as a linked series. | medium | caldiy, rfc5545 |
| `booking.reminders` Reminders | Automated email/SMS reminders sent ahead of a booking. | medium | caldiy |
| `booking.cancellation_policies` Cancellation and no-show policies | Rules for how and when a booking can be cancelled or rescheduled, and how a no-show is recorded. | medium | caldiy |
| `booking.minimum_notice` Minimum booking notice | A minimum lead time required between booking and the appointment start (blocks last-minute bookings). | low | caldiy |
| `booking.calendar_sync` Calendar sync | Two-way sync of bookings with an external calendar (Google Calendar, Outlook, CalDAV). | high | caldiy, easyappointments, rfc5545 |
| `booking.out_of_office` Out-of-office / blocked time | Mark a provider unavailable for a date range (vacation, sick leave), blocking new bookings. | high | caldiy, easyappointments |
| `booking.timezone_handling` Timezone-aware scheduling | Display and book slots correctly across the customer's and provider's timezones. | high | caldiy, easyappointments, rfc5545 |

## Recommended

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `booking.resources` Bookable resources | A non-human bookable unit (room, equipment, vehicle) with its own availability, alongside or instead of a provider. | low | wikipedia-resource-allocation |
| `booking.buffers_and_group_capacity` Group bookings / shared capacity | Allow multiple attendees to book the same time slot up to a capacity limit (e.g. a class or webinar). | medium | caldiy, easyappointments |
| `booking.deposits` Deposits and paid bookings | Collect a payment or deposit at the time of booking. | medium | caldiy |
| `booking.booking_widget` Embeddable booking widget / public link | A public, shareable booking page or embeddable widget for a service or provider. | medium | caldiy |
| `booking.webhooks` Booking webhooks | Fire outbound events (booking created/cancelled/rescheduled) to external systems. | high | caldiy, easyappointments |

## Optional

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `booking.multi_provider_teams` Teams and round-robin assignment | Assign a booking to one of several providers on a team, by availability, priority, or round robin. | medium | caldiy |
| `booking.booking_confirmation_approval` Manual booking approval | Require a provider or manager to approve a requested booking before it is confirmed. | medium | caldiy |
| `booking.waitlist` Booking waitlist | Let a customer join a waitlist for a fully booked slot and be notified if it opens up. | low | wikipedia-waiting-list |

