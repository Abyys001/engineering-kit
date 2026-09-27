# Real Estate sources

Class, license, and what each source informed. Full records: `feature-map.json` → `sources`.

| ID | Title | Type | License | Local clone | Informed |
|---|---|---|---|---|---|
| `openproperty` | [OpenProperty](https://github.com/clawnify/OpenProperty) | implementation | MIT | — | `deposit_management`, `document_management`, `lease_management`, `maintenance_requests`, `offers_negotiation`, `owner_portal`, `property_listings`, `property_management_dashboard`, `rent_collection`, `rental_application_screening`, `tenant_management`, `tenant_portal` |
| `movinin` | [Movin' In (rental property management platform)](https://github.com/aelassas/movinin) | implementation | MIT | — | `lead_capture_inquiries`, `lease_management`, `listing_media`, `property_listings`, `tenant_portal`, `viewings_scheduling` |
| `easy-property-listings` | [Easy Property Listings (WordPress plugin)](https://github.com/easypropertylistings/Easy-Property-Listings) | implementation | GPL-2.0 | — | `agent_broker_directory`, `document_management`, `lead_capture_inquiries`, `lead_management_crm`, `listing_media`, `listing_syndication`, `mortgage_calculator`, `offers_negotiation`, `open_houses`, `property_listings`, `saved_searches_alerts`, `search_and_map`, `viewings_scheduling`, `virtual_tours_3d` |
| `reso-data-dictionary` | [RESO Data Dictionary / Web API](https://www.reso.org/data-dictionary/) | authoritative | Published by RESO (Real Estate Standards Organization); fields are openly documented for implementers, exact redistribution terms not independently re-verified this pass | — | `agent_broker_directory`, `brokerage_management`, `commission_tracking`, `fair_housing_compliance_screening`, `mls_idx_integration`, `price_recommendation_ai`, `property_listings`, `valuations_cma` |
| `schema-org-real-estate` | [schema.org RealEstateListing / Residence / Offer](https://schema.org/RealEstateListing) | authoritative | schema.org vocabulary is free to use; site content under CC BY-SA (per schema.org's stated terms; not independently re-verified live this pass) | — | `property_listings`, `search_and_map` |

## Notes per source

### openproperty
- Retrieved: 2026-09-27; version: a493028ad12ba969990ee916fbc8cd2a98807a2d
- Not cloned; inspected via GitHub API (root LICENSE file confirms MIT). Reference-only, extraction-safe if cloned later. Self-hosted rental property management (TenantCloud/AppFolio/Buildium alternative): units, tenants, leases, rent collection, maintenance work orders (`src/server/schema.sql`, `src/client/components/{tenants,leases,maintenance}`).

### movinin
- Retrieved: 2026-09-27; version: b9110a087406d3532f1337e47ff121c95dd659b7
- Not cloned; inspected via GitHub API (root LICENSE file confirms MIT). Reference-only. MERN-stack property rental platform with mobile app: `backend/src/models/{Property,Booking,Location,User}.ts` — confirms property type enum (House/Apartment/Townhouse/Plot/Farm/Commercial/Industrial) and a booking(lease)-style status lifecycle (Void/Pending/Deposit/Paid/Reserved/Cancelled).

### easy-property-listings
- Retrieved: 2026-09-27; version: master branch, 2026-09-26 snapshot
- Not cloned; inspected via GitHub API (`license.txt` confirms GPL-2.0). Reference-only (GPL). Mature real-estate-agency-specific listing plugin: post types for property/rental/land/commercial/business/contact (agent) confirm the sales-vs-rental listing split and an agent/contact entity distinct from the property-management-focused sources above.

### reso-data-dictionary
- Retrieved: 2026-09-27; version: Data Dictionary 2.1
- Industry-standard field/entity vocabulary (Property, Member, Office, OpenHouse, etc.) used by North American MLS systems. This session's sandboxed network blocked a live re-fetch of reso.org, so this is cited from well-established prior knowledge at medium confidence rather than high. Not to be confused with `NationalAssociationOfRealtors/reso-data-dictionary` on GitHub, which is a thin MIT-licensed OData client wrapper, not the dictionary itself.

### schema-org-real-estate
- Retrieved: 2026-09-27; version: schema.org current release
- Structured-data vocabulary for listing search-engine markup (RealEstateListing, Offer, Residence/Apartment/SingleFamilyResidence types). Live re-verification failed in this sandbox (network/TLS restrictions); treated as well-established from training knowledge.
