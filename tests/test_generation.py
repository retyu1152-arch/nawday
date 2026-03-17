from app.backend.schemas.document_schema import GenerationConfig
from app.backend.services.ai_service import AIService


def test_ai_service_generates_outline_and_content():
    outline, content = AIService().generate_document(
        prompt="Create a renewable energy report",
        document_type="report",
        config=GenerationConfig(target_words=500),
    )

    assert "sections" in outline
    assert len(outline["sections"]) >= 3
    assert "##" in content
