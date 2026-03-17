"""Section generation module."""


class SectionGenerator:
    """Creates draft text for each outline section."""

    def generate_sections(self, outline: list[dict], context: str) -> dict[str, str]:
        sections: dict[str, str] = {}
        for item in outline:
            title = item["title"]
            sections[title] = (
                f"This section is generated for: {title}. "
                f"Context excerpt: {context[:180]}...\n"
                "Replace this deterministic placeholder with LLM-generated prose in Stage 2."
            )
        return sections
