# General SaaS

The cross-cutting product layer every B2B SaaS application needs, independent of its vertical
(CRM, support, booking, ...). Depends on `shared.*` for auth, users, organizations, permissions,
audit log, notifications, billing, and file storage rather than redefining them; this domain adds
the SaaS-operator-specific layer on top: tenancy UX, plans/entitlements, usage metering, invites,
API keys, webhooks, an internal admin console, status/changelog, enterprise SSO/SCIM, data export,
and feature flags.

NACE: J62.01 (Computer programming activities) — approximate; this is a horizontal software
category describing the vendor's own activity, not a customer industry vertical.

## Product types

- Multi-tenant B2B SaaS applications (the layer sits under any vertical product built on this kit).
- Developer-facing / API-first products (weights API keys, webhooks, rate limiting more heavily).
- Enterprise-sold SaaS (weights SSO/SCIM, custom roles, data residency, SOC 2/ISO 27001 more heavily).

## Users

`tenant_owner` (billing/deletion authority) · `tenant_admin` (members, security config) ·
`tenant_member` (regular user) · `developer` (API integrator) · `platform_support` (vendor's own
internal ops/support staff) · `system` (automation: metering, webhook delivery).

## Workflows

Team invite lifecycle, API key lifecycle, webhook delivery, SSO connection setup, data export
request, workspace offboarding (deletion with export + grace period), status incident lifecycle.
See `workflows.json` for full steps and state machines.

## Core capabilities

- **Workspace management** — create/switch/configure a tenant workspace.
- **Team invites** — email invites with a pre-assigned role.
- **Plans & entitlements** — plan tiers gating features and limits.
- **API keys** — scoped programmatic-access credentials per workspace.
- **SSO (SAML)** — enterprise sign-in against the customer's IdP.
- **Billing portal** — self-serve subscription/invoice/payment-method management.

## Common capabilities

Onboarding flow, usage metering, webhooks, audit log viewer, seat management, SCIM provisioning,
self-serve data export, feature flags, trial management.

## Recommended / optional / premium

Public status page, custom roles (recommended); public changelog, sandbox environment (optional);
data residency controls (premium, enterprise).

## Compliance-sensitive areas

GDPR (data export, erasure, cross-border transfer), CCPA/CPRA (California residents' rights),
SOC 2 Type II and ISO/IEC 27001 (enterprise sales blockers, not self-certifiable — see
`compliance.json`'s disclaimer). None of these are satisfied merely by building a feature; an
actual attestation/certification requires an independent audit.

## Integrations

Payment/billing provider (Stripe Billing-style), SAML and SCIM identity providers (Okta,
Azure AD/Entra ID, OneLogin), webhook delivery infrastructure (Svix-style), the workspace's own
webhook receiver endpoint.

## Entities

`workspace`, `invitation`, `api_key`, `webhook_subscription`, `webhook_delivery`, `plan`,
`entitlement`, `usage_event`, `feature_flag`, `sso_connection`, `scim_connection`, `export_job`,
`status_incident`, `changelog_entry`.

## UI patterns

Workspace switcher in the app shell; settings organized as tabs (General, Members, Security,
Billing, API & Webhooks); a billing portal embedded or linked out to the payment provider's
hosted UI; a status page as a separate, unauthenticated public site; an admin console as a
completely separate, staff-only surface (never exposed to tenant users).

## Mobile

Rarely a dedicated mobile app for this layer itself; workspace switching and settings are
typically reachable from any vertical product's mobile app rather than being their own app.

## AI

Low-to-medium opportunity surface: anomaly detection on usage patterns, natural-language search
over the admin console or audit log, and drafting release notes for the changelog. Optional by
default per the product builder's AI policy.

## Standards referenced

GDPR (Regulation (EU) 2016/679), CCPA/CPRA (California Civil Code Title 1.81.5), SOC 2 Trust
Services Criteria (AICPA), ISO/IEC 27001:2022, SAML 2.0 Core (OASIS), OpenID Connect Core 1.0,
SCIM (RFC 7643/7644). See `sources.md` for verification method and license of each.

## Terminology

**Workspace** and **tenant** are used interchangeably; "workspace" is the product-facing term,
"tenant" the backend/architecture term. **Seat** = a licensed member slot under a plan.
**Entitlement** = a specific limit or capability a plan grants. **Entitlement** differs from
**usage** (`usage_event`): entitlements are the ceiling, usage events are the metered consumption
against it.
