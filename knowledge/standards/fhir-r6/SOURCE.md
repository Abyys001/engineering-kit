# HL7 FHIR R6 (6.0.0-snapshot1)

- **Title**: FHIR (Fast Healthcare Interoperability Resources), Release 6, snapshot 1
- **Publisher**: HL7 International
- **URL(s) actually downloaded**:
  - `https://hl7.org/fhir/6.0.0-snapshot1/downloads.html` (downloads index, to find the definitions bundle)
  - `https://hl7.org/fhir/6.0.0-snapshot1/definitions.json.zip` (the JSON definitions zip only — not the full spec/website/examples bundles)
- **License**: HL7 FHIR specification content (schemas, definitions, narrative) is released under **CC0** (public domain dedication); the FHIR® name/logo are HL7 trademarks governed by HL7's IP policy, separate from the content license. Confirmed via `https://hl7.org/fhir/6.0.0-snapshot1/license.html`, which contains "CC0" / "Creative Commons" / "public domain" language.
- **Version**: 6.0.0-snapshot1 — a **pre-release development snapshot**, not a published normative or trial-use ballot version.
- **Retrieved**: 2026-09-26
- **File list** (extracted from `definitions.json.zip`, 5.5 MB; only these 4 files were extracted, not the full zip contents):
  - `definitions.json.zip` — 5.5 MB, kept as downloaded.
  - `profiles-resources.json` — 38 MB, Bundle of all base-resource `StructureDefinition`s + `OperationDefinition`s + `CompartmentDefinition`s + `CapabilityStatement`s.
  - `profiles-types.json` — 3.2 MB, Bundle of data-type `StructureDefinition`s.
  - `valuesets.json` — 5.0 MB, Bundle of `ValueSet`/`CodeSystem` resources.
  - `search-parameters.json` — 2.4 MB, Bundle of `SearchParameter` resources.
  - `extract.py` — stdlib-only script that reads `profiles-resources.json` and writes `../../entities/fhir-r6-resources.json`.
- **What it's useful for**: Healthcare resource model reference (resource types, their top-level elements/cardinalities, value sets) for the `healthcare` domain.
- **Redistribution/attribution notes**: CC0 imposes no attribution requirement, but HL7's trademark policy asks that "FHIR" and the HL7 flame logo not be used to imply endorsement; this is reference material only, not redistributed as a product.

## R4 vs R6 — which release to actually build against

**FHIR R4 (4.0.1)** is the release most production FHIR servers implement today (confirmed on `https://hl7.org/fhir/R4/`, which repeatedly identifies itself as "4.0.1", HL7's long-lived normative release; e.g. Medplum, most national health-IT programs, and the bulk of commercial FHIR servers target R4). **R6 6.0.0-snapshot1 is a pre-release development snapshot** — resource shapes, cardinalities, and even resource existence can still change before final publication. Use this R6 snapshot only for forward-looking reference/comparison; default any new implementation work to R4 semantics unless a project explicitly requires R6/R5 features. `std:fhir-r4` is recorded in `standards.json` as `reference_only` (URL only, no local copy) for this reason.

## Extraction method

`extract.py` (stdlib `json`/`re` only) filters `profiles-resources.json` to `StructureDefinition` entries where `kind == "resource"` and `derivation == "specialization"` (124 base resource types — profiles and logical models are excluded). For each it records:
- `name`, `description` (first sentence of the StructureDefinition description)
- `standards_status` — from the `structuredefinition-standards-status` extension (e.g. `normative`, `trial-use`). **R6 does not carry a numeric FMM (FHIR Maturity Model) level** in this snapshot's extensions (checked: no `structuredefinition-fmm` extension present anywhere in the file) — `standards_status` is the closest available analog, noted as such in the output file.
- `category` — from `structuredefinition-category` (e.g. `"Financial.General"`), used as the module grouping.
- `working_group` — from `structuredefinition-wg`.
- `key_elements` — every depth-1 element from `snapshot.element` (name, `min..max` cardinality, type code(s)).

Output: `knowledge/entities/fhir-r6-resources.json` (124 resources, ~528 KB).
