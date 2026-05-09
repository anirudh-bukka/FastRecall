"""Optional vector index skeleton.

This must remain optional. FastRecall should still work through lexical,
symbol, graph, and hierarchy indexes when embeddings are disabled.
"""

from fastrecall.models import ChunkRecord, RetrievalResult


class VectorIndex:
    """Optional semantic search index.

    TODO:
    - Support a no-op implementation when embeddings are disabled.
    - Add FAISS, Chroma, sqlite-vss, or a simple numpy store later.
    """

    def add_vector(self, chunk: ChunkRecord, vector: list[float]) -> None:
        """Add one vector for one chunk."""

        raise NotImplementedError

    def search(
        self,
        vector: list[float],
        repo_ids: list[str] | None = None,
        top_k: int = 10,
    ) -> list[RetrievalResult]:
        """Search semantically similar records."""

        raise NotImplementedError

