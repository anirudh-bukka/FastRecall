"""Registration helpers for repositories and documents.

TODO imports:
- hashlib or uuid for stable IDs.
- datetime for timestamps.
- fastrecall.models.RepositoryRecord and DocumentRecord.
"""

from pathlib import Path

from fastrecall.models import DocumentRecord, RepositoryRecord
from fastrecall.utils.hashing import stable_id


def register_repository(path: Path, name: str) -> RepositoryRecord:
    """Create a RepositoryRecord.

    Input:
    - path: local repository root.
    - name: user-visible repository name, e.g. repo_a.

    Output:
    - RepositoryRecord.

    TODO:
    - Validate that name is unique.
    - Detect language hints.
    - Store creation timestamp.
    """

    return RepositoryRecord(
        repo_id=stable_id("repo", name, str(path.resolve())),
        name=name,
        root_path=str(path),
    )


def register_document(path: Path) -> DocumentRecord:
    """Create a DocumentRecord for one document.

    TODO:
    - Derive title from metadata or first heading.
    - Store document type.
    - Store creation timestamp.
    """

    return DocumentRecord(
        document_id=stable_id("document", str(path.resolve())),
        source_path=str(path),
        title=path.stem,
        document_type=path.suffix.lower().lstrip(".") or None,
    )

