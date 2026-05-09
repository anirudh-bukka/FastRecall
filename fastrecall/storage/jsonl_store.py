"""Simple JSONL storage helpers.

TODO imports:
- dataclasses.asdict for dataclass serialization.
- json.
- pathlib.Path.
"""

from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any


def append_jsonl(path: Path, record: Any) -> None:
    """Append one record to a JSONL file.

    Input:
    - path: target JSONL path.
    - record: dataclass or dict.

    TODO:
    - Add atomic write strategy if needed.
    - Add schema/version field.
    """

    path.parent.mkdir(parents=True, exist_ok=True)
    payload = asdict(record) if is_dataclass(record) else record
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    """Read JSONL records from disk.

    TODO:
    - Stream large files instead of returning a list.
    - Handle corrupt lines with useful diagnostics.
    """

    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows

