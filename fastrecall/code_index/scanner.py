"""Repository scanner.

TODO imports:
- pathlib.Path.
- fastrecall.ingestion.discovery.iter_files, detect_language, is_probably_test.
- fastrecall.models.FileRecord, RepositoryRecord.
- fastrecall.utils.hashing.
"""

from pathlib import Path

from fastrecall.ingestion.discovery import detect_language, is_probably_test, iter_files
from fastrecall.models import FileRecord, RepositoryRecord
from fastrecall.utils.hashing import content_hash, stable_id


def scan_repository_files(repo: RepositoryRecord) -> list[FileRecord]:
    """Scan a repository and create FileRecord objects.

    Input:
    - repo: RepositoryRecord.

    Output:
    - list of FileRecord.

    TODO:
    - Add generated-file detection.
    - Add binary skip rules.
    - Store relative paths instead of absolute where useful.
    """

    root = Path(repo.root_path)
    records: list[FileRecord] = []
    for path in iter_files(root):
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        records.append(
            FileRecord(
                file_id=stable_id("file", repo.repo_id, rel),
                repo_id=repo.repo_id,
                path=rel,
                language=detect_language(path),
                size_bytes=path.stat().st_size,
                content_hash=content_hash(text),
                is_test=is_probably_test(path),
            )
        )
    return records

