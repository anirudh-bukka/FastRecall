# Retrieval

This folder routes user questions to the right retrieval strategies.

## Responsibilities

- classify query intent;
- choose lexical/symbol/graph/hierarchy/vector retrievers;
- enforce repo/document scopes;
- merge and rank results;
- support cross-repo comparison safely.

## Files

- `router.py`: intent detection and retrieval plan creation.
- `retrievers.py`: high-level retriever functions.
- `composer.py`: merge/dedupe/rank retrieval results.
- `results.py`: formatting helpers for retrieval results.

## Flow

User query -> router -> retrieval plan -> retrievers -> result composer ->
answer composer.

Keep routing simple at first. Keyword rules are fine before adding ML.

