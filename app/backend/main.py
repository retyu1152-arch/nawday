from fastapi import FastAPI

from app.backend.api.routes_documents import router as documents_router
from app.backend.api.routes_generation import router as generation_router
from app.backend.api.routes_user import router as user_router
from app.backend.config import get_settings
from app.backend.models.base import Base
from app.backend.utils.db import engine

settings = get_settings()
app = FastAPI(title=settings.app_name)


@app.on_event("startup")
def startup() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(user_router)
app.include_router(generation_router)
app.include_router(documents_router)
