from pathlib import Path

from app.pdf.pdf_renderer import PDFRenderer


def test_pdf_renderer_writes_file(tmp_path: Path) -> None:
    output_path = tmp_path / "output.pdf"
    PDFRenderer().render_markdown_to_pdf("# Title", str(output_path))

    assert output_path.exists()
    assert output_path.read_text(encoding="utf-8").startswith("%PDF-1.4")
