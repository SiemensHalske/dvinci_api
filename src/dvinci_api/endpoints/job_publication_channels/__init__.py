"""
File: src/dvinci_api/endpoints/job_publication_channels/__init__.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Initialization file for the job publication channels endpoints of the d.vinci API.

Imports:
--------
- JobPublicationChannelsEndpoints: Class to encapsulate job publication channels endpoints.
"""

from .job_publication_channels_endpoints import JobPublicationChannelsEndpoints

__all__ = ["JobPublicationChannelsEndpoints"]
