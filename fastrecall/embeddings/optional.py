"""Optional embedding setup helpers."""

from fastrecall.config import FastRecallConfig
from fastrecall.embeddings.base import DisabledEmbeddingProvider, EmbeddingProvider


def get_embedding_provider(config: FastRecallConfig) -> EmbeddingProvider:
    """Return the configured embedding provider.

    TODO:
    - If embeddings are enabled, load a local provider or API provider.
    - Otherwise return DisabledEmbeddingProvider.
    """

    _ = config
    return DisabledEmbeddingProvider()

