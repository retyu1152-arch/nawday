# nawday

AI-powered platform to generate structured documents and export them as PDFs.

## Deployment mode
This repository is configured as a **FastAPI backend** for deployment.

## Required runtime files
- `main.py` (root ASGI entrypoint exposing `app`)
- `api/index.py` (Vercel Python serverless entrypoint)
- `requirements.txt` (includes `fastapi` and `uvicorn`)

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Health endpoints
- `GET /` -> API welcome message
- `GET /health` -> readiness check

## Tests
```bash
pytest -q
```
