# Invoice Tool

A minimal monorepo for an invoicing app: a FastAPI backend and a Vite + React frontend.

Prerequisites

- Node.js (for the frontend and root dev scripts)
- uv (for the API, see https://docs.astral.sh/uv/)

Quick start

- Install root dev deps and run both apps:

```bash
npm run setup
npm run dev
```

- Run frontend only:

```bash
npm install --prefix packages/web
npm run dev:web
```

- Run API only (with uv):

```bash
uv sync --directory packages/api
uv run --directory packages/api fastapi dev main.py
```

Repository layout

- `packages/api` — FastAPI backend (routers, models, DB)
- `packages/web` — Vite + React frontend

Notes

- Root `package.json` includes a `dev` script that uses `concurrently` to run both services. The API is started with the FastAPI CLI (`uv`) by the root dev script.
- See `packages/api/pyproject.toml` and `packages/web/package.json` for package-specific details.
