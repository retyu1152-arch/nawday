"""PDF rendering backend."""
from pathlib import Path


class PDFRenderer:
    """Render markdown into a PDF artifact.

    Current implementation writes plain text bytes into a .pdf file as a safe
    placeholder for Stage 4. Integrate WeasyPrint or LaTeX in production.
    """

    def render_markdown_to_pdf(self, markdown_text: str, output_path: str) -> None:
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        pdf_stub = (
            "%PDF-1.4\n"
            "1 0 obj<<>>endobj\n"
            "2 0 obj<< /Length 3 0 R >>stream\n"
            f"{markdown_text}\n"
            "endstream endobj\n"
            "3 0 obj 0 endobj\n"
            "trailer<<>>\n%%EOF"
        )
        output.write_text(pdf_stub, encoding="utf-8")
