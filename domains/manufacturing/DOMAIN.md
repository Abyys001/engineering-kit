# Manufacturing

Small-to-mid manufacturing execution and ERP-lite (MES-lite): items and bills of material, routings and
work centers, production/work orders with a state machine, material requirements, lot/serial inventory,
quality inspection, maintenance, and shop-floor data collection. NACE Rev. 2.1: C25.62 (machining),
C28.29 (other general-purpose machinery), C33.12 (repair of machinery) — illustrative; actual codes
depend heavily on what is being manufactured.

## Product types

- Shop-floor execution systems (MES) layered over a simpler inventory/parts base (InvenTree-style).
- Full ERP manufacturing modules (Odoo mrp-style): BOM, routing, work orders, work centers, MRP.
- Traceability-first systems for regulated manufacturing (medical device, food, aerospace).

## Users

Production planner, shop floor operator, quality inspector, purchasing agent, maintenance technician,
plant/operations manager, external supplier/vendor, and an automated system actor (MRP engine, scan
ingestion). See `roles.json`.

## Core workflows

1. **BOM management** — define components, operations, and by-products for an item.
2. **Production order lifecycle** — draft → confirmed → in progress → to close → complete/cancelled.
3. **Work order execution** — per-operation blocked → ready → progress → done at a work center.
4. **Material requirements planning** — reorder-point-triggered replenishment suggestions.
5. **Quality inspection** and **traceability lookup** (forward/backward genealogy).

See `workflows.json` for full steps and state machines. The production-order and work-order state
machines are grounded in two independently-designed systems with different vocabularies (InvenTree's
`BuildStatus`; Odoo's `mrp.production.state`/`mrp.workorder.state`) — see each entity's provenance notes
for exactly which parts are verbatim vs. reconciled/reasoned.

## Capabilities by classification

- **Core**: items/products, BOM, routings & operations, work centers, production/work orders,
  inventory (lots/serials), shop-floor data collection, traceability.
- **Common**: MRP, stock locations, purchase orders, quality inspections, by-products/co-products.
- **Recommended**: BOM substitutes are optional but disassembly/unbuild, subcontracting, equipment
  maintenance, non-conformance management, and work order scheduling are recommended.
- **Optional**: supplier management, product variants, stocktake/cycle counting, cost tracking, work
  center capacity planning, production scrap tracking.

Full list with descriptions: `FEATURES.md` / `feature-map.json`.

## Compliance-sensitive areas

Product traceability regulations (industry- and jurisdiction-specific: medical device, food, automotive)
and ISO 9001 quality management (a voluntary certification, not a legal requirement). Both are
`requires_human_review: true` and are **not** implemented by either reference source. See
`compliance.json`. Citing a standard here never means a product built from this domain is compliant.

## Integrations

Barcode/QR scanning for shop-floor data entry; supplier EDI/catalog exchange for procurement. See
`integrations.json`.

## Entities

item, bill_of_materials, bom_line, bom_byproduct, routing_operation, work_center, production_order,
work_order, stock_item, stock_location, supplier, purchase_order, quality_inspection, non_conformance,
traceability_record, product_variant. See `entities.json`.

## UI patterns

BOM tree editor, Gantt-style work center schedule, kanban-style production order board by status,
shop-floor tablet screen (large touch targets, barcode scan field, start/pause/complete buttons),
traceability genealogy tree (upstream/downstream), inspection checklist form.

## Mobile

Shop-floor data collection is core: a tablet/mobile interface for scanning barcodes, starting/completing
operations, and reporting produced/scrapped quantity, used standing at a work center rather than at a desk.

## AI opportunities

Completion-date risk prediction, finite-capacity scheduling optimization, demand-driven reorder point
tuning, defect pattern detection across serials, predictive maintenance from downtime patterns,
bottleneck prediction on work center load.

## Standards

- **ISA-95 / IEC 62264** — the research brief names this for terminology/levels, but it is **not** in
  this kit's standards registry (`knowledge/standards/standards.json`) and was not added here (per the
  brief: propose additions in the final report rather than editing that file). No `std:isa-95` citation
  appears anywhere in this domain's JSON as a result — ISA-95 terminology is used informally in this
  prose only (e.g. "work center", "production order"), never as a cited provenance source.
- **GS1** (traceability/EPCIS) — referenced as `std:gs1-epcis` on the `stock_item` and
  `traceability_record` entities, but **not yet acquired locally** at time of writing; citations are
  low-confidence and name-only.

## Terminology

- **BOM** — bill of materials.
- **MRP** — material requirements planning (here: reorder-point-triggered, not full MRP II netting).
- **Work center** — a production resource (machine/line/team); **work order** here means a single
  operation's execution, distinct from the **production order** (the overall build).
- **Genealogy / traceability** — tracing which input lots went into which output lot, and vice versa.
