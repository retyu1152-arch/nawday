"""Vercel Python serverless entrypoint."""

from app.backend.main import app

__all__ = ["app"]
