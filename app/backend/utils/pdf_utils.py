from pathlib import Path


def markdown_to_html(title: str, content: str) -> str:
    html_body = content.replace("## ", "<h2>").replace("\n\n", "</h2><p>")
    return f"<html><body><h1>{title}</h1><p>{html_body}</p></body></html>"


def ensure_output_dir(path: str = "generated") -> Path:
    output = Path(path)
    output.mkdir(parents=True, exist_ok=True)
    return output
