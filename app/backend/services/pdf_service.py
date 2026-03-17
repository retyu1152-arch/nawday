from pathlib import Path

from app.backend.utils.pdf_utils import markdown_to_html
from app.pdf.pdf_renderer import PDFRenderer


class PDFService:
    def __init__(self):
        self.renderer = PDFRenderer()

    def generate_pdf(self, title: str, content: str, document_id: int) -> Path:
        html = markdown_to_html(title=title, content=content)
        return self.renderer.render(title=title, html=html, filename=f"document_{document_id}.pdf")
