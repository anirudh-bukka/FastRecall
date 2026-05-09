"""Hashing helpers for stable local IDs."""

import hashlib


def stable_id(prefix: str, *parts: str) -> str:
    """Create a stable ID from string parts.

    Input:
    - prefix: entity type, e.g. repo/file/symbol/page.
    - parts: stable identifying strings.

    Output:
    - compact stable ID.

    TODO:
    - Decide whether IDs should be longer for collision resistance.
    """

    payload = "\0".join(parts).encode("utf-8", errors="replace")
    digest = hashlib.sha256(payload).hexdigest()[:16]
    return f"{prefix}_{digest}"


def content_hash(text: str) -> str:
    """Hash file/document text content."""

    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()

