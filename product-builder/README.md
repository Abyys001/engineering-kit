# product-builder

Turns "build me X" into a scoped, dependency-ordered plan using domain knowledge (`../domains/`) and the kit's reusable implementations. Process and rules: [`PRODUCT-BUILDER.md`](PRODUCT-BUILDER.md).

| Path | Contents |
|---|---|
| `PRODUCT-BUILDER.md` | The decision process, scope levels, experience/mobile/real-time/AI rules, build order, when to ask |
| `schemas/` | JSON Schemas for a project's `project.json`, `feature-selection.json`, `architecture.json`, `build-plan.json` |
| `templates/blueprint.md` | One-page blueprint shown to the user before building |
| `examples/` | Worked examples built from real domain data |

Tooling (stdlib Python, from the kit root):

```bash
python3 tools/kb.py find --domain restaurant --platform mobile      # look up features
python3 tools/kb.py matrix restaurant --requested restaurant.reservations   # starting feature matrix
python3 tools/kb.py order restaurant.reservations --with-enhances   # dependency-ordered closure
python3 tools/kb.py validate && python3 tools/kb.py build           # after editing domains/
```

Filled project files live in the project (`~/Projects/<name>/docs/product/`), never here.
