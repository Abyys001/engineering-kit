# Logistics sources

## Implementations cloned (`sources/domains/<name>/`)

| Source | License | Status | Informed |
|---|---|---|---|
| [Karrio](https://github.com/karrioapi/karrio) (`sources/domains/karrio`) | LGPL-3.0 (root `LICENSE`; `ee/` under separate `LICENSE_EE`, not cloned) | reference-only | Address/Parcel/Commodity/Pickup/Tracking/Shipment/Manifest models and status enums (`modules/manager`, `modules/core`); Order model (`modules/orders`). Shipment fields (rates, selected_rate, carrier snapshot, customs, label/invoice) grounded most of the shipment-, label-, rate-, pickup-, tracking-, and customs-related features and entities. |
| [Fleetbase](https://github.com/fleetbase/fleetbase) (`sources/domains/fleetbase`) | AGPL-3.0 | reference-only | Full DB schema via the repo's own `database.mmd` ERD: orders, payloads, waypoints, routes, drivers, vehicles, fleets, manifests, tracking_statuses, issues, maintenance schedules, service rates/quotes, places, zones. Grounded dispatch, routes, drivers, vehicles, fleet maintenance, fuel tracking, geofencing/zones, exceptions, and proof-of-delivery fields. |

Both are copyleft (LGPL / AGPL): learned from for models and terminology only; no code was or will be
copied into the kit. License verified from each repository's actual root `LICENSE` file, not a README
badge — see each clone's `SOURCE.md`.

## Standards referenced

- `std:gs1-epcis` (GS1 EPCIS 2.0 / CBV) — genuinely relevant for shipment/location identification (SSCC,
  GLN) and event modeling. **Not yet acquired locally** at the time this domain was written (a separate
  standards-acquisition pass was in progress); citations in `entities.json` are marked low-confidence and
  name-only pending acquisition. Re-check `knowledge/standards/gs1-epcis/SUMMARY.md` and tighten the
  `tracking_event` entity's `standard_mapping` (EPCIS event types / CBV business steps) once it exists.
- `std:nace-rev2.1` — used only for the domain's `nace` classification codes, not as a feature source.

## Considered but not used

- **karrio's own PRDs/docs** (`sources/domains/karrio/source` does not include them; excluded by sparse-checkout)
  were not read — only source code under `modules/manager`, `modules/orders`, `modules/core` was inspected.
- **OpenBoxes** (warehouse/supply chain, EPL-1.0) — named in the research brief as a candidate for
  warehouse modeling, but not cloned (the domain's 2-clone budget went to karrio + fleetbase, which cover
  more of the requested feature surface — shipments/rates/carriers and fleet/dispatch — than a
  warehouse-only source would have). `logistics.warehouses` is consequently the domain's weakest-grounded
  feature (low confidence, reasoned only); a future pass should clone OpenBoxes or similar to strengthen it.
- **UN/EDIFACT, UN/CEFACT** — the brief asked to verify genuine relevance; no specific, verifiable feature
  in either cloned source pointed to them, so they were omitted rather than cited on assumption.
