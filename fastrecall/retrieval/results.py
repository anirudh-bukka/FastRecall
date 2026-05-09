"""Retrieval result formatting helpers."""

from fastrecall.models import RetrievalResult


def result_to_display(result: RetrievalResult) -> str:
    """Convert one RetrievalResult into a human-readable line."""

    title = result.title or result.source_id
    return f"[{result.retriever}] {title}: {result.snippet or ''}"


def results_to_display(results: list[RetrievalResult]) -> str:
    """Convert many results into a display string."""

    return "\n".join(result_to_display(result) for result in results)

