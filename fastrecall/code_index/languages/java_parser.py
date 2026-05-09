"""Java parser skeleton.

TODO:
- Extract packages.
- Extract imports.
- Extract classes, interfaces, enums.
- Extract methods.
- Extract inheritance/implements relationships.
- Consider tree-sitter later.
"""

from pathlib import Path

from fastrecall.models import FileRecord, RepositoryRecord, SymbolRecord


def parse_java_symbols(
    repo: RepositoryRecord,
    file_record: FileRecord,
    path: Path,
) -> list[SymbolRecord]:
    """Extract Java symbols from one file.

    TODO:
    - Start simple with regex.
    - Replace with a proper parser when needed.
    """

    _ = repo, file_record, path
    return []


def parse_java_imports(path: Path) -> list[str]:
    """Extract Java import statements."""

    _ = path
    return []

