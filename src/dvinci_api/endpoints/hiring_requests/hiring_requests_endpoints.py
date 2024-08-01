"""
File: src/dvinci_api/endpoints/hiring_requests/hiring_requests_endpoints.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Endpoints for the hiring requests section of the d.vinci API.

Classes:
--------
- HiringRequestsEndpoints: Class to encapsulate hiring requests endpoints.

Methods:
--------
- get_hiring_requests: Get a list of hiring requests.
- post_hiring_request: Create a new hiring request.
- get_hiring_request_by_external_id: Get a hiring request with the given externalId.
- get_hiring_request_by_id: Get a specific hiring request.
- put_hiring_request: Update a hiring request.
- get_hiring_request_history: Get all history entries for the given hiring request id.
- get_hiring_request_approvers: Get all approvers for the given hiring request id.
"""

from ...client import DvinciClient


class HiringRequestsEndpoints:
    """
    Class to encapsulate hiring requests endpoints.

    Attributes:
    -----------
    client : DvinciClient
        An instance of the DvinciClient class to make requests to the API.
    """

    def __init__(self, client: DvinciClient):
        """
        Initialize the HiringRequestsEndpoints with a DvinciClient instance.

        :param client: An instance of DvinciClient.
        """
        self.client = client

    def get_hiring_requests(self, **params):
        """
        Get a list of hiring requests.

        :param params: Query parameters for filtering hiring requests.
        :return: List of hiring requests.
        """
        return self.client.request("GET", "hiringRequests", params=params)

    def post_hiring_request(self, request_data: dict):
        """
        Create a new hiring request.

        :param request_data: Dictionary containing hiring request details.
        :return: Created hiring request data.
        """
        return self.client.request("POST", "hiringRequests", json=request_data)

    def get_hiring_request_by_external_id(self, external_id: str):
        """
        Get a hiring request with the given externalId.

        :param external_id: External ID of the hiring request.
        :return: Hiring request data.
        """
        return self.client.request("GET", "hiringRequests", params={"externalId": external_id})

    def get_hiring_request_by_id(self, request_id: int):
        """
        Get a specific hiring request.

        :param request_id: ID of the hiring request.
        :return: Hiring request data.
        """
        return self.client.request("GET", f"hiringRequests/{request_id}")

    def put_hiring_request(self, request_id: int, request_data: dict):
        """
        Update a hiring request.

        :param request_id: ID of the hiring request.
        :param request_data: Dictionary containing updated hiring request details.
        :return: Updated hiring request data.
        """
        return self.client.request("PUT", f"hiringRequests/{request_id}", json=request_data)

    def get_hiring_request_history(self, request_id: int):
        """
        Get all history entries for the given hiring request id.

        :param request_id: ID of the hiring request.
        :return: List of history entries.
        """
        return self.client.request("GET", f"hiringRequests/{request_id}/history")

    def get_hiring_request_approvers(self, request_id: int):
        """
        Get all approvers for the given hiring request id.

        :param request_id: ID of the hiring request.
        :return: List of approvers.
        """
        return self.client.request("GET", f"hiringRequests/{request_id}/approvers")
