"""
File: src/dvinci_api/endpoints/configuration/__init__.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Initialization file for the configuration endpoints of the d.vinci API.

Imports:
--------
- get_external_links: Function to get a list of external links of the given type.
- put_external_links: Function to add or update a list of external links of the given type.
"""

from .configuration_endpoints import (
    get_external_links,
    put_external_links
)

__all__ = [
    "get_external_links",
    "put_external_links"
]
