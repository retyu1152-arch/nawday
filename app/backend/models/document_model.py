"""Document ORM model."""
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import relationship

from app.backend.models.base import Base


class Document(Base):
    """Generated document persisted for editing/versioning."""

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(255), nullable=False)
    document_type = Column(String(64), nullable=False, index=True)
    prompt = Column(Text, nullable=False)
    outline = Column(JSON, nullable=True)
    content = Column(JSON, nullable=True)
    formatted_markdown = Column(Text, nullable=True)
    pdf_url = Column(String(1024), nullable=True)
    version = Column(Integer, default=1, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    owner = relationship("User", back_populates="documents")
