"""CLI entry point for FastRecall.

Installed as the `fastrecall` command via pyproject.toml:

    [project.scripts]
    fastrecall = "fastrecall.cli:main"

Commands
--------
fastrecall serve   -- start the HTTP cache server
fastrecall stats   -- print cache hit/miss stats
fastrecall clear   -- delete cached entries (optionally scoped to a namespace)

Dependencies: click (added to pyproject.toml).
"""

import click

from .config import CacheConfig


@click.group()
@click.version_option()
def main() -> None:
    """FastRecall: semantic LLM response cache."""


@main.command()
@click.option("--host", default="0.0.0.0", show_default=True, help="Bind address.")
@click.option("--port", default=8080, show_default=True, help="Listen port.")
@click.option(
    "--threshold",
    default=0.92,
    show_default=True,
    help="Cosine similarity cutoff (0-1).",
)
@click.option(
    "--storage",
    default=".fastrecall/cache.db",
    show_default=True,
    help="Path to the SQLite cache database.",
)
@click.option(
    "--upstream",
    default=None,
    help="Upstream LLM base URL, e.g. https://api.openai.com/v1",
)
@click.option("--api-key", default=None, envvar="UPSTREAM_API_KEY", help="Upstream API key.")
def serve(
    host: str,
    port: int,
    threshold: float,
    storage: str,
    upstream: str | None,
    api_key: str | None,
) -> None:
    """Start the FastRecall cache server.

    The server exposes an OpenAI-compatible endpoint at
    POST /v1/chat/completions that checks the semantic cache before forwarding
    to the real LLM.

    TODO:
    - Build a CacheConfig from the CLI options.
    - Import uvicorn and the FastAPI app from fastrecall.server.app.
    - Call uvicorn.run(app, host=host, port=port).
    """

    from pathlib import Path

    config = CacheConfig(
        host=host,
        port=port,
        similarity_threshold=threshold,
        storage_path=Path(storage),
        upstream_base_url=upstream,
        upstream_api_key=api_key,
    )
    click.echo(f"Starting FastRecall on {config.host}:{config.port} ...")
    raise NotImplementedError("Server startup is planned -- implement after server/app.py.")


@main.command()
@click.option("--storage", default=".fastrecall/cache.db", show_default=True)
def stats(storage: str) -> None:
    """Print cache hit/miss statistics.

    TODO:
    - Open the SQLite database at `storage`.
    - Read the counters from the stats table.
    - Pretty-print a table with total entries, hit count, miss count, hit rate.
    """

    raise NotImplementedError("Stats command is planned.")


@main.command()
@click.option("--namespace", default=None, help="Only clear entries in this namespace.")
@click.option("--storage", default=".fastrecall/cache.db", show_default=True)
@click.confirmation_option(prompt="This will delete cached entries. Are you sure?")
def clear(namespace: str | None, storage: str) -> None:
    """Delete cached entries.

    Without --namespace, clears all entries.  With --namespace, only entries
    in that partition are removed.

    TODO:
    - Open the SQLite database.
    - Execute DELETE FROM cache_entries WHERE namespace = ? (or no WHERE clause
      for a full clear).
    - Print how many rows were deleted.
    """

    raise NotImplementedError("Clear command is planned.")
