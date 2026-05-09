# Storage

This folder owns local persistence.

## Responsibilities

- create the `.fastrecall` workspace;
- store repository and document records;
- store lexical/symbol/graph/hierarchy index files;
- optionally store vectors later;
- keep repo namespaces separate.

## Files

- `paths.py`: workspace path helpers.
- `jsonl_store.py`: simple append/read helpers for JSONL records.
- `sqlite_store.py`: placeholder for structured metadata storage.
- `manifest.py`: registry manifest for indexed repositories/documents.

## Flow

Ingestion creates records -> storage persists records -> retrieval loads records.

Start with JSONL. Add SQLite only when querying structured metadata becomes
annoying with flat files.

