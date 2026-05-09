"""Document summary placeholders.

Summaries should eventually exist at document, page, and section levels.
"""

from fastrecall.models import PageNode


def summarize_page(node: PageNode) -> str:
    """Create a short page summary.

    TODO:
    - Start with extractive summaries before using an LLM.
    - Keep summaries traceable to page/source IDs.
    """

    raise NotImplementedError("Page summarization is planned.")


def summarize_document(nodes: list[PageNode]) -> str:
    """Create a document-level summary.

    TODO:
    - Compose from page/section summaries.
    - Preserve citations to pages.
    """

    raise NotImplementedError("Document summarization is planned.")

