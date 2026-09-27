# Domain knowledge schema (v1)

Contract for every `domains/<domain>/` folder. `tools/kb.py validate` enforces it; `tools/kb.py build` regenerates `domains/catalog.json`, `domains/features.json`, `domains/search-index.json`, and `domains/INDEX.md` from these files. Never hand-edit the generated files.

Domain knowledge is a **reasoning aid, not a scope list**: a feature's presence here never means a client asked for it (see `product-builder/PRODUCT-BUILDER.md`).

## Files

| File | Contents |
|---|---|
| `DOMAIN.md` | Human summary, ≤150 lines: description, product types, users, workflows, core/common/optional capabilities, compliance-sensitive areas, integrations, entities, UI patterns, mobile, AI, standards, terminology |
| `FEATURES.md` | Human table of the features in `feature-map.json`, grouped by classification |
| `feature-map.json` | Domain metadata, the domain's **source registry**, and feature records |
| `entities.json` | Conceptual entities (not a DB schema) |
| `roles.json` | Domain roles (knowledge, not app permissions) |
| `workflows.json` | Workflows and lifecycle state machines |
| `integrations.json` | External systems the domain commonly connects to |
| `compliance.json` | Regulations/standards, kept separate from features |
| `dependencies.json` | Feature dependency edges; drives build order |
| `implementation-map.json` | Feature → kit implementation paths and maturity |
| `sources.md` | Human list of sources with class, license, and what each informed |

All JSON files start with `"schema": 1`, `"domain": "<id>"`, `"last_reviewed": "YYYY-MM-DD"`.

## IDs

- Domain feature: `<domain>.<snake_case>` — `restaurant.reservations`.
- Shared capability (auth, notifications, …): `shared.<snake_case>`, defined only in `domains/shared-features.json`. Domain features depend on it; never redefine it inside a domain.
- A domain may depend on another domain's feature (`booking.availability`) instead of duplicating it.
- Entities, roles, workflows, integrations, compliance items: `snake_case`, unique within the domain.
- Sources: `<id>` from the domain's `sources` array, or `std:<id>` from `knowledge/standards/standards.json`.

## Enums

| Field | Values |
|---|---|
| `classification` | `core` · `common` · `recommended` · `optional` · `premium` · `compliance` · `integration` · `platform` · `infrastructure` (`requested` is set per project by the product builder, never in the catalog) |
| `ai_relevance`, `real_time_relevance` | `none` · `low` · `medium` · `high` · `core` |
| `confidence` | `high` (authoritative source, or ≥3 independent implementations) · `medium` (2 independent sources) · `low` (one source or reasoned inference) |
| `source_type` | `authoritative` · `implementation` · `secondary` |
| implementation `status` | `unknown` · `reference` · `partial` · `curated` · `tested` · `production_ready` (only after the kit quality gate) |
| `maturity` (domain) | `researching` · `partial` · `curated` (≥10 features, ≥3 sources, ≤30% low-confidence features, publisher sources actually checked) · `reviewed` (a human has reviewed it) |
| dependency `type` | `requires` (cannot work without) · `enhances` (better with, not needed) |

## feature-map.json

```json
{
  "schema": 1,
  "domain": "restaurant",
  "name": "Restaurant",
  "aliases": ["food service"],
  "description": "…",
  "nace": ["I56.1"],
  "maturity": "partial",
  "last_reviewed": "2026-09-26",
  "sources": [
    {
      "id": "frappe-hospitality",
      "title": "Frappe Hospitality",
      "url": "https://github.com/frappe/hospitality",
      "source_type": "implementation",
      "license": "GPL-3.0",
      "retrieved": "2026-09-26",
      "version": "<commit sha or version, if known>",
      "local_path": "sources/domains/frappe-hospitality",
      "notes": "reference only; GPL code never enters the kit"
    }
  ],
  "features": [
    {
      "id": "restaurant.reservations",
      "name": "Reservations",
      "classification": "core",
      "description": "Book tables for a date/time and party size.",
      "users": ["customer", "host", "manager"],
      "entities": ["reservation", "table", "guest"],
      "workflows": ["reservation_lifecycle"],
      "capabilities": ["availability", "conflict_detection"],
      "platforms": {"web": true, "mobile": true, "admin": true, "customer_portal": true, "backend": true, "ai": false, "real_time": false},
      "ai_relevance": "medium",
      "ai_opportunities": ["no-show prediction"],
      "real_time_relevance": "medium",
      "tags": ["core", "calendar", "customer", "staff"],
      "integrations": ["sms_gateway"],
      "compliance": [],
      "provenance": {"sources": ["frappe-hospitality", "std:nace-rev2.1"], "confidence": "medium", "notes": ""}
    }
  ]
}
```

`users` = role ids from `roles.json`; `entities` = entity ids; `workflows` = workflow ids; `integrations`/`compliance` = ids from those files. `dependencies` live only in `dependencies.json`, and implementation status only in `implementation-map.json`, so neither drifts.

Tags describe capabilities, not marketing: `core common optional premium admin customer staff mobile web backend ai real-time payment compliance integration analytics workflow calendar document communication inventory scheduling reporting location identity search`.

## entities.json

```json
{"schema": 1, "domain": "restaurant", "last_reviewed": "…", "entities": [{
  "id": "reservation", "name": "Reservation", "description": "…",
  "relationships": [{"type": "belongs_to", "target": "guest"}, {"type": "belongs_to", "target": "table", "note": "optional until seated"}],
  "important_fields": ["party_size", "start_at", "status"],
  "states": ["requested", "confirmed", "seated", "completed", "cancelled", "no_show"],
  "related_features": ["restaurant.reservations"],
  "standard_mapping": [{"source": "std:fhir-r6", "concept": "Appointment", "note": "healthcare only"}],
  "provenance": {"sources": ["…"], "confidence": "medium"}
}]}
```

Relationship `type`: `has_one` · `has_many` · `belongs_to` · `many_to_many`. `target` is an entity id in this domain, or `<domain>:<entity>`. Fields are illustrative unless `standard_mapping` cites a standard that defines them — never present an example field list as a standard.

## roles.json

```json
{"schema": 1, "domain": "…", "last_reviewed": "…", "roles": [{
  "id": "host", "name": "Host", "experience": "staff",
  "description": "…", "responsibilities": ["…"],
  "related_features": ["restaurant.reservations"], "common_permissions": ["reservation:create", "table:assign"],
  "provenance": {"sources": ["…"], "confidence": "medium"}
}]}
```

`experience`: `customer` · `staff` · `management` · `administration` · `partner` · `system`.

## workflows.json

```json
{"schema": 1, "domain": "…", "last_reviewed": "…", "workflows": [{
  "id": "reservation_lifecycle", "name": "…",
  "actor": "customer", "trigger": "Customer requests a table",
  "steps": ["Select date", "Select time", "Check availability", "…"],
  "entities": ["reservation", "table"],
  "features": ["restaurant.reservations"],
  "state_machine": {
    "entity": "reservation", "initial": "requested", "terminal": ["completed", "cancelled", "no_show"],
    "states": ["requested", "confirmed", "seated", "completed", "cancelled", "no_show"],
    "transitions": [{"from": "requested", "to": "confirmed", "event": "confirm"}]
  },
  "notifications": ["confirmation", "reminder"],
  "integrations": ["sms_gateway"],
  "provenance": {"sources": ["…"], "confidence": "medium"}
}]}
```

`state_machine` is optional; include it only where the lifecycle is meaningful. Every transition's `from`/`to` must be in `states`.

## integrations.json

```json
{"schema": 1, "domain": "…", "last_reviewed": "…", "integrations": [{
  "id": "pos", "name": "Point of sale", "category": "pos",
  "purpose": "…", "examples": ["Square", "Toast"], "protocols": ["REST", "webhooks"],
  "related_features": ["restaurant.pos_integration"], "classification": "common",
  "provenance": {"sources": ["…"], "confidence": "medium"}
}]}
```

Examples name real vendors/standards only as examples — never as a requirement.

## compliance.json

```json
{"schema": 1, "domain": "…", "last_reviewed": "…",
 "disclaimer": "Domain knowledge, not legal advice. Confirm applicability per jurisdiction with a qualified reviewer.",
 "items": [{
  "id": "pci_dss", "name": "PCI DSS", "kind": "standard", "version": "4.0.1",
  "jurisdiction": "global (card-network contractual)", "scope": "…",
  "affected_features": ["restaurant.payments"], "requires_human_review": true,
  "notes": "…", "url": "https://…",
  "provenance": {"sources": ["…"], "confidence": "high"}
}]}
```

`kind`: `regulation` · `standard` · `certification` · `guideline`.

## dependencies.json

```json
{"schema": 1, "domain": "…", "last_reviewed": "…", "edges": [
  {"from": "restaurant.reservations", "to": "restaurant.tables", "type": "requires", "reason": "Availability is computed per table"},
  {"from": "restaurant.reservations", "to": "shared.notifications", "type": "enhances", "reason": "Confirmations and reminders"}
]}
```

`from` depends on `to`. `requires` edges must form a DAG (the validator rejects cycles).

## implementation-map.json

```json
{"schema": 1, "domain": "…", "last_reviewed": "…", "mappings": [{
  "feature": "restaurant.reservations",
  "implementations": {"web": [], "backend": [], "mobile": [], "ai": []},
  "references": ["sources/domains/frappe-hospitality"],
  "status": "reference",
  "notes": "…"
}]}
```

`implementations` holds kit paths (relative to the kit root) that exist; the validator checks them. `references` holds `sources/…` paths used for learning only. Status is `unknown` when neither exists, `reference` when only sources exist.

## Provenance

Every feature, entity, role, workflow, integration, and compliance item carries `provenance` with `sources` (ids that resolve) and `confidence`. One repository is never enough for `high`. Mark reasoned-but-unsourced items `low` and say so in `notes`.
