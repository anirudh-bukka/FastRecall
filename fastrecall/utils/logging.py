"""Logging setup placeholder."""

import logging


def configure_logging(verbose: bool = False) -> None:
    """Configure basic logging for CLI commands."""

    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(levelname)s %(name)s: %(message)s",
    )

