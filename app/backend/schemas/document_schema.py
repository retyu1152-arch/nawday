from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class GenerationConfig(BaseModel):
    tone: str = "formal"
    target_words: int = Field(default=1200, ge=200, le=30000)
    include_references: bool = True
    structure: list[str] = Field(default_factory=list)


class DocumentCreate(BaseModel):
    title: str
    document_type: str
    prompt: str
    config: GenerationConfig = Field(default_factory=GenerationConfig)


class DocumentUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


class DocumentRead(BaseModel):
    id: int
    user_id: int
    title: str
    document_type: str
    prompt: str
    outline: dict[str, Any]
    content: str
    file_url: str | None
    version: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
