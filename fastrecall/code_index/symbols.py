"""Symbol extraction orchestration.

TODO imports:
- language parsers from fastrecall.code_index.languages.
- fastrecall.models.FileRecord, SymbolRecord.
"""

from pathlib import Path

from fastrecall.models import FileRecord, RepositoryRecord, SymbolRecord


def extract_symbols_for_file(
    repo: RepositoryRecord,
    file_record: FileRecord,
    repo_root: Path,
) -> list[SymbolRecord]:
    """Extract symbols from one file.

    Input:
    - repo: owning RepositoryRecord.
    - file_record: file metadata.
    - repo_root: repository root path.

    Output:
    - list of SymbolRecord.

    TODO:
    - Route by file_record.language.
    - Support Python, Java, Perl, Robot Framework.
    - Return [] for unsupported languages.
    """

    _ = repo, file_record, repo_root
    return []


def extract_symbols_for_repo(
    repo: RepositoryRecord,
    files: list[FileRecord],
) -> list[SymbolRecord]:
    """Extract symbols for every supported file in a repository."""

    root = Path(repo.root_path)
    symbols: list[SymbolRecord] = []
    for file_record in files:
        symbols.extend(extract_symbols_for_file(repo, file_record, root))
    return symbols

