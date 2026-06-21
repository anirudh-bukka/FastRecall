"""Embedding providers for FastRecall.

An embedding provider converts a text string into a fixed-length float vector.
The vector captures the *semantic meaning* of the text so that two queries with
the same meaning (even if worded differently) map to nearby points in the vector
space — and cosine similarity between those points will be high.

Available providers
-------------------
local     : uses sentence-transformers, runs entirely on your machine.
            No API key needed.  Default model: all-MiniLM-L6-v2 (384 dims).
openai    : uses OpenAI's text-embedding-3-small endpoint.
            Requires OPENAI_API_KEY.  Output: 1536 dims.

Adding a new provider
---------------------
Implement the EmbeddingProvider protocol from .base and register it in
.registry.get_provider().
"""

from .base import EmbeddingProvider
from .registry import get_provider

__all__ = ["EmbeddingProvider", "get_provider"]
