"""Query text normalization before embedding.

Why normalize?
--------------
Embedding models are sensitive to whitespace differences and minor formatting
variations.  Two queries that are semantically identical but differ only in
trailing whitespace would produce nearly identical but not byte-equal vectors.
Normalizing first ensures the embedding is as stable as possible.

This is NOT about lowercasing or stemming for keyword search — we keep the
original casing because LLMs are case-sensitive.  We only clean up structural
noise (extra spaces, newlines at the edges).
"""

import re


def normalize_query(text: str) -> str:
    """Collapse internal whitespace runs and strip leading/trailing whitespace.

    "What  is  Paris  ?" → "What is Paris ?"

    We intentionally do NOT lowercase: "Python" and "python" can have different
    meanings in some contexts, and the embedding model handles casing well.
    """

    return re.sub(r"\s+", " ", text).strip()


def messages_to_query_text(messages: list[dict], user_only: bool = True) -> str:
    """Flatten a list of chat messages into a single string to embed.

    This is the canonical representation used for similarity lookup.

    Args:
        messages:  list of {"role": str, "content": str} dicts.
        user_only: if True, only include user-role turns.  If False, include
                   all roles (system, user, assistant) separated by role labels.

    Design decision: embedding user messages only (user_only=True) means that
    queries with the same user question but different system prompts still hit
    the cache.  This is usually the right behavior for a shared cache — the
    system prompt is configuration, not part of the semantic query.  Set
    user_only=False if your system prompts carry semantic meaning you want to
    differentiate.

    TODO:
    - Handle multi-turn conversations: should the full history be embedded, or
      only the latest user turn?  For V1, concatenating all user messages gives
      a reasonable signal.  Revisit when multi-turn caching is a priority.
    """

    if user_only:
        parts = [m["content"] for m in messages if m.get("role") == "user"]
    else:
        parts = [f"{m.get('role', 'unknown')}: {m['content']}" for m in messages]

    return normalize_query(" ".join(parts))
