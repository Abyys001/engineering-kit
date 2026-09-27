# Karrio

| Field | Value |
|---|---|
| Source URL | https://github.com/karrioapi/karrio |
| GitHub repository | `karrioapi/karrio` |
| Category | domains/logistics |
| License | LGPL-3.0 — `LICENSE.txt` (verbatim copy of root `LICENSE`). The `ee/` directory (commercial/enterprise add-ons) is governed by a separate `LICENSE_EE` and was **not** cloned. |
| Author / organization | Karrio (karrioapi) |
| Acquired | 2026-09-27 |
| Revision | `deea10f8568b2d48c71bbcc11ec11c62cdaf2a6a` (main) |
| Attribution required | LGPL notice retention if code were reused (it is not — reference-only) |
| Status | reference-only — LGPL-3.0 is on the research brief's copyleft list; learn from it, never copy code into the kit. |

## Useful for
- **Shipment model** (`modules/manager/karrio/server/manager/models.py`, class `Shipment`): embedded JSON
  fields for `shipper`/`recipient`/`parcels`/`customs`/`return_address`/`billing_address`/`selected_rate`/
  `carrier` (snapshot keyed by `carrier_code`), plus `rates` (list of returned quotes), `label`/`invoice`,
  `tracking_number`, `is_return`/`return_shipment`, `order_id`, `applied_fees`. Grounds
  `logistics.shipments`, `logistics.labels`, `logistics.rates_quotes`, `logistics.carriers`,
  `logistics.customs_documents`, `logistics.exceptions_returns`, `logistics.freight_invoicing`.
- **Status enums** (`modules/core/karrio/server/core/serializers.py`): `ShipmentStatus` (draft, created,
  cancelled, shipped, in_transit, delivered, needs_attention, out_for_delivery, delivery_failed),
  `TrackerStatus` (pending, picked_up, unknown, on_hold, cancelled, delivered, in_transit,
  delivery_delayed, out_for_delivery, ready_for_pickup), `PickupStatus` (scheduled, picked_up, cancelled,
  closed). Used verbatim as the state vocabulary for `shipment_lifecycle`, `tracking_and_visibility`, and
  `pickup_scheduling` workflows.
- **Address/Parcel/Commodity/Pickup/Tracking/DocumentUploadRecord/Manifest models**
  (`modules/manager/karrio/server/manager/models.py`) — grounds the `parcel`, `commodity`, `label`,
  `pickup`, `manifest` entities.
- **Order model** (`modules/orders/karrio/server/orders/models.py`), `OrderStatus` (unfulfilled,
  cancelled, fulfilled, delivered, partial) in `modules/orders/karrio/server/orders/serializers/base.py`.
- **TrackingStatus** delivery/signature image URL fields (`core/serializers.py`, class `TrackingStatus`)
  — grounds `logistics.proof_of_delivery`.

## Where things live
- `source/modules/manager/karrio/server/manager/` — Address, Parcel, Commodity, Product, Pickup,
  Tracking, Shipment, DocumentUploadRecord, Manifest models, serializers, views.
- `source/modules/orders/karrio/server/orders/` — Order, OrderCounter, OrderKey models.
- `source/modules/core/karrio/server/core/serializers.py` — all status enums and the large shared
  serializer surface (rating/tracking/shipping request-response shapes).
- `source/LICENSE` — LGPL-3.0. `source/LICENSE_EE` — commercial license for `ee/` (not cloned).

## Known dependencies
- Django + DRF (`modules/manager`, `modules/orders`, `modules/core` are Django apps/serializers).
- Multi-tenant via `MULTI_ORGANIZATIONS` setting (`org` field conditionally included).

## Do not copy
- Any code from `modules/manager`, `modules/orders`, `modules/core` — LGPL-3.0. Reference-only per the
  research brief's license policy.
- The `ee/`, rating, providers/connectors, and dashboard/web app modules were deliberately **not cloned**
  (sparse-checkout limited to `modules/manager`, `modules/orders`, `modules/core`, `LICENSE`,
  `LICENSE_EE`, `README.md`) to stay within the per-clone size budget and focus on the domain model.

## Notes
- This is a genuinely well-modeled multi-carrier shipping platform; the status enums in particular are
  clean, explicit, and directly usable as a state-machine vocabulary (used verbatim in this domain's
  `workflows.json`).
- Confidence throughout this domain's JSON is marked `low` wherever karrio is the *only* source for a
  claim (per the research brief's rule: one source ⇒ low, even when the field is observed directly in
  code) and `medium` where fleetbase independently corroborates the same concept.
- Initial clone attempt used a broad sparse-checkout pattern and ballooned to 333 MB due to partial-clone
  blob fetching; re-cloned from scratch with the narrow `modules/manager` + `modules/orders` +
  `modules/core` pattern set *before* checkout, bringing it down to 4.8 MB.
