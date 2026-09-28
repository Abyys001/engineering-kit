# Logistics

Shipping, delivery, third-party logistics (3PL), and fleet/dispatch operations: rating and booking
shipments across carriers, planning and dispatching routes, tracking parcels and vehicles in real
time, and capturing proof of delivery. NACE Rev. 2.1: H49.41 (freight transport by road), H52.10
(warehousing), H52.29 (other transportation support), H53.10/H53.20 (postal and courier activities).

## Product types

- Multi-carrier shipping platforms (rate shopping, label purchase, tracking) — e.g. shipping APIs/aggregators.
- Fleet and last-mile dispatch platforms — driver/vehicle management, route planning, delivery execution.
- 3PL / courier operations combining both: warehouse-to-door fulfillment with owned or contracted fleets.

## Users

Shipper/customer (books and tracks), dispatcher (plans and assigns), driver (executes via mobile app),
warehouse staff, fleet manager, operations manager, customer support agent, external carrier/vendor,
and an automated system actor for webhook/telemetry ingestion. See `roles.json`.

## Core workflows

1. **Order to shipment** — a customer order is converted into one or more shipments.
2. **Shipment lifecycle** — rate shopping → label purchase → carrier hand-off → transit → delivery.
3. **Tracking and visibility** — carrier/telematics events are normalized into a live timeline.
4. **Dispatch and route planning** — orders are batched, sequenced into a route, and assigned to a driver/vehicle.
5. **Pickup scheduling**, **proof of delivery capture**, **exception and returns handling**, **fleet maintenance scheduling**.
6. **Warehouse fulfillment** — receive → put away → pick → pack → stage → carrier hand-off (GS1 CBV bizSteps).
7. **Carrier manifest close-out**, **customs export declaration**, **customer onboarding and rate setup**.
8. **Vehicle telemetry, geofencing, and driver scoring**; **load planning and ETA**; **freight settlement and claims**.

See `workflows.json` for full steps and state machines (11 of 15 workflows now carry one).

## Capabilities by classification

- **Core**: customers/shippers, orders, shipments, rates & quotes, carriers, labels, dispatch, routes,
  drivers, vehicles, proof of delivery.
- **Common**: parcels, manifests, pickups, warehouses & locations, exceptions & returns, driver mobile app.
- **Recommended**: customs documents, geofencing/zones, fleet maintenance, address validation, contract rates.
- **Optional/premium**: claims, fuel tracking, cash on delivery, ETA prediction, driver scoring, load
  planning, freight invoicing/audit.

Full list with descriptions: `FEATURES.md` / `feature-map.json`.

## Compliance-sensitive areas

Driver hours-of-service (US FMCSA 49 CFR Part 395; EU Regulation 561/2006), dangerous goods (ADR 2025 for
road, IATA DGR 67th Ed. for air, IMDG Code 2024 Ed. for sea), and customs/import-export declarations
(WCO Data Model 4.3.0, Incoterms 2020). All are jurisdiction-specific, `requires_human_review: true`, and
are **not** implemented by either reference source inspected here. See `compliance.json`. Citing a
standard here never means a product built from this domain is compliant.

## Integrations

Carrier APIs (rate/label/tracking), inbound webhook receivers, e-commerce platforms (order import),
mapping/geocoding (routing, geofencing, ETA), vehicle telematics, fuel card providers, payment gateways
(COD), customs broker/clearance APIs. See `integrations.json`.

## Entities

customer, order, shipment, parcel, commodity, label, carrier, carrier_service, rate_quote, manifest,
pickup, tracking_event, proof_of_delivery, dispatch_assignment, route, waypoint, place, driver, vehicle,
fleet, warehouse, exception, return, customs_document, zone, maintenance_record. See `entities.json`.

## UI patterns

Rate comparison table, label/document preview and print, live tracking timeline with map, dispatch
board (unassigned/assigned/en-route columns), route map with sequenced stops, exception queue,
driver mobile stop list with capture screens.

## Mobile

Driver mobile app is core to fleet/last-mile operations: offline-tolerant stop list, turn-by-turn
navigation hand-off, status updates, and photo/signature proof-of-delivery capture with queued upload.

## AI opportunities

Route optimization, dynamic ETA prediction, carrier/service auto-selection, exception auto-triage,
HS-code suggestion, driving-behavior anomaly detection. Real-time relevance is high across tracking,
dispatch, and the driver app — see individual features' `real_time_relevance`.

## Standards

- **GS1** — EPCIS 2.0 / CBV (`std:gs1-epcis`, acquired on disk) for supply-chain event visibility
  (what/when/where/why) and the CBV business-step vocabulary used for parcel/warehouse states; General
  Specifications (`gs1-general-specifications`, release 26.0) for GTIN, SSCC, GS1-128 Application
  Identifiers, and the GLN used to identify locations.
- **UPU S10** (`upu-s10`) — 13-character international postal item identifier.
- **UN/EDIFACT** IFTMIN/IFCSUM (`uncefact-iftmin-ifcsum`) — shipper-to-carrier transport instruction and
  forwarding/consolidation summary messages; exact current UNTDID release not pinned. **UN/CEFACT** Multi-
  Modal Transport Reference Data Model (`uncefact-mmt-rdm`) — multi-leg consignment data structures.
  ASC X12 204/990/214/210 (`x12-transportation`, secondary — official X12.org text not accessed) — motor
  carrier load tender / response / status / invoice.
- **IATA** e-AWB (Resolution 672) and Cargo-XML (`iata-eawb-cargoxml`) for air freight; **Incoterms 2020**
  (ICC, `incoterms-2020`) for delivery/cost responsibility transfer; **WCO Data Model 4.3.0**
  (`wco-data-model`) for customs declarations.
- **Dangerous goods** (compliance-only, never a feature): ADR 2025 (road), IATA DGR 67th Edition (air),
  IMDG Code 2024 Ed./Amdt 42-24 (sea) — see `compliance.json`.
- **NACE Rev. 2.1** — industry classification only; used for the domain's `nace` codes, not as a feature
  source.

## Terminology

- **POD** — Proof of delivery (photo/signature captured at the delivery stop).
- **Manifest** — either a carrier close-out batch of shipments, or a driver's route manifest of stops
  (the two cloned sources use the term for different but related things — see `entities.json`).
- **Waypoint** — a single stop (pickup, dropoff, or return) within a route.
- **HOS** — Hours of service (driver duty-time regulation).
