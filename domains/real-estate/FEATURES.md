# Real Estate features

Generated from `feature-map.json` (schema: `domains/_schema/SCHEMA.md`). 29 features.

## Core

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `real-estate.property_listings` Property listings | Create and manage for-sale/for-rent listings for a property or unit, with pricing and status. | high | none | none |
| `real-estate.listing_media` Listing media | Attach photos, floor plans, and video/virtual tours to a listing. | high | none | low |
| `real-estate.search_and_map` Search and map | Public-facing search with filters (price, beds, location) and a map view of results. | high | low | low |
| `real-estate.lead_capture_inquiries` Lead capture / inquiries | Capture a prospect's contact request against a listing. | high | low | low |
| `real-estate.viewings_scheduling` Viewings / showings | Schedule a property viewing between a prospect and an agent. | high | medium | low |
| `real-estate.agent_broker_directory` Agent / broker directory | Manage agents/brokers, their profile, license info, and listing assignments. | high | none | none |
| `real-estate.offers_negotiation` Offers and negotiation | Submit, counter, and accept/reject purchase or rental offers on a listing. | medium | low | low |
| `real-estate.lease_management` Lease management | Create and manage a lease/rental agreement between a tenant and a property/unit. | high | none | none |
| `real-estate.tenant_management` Tenant management | Track tenants, their contact info, lease history, and communication. | high | none | none |
| `real-estate.rent_collection` Rent collection | Generate rent invoices and collect recurring payments from tenants. | high | none | low |
| `real-estate.maintenance_requests` Maintenance requests | Let a tenant report an issue and track it through to resolution via a work order. | high | medium | low |

## Common

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `real-estate.saved_searches_alerts` Saved searches and alerts | Let a buyer/renter save a search and get notified of new matching listings. | medium | low | low |
| `real-estate.lead_management_crm` Lead / pipeline management | Track and follow up on leads through a pipeline (new, contacted, qualified, won, lost). | medium | none | medium |
| `real-estate.brokerage_management` Brokerage / agency management | Manage a multi-agent brokerage: office roster, listing assignment, commission splits. | medium | none | none |
| `real-estate.deposit_management` Security deposit management | Collect, hold, and reconcile a tenant's security deposit against a lease. | medium | none | none |
| `real-estate.property_management_dashboard` Owner portfolio dashboard | Give an owner a rollup view of their properties' occupancy, income, and maintenance status. | medium | none | low |
| `real-estate.document_management` Document management | Store lease agreements, disclosures, inspection reports, and other property documents. | high | none | low |
| `real-estate.owner_portal` Owner portal | Self-service access for an owner to view their properties, statements, and requests. | medium | none | none |
| `real-estate.tenant_portal` Tenant portal | Self-service access for a tenant to pay rent, view lease documents, and submit maintenance requests. | high | none | none |
| `real-estate.rental_application_screening` Rental application and screening | Collect a prospective tenant's application and run background/credit checks. | medium | none | medium |

## Recommended

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `real-estate.open_houses` Open houses | Publish a scheduled open-house event for a listing and track attendee sign-ins. | medium | low | none |
| `real-estate.listing_syndication` Listing syndication | Publish a listing out to third-party portals in addition to the operator's own site. | medium | none | none |
| `real-estate.commission_tracking` Commission tracking | Calculate and track agent/broker commission owed per closed transaction. | low | none | none |

## Optional

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `real-estate.valuations_cma` Valuations / comparative market analysis | Estimate a property's market value from comparable listings/sales. | low | none | high |
| `real-estate.mortgage_calculator` Mortgage / affordability calculator | Estimate monthly payments for a listed sale price given rate/term/down-payment inputs. | low | none | none |
| `real-estate.virtual_tours_3d` 3D / virtual tours | Embed a 3D walkthrough or 360° tour on a listing. | low | none | none |

## Premium

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `real-estate.price_recommendation_ai` AI price recommendation | Suggest a listing or renewal price using comparable listings and market trend data. | low | none | high |

## Compliance

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `real-estate.fair_housing_compliance_screening` Fair housing compliance screening | Flag listing copy or screening criteria that risks violating fair-housing / anti-discrimination rules. | low | none | medium |

## Integration

| Feature | Description | Confidence | Real-time | AI |
|---|---|---|---|---|
| `real-estate.mls_idx_integration` MLS / IDX feed integration | Pull in or syndicate listings via an MLS's IDX feed or RESO Web API. | high | none | none |
