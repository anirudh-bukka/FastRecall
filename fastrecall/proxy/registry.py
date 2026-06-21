"""Proxy factory — select the right upstream proxy from config."""

from ..config import CacheConfig
from .base import LLMProxy


def get_proxy(config: CacheConfig) -> LLMProxy | None:
    """Return the appropriate LLM proxy, or None if no upstream is configured.

    None means the server operates in cache-only mode: it returns cached
    responses on hits, and returns a 503 on misses (no upstream to forward to).
    This is useful for testing the cache in isolation.

    Args:
        config: active CacheConfig.

    Returns:
        An LLMProxy instance, or None.

    TODO:
    - If config.upstream_base_url is None: return None.
    - If "anthropic.com" in config.upstream_base_url:
          from .anthropic import AnthropicProxy
          return AnthropicProxy(api_key=config.upstream_api_key,
                                base_url=config.upstream_base_url)
    - Otherwise (OpenAI-compatible):
          from .openai import OpenAIProxy
          return OpenAIProxy(base_url=config.upstream_base_url,
                             api_key=config.upstream_api_key)
    """

    raise NotImplementedError("get_proxy is planned.")
