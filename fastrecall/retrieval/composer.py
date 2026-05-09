"""Retrieval result composer.

This module merges results from multiple retrieval views.
"""

from fastrecall.models import RetrievalResult


def dedupe_results(results: list[RetrievalResult]) -> list[RetrievalResult]:
    """Deduplicate retrieval results.

    TODO:
    - Deduplicate by `(source_type, source_id)`.
    - Preserve best score.
    - Merge metadata from multiple retrievers.
    """

    return results


def rank_results(results: list[RetrievalResult]) -> list[RetrievalResult]:
    """Rank retrieval results.

    TODO:
    - Prefer exact lexical and symbol matches for definition queries.
    - Prefer graph-connected results for usage/test queries.
    - Prefer hierarchy context for explanation queries.
    """

    return sorted(results, key=lambda r: r.score, reverse=True)


def compose_results(results: list[RetrievalResult]) -> list[RetrievalResult]:
    """Deduplicate and rank results."""

    return rank_results(dedupe_results(results))

