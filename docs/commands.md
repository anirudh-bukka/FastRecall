# Planned CLI Commands

These commands are planned; the scaffold only contains placeholders.

```bash
fastrecall init
```

Create local workspace folders, config, and empty metadata/index files.

```bash
fastrecall ingest-docs ./docs
```

Index documents using page and hierarchy indexing.

```bash
fastrecall ingest-repo ./repo-a --name repo_a
fastrecall ingest-repo ./repo-b --name repo_b
```

Register and index code repositories separately.

```bash
fastrecall query "Where is cache eviction implemented?" --repo repo_a
```

Run a repo-scoped query.

```bash
fastrecall query "Compare cache eviction in repo_a and repo_b"
```

Run a multi-repo comparison query.

```bash
fastrecall explain-symbol CacheManager --repo repo_a
```

Find a symbol and explain its file/module context.

```bash
fastrecall find-similar "retry logic" --repos repo_a repo_b
```

Use optional semantic retrieval plus lexical filtering to find conceptually
similar code.
