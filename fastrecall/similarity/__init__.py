"""Similarity engine — vector math for semantic cache lookup."""

from .cosine import cosine_similarity, find_best_match

__all__ = ["cosine_similarity", "find_best_match"]
