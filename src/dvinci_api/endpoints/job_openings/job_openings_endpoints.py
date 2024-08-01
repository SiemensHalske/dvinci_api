"""
File: src/dvinci_api/endpoints/job_openings/job_openings_endpoints.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Endpoints for the job openings section of the d.vinci API.

Classes:
--------
- JobOpeningsEndpoints: Class to encapsulate job openings endpoints.

Methods:
--------
- get_job_openings: Get a list of job openings.
- post_job_opening: Create a new job opening.
- get_job_opening_by_external_id: Get a job opening with the given externalId.
- get_job_opening_by_id: Get a specific job opening.
- put_job_opening: Update a job opening.
- get_job_opening_history: Get all history entries for the given job opening id.
- put_job_opening_history: Add or update a list of history entries for a given job opening.
- put_job_opening_history_by_external_id: Add a new or update an existing history entry for the given job opening.
"""

from ...client import DvinciClient


class JobOpeningsEndpoints:
    """
    Class to encapsulate job openings endpoints.

    Attributes:
    -----------
    client : DvinciClient
        An instance of the DvinciClient class to make requests to the API.
    """

    def __init__(self, client: DvinciClient):
        """
        Initialize the JobOpeningsEndpoints with a DvinciClient instance.

        :param client: An instance of DvinciClient.
        """
        self.client = client

    def get_job_openings(self, **params):
        """
        Get a list of job openings.

        :param params: Query parameters for filtering job openings.
        :return: List of job openings.
        """
        return self.client.request("GET", "jobOpenings", params=params)

    def post_job_opening(self, job_opening_data: dict):
        """
        Create a new job opening.

        :param job_opening_data: Dictionary containing job opening details.
        :return: Created job opening data.
        """
        return self.client.request("POST", "jobOpenings", json=job_opening_data)

    def get_job_opening_by_external_id(self, external_id: str):
        """
        Get a job opening with the given externalId.

        :param external_id: External ID of the job opening.
        :return: Job opening data.
        """
        return self.client.request("GET", "jobOpenings", params={"externalId": external_id})

    def get_job_opening_by_id(self, job_opening_id: int):
        """
        Get a specific job opening.

        :param job_opening_id: ID of the job opening.
        :return: Job opening data.
        """
        return self.client.request("GET", f"jobOpenings/{job_opening_id}")

    def put_job_opening(self, job_opening_id: int, job_opening_data: dict):
        """
        Update a job opening.

        :param job_opening_id: ID of the job opening.
        :param job_opening_data: Dictionary containing updated job opening details.
        :return: Updated job opening data.
        """
        return self.client.request("PUT", f"jobOpenings/{job_opening_id}", json=job_opening_data)

    def get_job_opening_history(self, job_opening_id: int):
        """
        Get all history entries for the given job opening id.

        :param job_opening_id: ID of the job opening.
        :return: List of history entries.
        """
        return self.client.request("GET", f"jobOpenings/{job_opening_id}/history")

    def put_job_opening_history(self, job_opening_id: int, history_data: dict):
        """
        Add or update a list of history entries for a given job opening.

        :param job_opening_id: ID of the job opening.
        :param history_data: Dictionary containing history details.
        :return: Updated history data.
        """
        return self.client.request("PUT", f"jobOpenings/{job_opening_id}/history", json=history_data)

    def put_job_opening_history_by_external_id(self, job_opening_id: int, external_id: str, history_data: dict):
        """
        Add a new or update an existing history entry for the given job opening.

        :param job_opening_id: ID of the job opening.
        :param external_id: External ID of the history entry.
        :param history_data: Dictionary containing history details.
        :return: Updated history entry data.
        """
        return self.client.request("PUT", f"jobOpenings/{job_opening_id}/history/{external_id}", json=history_data)
