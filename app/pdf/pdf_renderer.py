from pathlib import Path

from app.backend.utils.pdf_utils import ensure_output_dir

try:
    from weasyprint import HTML
except Exception:  # pragma: no cover - optional dependency
    HTML = None


class PDFRenderer:
    def render(self, title: str, html: str, filename: str) -> Path:
        output_dir = ensure_output_dir()
        output_path = output_dir / filename

        if HTML is None:
            # Fallback for environments where weasyprint is unavailable.
            output_path.write_bytes((title + "\n\n" + html).encode("utf-8"))
            return output_path

        HTML(string=html).write_pdf(str(output_path))
        return output_path
