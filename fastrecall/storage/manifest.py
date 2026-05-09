"""Workspace manifest helpers.

The manifest should eventually answer:
- which repositories are indexed?
- which documents are indexed?
- where are their index files?
- when were they last ingested?
"""

from pathlib import Path


def manifest_path(workspace_dir: Path) -> Path:
    """Return the manifest file path."""

    return workspace_dir / "manifest.json"


def load_manifest(workspace_dir: Path) -> dict:
    """Load the manifest.

    TODO:
    - Return a typed manifest model instead of dict.
    - Validate manifest version.
    """

    path = manifest_path(workspace_dir)
    if not path.exists():
        return {"version": 1, "repositories": {}, "documents": {}}
    raise NotImplementedError("Manifest loading not implemented yet.")


def save_manifest(workspace_dir: Path, manifest: dict) -> None:
    """Save the manifest.

    TODO:
    - Write atomically via temp file + rename.
    """

    raise NotImplementedError("Manifest saving not implemented yet.")

