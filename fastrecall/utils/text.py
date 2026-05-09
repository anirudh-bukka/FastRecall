"""Text normalization helpers."""

import re


def normalize_text(text: str) -> str:
    """Normalize text for lexical matching.

    TODO:
    - Decide casing rules.
    - Preserve code-sensitive tokens separately.
    """

    return re.sub(r"\s+", " ", text).strip().lower()


def simple_tokens(text: str) -> list[str]:
    """Tokenize text simply for v1 lexical search."""

    return re.findall(r"[A-Za-z_][A-Za-z0-9_]*|\d+|[^\s]", text)

