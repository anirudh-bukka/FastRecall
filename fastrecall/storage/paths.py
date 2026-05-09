"""Workspace path helpers."""

from pathlib import Path

from fastrecall.config import FastRecallConfig


def ensure_workspace(config: FastRecallConfig) -> None:
    """Create local workspace directories.

    TODO:
    - Create subfolders for records, indexes, summaries, and optional vectors.
    - Avoid deleting existing data.
    """

    config.workspace_dir.mkdir(parents=True, exist_ok=True)
    config.storage_dir.mkdir(parents=True, exist_ok=True)


def repo_namespace_dir(config: FastRecallConfig, repo_name: str) -> Path:
    """Return storage directory for one repo namespace."""

    return config.storage_dir / "repos" / repo_name


def documents_dir(config: FastRecallConfig) -> Path:
    """Return storage directory for document indexes."""

    return config.storage_dir / "documents"

