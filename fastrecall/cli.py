"""CLI entrypoints for FastRecall.

TODO imports:
- argparse for a zero-dependency CLI.
- pathlib.Path for command paths.
- fastrecall.config.load_config.
- ingestion functions from fastrecall.ingestion.
- retrieval functions from fastrecall.retrieval.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from fastrecall.config import load_config


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser.

    TODO:
    - Add `init`.
    - Add `ingest-docs PATH`.
    - Add `ingest-repo PATH --name NAME`.
    - Add `query TEXT [--repo NAME] [--repos A B]`.
    - Add `explain-symbol SYMBOL --repo NAME`.
    - Add `find-similar TEXT --repos A B`.
    """

    parser = argparse.ArgumentParser(prog="fastrecall")
    subcommands = parser.add_subparsers(dest="command")

    subcommands.add_parser("init", help="Initialize local FastRecall storage.")

    ingest_docs = subcommands.add_parser("ingest-docs", help="Index documents.")
    ingest_docs.add_argument("path", type=Path)

    ingest_repo = subcommands.add_parser("ingest-repo", help="Index a code repository.")
    ingest_repo.add_argument("path", type=Path)
    ingest_repo.add_argument("--name", required=True)

    query = subcommands.add_parser("query", help="Query indexed content.")
    query.add_argument("text")
    query.add_argument("--repo")
    query.add_argument("--repos", nargs="*")

    explain = subcommands.add_parser("explain-symbol", help="Explain a code symbol.")
    explain.add_argument("symbol")
    explain.add_argument("--repo", required=True)

    similar = subcommands.add_parser("find-similar", help="Find similar code or concepts.")
    similar.add_argument("text")
    similar.add_argument("--repos", nargs="*")

    return parser


def main(argv: list[str] | None = None) -> int:
    """Main CLI dispatcher.

    Input:
    - argv: optional arguments for tests.

    Output:
    - process exit code.

    TODO:
    - Replace placeholder print statements with calls into ingestion/retrieval.
    - Keep this file thin; real work belongs in package modules.
    """

    parser = build_parser()
    args = parser.parse_args(argv)
    config = load_config()

    if args.command is None:
        parser.print_help()
        return 2

    # TODO: dispatch to actual command handlers.
    print(f"FastRecall command placeholder: {args.command}")
    print(f"Workspace: {config.workspace_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

