"""
File: src/dvinci_api/endpoints/onboardings/__init__.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Initialization file for the onboardings endpoints of the d.vinci API.

Imports:
--------
- OnboardingsEndpoints: Class to encapsulate onboardings endpoints.
"""

from .onboardings_endpoints import OnboardingsEndpoints

__all__ = ["OnboardingsEndpoints"]
