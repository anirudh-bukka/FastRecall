"""Hierarchy index skeleton."""

from fastrecall.models import CodeNode, PageNode, RetrievalResult


class HierarchyIndex:
    """Parent/child/neighbor lookup for documents and code."""

    def add_page_node(self, node: PageNode) -> None:
        """Add one document hierarchy node."""

        raise NotImplementedError

    def add_code_node(self, node: CodeNode) -> None:
        """Add one code hierarchy node."""

        raise NotImplementedError

    def get_context(self, node_id: str) -> list[RetrievalResult]:
        """Return parent, children, previous, and next context."""

        raise NotImplementedError

