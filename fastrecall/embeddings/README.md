# Embeddings

This folder contains optional embedding support.

## Responsibilities

- define an embedding provider interface;
- provide a disabled/no-op path;
- allow future local or API-based embedding providers;
- keep vector retrieval optional.

## Files

- `base.py`: provider interface.
- `optional.py`: helper for optional embedding configuration.

## Flow

If embeddings are disabled, retrieval should still work through lexical,
symbol, graph, and hierarchy indexes.

Do not make this folder a hard dependency for the rest of FastRecall.

