"""Programmatic server entry point.

For production deployments you can run FastRecall directly with uvicorn:

    uvicorn fastrecall.main:app --host 0.0.0.0 --port 8080

This module exposes the `app` object that uvicorn expects.  Configuration is
read from environment variables (see config.from_env()).

For the CLI-driven workflow (development, local testing), use:

    fastrecall serve --port 8080

TODO:
- from .config import from_env
- from .server.app import create_app
- config = from_env()
- app = create_app(config)
"""

app = None  # placeholder until create_app is implemented
