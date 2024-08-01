"""
File: src/dvinci_api/endpoints/dvinci_users/users_endpoints.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Endpoints for the d.vinci users section of the d.vinci API.

Classes:
--------
- DvinciUsersEndpoints: Class to encapsulate d.vinci users endpoints.

Methods:
--------
- get_users: Get a list of users.
- post_user: Add a new d.vinci user.
- get_user_by_id: Get a specific d.vinci user.
- put_user: Update a d.vinci user.
- delete_user: Delete a d.vinci user.
"""

from ...client import DvinciClient


class DvinciUsersEndpoints:
    """
    Class to encapsulate d.vinci users endpoints.

    Attributes:
    -----------
    client : DvinciClient
        An instance of the DvinciClient class to make requests to the API.
    """

    def __init__(self, client: DvinciClient):
        """
        Initialize the DvinciUsersEndpoints with a DvinciClient instance.

        :param client: An instance of DvinciClient.
        """
        self.client = client

    def get_users(self):
        """
        Get a list of users.

        :return: List of users.
        """
        return self.client.request("GET", "dvinciUsers")

    def post_user(self, user_data: dict):
        """
        Add a new d.vinci user.

        :param user_data: Dictionary containing user details.
        :return: Created user data.
        """
        return self.client.request("POST", "dvinciUsers", json=user_data)

    def get_user_by_id(self, user_id: int):
        """
        Get a specific d.vinci user.

        :param user_id: ID of the user.
        :return: User data.
        """
        return self.client.request("GET", f"dvinciUsers/{user_id}")

    def put_user(self, user_id: int, user_data: dict):
        """
        Update a d.vinci user.

        :param user_id: ID of the user.
        :param user_data: Dictionary containing updated user details.
        :return: Updated user data.
        """
        return self.client.request("PUT", f"dvinciUsers/{user_id}", json=user_data)

    def delete_user(self, user_id: int):
        """
        Delete a d.vinci user.

        :param user_id: ID of the user.
        :return: Response data.
        """
        return self.client.request("POST", f"dvinciUsers/{user_id}/delete")
