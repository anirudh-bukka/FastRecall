"""Robot Framework parser skeleton.

TODO:
- Extract suite metadata.
- Extract test cases.
- Extract keywords.
- Extract variables.
- Extract resources.
- Extract tags.
- Extract keyword-to-resource relationships.
"""

from pathlib import Path

from fastrecall.models import FileRecord, RepositoryRecord, SymbolRecord


def parse_robot_symbols(
    repo: RepositoryRecord,
    file_record: FileRecord,
    path: Path,
) -> list[SymbolRecord]:
    """Extract Robot Framework test cases and keywords."""

    _ = repo, file_record, path
    return []


def parse_robot_resources(path: Path) -> list[str]:
    """Extract Robot Framework resource imports."""

    _ = path
    return []

