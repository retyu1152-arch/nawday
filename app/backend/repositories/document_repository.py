from sqlalchemy.orm import Session

from app.backend.models.document_model import Document


class DocumentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, **kwargs) -> Document:
        document = Document(**kwargs)
        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)
        return document

    def get_for_user(self, user_id: int) -> list[Document]:
        return self.db.query(Document).filter(Document.user_id == user_id).order_by(Document.updated_at.desc()).all()

    def get_by_id(self, document_id: int, user_id: int) -> Document | None:
        return self.db.query(Document).filter(Document.id == document_id, Document.user_id == user_id).first()

    def update(self, document: Document, **kwargs) -> Document:
        for key, value in kwargs.items():
            if value is not None:
                setattr(document, key, value)
        document.version += 1
        self.db.commit()
        self.db.refresh(document)
        return document
