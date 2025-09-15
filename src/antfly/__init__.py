"""
Antfly SDK - Python client for Antfly distributed key-value store and search engine.
"""

from .client import AntflyClient
from .exceptions import AntflyAuthError, AntflyConnectionError, AntflyException

__version__ = "0.1.0"

__all__ = [
    "AntflyClient",
    "AntflyException",
    "AntflyConnectionError",
    "AntflyAuthError",
    "__version__",
]
