# Plate

| Field | Value |
|---|---|
| Source URL | https://platejs.org |
| GitHub repository | `udecode/plate` (owner udecode, org — not a fork) |
| Category | web |
| License | MIT — root `LICENSE` (copyright Ziad Beyens, Dylan Schiemann, Joe Anderson, Felix Feng). The root notice defers to per-package `LICENSE` files; all nine found at the pinned revision are MIT (`apps/www`, `packages/core`, `packages/markdown`, `packages/playwright`, `packages/slate`, `packages/udecode/depset`, `templates/plate-playground-template`, `templates/plate-template`), except `packages/diff`, which is **dual MIT + Apache-2.0** (it carries changes derived from `slate-diff`) |
| Author / organization | udecode (Ziad Beyens et al.) |
| Acquired | not acquired — license and revision verified over the GitHub API on 2026-09-27; no checkout exists |
| Revision | `babb3c2a733f821a33569d288e45da3f54eaf643` (committed 2026-09-27) |
| Attribution required | License notice only (plus the Apache-2.0 notice if `packages/diff` is ever used) |
| Status | license-cleared, not acquired — MIT throughout at the pinned revision; no Commons Clause or enterprise carve-out in any license file. Deliberately **not** cloned: disk budget (see `sources/CURATION.md`, and the "no large downloads" rule in `docs/conventions/engineering-policy.md`) |

## Useful for
- Notion-style rich-text editing on Slate: plugin architecture, per-feature packages so only what a product needs gets pulled in
- The kit has no rich-text/document-editor capability at all; this is the leading permissive candidate for `shared.documents`-adjacent editing surfaces

## Where things live
Verified from the pinned revision's git tree (paths only — no file contents were fetched):
- `packages/` — 50 feature packages, one capability each: `core`, `slate`, `plate`, `ai`, `comment`, `suggestion`, `table`, `list`, `list-classic`, `media`, `mention`, `markdown`, `docx`, `docx-io`, `csv`, `math`, `code-block`, `code-drawing`, `excalidraw`, `emoji`, `link`, `footnote`, `toc`, `toggle`, `callout`, `caption`, `date`, `tag`, `dnd`, `resizable`, `selection`, `cursor`, `find-replace`, `slash-command`, `combobox`, `autoformat`, `basic-nodes`, `basic-styles`, `indent`, `layout`, `floating`, `tabbable`, `juice`, `yjs`, `diff`, `utils`, `test-utils`, `playwright`, `plate-scripts`, `udecode/depset`
- `apps/www/` — docs + registry site (MIT, copyright line includes shadcn); the shadcn-registry-style component source usually lives here
- `templates/plate-template`, `templates/plate-playground-template` — MIT starters
- `tooling/` — `cn`, `config`, `preset`, `scripts`, `templates` (build/lint config, not product code)
- `benchmarks/`, `content/docs/`, `docs/` — perf harness and design notes; reference only

## Known dependencies
Not inspected — no checkout. `packages/core`/`packages/slate` sit on Slate; `packages/yjs` implies a Yjs CRDT stack; `packages/excalidraw` and `packages/math` pull heavy third-party editors. Resolve per-package `package.json` before promoting anything.

## Do not copy
- `.claude/skills/`, `.agents/`, `.codex/`, `.github/prompts/` — upstream agent instructions; never executed or trusted (untrusted-source rule, `domains/_schema/RESEARCH-BRIEF.md`)
- Plate **Pro** components — a separate paid product, not in this repository; do not pull them in from the docs site or a paid registry
- `packages/diff` unless the Apache-2.0 notice is carried too

## Notes
- A whole-repo clone is the wrong shape for this source. When it is needed, sparse-checkout only the specific `packages/<name>` a feature requires (`sparse` is supported by `tools/fetch-sources.sh`).
- `fetch: false` in `sources/MANIFEST.json` keeps `tools/fetch-sources.sh` from cloning it; flip that flag (and add `sparse`) when a product actually needs an editor.
