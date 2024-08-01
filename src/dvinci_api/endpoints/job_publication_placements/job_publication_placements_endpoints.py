"""
File: src/dvinci_api/endpoints/job_publication_placements/job_publication_placements_endpoints.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Endpoints for the job publication placements section of the d.vinci API.

Classes:
--------
- JobPublicationPlacementsEndpoints: Class to encapsulate job publication placements endpoints.

Methods:
--------
- get_placements: Get a list of job publication placements for a given partner.
- post_placement: Create a new job publication placement for a given partner.
- get_placement_by_external_id: Get a job publication placement for the partner with the given externalId.
- get_placements_by_job_publication_id: Get all job publication placements for the job publication and given partner.
- get_placement_by_id: Get a specific job publication placement for the partner.
- put_placement: Update a job publication placement for the partner.
- delete_placement: Delete a specific job publication placement for the partner.
"""

from ...client import DvinciClient


class JobPublicationPlacementsEndpoints:
    """
    Class to encapsulate job publication placements endpoints.

    Attributes:
    -----------
    client : DvinciClient
        An instance of the DvinciClient class to make requests to the API.
    """

    def __init__(self, client: DvinciClient):
        """
        Initialize the JobPublicationPlacementsEndpoints with a DvinciClient instance.

        :param client: An instance of DvinciClient.
        """
        self.client = client

    def get_placements(self, partner_id: str, **params):
        """
        Get a list of job publication placements for a given partner.

        :param partner_id: ID of the partner.
        :param params: Query parameters for filtering placements.
        :return: List of job publication placements.
        """
        return self.client.request("GET", f"jobPublicationPlacements/{partner_id}/placements", params=params)

    def post_placement(self, partner_id: str, placement_data: dict):
        """
        Create a new job publication placement for a given partner.

        :param partner_id: ID of the partner.
        :param placement_data: Dictionary containing placement details.
        :return: Created job publication placement data.
        """
        return self.client.request("POST", f"jobPublicationPlacements/{partner_id}/placements", json=placement_data)

    def get_placement_by_external_id(self, partner_id: str, external_id: str):
        """
        Get a job publication placement for the partner with the given externalId.

        :param partner_id: ID of the partner.
        :param external_id: External ID of the job publication placement.
        :return: Job publication placement data.
        """
        return self.client.request("GET", f"jobPublicationPlacements/{partner_id}/placements", params={"externalId": external_id})

    def get_placements_by_job_publication_id(self, partner_id: str, job_publication_id: str):
        """
        Get all job publication placements for the job publication and given partner.

        :param partner_id: ID of the partner.
        :param job_publication_id: ID of the job publication.
        :return: List of job publication placements.
        """
        return self.client.request("GET", f"jobPublicationPlacements/{partner_id}/placements", params={"jobPublicationId": job_publication_id})

    def get_placement_by_id(self, partner_id: str, placement_id: int):
        """
        Get a specific job publication placement for the partner.

        :param partner_id: ID of the partner.
        :param placement_id: ID of the job publication placement.
        :return: Job publication placement data.
        """
        return self.client.request("GET", f"jobPublicationPlacements/{partner_id}/placements/{placement_id}")

    def put_placement(self, partner_id: str, placement_id: int, placement_data: dict):
        """
        Update a job publication placement for the partner.

        :param partner_id: ID of the partner.
        :param placement_id: ID of the job publication placement.
        :param placement_data: Dictionary containing updated placement details.
        :return: Updated job publication placement data.
        """
        return self.client.request("PUT", f"jobPublicationPlacements/{partner_id}/placements/{placement_id}", json=placement_data)

    def delete_placement(self, partner_id: str, placement_id: int):
        """
        Delete a specific job publication placement for the partner.

        :param partner_id: ID of the partner.
        :param placement_id: ID of the job publication placement.
        :return: Response data.
        """
        return self.client.request("POST", f"jobPublicationPlacements/{partner_id}/placements/{placement_id}/delete")
