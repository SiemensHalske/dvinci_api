"""
File: src/dvinci_api/endpoints/locations/__init__.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Initialization file for the locations endpoints of the d.vinci API.

Imports:
--------
- LocationsEndpoints: Class to encapsulate locations endpoints.
"""

from .locations_endpoints import LocationsEndpoints

__all__ = ["LocationsEndpoints"]
