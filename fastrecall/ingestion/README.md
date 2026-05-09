# Ingestion

This folder is responsible for discovering inputs and turning them into records
that indexers can process.

## Files

- `discovery.py`: file discovery and ignore rules.
- `registry.py`: repository/document registration.
- `documents.py`: document ingestion orchestration.
- `repositories.py`: code repository ingestion orchestration.

## Flow

1. CLI receives a path.
2. Discovery walks files.
3. Registry creates `RepositoryRecord` or `DocumentRecord`.
4. Document paths are sent to `document_index/`.
5. Repository paths are sent to `code_index/`.
6. Records are persisted through `storage/`.

Keep ingestion simple. It should orchestrate, not parse every language itself.

