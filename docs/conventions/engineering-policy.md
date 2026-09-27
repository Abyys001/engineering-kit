# MASTER ENGINEERING POLICY

## Personal Technology Stack, Architecture, Reusable Engineering System & Local Template Library

> Adopted 2026-09-26. The §40 setup task was completed that day — don't re-run it. The addendum at the end comes from the shorter companion version of this policy.

This document defines my permanent engineering standards, technology choices, architecture rules, reusable-code strategy, project organization, and local template system.

Treat this document as the **source of truth for all new software projects** unless I explicitly override a rule in a future message.

---

# 1. CORE RULE

From this point forward:

* Do NOT automatically use technology from my previous projects.
* Do NOT assume that an older project stack is still my preferred stack.
* Do NOT introduce a different framework or library just because it is familiar to you.
* Before implementing something, identify which category the task belongs to and use the corresponding stack defined in this document.
* Prefer reusing existing templates, components, modules, and patterns over writing the same functionality from scratch.
* If an existing reusable implementation is close to the requested functionality, adapt it instead of rebuilding it.
* Keep architecture consistent across projects.
* Optimize for long-term maintainability, development speed, AI-assisted development, type safety, testing, and production readiness.

These rules supersede my older general stack preferences unless I explicitly tell you otherwise.

---

# 2. DEVELOPMENT ENVIRONMENT

My primary development environment is:

* OS: Kali Linux
* Shell/environment: Linux
* Main project directory: `~/Projects`

All of my software projects are stored inside:

```text
~/Projects
```

Treat `~/Projects` as the main workspace.

Do not create project source code randomly outside this workspace unless I explicitly request it.

When starting a new project, prefer creating it under:

```text
~/Projects/<project-name>
```

---

# 3. PERSONAL ENGINEERING LIBRARY

Create and maintain a dedicated reusable engineering library inside my Projects directory.

The default location is:

```text
~/Projects/engineering-kit
```

This directory is extremely important.

It is my **local source of truth for reusable code, templates, starters, components, modules, architecture patterns, and common project infrastructure**.

Create this directory if it does not already exist.

Initial structure:

```text
~/Projects/engineering-kit/
│
├── README.md
│
├── starters/
│   ├── web-saas/
│   ├── backend-api/
│   ├── flutter-app/
│   └── ai-service/
│
├── components/
│   ├── web/
│   └── flutter/
│
├── features/
│   ├── auth/
│   ├── users/
│   ├── dashboard/
│   ├── settings/
│   ├── billing/
│   ├── notifications/
│   ├── file-upload/
│   ├── search/
│   ├── filtering/
│   └── pagination/
│
├── backend/
│   ├── authentication/
│   ├── authorization/
│   ├── logging/
│   ├── audit-log/
│   ├── permissions/
│   ├── jobs/
│   ├── notifications/
│   └── file-storage/
│
├── mobile/
│   ├── networking/
│   ├── storage/
│   ├── routing/
│   ├── theme/
│   └── common/
│
├── ai/
│   ├── providers/
│   ├── rag/
│   ├── agents/
│   ├── embeddings/
│   └── evaluation/
│
├── patterns/
│   ├── architecture/
│   ├── api/
│   ├── database/
│   └── infrastructure/
│
└── docs/
    ├── conventions/
    └── decisions/
```

Do not populate this library with random placeholder implementations.

Create the directories and basic documentation structure first.

Actual reusable templates should be added when they are intentionally selected, tested, or generated.

---

# 4. LOCAL-FIRST RULE

This is a critical rule.

For every coding task involving a common feature, component, architecture pattern, or infrastructure:

**Search the local engineering-kit FIRST.**

Preferred order:

```text
1. Current project
2. ~/Projects/engineering-kit
3. Existing installed/project dependencies
4. Official documentation
5. Internet / external repositories
6. Implement from scratch
```

Do NOT immediately search the internet for a solution that may already exist locally.

Do NOT regenerate code that already exists inside:

```text
~/Projects/engineering-kit
```

Before implementing a reusable feature, inspect the relevant local directories.

Examples:

```text
~/Projects/engineering-kit/components/web
~/Projects/engineering-kit/features
~/Projects/engineering-kit/backend
~/Projects/engineering-kit/ai
```

---

# 5. TOKEN-EFFICIENCY RULE

Optimize AI context and token usage.

When implementing a feature:

* Prefer local reusable templates.
* Read only the files necessary to understand and adapt the template.
* Do not dump entire repositories into context.
* Do not repeatedly rediscover the same implementation.
* Do not inspect unrelated files.
* Do not search the internet when a suitable local implementation already exists.
* Do not rewrite existing code just to produce a fresh implementation.
* Reuse small, focused modules rather than recreating them.
* Keep documentation concise and useful.
* Prefer references to existing local files over copying large amounts of code into the conversation.

The goal is:

```text
Less searching
Less repeated code
Less context
Less token usage
More reuse
More consistency
```

---

# 6. TEMPLATE-FIRST CODING

Before writing implementation code for a common feature:

1. Search the current project.
2. Search `~/Projects/engineering-kit`.
3. Find the closest existing template/component/module.
4. Read only the relevant files.
5. Copy/adapt the implementation into the current project.
6. Modify only what is required.
7. Keep the original engineering-kit template unchanged unless I explicitly ask to improve the shared template.

The engineering-kit should act as a **source library**, not as a location where individual projects directly modify shared source files.

---

# 7. TEMPLATE MATCHING

When I request a feature, think in terms of similarity.

Example:

If I say:

> Add an admin sidebar.

Search for:

```text
~/Projects/engineering-kit/components/web/
```

and identify the closest Sidebar/AppShell/Navigation implementation.

If I say:

> Add user management.

Search:

```text
~/Projects/engineering-kit/features/users/
~/Projects/engineering-kit/features/auth/
```

If I say:

> Add logging.

Search:

```text
~/Projects/engineering-kit/backend/logging/
```

If I say:

> Add an AI chat endpoint.

Search:

```text
~/Projects/engineering-kit/ai/
~/Projects/engineering-kit/starters/ai-service/
```

Do not rebuild functionality from scratch when an appropriate template exists.

---

# 8. ENGINEERING-KIT QUALITY RULE

Only place reusable code into the engineering-kit when it is:

* stable
* understandable
* reusable
* reasonably tested
* production-oriented
* not tightly coupled to one project

Do not turn the engineering-kit into a dumping ground for unfinished experiments.

Experimental code should stay inside the project until it becomes reusable and intentionally promoted into the kit.

---

# 9. TEMPLATE DOCUMENTATION

Each reusable template should have a small README.

Example:

```text
features/users/
├── README.md
├── components/
├── api/
├── hooks/
├── schemas/
├── types/
└── tests/
```

The README should explain:

* What problem the template solves.
* When to use it.
* Important dependencies.
* Expected integration points.
* Any assumptions.
* How to adapt it.

Keep these READMEs concise.

---

# 10. PRIMARY TECHNOLOGY STACK

## 10.1 Web Applications

For new web applications, the default stack is:

* React
* Next.js
* TypeScript
* Tailwind CSS
* shadcn/ui
* TanStack Query

Default rules:

* Use TypeScript, not JavaScript.
* Use React components.
* Use Next.js for the application framework.
* Use Tailwind CSS for styling.
* Use shadcn/ui as the base UI component system.
* Prefer composition of existing components over creating new UI primitives.
* Use TanStack Query for server state and API data management where appropriate.

Do not introduce Vue, Nuxt, Angular, or another frontend framework for a new web project unless I explicitly request it.

---

# 11. UI SYSTEM

The default UI system is:

* Tailwind CSS
* shadcn/ui

shadcn/ui should be treated as the foundation, not as a rigid third-party UI dependency.

Components should be copied into the project and customized when necessary.

Common reusable components should include:

* Button
* Input
* Select
* Combobox
* Dialog
* Drawer
* Dropdown
* Tooltip
* Tabs
* Accordion
* Sheet
* Command
* Calendar
* Date Picker
* Data Table
* Pagination
* Form
* Alert
* Toast
* Skeleton
* Empty State
* Error State
* Loading State
* File Upload
* Avatar
* Badge
* Card
* Sidebar
* Navigation
* Modal
* Confirmation Dialog

Before creating one of these from scratch, check the existing engineering-kit.

---

# 12. WEB APPLICATION STRUCTURE

Prefer a feature-oriented structure.

Example:

```text
src/
  app/
  components/
  features/
    auth/
    users/
    dashboard/
    settings/
  lib/
  hooks/
  services/
  types/
  schemas/
  config/
```

Avoid creating huge generic folders where unrelated business logic is mixed together.

Business features should remain isolated and easy to move, test, and reuse.

---

# 13. BACKEND

The default backend stack for NEW projects is:

* NestJS
* TypeScript
* PostgreSQL
* Drizzle ORM
* Redis
* BullMQ

Use NestJS for the primary application/API backend.

Do NOT default to Django for new projects unless I explicitly request Django or the project has a strong technical reason requiring it.

Do NOT default to Express when NestJS is appropriate.

Do NOT introduce another backend framework without a concrete reason.

---

# 14. BACKEND ARCHITECTURE

Prefer modular architecture.

Typical structure:

```text
src/
  common/
    errors/
    filters/
    guards/
    interceptors/
    decorators/
    logging/
  config/
  auth/
  users/
  permissions/
  files/
  notifications/
  health/
  modules/
  database/
```

Business modules should be isolated.

Each major module should contain its own:

* controller
* service
* repository/data access
* DTOs
* schemas
* types
* tests

Do not create a giant service or giant controller.

---

# 15. DATABASE

Default database:

PostgreSQL.

Default ORM:

Drizzle ORM.

Use PostgreSQL unless the project has a clear reason to use another database.

Do not introduce MongoDB or another database simply because it is popular or convenient.

Use relational modeling by default.

Use migrations.

Keep database access explicit and type-safe.

---

# 16. REDIS

Use Redis when the application needs:

* caching
* temporary state
* distributed coordination
* rate limiting
* queues
* background processing
* pub/sub
* session-like temporary data

Do not add Redis to a project without a reason.

---

# 17. BACKGROUND JOBS

Default queue system:

BullMQ + Redis.

Use background jobs for operations such as:

* sending emails
* notifications
* image processing
* video processing
* report generation
* file processing
* scheduled tasks
* webhooks
* long-running operations
* AI processing
* external API synchronization

Do not block an HTTP request while performing expensive work if it can safely be processed asynchronously.

---

# 18. MOBILE APPLICATIONS

Default mobile stack:

* Flutter
* Dart

For new mobile applications, use Flutter unless I explicitly request another technology.

Preferred architecture:

* UI layer
* ViewModel/presentation logic
* Repository
* Data source/API layer

Use:

* go_router for navigation when appropriate
* clear separation of networking, storage, routing, theme, and features

Example:

```text
lib/
  core/
    networking/
    storage/
    routing/
    theme/
    errors/
  features/
    auth/
    users/
    dashboard/
  ui/
```

Do not introduce React Native unless I explicitly request it.

---

# 19. AI / MACHINE LEARNING

AI projects use a separate stack.

Default AI stack:

* Python
* FastAPI
* Pydantic
* PostgreSQL
* Redis
* background workers
* appropriate model/AI libraries

AI backend should be independent from the main TypeScript backend when appropriate.

Architecture:

```text
Client
  ↓
FastAPI
  ↓
Service Layer
  ↓
AI Provider / Model
  ↓
Database / Vector Storage / External Services
```

Create provider abstractions when multiple AI providers may be used.

Example:

```text
LLMProvider
  ├── OpenAIProvider
  ├── AnthropicProvider
  ├── GeminiProvider
  └── LocalProvider
```

Application code should not be tightly coupled to one model provider unless the project explicitly requires it.

---

# 20. AI PROJECT CATEGORIES

When building AI functionality, first identify the category.

Possible categories:

* LLM API integration
* RAG
* embeddings
* document processing
* agents
* tool calling
* AI workers
* classification
* extraction
* summarization
* evaluation
* model inference
* computer vision
* speech
* recommendation systems
* ML pipelines

Use the simplest architecture that satisfies the requirement.

Do not introduce an agent framework, vector database, orchestration system, or additional infrastructure unless it provides a real benefit.

---

# 21. REUSABLE ENGINEERING KIT

The engineering library should contain:

```text
engineering-kit/
│
├── starters/
│   ├── web-saas/
│   ├── backend-api/
│   ├── flutter-app/
│   └── ai-service/
│
├── components/
│   ├── web/
│   └── flutter/
│
├── features/
│   ├── auth/
│   ├── users/
│   ├── dashboard/
│   ├── settings/
│   ├── billing/
│   ├── notifications/
│   ├── file-upload/
│   ├── search/
│   ├── filtering/
│   └── pagination/
│
├── backend/
│   ├── authentication/
│   ├── authorization/
│   ├── logging/
│   ├── audit-log/
│   ├── permissions/
│   └── jobs/
│
├── mobile/
│
├── ai/
│
├── patterns/
│
└── docs/
```

---

# 22. REUSE-FIRST RULE

This is one of the most important rules.

Before implementing a common feature:

1. Search the existing project.
2. Search `~/Projects/engineering-kit`.
3. Identify the closest existing implementation.
4. Reuse it.
5. Modify only what is necessary.
6. Do not recreate an existing component or module from scratch without a good reason.

Examples:

If I need a sidebar:

Do NOT immediately create a new sidebar.

First search for:

* existing Sidebar
* AppShell
* Navigation
* MobileNavigation

If I need authentication:

Search for:

* auth starter
* authentication module
* login
* session
* permissions

If I need logging:

Search for the existing logging system.

If I need a DataTable:

Search for the existing DataTable.

The goal is:

```text
REUSE → ADAPT → EXTEND
```

not:

```text
REBUILD → DUPLICATE → DRIFT
```

---

# 23. TEMPLATE-FIRST DEVELOPMENT

For common features, maintain reusable templates.

Examples:

User Management Template:

```text
user-management/
  components/
    user-table
    user-filters
    user-form
    user-details
  api/
  hooks/
  schemas/
  types/
  tests/
```

Authentication Template:

```text
auth/
  login/
  register/
  forgot-password/
  reset-password/
  verification/
  session/
  permissions/
```

Dashboard Template:

```text
dashboard/
  app-shell/
  sidebar/
  topbar/
  stats/
  charts/
  activity/
  tables/
```

The exact structure can evolve, but reusable functionality should be packaged as complete features rather than isolated snippets whenever possible.

---

# 24. AI CODING RULES

When I ask you to implement something:

1. Understand the requirement.
2. Identify the technology category.
3. Identify the correct stack from this document.
4. Search the existing project for reusable code.
5. Search `~/Projects/engineering-kit` for reusable templates/components.
6. Reuse the closest implementation.
7. Modify only what is necessary.
8. Follow existing project conventions.
9. Do not introduce unnecessary dependencies.
10. Do not rewrite working code without a reason.
11. Keep the implementation production-ready.
12. Add tests where appropriate.

Do not generate a new abstraction merely because you can.

Do not create a new component when an existing component can be extended cleanly.

---

# 25. LOGGING STANDARD

Every backend starter should have a consistent structured logging system.

Logs should support things such as:

* timestamp
* log level
* request ID
* user ID when appropriate
* service/module
* operation
* error information
* relevant metadata

Avoid random `console.log` statements in production code.

Create a reusable logging abstraction.

---

# 26. ERROR HANDLING

Every backend starter should have:

* centralized error handling
* consistent API error format
* validation errors
* application errors
* authentication errors
* authorization errors
* database errors
* unexpected error handling
* structured logging

Frontend applications should also have consistent:

* loading states
* error states
* empty states
* retry behavior where appropriate

---

# 27. VALIDATION

Use schema-based validation.

Backend:

Pydantic for Python services.

Use the appropriate TypeScript schema validation solution for TypeScript services.

Validation should happen at system boundaries.

Never trust client input.

---

# 28. TESTING

Testing should focus on valuable behavior.

Use:

* unit tests
* integration tests
* API tests
* end-to-end tests where appropriate

Do not write meaningless tests simply to increase coverage.

Critical business logic must be tested.

Authentication, authorization, payments, data mutations, and important workflows should receive stronger test coverage.

---

# 29. INFRASTRUCTURE

Default infrastructure:

* Docker
* Docker Compose for local multi-service development
* GitHub Actions for CI/CD
* PostgreSQL
* Redis
* Nginx or Caddy where appropriate

Keep local development simple.

Production infrastructure should be reproducible.

---

# 30. DEPENDENCY RULE

Before adding a dependency, ask:

1. Do we already have something that solves this?
2. Does the engineering-kit already contain it?
3. Is the dependency actively maintained?
4. Is it necessary?
5. Does it significantly reduce complexity?
6. Does it fit the existing architecture?

Avoid dependency bloat.

Do not add a library for a problem that can be solved cleanly with a small amount of existing code.

---

# 31. ARCHITECTURE DECISION RULE

When multiple technologies could work:

Prefer, in order:

1. Existing project standard
2. Existing engineering-kit component/template
3. Defined stack in this document
4. Established ecosystem solution
5. Simpler solution
6. New technology only when there is a clear technical reason

Do not optimize for novelty.

Optimize for:

* maintainability
* reliability
* developer productivity
* type safety
* testability
* performance
* ecosystem maturity
* AI-assisted development

---

# 32. WHEN TO SEARCH THE INTERNET

External research is allowed when:

* the required functionality does not exist locally
* an official technology document is needed
* the local implementation is outdated
* a package/version must be verified
* a real technical decision requires current information

However:

**Do not browse the internet merely because it is easier than checking the local engineering-kit.**

Always search locally first for reusable implementation.

When external code is selected for reuse, review it before adding it to the engineering-kit.

Do not blindly download random GitHub repositories or snippets.

---

# 33. WHEN TO ADD SOMETHING TO THE ENGINEERING-KIT

If, during project development, we create something that is:

* generic
* reusable
* stable
* useful across projects

consider promoting it into:

```text
~/Projects/engineering-kit
```

But do not automatically copy every project-specific implementation into the kit.

The kit should contain reusable engineering assets, not project-specific business logic.

---

# 34. SHARED TEMPLATE IMMUTABILITY

When using:

```text
~/Projects/engineering-kit
```

do not modify the shared template merely to satisfy one project.

Instead:

```text
engineering-kit/template
        ↓
copy
        ↓
current project
        ↓
adapt
```

If the shared template itself should be improved, make that an explicit engineering-kit change.

---

# 35. PROJECT CREATION RULE

When I ask to create a new project:

1. Determine the project type.
2. Select the correct stack.
3. Check `~/Projects/engineering-kit/starters/`.
4. Select the closest starter.
5. Copy/adapt the starter into:

```text
~/Projects/<project-name>
```

6. Remove unnecessary example/demo code.
7. Keep only the infrastructure that is useful.
8. Start implementation from the reusable foundation.

Do not initialize every new project completely from scratch when a suitable starter already exists.

---

# 36. PROJECT DISCOVERY RULE

When working inside `~/Projects`, assume that other projects may contain useful patterns, but do not blindly copy project-specific code.

You may inspect previous projects to discover:

* proven patterns
* reusable architecture
* useful components
* bug fixes
* conventions

However, prefer the cleaned and generalized version in:

```text
~/Projects/engineering-kit
```

for actual reuse.

---

# 37. CODING STYLE

Always prefer:

* simple code
* explicit code
* readable code
* maintainable architecture
* strong typing
* small focused modules
* clear naming
* predictable behavior
* proper error handling
* production-ready implementation

Avoid:

* unnecessary abstractions
* over-engineering
* duplicated logic
* magic behavior
* giant files
* giant functions
* unnecessary dependencies
* speculative architecture

---

# 38. DECISION CHECK BEFORE CODING

Before writing code for a new feature, internally answer:

1. What type of project is this?
2. Which stack applies?
3. Is there a matching local starter?
4. Is there an existing component?
5. Is there an existing feature template?
6. Can an existing module be extended?
7. What is the simplest production-ready implementation?
8. What tests are needed?

Then implement.

---

# 39. MEMORY / PERSISTENCE INSTRUCTION

Treat this document as my current engineering standard and long-term preference.

When persistent memory is available:

* Save the important stack decisions from this document.
* Save the location and purpose of the engineering-kit:
  `~/Projects/engineering-kit`
* Remember that `~/Projects` is my main workspace.
* Prefer these decisions in future conversations.
* Do not rely on older conflicting stack preferences.
* When an older memory conflicts with this document, this document wins.
* Do not resurrect old technology preferences unless I explicitly request them.

Important:

Do not interpret this as permission to delete system-level memories or data that you cannot actually control.

If your platform provides a user-controlled memory system, use the appropriate persistent project/memory instructions available there.

---

# 40. INITIAL SETUP TASK

After reading and accepting this policy, perform the following setup task:

1. Inspect:

```text
~/Projects
```

2. Create:

```text
~/Projects/engineering-kit
```

if it does not exist.

3. Create the directory structure defined in this document.

4. Create a concise:

```text
~/Projects/engineering-kit/README.md
```

that explains:

* purpose of the engineering-kit
* reuse-first rule
* local-first rule
* token-efficiency rule
* project stack mapping
* how templates should be promoted and maintained

5. Do not download large template collections yet.

6. Do not randomly install dependencies.

7. Do not populate the engineering-kit with low-quality placeholder code.

8. The initial setup should establish the structure only.

After setup, report exactly:

* what directories were created
* whether `~/Projects/engineering-kit` already existed
* what was created
* any problems or permission issues encountered

---

# 41. PROJECT TYPE → STACK MAPPING

Use this mapping by default.

### SaaS Web Application

```text
Next.js
+
React
+
TypeScript
+
Tailwind
+
shadcn/ui
+
TanStack Query
+
NestJS
+
PostgreSQL
+
Drizzle
+
Redis
+
BullMQ
```

### Admin Dashboard

```text
Next.js
+
React
+
TypeScript
+
Tailwind
+
shadcn/ui
+
TanStack Query
+
NestJS API
```

### Mobile Application

```text
Flutter
+
Dart
+
go_router
+
Repository-based architecture
```

### AI Service

```text
Python
+
FastAPI
+
Pydantic
+
PostgreSQL
+
Redis
+
appropriate AI/ML libraries
```

### AI + Web Product

```text
Next.js frontend
+
NestJS application backend
+
Python/FastAPI AI service
+
PostgreSQL
+
Redis
+
BullMQ
```

### Background Processing

```text
NestJS worker or Python worker depending on the domain
+
Redis
+
BullMQ / appropriate queue mechanism
```

---

# 42. LEGACY PROJECTS

Existing projects may continue using their current technology.

Do NOT automatically migrate an existing project just because the default stack has changed.

Migration should happen only when explicitly requested or when there is a clear business/technical reason.

However, for NEW projects, follow this document.

---

# 43. FINAL RULE

When I ask:

> "How should we build this?"

Do not immediately start coding.

First:

```text
CLASSIFY
    ↓
SELECT STACK
    ↓
SEARCH LOCAL PROJECT
    ↓
SEARCH ENGINEERING-KIT
    ↓
REUSE
    ↓
ADAPT
    ↓
IMPLEMENT
    ↓
TEST
```

The long-term objective is:

```text
STANDARDIZE
    ↓
REUSE
    ↓
ADAPT
    ↓
SHIP
```

Never:

```text
REINVENT
    ↓
DUPLICATE
    ↓
MAINTAIN THE SAME CODE AGAIN
```

The engineering-kit is a permanent part of my development workflow.

Always check it before reinventing common functionality.

---

# ADDENDUM — WHEN TO BREAK THE STANDARD

The stack defined here is the DEFAULT, not an absolute law.

You may recommend another technology only when there is a concrete reason.

When proposing a deviation, explicitly explain:

* what the standard solution would be
* why it is insufficient
* what alternative you recommend
* what trade-offs it introduces

Do not silently change the stack.

I make the final decision.
