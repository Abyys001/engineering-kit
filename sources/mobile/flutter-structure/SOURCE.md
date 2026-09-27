# Flutter Template (flutter-structure)

| Field | Value |
|---|---|
| Source URL | https://github.com/MiguelCovarrubiasdaiz/flutter-structure |
| GitHub repository | `MiguelCovarrubiasdaiz/flutter-structure` (user account) |
| Category | mobile |
| License | MIT — `LICENSE.txt` (verbatim copy of root `LICENSE`; copyright held by "Apto", no nested LICENSE/NOTICE files) |
| Author / organization | Miguel Covarrubias (`MiguelCovarrubiasdaiz`) |
| Acquired | 2026-09-26 |
| Revision | `d50c69974a23db3f5bd18e756ebe159521924bc9` (main, committed 2026-07-30) |
| Attribution required | License notice only |
| Status | extraction-safe — MIT, no conditions beyond notice retention; low adoption (1 star) but code quality is high on direct review, see Notes |

## Useful for
- Full UI → ViewModel → Repository → data source pipeline, exactly matching our Flutter policy: `features/posts/{presentation,domain,data}` is a complete worked example (entity → repository interface → usecase → repository impl → remote data source → Riverpod providers → controller → page), directly liftable into `starters/flutter-app`.
- `go_router` app shell: `app/router/app_router.dart` uses `StatefulShellRoute.indexedStack` for a bottom-tab shell with per-branch nav stacks, an auth-gated `redirect`, and a Riverpod-backed `refreshListenable` bridge (`_AuthRefreshNotifier`) — strong reference for our "App Shell/Navigation" mobile priority.
- Networking: `core/network/dio_client.dart` (centralized `Dio` construction, configurable interceptors, `validateStatus` so non-5xx isn't thrown) + `logging_interceptor.dart` — clean, testable, ORM/backend-agnostic.
- Storage: `core/storage/secure_store.dart` (interface over `flutter_secure_storage`) and `key_value_store.dart` (interface over `shared_preferences`) — both are abstracted behind interfaces for testability, matching our "Storage" need.
- Error handling: `core/error/exceptions.dart` (data-layer exceptions) mapped to `core/error/failure.dart` (sealed `Failure` hierarchy) via repository `_run()` catch blocks, surfaced through a `Result<T>` type — a complete, consistent error-handling story for our "Error Handling" priority.
- Theme: `core/theme/app_theme.dart` — single-seed-color Material 3 light/dark theme generation, minimal and easy to re-skin.
- Common widgets: `core/widgets/` barrel (`app_button`, `app_card`, `app_text_field`, `app_avatar`, `app_snack_bar`, `confirm_dialog`, `empty_view`, `error_view`, `loading_overlay`, `section_header`, `gap`) plus a live components-gallery page (`features/showcase/`) — good seed set for our "Common Widgets" need.
- Auth flow (`features/auth/`): `login_page.dart` + `auth_controller.dart` (Riverpod `Notifier<bool>`) wired into router redirects — a minimal but complete example.
- i18n: `flutter_localizations` + official `gen-l10n` (`l10n.yaml`, `lib/l10n/arb/{app_en,app_es}.arb`, generated `AppLocalizations`) plus a `failure_l10n.dart` that localizes `Failure` messages — directly useful pattern.
- Config/flavors: `core/config/app_config.dart` uses `--dart-define`/`--dart-define-from-file` (no secrets in source), with `config/{dev,staging,prod}.example.json` templates — matches our env-flag conventions.
- Tests: unit (`core/utils/result_test.dart`, `core/storage/secure_store_test.dart`), repository-with-mocktail (`post_repository_impl_test.dart`), and widget tests (`login_page_test.dart`, `posts_page_test.dart`, `components_gallery_page_test.dart`) — genuine coverage across layers, not just a token test.

## Where things live
- `source/lib/core/` — `network/`, `storage/`, `error/`, `theme/`, `config/`, `widgets/`, `providers/core_providers.dart`, `utils/` (entry points to open first).
- `source/lib/app/` — `app.dart`, `router/app_router.dart`, `router/app_routes.dart`.
- `source/lib/features/posts/` — the reference Clean Architecture feature (data/domain/presentation).
- `source/lib/features/auth/`, `source/lib/features/shell/`, `source/lib/features/showcase/` — auth flow, nav shell, widget gallery.
- `source/lib/l10n/` — ARB source + generated localizations.
- `source/test/` — mirrors `lib/` layout; `source/test/support/pump_app.dart` is the shared widget-test harness.
- `source/analysis_options.yaml`, `source/AGENTS.md`, `source/Makefile` — lint config + agent/operational contract, worth reading before extracting (upstream `CLAUDE.md` only points to `AGENTS.md` and is excluded from the checkout).

## Known dependencies
- Flutter SDK `^3.11.0`, `flutter_riverpod ^3.3.2` (no code-gen — plain `Provider`/`NotifierProvider`/`AsyncNotifierProvider`, deliberately avoiding `riverpod_generator` per `AGENTS.md` due to a `freezed_annotation` version conflict), `go_router ^17.3.0`, `dio ^5.11.0`, `freezed ^3.2.5` + `json_serializable` (models/DTOs only), `shared_preferences ^2.5.5`, `flutter_secure_storage ^10.3.1`, `logger ^2.7.0`, `intl ^0.20.2`, `mocktail ^1.0.5` (tests), `flutter_lints ^6.0.0`.

## Do not copy
- `source/lib/features/counter/**` — throwaway demo feature (Riverpod 101 example), not representative of real app code.
- `source/config/*.example.json` values, `source/android/app/**`, `source/ios/Runner/**` bundle IDs/signing config — placeholder/app-identity scaffolding to regenerate per project, not to copy verbatim.
- `AppConfig.apiBaseUrl` default (`jsonplaceholder.typicode.com`) — demo API, swap for our own.

## Notes
- Very low adoption (1 star) but the code itself is genuinely strong: `analysis_options.yaml` enables `strict-casts`/`strict-inference`/`strict-raw-types`, treats `unawaited_futures` as an error, and adds ~20 extra lints beyond `flutter_lints` defaults; every file carries purposeful doc comments explaining *why*, not *what*; the dependency-injection graph (`core_providers.dart`, feature `*_providers.dart`) is consistently composed with no shortcuts seen.
- `AGENTS.md` documents real constraints found in code (e.g. the `riverpod_generator`/`freezed` version conflict) rather than aspirational rules — a good sign the doc reflects the actual codebase.
- Tests are substantive, not token coverage: the reviewed repository test mocks the data source and asserts both success mapping and exception→Failure mapping paths.
- Repo also ships `CLAUDE.md`/`AGENTS.md` (AI-agent operating contracts) and a `Makefile` (`make setup`, `make verify`) — not extraction targets themselves but useful models for our own starter's contributor docs.
- Checkout is a shallow single-commit clone; includes standard Flutter `ios/`/`android/` platform scaffolding and app icon assets (not relevant to extraction).
