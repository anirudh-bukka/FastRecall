"""Perl parser skeleton.

TODO:
- Extract package declarations.
- Extract `use` statements.
- Extract `sub` definitions.
- Extract constants where practical.
"""

from pathlib import Path

from fastrecall.models import FileRecord, RepositoryRecord, SymbolRecord


def parse_perl_symbols(
    repo: RepositoryRecord,
    file_record: FileRecord,
    path: Path,
) -> list[SymbolRecord]:
    """Extract Perl symbols from one file."""

    _ = repo, file_record, path
    return []


def parse_perl_uses(path: Path) -> list[str]:
    """Extract Perl `use` statements."""

    _ = path
    return []

