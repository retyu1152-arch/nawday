"""Template loading and validation service."""
import json
from pathlib import Path


class TemplateService:
    """Loads JSON templates by document type."""

    def __init__(self, template_dir: str = "app/templates") -> None:
        self.template_dir = Path(template_dir)

    def load_template(self, document_type: str) -> dict:
        template_path = self.template_dir / f"{document_type}_template.json"
        if not template_path.exists():
            raise FileNotFoundError(f"Template not found for '{document_type}'")

        with template_path.open("r", encoding="utf-8") as file:
            return json.load(file)
