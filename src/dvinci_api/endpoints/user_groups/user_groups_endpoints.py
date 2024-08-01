"""
File: src/dvinci_api/endpoints/user_groups/user_groups_endpoints.py

Author: Hendrik Siemens
Date: 2024-07-30
Last modified: 2024-07-30
License: MIT

Description:
------------
Endpoints for the user groups section of the d.vinci API.

Classes:
--------
- UserGroupsEndpoints: Class to encapsulate user groups endpoints.

Methods:
--------
- get_user_groups: Get a list of user groups.
- post_user_group: Add a new user group.
- get_user_group_by_id: Get a specific user group.
- put_user_group: Update a user group.
- delete_user_group: Delete a user group.
"""

from ...client import DvinciClient


class UserGroupsEndpoints:
    """
    Class to encapsulate user groups endpoints.

    Attributes:
    -----------
    client : DvinciClient
        An instance of the DvinciClient class to make requests to the API.
    """

    def __init__(self, client: DvinciClient):
        """
        Initialize the UserGroupsEndpoints with a DvinciClient instance.

        :param client: An instance of DvinciClient.
        """
        self.client = client

    def get_user_groups(self):
        """
        Get a list of user groups.

        :return: List of user groups.
        """
        return self.client.request("GET", "userGroups")

    def post_user_group(self, user_group_data: dict):
        """
        Add a new user group.

        :param user_group_data: Dictionary containing user group details.
        :return: Created user group data.
        """
        return self.client.request("POST", "userGroups", json=user_group_data)

    def get_user_group_by_id(self, user_group_id: int):
        """
        Get a specific user group.

        :param user_group_id: ID of the user group.
        :return: User group data.
        """
        return self.client.request("GET", f"userGroups/{user_group_id}")

    def put_user_group(self, user_group_id: int, user_group_data: dict):
        """
        Update a user group.

        :param user_group_id: ID of the user group.
        :param user_group_data: Dictionary containing updated user group details.
        :return: Updated user group data.
        """
        return self.client.request("PUT", f"userGroups/{user_group_id}", json=user_group_data)

    def delete_user_group(self, user_group_id: int):
        """
        Delete a user group.

        :param user_group_id: ID of the user group.
        :return: Response data.
        """
        return self.client.request("POST", f"userGroups/{user_group_id}/delete")
