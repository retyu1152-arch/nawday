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
pip install -e .[dev]
uvicorn app.backend.main:app --reload
```

## Tests
```bash
pytest
```
