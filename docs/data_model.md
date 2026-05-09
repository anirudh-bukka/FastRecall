# Internal Data Model

These records are intentionally simple. They can start as dataclasses and later
be persisted to JSONL or SQLite.

## RepositoryRecord

Represents one indexed repository.

Fields:

- `repo_id`: stable internal ID;
- `name`: human-friendly name such as `repo_a`;
- `root_path`: local path at ingest time;
- `language_hints`: detected or configured languages;
- `created_at`: ingest timestamp.

## DocumentRecord

Represents one indexed document.

Fields:

- `document_id`;
- `source_path`;
- `title`;
- `document_type`;
- `created_at`;
- `metadata`.

## FileRecord

Represents one file inside a repository.

Fields:

- `file_id`;
- `repo_id`;
- `path`;
- `language`;
- `size_bytes`;
- `content_hash`;
- `is_test`;
- `is_generated`.

## SymbolRecord

Represents a code symbol.

Fields:

- `symbol_id`;
- `repo_id`;
- `file_id`;
- `name`;
- `kind`;
- `language`;
- `start_line`;
- `end_line`;
- `parent_symbol_id`;
- `signature`;
- `docstring`.

## ChunkRecord

Represents a small text span used for lexical search, summaries, or optional
embedding.

Fields:

- `chunk_id`;
- `source_type`;
- `source_id`;
- `repo_id`;
- `document_id`;
- `text`;
- `start_line`;
- `end_line`;
- `page_number`;
- `metadata`.

## PageNode

Represents a document page or structural node.

Fields:

- `node_id`;
- `document_id`;
- `kind`;
- `title`;
- `page_number`;
- `parent_id`;
- `previous_id`;
- `next_id`;
- `text`.

## CodeNode

Represents a repository, folder, file, class, function, method, test, or keyword
in the code hierarchy.

Fields:

- `node_id`;
- `repo_id`;
- `file_id`;
- `symbol_id`;
- `kind`;
- `name`;
- `parent_id`;
- `summary`.

## EdgeRecord

Represents a relationship.

Fields:

- `edge_id`;
- `repo_id`;
- `from_id`;
- `to_id`;
- `edge_type`;
- `confidence`;
- `metadata`.

Example edge types:

- `imports`;
- `calls`;
- `inherits`;
- `tests`;
- `defines`;
- `uses_config`;
- `robot_uses_resource`;
- `similar_to`.

## RetrievalResult

Represents one candidate returned by retrieval.

Fields:

- `result_id`;
- `source_type`;
- `source_id`;
- `repo_id`;
- `document_id`;
- `score`;
- `retriever`;
- `title`;
- `snippet`;
- `metadata`.
