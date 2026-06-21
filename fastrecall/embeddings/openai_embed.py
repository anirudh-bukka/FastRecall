"""OpenAI embedding provider using text-embedding-3-small.

When to use this instead of the local provider
-----------------------------------------------
- You already pay for OpenAI and want consistent embeddings with your LLM.
- You need multilingual support out of the box.
- You cannot install a model locally (e.g. very constrained container).

When NOT to use this
---------------------
- You want zero per-query cost (use local instead).
- You want to run fully offline.

Cost note: text-embedding-3-small is $0.02 per million tokens (~$0.00002 per
average query).  For a cache that saves you $0.002+ per LLM call, the
embedding cost is negligible past the first hit.

Batching
---------
OpenAI allows up to 2048 inputs per request.  embed_batch() takes full
advantage of this — pre-warming a large cache with embed_batch() costs the
same number of API calls as a single request for small batches.

Installation
------------
pip install openai
"""

from __future__ import annotations


class OpenAIEmbeddingProvider:
    """OpenAI text-embedding-3-small provider.

    Args:
        model_name: defaults to "text-embedding-3-small".  Can also be
                    "text-embedding-3-large" for higher quality (3072 dims).
        api_key:    OpenAI API key.  Defaults to the OPENAI_API_KEY env var.

    TODO:
    - In __init__, do:
          try:
              from openai import OpenAI
          except ImportError as e:
              raise ImportError(
                  "openai package is required for the openai provider.  "
                  "Install it with: pip install fastrecall[openai]"
              ) from e
          self._client = OpenAI(api_key=api_key)
          self._model_name = model_name
          # Dimension map: 3-small=1536, 3-large=3072.
          self._dimensions = 1536 if "small" in model_name else 3072
    """

    _DIM_MAP = {
        "text-embedding-3-small": 1536,
        "text-embedding-3-large": 3072,
        "text-embedding-ada-002": 1536,  # legacy
    }

    def __init__(
        self,
        model_name: str = "text-embedding-3-small",
        api_key: str | None = None,
    ) -> None:
        raise NotImplementedError("OpenAIEmbeddingProvider.__init__ is planned.")

    @property
    def model_name(self) -> str:
        return self._model_name  # type: ignore[attr-defined]

    @property
    def dimensions(self) -> int:
        return self._dimensions  # type: ignore[attr-defined]

    def embed(self, text: str) -> list[float]:
        """Embed a single text via the OpenAI embeddings API.

        TODO:
        - Call self._client.embeddings.create(input=text, model=self._model_name).
        - Return response.data[0].embedding (already a list[float]).
        """

        raise NotImplementedError("OpenAIEmbeddingProvider.embed is planned.")

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """Embed up to 2048 texts in a single API request.

        TODO:
        - Call self._client.embeddings.create(input=texts, model=self._model_name).
        - Sort response.data by .index to guarantee order matches input.
        - Return [item.embedding for item in sorted_data].
        """

        raise NotImplementedError("OpenAIEmbeddingProvider.embed_batch is planned.")
