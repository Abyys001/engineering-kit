# Healthcare (clinic / practice management)

Ambulatory clinic and practice management: patient records, scheduling, clinical documentation, orders/results, billing, and interoperable data exchange. Modeled on FHIR R4 4.0.1 (what production systems, including Medplum, implement today). `knowledge/entities/fhir-r6-resources.json` (R6 6.0.0-snapshot1, pre-release) is present and was consulted for verified R4→R6 element differences only — it carries cardinality and type, not bound ValueSet codes, so every status enum here stays R4. See `## Standards` below.

## Product types
Single/multi-provider clinics, specialty practices, telehealth-first practices, and platforms (like Medplum) that let developers build EHR-adjacent apps on a FHIR-native backend.

## Users
Patient, physician/clinician, nurse, front desk/scheduler, billing specialist, lab technician, care coordinator, pharmacist (partner), compliance/privacy officer, practice manager, system/integration account. See `roles.json`.

## Core workflows
Appointment lifecycle (Schedule → Slot → Appointment), encounter lifecycle, lab order/result lifecycle, prescription lifecycle, billing claim lifecycle, patient intake, referrals, telehealth visits. State machines mirror FHIR R4 status value sets verbatim where one exists (`workflows.json`).

## Capabilities
- **Core**: patient registration, practitioner directory, organizations/locations, scheduling, encounters, clinical notes, problem list, observations/vitals, e-prescribing, allergy tracking, billing & claims.
- **Common**: patient portal, appointment reminders, telehealth, document management, lab orders/results, insurance eligibility, digital intake forms.
- **Compliance-classified**: patient consent, fine-grained access policies.
- **Recommended/optional/premium**: care team, referrals, immunizations, care plans, waitlist, patient invoicing, no-show risk scoring (AI).

Full list with confidence/tags: `FEATURES.md`.

## Compliance-sensitive areas
HIPAA (US, high confidence), GDPR special-category health data (EU/EEA), 42 CFR Part 2 (US substance-use records, low confidence — single-source inference), ONC Cures Act information blocking (US patient-access rule), HITRUST CSF (certification), cross-jurisdiction telehealth licensure, PCI DSS (card payments). All `requires_human_review: true`; see `compliance.json` disclaimer. Regional variants are flagged, not resolved — nothing here claims a product "is compliant."

## Integrations
Lab interfaces (HL7v2/FHIR), e-prescribing networks (NCPDP SCRIPT), billing clearinghouses (X12 EDI), telehealth video platforms, SMS gateways, patient payment gateways, SMART on FHIR / HIE interoperability, fax/eFax, calendar sync, identity verification.

## Entities
Patient, Practitioner(Role), Organization, Location, Schedule, Slot, Appointment, Encounter, ClinicalNote, Condition, Observation, MedicationRequest, AllergyIntolerance, Document, ServiceRequest, DiagnosticReport, Coverage, Claim, Consent, AccessPolicy (Medplum-specific, no FHIR standard mapping), CareTeam, CarePlan, Immunization. Most map to a FHIR R4 resource — see `entities.json` `standard_mapping`.

## UI patterns
Patient timeline/summary, scheduler/calendar grid, SOAP-style note editor, resource form/table for structured clinical data, questionnaire-driven intake forms, document/attachment viewer.

## Mobile
Patient portal (appointments, results, messaging, forms) is the primary mobile surface; staff-facing scheduling has secondary mobile relevance.

## AI
Ambient/assisted clinical note drafting, no-show risk scoring, denial-risk prediction for claims, abnormal-result triage, duplicate-record detection — all `ai_relevance: medium` or higher features, none marked `core` (human review stays in the loop).

## Standards
`std:fhir-r4` (authoritative, what production systems including Medplum implement) drives most entity/workflow modeling. `knowledge/entities/fhir-r6-resources.json` (acquired concurrently by another pass) was consulted for one verified R6 difference: `Encounter.class` became repeatable (0..* CodeableConcept) in R6 vs. a single 0..1 Coding in R4 — see `entities.json`. That file records element cardinality/type only, not bound ValueSet codes, so no R6 status-enum claims are made.

## Terminology
EHR/EMR (electronic health/medical record), FHIR (Fast Healthcare Interoperability Resources), PHI (protected health information), HIE (health information exchange), SMART on FHIR (app-launch/authorization framework), Access Policy (Medplum's resource/compartment-level authorization rule, not a FHIR standard).

## Sources
Medplum (Apache-2.0, cloned), OpenEMR (GPL-3.0, reference-only), OpenMRS core (MPL-2.0, reference-only). Details: `sources.md`.
