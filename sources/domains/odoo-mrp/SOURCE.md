# Odoo (mrp addon)

| Field | Value |
|---|---|
| Source URL | https://github.com/odoo/odoo (subdirectory `addons/mrp`) |
| GitHub repository | `odoo/odoo`, branch `20.0` |
| Category | domains/manufacturing |
| License | LGPL-3.0 — `LICENSE.txt` (verbatim copy of root `LICENSE`); see also root `COPYRIGHT` |
| Author / organization | Odoo S.A. |
| Acquired | 2026-09-27 |
| Revision | `9b1a92e38dbae2bb83ad80700ccec0535f8ac68f` (branch `20.0`) |
| Attribution required | LGPL notice retention if code were reused (it is not — reference-only) |
| Status | reference-only — LGPL-3.0 is on the research brief's copyleft list; learn from it, never copy code into the kit. |

## Useful for
- **mrp.production** (`models/mrp_production.py`) — the production/manufacturing order: `name`
  (reference), `priority`, `origin`, `product_id`/`product_qty`/`uom_id`, `picking_type_id`,
  `location_src_id`/`location_dest_id`, `date_deadline`/`date_start`/`date_finished`,
  `duration_expected`/`duration`, `bom_id`, and the **state machine**: `state` selection (draft,
  confirmed, progress, to_close, done, cancel) plus `reservation_state` (confirmed/assigned/waiting).
  Grounds `manufacturing.production_orders`.
- **mrp.workorder** (`models/mrp_workorder.py`) — a single operation's execution: `production_id`,
  `workcenter_id`, `qty_producing`/`qty_produced`, `date_start` (Planned Date), `leave_id` (calendar
  slot), and its own **state machine**: `state` selection (blocked, ready, progress, done, cancel) with
  explicit `_compute_state` logic (blocked while a prerequisite `blocked_by_workorder` isn't done/cancel).
  Grounds `manufacturing.work_order_scheduling`, `work_order_execution` workflow.
- **mrp.workcenter** (`models/mrp_workcenter.py`) — `name`, `code`, `costs_hour`, `time_start`/
  `time_stop` (setup/cleanup), `routing_line_ids`, `order_ids`, computed `workorder_*_count` fields, and
  `working_state` (normal/blocked/done). Grounds `manufacturing.work_centers`,
  `manufacturing.workcenter_capacity_planning`, `manufacturing.equipment_maintenance` (reasoned).
- **mrp.bom / mrp.bom.line / mrp.bom.byproduct** (`models/mrp_bom.py`) — BOM header (`type`: normal/phantom,
  `product_tmpl_id`/`product_id`, `bom_line_ids`, `byproduct_ids`, `operation_ids`). Grounds
  `manufacturing.bill_of_materials`, `manufacturing.bom_byproducts`.
- **mrp.routing.workcenter** (`models/mrp_routing.py`) — routing/operation steps. Grounds
  `manufacturing.routings_operations`.
- **mrp.unbuild** (`models/mrp_unbuild.py`) — reverses a production order. Grounds
  `manufacturing.disassembly_unbuild`.
- **stock_orderpoint.py** (bundled in this addon, extends `stock.warehouse.orderpoint` with `bom_id`/
  `effective_bom_id`) — reorder-point replenishment. Grounds
  `manufacturing.material_requirements_planning`.
- **stock_lot.py**, **stock_move.py**, **stock_move_line.py**, **stock_package.py**, **stock_quant.py**,
  **stock_picking.py**, **stock_rule.py**, **stock_warehouse.py** — these are `stock` module extensions
  *bundled inside* `addons/mrp` (not the full `stock` module itself), adding manufacturing-specific
  behavior to lots, moves, and warehouses. Cross-referenced for `manufacturing.inventory_lots_serials`
  and `manufacturing.traceability` alongside InvenTree.

## Where things live
- `source/addons/mrp/models/` — all model files listed above, one Python file per model group.
- `source/addons/mrp/views/`, `report/`, `security/`, `data/`, `wizard/`, `static/`, `tests/`, `i18n/` —
  present in the clone (part of the addon) but not inspected for this domain-knowledge pass.
- `source/LICENSE` — LGPL-3.0. `source/COPYRIGHT` — per-file copyright attribution notes.

## Known dependencies
- Odoo's ORM (`odoo.fields`/`odoo.models`), part of the broader `odoo/odoo` monorepo; the `mrp` addon
  depends on the `stock` and `product` addons (referenced via `_name` foreign keys like
  `stock.warehouse.orderpoint`, `product.template`) which were **not** cloned — only the extension files
  Odoo ships *inside* `addons/mrp` itself.

## Do not copy
- Any code from `addons/mrp` — LGPL-3.0. Reference-only per the research brief's license policy.
- The rest of the `odoo/odoo` monorepo (all other addons, ~17.8 GB at the repo root) was **not** cloned;
  only `addons/mrp` plus root `LICENSE`/`COPYRIGHT` via sparse-checkout.

## Notes
- Two independent, real state-machine vocabularies now ground this domain's core lifecycle: Odoo's
  `mrp.production.state`/`mrp.workorder.state` (used verbatim in `workflows.json`) and InvenTree's
  `BuildStatus` (cross-referenced, not verbatim). Neither is claimed to be "the" industry standard —
  both are recorded as what they are: two real, independently-designed implementations.
- Odoo's dedicated `quality`, `maintenance`, and `purchase` addons were **not** cloned (only `mrp`), so
  several features in this domain are grounded in InvenTree alone or in `mrp`'s own bundled stock-file
  extensions rather than Odoo's purpose-built modules for those areas — see `sources.md` for the list.
