"""Python parser skeleton.

TODO imports:
- ast.
- pathlib.Path.
- fastrecall.models.FileRecord, RepositoryRecord, SymbolRecord.
- fastrecall.utils.hashing.stable_id.
"""

import ast
from pathlib import Path

from fastrecall.models import FileRecord, RepositoryRecord, SymbolRecord
from fastrecall.utils.hashing import stable_id


def parse_python_symbols(
    repo: RepositoryRecord,
    file_record: FileRecord,
    path: Path,
) -> list[SymbolRecord]:
    """Extract Python classes and functions using ast.

    Input:
    - repo: repository metadata.
    - file_record: file metadata.
    - path: absolute file path.

    Output:
    - list of SymbolRecord.

    TODO:
    - Extract classes.
    - Extract functions.
    - Extract methods with parent class.
    - Extract decorators.
    - Extract imports separately for graph edges.
    """

    source = path.read_text(encoding="utf-8", errors="replace")
    tree = ast.parse(source)
    records: list[SymbolRecord] = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            kind = "class" if isinstance(node, ast.ClassDef) else "function"
            records.append(
                SymbolRecord(
                    symbol_id=stable_id("symbol", repo.repo_id, file_record.path, node.name),
                    repo_id=repo.repo_id,
                    file_id=file_record.file_id,
                    name=node.name,
                    kind=kind,
                    language="python",
                    start_line=getattr(node, "lineno", None),
                    end_line=getattr(node, "end_lineno", None),
                    signature=None,
                    docstring=ast.get_docstring(node),
                )
            )
    return records


def parse_python_imports(path: Path) -> list[str]:
    """Extract imported module names.

    TODO:
    - Return structured import records, not strings.
    - Preserve line numbers.
    """

    _ = path
    return []

