"""Graph index skeleton."""

from fastrecall.models import EdgeRecord, RetrievalResult


class GraphIndex:
    """Relationship lookup for imports, calls, tests, config usage, etc."""

    def add_edge(self, edge: EdgeRecord) -> None:
        """Add one relationship edge."""

        raise NotImplementedError

    def outgoing(self, node_id: str, edge_type: str | None = None) -> list[RetrievalResult]:
        """Find relationships leaving a node."""

        raise NotImplementedError

    def incoming(self, node_id: str, edge_type: str | None = None) -> list[RetrievalResult]:
        """Find relationships pointing to a node."""

        raise NotImplementedError

