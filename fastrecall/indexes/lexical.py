"""Lexical index skeleton.

Use this for exact text, identifiers, filenames, errors, imports, config keys,
Robot keywords, and environment variables.
"""

from fastrecall.models import ChunkRecord, RetrievalResult


class LexicalIndex:
    """Simple local lexical index.

    TODO:
    - Start with an in-memory inverted index.
    - Persist later to JSONL or SQLite.
    - Support repo/document filters.
    """

    def add_chunk(self, chunk: ChunkRecord) -> None:
        """Add one chunk to the lexical index."""

        raise NotImplementedError

    def search(
        self,
        query: str,
        repo_ids: list[str] | None = None,
        document_ids: list[str] | None = None,
    ) -> list[RetrievalResult]:
        """Search exact/token matches."""

        raise NotImplementedError

