from app.ai.outline_generator import generate_outline
from app.ai.prompt_builder import build_prompt
from app.ai.section_generator import generate_sections
from app.backend.schemas.document_schema import GenerationConfig


class AIService:
    """Abstraction point for OpenAI/local model providers.

    Current implementation uses deterministic local generators to keep
    development and tests reproducible.
    """

    def generate_document(self, prompt: str, document_type: str, config: GenerationConfig) -> tuple[dict, str]:
        _effective_prompt = build_prompt(prompt, document_type, config)
        outline = generate_outline(document_type=document_type, prompt=_effective_prompt)
        content = generate_sections(outline)
        return outline, content
