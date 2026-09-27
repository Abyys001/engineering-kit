# Real Estate

Property listing/search for buyers and renters, plus rental property management: leases, tenants, rent collection, and maintenance. Two product archetypes cross-cut this domain — a public-facing listing/marketplace site and an operator-facing property-management back office — and most products lean toward one or blend both. No repository was cloned for this domain; researched via GitHub API inspection of actual schemas/models (see `sources.md`).

## Product types
Consumer listing/search portals, agent/brokerage CRM & listing management, rental property management platforms (owner/tenant self-service), and MLS-integrated agent tools.

## Users
Buyer/renter, property owner/landlord, agent, broker, property manager, tenant, maintenance vendor (partner), leasing/listing admin, compliance officer, system/integration account. See `roles.json`.

## Core workflows
Listing lifecycle, lead-to-viewing, offer negotiation, lease lifecycle, rent collection, maintenance request handling, tenant application/screening. State machines are informed by the three reference implementations (medium confidence — no external standard fixes these enums the way FHIR does for healthcare).

## Capabilities
- **Core**: property listings, listing media, search & map, lead capture, viewings/showings, agent/broker directory, offers & negotiation, lease management, tenant management, rent collection, maintenance requests.
- **Common**: saved searches/alerts, lead pipeline (CRM), brokerage management, deposit management, owner portfolio dashboard, document management, owner/tenant portals, rental application & screening.
- **Recommended/optional**: open houses, valuations/CMA, mortgage calculator, listing syndication, 3D/virtual tours, commission tracking.
- **Integration**: MLS/IDX feed sync.
- **Compliance-classified**: fair-housing compliance screening.
- **Premium**: AI price recommendation.

Full list with confidence/tags: `FEATURES.md`.

## Compliance-sensitive areas
Fair Housing Act (US, high confidence — governs listing copy and screening criteria), GDPR (EU/EEA, buyer/tenant personal data), AML obligations for estate/letting agents (UK/EU example, jurisdiction-specific), tenant deposit protection schemes (not universal — UK example given), property/seller disclosure requirements (varies sharply by jurisdiction). All `requires_human_review: true`; see `compliance.json` disclaimer.

## Integrations
MLS/IDX feed (RESO Web API), listing portal syndication (Zillow/Realtor.com-style), mapping/geocoding, payment gateway (rent/deposits), e-signature (leases), background/credit check screening, SMS/email gateway, 3D virtual tour hosting.

## Entities
Property, Unit, MediaAsset, Listing, Agent, Brokerage, Lead, Viewing, OpenHouse, Offer, Lease, Tenant, RentPayment, MaintenanceRequest, SecurityDeposit, Document, SavedSearch, Valuation. Property/Listing/Agent/Brokerage/OpenHouse map to RESO Data Dictionary concepts; Listing also maps to schema.org's `RealEstateListing` — see `entities.json` `standard_mapping`.

## UI patterns
Map + list split-view search, listing detail gallery/carousel, lead inbox, calendar-based viewing scheduler, kanban-style offer/lease pipeline, tenant/owner dashboard with statements, maintenance ticket board.

## Mobile
Buyer/renter search and saved-search alerts, and the tenant portal (rent payment, maintenance requests) are the primary mobile surfaces.

## AI
Discriminatory-language detection in listing copy, automated valuation/price recommendation, late-payment risk prediction, application risk scoring, no-show risk for viewings — all `ai_relevance: medium` or higher, none `core`.

## Standards
RESO Data Dictionary/Web API (Property, Member, Office, OpenHouse concepts; North American MLS standard) and schema.org `RealEstateListing`/`Residence`/`Offer` (search-engine structured-data vocabulary). Both are real, well-established standards, but this pass could not independently re-verify their publisher pages live (sandboxed network blocked outbound fetches to non-GitHub hosts), so they're cited at `medium` confidence with that caveat noted in `sources.md`.

## Terminology
MLS (Multiple Listing Service), IDX (Internet Data Exchange), CMA (comparative market analysis), AVM (automated valuation model), listing (a published ad) vs. property/unit (the underlying asset).

## Sources
OpenProperty (MIT, extraction-safe if cloned), Movin' In (MIT, extraction-safe if cloned), Easy Property Listings (GPL-2.0, reference-only), plus RESO Data Dictionary and schema.org RealEstateListing standards. Details: `sources.md`.
