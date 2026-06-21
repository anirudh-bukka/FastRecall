"""EmbeddingProvider protocol — the interface all providers must satisfy.

Why a Protocol instead of an ABC?
----------------------------------
Protocol-based structural subtyping (PEP 544) means any object with the right
methods is a valid provider — no inheritance required.  This keeps provider
implementations thin and makes it easy to drop in a third-party client without
wrapping it.

Dimensionality contract
-----------------------
All entries in the cache for a given namespace must share the same embedding
dimension.  If you switch providers or models after entries are already stored,
the existing vectors will have the wrong dimension and cosine similarity will
produce nonsense.  FastRecall stores the model name with every entry so this
mismatch can be detected and the caller warned.
"""

from typing import Protocol, runtime_checkable


@runtime_checkable
class EmbeddingProvider(Protocol):
    """Structural interface for text embedding providers.

    Implementations only need to satisfy embed() and embed_batch().
    embed_batch() is provided as a separate method so providers can take
    advantage of batched API calls (e.g. OpenAI charges the same latency for
    1 or 100 texts in a single request).
    """

    @property
    def model_name(self) -> str:
        """Stable identifier for this model, stored with every cache entry.

        Used to detect dimension mismatches when the provider changes.
        Example values: "all-MiniLM-L6-v2", "text-embedding-3-small".
        """
        ...

    @property
    def dimensions(self) -> int:
        """Length of each output vector.

        384 for all-MiniLM-L6-v2, 1536 for text-embedding-3-small.
        Stored so the similarity engine can allocate the right-sized arrays.
        """
        ...

    def embed(self, text: str) -> list[float]:
        """Return a single embedding vector for `text`.

        Args:
            text: a non-empty string (the normalized query text).

        Returns:
            A list of floats of length self.dimensions.  The vector is
            already L2-normalized (unit norm) so cosine similarity reduces
            to a dot product — no extra normalization needed at lookup time.
        """
        ...

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """Return one embedding vector per text, in the same order.

        Args:
            texts: a non-empty list of strings.

        Returns:
            A list of float lists, one per input text.

        The default implementation falls back to calling embed() in a loop.
        Providers that support native batching (OpenAI, Cohere) should override
        this to make a single API call.
        """
        ...
