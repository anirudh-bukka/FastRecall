"""OpenAI-compatible proxy for cache misses.

This proxy forwards requests to any OpenAI-compatible endpoint:
- api.openai.com (OpenAI)
- api.together.xyz (Together AI)
- localhost:11434/v1 (Ollama with OpenAI compat mode)
- any vLLM or LiteLLM instance

Why httpx instead of the openai SDK?
--------------------------------------
We want to forward the request body verbatim — headers, extra fields, and all.
The openai SDK parses and re-constructs the body, which would strip unknown
fields that the caller might be relying on.  httpx lets us pass the raw dict
straight through and return the raw response, which is exactly what a proxy
should do.

The OpenAI chat completions response format
--------------------------------------------
{
  "id": "chatcmpl-...",
  "object": "chat.completion",
  "choices": [{"message": {"role": "assistant", "content": "Paris."}, ...}],
  "model": "gpt-4o",
  ...
}

extract_text() pulls out choices[0].message.content for logging and storage.
"""

from __future__ import annotations

import json
from typing import Any

from .base import ProxyResponse


class OpenAIProxy:
    """Forwards requests to an OpenAI-compatible /v1/chat/completions endpoint.

    Args:
        base_url: base URL of the upstream, e.g. "https://api.openai.com/v1".
        api_key:  default API key.  Can be overridden per-call.
        timeout:  request timeout in seconds.  Default: 60.

    TODO:
    - In __init__, store base_url, api_key, timeout.
    - Lazily create an httpx.AsyncClient (create it once on first use).
    """

    def __init__(
        self,
        base_url: str = "https://api.openai.com/v1",
        api_key: str | None = None,
        timeout: int = 60,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._api_key = api_key
        self._timeout = timeout
        self._client = None  # lazy httpx.AsyncClient

    async def forward(
        self,
        body: dict[str, Any],
        api_key: str | None = None,
    ) -> ProxyResponse:
        """Forward body to {base_url}/chat/completions and return the response.

        TODO:
        - Import httpx at the top of the method (or in __init__ with a helpful
          ImportError if missing).
        - If self._client is None:
              import httpx
              self._client = httpx.AsyncClient(timeout=self._timeout)
        - key = api_key or self._api_key
        - headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
        - url = f"{self._base_url}/chat/completions"
        - resp = await self._client.post(url, json=body, headers=headers)
        - data = resp.json()
        - text = _extract_text(data)
        - model = data.get("model")
        - return ProxyResponse(raw_body=data, response_text=text, model=model, status_code=resp.status_code)
        """

        raise NotImplementedError("OpenAIProxy.forward is planned.")

    async def close(self) -> None:
        """Close the underlying httpx client.

        TODO:
        - If self._client is not None: await self._client.aclose()
        """

        raise NotImplementedError("OpenAIProxy.close is planned.")


def _extract_text(response_body: dict[str, Any]) -> str:
    """Pull the assistant message text out of a chat completions response.

    Returns an empty string if the response is malformed (e.g. an error body).

    TODO:
    - Try: return response_body["choices"][0]["message"]["content"]
    - Except (KeyError, IndexError, TypeError): return ""
    """

    raise NotImplementedError("_extract_text is planned.")
