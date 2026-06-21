"""Background eviction sweep for the FastRecall server.

When the server runs, two kinds of eviction happen:

1. Lazy TTL eviction  (in storage/sqlite.py:load_entries)
   Expired entries are filtered out during every lookup.  They stay in the
   database until the sweep below deletes them, but they are never returned
   to a caller.  This is "lazy" because we only clean up during normal traffic.

2. Periodic sweep  (this module)
   A background task runs every sweep_interval_seconds and deletes all expired
   rows from the database.  Without this, expired rows accumulate and slow down
   load_entries (which must filter them on every lookup).

Why both?
----------
Lazy eviction alone is safe but wasteful: if traffic drops to zero after
entries expire, they sit on disk forever.  The background sweep reclaims disk
and keeps the database size bounded.

The sweep is optional — if the server is not running (library mode), no sweep
runs and lazy eviction is sufficient.
"""

from __future__ import annotations

import asyncio

from ..cache.engine import SemanticCache
from ..utils.logging import get_logger

logger = get_logger(__name__)


async def eviction_sweep(cache: SemanticCache, interval_seconds: int = 60) -> None:
    """Async background task: delete expired entries every interval_seconds.

    Designed to be started with asyncio.create_task() in the FastAPI lifespan.

    Args:
        cache:            the shared SemanticCache instance.
        interval_seconds: how often to run the sweep.  Default: 60 seconds.

    TODO:
    - while True:
          await asyncio.sleep(interval_seconds)
          conn = cache._get_conn()
          deleted = storage.sqlite.delete_expired(conn)
          if deleted:
              logger.info("Eviction sweep removed %d expired entries.", deleted)
    """

    raise NotImplementedError("eviction_sweep is planned.")
