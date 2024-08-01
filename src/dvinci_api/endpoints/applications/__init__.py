"""
File: src/dvinci_api/endpoints/applications/__init__.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Initialization file for the applications endpoints of the d.vinci API.

Imports:
--------
- get_applications: Function to get a list of permitted applications.
- post_application: Function to create a new application.
- get_application_by_external_id: Function to get an application with the given externalId.
- get_application_by_id: Function to get a specific application.
- delete_application: Function to delete a specific application.
- change_application_status: Function to change status for a specific application.
- move_application_job_opening: Function to change the associated job opening of
    a specific application.
"""

from .applications_endpoints import (
    get_applications,
    post_application,
    get_application_by_external_id,
    get_application_by_id,
    delete_application,
    change_application_status,
    move_application_job_opening
)

__all__ = [
    "get_applications",
    "post_application",
    "get_application_by_external_id",
    "get_application_by_id",
    "delete_application",
    "change_application_status",
    "move_application_job_opening"
]
