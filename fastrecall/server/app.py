"""FastAPI application factory for FastRecall.

Why FastAPI?
------------
FastAPI gives us:
- Async request handling (important for I/O-bound proxy calls to the LLM).
- Automatic OpenAPI docs at /docs — callers can explore the API in a browser.
- Pydantic request/response validation out of the box.
- A clean lifespan hook to initialize and tear down the cache + proxy.

Application state
-----------------
The cache and proxy are created once during startup and stored as app.state
attributes so every request handler can access them without re-initializing.
Using app.state is FastAPI's idiomatic way to share per-process singletons.

Lifespan
--------
FastAPI's lifespan context manager (introduced in 0.93) replaces the old
@app.on_event("startup") / @app.on_event("shutdown") pattern.  It runs the
startup code before any request is served and the shutdown code (after the
yield) when the server receives SIGTERM.

OpenAPI customization
---------------------
We override the title and description so the auto-generated /docs page is
useful to callers right away, without any extra configuration.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from ..cache.engine import SemanticCache
from ..config import CacheConfig


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Startup and shutdown lifecycle for the FastAPI app.

    On startup:
    - Build the SemanticCache from the config stored on app.state.
    - Build the LLM proxy from the same config.
    - Start the background eviction sweep task.

    On shutdown:
    - Cancel the eviction task.
    - Close the proxy's httpx client.
    - Close the SemanticCache's SQLite connection.

    TODO:
    - config: CacheConfig = app.state.config
    - app.state.cache = SemanticCache(config)
    - from ..proxy.registry import get_proxy
    - app.state.proxy = get_proxy(config)
    - from ..cache.eviction import eviction_sweep
    - import asyncio
    - app.state.eviction_task = asyncio.create_task(eviction_sweep(app.state.cache))
    - yield   ← server is running while we're here
    - app.state.eviction_task.cancel()
    - if app.state.proxy: await app.state.proxy.close()
    - app.state.cache.close()
    """

    raise NotImplementedError("lifespan is planned.")
    yield  # makes this an async generator even before implementation


def create_app(config: CacheConfig | None = None) -> FastAPI:
    """Construct and return the FastAPI application.

    Args:
        config: active configuration.  Defaults to CacheConfig() if not given.

    Returns:
        A FastAPI app instance with routes registered and config attached.

    TODO:
    - resolved_config = config or CacheConfig()
    - app = FastAPI(
          title="FastRecall",
          description="Semantic LLM response cache.",
          version="0.1.0",
          lifespan=lifespan,
      )
    - app.state.config = resolved_config
    - from .routes import router
    - app.include_router(router)
    - return app
    """

    raise NotImplementedError("create_app is planned.")
