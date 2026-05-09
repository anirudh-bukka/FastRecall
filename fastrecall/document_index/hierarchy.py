"""Document hierarchy helpers.

TODO imports:
- re for simple heading detection.
- fastrecall.models.PageNode.
"""

from fastrecall.models import PageNode


def detect_markdown_headings(text: str) -> list[tuple[int, str]]:
    """Detect Markdown headings.

    Output:
    - list of `(level, title)` tuples.

    TODO:
    - Return line numbers.
    - Preserve heading text spans.
    """

    headings: list[tuple[int, str]] = []
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("#"):
            level = len(stripped) - len(stripped.lstrip("#"))
            title = stripped[level:].strip()
            if title:
                headings.append((level, title))
    return headings


def attach_section_nodes(page_nodes: list[PageNode]) -> list[PageNode]:
    """Create section/heading nodes and attach them to pages.

    TODO:
    - Build a real tree.
    - Add parent-child links.
    - Handle non-Markdown documents.
    """

    return page_nodes

