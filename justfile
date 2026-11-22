@a_default:
    just --list

@dev:
    uv run uvicorn app.main:app --reload --log-config log_config.yaml

@lint_check:
    uv run ruff check .

@lint_fix:
    uv run ruff check . --fix

@format:
    uv run ruff format .