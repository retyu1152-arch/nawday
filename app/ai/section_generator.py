from typing import Any


def generate_sections(outline: dict[str, Any]) -> str:
    chunks: list[str] = []
    for section in outline.get("sections", []):
        heading = section["heading"]
        summary = section["summary"]
        chunks.append(f"## {heading}\n\n{summary}\n")
    return "\n".join(chunks)
