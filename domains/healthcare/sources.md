# Healthcare sources

Class, license, and what each source informed. Full records: `feature-map.json` → `sources`.

| ID | Title | Type | License | Local clone | Informed |
|---|---|---|---|---|---|
| `medplum` | [Medplum (headless EHR platform)](https://github.com/medplum/medplum) | implementation | Apache-2.0 | sources/domains/medplum/source | `access_policies`, `allergy_tracking`, `billing_claims`, `care_plans`, `care_team`, `clinical_notes`, `document_management`, `encounters`, `immunizations`, `insurance_eligibility`, `lab_orders`, `lab_results`, `observations_vitals`, `organization_locations`, `patient_consent`, `patient_intake_forms`, `patient_portal`, `patient_registration`, `practitioner_directory`, `problem_list`, `referrals`, `scheduling` |
| `openemr` | [OpenEMR](https://github.com/openemr/openemr) | implementation | GPL-3.0 | — | `allergy_tracking`, `appointment_reminders`, `billing_claims`, `clinical_notes`, `document_management`, `e_prescribing`, `encounters`, `insurance_eligibility`, `lab_orders`, `lab_results`, `observations_vitals`, `organization_locations`, `patient_invoicing`, `patient_portal`, `patient_registration`, `practitioner_directory`, `problem_list`, `referrals`, `scheduling`, `telehealth`, `waitlist` |
| `openmrs-core` | [OpenMRS core](https://github.com/openmrs/openmrs-core) | implementation | MPL-2.0 | — | `allergy_tracking`, `care_plans`, `clinical_notes`, `encounters`, `immunizations`, `observations_vitals`, `organization_locations`, `patient_registration`, `problem_list` |

## Notes per source

### medplum
- Retrieved: 2026-09-27; version: 2a810b6f7eaf149c290915f885c3f8423cd5d0ee
- Extraction-safe (Apache-2.0, NOTICE present, preserve on reuse). Sparse checkout: packages/definitions (FHIR R4 StructureDefinitions/ValueSets + Medplum extensions incl. AccessPolicy), packages/react (form/display components: Scheduler, PatientHeader/Summary/Timeline, QuestionnaireForm/Builder, EncounterTimeline, ServiceRequestTimeline, DiagnosticReportDisplay), packages/core, packages/fhirtypes, packages/mock (synthetic FHIR test data), packages/app (web app shell incl. src/lab), examples/ (foomedical patient portal, medplum-patient-intake-demo, medplum-eligibility-demo, medplum-provider, medplum-smart-on-fhir-demo). Excluded packages/docs, packages/server, packages/agent and other packages to stay well under the size cap.

### openemr
- Retrieved: 2026-09-27; version: main branch, 2026-09-26 snapshot
- Not cloned; inspected via GitHub API (repo license field GPL-3.0). Reference-only — most widely deployed open-source ambulatory EHR/PM system; informs scheduling, encounters, billing/claims, and patient portal feature scope. No code copied.

### openmrs-core
- Retrieved: 2026-09-27; version: main branch, 2026-09-26 snapshot
- License verified from actual root LICENSE file (Mozilla Public License 2.0; GitHub API license field reported NOASSERTION). Reference-only (copyleft-per-file). Global-health-oriented EMR; informs patient/encounter/observation model and concept dictionary approach. No code copied.
