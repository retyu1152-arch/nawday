# nawday

AI-powered platform to generate structured documents and export them as PDFs.

## Stack
- Frontend: React/Next.js (scaffold)
- Backend: FastAPI + SQLAlchemy
- AI Layer: prompt/outline/section modules (pluggable)
- PDF Layer: renderer abstraction (placeholder implemented)

## Project layout
See `docs/ARCHITECTURE.md` for full architecture and module responsibilities.

## Backend quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .[dev]
uvicorn app.backend.main:app --reload
```

## Tests
```bash
pytest
```


## Deploy on Vercel (fix for 404)
This repository is a monorepo-like layout where the Next.js app lives in `app/frontend`.
Without telling Vercel where to build from, deployment can return **404 Page Not Found**.

This repo now includes `vercel.json` to run install/build/dev commands from `app/frontend`.
