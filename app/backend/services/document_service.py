"""Document business logic service."""
from sqlalchemy.orm import Session

from app.backend.models.document_model import Document
from app.backend.repositories.document_repository import DocumentRepository
from app.backend.schemas.document_schema import DocumentCreate, DocumentUpdate
from app.backend.services.ai_service import AIService
from app.backend.services.pdf_service import PDFService
from app.backend.utils.text_formatter import sections_to_markdown


class DocumentService:
    """Coordinates document generation, persistence, and PDF rendering."""

    def __init__(self, db: Session) -> None:
        self.db = db
        self.repository = DocumentRepository(db)
        self.ai_service = AIService()
        self.pdf_service = PDFService()

    def create_document(self, owner_id: int, payload: DocumentCreate) -> Document:
        document = Document(owner_id=owner_id, **payload.model_dump())
        return self.repository.create(document)

    def generate_document(
        self,
        owner_id: int,
        title: str,
        document_type: str,
        prompt: str,
        config: dict,
    ) -> Document:
        outline, sections = self.ai_service.generate_structured_document(
            prompt=prompt,
            document_type=document_type,
            config=config,
        )
        markdown = sections_to_markdown(title, sections)
        document = self.repository.create(
            Document(
                owner_id=owner_id,
                title=title,
                document_type=document_type,
                prompt=prompt,
                outline=outline,
                content=sections,
                formatted_markdown=markdown,
            )
        )

        pdf_path = self.pdf_service.render(document.id, markdown)
        document.pdf_url = pdf_path
        return self.repository.update(document)

    def get_document(self, document_id: int) -> Document | None:
        return self.repository.get_by_id(document_id)

    def list_documents(self, owner_id: int) -> list[Document]:
        return self.repository.list_by_owner(owner_id)

    def update_document(self, document: Document, update_data: DocumentUpdate) -> Document:
        changes = update_data.model_dump(exclude_unset=True)
        for key, value in changes.items():
            setattr(document, key, value)

        if changes:
            document.version += 1

        return self.repository.update(document)
