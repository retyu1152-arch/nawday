"""Database base and session helpers."""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.backend.config import get_settings

settings = get_settings()
engine = create_engine(settings.database_url, echo=settings.debug, future=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_db():
    """FastAPI dependency to provide a database session."""

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
