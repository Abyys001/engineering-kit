# ENGINEERING-KIT ACQUISITION, CURATION & AUTONOMOUS PROJECT BUILDER

> Adopted 2026-09-26. The §47 initial acquisition ran that day — don't re-run it; refresh individual sources as described in the kit README.

You already have my Master Engineering Policy and the local engineering-kit at:

```text
~/Projects/engineering-kit
```

That policy remains the source of truth for architecture and technology choices.

Your job now is to populate, organize, curate, and continuously use the engineering-kit as my local reusable development system.

---

# 1. PRIMARY OBJECTIVE

Turn:

```text
~/Projects/engineering-kit
```

into a high-quality local engineering library that allows you to:

* reuse existing code
* reuse UI components
* reuse complete features
* reuse architecture patterns
* reuse starter projects
* reduce token usage
* reduce repetitive coding
* avoid rebuilding common functionality
* create visually different applications
* make autonomous architectural decisions
* understand the full scope of a project
* build related services in the correct order
* use the closest reusable implementation instead of starting from zero

The engineering-kit is not a random collection of GitHub repositories.

It must become a **curated, normalized, production-oriented personal engineering library**.

---

# 2. SOURCE COLLECTIONS

Create a dedicated source area inside the engineering-kit:

```text
~/Projects/engineering-kit/sources/
```

Organize it by category:

```text
sources/
├── web/
├── dashboards/
├── ai/
├── backend/
├── mobile/
├── registries/
└── references/
```

Do NOT mix downloaded upstream repositories directly with my cleaned reusable templates.

Use:

```text
sources/
```

for upstream/reference material.

Use:

```text
components/
features/
starters/
backend/
mobile/
ai/
patterns/
```

for our cleaned and curated implementations.

---

# 3. DOWNLOAD POLICY

Download/clone the following resources.

Use shallow Git clones where possible:

```bash
git clone --depth 1 ...
```

Do NOT install their dependencies just to download them.

Do NOT run:

```text
npm install
pnpm install
yarn
bun install
flutter pub get
pip install
```

unless it is genuinely necessary to inspect or validate a specific implementation.

The initial objective is source acquisition and curation, not running every repository.

---

# 4. WEB UI SOURCES

## 4.1 shadcn/ui

Official repository:

```text
https://github.com/shadcn-ui/ui
```

Purpose:

Base UI system and canonical component patterns.

Use it as the foundational reference for:

* buttons
* forms
* dialogs
* sheets
* dropdowns
* navigation
* sidebar
* tables
* calendars
* command interfaces
* feedback
* layout primitives
* accessibility patterns

The official repository is MIT licensed.

Do not blindly copy the entire repository into a project.

Extract and curate useful components.

---

# 5. ORIGIN UI

Repository:

```text
https://github.com/shadcn/originui
```

Purpose:

Large collection of application-oriented components.

Use especially for:

* advanced forms
* inputs
* date/time inputs
* navigation
* filters
* complex controls
* data display
* application UI
* polished SaaS components

Origin UI follows shadcn-style copy/paste conventions.

Its repository is MIT licensed.

Treat it as a major component source.

---

# 6. CULT UI

Repository:

```text
https://github.com/nolly-studio/cult-ui
```

Purpose:

Distinctive and more experimental/creative UI components.

Use especially for:

* animated interfaces
* special cards
* modern interactions
* landing pages
* premium-looking UI
* design-heavy sections
* interactive controls

Cult UI is MIT licensed.

Do NOT use it blindly for every project.

Choose it when its visual style fits the product.

---

# 7. KOKONUT UI

Repository:

```text
https://github.com/kokonut-labs/kokonutui
```

Purpose:

Modern polished components based on:

* Tailwind CSS
* shadcn/ui
* Motion

Use it especially for:

* dashboards
* SaaS interfaces
* cards
* navigation
* animations
* modern sections
* visual polish

Kokonut UI is MIT licensed.

Use it as a source of design alternatives rather than making it the default visual identity of every application.

---

# 8. REACT BITS

Repository:

```text
https://github.com/epodak/reactbits
```

Purpose:

Creative animated React components.

Use especially for:

* hero sections
* text animation
* scroll effects
* backgrounds
* interactive sections
* marketing pages
* visual enhancement

React Bits provides TypeScript/Tailwind variants and is MIT licensed.

Use animation deliberately.

Do not add animation just because it exists.

---

# 9. TREMOR

Repository:

```text
https://github.com/tremorlabs/tremor
```

Purpose:

Analytics and dashboard UI.

Use especially for:

* charts
* KPI cards
* metrics
* analytics dashboards
* tables
* monitoring
* business reporting

Tremor is Apache 2.0 licensed.

Record its license information in the source metadata.

---

# 10. NEXT SHADCN DASHBOARD

Repository:

```text
https://github.com/shadcndashboard/next-shadcn-dashboard
```

Purpose:

Admin dashboards and application shell reference.

Use especially for:

* dashboard structures
* navigation
* sidebar
* tables
* forms
* analytics pages
* settings
* reusable admin layouts

License:

MIT.

IMPORTANT:

The repository states that attribution is required.

Preserve and document any attribution requirement when extracting code.

Do not remove legal notices blindly.

---

# 11. KIRANISM DASHBOARD

Repository:

```text
https://github.com/Kiranism/next-shadcn-dashboard-starter
```

Purpose:

Advanced dashboard and SaaS patterns.

Use especially for:

* admin dashboard architecture
* data tables
* filters
* forms
* billing UI
* settings
* navigation
* reusable application layouts

License:

MIT.

Use it as a strong reference for complete dashboard patterns.

Do not copy project-specific business logic.

---

# 12. SHADCN CHATBOT TEMPLATE

Repository:

```text
https://github.com/shadcn-ui/chatbot-template
```

Purpose:

Modern AI UI.

Use especially for:

* chat UI
* streaming messages
* tool calls
* message parts
* citations
* questionnaire UI
* AI interaction patterns

License:

MIT.

Extract reusable UI and interaction patterns.

Do not automatically use the entire Vercel AI Gateway architecture in every project.

---

# 13. VERCEL CHATBOT

Repository:

```text
https://github.com/vercel/chatbot
```

Purpose:

Advanced reference for real-world AI application UX and architecture.

Use especially for:

* AI chat UX
* artifacts
* streaming
* tool UI
* message rendering
* AI application architecture
* testing
* Next.js integration
* Drizzle patterns

License:

Apache 2.0.

Use this primarily as a reference and source of reusable patterns.

Do not force its complete architecture into every AI project.

---

# 14. FLUTTER SOURCE

Repository:

```text
https://github.com/MiguelCovarrubiasdaiz/flutter-structure
```

Purpose:

Flutter starter and architecture reference.

Use especially for:

* feature-first architecture
* Clean Architecture
* Riverpod
* go_router
* Dio
* widget kit
* error handling
* networking
* localization
* testing
* theming
* configuration
* AI-agent-friendly project structure

License:

MIT.

Use it as a major reference for the Flutter starter.

Do not blindly copy every example feature.

Extract the architecture and reusable building blocks that fit our Flutter policy.

---

# 15. NESTJS STARTER

Repository:

```text
https://github.com/hmake98/nestjs-starter
```

Purpose:

Backend infrastructure reference.

Use especially for:

* NestJS structure
* JWT authentication
* RBAC
* Redis
* BullMQ
* structured logging
* request correlation IDs
* health checks
* Swagger/OpenAPI
* validation
* rate limiting
* testing
* Docker
* CI

License:

MIT.

IMPORTANT:

It uses Prisma.

Our standard is:

```text
Drizzle ORM
```

Therefore:

DO NOT adopt Prisma as our backend standard.

Instead:

* inspect the architecture
* extract useful patterns
* adapt database code to Drizzle
* preserve our master engineering policy

---

# 16. FASTAPI FULL STACK TEMPLATE

Repository:

```text
https://github.com/fastapi/full-stack-fastapi-template
```

Purpose:

Python/FastAPI reference.

Use especially for:

* FastAPI structure
* authentication
* JWT
* email flows
* Docker
* CI/CD
* testing
* frontend/backend integration
* configuration
* deployment patterns

License:

MIT.

IMPORTANT:

The template uses SQLModel.

Our Python AI stack should not automatically adopt SQLModel.

Our database policy remains:

```text
PostgreSQL
```

and our project-specific data layer should follow the engineering policy.

Use this repository primarily as a reference for FastAPI production structure.

---

# 17. SHADCN REGISTRY TEMPLATE

Repository:

```text
https://github.com/shadcn-ui/registry-template
```

Purpose:

Potential future personal component registry.

Study and preserve the architecture needed to eventually create:

```text
@siavash/*
```

or another private/personal component registry.

The official shadcn registry system can distribute much more than simple components, including:

* components
* hooks
* utilities
* pages
* templates
* configuration
* docs
* rules
* workflows

This is important for the long-term evolution of the engineering-kit.

Do NOT implement the registry immediately unless there is enough curated content to justify it.

---

# 18. SOURCE METADATA

For every downloaded repository, create metadata.

Example:

```text
sources/web/originui/
├── source/
├── SOURCE.md
└── LICENSE.txt
```

`SOURCE.md` must contain:

* project name
* source URL
* GitHub repository
* category
* license
* original author/organization
* date acquired
* commit SHA or version/tag used
* what it is useful for
* known dependencies
* whether attribution is required
* whether it is reference-only or extraction-safe
* notes about anything that must not be copied

Record the exact revision used whenever practical.

---

# 19. LICENSE POLICY

For reusable code intended for my commercial projects:

Prefer:

* MIT
* Apache 2.0
* BSD
* ISC

Do not import code with GPL/AGPL/copyleft licensing into the reusable production kit by default.

If a source has:

* unusual licensing
* attribution requirements
* non-commercial restrictions
* redistribution restrictions
* unclear licensing
* mixed licenses
* third-party assets with separate licenses

do NOT silently extract it.

Instead mark it:

```text
REVIEW_REQUIRED
```

and document the issue.

License information must remain attached to extracted reusable source where legally required.

---

# 20. DO NOT CREATE A GIANT COPY OF THE INTERNET

Do not copy every component from every repository.

The goal is not:

```text
1000 duplicate components
```

The goal is:

```text
a small number of high-quality reusable building blocks
```

When multiple sources implement essentially the same thing:

Compare them.

Select the most useful implementation.

Keep alternatives only when they provide meaningfully different behavior or visual style.

---

# 21. CURATION PROCESS

Every source should go through:

```text
DOWNLOAD
    ↓
INSPECT
    ↓
CLASSIFY
    ↓
LICENSE CHECK
    ↓
REMOVE PROJECT-SPECIFIC LOGIC
    ↓
REMOVE UNNECESSARY DEPENDENCIES
    ↓
ADAPT TO OUR STACK
    ↓
CLEAN NAMING
    ↓
TYPECHECK
    ↓
TEST WHERE APPROPRIATE
    ↓
DOCUMENT
    ↓
PROMOTE TO ENGINEERING-KIT
```

Do not consider downloaded source to be production-ready just because the original repository is popular.

---

# 22. ENGINEERING-KIT DESTINATION CATEGORIES

Promote curated code into the correct area.

### UI Components

```text
~/Projects/engineering-kit/components/web/
```

Examples:

* buttons
* inputs
* dialogs
* sidebars
* charts
* cards
* command menus
* data tables
* animations

### Features

```text
~/Projects/engineering-kit/features/
```

Examples:

* authentication
* user management
* dashboard
* settings
* billing
* notifications
* search
* filtering
* file upload
* AI chat

### Backend

```text
~/Projects/engineering-kit/backend/
```

Examples:

* authentication
* authorization
* logging
* audit logs
* permissions
* jobs
* file storage
* notifications

### Mobile

```text
~/Projects/engineering-kit/mobile/
```

### AI

```text
~/Projects/engineering-kit/ai/
```

### Starters

```text
~/Projects/engineering-kit/starters/
```

### Patterns

```text
~/Projects/engineering-kit/patterns/
```

---

# 23. NORMALIZATION RULE

The engineering-kit must not become dependent on the original repository's internal structure.

Example:

Do NOT leave:

```text
components/from-kokonut/project-specific-name.tsx
```

if that name only makes sense inside the source repository.

Instead normalize it into:

```text
components/web/cards/animated-stat-card.tsx
```

Use names based on what the component does.

The same principle applies to features and backend modules.

---

# 24. REUSABLE COMPONENT RULE

Each curated component should ideally:

* use our standard stack
* have clean TypeScript
* expose clear props
* have minimal dependencies
* avoid unnecessary application-specific assumptions
* work independently
* be easy for Claude to understand
* be easy to copy into a project
* be documented briefly

Do not create a component that requires importing half of a source repository.

---

# 25. VARIATION SYSTEM

A major requirement:

Do NOT generate the same visual interface for every project.

The stack should remain consistent.

The design should not.

Use the available component sources to create meaningful visual variation.

Variation may include:

* different sidebar styles
* different navigation patterns
* different card styles
* different dashboard layouts
* different hero layouts
* different table compositions
* different typography hierarchy
* different spacing density
* different animation levels
* different chart layouts
* different empty states
* different page composition
* different mobile navigation
* different filter placement

Do not make the interface random.

Variation must be driven by:

* product type
* target users
* domain
* expected workflows
* information density
* branding
* platform
* purpose of the page

The architecture remains standardized.

The visual composition may vary.

---

# 26. DESIGN VARIETY RULE

When building multiple applications:

Do not repeatedly produce:

```text
sidebar
topbar
4 cards
large table
same chart
```

unless that structure genuinely fits the product.

For example:

A trading platform may prefer:

```text
dense workspace
charts
toolbars
watchlists
side panels
activity feeds
```

A CRM may prefer:

```text
pipeline
filters
customer table
detail drawer
activity timeline
```

A finance dashboard may prefer:

```text
metrics
charts
cash flow
transactions
alerts
```

A content platform may prefer:

```text
content cards
editor
calendar
media library
publishing queue
```

A mobile consumer application may need:

```text
bottom navigation
tabs
full-screen flows
gesture-friendly interactions
```

Choose the structure based on the actual product.

---

# 27. AUTONOMOUS PROJECT ANALYSIS

When I say:

> Build me an application for X

do NOT interpret that as:

> only create the page I mentioned.

Instead determine the likely system required to make the product functional.

Analyze:

### Frontend

Does it need:

* public website?
* landing page?
* login?
* dashboard?
* admin panel?
* settings?
* profile?
* billing?
* notifications?
* reports?
* analytics?
* content management?
* search?
* file management?

### Backend

Does it need:

* API?
* authentication?
* authorization?
* roles?
* database?
* background jobs?
* notifications?
* file storage?
* audit logs?
* integrations?
* webhooks?

### Mobile

Does the product naturally require:

* Android/iOS?
* customer application?
* employee/technician application?
* admin mobile?
* push notifications?
* offline support?

### AI

Does the product benefit from:

* chat?
* extraction?
* classification?
* recommendations?
* RAG?
* document processing?
* AI assistant?
* agents?
* automation?

### Infrastructure

Does it need:

* PostgreSQL?
* Redis?
* queue workers?
* object storage?
* reverse proxy?
* Docker?
* CI/CD?
* monitoring?

Determine this before implementation.

---

# 28. DO NOT ASK OBVIOUS QUESTIONS

Do not ask me for information that can reasonably be inferred from the product requirements.

For example:

If I say:

> Build a SaaS platform for exchange businesses.

You should already infer that it likely needs:

* web application
* authentication
* roles/permissions
* dashboard
* backend API
* PostgreSQL
* admin functionality
* settings
* business data management

Use your engineering judgment.

---

# 29. WHEN TO ASK

Ask a question only when the missing information is genuinely blocking an important architectural or business decision.

Examples:

* Is mobile actually required?
* Should this support multiple organizations/tenants?
* Is payment required?
* Is AI a core feature or optional?
* Is the application public or internal?
* Is this a prototype or production system?

If a reasonable assumption can be made safely, make the assumption and continue.

State important assumptions briefly.

Do not stop the whole implementation because of minor uncertainty.

---

# 30. AUTONOMOUS IMPLEMENTATION CHAIN

Once the project scope is clear, build the project in a sensible dependency order.

Typical chain:

```text
1. Project classification
        ↓
2. Architecture decision
        ↓
3. Select starter
        ↓
4. Select reusable components
        ↓
5. Database schema
        ↓
6. Backend foundation
        ↓
7. Authentication / authorization
        ↓
8. Core API
        ↓
9. Frontend foundation
        ↓
10. Shared UI
        ↓
11. Feature implementation
        ↓
12. Mobile app if required
        ↓
13. AI service if required
        ↓
14. Background jobs
        ↓
15. Integration
        ↓
16. Validation
        ↓
17. Tests
        ↓
18. Docker
        ↓
19. CI/CD
        ↓
20. Documentation
```

Adjust the order when the project needs a different dependency graph.

The important rule is:

**Build dependencies before dependent features.**

---

# 31. CROSS-SYSTEM THINKING

Do not build each layer as an isolated project.

For example:

If a mobile app needs user authentication:

```text
Database
   ↓
Backend auth
   ↓
API
   ↓
Mobile networking
   ↓
Mobile auth state
   ↓
Protected screens
```

Build the dependency chain coherently.

Similarly:

```text
AI feature
   ↓
AI API
   ↓
Queue/worker if needed
   ↓
Main backend integration
   ↓
Web/mobile UI
```

Do not create disconnected placeholder APIs unless explicitly requested.

---

# 32. FULL-PROJECT THINKING

When I request a complete application, think at system level.

Do not stop after:

```text
UI completed
```

Check whether the project also needs:

* data model
* API
* auth
* permissions
* persistence
* background jobs
* error handling
* validation
* testing
* deployment
* monitoring
* documentation

The goal is to maximize useful completion without requiring me to explicitly enumerate every obvious subsystem.

---

# 33. EXISTING PROJECT RULE

When working in an existing project:

First inspect:

```text
current project
```

Then:

```text
~/Projects/engineering-kit
```

Never replace working project architecture merely because a newer template exists.

Respect existing project constraints unless migration is explicitly requested.

---

# 34. NEW PROJECT RULE

When creating a NEW project:

1. classify it
2. choose the correct stack
3. inspect the matching starter
4. inspect reusable components
5. inspect reusable features
6. build the foundation
7. adapt the UI to the product
8. connect backend/frontend/mobile/AI where necessary
9. test
10. document

Do not build everything from scratch unless no suitable reusable foundation exists.

---

# 35. TOKEN-EFFICIENCY RULE

Minimize unnecessary context.

When working with a source repository:

* read targeted files
* inspect only required directories
* avoid loading the entire repository into context
* use metadata and READMEs first
* inspect implementations only when needed
* reuse known templates
* do not repeatedly rediscover the same code
* use local files rather than repeating source code in the conversation

For a large repository, identify the relevant files first.

Do not recursively dump the entire source tree into the context.

---

# 36. LOCAL-FIRST RULE

Always prefer:

```text
Current Project
      ↓
~/Projects/engineering-kit
      ↓
Already downloaded source repositories
      ↓
Official documentation
      ↓
External search
      ↓
New implementation
```

The engineering-kit is intentionally local so that repeated work becomes cheaper in both time and tokens.

---

# 37. SOURCE-TO-TEMPLATE PROMOTION

Do not use upstream repositories directly as the application's final architecture.

Instead:

```text
source repository
       ↓
selected implementation
       ↓
cleaning
       ↓
normalization
       ↓
our conventions
       ↓
engineering-kit
       ↓
project
```

This creates independence from the original project.

---

# 38. TEMPLATE QUALITY GATE

Before promoting anything into the engineering-kit, check:

* Is it actually reusable?
* Does it match our stack?
* Are dependencies necessary?
* Is it understandable?
* Is it appropriately isolated?
* Is licensing documented?
* Does it need attribution?
* Does it introduce architectural conflicts?
* Does it contain project-specific code?
* Does it have tests where useful?
* Is it better than what we already have?

If not, do not promote it.

---

# 39. DUPLICATE DETECTION

Do not create multiple nearly identical implementations.

Before adding something:

Search:

```text
~/Projects/engineering-kit
```

for similar components/features.

If a similar implementation exists:

* improve it,
* generalize it,
* or document the difference.

Do not create unnecessary duplicates.

---

# 40. ENGINEERING-KIT INDEX

Create and maintain an index:

```text
~/Projects/engineering-kit/INDEX.md
```

This is extremely important.

The index should help an AI agent quickly understand what exists.

For each reusable item record:

* name
* category
* purpose
* path
* source
* dependencies
* license
* when to use
* when NOT to use
* related components
* related features
* supported platform

Example:

```text
## Animated KPI Card

Path:
components/web/data-display/animated-kpi-card

Use when:
- dashboard has important KPI metrics
- subtle animation adds value

Avoid when:
- dashboard is extremely dense
- animation would distract

Source:
Kokonut UI

License:
MIT
```

Keep the index concise.

---

# 41. SEARCHABLE CATALOG

Also maintain:

```text
~/Projects/engineering-kit/catalog.json
```

The catalog should contain structured metadata that Claude can search quickly.

Each entry should have fields similar to:

```json
{
  "name": "animated-kpi-card",
  "category": "web-component",
  "path": "components/web/data-display/animated-kpi-card",
  "tags": [
    "dashboard",
    "analytics",
    "metrics",
    "animation"
  ],
  "source": "kokonutui",
  "license": "MIT",
  "dependencies": [],
  "use_cases": [
    "dashboard metrics"
  ]
}
```

Keep this machine-readable.

---

# 42. PROJECT BLUEPRINT THINKING

For every new application, create a lightweight internal project blueprint before substantial implementation.

The blueprint should identify:

```text
Product type
Frontend
Backend
Database
Authentication
Authorization
Mobile
AI
Workers
Storage
Integrations
Deployment
Testing
```

Do not make this a huge document.

Its goal is to prevent missing important parts.

---

# 43. OUTPUT BEHAVIOR

When I ask you to build a project, do not respond only with:

> "Here is the code for X."

Instead, reason about the complete system.

You should naturally identify:

* what the product needs
* what stack applies
* what reusable assets already exist
* what needs to be created
* what can be reused
* what needs to be integrated
* what should be deferred

Then proceed.

---

# 44. MAXIMUM-AUTONOMY RULE

My intent is for you to perform as much useful engineering work as possible without requiring me to micromanage implementation details.

Therefore:

DO:

* infer obvious requirements
* inspect the repository
* inspect the engineering-kit
* select components
* select templates
* create related files
* connect dependencies
* implement supporting infrastructure
* add tests
* update documentation
* fix issues discovered during implementation

DO NOT:

* ask me how to implement obvious technical details
* ask me which folder to create when the architecture already determines it
* ask me whether an obvious API is required
* ask me whether authentication is needed when the application clearly has user accounts

Ask only when a missing decision materially changes the product or architecture.

---

# 45. DON'T OVER-ENGINEER

Autonomy does NOT mean adding everything.

Do not automatically add:

* microservices
* Kubernetes
* event sourcing
* message brokers beyond actual needs
* vector databases
* AI agents
* complex caching
* multiple frontend frameworks
* unnecessary abstractions

Use the simplest architecture that can reasonably support the product.

---

# 46. VISUAL DIFFERENTIATION WITHOUT ARCHITECTURAL CHAOS

The same engineering standards should produce different products.

Therefore:

```text
Architecture = standardized
Technology = standardized
Quality = standardized

Visual design = product-specific
UX composition = product-specific
Feature priority = product-specific
Interaction patterns = product-specific
```

Never confuse consistency with repetition.

---

# 47. INITIAL ACQUISITION TASK

Now execute the following:

1. Inspect the current:

```text
~/Projects/engineering-kit
```

2. Create:

```text
sources/
INDEX.md
catalog.json
```

3. Download all repositories listed in this document into the appropriate source folders.

4. Record source metadata and licenses.

5. Do NOT install dependencies globally.

6. Do NOT modify unrelated projects.

7. Do NOT overwrite existing engineering-kit work without inspecting it first.

8. Do NOT create low-quality placeholder implementations.

9. Do NOT promote everything immediately.

10. First establish the source library and metadata.

11. Then identify the highest-value reusable components/features/starters from each source.

12. Create a curation report showing what should eventually be promoted into the engineering-kit.

---

# 48. FIRST CURATION PRIORITY

Prioritize these categories first:

### Web Components

* Sidebar
* App Shell
* Topbar
* Data Table
* Advanced Form
* Search
* Filters
* Date Picker
* Combobox
* Modal
* Drawer
* Command Menu
* Notifications
* Empty State
* Error State
* Loading State
* File Upload
* Charts
* KPI Cards
* Activity Timeline

### Features

* Authentication
* User Management
* Settings
* Dashboard
* Notifications
* File Management
* Search
* Filtering
* Pagination
* AI Chat

### Backend

* Auth
* RBAC
* Logging
* Error Handling
* Validation
* Audit Log
* Jobs
* Redis
* BullMQ
* File Storage
* Health Checks
* API Documentation

### Mobile

* App Shell
* Navigation
* Auth
* Networking
* Storage
* Theme
* Error Handling
* Common Widgets
* Forms

### AI

* Chat
* Provider abstraction
* Streaming
* Tool calling
* Structured output
* Embeddings
* RAG
* Evaluation
* AI workers

---

# 49. FINAL BEHAVIOR

From now on, when I say:

> "Build me X"

interpret it as:

```text
Understand X
    ↓
Classify the product
    ↓
Infer required platforms
    ↓
Infer required subsystems
    ↓
Select correct stack
    ↓
Search current project
    ↓
Search engineering-kit
    ↓
Select reusable templates
    ↓
Select suitable visual style
    ↓
Build dependencies first
    ↓
Connect systems
    ↓
Implement features
    ↓
Test
    ↓
Validate
    ↓
Document
```

Do as much of this as reasonably possible without asking me to specify obvious details.

When something genuinely blocks a meaningful architectural decision, ask a concise question.

Otherwise, make a reasonable engineering decision and continue.

---

# 50. LONG-TERM GOAL

The end state of this system should be:

```text
IDEA
  ↓
PROJECT ANALYSIS
  ↓
AUTOMATIC STACK SELECTION
  ↓
ENGINEERING-KIT SEARCH
  ↓
TEMPLATE SELECTION
  ↓
COMPONENT SELECTION
  ↓
ARCHITECTURE
  ↓
DATABASE
  ↓
BACKEND
  ↓
WEB / MOBILE
  ↓
AI
  ↓
WORKERS
  ↓
INTEGRATION
  ↓
TESTING
  ↓
DEPLOYMENT
```

The objective is not to make Claude blindly follow templates.

The objective is to make Claude **think like a senior engineer with a large private toolbox**.

The toolbox is:

```text
~/Projects/engineering-kit
```

The policy is:

```text
~/Projects/engineering-kit/docs/conventions/engineering-policy.md
```

The catalog is:

```text
~/Projects/engineering-kit/catalog.json
```

The human-readable index is:

```text
~/Projects/engineering-kit/INDEX.md
```

Always use these as the primary local engineering resources.
