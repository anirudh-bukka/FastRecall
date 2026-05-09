# FastRecall

**This is WIP.**

FastRecall is a local-first Python project for indexing and querying documents
and code repositories with structure-aware retrieval.

It is inspired by FerroCache's clean organization, but it is not a direct
Rust-to-Python translation. FastRecall starts simpler:

- documents are indexed as pages, sections, headings, paragraphs, tables, and
  summary nodes;
- code repositories are indexed as files, modules, symbols, imports,
  relationships, tests, and summaries;
- embeddings are optional support, not the only retrieval mechanism;
- two repositories can be indexed side by side without mixing metadata;
- the first version should be understandable, hackable, and local-first.

## What FastRecall Is

FastRecall is intended to answer questions like:

- "Where is cache eviction implemented in repo_a?"
- "Does repo_b have an equivalent implementation?"
- "Compare retry logic across both repositories."
- "Which tests cover this behavior?"
- "Explain this PDF section and show neighboring context."
- "Find similar functions related to authentication."

## What FastRecall Is Not

FastRecall is not intended to begin as:

- a production distributed cache;
- a Kubernetes/microservice system;
- a naive "chunk everything and throw it into a vector database" project;
- a replacement for source control, documentation, or test runners;
- a finished implementation.

This repository is intentionally skeletal. The Python files contain commented
TODOs, expected classes, expected functions, and input/output notes so the
implementation can be written gradually.

## Important Docs

- [Architecture](docs/architecture.md)
- [Flowcharts](docs/flowcharts.md)
- [Data Model](docs/data_model.md)
- [Developer Journey](docs/developer_journey.md)
- [Example Commands](docs/commands.md)

## Planned Commands

```bash
fastrecall init
fastrecall ingest-docs ./docs
fastrecall ingest-repo ./repo-a --name repo_a
fastrecall ingest-repo ./repo-b --name repo_b
fastrecall query "Where is cache eviction implemented?" --repo repo_a
fastrecall query "Compare cache eviction in repo_a and repo_b"
fastrecall explain-symbol CacheManager --repo repo_a
fastrecall find-similar "retry logic" --repos repo_a repo_b
```

## Design Principle

Vector search answers: "What looks semantically related?"

Page and hierarchy indexing answers: "Where in the document structure should I
look?"

Symbol and graph indexing answers: "What is actually connected in the code?"

FastRecall combines those views instead of choosing only one.
