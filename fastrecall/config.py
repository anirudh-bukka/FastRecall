"""Configuration for FastRecall.

CacheConfig is the single source of truth for tunable parameters.  It can be
constructed directly in Python (library mode) or loaded from environment
variables / a TOML file (server mode).

Design note: we use a plain dataclass rather than pydantic so the package has
zero required dependencies for the config layer itself.  The server and
embedding layers bring in their own optional dependencies.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class CacheConfig:
    """Runtime configuration for the FastRecall semantic cache.

    Storage
    -------
    storage_path: where the SQLite database lives on disk.  The parent
        directory is created automatically if it does not exist.

    Similarity
    ----------
    similarity_threshold: cosine similarity cutoff in [0, 1].  A query whose
        best cached match scores below this value is treated as a miss.
        - 0.95+ : near-identical queries only (very strict)
        - 0.90  : paraphrases usually match (good starting point)
        - 0.80  : broader matching; more hits, more risk of wrong answers
    embed_user_messages_only: when True, only the user-role turns are embedded
        for similarity; the system prompt is excluded.  This means "What is
        the capital of France?" matches in two conversations that share the same
        user question but have different system prompts.  Set to False if the
        system prompt is part of the semantic meaning you want to differentiate.

    Embedding
    ---------
    embedding_provider: "local" uses sentence-transformers (no API key needed,
        runs entirely on your machine).  "openai" uses text-embedding-3-small.
    embedding_model: the model name passed to the chosen provider.
        - local  → e.g. "all-MiniLM-L6-v2"  (fast, 384-dim)
        - openai → e.g. "text-embedding-3-small"

    TTL / Eviction
    --------------
    ttl_seconds: seconds before a cache entry is considered expired.  None
        means entries never expire.  Expired entries are deleted lazily (at
        lookup time) and also by a background sweep if the server is running.
    max_entries: if set, the cache evicts the least-recently-used entries when
        this limit is reached.  None means the cache grows unboundedly.

    Server
    ------
    host: bind address for the HTTP server.
    port: listen port.

    Upstream LLM
    ------------
    upstream_base_url: the base URL of the real LLM API to call on a cache
        miss, e.g. "https://api.openai.com/v1".
    upstream_api_key: API key forwarded to the upstream on every miss.
    """

    # Storage
    storage_path: Path = Path(".fastrecall/cache.db")

    # Similarity
    similarity_threshold: float = 0.92
    embed_user_messages_only: bool = True

    # Embedding
    embedding_provider: str = "local"          # "local" | "openai"
    embedding_model: str = "all-MiniLM-L6-v2"

    # TTL / Eviction
    ttl_seconds: int | None = None
    max_entries: int | None = None

    # Server
    host: str = "0.0.0.0"
    port: int = 8080

    # Upstream LLM
    upstream_base_url: str | None = None
    upstream_api_key: str | None = None


def from_env() -> CacheConfig:
    """Build a CacheConfig from environment variables.

    Variable names mirror the field names in uppercase with a FASTRECALL_
    prefix, e.g. FASTRECALL_PORT, FASTRECALL_SIMILARITY_THRESHOLD.

    TODO:
    - Read each known env var with os.getenv().
    - Cast strings to the right types (int, float, bool, Path).
    - Return a CacheConfig with the merged values.
    """

    raise NotImplementedError("Environment-variable config loading is planned.")


def from_toml(path: Path) -> CacheConfig:
    """Load a CacheConfig from a TOML file.

    The TOML file should have a [fastrecall] table whose keys match the
    CacheConfig field names.

    TODO:
    - Use tomllib (stdlib in Python 3.11+) to parse the file.
    - Map the parsed dict onto CacheConfig fields.
    - Raise a clear error if required fields are missing or types are wrong.
    """

    raise NotImplementedError("TOML config loading is planned.")
