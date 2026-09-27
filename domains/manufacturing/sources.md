# Manufacturing sources

## Implementations cloned (`sources/domains/<name>/`)

| Source | License | Status | Informed |
|---|---|---|---|
| [InvenTree](https://github.com/inventree/InvenTree) (`sources/domains/inventree`) | MIT | reference-only (kept sparse to a domain-model subset, not promoted into the kit) | Part (IPN/revision/assembly/component/trackable/purchaseable/salable/consumable), BomItem/BomItemSubstitute, StockItem/StockLocation/StockItemTracking/StockItemTestResult, Build/BuildLine/BuildItem, PurchaseOrderStatus, company app (Company/SupplierPart/ManufacturerPart). |
| [Odoo — `addons/mrp`](https://github.com/odoo/odoo) (`sources/domains/odoo-mrp`) | LGPL-3.0 | reference-only | mrp.production (state machine), mrp.workorder (state machine), mrp.workcenter, mrp.bom/mrp.bom.line/mrp.bom.byproduct, mrp.routing.workcenter, mrp.unbuild, stock_orderpoint.py (reorder points), stock_lot.py. |

InvenTree is MIT (permissive) — it was still kept **reference-only** in this pass rather than promoted
into `starters/`/`features/`, since this task was scoped to domain-knowledge research, not kit
implementation; a future pass could sparse-clone its models more fully as a starting point for an actual
InvenTree-derived module (per the research brief: "InvenTree — good candidate for a sparse clone of its
models"). Odoo is LGPL-3.0: learned from for models/terminology only, no code copied or will be copied.
Licenses verified from each repository's actual root `LICENSE` file.

## Standards referenced

- `std:gs1-epcis` — cited on `stock_item` and `traceability_record` for lot/serial identification and
  event modeling. **Not yet acquired locally** at time of writing; low-confidence, name-only citations.
- **ISA-95 / IEC 62264** — named in the research brief as the domain's terminology standard, but it is
  **not present** in `knowledge/standards/standards.json` and was **not added** (out of scope: "don't
  touch `standards.json`"). No `std:isa-95` citation exists anywhere in this domain. Flagged in the final
  report as a gap worth adding to the standards registry in a future pass.
- `std:nace-rev2.1` — used only for the domain's `nace` classification codes, not as a feature source.

## Considered but not used

- **ERPNext manufacturing** (frappe/erpnext) — named in the brief; confirmed GPL-3.0 via the GitHub API
  and its repository size (~1.9 GB) is far over the 200,000 KB direct-clone threshold and would need a
  narrow sparse-checkout of just its manufacturing app. Not cloned in this pass: Odoo's `addons/mrp` and
  InvenTree together already cover the requested feature surface (BOM, routing, work orders, work
  centers, MRP, inventory/lots, quality, traceability) without a third clone, and the domain's 2-clone
  budget was spent accordingly. A future pass could add it to cross-validate the "single source, low
  confidence" features flagged throughout this domain (routings_operations, work_centers, work_order
  scheduling, MRP, equipment_maintenance, quality_inspections, bom_byproducts) up to `medium`.
- Odoo's own quality (`quality`), maintenance (`maintenance`), and purchase (`purchase`) apps were **not**
  cloned (only `addons/mrp` was, per the sparse-checkout) — several manufacturing features here
  (`quality_inspections`, `equipment_maintenance`, `purchase_orders`) are consequently grounded only in
  InvenTree or reasoned from `mrp`'s own bundled files, not in Odoo's dedicated modules for those areas.
