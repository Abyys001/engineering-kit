# Flutter Riverpod Clean Architecture

| Field | Value |
|---|---|
| Source URL | https://github.com/ssoad/flutter_riverpod_clean_architecture |
| GitHub repository | `ssoad/flutter_riverpod_clean_architecture` (owner ssoad, User account) |
| Category | mobile |
| License | MIT — `LICENSE.txt` (root `LICENSE`); no other license files found in the checkout |
| Author / organization | Sohanuzzaman Soad |
| Acquired | 2026-09-26 |
| Revision | `7d898f67eced53a212de2beb60241b6dee1f23fa` (main, committed 2026-09-02) |
| Attribution required | License notice only |
| Status | extraction-safe — plain MIT, no conditions beyond keeping the license text |

## Useful for
- Full Flutter clean-architecture layering (data/domain/presentation, providers, usecases, repositories) per feature — `lib/features/auth/`, `lib/features/chat/`, `lib/features/posts/`
- Riverpod 3 + go_router 17 wiring: router setup, route guards — `lib/core/router/`
- Cross-cutting core: networking (Dio + interceptors), secure storage, caching, error handling, feature flags, analytics, notifications, accessibility, theming — all under `lib/core/`
- Reusable UI kit (buttons, cards, dialogs, inputs, feedback, typography, navigation) — `lib/core/ui/`
- Code generators for scaffolding new features — `lib/core/generators/`, `generate_feature.sh`

## Where things live
- `source/lib/core/{network,storage,auth,error,router,theme,providers,usecases,accessibility,analytics,notifications,feature_flags,logging,localization,background}/` — cross-cutting infrastructure, one dir per concern
- `source/lib/core/ui/{buttons,cards,dialogs,inputs,feedback,typography,navigation,widgets}/` — shared design-system widgets
- `source/lib/features/{auth,chat,home,notifications,posts,settings,survey,tasks,ui_showcase}/` — each follows `data/{models,repositories,datasources}`, `domain/{entities,repositories,usecases}`, `presentation/{screens,providers}`
- `source/lib/core/generators/` + `source/generate_feature.sh`, `source/generate_icons.sh`, `source/generate_language.sh` — scaffolding tooling
- `source/test/` — test suite structure to mirror

## Known dependencies
- `pubspec.yaml`: sdk >=3.10.0 <4.0.0; flutter_riverpod ^3.0.3, riverpod_annotation ^4.0.0, go_router ^17.0.1, dio ^5.8.0+1, freezed_annotation ^3.0.0, hive ^2.2.3, flutter_secure_storage ^10.0.0, connectivity_plus ^7.0.0, local_auth ^3.0.0, flutter_form_builder ^10.2.0, grpc ^4.0.4, fpdart ^1.2.0
- Matches our target mobile stack exactly: Flutter + Riverpod + go_router

## Do not copy
- Nothing asset-wise to withhold — `assets/fonts/PLACE_FONTS_HERE` and every file under `assets/images/**/*.png.placeholder` are empty placeholder stand-ins (tiny text files, not real fonts/images), safe to ignore rather than "not copy"
- `android/`, `ios/`, `linux/`, `macos/`, `windows/`, `web/` platform scaffolding — regenerate via `flutter create` per-project rather than copying, to avoid stale bundle IDs/signing config

## Notes
- Closest stack match among the four repos (Flutter + Riverpod + go_router is exactly our target) — high promote value for the `lib/core/` infrastructure and the feature-layering template.
- `rename_app.sh`, `flutter_launcher_icons.yaml` are template-project tooling (renaming the boilerplate) — reference only, not something to promote as a component.
- No Commons Clause, no separately-licensed bundled assets found.
