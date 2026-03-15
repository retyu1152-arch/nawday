"""AI orchestration service for generating document outlines and content."""
from typing import Any

from app.ai.outline_generator import OutlineGenerator
from app.ai.prompt_builder import PromptBuilder
from app.ai.section_generator import SectionGenerator


class AIService:
    """Coordinates prompt building, outline generation, and section drafting."""

    def __init__(self) -> None:
        self.prompt_builder = PromptBuilder()
        self.outline_generator = OutlineGenerator()
        self.section_generator = SectionGenerator()

    def generate_structured_document(
        self,
        prompt: str,
        document_type: str,
        config: dict[str, Any],
    ) -> tuple[list[dict[str, Any]], dict[str, str]]:
        generated_prompt = self.prompt_builder.build(prompt, document_type, config)
        outline = self.outline_generator.generate(document_type=document_type, prompt=generated_prompt)
        sections = self.section_generator.generate_sections(outline=outline, context=generated_prompt)
        return outline, sections
