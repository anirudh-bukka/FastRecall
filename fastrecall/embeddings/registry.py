"""Provider factory — maps config strings to provider instances.

Centralizing construction here means CacheConfig.embedding_provider is just a
string ("local" or "openai"), and the rest of the codebase never imports
provider-specific classes directly.
"""

from ..config import CacheConfig
from .base import EmbeddingProvider


def get_provider(config: CacheConfig) -> EmbeddingProvider:
    """Construct and return the embedding provider specified in config.

    Args:
        config: the active CacheConfig.

    Returns:
        An object that satisfies the EmbeddingProvider protocol.

    Raises:
        ValueError: if config.embedding_provider is not a known value.
        ImportError: if the required optional dependency is not installed.

    TODO:
    - If config.embedding_provider == "local":
          from .local import LocalEmbeddingProvider
          return LocalEmbeddingProvider(model_name=config.embedding_model)
    - If config.embedding_provider == "openai":
          from .openai_embed import OpenAIEmbeddingProvider
          return OpenAIEmbeddingProvider(model_name=config.embedding_model)
    - Otherwise raise ValueError(f"Unknown embedding provider: {config.embedding_provider!r}").
    """

    raise NotImplementedError("get_provider is planned.")
