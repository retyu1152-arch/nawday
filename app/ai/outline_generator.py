from typing import Any


def generate_outline(document_type: str, prompt: str) -> dict[str, Any]:
    base_sections = ["Introduction", "Main Analysis", "Conclusion"]
    if document_type in {"dissertation", "academic_paper"}:
        base_sections.insert(1, "Literature Review")
        base_sections.insert(3, "Methodology")
    if "business" in document_type:
        base_sections = ["Executive Summary", "Problem", "Solution", "Financials", "Conclusion"]

    return {
        "title": f"Generated {document_type.replace('_', ' ').title()}",
        "sections": [{"heading": h, "summary": f"Discuss {h.lower()} based on: {prompt}"} for h in base_sections],
    }
