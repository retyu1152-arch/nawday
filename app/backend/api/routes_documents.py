"""Document CRUD API routes."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.backend.api.deps import get_current_user
from app.backend.models.base import get_db
from app.backend.models.user_model import User
from app.backend.schemas.document_schema import DocumentRead, DocumentUpdate
from app.backend.services.document_service import DocumentService

router = APIRouter(prefix="/api/documents", tags=["documents"])


@router.get("", response_model=list[DocumentRead])
def list_documents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[DocumentRead]:
    """List all documents for current user."""

    return DocumentService(db).list_documents(current_user.id)


@router.get("/{document_id}", response_model=DocumentRead)
def get_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> DocumentRead:
    """Get a single document if owned by current user."""

    document = DocumentService(db).get_document(document_id)
    if not document or document.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document not found")
    return document


@router.patch("/{document_id}", response_model=DocumentRead)
def update_document(
    document_id: int,
    payload: DocumentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> DocumentRead:
    """Update editable document fields and increment version."""

    service = DocumentService(db)
    document = service.get_document(document_id)
    if not document or document.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document not found")
    return service.update_document(document, payload)
