"""PDF helper utilities."""
from pathlib import Path


def ensure_output_dir(path: str) -> Path:
    """Ensure output directory exists and return resolved path."""

    output_path = Path(path)
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path
