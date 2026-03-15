"""Template ORM model."""
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, JSON, String, Text

from app.backend.models.base import Base


class Template(Base):
    """Template metadata and schema definition."""

    __tablename__ = "templates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), unique=True, nullable=False, index=True)
    document_type = Column(String(64), nullable=False, index=True)
    description = Column(Text, nullable=True)
    schema = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
