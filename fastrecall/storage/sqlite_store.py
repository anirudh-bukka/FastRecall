"""SQLite storage placeholder.

TODO imports:
- sqlite3.
- pathlib.Path.
- fastrecall.models dataclasses.
"""

from pathlib import Path


def open_database(path: Path):
    """Open a SQLite database connection.

    TODO:
    - Return sqlite3.Connection.
    - Create tables for repositories, documents, files, symbols, edges,
      chunks, page nodes, and retrieval logs.
    """

    raise NotImplementedError("SQLite storage is planned but not implemented.")


def initialize_schema(path: Path) -> None:
    """Create SQLite tables.

    TODO:
    - Keep schema tiny in v1.
    - Prefer explicit tables over generic JSON blobs once needed.
    """

    raise NotImplementedError("SQLite schema initialization is planned.")

