"""
File: src/dvinci_api/endpoints/applications/applications_endpoints.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Endpoints for the applications section of the d.vinci API.

Functions:
----------
- get_applications(client: DvinciClient, **params): Get a list of permitted applications.
- post_application(client: DvinciClient, application_data: dict): Create a new application.
- get_application_by_external_id(client: DvinciClient, external_id: str): Get an application
    with the given externalId.
- get_application_by_id(client: DvinciClient, application_id: int): Get a specific application.
- delete_application(client: DvinciClient, application_id: int): Delete a specific application.
- change_application_status(client: DvinciClient, application_id: int, status_id: str): Change
    status for a specific application.
- move_application_job_opening(client: DvinciClient, application_id: int, job_opening_id: int):
    Change the associated job opening of a specific application.
"""

from ...client import DvinciClient


def get_applications(client: DvinciClient, **params):
    """
    Get a list of permitted applications.

    :param client: An instance of DvinciClient.
    :param params: Query parameters for filtering applications.
    :return: List of applications.
    """
    return client.request("GET", "applications", params=params)


def post_application(client: DvinciClient, application_data: dict):
    """
    Create a new application.

    :param client: An instance of DvinciClient.
    :param application_data: Dictionary containing application details.
    :return: Created application data.
    """
    return client.request("POST", "applications", json=application_data)


def get_application_by_external_id(client: DvinciClient, external_id: str):
    """
    Get an application with the given externalId.

    :param client: An instance of DvinciClient.
    :param external_id: External ID of the application.
    :return: Application data.
    """
    return client.request("GET", "applications", params={"externalId": external_id})


def get_application_by_id(client: DvinciClient, application_id: int):
    """
    Get a specific application.

    :param client: An instance of DvinciClient.
    :param application_id: ID of the application.
    :return: Application data.
    """
    return client.request("GET", f"applications/{application_id}")


def delete_application(client: DvinciClient, application_id: int):
    """
    Delete a specific application.

    :param client: An instance of DvinciClient.
    :param application_id: ID of the application to delete.
    :return: Response data.
    """
    return client.request("POST", f"applications/{application_id}/delete")


def change_application_status(client: DvinciClient, application_id: int, status_id: str):
    """
    Change status for a specific application.

    :param client: An instance of DvinciClient.
    :param application_id: ID of the application.
    :param status_id: New status ID.
    :return: Updated application data.
    """
    return client.request("POST", f"applications/{application_id}/statusChange/{status_id}")


def move_application_job_opening(client: DvinciClient, application_id: int, job_opening_id: int):
    """
    Change the associated job opening of a specific application.

    :param client: An instance of DvinciClient.
    :param application_id: ID of the application.
    :param job_opening_id: ID of the new job opening.
    :return: Updated application data.
    """
    return client.request("POST", f"applications/{application_id}/jobOpeningMove/{job_opening_id}")
