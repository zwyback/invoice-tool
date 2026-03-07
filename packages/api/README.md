# API (FastAPI)

Minimal FastAPI backend for the invoicing app.

Prerequisites

- Python (create a virtual environment)
- See `pyproject.toml` for dependencies

Quick start

```bash
cd packages/api
python -m venv .venv
source .venv/bin/activate
pip install -e .
# start the API with the FastAPI CLI (`uv`)
uv run fastapi dev main.py
```

Notes

- Database tables are created on startup (`Base.metadata.create_all` in `main.py`).
- API routes are defined under `routers/`.
