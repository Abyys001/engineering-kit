# General SaaS sources

Sources cited in this domain's provenance fields.

| ID | Title | Type | License | Retrieved | Local path |
|---|---|---|---|---|---|
| `boxyhq-saas-starter` | [BoxyHQ SaaS Starter Kit](https://github.com/boxyhq/saas-starter-kit) | implementation | Apache-2.0 | 2026-09-26 | `sources/dashboards/boxyhq-saas-starter/source` |
| `nextcrm` | [NextCRM](https://github.com/pdovhomilja/nextcrm-app) | implementation | MIT | 2026-09-26 | `sources/dashboards/nextcrm/source` |
| `unleash` | [Unleash](https://github.com/Unleash/unleash) | implementation | AGPL-3.0 | 2026-09-27 | — |
| `lago-api` | [Lago (billing API)](https://github.com/getlago/lago-api) | implementation | AGPL-3.0 | 2026-09-27 | — |
| `cachet` | [Cachet](https://github.com/CachetHQ/Cachet) | implementation | Custom (Cachet License, source-available, non-OSI, see LICENSE.md) | 2026-09-27 | — |
| `gdpr-2016-679` | [Regulation (EU) 2016/679 (General Data Protection Regulation)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679) | authoritative | EU official legislation; EUR-Lex reuse policy (CC BY 4.0 for reuse of Commission material unless stated otherwise) | 2026-09-26 | — |
| `ccpa-cpra` | [California Consumer Privacy Act of 2018 (as amended by CPRA), Civil Code Title 1.81.5](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=CIV&division=3.&title=1.81.5.&part=4.&chapter=&article=) | authoritative | Public — California state statutory text | 2026-09-26 | — |
| `soc2-tsc` | [2017 Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy (With Revised Points of Focus – 2022)](https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022) | authoritative | © AICPA & CIMA; freely downloadable resource, redistribution of the document itself not authorized | 2026-09-27 | — |
| `iso-27001-2022` | [ISO/IEC 27001:2022 — Information security management systems](https://www.iso.org/standard/27001) | authoritative | © ISO/IEC; standard text is paywalled, catalogue/summary page is public | 2026-09-27 | — |
| `scim-rfc` | [System for Cross-domain Identity Management (SCIM): Core Schema (RFC 7643) and Protocol (RFC 7644)](https://datatracker.ietf.org/doc/html/rfc7644) | authoritative | IETF Trust Legal Provisions — freely publishable | 2026-09-27 | — |
| `oidc-core` | [OpenID Connect Core 1.0 incorporating errata set 2](https://openid.net/specs/openid-connect-core-1_0.html) | authoritative | OpenID Foundation IPR policy — freely publishable, attribution required | 2026-09-27 | — |
| `saml-core-2.0` | [Assertions and Protocols for the OASIS Security Assertion Markup Language (SAML) V2.0](https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf) | authoritative | OASIS IPR Policy — freely publishable, attribution required | 2026-09-27 | — |

## Notes

- **`boxyhq-saas-starter`** (abc9b686823cbfb4973c79bc36fea37a3244be6c): Verified from repo LICENSE file (Apache-2.0) by an earlier session. Prisma schema: Team (tenant), TeamMember, Invitation, ApiKey, Subscription/Price/Service (billing). Webhooks via svix (pages/api/teams/[slug]/webhooks), SSO via BoxyHQ Jackson SAML (lib/jackson, pages/api/teams/[slug]/sso.ts), SCIM directory sync via Jackson dsync (pages/api/scim/v2.0/[...directory].ts), audit log via Retraced (lib/retraced.ts). No onboarding wizard, no platform-wide admin console/impersonation, no rate limiting found in this repo (checked by grep).
- **`nextcrm`** (b46b563b61c948a07a9cc5a340032444db1f8188): Cited here only for its ApiKeys model (prisma model ApiKeys: scope, provider, encryptedKey, per-user) as a second, independent API-key-management implementation. NextCRM is single-tenant (no Team/workspace model) so it does not inform tenancy/invite features.
- **`unleash`** (03aeb9b77428034f6311292fae7cbe558c13f847): Verified license from repo LICENSE file (AGPL-3.0, not Apache as sometimes assumed) via `gh api`; reference-only, never copy code. Inspected src/lib/types/model.ts remotely: FeatureToggle, IFeatureStrategy (strategies+constraints), IEnvironment, IProject, IVariant — feature-flag data model.
- **`lago-api`** (46b1398eda4fd0eb72c90577930c4febb0264146): Verified license from repo LICENSE file (AGPL-3.0) via `gh api`; reference-only, never copy code. Inspected app/models remotely: BillableMetric, Event, DailyUsage, Plan, Entitlement, Wallet, UsageThreshold — usage-metering and plan-entitlement data model.
- **`cachet`** (3.x branch): Custom non-OSI license verified from LICENSE.md via `gh api` (GitHub reports NOASSERTION); reference-only, never copy code. Used only as a single reasoned reference for the shape of a public status/incident page (components, incidents, subscribers). Not independently cross-referenced against a second status-page implementation, so status_page confidence is capped at low-medium.
- **`gdpr-2016-679`** (OJ L 119, 4.5.2016; CELEX 32016R0679): Verified live via WebFetch: title and CELEX number confirmed.
- **`ccpa-cpra`** (Civil Code 1798.100-1798.199.100, amended through 2025): Verified live via WebFetch: exact title heading confirmed.
- **`soc2-tsc`** (2017 TSC with 2022 revised points of focus): Verified via web search matching exact document title and URL on aicpa-cima.com.
- **`iso-27001-2022`** (2022 edition (3rd edition), amended by Amd 1:2024): iso.org blocks direct automated fetches (HTTP 403); verified the exact title and URL via web search results instead of direct fetch.
- **`scim-rfc`** (RFC 7643 / RFC 7644, September 2015): Both RFC 7643 (Core Schema) and RFC 7644 (Protocol) verified live via WebFetch (exact titles and dates confirmed).
- **`oidc-core`** (errata set 2, 2023-12-15): Verified live via WebFetch: exact title and date confirmed.
- **`saml-core-2.0`** (OASIS Standard, 15 March 2005): URL confirmed reachable (WebFetch retrieved a genuine 615.6KB PDF); binary content could not be parsed to text by the fetch tool, title/date is from well-established public record of this OASIS Standard's identifier.
