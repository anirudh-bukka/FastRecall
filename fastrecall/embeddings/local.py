"""Local embedding provider using sentence-transformers.

sentence-transformers runs the model entirely on your machine — no API key,
no network round-trip, no per-token cost.  For a shared cache server this is
the recommended default: pay the model-load cost once at startup, then embed
at ~1ms per query on CPU (10x faster on GPU).

Recommended models
------------------
all-MiniLM-L6-v2   384 dims  Fast, good quality for English.  ~22MB download.
all-mpnet-base-v2  768 dims  Higher quality, ~4x slower.      ~420MB download.
paraphrase-multilingual-MiniLM-L12-v2  384 dims  Multilingual.

Installation
------------
pip install sentence-transformers

The sentence-transformers library is an optional dependency.  If it is not
installed, importing this module raises ImportError with a helpful message.

Output normalization
--------------------
We call encode() with normalize_embeddings=True so every vector has unit norm.
This means cosine_similarity(a, b) == dot(a, b), which is faster to compute
(no division needed).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


class LocalEmbeddingProvider:
    """Sentence-transformers backed embedding provider.

    Args:
        model_name: a sentence-transformers model identifier.
                    Defaults to "all-MiniLM-L6-v2".
        device:     "cpu", "cuda", or "mps".  Defaults to "cpu".

    Usage:
        provider = LocalEmbeddingProvider()
        vec = provider.embed("What is the capital of France?")
        # vec is a list[float] of length 384

    TODO:
    - In __init__, do:
          try:
              from sentence_transformers import SentenceTransformer
          except ImportError as e:
              raise ImportError(
                  "sentence-transformers is required for the local provider.  "
                  "Install it with: pip install fastrecall[local]"
              ) from e
          self._model = SentenceTransformer(model_name, device=device)
          self._model_name = model_name
          self._dimensions = self._model.get_sentence_embedding_dimension()
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2", device: str = "cpu") -> None:
        raise NotImplementedError("LocalEmbeddingProvider.__init__ is planned.")

    @property
    def model_name(self) -> str:
        return self._model_name  # type: ignore[attr-defined]

    @property
    def dimensions(self) -> int:
        return self._dimensions  # type: ignore[attr-defined]

    def embed(self, text: str) -> list[float]:
        """Embed a single text string.

        TODO:
        - Call self._model.encode(text, normalize_embeddings=True).
        - The result is a numpy array; convert with .tolist() before returning.
        """

        raise NotImplementedError("LocalEmbeddingProvider.embed is planned.")

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """Embed multiple texts in one forward pass.

        TODO:
        - Call self._model.encode(texts, normalize_embeddings=True, batch_size=64).
        - Convert each row with .tolist().
        - Return a list of lists.
        """

        raise NotImplementedError("LocalEmbeddingProvider.embed_batch is planned.")
