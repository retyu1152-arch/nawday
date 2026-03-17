"""Prompt construction utilities for document generation."""


class PromptBuilder:
    """Builds deterministic prompts for downstream LLM calls."""

    def build(self, user_prompt: str, document_type: str, config: dict) -> str:
        return (
            f"Document type: {document_type}\n"
            f"Requested tone: {config.get('tone', 'formal')}\n"
            f"Target length: {config.get('length', 'medium')}\n"
            f"Include references: {config.get('include_references', True)}\n\n"
            f"User request:\n{user_prompt.strip()}"
        )
