from app.backend.schemas.document_schema import GenerationConfig


def build_prompt(user_prompt: str, document_type: str, config: GenerationConfig) -> str:
    structure_hint = ", ".join(config.structure) if config.structure else "auto-structured sections"
    references_hint = "include references" if config.include_references else "no references section"
    return (
        f"Generate a {document_type} with a {config.tone} tone. "
        f"Target length: {config.target_words} words. "
        f"Use structure: {structure_hint}; {references_hint}. "
        f"User request: {user_prompt}"
    )
