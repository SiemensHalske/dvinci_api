"""
File: src/dvinci_api/endpoints/org_units/__init__.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Initialization file for the organisation units endpoints of the d.vinci API.

Imports:
--------
- OrgUnitsEndpoints: Class to encapsulate organisation units endpoints.
"""

from .org_units_endpoints import OrgUnitsEndpoints

__all__ = ["OrgUnitsEndpoints"]
