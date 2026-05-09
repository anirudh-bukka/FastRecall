# Indexes

This folder contains local index abstractions.

## Responsibilities

- lexical index for exact text and identifiers;
- symbol index for definitions;
- graph index for relationships;
- hierarchy index for document/code trees;
- optional vector index for semantic support.

## Files

- `lexical.py`: exact and token-based search.
- `symbol.py`: symbol lookup.
- `graph.py`: relationship lookup.
- `hierarchy.py`: parent/child/neighbor lookup.
- `vector.py`: optional embedding-backed search.

## Flow

Indexers write index records -> retrieval loads index records -> query router
chooses which index to search.

FastRecall should work without `vector.py` being implemented.

