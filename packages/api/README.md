# API (FastAPI)

Minimal FastAPI backend for the invoicing app.

Prerequisites

- uv (for the API, see https://docs.astral.sh/uv/)

Quick start

```bash
uv sync
uv run fastapi dev main.py
# or
npm run dev:api
```

Notes

- Database tables are created on startup (`Base.metadata.create_all` in `main.py`).
- API routes are defined under `routers/`.
