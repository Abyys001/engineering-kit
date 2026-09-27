# Healthcare features

Generated from `feature-map.json` (schema: `domains/_schema/SCHEMA.md`). 28 features.

## Core

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `healthcare.patient_registration` Patient registration | Capture demographics, contact info, and identifiers for a new patient. | high | none | low |
| `healthcare.practitioner_directory` Practitioner directory | Manage clinicians, credentials, specialties, and their roles at organizations/locations. | high | none | none |
| `healthcare.organization_locations` Organizations and locations | Model clinics, departments, and physical locations/rooms a practice operates. | high | none | none |
| `healthcare.scheduling` Appointment scheduling | Define practitioner/room availability (Schedule/Slot) and book patient appointments. | high | medium | medium |
| `healthcare.encounters` Encounters / visits | Record a clinical encounter: type, participants, location, period, and reason. | high | low | low |
| `healthcare.clinical_notes` Clinical documentation | Structured/narrative visit notes (SOAP-style) attached to an encounter. | high | none | medium |
| `healthcare.problem_list` Problem list / conditions | Track a patient's active and historical diagnoses/conditions. | high | none | low |
| `healthcare.observations_vitals` Observations and vitals | Record discrete clinical measurements: vitals, exam findings, screening scores. | high | none | low |
| `healthcare.e_prescribing` E-prescribing | Create, route, and track medication orders/prescriptions electronically. | medium | low | medium |
| `healthcare.allergy_tracking` Allergy and intolerance tracking | Record allergies/intolerances with severity and reaction for safety checks. | high | none | low |
| `healthcare.billing_claims` Billing and insurance claims | Generate charges and submit insurance claims for rendered services. | high | none | low |

## Common

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `healthcare.patient_portal` Patient portal | Patient-facing web/mobile access to appointments, records, messages, and forms. | high | low | low |
| `healthcare.appointment_reminders` Appointment reminders | Automated SMS/email/push reminders and confirmations ahead of a visit. | medium | low | low |
| `healthcare.telehealth` Telehealth visits | Video/audio visits linked to an appointment and encounter, with a waiting room. | low | high | low |
| `healthcare.document_management` Clinical document management | Store and retrieve scanned documents, referral letters, and imported records. | high | none | low |
| `healthcare.lab_orders` Lab and diagnostic orders | Place orders for laboratory or diagnostic services against a patient. | high | medium | none |
| `healthcare.lab_results` Lab and diagnostic results | Receive, display, and flag lab/diagnostic results against the ordering request. | high | medium | medium |
| `healthcare.insurance_eligibility` Insurance eligibility verification | Check a patient's coverage and benefits before or at time of service. | high | low | none |
| `healthcare.patient_intake_forms` Digital intake forms | Structured questionnaires (history, consent, screening) completed before or at a visit. | high | none | low |

## Recommended

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `healthcare.care_team` Care team management | Track the group of practitioners/caregivers responsible for a patient's care. | medium | none | none |
| `healthcare.referrals` Referrals | Refer a patient to another practitioner, specialty, or organization. | medium | none | none |
| `healthcare.care_plans` Care plans | Structured goals, activities, and follow-up schedule for chronic or complex care. | medium | none | low |

## Optional

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `healthcare.immunizations` Immunization records | Track vaccines administered, including lot, site, and schedule adherence. | medium | none | none |
| `healthcare.waitlist` Appointment waitlist | Hold patients wanting an earlier slot and notify them when one opens. | low | medium | low |
| `healthcare.patient_invoicing` Patient invoicing and self-pay | Bill patients directly for co-pays, deductibles, or self-pay services. | low | none | none |

## Premium

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `healthcare.no_show_prediction` No-show risk scoring | Predict the likelihood a booked appointment will be missed to prioritize outreach. | low | none | high |

## Compliance

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `healthcare.patient_consent` Consent management | Record and enforce patient consent for treatment, data sharing, and communications. | high | none | none |
| `healthcare.access_policies` Fine-grained access policies | Restrict which users/roles can see which resources or data, beyond coarse RBAC. | medium | none | none |
