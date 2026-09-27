# Booking sources

Sources cited in this domain's provenance fields.

| ID | Title | Type | License | Retrieved | Local path |
|---|---|---|---|---|---|
| `caldiy` | [Cal.diy (Cal.com's open-source community edition)](https://github.com/calcom/cal.com) | implementation | MIT | 2026-09-26 | — |
| `easyappointments` | [Easy!Appointments](https://github.com/alextselegidis/easyappointments) | implementation | GPL-3.0 | 2026-09-26 | — |
| `rfc5545` | [RFC 5545 — Internet Calendaring and Scheduling Core Object Specification (iCalendar)](https://www.rfc-editor.org/rfc/rfc5545) | authoritative | IETF Trust — freely usable/implementable per BCP 78/79 | 2026-09-26 | — |
| `wikipedia-no-show` | [Wikipedia: No-show (booking)](https://en.wikipedia.org/wiki/No-show_(booking)) | secondary | CC BY-SA 4.0 | 2026-09-26 | — |
| `pci-dss` | [PCI Data Security Standard v4.0.1](https://www.pcisecuritystandards.org/document_library/) | authoritative | PCI SSC copyright; free to read/download with registration | 2026-09-26 | — |
| `wikipedia-resource-allocation` | [Wikipedia: Resource allocation](https://en.wikipedia.org/wiki/Resource_allocation) | secondary | CC BY-SA 4.0 | 2026-09-26 | — |
| `wikipedia-waiting-list` | [Wikipedia: Waiting list](https://en.wikipedia.org/wiki/Waiting_list) | secondary | CC BY-SA 4.0 | 2026-09-26 | — |

## Notes

- **`caldiy`** (main branch, 2026-09-26 snapshot): Not cloned (monorepo, 1.1GB, exceeds practical clone cost for this pass; inspected via raw.githubusercontent.com Prisma schema). Root LICENSE file verified as MIT, 2026-09-26 — the repository's own README states it is 'Cal.diy', a fork of Cal.com with all enterprise/commercial code removed and '100% MIT-licensed, no Open Core split'. This CORRECTS an initial assumption (carried in the task brief) that calcom/cal.com is AGPL: that historically described Cal.com's paid/Enterprise-Edition core, which is not what this repository now contains. Permissive license means it is not marked reference-only for licensing reasons, though nothing was copied — only entity/field names were read from packages/prisma/schema.prisma (EventType, Booking, Attendee, Host, Schedule, Availability, OutOfOfficeEntry, BookingSeat, BookingReference, Payment, Webhook).
- **`easyappointments`** (main branch, 2026-09-26 snapshot): Not cloned (inspected via raw.githubusercontent.com README + openapi.yml). GPL-3.0 verified from actual LICENSE file. Reference-only, no code copied. Its own OpenAPI contract (openapi.yml) confirms: appointments, availabilities, unavailabilities, customers, services, service_categories, providers, secretaries (a scheduling-on-behalf-of role), working_plan_exceptions, blocked_periods, webhooks. README notes some capabilities (e.g. SMS reminders, deposits) may be gated behind a paid 'premium' tier, not confirmed present in the open-source core — flagged per-feature below.
- **`rfc5545`** (RFC 5545): Authoritative standard for calendar events, recurrence rules (RRULE), and time-zone handling; the canonical reference for recurring bookings and calendar sync/export.
- **`wikipedia-no-show`** (2026-09-26 snapshot): General background for no-show policy; used only where not directly evidenced in the two inspected implementations.
- **`pci-dss`** (4.0.1): Same standard already verified for domains/restaurant and domains/hospitality; applies identically to any booking product collecting card deposits/payments.
- **`wikipedia-resource-allocation`** (2026-09-26 snapshot): General background for non-human bookable resources (rooms, equipment); neither Cal.diy nor Easy!Appointments models a generic resource entity.
- **`wikipedia-waiting-list`** (2026-09-26 snapshot): General background for booking waitlists; not present in either inspected implementation.
