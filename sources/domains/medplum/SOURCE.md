# Medplum

| Field | Value |
|---|---|
| Source URL | https://github.com/medplum/medplum |
| GitHub repository | `medplum/medplum` |
| Category | domains/healthcare |
| License | Apache-2.0 — `LICENSE.txt` (verbatim copy of root `LICENSE.txt`) + root `NOTICE` (present in clone) |
| Author / organization | Orangebot, Inc. and Medplum contributors |
| Acquired | 2026-09-26 |
| Revision | `2a810b6f7eaf149c290915f885c3f8423cd5d0ee` (main) |
| Attribution required | NOTICE-file retention only (standard Apache-2.0; "Medplum" is a registered trademark — do not imply endorsement) |
| Status | extraction-safe — Apache-2.0 confirmed from actual root `LICENSE.txt`, `NOTICE` present and preserved, no nested conflicting licenses found in the paths checked out |

## Acquisition notes
Monorepo (`size` ~440 MB per `gh api repos/medplum/medplum`). Sparse checkout limited to high-value paths, kept under ~150 MB total:
`packages/definitions`, `packages/react`, `packages/core`, `packages/fhirtypes`, `packages/mock`, `packages/app`, `examples/`, `postgres/`, root `LICENSE.txt`/`NOTICE`/`README.md`. Excluded (size or relevance): `packages/docs` (~103 MB), `packages/server` (~9 MB Node backend), `packages/agent`, `packages/ccda`, `packages/react-scheduling`, `packages/bot-layer`, `packages/cli`, `packages/react-hooks`, `packages/examples`, `packages/fhir-router`, `packages/storybook`, `packages/cdk`, `packages/generator`, `packages/hl7`, DoseSpot/Health-Gorilla/ScriptSure integration packages, `packages/eslint-config`, `packages/graphiql`, `packages/e2e`, `packages/create-medplum`, `terraform/`, `charts/`, `scripts/`, `.github/`. Also excluded per the brief's standard exclusion list (`.claude/`, `CLAUDE.md`, etc.).

## Useful for
- **FHIR resource definitions** (`packages/definitions/src/fhir/r4/`): full FHIR R4 `StructureDefinition`/`ValueSet` JSON plus Medplum's own extensions — `profiles-medplum.json` defines the non-standard `AccessPolicy` resource used for fine-grained authorization; `search-parameters-medplum.json` and `valuesets-medplum.json` extend search/value-set behavior.
- **React healthcare UI components** (`packages/react/src/`): `Scheduler`, `PatientHeader`/`PatientSummary`/`PatientTimeline`, `EncounterTimeline`, `ServiceRequestTimeline`, `DiagnosticReportDisplay`, `QuestionnaireForm`/`QuestionnaireBuilder`, `AttachmentDisplay`/`AttachmentInput`, `PlanDefinitionBuilder`, `ResourceTable`/`ResourceForm` (generic FHIR resource CRUD UI), `AccessPolicy`-aware auth components under `auth/`.
- **Mock/synthetic FHIR data** (`packages/mock/src/test-resources`): realistic-shaped Patient/Encounter/Observation/etc. fixtures for demos and tests without any real PHI.
- **Example apps** (`examples/`): `foomedical` (full patient-portal reference app), `medplum-patient-intake-demo` (Questionnaire-driven intake), `medplum-eligibility-demo` (Coverage eligibility check), `medplum-provider` (clinician-facing app), `medplum-smart-on-fhir-demo` (SMART App Launch / EHR interoperability), `medplum-efax-demo` (fax integration).
- **Core SDK** (`packages/core`, `packages/fhirtypes`): typed FHIR client, resource types — ORM/backend-agnostic reference for how a FHIR-native data layer is shaped.

## Where things live
- `source/packages/definitions/src/fhir/r4/` — FHIR R4 schema, profiles, value sets, search parameters (standard + Medplum extensions).
- `source/packages/react/src/<ComponentName>/` — one folder per component, each with its own tests/stories.
- `source/packages/mock/src/test-resources/` — synthetic FHIR fixtures.
- `source/packages/app/src/` — web app shell; `src/lab/` is the lab-order/result UI area; `src/admin/`, `src/resource/` are generic admin/resource browsing.
- `source/examples/<name>/` — one directory per standalone example app/bot, each with its own README.
- `source/postgres/` — DB init scripts (included incidentally via sparse pattern; not a primary reason for acquisition).

## Do not copy
- Anything under `packages/app` or `packages/react` verbatim into the kit without re-checking for Medplum-specific branding/trademarks ("Medplum" wordmark, logo) — strip before reuse.
- Treat `AccessPolicy` as a *pattern* to learn from, not a resource to reproduce byte-for-byte — it is Medplum's proprietary extension to FHIR, not a standard resource.

## Notes
- License verdict verified against the actual `LICENSE.txt` in the clone (Apache License 2.0, standard text) and root `NOTICE` file (copyright + trademark notice for "Medplum"), not inferred from README badges.
- No `node_modules`, build artifacts, or binary media were pulled in; checkout is source/config/JSON/docs only.
- Everything under `source/` is reference material for learning FHIR-native app patterns, healthcare workflows, and React healthcare components — not copied into kit `features/`/`backend/` in this pass (those folders remain empty per the kit's current state).
