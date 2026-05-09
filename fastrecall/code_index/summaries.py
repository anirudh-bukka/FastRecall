"""Code summary placeholders."""

from fastrecall.models import FileRecord, RepositoryRecord, SymbolRecord


def summarize_repository(repo: RepositoryRecord, files: list[FileRecord]) -> str:
    """Create a repository-level summary.

    TODO:
    - Start with folder/language counts.
    - Later use file summaries.
    """

    raise NotImplementedError("Repository summarization is planned.")


def summarize_file(file_record: FileRecord, symbols: list[SymbolRecord]) -> str:
    """Create a file-level summary.

    TODO:
    - Use imports, symbols, docstrings, and file path.
    """

    raise NotImplementedError("File summarization is planned.")


def summarize_symbol(symbol: SymbolRecord) -> str:
    """Create a symbol-level summary."""

    raise NotImplementedError("Symbol summarization is planned.")

