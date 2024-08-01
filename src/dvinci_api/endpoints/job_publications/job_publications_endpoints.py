"""
File: src/dvinci_api/endpoints/job_publications/job_publications_endpoints.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Endpoints for the job publications section of the d.vinci API.

Classes:
--------
- JobPublicationsEndpoints: Class to encapsulate job publications endpoints.

Methods:
--------
- get_job_publications: Get a list of job publications.
- post_job_publication: Create a new job publication.
- get_job_publication_by_external_id: Get a job publication with the given externalId.
- get_job_publication_by_id: Get a specific job publication.
- put_job_publication: Update a job publication.
- delete_job_publication: Delete a specific job publication.
"""

from ...client import DvinciClient


class JobPublicationsEndpoints:
    """
    Class to encapsulate job publications endpoints.

    Attributes:
    -----------
    client : DvinciClient
        An instance of the DvinciClient class to make requests to the API.
    """

    def __init__(self, client: DvinciClient):
        """
        Initialize the JobPublicationsEndpoints with a DvinciClient instance.

        :param client: An instance of DvinciClient.
        """
        self.client = client

    def get_job_publications(self, **params):
        """
        Get a list of job publications.

        :param params: Query parameters for filtering job publications.
        :return: List of job publications.
        """
        return self.client.request("GET", "jobPublications", params=params)

    def post_job_publication(self, publication_data: dict):
        """
        Create a new job publication.

        :param publication_data: Dictionary containing job publication details.
        :return: Created job publication data.
        """
        return self.client.request("POST", "jobPublications", json=publication_data)

    def get_job_publication_by_external_id(self, external_id: str):
        """
        Get a job publication with the given externalId.

        :param external_id: External ID of the job publication.
        :return: Job publication data.
        """
        return self.client.request("GET", "jobPublications", params={"externalId": external_id})

    def get_job_publication_by_id(self, publication_id: int):
        """
        Get a specific job publication.

        :param publication_id: ID of the job publication.
        :return: Job publication data.
        """
        return self.client.request("GET", f"jobPublications/{publication_id}")

    def put_job_publication(self, publication_id: int, publication_data: dict):
        """
        Update a job publication.

        :param publication_id: ID of the job publication.
        :param publication_data: Dictionary containing updated job publication details.
        :return: Updated job publication data.
        """
        return self.client.request("PUT", f"jobPublications/{publication_id}", json=publication_data)

    def delete_job_publication(self, publication_id: int):
        """
        Delete a specific job publication.

        :param publication_id: ID of the job publication.
        :return: Response data.
        """
        return self.client.request("POST", f"jobPublications/{publication_id}/delete")
