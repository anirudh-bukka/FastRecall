"""Stable ID generation for cache entries."""

import hashlib
import uuid


def new_entry_id() -> str:
    """Generate a UUID4 string for a new cache entry.

    We use UUID4 (random) rather than a hash of the query so that two identical
    queries stored at different times each get their own row.  Deduplication is
    handled at lookup time via cosine similarity, not at insertion time via key
    collision.
    """

    return str(uuid.uuid4())


def query_fingerprint(text: str) -> str:
    """Produce a short deterministic fingerprint for a query string.

    This is NOT the cache key (lookups use cosine similarity over embeddings).
    The fingerprint is only used for debugging and logging — it gives you a
    short stable string you can grep for across logs without exposing the full
    query text.
    """

    digest = hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()
    return digest[:12]
