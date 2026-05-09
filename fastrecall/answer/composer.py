"""Answer composition skeleton."""

from fastrecall.models import RetrievalResult


def compose_answer(query: str, results: list[RetrievalResult]) -> str:
    """Compose a simple answer from retrieval results.

    Input:
    - query: original user question.
    - results: ranked retrieval results.

    Output:
    - answer text.

    TODO:
    - Add citations.
    - Group by repo/document.
    - Handle no-result answers.
    - Add comparison mode.
    """

    if not results:
        return f"No results found for: {query}"
    lines = [f"Query: {query}", "", "Top evidence:"]
    for result in results[:5]:
        title = result.title or result.source_id
        lines.append(f"- {title}: {result.snippet or ''}")
    return "\n".join(lines)


def compose_comparison_answer(
    query: str,
    grouped_results: dict[str, list[RetrievalResult]],
) -> str:
    """Compose an answer comparing repositories.

    TODO:
    - Keep repo sections separate.
    - Highlight equivalent symbols/files.
    - Highlight missing behavior.
    """

    lines = [f"Comparison query: {query}"]
    for repo_name, results in grouped_results.items():
        lines.append("")
        lines.append(f"## {repo_name}")
        if not results:
            lines.append("No results.")
            continue
        for result in results[:5]:
            lines.append(f"- {result.title or result.source_id}: {result.snippet or ''}")
    return "\n".join(lines)

