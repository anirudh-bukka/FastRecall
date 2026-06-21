"""Shared types for the proxy layer.

On a cache miss the server needs to forward the original request to the real
LLM and return its response to the caller — and also store that response in
the cache.

ProxyResponse
-------------
A thin wrapper around what the upstream returned.  We keep both the raw JSON
body and the extracted text so:
- The HTTP server can forward the raw body verbatim (caller sees exactly what
  the real API would have returned).
- The cache engine stores the raw body as the cached response, so future hits
  also return the real API shape.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


@dataclass
class ProxyResponse:
    """Result of forwarding a request to the upstream LLM.

    raw_body:      the full JSON response dict from the upstream API.
    response_text: the extracted assistant message text (for logging/debugging).
    model:         the model name from the response, if present.
    status_code:   HTTP status code from the upstream (200, 429, 500, etc.).
    """

    raw_body: dict[str, Any]
    response_text: str
    model: str | None
    status_code: int


class LLMProxy(Protocol):
    """Structural interface for upstream LLM proxies.

    Each provider (OpenAI, Anthropic, ...) implements this protocol.
    The HTTP server calls forward() on a cache miss and stores the result.
    """

    async def forward(
        self,
        body: dict[str, Any],
        api_key: str | None = None,
    ) -> ProxyResponse:
        """Forward a request body to the upstream LLM.

        Args:
            body:    the decoded JSON request body received from the caller.
            api_key: override the configured API key for this request
                     (useful when the caller passes their own key).

        Returns:
            ProxyResponse containing the full upstream response.
        """
        ...
