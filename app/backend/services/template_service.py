import json
from pathlib import Path


class TemplateService:
    def __init__(self, templates_dir: str = "app/templates"):
        self.templates_dir = Path(templates_dir)

    def load_template(self, document_type: str) -> dict:
        path = self.templates_dir / f"{document_type}_template.json"
        if not path.exists():
            return {"name": document_type, "sections": []}
        return json.loads(path.read_text())
