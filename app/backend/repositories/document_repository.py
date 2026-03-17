"""Data access layer for document entities."""
from sqlalchemy.orm import Session

from app.backend.models.document_model import Document


class DocumentRepository:
    """Encapsulates document persistence operations."""

    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, document: Document) -> Document:
        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)
        return document

    def get_by_id(self, document_id: int) -> Document | None:
        return self.db.query(Document).filter(Document.id == document_id).first()

    def list_by_owner(self, owner_id: int) -> list[Document]:
        return self.db.query(Document).filter(Document.owner_id == owner_id).all()

    def update(self, document: Document) -> Document:
        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)
        return document
