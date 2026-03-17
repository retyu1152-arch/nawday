"""Outline generation module."""
from typing import Any


class OutlineGenerator:
    """Generates a high-level document outline."""

    DEFAULT_SECTIONS = [
        "Abstract",
        "Introduction",
        "Core Analysis",
        "Methodology",
        "Results",
        "Conclusion",
        "References",
    ]

    def generate(self, document_type: str, prompt: str) -> list[dict[str, Any]]:
        # Stage 2 placeholder with deterministic output for baseline testing.
        return [
            {
                "title": section,
                "goal": f"Provide the {section.lower()} for a {document_type}.",
                "prompt_context": prompt[:120],
            }
            for section in self.DEFAULT_SECTIONS
        ]
