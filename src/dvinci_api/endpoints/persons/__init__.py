"""
File: src/dvinci_api/endpoints/persons/__init__.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Initialization file for the persons endpoints of the d.vinci API.

Imports:
--------
- PersonsEndpoints: Class to encapsulate persons endpoints.
"""

from .persons_endpoints import PersonsEndpoints

__all__ = ["PersonsEndpoints"]
