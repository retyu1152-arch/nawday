from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.backend.api.deps import get_current_user
from app.backend.schemas.document_schema import DocumentCreate, DocumentRead
from app.backend.services.document_service import DocumentService
from app.backend.utils.db import get_db

router = APIRouter(prefix="/api/generation", tags=["generation"])


@router.post("/generate", response_model=DocumentRead)
def generate_document(
    payload: DocumentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return DocumentService(db).create_generated_document(current_user.id, payload)
