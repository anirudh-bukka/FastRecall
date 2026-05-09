# Code Indexing

This folder indexes code repositories using code-aware views.

## Responsibilities

- scan repository files;
- create file records;
- extract symbols;
- build import/call/test/config relationship edges where practical;
- create hierarchy nodes and summary placeholders;
- keep each repository in its own namespace.

## Files

- `scanner.py`: creates `FileRecord` objects from discovered files.
- `symbols.py`: routes files to language parsers.
- `graph.py`: builds relationship edges.
- `summaries.py`: summary placeholders for repo/folder/file/symbol levels.
- `languages/`: language-specific parsers.

## Flow

RepositoryRecord -> FileRecord list -> language parsers -> SymbolRecord list
-> EdgeRecord list -> indexes/storage.

Do not treat repositories as pages. Code needs symbols, files, imports, tests,
and relationships.

