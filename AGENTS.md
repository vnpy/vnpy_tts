# Repository Guidelines

## Project Structure

- `vnpy_tts/`: installable Python package.
  - `vnpy_tts/gateway/tts_gateway.py`: VeighNa `BaseGateway` implementation (TTS trading + market data).
  - `vnpy_tts/api/`: native bindings and vendor libraries (`*.dll`, `*.so`, `*.lib`) plus code generators under `vnpy_tts/api/generator/`.
- `script/run.py`: minimal launcher to start the VeighNa UI with `TtsGateway` registered.
- `meson.build`: Meson build for the C++/pybind11 extension modules.
- `.github/workflows/pythonapp.yml`: CI runs lint, type-check, and sdist build.

## Build, Test, and Development Commands

- Install from source (builds native extensions): `pip install .`
- Editable/dev install (uses repo build dir): `pip install -e . --no-build-isolation --config-settings=build-dir=./vnpy_tts/api`
- Lint: `ruff check .`
- Type check: `mypy vnpy_tts`
- Build sdist (CI): `uv build --sdist` (or `python -m build --sdist` if you prefer `build`).
- Run locally (requires `vnpy` UI deps): `python script/run.py`

Native compilation requires Visual Studio (Windows) or GCC (Linux). Prebuilt vendor libs live under `vnpy_tts/api/`; ensure they are present for your target platform.

On macOS, the vendor API is typically provided as `*.framework` bundles or `*.dylib` files; place them under `vnpy_tts/api/` before building.

## Coding Style & Naming Conventions

- Python: 4-space indentation, type hints required (mypy is configured in strict mode).
- Linting: Ruff is the source of truth (`pyproject.toml`); long lines are tolerated (`E501` ignored).
- Naming: `snake_case` for functions/vars, `PascalCase` for classes, `UPPER_SNAKE_CASE` for constants.

## Testing Guidelines

This repo currently does not include a unit-test suite. Changes should at minimum:
- pass `ruff check .` and `mypy vnpy_tts`
- include a quick import/smoke check (e.g., `python -c "from vnpy_tts import TtsGateway"`), and a manual UI run when gateway behavior changes.

## Commit & Pull Request Guidelines

- Commit messages commonly use bracketed prefixes: `[Add]`, `[Mod]`, `[Fix]`, `[Del]` followed by a short summary.
- PRs should describe platform(s) validated (Windows/Linux), link issues when applicable, and update `CHANGELOG.md` for user-facing changes. For releases, keep versions in `pyproject.toml` and `meson.build` in sync.

## Security & Configuration Tips

Do not commit credentials or real endpoints. Gateway connection fields (用户名/密码/服务器地址等) should be provided via local settings only.
