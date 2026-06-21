-- FastRecall cache schema.
--
-- Why SQLite?
-- -----------
-- SQLite gives us persistence with zero infrastructure: no server to run, no
-- port to open, no container to manage.  The cache survives application
-- restarts and can be shared across processes on the same host via WAL mode.
-- For cross-machine sharing, the caller would need to deploy FastRecall as a
-- service (which is the intended use case anyway).
--
-- Tables
-- ------
-- cache_entries  : the core table — one row per cached LLM response.
-- request_log    : append-only log of every hit and miss for computing stats.

PRAGMA journal_mode = WAL;   -- concurrent reads while a write is happening
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS cache_entries (
    entry_id    TEXT    PRIMARY KEY,
    query_text  TEXT    NOT NULL,          -- normalized query string
    embedding   BLOB    NOT NULL,          -- float32 array serialized with numpy.tobytes()
    response    TEXT    NOT NULL,          -- JSON string from the upstream LLM
    model       TEXT,                      -- e.g. "gpt-4o"
    namespace   TEXT    NOT NULL DEFAULT 'default',
    created_at  REAL    NOT NULL,          -- Unix timestamp
    expires_at  REAL,                      -- Unix timestamp or NULL (never expires)
    hit_count   INTEGER NOT NULL DEFAULT 0
);

-- Index on namespace so per-namespace scans stay fast even with a large cache.
CREATE INDEX IF NOT EXISTS idx_entries_namespace
    ON cache_entries (namespace);

-- Index on expires_at so the eviction sweep can quickly find stale rows.
CREATE INDEX IF NOT EXISTS idx_entries_expires
    ON cache_entries (expires_at)
    WHERE expires_at IS NOT NULL;

CREATE TABLE IF NOT EXISTS request_log (
    log_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    namespace   TEXT    NOT NULL DEFAULT 'default',
    hit         INTEGER NOT NULL,          -- 1 for hit, 0 for miss
    similarity  REAL,                      -- cosine score on hit, NULL on miss
    logged_at   REAL    NOT NULL           -- Unix timestamp
);

-- Index on namespace so per-namespace stat aggregation is fast.
CREATE INDEX IF NOT EXISTS idx_log_namespace
    ON request_log (namespace);
