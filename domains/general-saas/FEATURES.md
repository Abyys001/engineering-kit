# General SaaS features

Generated from `feature-map.json`. See `DOMAIN.md` for narrative context.

## Core

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `general-saas.workspace_management` Workspace management | Create, rename, and switch between tenant workspaces; manage workspace-level settings and branding. | medium | boxyhq-saas-starter |
| `general-saas.team_invites` Team invites | Invite people to a workspace by email with a pre-assigned role; manage pending, accepted, and expired invitations. | medium | boxyhq-saas-starter |
| `general-saas.plans_entitlements` Plans and entitlements | Subscription plan tiers with feature gating and usage/seat limits enforced per workspace. | medium | boxyhq-saas-starter, lago-api |
| `general-saas.api_keys` API keys | Issue and revoke scoped API keys per workspace for programmatic access, with prefix display and last-used tracking. | medium | boxyhq-saas-starter, nextcrm |
| `general-saas.admin_console` Internal admin console | An internal, staff-only console for searching tenants, viewing account health, and taking support actions across workspaces. | low | soc2-tsc |
| `general-saas.billing_portal` Self-serve billing portal | Let a workspace owner view invoices, update payment method, and upgrade/downgrade/cancel their subscription. | medium | boxyhq-saas-starter |

## Common

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `general-saas.onboarding_flow` Guided onboarding | A first-run setup wizard that walks a new workspace owner through initial configuration after signup. | low | boxyhq-saas-starter |
| `general-saas.usage_metering` Usage metering | Record usage events (API calls, seats, storage, etc.) per workspace to drive limits, alerts, and usage-based billing. | low | lago-api |
| `general-saas.webhooks` Outbound webhooks | Let a workspace subscribe to product events and receive signed HTTP callbacks, with delivery retry and a delivery log. | low | boxyhq-saas-starter |
| `general-saas.sso_saml` SSO (SAML) | Enterprise single sign-on into a workspace via SAML 2.0 against the customer's identity provider. | high | boxyhq-saas-starter, saml-core-2.0 |
| `general-saas.data_export` Self-serve data export | Let a workspace owner export their tenant's data (CSV/JSON) for backup or portability. | medium | gdpr-2016-679 |
| `general-saas.feature_flags` Feature flags | Toggle features on/off or roll them out gradually, targeted by workspace, user segment, or environment. | low | unleash |
| `general-saas.audit_log_viewer` Audit log viewer | A workspace-scoped UI over the audit log with filters, search, and export, for admins to review who changed what. | low | boxyhq-saas-starter |
| `general-saas.seat_management` Seat management | Track seats included in a plan, assign/reclaim seats as members are invited or removed, and show pending vs active seat counts. | medium | boxyhq-saas-starter, lago-api |
| `general-saas.trial_management` Trial management | Time-boxed free trial on a paid plan with expiration handling and trial-to-paid conversion prompts. | low | boxyhq-saas-starter |

## Recommended

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `general-saas.status_page` Public status page | A public page showing current system status, component health, and incident history, with subscriber notifications. | low | cachet |
| `general-saas.scim_provisioning` SCIM provisioning | Automatic user provisioning and deprovisioning into a workspace from the customer's identity provider via SCIM. | high | boxyhq-saas-starter, scim-rfc |
| `general-saas.custom_roles` Custom roles | Let a workspace define its own roles and permission sets beyond the built-in owner/admin/member roles. | low | boxyhq-saas-starter |

## Optional

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `general-saas.changelog` Public changelog | A public or in-app feed of shipped changes and release notes, often paired with an unread-updates indicator. | low | boxyhq-saas-starter |
| `general-saas.sandbox_environment` Sandbox / test environment | A separate test workspace or API mode with synthetic data, isolated from production, for integration testing. | low | boxyhq-saas-starter |

## Premium

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `general-saas.data_residency` Data residency controls | Let an enterprise workspace pin where its data is stored/processed (e.g. EU vs US region) to satisfy jurisdictional requirements. | low | gdpr-2016-679, iso-27001-2022 |

## Compliance

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `general-saas.workspace_deletion_export` Workspace deletion with export | Let a workspace owner delete their workspace, with a data export offer and a grace period before hard deletion, supporting the right to erasure. | medium | boxyhq-saas-starter, gdpr-2016-679 |

## Infrastructure

| Feature | Description | Confidence | Sources |
|---|---|---|---|
| `general-saas.public_api_rate_limiting` Public API rate limiting | Per-key and per-plan request rate limits on the public API, with standard rate-limit response headers. | low | boxyhq-saas-starter |

