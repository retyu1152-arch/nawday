from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.backend.api.deps import get_current_user
from app.backend.schemas.document_schema import DocumentRead, DocumentUpdate
from app.backend.services.document_service import DocumentService
from app.backend.utils.db import get_db

router = APIRouter(prefix="/api/documents", tags=["documents"])


@router.get("/", response_model=list[DocumentRead])
def list_documents(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return DocumentService(db).list_documents(current_user.id)


@router.patch("/{document_id}", response_model=DocumentRead)
def update_document(
    document_id: int,
    payload: DocumentUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    updated = DocumentService(db).update_document(current_user.id, document_id, payload)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document not found")
    return updated
