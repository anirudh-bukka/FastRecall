# FastRecall Architecture

FastRecall has two indexing philosophies.

## 1. Document Indexing

Long-form documents are structured artifacts. A PDF, Markdown file, report, or
manual should not be treated as only a bag of chunks. FastRecall should preserve:

- document identity;
- pages;
- sections;
- headings;
- paragraphs;
- tables;
- figure references when available;
- summaries;
- parent-child relationships;
- neighboring pages and sections.

The document index answers structural questions:

- Where in the document is this topic discussed?
- Which page or section should I inspect?
- What is the parent section?
- What neighboring context matters?

Embeddings may be added later, but the hierarchy should remain the primary
document abstraction.

## 2. Code Repository Indexing

A code repository is not a long document. It has files, modules, functions,
classes, imports, tests, configuration, and execution flow.

FastRecall should index code using multiple views:

- lexical search for exact strings, filenames, identifiers, errors, imports,
  environment variables, and config keys;
- symbol index for classes, functions, methods, packages, Robot Framework
  keywords, and test cases;
- file/module/package index for repository structure;
- graph/dependency index for imports, calls, inheritance, test relationships,
  and config references;
- optional embedding index for semantic similarity and cross-repo comparison;
- hierarchical summaries from repository to folder to file to symbol.

The code index answers connection questions:

- Where is `CacheManager` defined?
- What calls this function?
- Which tests cover this behavior?
- Does repo_b have an equivalent implementation?
- Which files are connected by imports?

## Main Components

### CLI Entrypoints

`fastrecall/cli.py` should eventually expose commands such as `init`,
`ingest-docs`, `ingest-repo`, `query`, `explain-symbol`, and `find-similar`.

### Ingestion

`fastrecall/ingestion/` discovers files and creates records for documents and
repositories. It should decide whether a path is a document source or a code
repository source, then hand off to the right indexer.

### Document Indexing

`fastrecall/document_index/` parses documents into page and hierarchy nodes.
The first implementation can be simple: plain text and Markdown. PDF support
can come later.

### Code Indexing

`fastrecall/code_index/` indexes repository files. Language-specific parsing
lives under `fastrecall/code_index/languages/`.

Initial planned language support:

- Python;
- Java;
- Perl;
- Robot Framework.

### Indexes

`fastrecall/indexes/` contains local indexes:

- lexical index;
- symbol index;
- graph index;
- hierarchy index;
- optional vector index.

The vector index should be optional. FastRecall should still work in a limited
mode without embeddings.

### Storage

`fastrecall/storage/` owns local persistence. Keep this simple first:

- JSONL for append-friendly records;
- SQLite for structured metadata;
- local folders for generated summaries and index files.

### Retrieval

`fastrecall/retrieval/` contains the query router and retrievers. The router
inspects the query and decides which retrieval methods to use.

Examples:

- "Where is X defined?" -> lexical + symbol search.
- "What calls X?" -> symbol + graph search.
- "Explain this module" -> hierarchy + summaries + snippets.
- "Find similar code" -> embeddings + lexical filters.
- "Why does this error happen?" -> exact lexical search, then graph expansion.
- "Which tests cover this?" -> test index + graph relationships.
- "Compare repo A and repo B" -> scoped retrieval in both repos.

### Answer Composition

`fastrecall/answer/` should eventually turn retrieval results into a coherent
answer with citations to files, pages, symbols, or records.

## Multi-Repo Safety

Each repository must have its own:

- repository ID;
- human name;
- root path;
- file records;
- symbol table;
- graph relationships;
- summaries;
- index namespace.

Queries can be scoped to one repo or multiple repos. Cross-repo comparison
should run retrieval separately per repo, then compare the results. This avoids
accidental mixing while still allowing useful comparison.

## How This Differs From Traditional RAG + VectorDB

Traditional RAG often does this:

1. split everything into chunks;
2. embed each chunk;
3. store vectors in a vector database;
4. retrieve top-k chunks by semantic similarity.

FastRecall should not start there.

For documents, structure matters. Page and hierarchy indexing preserve where
information lives.

For code, symbols and relationships matter. A function call, import, test
relationship, or class definition is often more important than semantic
similarity.

Embeddings are still useful, but they are one retrieval view among several.
