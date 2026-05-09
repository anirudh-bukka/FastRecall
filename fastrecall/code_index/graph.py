"""Code relationship graph construction.

TODO imports:
- fastrecall.models.EdgeRecord, FileRecord, SymbolRecord.
- language-specific import/call extraction outputs.
"""

from fastrecall.models import EdgeRecord, FileRecord, SymbolRecord


def build_import_edges(files: list[FileRecord], symbols: list[SymbolRecord]) -> list[EdgeRecord]:
    """Build import/dependency edges.

    TODO:
    - Start with file-to-file import relationships.
    - Later resolve imported symbols to definitions where practical.
    """

    _ = files, symbols
    return []


def build_call_edges(symbols: list[SymbolRecord]) -> list[EdgeRecord]:
    """Build function/method call edges where practical.

    TODO:
    - Begin with simple textual references.
    - Use AST/tree-sitter later for higher confidence.
    """

    _ = symbols
    return []


def build_test_edges(files: list[FileRecord], symbols: list[SymbolRecord]) -> list[EdgeRecord]:
    """Build test-to-code relationship edges.

    TODO:
    - Use naming conventions first.
    - Match test files to source files.
    - Match Robot test cases/keywords to resources.
    """

    _ = files, symbols
    return []

