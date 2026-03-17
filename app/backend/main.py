"""FastAPI entrypoint for AI Document Generator."""
from fastapi import FastAPI

from app.backend.api.routes_documents import router as documents_router
from app.backend.api.routes_generation import router as generation_router
from app.backend.api.routes_user import router as user_router
from app.backend.config import get_settings
from app.backend.models.base import Base, engine

settings = get_settings()
app = FastAPI(title=settings.app_name, debug=settings.debug)


@app.on_event("startup")
def startup_event() -> None:
    """Initialize infrastructure resources."""

    Base.metadata.create_all(bind=engine)


@app.get("/")
def root() -> dict[str, str]:
    """Root endpoint used by platform health checks."""

    return {"message": "AI Document Generator API"}


@app.get("/health")
def healthcheck() -> dict[str, str]:
    """Readiness endpoint."""

    return {"status": "ok"}


app.include_router(user_router)
app.include_router(documents_router)
app.include_router(generation_router)
