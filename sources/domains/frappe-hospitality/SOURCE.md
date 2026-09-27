# Frappe Hospitality

| Field | Value |
|---|---|
| Source URL | https://github.com/frappe/hospitality |
| GitHub repository | `frappe/hospitality` |
| Category | domains/restaurant, domains/hospitality (shared) |
| License | GPL-3.0 — `LICENSE.txt` (verbatim copy of root `license.txt`) |
| Author / organization | Frappe Technologies Pvt. Ltd. |
| Acquired | 2026-09-26 |
| Revision | `2003ff8db7d7fbc453a9d14da0f971b9186a0b4b` (develop) |
| Attribution required | Copyleft — full GPL-3.0 obligations (source availability, same license) if distributed |
| Status | **reference-only** — GPL-3.0; DocType JSON models and workflow structure inform domain knowledge only, no code or JSON schema copied into the kit |

## Useful for
- ERPNext's Hospitality module covers two sub-domains in one app: `hospitality/hotels/` (hotel room inventory, pricing, reservations) and `hospitality/restaurant/` (restaurant, tables, menu, order entry, reservation) — confirms both restaurant and hospitality domains share a lineage and terminology.
- DocType JSON files under `*/doctype/*/*.json` are Frappe's entity models: field lists, `Link` fields show relationships (foreign keys), `Select` fields enumerate lifecycle states, `Table` fields are child/line-item tables (one-to-many).
- Hotel side: `Hotel Room` (belongs to `Hotel Room Type`), `Hotel Room Type` (has `Hotel Room Amenity` line items), `Hotel Room Pricing` (date-ranged rate plan with `Hotel Room Pricing Item`/`Hotel Room Pricing Package` line items — i.e. a rate plan per room type per date range), `Hotel Room Reservation` (guest/customer, date range, `status`: Booked → Advance Paid → Invoiced → Paid → Completed / Cancelled, line items = `Hotel Room Reservation Item` per room), `Hotel Settings` (property-level defaults).
- Restaurant side: `Restaurant` (property; default customer/tax template/menu), `Restaurant Table` (seats, minimum seating, belongs to restaurant), `Restaurant Menu`/`Restaurant Menu Item` (menu = priced item list against a Price List), `Restaurant Reservation` (`status`: Open → Waitlisted/Cancelled/No Show/Success, party size, time window, contact), `Restaurant Order Entry`/`Restaurant Order Entry Item` (dine-in order tied to a table, generates a Sales Invoice).
- Reservation and order flows are built on ERPNext's generic `Customer`, `Item`, `Price List`, `Sales Invoice`, `Sales Taxes and Charges Template` — i.e. hospitality/restaurant-specific DocTypes are a thin layer over a generic ERP core, not a self-contained domain model.
- `hotel_room_occupancy` report (`hospitality/hotels/report/`) confirms occupancy reporting as a real feature, not just inference.

## Where things live
- `source/hospitality/hotels/doctype/` — hotel room, room type, room amenity, room pricing (+ items/packages), room reservation (+ items), hotel settings.
- `source/hospitality/restaurant/doctype/` — restaurant, restaurant table, restaurant menu (+ items), restaurant reservation, restaurant order entry (+ items).
- `source/hospitality/hospitality/doctype/` — duplicate/legacy copy of the same DocTypes at the module root (older module layout kept alongside the newer `hotels/`/`restaurant/` split; both present in this checkout).
- `source/hospitality/hotels/report/hotel_room_occupancy/` — server report script + query.
- `source/README.md` — module scope statement ("Hospitality module ... handle workflows for Hotels and Restaurants").

## Known dependencies
- Frappe Framework + ERPNext (this app installs into an existing ERPNext/Frappe bench; not standalone). Depends on ERPNext core DocTypes: `Customer`, `Item`, `Price List`, `Sales Invoice`, `Company`, `Address`, `Currency`, `Sales Taxes and Charges Template`.

## Do not copy
- No code, DocType JSON, or field/schema definitions are copied into the kit (GPL-3.0, reference-only). Used only to identify feature names, entity relationships, and lifecycle states for `domains/restaurant/` and `domains/hospitality/` knowledge files, which are original writing.

## Notes
- Small app (70 KB repo size) — essentially a thin ERPNext add-on, not a full standalone restaurant/hotel system. Treated as one implementation signal among several, not sole authority; cross-referenced with other open-source systems per domain before marking any feature `high` confidence.
- Two parallel doctype trees (`hospitality/hospitality/doctype/` and `hospitality/hotels/`+`hospitality/restaurant/`) contain identical DocTypes — a mid-refactor module split left both in the repo at this commit.
- Shallow, blobless sparse checkout (`--filter=blob:none`, tracked paths only); no `.claude/`/`AGENTS.md`/CI-instruction files were present to exclude.
