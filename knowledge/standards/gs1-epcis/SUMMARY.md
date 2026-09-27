# GS1 EPCIS 2.0 / CBV summary

Full provenance: `SOURCE.md` (GS1 disclaimer license, SHA `6f71468`, EPCIS/CBV 2.0 development+public-review content).

## Event types (from `Ontology/EPCIS.jsonld` / `EPCIS.ttl`)

Base class `epcis:EPCISEvent`, specialized as:

- **ObjectEvent** - something happened to one or more physical/digital objects (EPCs).
- **AggregationEvent** - objects were physically aggregated into/disaggregated from a parent (e.g. cases onto a pallet).
- **TransactionEvent** - objects were associated with one or more business transactions (e.g. a PO or invoice).
- **TransformationEvent** - input objects were consumed to create output objects (e.g. manufacturing).
- **AssociationEvent** - a persistent (non-transactional) link/unlink between an object and other objects or an asset (e.g. attaching a reusable sensor tag).

## The five (+one) event dimensions

| Dimension | Fields | Source |
|---|---|---|
| **What** | `epcList`, `quantityList`, `parentID`, `childEPCs`, `childQuantityList`, `inputEPCList`/`outputEPCList`, `epcClass` | `Ontology/EPCIS.jsonld` |
| **When** | `eventTime`, `eventTimeZoneOffset`, `recordTime` | `Ontology/EPCIS.jsonld` |
| **Where** | `readPoint`, `bizLocation` | `Ontology/EPCIS.jsonld` |
| **Why** | `bizStep`, `disposition`, `bizTransactionList` | `Ontology/EPCIS.jsonld` + `Ontology/CBV.jsonld` |
| **How** (new in EPCIS 2.0) | `sensorElementList`, `sensorReport`, `ilmd` (Instance/Lot Master Data) | `Ontology/EPCIS.jsonld`, `Implementation Guideline/Section3.5NEW_TheHOWDimension.md` |
| Disposition persistence | `persistentDisposition` (set/unset) for objects with a disposition that outlives a single event | `Ontology/EPCIS.jsonld` |

## CBV business steps (41), from `JSON-LD-Context/cbv-context-bizstep.jsonld`

accepting, arriving, assembling, collecting, commissioning, consigning, creating_class_instance, cycle_counting, decommissioning, departing, destroying, disassembling, dispensing, encoding, entering_exiting, holding, inspecting, installing, killing, loading, other, packing, picking, receiving, removing, repackaging, repairing, replacing, reserving, retail_selling, sampling, sensor_reporting, shipping, staging_outbound, stock_taking, stocking, storing, transporting, unloading, unpacking, void_shipping

## CBV dispositions (33), from `JSON-LD-Context/cbv-context-disposition.jsonld`

active, available, completeness_inferred, completeness_verified, conformant, container_closed, container_open, damaged, destroyed, dispensed, disposed, encoded, expired, in_progress, in_transit, inactive, mismatch_class, mismatch_instance, mismatch_quantity, needs_replacement, no_pedigree_match, non_conformant, non_sellable_other, partially_dispensed, recalled, reserved, retail_sold, returned, sellable_accessible, sellable_not_accessible, stolen, unavailable, unknown

## Other CBV vocabularies present

- **Business transaction types** (`JSON-LD-Context/cbv-context-biztransaction-type.jsonld`): bol, cert, desadv, inv, pedigree, po, poc, prodorder, recadv, rma, testprd, testres, upevt.
- **Source/destination types** (`JSON-LD-Context/cbv-context-sourcedest-type.jsonld`): owning_party, possessing_party, location.
- Error reasons: `JSON-LD-Context/cbv-context-error-reason.jsonld`.

## Machine-readable entry points

| Format | File |
|---|---|
| RDF/Turtle ontology | `Ontology/EPCIS.ttl`, `Ontology/CBV.ttl` |
| JSON-LD context (whole spec) | `epcis-context.jsonld` (full), `epcis-context-simple.jsonld` (flattened terms, easier to consume) |
| JSON-LD ontology | `Ontology/EPCIS.jsonld`, `Ontology/CBV.jsonld` |
| JSON Schema | `EPCIS-JSON-Schema.json`, `JSON-Schema/EPCIS-Document-JSON-Schema.json`, `JSON-Schema/EPCIS-Event-JSON-Schema.json` |
| SHACL shapes (validation) | `Ontology/EPCIS-SHACL.ttl` |
| XML Schema (legacy binding) | `XSD/EPCglobal-epcis-2_0.xsd` |
| REST API contract | `REST Bindings/openapi.yaml` / `openapi.json` |

Prefer the JSON-LD context + JSON Schema pair for a NestJS/TypeScript implementation; use the OpenAPI file directly as the REST contract if implementing an EPCIS query/capture service.
