# FastRecall

**Status: skeleton — implementation in progress.**

FastRecall is a semantic LLM response cache.  It sits in front of your LLM
API calls and returns cached responses for semantically similar queries.
Because it exposes an HTTP API, any language can use it.

```
Client ──► POST /v1/chat/completions
                │
        ┌───────▼────────┐
        │  Semantic Cache │
        │  (cosine sim)   │
        └───┬─────────┬───┘
        HIT │         │ MISS
            │         ▼
            │    upstream LLM
            │    (OpenAI/Anthropic/…)
            │         │
            └────◄────┘ store + return
```

## Why semantic caching?

LLM API calls are expensive.  Semantically similar queries should reuse cached
answers instead of paying for a new completion.

- "What is the capital of France?" and "France's capital city?" → same answer.
- Unlike exact-string caching, semantically equivalent phrasings always hit.
- The cache survives application restarts (SQLite on disk).
- Deploy once, share across your entire fleet.

## Install

```bash
# Core server + local embeddings (no API key needed):
pip install fastrecall[local]

# If you prefer OpenAI embeddings:
pip install fastrecall[openai]
```

## Quick start — server mode

```bash
# Start the cache server (forwards misses to OpenAI):
fastrecall serve \
  --upstream https://api.openai.com/v1 \
  --api-key $OPENAI_API_KEY \
  --threshold 0.92

# Point your client at FastRecall instead of OpenAI:
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-4o", "messages": [{"role": "user", "content": "What is the capital of France?"}]}'
```

On the first request: miss — FastRecall forwards to OpenAI and stores the
response.  On a semantically identical follow-up: hit — returned in <5ms
with `X-Cache: HIT`.

## Quick start — library mode

```python
from fastrecall import SemanticCache, CacheConfig
from pathlib import Path

cache = SemanticCache(CacheConfig(storage_path=Path("cache.db")))

result = cache.lookup("What is the capital of France?")
if result.hit:
    print("Cache hit:", result.entry.response)
else:
    response = call_my_llm("What is the capital of France?")
    cache.store(query_text="What is the capital of France?", response=response, model="gpt-4o")
```

## Configuration

| Option | Default | Description |
|---|---|---|
| `similarity_threshold` | `0.92` | Cosine similarity cutoff (0–1). Lower = more hits, higher risk of wrong answers. |
| `embedding_provider` | `"local"` | `"local"` (sentence-transformers) or `"openai"`. |
| `embedding_model` | `"all-MiniLM-L6-v2"` | Model passed to the provider. |
| `ttl_seconds` | `None` | Seconds before entries expire. `None` = never. |
| `max_entries` | `None` | LRU eviction cap. `None` = unbounded. |
| `storage_path` | `.fastrecall/cache.db` | SQLite database path. |
| `upstream_base_url` | `None` | LLM endpoint to call on misses. |

## Architecture

```
fastrecall/
├── cache/
│   ├── engine.py        ← SemanticCache: lookup() + store()
│   └── eviction.py      ← background TTL sweep
├── embeddings/
│   ├── base.py          ← EmbeddingProvider Protocol
│   ├── local.py         ← sentence-transformers (default)
│   └── openai_embed.py  ← OpenAI text-embedding-3-small
├── similarity/
│   └── cosine.py        ← vectorized cosine similarity (numpy)
├── storage/
│   ├── schema.sql       ← SQLite table definitions
│   └── sqlite.py        ← insert, load, evict, stats
├── proxy/
│   ├── openai.py        ← forward misses to OpenAI-compatible APIs
│   └── anthropic.py     ← forward misses to Anthropic Messages API
├── server/
│   ├── app.py           ← FastAPI app factory + lifespan
│   └── routes.py        ← POST /v1/chat/completions, GET /cache/stats, …
├── config.py            ← CacheConfig dataclass
├── models.py            ← CacheEntry, CacheLookupResult, CacheStats
└── cli.py               ← `fastrecall serve / stats / clear`
```

## CLI

```bash
fastrecall serve --port 8080 --threshold 0.92
fastrecall stats
fastrecall clear --namespace my-app
```

## Namespaces

Use the `X-Namespace` request header to partition the cache.  Different
applications sharing one FastRecall instance will not see each other's entries:

```bash
curl -H "X-Namespace: app-a" http://localhost:8080/v1/chat/completions ...
curl -H "X-Namespace: app-b" http://localhost:8080/v1/chat/completions ...
```

## Scaling beyond SQLite

For V1, FastRecall scans all stored vectors in memory (O(n) per lookup).  This
handles tens of thousands of entries with sub-millisecond similarity search.
To scale further, replace `storage/sqlite.py` with a vector-database-backed
implementation (Qdrant, pgvector, Chroma) — the `SemanticCache` API does not
change.
