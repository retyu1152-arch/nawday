"""Document generation API routes."""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.backend.api.deps import get_current_user
from app.backend.models.base import get_db
from app.backend.models.user_model import User
from app.backend.schemas.document_schema import DocumentGenerateRequest, DocumentRead
from app.backend.services.document_service import DocumentService

router = APIRouter(prefix="/api/generation", tags=["generation"])


@router.post("/generate", response_model=DocumentRead, status_code=status.HTTP_201_CREATED)
def generate_document(
    payload: DocumentGenerateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> DocumentRead:
    """Run generation pipeline and persist generated document with PDF."""

    service = DocumentService(db)
    return service.generate_document(
        owner_id=current_user.id,
        title=payload.title,
        document_type=payload.document_type,
        prompt=payload.prompt,
        config=payload.config.model_dump(),
    )
