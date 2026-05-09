"""Code repository ingestion orchestration.

TODO imports:
- discovery helpers.
- registry.register_repository.
- code_index.scanner.
- code_index.symbols.
- code_index.graph.
- storage stores.
"""

from pathlib import Path

from fastrecall.ingestion.registry import register_repository
from fastrecall.models import FileRecord, RepositoryRecord


def ingest_repository(path: Path, name: str) -> tuple[RepositoryRecord, list[FileRecord]]:
    """Ingest one code repository.

    Input:
    - path: repository root.
    - name: namespace name such as repo_a.

    Output:
    - RepositoryRecord.
    - list of FileRecord objects.

    TODO:
    - Scan files.
    - Build lexical index.
    - Extract symbols.
    - Build graph edges.
    - Persist everything under repo namespace.
    """

    repo = register_repository(path, name)
    file_records: list[FileRecord] = []
    return repo, file_records

