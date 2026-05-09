"""Document parsing placeholders.

TODO imports:
- pathlib.Path.
- fastrecall.models.DocumentRecord, PageNode, ChunkRecord.
- Optional later: pypdf, markdown parser, BeautifulSoup.
"""

from pathlib import Path


def parse_text_file(path: Path) -> list[str]:
    """Parse a plain text file into pseudo-pages.

    Input:
    - path: text file path.

    Output:
    - list of page-like text strings.

    TODO:
    - Decide page size for text files.
    - Preserve line offsets.
    - Detect headings if possible.
    """

    return [path.read_text(encoding="utf-8", errors="replace")]


def parse_markdown_file(path: Path) -> list[str]:
    """Parse Markdown into page-like units.

    TODO:
    - Split by headings or approximate pages.
    - Preserve heading levels.
    - Extract tables separately.
    """

    return parse_text_file(path)


def parse_pdf_file(path: Path) -> list[str]:
    """Parse PDF into pages.

    TODO:
    - Add optional PDF dependency later.
    - Return one string per physical page.
    - Preserve page numbers.
    """

    raise NotImplementedError("PDF parsing is planned but not implemented.")


def parse_document(path: Path) -> list[str]:
    """Route a document path to the appropriate parser."""

    suffix = path.suffix.lower()
    if suffix == ".md":
        return parse_markdown_file(path)
    if suffix == ".txt":
        return parse_text_file(path)
    if suffix == ".pdf":
        return parse_pdf_file(path)
    return parse_text_file(path)

