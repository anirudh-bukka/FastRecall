"""Page index construction.

TODO imports:
- fastrecall.models.DocumentRecord, PageNode, ChunkRecord.
- fastrecall.utils.hashing.stable_id.
"""

from fastrecall.models import DocumentRecord, PageNode
from fastrecall.utils.hashing import stable_id


def build_page_nodes(document: DocumentRecord, pages: list[str]) -> list[PageNode]:
    """Build PageNode records from parsed page text.

    Input:
    - document: DocumentRecord.
    - pages: one string per page/pseudo-page.

    Output:
    - list of PageNode objects with previous/next links.

    TODO:
    - Add section/heading child nodes.
    - Add table nodes.
    - Add summary nodes.
    """

    nodes: list[PageNode] = []
    for index, text in enumerate(pages, start=1):
        node_id = stable_id("page", document.document_id, str(index))
        previous_id = nodes[-1].node_id if nodes else None
        node = PageNode(
            node_id=node_id,
            document_id=document.document_id,
            kind="page",
            title=f"Page {index}",
            page_number=index,
            previous_id=previous_id,
            text=text,
        )
        if nodes:
            nodes[-1].next_id = node_id
        nodes.append(node)
    return nodes


def build_page_chunks(nodes: list[PageNode]):
    """Build ChunkRecord objects from page nodes.

    TODO:
    - Keep chunks tied to page/section parents.
    - Avoid making chunks the primary document abstraction.
    """

    raise NotImplementedError("Page chunk creation is planned.")

