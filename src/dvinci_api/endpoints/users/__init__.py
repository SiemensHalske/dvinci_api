"""
File: src/dvinci_api/endpoints/dvinci_users/__init__.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Initialization file for the d.vinci users endpoints of the d.vinci API.

Imports:
--------
- DvinciUsersEndpoints: Class to encapsulate d.vinci users endpoints.
"""

from .users_endpoints import DvinciUsersEndpoints

__all__ = ["DvinciUsersEndpoints"]
