# InvenTree

| Field | Value |
|---|---|
| Source URL | https://github.com/inventree/InvenTree |
| GitHub repository | `inventree/InvenTree` |
| Category | domains/manufacturing |
| License | MIT — `LICENSE.txt` (verbatim copy of root `LICENSE`) |
| Author / organization | InvenTree Developers |
| Acquired | 2026-09-27 |
| Revision | `ba848a83aa95bc897ddec9a2a64b270ab464819b` (master) |
| Attribution required | MIT notice retention if code were reused (it is not in this pass — reference-only) |
| Status | reference-only for this domain-knowledge pass (see `sources.md` for why it was not promoted despite the permissive license) |

## Useful for
- **Part model** (`src/backend/InvenTree/part/models.py`, class `Part`): `IPN`, `revision`,
  `is_template`/`variant_of`, `assembly`/`component`/`trackable`/`testable`/`purchaseable`/`salable`/
  `consumable`/`virtual` boolean flags, `minimum_stock`, `units`. Grounds `manufacturing.items_products`,
  `manufacturing.product_variants`.
- **BomItem / BomItemSubstitute** (same file) — grounds `manufacturing.bill_of_materials`,
  `manufacturing.bom_substitutes`.
- **PartTestTemplate / StockItemTestResult** — grounds `manufacturing.quality_inspections`.
- **PartStocktake** — grounds `manufacturing.stocktake_cycle_counting`.
- **StockItem** (`src/backend/InvenTree/stock/models.py`): `serial`, `batch`, `quantity`, `is_building`,
  `purchase_order`/`sales_order` links, `expiry_date`, `stocktake_date`. **StockStatus** enum (OK,
  ATTENTION, DAMAGED, DESTROYED, REJECTED, LOST, QUARANTINED, RETURNED) and **StockHistoryCode** (a much
  longer append-only audit-trail enum including `INSTALLED_CHILD_ITEM`/`REMOVED_CHILD_ITEM`/
  `DISASSEMBLED`/`CREATED_FROM_DISASSEMBLY`/`BUILD_OUTPUT_COMPLETED`/`BUILD_OUTPUT_REJECTED`) — grounds
  `manufacturing.inventory_lots_serials`, `manufacturing.traceability`, `manufacturing.disassembly_unbuild`,
  `manufacturing.non_conformance_management` (reasoned), `manufacturing.production_scrap_tracking` (reasoned).
- **StockLocation / StockLocationType** — grounds `manufacturing.stock_locations`.
- **Build / BuildLine / BuildItem** (`src/backend/InvenTree/build/models.py`): `reference`, `title`,
  `quantity`, `parent` (sub-builds), `sales_order`, `take_from`/`destination` locations, `batch`,
  `creation_date`/`start_date`/`target_date`/`completion_date`, `completed_by`/`issued_by`/`responsible`,
  `project_code`, `external` (subcontract flag). **BuildStatus** enum (PENDING, PRODUCTION, ON_HOLD,
  CANCELLED, COMPLETE) — grounds `manufacturing.production_orders`, `manufacturing.subcontracting`.
- **order app** `PurchaseOrderStatus`/`SalesOrderStatus`/`ReturnOrderStatus`/`TransferOrderStatus` enums
  (`src/backend/InvenTree/order/status_codes.py`) — grounds `manufacturing.purchase_orders`.
- **company app** (cloned but not deeply inspected beyond confirming Company/SupplierPart/
  ManufacturerPart models exist) — grounds `manufacturing.supplier_management`.

## Where things live
- `source/src/backend/InvenTree/part/` — Part, BomItem, PartTestTemplate, PartStocktake, and related models.
- `source/src/backend/InvenTree/stock/` — StockItem, StockLocation, StockItemTracking, StockItemTestResult.
- `source/src/backend/InvenTree/build/` — Build, BuildLine, BuildItem, `status_codes.py` (BuildStatus).
- `source/src/backend/InvenTree/order/` — PurchaseOrder/SalesOrder/ReturnOrder/TransferOrder models and
  `status_codes.py`.
- `source/src/backend/InvenTree/company/` — Company, SupplierPart, ManufacturerPart.
- `source/src/backend/InvenTree/common/` — shared model mixins (`InvenTreeModel`, `MetadataMixin`, etc.)
  used throughout the other cloned apps.
- `source/LICENSE` — MIT.

## Known dependencies
- Django backend (`src/backend`); a separate frontend under `src/frontend` was **not** cloned.
- Repo ships `AGENTS.md` and `CLAUDE.md` at root (AI-agent tooling files) — excluded by the sparse-checkout
  pattern, not relevant to extraction.

## Do not copy
- No InvenTree code was copied into the kit in this pass (domain-knowledge research only, not kit
  implementation). If a future pass promotes InvenTree's models into `starters/` or `features/`, the MIT
  license permits it with attribution — see `sources.md` for why that wasn't done here.

## Notes
- InvenTree focuses on inventory/parts with a build-order layer bolted on; it does **not** model routings,
  operations, or work centers as distinct entities the way Odoo's `mrp` module does. This asymmetry is
  called out throughout `feature-map.json`/`entities.json` (features grounded only in `odoo-mrp`).
- `src/backend` alone is ~10 MB after sparse-checkout (well under the 200,000 KB threshold that would
  have required narrowing further), even though the full repository is ~375 MB.
