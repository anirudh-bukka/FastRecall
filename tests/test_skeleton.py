"""Skeleton smoke tests."""

from fastrecall.retrieval.router import route_query
from fastrecall.utils.hashing import stable_id


def test_stable_id_has_prefix() -> None:
    assert stable_id("repo", "repo_a").startswith("repo_")


def test_query_router_detects_compare() -> None:
    plan = route_query("Compare cache eviction in repo_a and repo_b", ["repo_a", "repo_b"])
    assert plan.mode == "compare"
    assert plan.use_symbol

