# Web (Vite + React)

Minimal Vite + React frontend for the invoicing app.

Prerequisites

- Node.js and npm

Quick start

````bash
cd packages/web
npm install
npm run dev
# Web (Vite + React)

Minimal Vite + React frontend for the invoicing app.

Prerequisites

- Node.js and npm

Quick start

```bash
cd packages/web
npm install
npm run dev
````

Build

```bash
npm run build
```

Notes

- Entry is `src/main.jsx`; config in `vite.config.js`.
- ESLint setup is included (see `eslint.config.js`).
- The API is started with the FastAPI CLI (`uv`). Running `npm run dev` from the repository root will start the API using `uv` via the root script.
