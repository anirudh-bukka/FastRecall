"""FastRecall: semantic LLM response cache.

Public surface area for library mode.  When someone installs the package and
wants to use it programmatically (rather than running the server), they import
from here:

    from fastrecall import SemanticCache, CacheConfig

Server mode is started via the CLI:

    fastrecall serve --port 8080
"""

__version__ = "0.1.0"

from .config import CacheConfig
from .cache.engine import SemanticCache

__all__ = ["CacheConfig", "SemanticCache"]
