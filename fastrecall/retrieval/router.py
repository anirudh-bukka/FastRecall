"""Query router skeleton.

The router decides which retrieval methods to use.
"""

from dataclasses import dataclass, field
from typing import Literal


RetrievalMode = Literal[
    "definition",
    "usage",
    "error_or_exact",
    "explain",
    "similarity",
    "tests",
    "compare",
    "general",
]


@dataclass(slots=True)
class RetrievalPlan:
    """A simple plan produced by the query router."""

    query: str
    mode: RetrievalMode
    repo_names: list[str] = field(default_factory=list)
    use_lexical: bool = True
    use_symbol: bool = False
    use_graph: bool = False
    use_hierarchy: bool = False
    use_vector: bool = False


def route_query(query: str, repo_names: list[str] | None = None) -> RetrievalPlan:
    """Create a retrieval plan from a user query.

    TODO:
    - Improve intent detection.
    - Detect symbol names.
    - Detect repo comparison requests.
    - Detect "what calls", "where defined", "which tests cover".
    """

    q = query.lower()
    repos = repo_names or []

    if "compare" in q or len(repos) > 1:
        return RetrievalPlan(
            query=query,
            mode="compare",
            repo_names=repos,
            use_lexical=True,
            use_symbol=True,
            use_graph=True,
            use_hierarchy=True,
            use_vector=True,
        )
    if "where" in q and ("defined" in q or "implemented" in q):
        return RetrievalPlan(query=query, mode="definition", repo_names=repos, use_symbol=True)
    if "what calls" in q or "usage" in q or "used by" in q:
        return RetrievalPlan(
            query=query,
            mode="usage",
            repo_names=repos,
            use_symbol=True,
            use_graph=True,
        )
    if "test" in q or "covered" in q:
        return RetrievalPlan(
            query=query,
            mode="tests",
            repo_names=repos,
            use_lexical=True,
            use_symbol=True,
            use_graph=True,
        )
    if "similar" in q:
        return RetrievalPlan(query=query, mode="similarity", repo_names=repos, use_vector=True)
    if "explain" in q:
        return RetrievalPlan(
            query=query,
            mode="explain",
            repo_names=repos,
            use_hierarchy=True,
            use_symbol=True,
        )
    return RetrievalPlan(query=query, mode="general", repo_names=repos)

