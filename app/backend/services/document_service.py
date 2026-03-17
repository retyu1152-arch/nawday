from sqlalchemy.orm import Session

from app.backend.repositories.document_repository import DocumentRepository
from app.backend.schemas.document_schema import DocumentCreate, DocumentUpdate
from app.backend.services.ai_service import AIService
from app.backend.services.pdf_service import PDFService
from app.backend.services.template_service import TemplateService
from app.backend.utils.text_formatter import normalize_spacing


class DocumentService:
    def __init__(self, db: Session):
        self.repo = DocumentRepository(db)
        self.ai_service = AIService()
        self.template_service = TemplateService()
        self.pdf_service = PDFService()

    def create_generated_document(self, user_id: int, payload: DocumentCreate):
        template = self.template_service.load_template(payload.document_type)
        config = payload.config
        if not config.structure and template.get("sections"):
            config.structure = template["sections"]

        outline, content = self.ai_service.generate_document(
            prompt=payload.prompt,
            document_type=payload.document_type,
            config=config,
        )
        content = normalize_spacing(content)
        document = self.repo.create(
            user_id=user_id,
            title=payload.title,
            document_type=payload.document_type,
            prompt=payload.prompt,
            outline=outline,
            content=content,
        )
        pdf_path = self.pdf_service.generate_pdf(payload.title, content, document.id)
        return self.repo.update(document, file_url=str(pdf_path))

    def list_documents(self, user_id: int):
        return self.repo.get_for_user(user_id)

    def update_document(self, user_id: int, document_id: int, payload: DocumentUpdate):
        document = self.repo.get_by_id(document_id, user_id)
        if not document:
            return None
        return self.repo.update(document, title=payload.title, content=payload.content)
