# BoxyHQ SaaS Starter Kit

| Field | Value |
|---|---|
| Source URL | https://github.com/boxyhq/saas-starter-kit |
| GitHub repository | `boxyhq/saas-starter-kit` (owner BoxyHQ, Organization repo) |
| Category | dashboards |
| License | Apache License 2.0 — `LICENSE.txt` (root `LICENSE`); no other license files or per-package licenses found |
| Author / organization | BoxyHQ |
| Acquired | 2026-09-26 |
| Revision | `abc9b686823cbfb4973c79bc36fea37a3244be6c` (main, committed 2026-05-08) |
| Attribution required | License notice only (Apache 2.0: preserve copyright/license notice and NOTICE if one existed — none present) |
| Status | extraction-safe — plain Apache 2.0, no Commons Clause or enterprise-tier split found in this checkout |

## Useful for
- Multi-tenant SaaS shell: teams/orgs, member roles, invitations — `models/team.ts`, `models/teamMember.ts`, `models/invitation.ts`, `pages/teams/[slug]`
- Auth: NextAuth wiring, SSO (SAML/OIDC via BoxyHQ Jackson), password reset, account lockout — `lib/nextAuth.ts`, `lib/jackson.ts`, `pages/auth/sso`, `lib/accountLock.ts`
- API keys & webhooks for a SaaS product — `models/apiKey.ts`, `components/apiKey/`, `components/webhook/`, `lib/svix.ts`
- Billing: Stripe subscriptions/customer portal — `lib/stripe.ts`, `sync-stripe.js`, `prisma/migrations/20240212105842_stripe`
- RBAC/permissions pattern — `lib/permissions.ts`, `lib/rbac.ts`
- SCIM provisioning — `pages/api/scim`

## Where things live
- `source/models/` — data-access functions per entity (account, team, teamMember, apiKey, invitation, subscription, price, session, user, verificationToken) — thin wrappers over Prisma, good reference for a Drizzle port
- `source/components/{account,apiKey,auth,billing,invitation,team,webhook,shared,layouts}/` — React components per feature area
- `source/pages/api/{auth,teams,invitations,sessions,webhooks,oauth,scim,well-known}/` — Next.js Pages Router API routes
- `source/lib/` — cross-cutting: `auth.ts`, `nextAuth.ts`, `session.ts`, `permissions.ts`, `rbac.ts`, `stripe.ts`, `svix.ts`, `jackson.ts`, `recaptcha.ts`, `slack.ts`, `retraced.ts`, `email/`, `zod/`
- `source/prisma/schema.prisma` — 15 models; `source/prisma/migrations/` — full migration history (SQL reference even off-Prisma)
- `source/locales/` — i18next translation files (many languages)

## Known dependencies
- `package.json`: next 15.5.14, react 18.3.1, next-auth 4.24.13, prisma/@prisma-client 6.10.0, tailwindcss 3.4.17 (v3, not v4), stripe 17.7.0, svix 1.89.0, @heroicons/react 2.2.0
- Uses Pages Router (not App Router) and Tailwind v3 — both mismatch our target stack (Next.js App Router + Tailwind v4 + shadcn/ui on Base UI); treat as pattern/logic reference, not drop-in UI

## Do not copy
- `prisma/` schema/migrations wholesale — target stack is Drizzle, not Prisma; port the entity shapes, not the ORM code
- UI components as-is — built on Tailwind v3 utility classes + Headless UI/custom markup, not shadcn/ui or Base UI; re-implement styling in the target design system
- `public/` — check for any stock/marketing imagery before reuse (not inspected in depth; low risk, not a focus of this repo)

## Notes
- No Commons Clause, BSL, or enterprise/"ee" split found — this is the full, single-tier open-source starter (unlike some BoxyHQ products that ship separate enterprise editions elsewhere).
- SSO/SCIM features depend on BoxyHQ's own Jackson service (`lib/jackson.ts`) — an external dependency, not bundled code; factor that in before promoting the SSO pieces.
- Strongest promote candidates are the *domain logic* (team/member/invitation/API-key/subscription models and their API routes), since the Next.js Pages Router + Tailwind v3 + Prisma combo doesn't match our stack directly.
