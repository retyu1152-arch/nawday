"""PDF generation service wrapper."""
from pathlib import Path

from app.pdf.pdf_renderer import PDFRenderer


class PDFService:
    """Converts markdown content to rendered PDF files."""

    def __init__(self, output_dir: str = "generated") -> None:
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.renderer = PDFRenderer()

    def render(self, document_id: int, markdown: str) -> str:
        file_path = self.output_dir / f"document_{document_id}.pdf"
        self.renderer.render_markdown_to_pdf(markdown, str(file_path))
        return str(file_path)
