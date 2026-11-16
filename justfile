@a_default:
    just --list

@dev:
    uv run fastapi dev app/main.py

@lint_check:
    uv run ruff check .

@lint_fix:
    uv run ruff check . --fix

@format:
    uv run ruff format .