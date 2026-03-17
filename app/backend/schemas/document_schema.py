"""Pydantic schemas for documents and generation requests."""
from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class GenerationConfig(BaseModel):
    length: str = Field(default="medium", pattern="^(short|medium|long)$")
    tone: str = Field(default="formal")
    include_references: bool = True


class DocumentGenerateRequest(BaseModel):
    title: str = Field(min_length=3, max_length=255)
    document_type: str = Field(min_length=3, max_length=64)
    prompt: str = Field(min_length=10)
    config: GenerationConfig = GenerationConfig()


class DocumentCreate(BaseModel):
    title: str
    document_type: str
    prompt: str
    outline: list[dict[str, Any]] = []
    content: dict[str, Any] = {}
    formatted_markdown: str | None = None


class DocumentUpdate(BaseModel):
    title: str | None = None
    formatted_markdown: str | None = None
    content: dict[str, Any] | None = None


class DocumentRead(BaseModel):
    id: int
    owner_id: int
    title: str
    document_type: str
    prompt: str
    outline: list[dict[str, Any]] | None
    content: dict[str, Any] | None
    formatted_markdown: str | None
    pdf_url: str | None
    version: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
