# Developer Journey

Implement FastRecall in phases. Avoid jumping to embeddings too early.

## Phase 1: File Discovery and Repo Registry

Goal: know what exists.

- Implement workspace initialization.
- Create local storage folders.
- Register repositories by name.
- Scan files.
- Store `RepositoryRecord` and `FileRecord`.

## Phase 2: Lexical Index

Goal: exact search works.

- Tokenize text simply.
- Index filenames, paths, identifiers, strings, config keys, and raw text.
- Implement exact and substring search.
- Make `fastrecall query "some string"` return candidate files.

## Phase 3: Basic Code Symbol Extraction

Goal: definitions work.

- Start with Python using `ast`.
- Add simple Java regex/tree-sitter later.
- Add Perl and Robot Framework gradually.
- Store `SymbolRecord`.
- Implement `explain-symbol`.

## Phase 4: Document Page/Hierarchy Index

Goal: documents are not blind chunks.

- Parse Markdown headings.
- Parse text files into pseudo-pages.
- Add PDF page extraction later.
- Store `DocumentRecord`, `PageNode`, and `ChunkRecord`.

## Phase 5: Query Router

Goal: route by intent.

- Detect definition queries.
- Detect caller/usage queries.
- Detect compare queries.
- Detect tests coverage queries.
- Detect document explanation queries.

## Phase 6: Retrieval Composer

Goal: combine retrieval views.

- Merge lexical, symbol, hierarchy, and graph results.
- Deduplicate by source.
- Rank simply.
- Return clean `RetrievalResult` objects.

## Phase 7: Optional Embeddings

Goal: semantic support without making it mandatory.

- Add an embedding provider interface.
- Store vectors locally if configured.
- Use embeddings for "similar code" and concept search.
- Keep lexical/symbol retrieval working without embeddings.

## Phase 8: Graph Relationships

Goal: answer connection questions.

- Store imports.
- Store simple call references where practical.
- Store test-to-source heuristics.
- Store Robot keyword/resource relationships.

## Phase 9: Multi-Repo Comparison

Goal: compare two repositories safely.

- Enforce repo namespaces.
- Run scoped retrieval per repo.
- Compare result groups.
- Add cross-repo similarity only after repo-scoped retrieval is solid.
