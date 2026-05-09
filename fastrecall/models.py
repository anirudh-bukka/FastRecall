"""Shared data models for FastRecall.

These models are intentionally plain dataclasses. They should be easy to
serialize to JSONL or SQLite rows.
"""

from dataclasses import dataclass, field
from typing import Any, Literal


@dataclass(slots=True)
class RepositoryRecord:
    """One indexed code repository."""

    repo_id: str
    name: str
    root_path: str
    language_hints: list[str] = field(default_factory=list)
    created_at: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class DocumentRecord:
    """One indexed document."""

    document_id: str
    source_path: str
    title: str | None = None
    document_type: str | None = None
    created_at: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class FileRecord:
    """One source file inside a repository."""

    file_id: str
    repo_id: str
    path: str
    language: str | None = None
    size_bytes: int = 0
    content_hash: str | None = None
    is_test: bool = False
    is_generated: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class SymbolRecord:
    """One code symbol: class, function, method, package, keyword, etc."""

    symbol_id: str
    repo_id: str
    file_id: str
    name: str
    kind: str
    language: str
    start_line: int | None = None
    end_line: int | None = None
    parent_symbol_id: str | None = None
    signature: str | None = None
    docstring: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ChunkRecord:
    """A text span used for lexical search, summaries, or optional embeddings."""

    chunk_id: str
    source_type: Literal["document", "code", "summary"]
    source_id: str
    text: str
    repo_id: str | None = None
    document_id: str | None = None
    start_line: int | None = None
    end_line: int | None = None
    page_number: int | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class PageNode:
    """A document page, section, heading, paragraph, table, or summary node."""

    node_id: str
    document_id: str
    kind: str
    title: str | None = None
    page_number: int | None = None
    parent_id: str | None = None
    previous_id: str | None = None
    next_id: str | None = None
    text: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class CodeNode:
    """A repository/folder/file/symbol node in the code hierarchy."""

    node_id: str
    repo_id: str
    kind: str
    name: str
    file_id: str | None = None
    symbol_id: str | None = None
    parent_id: str | None = None
    summary: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class EdgeRecord:
    """A relationship between two records/nodes."""

    edge_id: str
    repo_id: str
    from_id: str
    to_id: str
    edge_type: str
    confidence: float = 1.0
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class RetrievalResult:
    """One retrieval candidate returned by a retriever."""

    result_id: str
    source_type: str
    source_id: str
    score: float
    retriever: str
    title: str | None = None
    snippet: str | None = None
    repo_id: str | None = None
    document_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

