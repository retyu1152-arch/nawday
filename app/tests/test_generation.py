from app.ai.outline_generator import OutlineGenerator
from app.ai.prompt_builder import PromptBuilder
from app.ai.section_generator import SectionGenerator


def test_generation_pipeline_shapes() -> None:
    prompt = PromptBuilder().build(
        user_prompt="Generate a technical report on zero-trust architecture.",
        document_type="report",
        config={"tone": "formal", "length": "medium", "include_references": True},
    )
    outline = OutlineGenerator().generate(document_type="report", prompt=prompt)
    sections = SectionGenerator().generate_sections(outline=outline, context=prompt)

    assert len(outline) >= 3
    assert "Introduction" in sections
    assert "Replace this deterministic placeholder" in sections["Introduction"]
