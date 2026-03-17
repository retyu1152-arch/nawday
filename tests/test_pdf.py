from app.backend.services.pdf_service import PDFService


def test_pdf_service_generates_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    file_path = PDFService().generate_pdf("Test", "## Intro\n\nHello", 1)
    assert file_path.exists()
    assert file_path.name == "document_1.pdf"
