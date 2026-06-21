"""Core data models for FastRecall.

Every record here is a plain dataclass so it can be serialized to JSON or
stored as a SQLite row without any ORM magic.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class CacheEntry:
    """One cached LLM response stored in the semantic cache.

    The embedding is stored alongside the query text so we can compute cosine
    similarity at lookup time without re-embedding every entry.

    Fields:
        entry_id:   stable UUID for this row.
        query_text: the normalized text that was embedded (see cache/engine.py
                    for what "normalized" means for chat messages).
        embedding:  the float vector produced by the embedding provider.
        response:   the raw LLM response, stored as a JSON string so the caller
                    receives exactly what the upstream API would have returned.
        model:      the upstream model name (e.g. "gpt-4o", "claude-3-5-sonnet").
        namespace:  logical partition so different apps can share one server
                    without seeing each other's entries.
        created_at: Unix timestamp (float) of when this entry was written.
        expires_at: Unix timestamp after which this entry is stale, or None for
                    no expiry.
        hit_count:  how many times this entry has been served from cache.
        metadata:   arbitrary caller-supplied key/value pairs.
    """

    entry_id: str
    query_text: str
    embedding: list[float]
    response: str
    model: str | None
    namespace: str
    created_at: float
    expires_at: float | None = None
    hit_count: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class CacheLookupResult:
    """Outcome of a semantic cache lookup.

    hit=True  means a sufficiently similar entry was found and its response
              can be returned directly to the caller.
    hit=False means no match exceeded the similarity threshold; the caller must
              forward the request to the upstream LLM and then call store().
    """

    hit: bool
    entry: CacheEntry | None = None
    similarity: float | None = None


@dataclass
class CacheStats:
    """Runtime metrics returned by GET /cache/stats.

    hit_rate is computed as hit_count / (hit_count + miss_count), or 0.0 when
    no requests have been served yet.
    """

    total_entries: int
    hit_count: int
    miss_count: int
    hit_rate: float
    oldest_entry_age_seconds: float | None


@dataclass
class ChatMessage:
    """One turn in a chat conversation (mirrors the OpenAI messages schema).

    Storing this as a dataclass rather than a raw dict makes it easier to
    extract the parts we care about when building the query text to embed.
    """

    role: str    # "system" | "user" | "assistant" | "tool"
    content: str


@dataclass
class ProxiedRequest:
    """A decoded incoming request that the server will try to serve from cache.

    If the cache misses, the server uses this record to reconstruct the exact
    body to forward to the upstream LLM.
    """

    messages: list[ChatMessage]
    model: str
    namespace: str
    raw_body: dict[str, Any]  # original request JSON, forwarded verbatim on miss
