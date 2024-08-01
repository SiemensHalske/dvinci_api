"""
File: src/dvinci_api/endpoints/job_publication_channels/job_publication_channels_endpoints.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Endpoints for the job publication channels section of the d.vinci API.

Classes:
--------
- JobPublicationChannelsEndpoints: Class to encapsulate job publication channels endpoints.

Methods:
--------
- get_job_publication_channel: Get a specific job publication channel.
- put_job_publication_channel: Update a job publication channel.
"""

from ...client import DvinciClient


class JobPublicationChannelsEndpoints:
    """
    Class to encapsulate job publication channels endpoints.

    Attributes:
    -----------
    client : DvinciClient
        An instance of the DvinciClient class to make requests to the API.
    """

    def __init__(self, client: DvinciClient):
        """
        Initialize the JobPublicationChannelsEndpoints with a DvinciClient instance.

        :param client: An instance of DvinciClient.
        """
        self.client = client

    def get_job_publication_channel(self, channel_id: int):
        """
        Get a specific job publication channel.

        :param channel_id: ID of the job publication channel.
        :return: Job publication channel data.
        """
        return self.client.request("GET", f"jobPublicationChannels/{channel_id}")

    def put_job_publication_channel(self, channel_id: int, channel_data: dict):
        """
        Update a job publication channel.

        :param channel_id: ID of the job publication channel.
        :param channel_data: Dictionary containing updated channel details.
        :return: Updated job publication channel data.
        """
        return self.client.request("PUT", f"jobPublicationChannels/{channel_id}", json=channel_data)
