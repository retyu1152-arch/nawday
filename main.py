"""Root entrypoint for platform deployments (Render/Netlify adapters/local uvicorn)."""

from app.backend.main import app

__all__ = ["app"]
