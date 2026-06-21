"""Anthropic Messages API proxy for cache misses.

Unlike the OpenAI proxy, this one speaks Anthropic's native API format:

  POST https://api.anthropic.com/v1/messages
  Headers:
    x-api-key: <key>
    anthropic-version: 2023-06-01
    content-type: application/json

  Body:
    {
      "model": "claude-3-5-sonnet-20241022",
      "max_tokens": 1024,
      "messages": [{"role": "user", "content": "Hello"}]
    }

  Response:
    {
      "content": [{"type": "text", "text": "Hello! How can I help you?"}],
      "model": "claude-3-5-sonnet-20241022",
      ...
    }

Note: the response schema differs from OpenAI's choices[] structure.
_extract_text() handles the Anthropic-specific content[] format.

When to use this proxy vs. the OpenAI proxy
--------------------------------------------
If you're using Claude via Anthropic's direct API (not via an OpenAI-compat
wrapper), use this.  If you're using Claude via AWS Bedrock or a proxy like
LiteLLM that exposes an OpenAI-compatible interface, use OpenAIProxy.
"""

from __future__ import annotations

from typing import Any

from .base import ProxyResponse

ANTHROPIC_API_VERSION = "2023-06-01"


class AnthropicProxy:
    """Forwards requests to the Anthropic Messages API.

    Args:
        api_key: Anthropic API key.  Falls back to ANTHROPIC_API_KEY env var.
        base_url: override for testing against a mock server.
        timeout: request timeout in seconds.

    TODO:
    - In __init__, store api_key (falling back to os.environ.get("ANTHROPIC_API_KEY")),
      base_url, timeout.
    - Lazily initialize httpx.AsyncClient on first use.
    """

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str = "https://api.anthropic.com/v1",
        timeout: int = 60,
    ) -> None:
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout
        self._client = None

    async def forward(
        self,
        body: dict[str, Any],
        api_key: str | None = None,
    ) -> ProxyResponse:
        """Forward body to {base_url}/messages and return the response.

        TODO:
        - Build headers with x-api-key, anthropic-version, content-type.
        - POST to {self._base_url}/messages with json=body.
        - Parse the response JSON.
        - Extract text with _extract_text().
        - Return ProxyResponse(...).
        """

        raise NotImplementedError("AnthropicProxy.forward is planned.")

    async def close(self) -> None:
        """TODO: close the httpx client."""

        raise NotImplementedError("AnthropicProxy.close is planned.")


def _extract_text(response_body: dict[str, Any]) -> str:
    """Pull the assistant text out of an Anthropic Messages response.

    Anthropic returns content as a list of blocks:
      {"content": [{"type": "text", "text": "Hello!"}], ...}

    We concatenate all text blocks.

    TODO:
    - Try: return " ".join(block["text"] for block in response_body["content"]
                           if block.get("type") == "text")
    - Except (KeyError, TypeError): return ""
    """

    raise NotImplementedError("_extract_text is planned.")
