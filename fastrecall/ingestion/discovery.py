"""File discovery helpers.

TODO imports:
- pathlib.Path.
- fnmatch for ignore patterns.
- fastrecall.models.FileRecord if discovery creates records directly.
"""

from pathlib import Path


DEFAULT_IGNORE_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    "target",
    "build",
    "dist",
}


def iter_files(root: Path) -> list[Path]:
    """Return files below a root path.

    Input:
    - root: file or directory path.

    Output:
    - list of discovered file paths.

    TODO:
    - Preserve deterministic ordering.
    - Apply ignore directories.
    - Add size limits.
    - Add binary-file detection.
    """

    if root.is_file():
        return [root]
    files: list[Path] = []
    for path in root.rglob("*"):
        if any(part in DEFAULT_IGNORE_DIRS for part in path.parts):
            continue
        if path.is_file():
            files.append(path)
    return sorted(files)


def detect_language(path: Path) -> str | None:
    """Detect a file language from extension/name.

    TODO:
    - Python: `.py`.
    - Java: `.java`.
    - Perl: `.pl`, `.pm`, `.t`.
    - Robot Framework: `.robot`, `.resource`.
    - Markdown/docs: `.md`, `.txt`, `.rst`, `.pdf`.
    """

    suffix = path.suffix.lower()
    mapping = {
        ".py": "python",
        ".java": "java",
        ".pl": "perl",
        ".pm": "perl",
        ".t": "perl",
        ".robot": "robot",
        ".resource": "robot",
        ".md": "markdown",
        ".txt": "text",
        ".rst": "rst",
        ".pdf": "pdf",
    }
    return mapping.get(suffix)


def is_probably_test(path: Path) -> bool:
    """Return whether a file is likely a test file.

    TODO:
    - Support Python, Java, Perl, and Robot naming conventions.
    """

    name = path.name.lower()
    return (
        name.startswith("test_")
        or name.endswith("_test.py")
        or name.endswith("test.java")
        or "/tests/" in path.as_posix().lower()
    )

