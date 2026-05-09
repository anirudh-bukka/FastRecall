"""Document ingestion orchestration.

TODO imports:
- fastrecall.ingestion.discovery.iter_files.
- fastrecall.ingestion.registry.register_document.
- fastrecall.document_index.parser.
- fastrecall.document_index.page_index.
- fastrecall.storage stores.
"""

from pathlib import Path

from fastrecall.ingestion.discovery import iter_files
from fastrecall.ingestion.registry import register_document
from fastrecall.models import DocumentRecord


def ingest_documents(path: Path) -> list[DocumentRecord]:
    """Ingest documents from a file or directory.

    Input:
    - path: document file or folder.

    Output:
    - list of DocumentRecord objects created.

    TODO:
    - Filter only supported document files.
    - Parse each document into PageNode/ChunkRecord.
    - Persist records and indexes through storage.
    """

    records: list[DocumentRecord] = []
    for file_path in iter_files(path):
        records.append(register_document(file_path))
    return records

