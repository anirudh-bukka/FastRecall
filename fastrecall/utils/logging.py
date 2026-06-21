"""Logging configuration for FastRecall."""

import logging


def configure_logging(verbose: bool = False) -> None:
    """Set up structured logging for the server and CLI.

    In verbose mode (--verbose flag or DEBUG env) every SQL query, embedding
    call, and similarity score is logged.  In normal mode only hits, misses,
    and errors are logged.
    """

    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )


def get_logger(name: str) -> logging.Logger:
    """Return a module-level logger.

    Usage inside any module:
        from fastrecall.utils.logging import get_logger
        logger = get_logger(__name__)
    """

    return logging.getLogger(name)
