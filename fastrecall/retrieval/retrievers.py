"""High-level retriever placeholders."""

from fastrecall.models import RetrievalResult
from fastrecall.retrieval.router import RetrievalPlan


def run_retrieval_plan(plan: RetrievalPlan) -> list[RetrievalResult]:
    """Run the retrievers requested by a RetrievalPlan.

    TODO:
    - Load indexes from storage.
    - Run lexical retriever.
    - Run symbol retriever.
    - Run graph retriever.
    - Run hierarchy retriever.
    - Run vector retriever only when configured.
    """

    _ = plan
    return []


def retrieve_for_single_repo(query: str, repo_name: str) -> list[RetrievalResult]:
    """Run scoped retrieval for one repository."""

    _ = query, repo_name
    return []


def retrieve_for_multiple_repos(query: str, repo_names: list[str]) -> dict[str, list[RetrievalResult]]:
    """Run retrieval independently per repo for safe comparison."""

    return {repo: retrieve_for_single_repo(query, repo) for repo in repo_names}

