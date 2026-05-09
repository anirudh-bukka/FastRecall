"""Configuration placeholders for FastRecall.

TODO imports:
- pathlib.Path for workspace paths.
- dataclasses.dataclass for simple config records.
- json or tomllib if config files are added.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class FastRecallConfig:
    """Runtime configuration for local-first FastRecall.

    Expected fields:
    - workspace_dir: where FastRecall stores metadata and indexes.
    - storage_dir: where JSONL/SQLite/index files live.
    - embeddings_enabled: whether optional vector retrieval is active.
    - default_repo_scope: optional default repository name.
    """

    workspace_dir: Path
    storage_dir: Path
    embeddings_enabled: bool = False
    default_repo_scope: str | None = None


def default_config(project_root: Path | None = None) -> FastRecallConfig:
    """Return a default local config.

    Input:
    - project_root: optional root directory for `.fastrecall`.

    Output:
    - FastRecallConfig.

    TODO:
    - Decide whether workspace should default to current working directory.
    - Create a config loader that reads a local config file if present.
    """

    root = project_root or Path.cwd()
    workspace = root / ".fastrecall"
    return FastRecallConfig(
        workspace_dir=workspace,
        storage_dir=workspace / "storage",
    )


def load_config(path: Path | None = None) -> FastRecallConfig:
    """Load config from disk or return defaults.

    TODO:
    - Use TOML or JSON for project config.
    - Validate paths.
    - Avoid global mutable config.
    """

    return default_config(path.parent if path else None)

