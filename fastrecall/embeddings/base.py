"""Embedding provider interfaces."""

from typing import Protocol


class EmbeddingProvider(Protocol):
    """Protocol for optional embedding providers."""

    def embed_text(self, text: str) -> list[float]:
        """Return an embedding vector for text."""


class DisabledEmbeddingProvider:
    """No-op provider used when embeddings are disabled."""

    def embed_text(self, text: str) -> list[float]:
        """Raise clearly when embeddings are unavailable."""

        _ = text
        raise RuntimeError("Embeddings are disabled for this FastRecall workspace.")

