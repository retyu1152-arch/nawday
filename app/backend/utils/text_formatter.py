"""Text formatter utilities."""


def normalize_whitespace(text: str) -> str:
    """Collapse excessive blank lines and trim line whitespace."""

    lines = [line.rstrip() for line in text.strip().splitlines()]
    compact_lines: list[str] = []
    for line in lines:
        if line == "" and compact_lines and compact_lines[-1] == "":
            continue
        compact_lines.append(line)
    return "\n".join(compact_lines)


def sections_to_markdown(title: str, sections: dict[str, str]) -> str:
    """Convert generated sections into markdown format."""

    markdown_lines = [f"# {title}", ""]
    for heading, body in sections.items():
        markdown_lines.extend([f"## {heading}", body, ""])
    return normalize_whitespace("\n".join(markdown_lines))
