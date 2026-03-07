# Invoice Tool (rechnungstool)

A minimal monorepo for an invoicing app: a FastAPI backend and a Vite + React frontend.

Prerequisites

- Node.js (for the frontend and root dev scripts)
- Python (see `packages/api/pyproject.toml` for required version and deps)

Quick start

- Install root dev deps and run both apps:

```bash
npm install
npm run dev
```

- Or run the repository setup to install frontend deps and sync the API with `uv`:

```bash
npm run setup
```

- Run frontend only:

```bash
cd packages/web
npm install
npm run dev
```

- Run API only (create/activate a venv first):

```bash
cd packages/api
python -m venv .venv
source .venv/bin/activate
pip install -e .
# start the API with the FastAPI CLI (`uv`)
uv run fastapi dev main.py
```

Repository layout

- `packages/api` — FastAPI backend (routers, models, DB)
- `packages/web` — Vite + React frontend

Notes

- Root `package.json` includes a `dev` script that uses `concurrently` to run both services. The API is started with the FastAPI CLI (`uv`) by the root dev script.
- See `packages/api/pyproject.toml` and `packages/web/package.json` for package-specific details.
