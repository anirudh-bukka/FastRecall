# fastrecall Package

This is the main Python package.

## Responsibilities

- expose CLI entrypoints;
- define shared configuration and data models;
- coordinate ingestion, indexing, retrieval, storage, and answer composition;
- keep embeddings optional.

## Folders

- `ingestion/`: discovers documents and repositories.
- `document_index/`: builds page/hierarchy indexes for documents.
- `code_index/`: builds code-aware indexes for repositories.
- `indexes/`: local lexical, symbol, graph, hierarchy, and optional vector indexes.
- `retrieval/`: query routing and retrieval composition.
- `storage/`: local persistence.
- `answer/`: answer construction from retrieval results.
- `embeddings/`: optional embedding provider interfaces.
- `utils/`: small shared helpers.

## Flow

CLI command -> config -> ingestion/retrieval -> storage/indexes -> answer.

